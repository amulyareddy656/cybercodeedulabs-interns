import re
import time
from datetime import datetime

auth_log="/var/log/auth.log"
sys_log="/var/log/syslog"

#Extracting ip address from auth.log
def extract_ip(line):
	ip_match=re.search(r'(\d+\.\d+\.\d+\.\d+)',line)
	if ip_match:
		return ip_match.group(1)

#Extracting username from auth.log
def extract_user(line):
	patterns=[ r'for (\w+)' ]
	for pattern in patterns:
		match=re.search(pattern,line)
		if match:
			return match.group(1)

def detect_auth_event(line):
	if "Failed password for root" in line:
		event_type="ROOT_ATTACK"
		severity="HIGH"
		ip=extract_ip(line)
		user=extract_user(line)
		record_event(event_type,severity,ip)
		return event_type, severity, ip, user
	elif "Failed password for" in line or "Invalid user" in line:
		event_type="SSH_FAILURE"
		severity="MEDIUM"
		ip=extract_ip(line)
		user=extract_user(line)
		record_event(event_type,severity,ip)
		return event_type, severity, ip, user
	elif "Accepted password" in line or "Accepted publickey" in line:
		event_type="LOGIN_SUCCESS"
		severity="LOW"
		ip=extract_ip(line)
		user=extract_user(line)
		return event_type,severity,ip,user
	return None
#Extracting source ip and destination port from syslog
def detect_ufw(line):
	if "[UFW BLOCK]" in line:
		src_match=re.search(r'SRC=(\d+\.\d+\.\d+\.\d+)',line)
		dpt_match=re.search(r'DPT=(\d+)',line)
		if src_match and dpt_match:
			return src_match.group(1), dpt_match.group(1)
	return None

def detect_sql_injection(line):
	patterns=["UNION" , "SELECT" , "DROP" , "OR 1=1"]
	for pattern in patterns:
		if pattern.lower() in line.lower():
			return True
	return False

#def detect_hhtp_probe(line):
#	patterns=["/admin", "/phpmyadmin", "/test", "/login", "/wp-admin", "/.env"]
#	for pattern in patterns:
#		if pattern.lower() in line.lower():
#			return True
#	return False

#Record the events and finding the highest sever event
def record_event(event_type,severity,ip):
        global highest_severity
        global highest_event
        event_count[event_type]=(event_count.get(event_type,0)+1)
        ip_count[ip]=(ip_count.get(ip,0)+1)
        if severity_rank[severity] > severity_rank[highest_severity]:
                highest_severity=severity
                highest_event=event_type
        if event_type in kill_chain:
                if ip not in ip_data:
                        ip_data[ip] ={"events":[], "stages":set() }
                ip_data[ip]["events"].append(event_type)
                ip_data[ip]["stages"].add(kill_chain[event_type])

#Calculating priority score based on the weights and frequency of the event type
def calculate_score(ip):
	score=0
	events=ip_data[ip]["events"]
	for event in set(events):
		count=events.count(event)
		weight=attack_weights[event]
		if count<=3:
			multiplier=1
		elif count<=9:
			multiplier=1.5
		else:
			multiplier=2
		score=score+(weight*count*multiplier)
	if len(ip_data[ip]["stages"])>=2:
		score+=10
	if score<=10:
		priority="LOW"
		recommendation="Continue monitoring"
	elif score <=25:
		priority="MEDIUM"
		recommendation="Continue monitoring"
	elif score<=50:
		priority="HIGH"
		recommendation="Monitor closely"
	else:
		priority="Critical"
		recommendation="Block the IP immediately"
	return score,priority,recommendation

ip_failure={}
event_count = {}
ip_count = {}
highest_severity = "LOW"
highest_event = "None"
severity_rank = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}
port_scan_dict = {}
ip_data = {}
kill_chain = {
    "PORT_SCAN": "RECONNAISSANCE(1)",
    "SSH_FAILURE": "DELIVERY(3)",
    "BRUTE_FORCE": "DELIVERY(3)",
    "ROOT_ATTACK": "EXPLOITATION(4)",
    "SQL_INJECTION": "EXPLOITATION(4)",
    "LATERAL_MOVEMENT": "LATERAL_MOVEMENT(5)"
}
attack_weights = {
    "PORT_SCAN": 1,
    "SSH_FAILURE": 3,
    "BRUTE_FORCE": 5,
    "ROOT_ATTACK": 8,
    "SQL_INJECTION": 8,
    "LATERAL_MOVEMENT": 10
}

