import socket
import time
from datetime import datetime


def print_report(target_ip, open_ports, scan_time, checked_at):
    """Display scan results."""

    print("\n========== Port Scan Report ==========")
    print(f"Target IP    : {target_ip}")
    print()

    if open_ports:
        print("Open Ports:")
        for port, service in open_ports:
            print(f"  Port {port:<5} ({service}) : OPEN")
    else:
        print("No common open ports found.")

    print()
    print(f"Scan Time    : {scan_time:.3f} seconds")
    print(f"Checked At   : {checked_at}")
    print("======================================")


def save_report(target_ip, open_ports, scan_time, checked_at):
    """Save results to results.txt"""

    with open("results.txt", "w") as file:
        file.write("Port Scan Report\n")
        file.write("=" * 35 + "\n")
        file.write(f"Target IP    : {target_ip}\n\n")

        if open_ports:
            file.write("Open Ports:\n")
            for port, service in open_ports:
                file.write(f"Port {port:<5} ({service}) : OPEN\n")
        else:
            file.write("No common open ports found.\n")

        file.write(f"\nScan Time    : {scan_time:.3f} seconds\n")
        file.write(f"Checked At   : {checked_at}\n")


# Common ports to scan
COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Alternate",
}


target_ip = input("Enter Target IP Address: ").strip()

checked_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

open_ports = []

try:

    # Validate IP / hostname
    socket.gethostbyname(target_ip)

    start = time.perf_counter()

    for port, service in COMMON_PORTS.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append((port, service))

        sock.close()

    scan_time = time.perf_counter() - start

    print_report(
        target_ip,
        open_ports,
        scan_time,
        checked_at,
    )

    save_report(
        target_ip,
        open_ports,
        scan_time,
        checked_at,
    )

    print("\nResults saved to results.txt")

except socket.gaierror:

    print("\nError: Invalid IP address or hostname.")

except socket.timeout:

    print("\nError: Connection timed out.")

except KeyboardInterrupt:

    print("\nScan cancelled by user.")

except Exception as error:

    print(f"\nUnexpected Error: {error}")