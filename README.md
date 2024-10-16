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

python Port_Scanner.py -s 20 -e 40000 -t 500 -V 192.168.1.2

Open Ports Found - [80, 443, 8080]
Time taken - 15.42 seconds
