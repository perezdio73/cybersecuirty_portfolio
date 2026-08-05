# File containing the current allow list
import_file = "allow_list.txt"

# IP addresses that should be removed from the allow list
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Read the current allow list
with open(import_file, "r") as file:
    ip_addresses = file.read().split()

# Remove unauthorized IP addresses
for ip in remove_list:
    if ip in ip_addresses:
        ip_addresses.remove(ip)

# Save the updated allow list
with open(import_file, "w") as file:
    file.write("\n".join(ip_addresses))
