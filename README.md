Cybersecurity Labs

 welcome to my lab repo, This is where I put all my hands on network security labs and projects, system hardening setups, and python automation scripts, its basically a environment for the tools and where i show how i analyze traffic, catch threats, and lock down systems.

What's in Here
1. Packet Analysis & Traffic Inspection:
 Inspecting raw traffic, decoding payloads, and tracking down connection problems.

Tools used: Wireshark, Nmap, tcpdump

What I do is Follow the TCP streams, spot unencrypted logins, inspect packet flags like syn or ack and figure out why then netoworks traffic isn't flowing right.

2. Firewalls & Network Setup:
 Setting up firewall rules, dropping bad traffic, and keeping subnets separated.

Tools i used: pfSense, vlans, stateful firewalls

What i do is Build default deny rules and separate guest vlans from the main internal networks, filter inbound & outbound traffic and check firewall logs when activity gets blocked.

3. SIEM & Log Monitoring:
 Pooling logs together, hunting for suspicious activity, and tracking down alerts.

Tools used: Splunk, Syslog, mitre attack

What I do is Write a SPL search , build basic SOC dashboards, catch sudden spikes in failed logins

4. Linux Hardening & System Admin:
 Securing Linux boxes, checking for open ports, and auto blocking brute force attacks.

Tools used: Ubuntu & Debian CLI, SSH, Fail2ban, ss, lsof, systemctl

What I do is turn off SSH root logins, switch to SSH keys, find open  ports with ss or lsof, kill off any unneeded services, and set up Fail2ban to auto block bad IPs.

5. Python Automation & Scripting:
 Writing quick scripts to handle boring tasks and parse logs faster.

Tools used: Python 3, Bash, Regex

What I do: Parse raw auth logs, pull out bad IP addresses, update allow and deny lists automatically, and write clean scripts.

Quick  Overview
Traffic & Scans: Wireshark, Nmap, tcpdump

Defensive Tools: pfSense, VLANs, Fail2ban, OpenSSH

SIEM & Logs: Splunk SPL, Syslog, auth.log, MITRE ATT&CK

Linux & Code: Python 3, Bash, Ubuntu & Debian CLI, ss, lsof, systemctl

Protocols: TCP/IP, HTTP/HTTPS, DNS, SSH, Subnetting
