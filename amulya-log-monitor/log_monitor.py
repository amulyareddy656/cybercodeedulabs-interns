import re
import time
from datetime import datetime
LOG_FILE="/var/log/auth.log"
def extract_ip(line):
	ip_match=re.search(r'(\d+\.\d+\.\d+\.\d+)',line)
	if ip_match:
		return ip_match.group(1)
def extract_user(line):
	patterns=[ r'for (\w+)' ]
	for pattern in patterns:
		match=re.search(pattern,line)
		if match:
			return match.group(1)
ip_failure={}
try:
	file=open(LOG_FILE,"r")
	file.seek(0,2)
	while True:
		line=file.readline()
		if not line:
			time.sleep(0.5)
			continue
		if "Failed password for root" in line:
			event_type="ROOT_ATTACK"
			severity="HIGH"
			ip=extract_ip(line)
			user=extract_user(line)
		elif "Failed password for" in line or "Invalid user" in line:
			event_type="SSH_FAILURE"
			severity="MEDIUM"
			ip=extract_ip(line)
			user=extract_user(line)
		elif "Accepted password" in line or "Accepted publickey" in line:
			event_type="LOGIN_SUCCESS"
			severity="LOW"
			ip=extract_ip(line)
			user=extract_user(line)
		else:
			continue
		timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		if event_type=="SSH_FAILURE":
			key=extract_ip(line)
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
				print(f"[{timestamp}] BRUTE_FORCE | HIGH | IP : {ip} | 5 failures in 60 seconds")
		#print(f"[{timestamp}] {event_type} | {severity} | IP: {ip} | User: {user}")
except KeyboardInterrupt:
	print("Stop monitoring")
finally:
	file.close()
