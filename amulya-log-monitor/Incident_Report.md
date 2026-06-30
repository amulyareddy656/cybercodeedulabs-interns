INCIDENT REPORT

Date:26-jun-2026

Time:14:05

Analyst name: Amulya

Attacker IP: 185.220.101.47

Incident status: Closed

CERT reportable: No

Executive summary
------------------

On 26 June 2026, during the scheduled Digital Fort attack simulation, several suspicious activities were detected on my assigned c3 container. The monitoring script I developed continuously analyzed authentication logs, system logs, and web server logs, and identified different attack types such as SSH failures, brute-force attempts, root account attacks, port scanning, firewall blocks, HTTP probes, and process anomalies. All the attacks originated from the IP address 185.220.101.47. Based on the observed activity and the calculated priority score, the incident was classified as Critical. No successful login or system compromise was observed during the simulation, but immediate security measures were recommended.

Incident timeline
------------------

[2026-06-26 14:05:10] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : admin
[2026-06-26 14:05:11] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : deploy
[2026-06-26 14:05:12] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : ubuntu
[2026-06-26 14:05:13] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : test
[2026-06-26 14:05:14] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : git
[2026-06-26 14:05:14] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:24] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:05:25] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:05:27] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:05:37] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser1
[2026-06-26 14:05:37] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:38] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser2
[2026-06-26 14:05:38] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:38] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser3
[2026-06-26 14:05:38] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:39] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser4
[2026-06-26 14:05:39] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:39] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser5
[2026-06-26 14:05:39] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:40] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser6
[2026-06-26 14:05:40] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:40] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser7
[2026-06-26 14:05:40] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:41] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser8
[2026-06-26 14:05:41] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:05:51] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 21
[2026-06-26 14:05:51] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 23
[2026-06-26 14:05:52] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 25
[2026-06-26 14:05:52] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:52] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 3306
[2026-06-26 14:05:52] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:53] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 5432
[2026-06-26 14:05:53] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:53] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 6379
[2026-06-26 14:05:53] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:54] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8080
[2026-06-26 14:05:54] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:54] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8443
[2026-06-26 14:05:54] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:55] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 9200
[2026-06-26 14:05:55] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:05:55] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 27017
[2026-06-26 14:05:55] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:06] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:06:06] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:06] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:06:06] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 139
[2026-06-26 14:06:06] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:06:06] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:06:07] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 1433
[2026-06-26 14:06:07] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:07] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:06:07] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:07] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:06:08] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 5900
[2026-06-26 14:06:08] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:18] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:19] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:19] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:20] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:20] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:21] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:06:31] PROCESS_ANOMALY | HIGH | IP : None
[2026-06-26 14:07:07] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : admin
[2026-06-26 14:07:07] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : deploy
[2026-06-26 14:07:09] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : ubuntu
[2026-06-26 14:07:10] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : test
[2026-06-26 14:07:10] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : git
[2026-06-26 14:07:21] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:07:22] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:07:23] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:07:34] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser1
[2026-06-26 14:07:34] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:34] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser2
[2026-06-26 14:07:34] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser3
[2026-06-26 14:07:35] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser4
[2026-06-26 14:07:35] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser5
[2026-06-26 14:07:35] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:36] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser6
[2026-06-26 14:07:36] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:36] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser7
[2026-06-26 14:07:36] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:37] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser8
[2026-06-26 14:07:37] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:07:48] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 21
[2026-06-26 14:07:48] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 23
[2026-06-26 14:07:48] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 25
[2026-06-26 14:07:48] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:49] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 3306
[2026-06-26 14:07:49] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:49] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 5432
[2026-06-26 14:07:49] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:50] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 6379
[2026-06-26 14:07:50] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:51] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8080
[2026-06-26 14:07:51] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:52] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8443
[2026-06-26 14:07:52] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:52] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 9200
[2026-06-26 14:07:52] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:07:53] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 27017
[2026-06-26 14:07:53] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:03] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:08:03] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:03] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:08:04] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 139
[2026-06-26 14:08:04] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:05] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:08:05] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:05] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:08:06] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 1433
[2026-06-26 14:08:06] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:06] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:08:06] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:06] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:08:07] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 5900
[2026-06-26 14:08:07] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:18] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:18] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:19] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:19] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:20] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:20] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:08:31] PROCESS_ANOMALY | HIGH | IP : None
[2026-06-26 14:09:06] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : admin
[2026-06-26 14:09:07] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : deploy
[2026-06-26 14:09:08] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : ubuntu
[2026-06-26 14:09:09] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : test
[2026-06-26 14:09:09] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : git
[2026-06-26 14:09:09] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:09:20] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:09:21] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:09:22] ROOT_ATTACK | HIGH | IP : 185.220.101.47 | User : root
[2026-06-26 14:09:33] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser1
[2026-06-26 14:09:33] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser2
[2026-06-26 14:09:34] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser3
[2026-06-26 14:09:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser4
[2026-06-26 14:09:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser5
[2026-06-26 14:09:35] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:09:35] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser6
[2026-06-26 14:09:35] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:09:36] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser7
[2026-06-26 14:09:36] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:09:36] SSH_FAILURE | MEDIUM | IP : 185.220.101.47 | User : bruteuser8
[2026-06-26 14:09:36] BRUTE_FORCE | HIGH | IP : 185.220.101.47 | 5 failures in 60 seconds
[2026-06-26 14:09:46] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 21
[2026-06-26 14:09:47] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 23
[2026-06-26 14:09:47] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 25
[2026-06-26 14:09:47] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:48] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 3306
[2026-06-26 14:09:48] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:48] UFW_BLOCK | CRITICAL | SRC_IP : 185.220.101.47 | DPT : 5432
[2026-06-26 14:09:48] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:49] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 6379
[2026-06-26 14:09:49] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:49] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8080
[2026-06-26 14:09:49] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:49] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 8443
[2026-06-26 14:09:49] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:09:50] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 9200
[2026-06-26 14:11:46] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:47] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 27017
[2026-06-26 14:11:47] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:57] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:11:57] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:57] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 135
[2026-06-26 14:11:57] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 139
[2026-06-26 14:11:57] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:58] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:11:58] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:58] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 445
[2026-06-26 14:11:58] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 1433
[2026-06-26 14:11:58] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:59] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:11:59] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:11:59] FIREWALL_BLOCK | LOW | IP : 185.220.101.47 | DPT : 3389
[2026-06-26 14:11:59] UFW_BLOCK | MEDIUM | SRC_IP : 185.220.101.47 | DPT : 5900
[2026-06-26 14:11:59] PORT_SCAN | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:09] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:10] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:10] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:11] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:12] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:12] HTTP_PROBE | MEDIUM | IP : 185.220.101.47
[2026-06-26 14:12:23] PROCESS_ANOMALY | HIGH | IP : None


