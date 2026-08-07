Network Security & Defense Labs
Hey, welcome to my lab repo. This is where I dump all my hands-on network security stuff, system hardening setups, and python automation scripts. It's basically a sandbox for the tools and workflows I use to analyze traffic, catch threats, and lock down systems.

What's in Here
1. Packet Analysis & Traffic Inspection
Focus: Inspecting raw traffic, decoding payloads, and tracking down connection problems.

Tools: Wireshark, Nmap, tcpdump

What I do: Follow TCP streams, spot unencrypted logins (HTTP/DNS/FTP), inspect packet flags (SYN/ACK), and figure out why traffic isn't flowing right.

2. Firewalls & Network Setup
Focus: Setting up firewall rules, dropping bad traffic, and keeping subnets separated.

Tools: pfSense, VLANs, stateful firewalls

What I do: Build default-deny rules, separate guest VLANs from main internal networks, filter inbound/outbound traffic, and check firewall logs when stuff gets blocked.

3. SIEM & Log Monitoring
Focus: Pooling logs together, hunting for suspicious activity, and tracking down alerts.

Tools: Splunk, Syslog, MITRE ATT&CK

What I do: Write SPL search queries, build basic SOC dashboards, catch sudden spikes in failed logins, and match alerts to MITRE ATT&CK techniques.

4. Linux Hardening & System Admin
Focus: Securing Linux boxes, checking open ports, and auto-blocking brute-force attacks.

Tools: Ubuntu/Debian CLI, SSH, Fail2ban, ss, lsof, systemctl

What I do: Turn off SSH root logins, switch to SSH keys, find open listening ports with ss/lsof, kill off unneeded services, and set up Fail2ban to auto-ban bad IPs.

5. Python Automation & Scripting
Focus: Writing quick scripts to handle boring tasks and parse logs fast.

Tools: Python 3, Bash, Regex

What I do: Parse raw auth logs, pull out bad IP addresses, update allow/deny lists automatically, and write clean script utilities.

Quick Stack Overview
Traffic & Scans: Wireshark, Nmap, tcpdump

Defensive Tools: pfSense, VLANs, Fail2ban, OpenSSH

SIEM & Logs: Splunk (SPL), Syslog, auth.log, MITRE ATT&CK

Linux & Code: Python 3, Bash, Ubuntu/Debian CLI, ss, lsof, systemctl

Protocols: TCP/IP, HTTP/HTTPS, DNS, SSH, Subnetting
