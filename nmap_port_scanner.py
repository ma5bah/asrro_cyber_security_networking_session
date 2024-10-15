# pip install python-nmap
# Usage: python nmap_port_scanner.py

import nmap

from simple_port_scanner import target_ip


# Function to scan open ports and detect OS
def scan_target(target_ip):
    # Initialize the nmap scanner
    nm = nmap.PortScanner()

    print(f"Scanning {target_ip} for open ports and OS detection...")

    # Scan ports and enable OS detection
    nm.scan(target_ip, '1-10000', arguments='-A')

    print(nm.csv())
    # Gather open ports
    open_ports = []
    if 'tcp' in nm[target_ip]:
        for port in nm[target_ip]['tcp']:
            if nm[target_ip]['tcp'][port]['state'] == 'open':
                open_ports.append(port)

    # Output the open ports
    if open_ports:
        print(f"\n[+] Open ports on {target_ip}: {open_ports}")
    else:
        print(f"[-] No open ports found on {target_ip}")


# Main script to input target IP and scan
if __name__ == "__main__":
    # target_ip = input("Enter the target IP address: ").strip()
    target_ip="127.0.0.1"
    try:
        scan_target(target_ip)
    except Exception as e:
        print(f"Error occurred: {e}")

