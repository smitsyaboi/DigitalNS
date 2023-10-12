import argparse
import ipaddress
import socket
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
"""
# Network Scanner

 This script does a simple network scan and can perform two types of scans:
   1. ICMP (Ping) Scan: Checks if hosts in a given IP network are online by sending ICMP echo requests.
   2. TCP Port Scan: hecks if hosts in a given IP network have a specific TCP port open by attempting connection.

# Usage:
   python network_scanner.py <network> <mode> [--port <port>]

   - <network> specifies the network address to scan, e.g., 192.168.2.0/24.
   - <mode> can be either "icmp" for ICMP scan or "tcp" for TCP scan.
   - [--port <port>] required only for the TCP scan mode, specifying the port to check.

# Example Usages:
   1. Perform an ICMP scan on network 192.168.1.0/24:
      python network_scanner.py 192.168.1.0/24 icmp

   2. Perform a TCP port scan on network 192.168.1.0/24, checking if port 80 is open:
      python network_scanner.py 192.168.1.0/24 tcp --port 80

 ctrl+c can be used to stop the script at any time.

 The script will log the results, and indicate whether hosts are online or offline based on the chosen scan mode. 
 
 Author: Joshua Smith
 Date: 2023-09-25
"""
# Function for ICMP (Ping) Scan
def icmpScan(network):
    liveHosts = set()
    network = ipaddress.ip_network(network, strict=False)
    
    for host in network.hosts():
        host = str(host)
        try:
            # Use subprocess to run the 'ping' command and check if the host is online
            subprocess.check_output(["ping", "-c", "1", host])
            liveHosts.add(host)
            logging.info(f"Host {host} is online.")
        except subprocess.CalledProcessError:
            # If 'ping' fails, log that the host is offline
            logging.info(f"Host {host} is offline.")
            pass
    
    return liveHosts

# Function for TCP Port Scan
def tcpScan(network, port):
    liveHosts = set()
    network = ipaddress.ip_network(network, strict=False)
    
    for host in network.hosts():
        host = str(host)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            # Use a socket to attempt a TCP connection to the specified port
            sock.connect((host, port))
            liveHosts.add(host)
            logging.info(f"Host {host} on port {port} is online.")
        except (socket.timeout, ConnectionRefusedError):
            # If the connection times out or is refused, log that the host is offline
            logging.info(f"Host {host} on port {port} is offline.")
            pass
        finally:
            sock.close()
    
    return liveHosts

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("network", help="Network address to scan, e.g., 192.168.2.0/24")
    parser.add_argument("mode", choices=["icmp", "tcp"], help="Scan mode: ICMP or TCP")
    parser.add_argument("--port", type=int, help="Port to scan (required for TCP mode)")

    args = parser.parse_args()

    if args.mode == "icmp":
        liveHosts = icmpScan(args.network)
    elif args.mode == "tcp":
        if args.port is None:
            logging.error("Port is required for TCP mode.")
            sys.exit(1)
        liveHosts = tcpScan(args.network, args.port)
    
    if liveHosts:
        logging.info("Live hosts:")
        for host in liveHosts:
            print(host)
    else:
        logging.info("No live hosts found.")

if __name__ == "__main__":
    main()
