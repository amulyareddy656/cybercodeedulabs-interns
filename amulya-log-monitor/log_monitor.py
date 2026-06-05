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
		print(f"[{timestamp}] {event_type} | {severity} | IP: {ip} | User: {user}")
except KeyboardInterrupt:
	print("Stop monitoring")
finally:
	file.close()
