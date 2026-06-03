LOG_FILE="/var/log/auth.log"
file=open(LOG_FILE,"r")
for line in file:
	if "Failed password for root" in line:
		print("ROOT_ATTACK | HIGH")
		print(line)
	elif "Failed password for" in line or "Invalid user" in line:
		print("SSH_FAILURE | MEDIUM")
		print(line)
	elif "Accepted  password" in line or "Accepted publicly" in line:
		print("LOGIN_SUCCESS | LOW")
		print(line)
file.close()