Attack Details
---------------

1.SSH Failure

Multiple failed SSH authentication attempts were detected from the attacker IP targeting several usernames including admin, deploy, ubuntu, test, git, and bruteuser accounts. These events were identified using the authentication log by matching the "Failed password" pattern. Each failed login attempt was classified as Medium severity because repeated failures indicate credential guessing attempts.
MITRE technique: T1110.001
Killchain phase: Delivery
 
2.Brute Force Attack

After five failed SSH login attempts within sixty seconds, the monitoring tool classified the activity as a Brute Force attack. The attack was assigned High severity because repeated authentication failures significantly increase the probability of unauthorized access if weak credentials exist.
MITRE technique: T1110
Killchain phase: Delivery

3.Root Attack

The attacker repeatedly attempted to authenticate using the root account. Since the root account has unrestricted administrative privileges, these attempts were classified as High severity and represent a significant threat to the server.
MITRE technique: T1078.003
Killchain phase: Exploitation

4.Port Scan

The attacker sequentially scanned multiple ports including:
21,
23,
25,
3306,
5432,
6379,
8080,
8443,
9200,
27017,
135
The monitoring tool detected scans by observing multiple UFW blocked connections from the same IP address to different destination ports. This activity indicates reconnaissance prior to exploitation.
MITRE technique: T1595.001
Killchain phase: Reconnaissance

