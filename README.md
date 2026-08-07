Cybersecurity & Network Defense Portfolio
Welcome to my main cybersecurity lab repo. This is where I drop my hands-on projects, security automation scripts, packet captures, and server hardening configs. It covers pretty much everything I work on around security ops, threat detection, and network defense.

🛠️ Portfolio Overview & Lab Modules
1. Python Automation & Security Scripts
The Goal: Automate repetitive security tasks like parsing through raw log files and updating access control lists.

The Files:

log_parser.py – Script that reads through auth logs (server_auth.log) to spot brute-force attempts and flag bad IP addresses.

allow_list_updater.py – Script that automatically updates IP allow lists (allow_list.txt) based on defined security rules.

2. Linux Hardening & Defensive Setup (Fail2ban & SSH)
The Goal: Lock down an Ubuntu server, cut down potential attack vectors, and auto-block bad traffic.

The Files:

configs/ – My hardened SSH config settings (no direct root login, key-based auth only) and custom Fail2ban jail settings.

fail2ban_banned_ips.txt – Live output log showing IPs getting automatically banned after triggering failed login limits.

3. Network Traffic Analysis & Wireshark PCAPs
The Goal: Dig into application traffic, reconstruct TCP streams, and catch unencrypted data moving across the network.

The Findings: Caught cleartext login credentials sent over plain HTTP POST requests and broke down TCP flags (SYN/ACK) during Nmap port scans.

The Files: cleartext_http_capture.pcapng

4. Firewall Rules & Network Segmentation (pfSense)
The Goal: Set up strict network access controls and separate internal traffic across different VLANs.

The Findings: Set up default-deny firewall policies in pfSense to keep guest network traffic completely isolated from trusted internal subnets.

The Files: firewall_rules_lan.png, firewall_block_events.txt

5. SIEM Threat Detection & Log Analysis (Splunk)
The Goal: Pull in logs from multiple sources, write custom search queries, and map detected attacks back to security frameworks.

The Findings: Built custom SPL queries in Splunk to flag login spikes and port scans, mapping alerts directly to MITRE ATT&CK (Brute Force - T1110).

The Files: queries/failed_login_spikes.spl, reports/incident_report_brute_force.md

💻 Tech & Tools I Use
Languages & Scripting: Python, Bash, SPL (Splunk)

Packet & Network Analysis: Wireshark, Nmap, tcpdump

System Defense & Linux Admin: Ubuntu/Debian, SSH, Fail2ban, ss, lsof, systemctl

Networking & Firewalls: pfSense, VLANs, TCP/IP, HTTP/HTTPS Protocol Analysis