#Detecting the events like ssh failure, root attack, login successful, brute force, port scan and printing the summary for every 60 seconds.
try:
	auth_file=open(auth_log,"r")
	auth_file.seek(0,2)
	sys_file=open(sys_log,"r")
	sys_file.seek(0,2)
	last_report=time.time()
	print("Monitoring started")

	while True:
		auth_line=auth_file.readline()
		sys_line=sys_file.readline()
		if not auth_line and not sys_line:
			time.sleep(0.5)
			continue
		event_type = None
		severity = None
		ip = None
		user = None
		timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		result=detect_auth_event(auth_line)
		if result:
			event_type,severity,ip,user=result
			print(f"[{timestamp}] {event_type} | {severity} | IP : {ip} | User : {user}")

		#Brute force detection logic
		if event_type=="SSH_FAILURE":
			key=extract_ip(auth_line)
			value=datetime.now()
			if key not in ip_failure:
				ip_failure[key]=[]
			ip_failure[key].append(value)
			while ip_failure[key]:
				timestamp_difference=value-ip_failure[key][0]
				if(timestamp_difference.total_seconds()>=60):
					ip_failure[key].pop(0)
				else:
					break
			if len(ip_failure[key])>=5:
				event_type="BRUTE_FORCE"
				severity="HIGH"
				record_event(event_type,severity,ip)
				print(f"[{timestamp}] {event_type} | {severity} | IP : {ip} | 5 failures in 60 seconds")

		#Port scan detection logic
		result=detect_ufw(sys_line)
		if result:
			src_ip,dpt=result
			if src_ip not in port_scan_dict:
				port_scan_dict[src_ip]=set()
			port_scan_dict[src_ip].add(dpt)
			print("PORTS =", port_scan_dict[src_ip])
			if dpt=="22":
				severity="HIGH"
			elif dpt in ["3306" , "5432"]:
				severity="CRITICAL"
			else:
				severity="MEDIUM"
			event_type="UFW_BLOCK"
			print(f"[{timestamp}] {event_type} | {severity} | SRC_IP : {src_ip} | DPT : {dpt}")
			record_event(event_type,severity,src_ip)
			if len(port_scan_dict[src_ip])>=3:
				event_type="PORT_SCAN"
				severity="MEDIUM"
				print(f"[{timestamp}] {event_type} | {severity} | IP : {src_ip}")
				record_event(event_type,severity,src_ip)

		if event_type and  event_type=="LOGIN_SUCCESS":
			if ip in ip_failure and len(ip_failure[ip])>=5:
				event_type="LATERAL_MOVEMENT"
				severity="CRITICAL"
				record_event(event_type,severity,ip)
				print(f"[{timestamp}] {event_type} | {severity} | IP : {ip}")

		if sys_line and detect_sql_injection(sys_line):
			event_type="SQL_INJECTION"
			severity="CRITICAL"
			ip=extract_ip(sys_line)
			record_event(event_type,severity,ip)
			print(f"[{timestamp}] {event_type} | {severity} | IP : {ip}")

#		if sys_line and detect_http_probe(sys_line):
#			event_type="HTTP_PROBE"
#			severity="LOW"
#			ip=extract_ip(sys_line)
#			record_event(event_type,severity,ip)
#			print(f"[{timestamp}] {event_type} | {severity} | IP : {ip}")

		#Printing the summary like total event types, top 3 attackin ips, highest severe event, priority score.
		if time.time()-last_report>=60:
			print("\n=======SUMMARY=======\n")
			print("Total event types")
			for event,count in event_count.items():
				print(f"{event} : {count}")
			print("\nTop 3 attacking IPs")
			temp=ip_count.copy()
			for i in range(min(3,len(temp))):
				max_ip=max(temp,key=temp.get)
				print(max_ip,temp[max_ip])
				del temp[max_ip]
			print("\nHighest severity event")
			print(f"{highest_event} | {highest_severity}")
			print()
			for ip in ip_data:
				score,priority,recommendation=calculate_score(ip)
				print(f"IP : {ip} | Score : {score} | Priority : {priority} | Recommendation : {recommendation}")
			event_count.clear()
			ip_count.clear()
			ip_data.clear()
			ip_failure.clear()
			port_scan_dict.clear()
			highest_severity = "LOW"
			highest_event = "None"
			last_report=time.time()

except Exception as e:
	import traceback
	traceback.print_exc()
	print("Error: ",e)
finally:
	auth_file.close()
	sys_file.close()