5.Firewall Block

Firewall blocks were detected on sensitive services including ports 135, 445, and 3389. These ports are commonly associated with Windows RPC, SMB, and Remote Desktop Protocol services. The firewall successfully prevented unauthorized access attempts.
MITRE technique: T1562.004
Killchain phase: Weaponisation

6.HTTP Probe

Several HTTP probing attempts were identified through the web server access logs. These requests indicate that the attacker attempted to discover vulnerable web resources before attempting exploitation. Such reconnaissance activity commonly precedes attacks such as SQL injection or directory traversal.
MITRE technique: T1595.002
Killchain phase:Reconnaissance

7.Process Anomaly

A suspicious process execution event was detected through the system logs involving an EXECVE operation from the /tmp directory. Execution of binaries from temporary directories is commonly associated with malware or unauthorized payload execution and was therefore classified as High severity.
MITRE technique: T1055
Killchain phase: Installation


Technical analysis
-------------------

The attack started with multiple failed SSH login attempts against different user accounts. After several consecutive failures, the monitoring script classified the activity as a brute-force attack because the same IP address generated more than five failed login attempts within sixty seconds. The attacker then tried to access the root account, which indicates an attempt to gain administrative privileges.

After the SSH attacks, the attacker started scanning different network ports, including database ports such as 3306 and 5432, as well as other commonly used service ports. Since the firewall blocked these requests, they were recorded as UFW block events. Once multiple different ports were targeted by the same IP address, the monitoring script classified the activity as a port scan.

Later, HTTP probe events were detected from the web server logs, indicating that the attacker was searching for vulnerable web resources. Towards the end of the simulation, a process anomaly was detected because a suspicious EXECVE operation was executed from the /tmp directory, which may indicate an attempt to execute unauthorized code.

Throughout the simulation, the monitoring script successfully detected, classified, and reported each event in real time while assigning severity levels and generating periodic summaries


Impact assessment
------------------

Such attacks would have posed some serious security threats in case they took place on a production server. The success of any brute-force attacks would mean that the attacker gains SSH access to the server. The root user attacks would mean that the attacker gains full control of the server. Port scanning can enable the attacker to find vulnerable ports, whereas HTTP probing can enable the attacker to carry out web application attacks. The anomaly in the process detected in the simulation can mean that there is an attempt to run a malicious program.


Immediate remediation
-------------------

The following actions would be recommended in case of the attcks like these:
-> Block the attacker's IP address using UFW.
-> Enable Fail2Ban to automatically block repeated SSH login attempts.
-> Disable direct root login through SSH.
-> Restart the SSH service after verifying its configuration.
-> Continue monitoring system logs for suspicious activities.


Lessons learned
----------------

This event has illustrated that log monitoring from different sources is far more beneficial in tracking attacks than log monitoring from a single source. This simulation also taught me about how reconnaissance processes like port scanning happen prior to exploiting attacks. Having a custom-built monitoring tool helped us learn about event classification, severity, and priority in real time. Log monitoring on an ongoing basis can reduce the effects of cyberattacks.


Evidance collected
-------------------

The primary evidence used for this investigation was the live monitoring output (live_output.txt) generated by the custom Python monitoring script. This file contained all detected security events, timestamps, source IP addresses, destination ports, severity levels, and periodic summaries used to reconstruct the incident timeline and analyze the attack sequence.


Conclusion
-----------

This incident response drill offered hands-on experience on how to monitor and analyze various attacks by using real log information. The custom monitoring script was able to detect several attack methods, categorize them based on their level of threat, and produce helpful reports that assisted in understanding the attack sequence. Though no compromise was made during this exercise, the attack techniques that were used stress the need for monitoring, authentication, and timely incident response.
