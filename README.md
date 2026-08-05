# Python Allow List Automation

## Project Overview

This project uses Python to automate the process of updating an IP allow list. The script reads a file containing authorized IP addresses, then compares it against a list of unauthorized IPs and removes any matches, and saves the updated allow list back to its file.

This type of automation can help reduce manual work  when managing access to sensitive systems.

---

## Technologies Used

- Python
- File Handling
- Lists
- Loops
- Conditional Statements
- String Manipulation

---

## How It Works

1. Reads the allow list from a text file.
2. Converts the file contents into a Python list.
3. Checks each IP address in the remove list.
4. Removes matching IP addresses from the allow list.
5. Writes the updated allow list back to the original file.

---

## Code

```python
# File containing the current allow list
import_file = "allow_list.txt"

# IP addresses that should be removed
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
```

---

## What I Learned

This project helped me practice working with files in Python, using loops and conditional statements, and automating cybersecurity task. It also shows me how scripting can simplify repetitive administrative work and reduce  manual errors.
