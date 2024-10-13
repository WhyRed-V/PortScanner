# Port Scanner

This Python script performs a basic **port scan** on one or more target IP addresses, checking if specified ports are open. It uses the `socket` library to attempt connections and displays the open ports.

## Features
- **Single or Multiple Targets**: You can scan one or more target IP addresses.
- **Customizable Port Range**: Specify how many ports (starting from 1) to scan.
- **Results**: Only open ports are displayed for each target.

## How It Works
1. The script prompts you to enter the target IP addresses (comma-separated for multiple IPs).
2. Then, it asks for the number of ports you want to scan, starting from port 1.
3. The script scans each target for the specified number of ports and prints the open ports.


## Requirements
- Python 3.x
- `socket` (Standard Library)
- `termcolor` (for colored terminal output)

You can install `termcolor` via pip:


## Usage
1. Clone this repository:
2. 2. Run the script:


