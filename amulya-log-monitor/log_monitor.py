import re
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
file=open(LOG_FILE,"r")
for line in file:
	if "Failed password for root" in line:
		print("ROOT_ATTACK | HIGH")
		ip=extract_ip(line)
		print("IP:",ip)
		user=extract_user(line)
		print("User:",user)
	elif "Failed password for" in line or "Invalid user" in line:
		print("SSH_FAILURE | MEDIUM")
		ip=extract_ip(line)
		print("IP:",ip)
		user=extract_user(line)
		print("User:",user)
	elif "Accepted password" in line or "Accepted publickey" in line:
		print("LOGIN_SUCCESS | LOW")
		ip=extract_ip(line)
		print("IP:",ip)
		user=extract_user(line)
		print("User:",user)
file.close()
