# log_parser.py
# Analyzes authentication logs for repeated failed login attempts

log_file = "server_auth.log"
failed_attempts = {}

# Read the log file
with open(log_file, "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            parts = line.split()
            ip = parts[-1]

            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("=== Suspicious Login Report ===")

for ip, attempts in failed_attempts.items():
    if attempts >= 3:
        print(f"[ALERT] {ip} - {attempts} failed login attempts")
