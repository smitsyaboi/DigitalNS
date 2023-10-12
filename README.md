# Log Analysis Program

## Description
This program, the **Log Analysis Program**, is designed to analyze log entries, track the occurrences of different components throughout the day, and categorize them into total counts, counts during working hours (9:00 to 17:00), and counts after working hours. The program processes log entries in a structured manner:

- It extracts timestamps and component information from each log entry.
- Utilizing a dictionary, it maintains a record of the total count of each component throughout the day.
- The program categorizes log entries as either within working hours or after working hours.
- For visualization purposes, it maintains separate dictionaries for counts during working hours and after working hours.

## Usage

To use the Log Analysis Program:

1. Install the required library using pip: pip install matplotlib
2. Ensure the log entries are available and specified in the `log_file_path` variable within the script.
3. Run the script.

## Author
- Joshua Smith
- Date: 2023-09-21

## License
This program is provided under an open-source license. You are welcome to use it as a reference with proper credit.

# Network Scanner

## Description
The **Network Scanner** is a versatile script for conducting network scans. It offers two types of scans:

1. **ICMP (Ping) Scan**: This scan checks if hosts within a specified IP network are online by sending ICMP echo requests.

2. **TCP Port Scan**: In this mode, the script checks if hosts within the provided IP network have a specific TCP port open by attempting a connection.

## Usage

To use the Network Scanner, follow the format: python network_scanner.py <network> <mode> [--port <port>]
- `<network>` specifies the network address to scan (e.g., 192.168.2.0/24).
- `<mode>` can be either "icmp" for an ICMP scan or "tcp" for a TCP port scan.
- `--port <port>` is required only for the TCP scan mode and specifies the port to check.

## Example Usages

1. Perform an ICMP scan on the network 192.168.1.0/24: python network_scanner.py 192.168.1.0/24 icmp
2. Perform a TCP port scan on the network 192.168.1.0/24, checking if port 80 is open: python network_scanner.py 192.168.1.0/24 tcp --port 80

You can stop the script at any time using Ctrl+C. The script logs the results and indicates whether hosts are online or offline based on the chosen scan mode.

## Author
- Joshua Smith
- Date: 2023-09-25

## License
This script is provided under an open-source license. Feel free to use it for reference with proper credit.
