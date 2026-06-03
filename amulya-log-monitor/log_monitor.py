LOG_FILE="/var/log/auth.log"

file=open(LOG_FILE,"r")

print(file.read())

file.close()
