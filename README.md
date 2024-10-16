# Python Port Scanner

## Description

This Python script is a multi-threaded port scanner that allows you to scan a range of ports on a target IPv4 address to identify open ports. It uses Python's `socket` library to attempt connections on the specified ports and returns the list of open ports.

The script is highly customizable, allowing you to specify the range of ports, the number of threads to use for scanning, and verbosity for detailed output.

## Features

- **Multi-threaded Scanning**: The script allows for faster port scanning by using multiple threads.
- **Customizable Port Range**: You can specify the starting and ending ports.
- **Verbose Mode**: View open ports in real-time during the scan.
- **Time-efficient**: Displays the total time taken for the scan to complete.
  
## Requirements

- Python 3.x
- `socket` library (included in Python)
- `argparse` library (included in Python)
- `threading` library (included in Python)

## Usage

```bash
python Port_Scanner.py [options] IPv4
```
## Example Usage
python Port_Scanner.py -s 20 -e 40000 -t 500 -V 192.168.1.2

## Arguements:
IPv4	The target IP address to scan.
-s, --start	Starting port number for scanning.	
-e, --end	Ending port number for scanning.	
-t, --threads	Number of threads to use for scanning.	
-V, --verbose	Enable verbose output for real-time status.	
-v, --version	Display the version information.

## How it works
1. Prepare Arguments: The script uses argparse to parse command-line arguments, allowing you to specify the IP address, port range, and other options.
2. Port Generation: A generator function is used to create the range of ports based on the user input.
3. Scanning Ports: The script uses multiple threads to scan ports in parallel. For each port, it tries to establish a connection to the target IP. If the port is open, it is added to the list of open ports.
4. Output: After all ports have been scanned, the list of open ports is printed along with the time taken for the scan.

## Example Output
Open Ports Found - [80, 443, 8080]
Time taken - 15.42 seconds
