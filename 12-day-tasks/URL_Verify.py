import requests
import time
from datetime import datetime


def print_report(url, status, reason, status_code=None, response_time=None, checked_at=None):
    """Display a formatted report."""

    print("\n========== Website Report ==========")
    print(f"URL          : {url}")
    print(f"Status       : {status}")

    if status_code:
        print(f"Status Code  : {status_code}")

    print(f"Reason       : {reason}")

    if response_time is not None:
        print(f"Response Time: {response_time:.3f} seconds")

    if checked_at:
        print(f"Checked At   : {checked_at}")

    print("====================================")


def save_report(url, status, reason, status_code=None, response_time=None, checked_at=None):
    """Save report to results.txt"""

    with open("results.txt", "w") as file:
        file.write("Website Availability Report\n")
        file.write("=" * 35 + "\n")
        file.write(f"URL          : {url}\n")
        file.write(f"Status       : {status}\n")

        if status_code:
            file.write(f"Status Code  : {status_code}\n")

        file.write(f"Reason       : {reason}\n")

        if response_time is not None:
            file.write(f"Response Time: {response_time:.3f} seconds\n")

        if checked_at:
            file.write(f"Checked At   : {checked_at}\n")


# ---------------- MAIN PROGRAM ---------------- #

url = input("Enter Website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

checked_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

try:
    start = time.perf_counter()

    response = requests.get(url, timeout=10)

    elapsed = time.perf_counter() - start

    status = "Reachable"
    reason = "Website is online."
    status_code = f"{response.status_code} {response.reason}"

    print_report(
        url,
        status,
        reason,
        status_code,
        elapsed,
        checked_at,
    )

    save_report(
        url,
        status,
        reason,
        status_code,
        elapsed,
        checked_at,
    )

    print("\nResults saved to results.txt")

except requests.exceptions.InvalidURL:

    status = "Invalid URL"
    reason = "The URL format is not valid."

    print_report(url, status, reason)
    save_report(url, status, reason)

except requests.exceptions.Timeout:

    status = "Timed Out"
    reason = "The website took too long to respond."

    print_report(url, status, reason)
    save_report(url, status, reason)

except requests.exceptions.SSLError:

    status = "SSL Error"
    reason = "A secure HTTPS connection could not be established."

    print_report(url, status, reason)
    save_report(url, status, reason)

except requests.exceptions.ConnectionError as error:

    message = str(error).lower()

    if (
        "failed to resolve" in message
        or "nameresolutionerror" in message
        or "getaddrinfo failed" in message
        or "name or service not known" in message
        or "temporary failure in name resolution" in message
    ):
        status = "DNS Lookup Failed"
        reason = "The domain name could not be resolved. Check the website address."

    else:
        status = "Connection Error"
        reason = "Unable to connect to the website. Check your internet connection or try again later."

    print_report(url, status, reason)
    save_report(url, status, reason)

except requests.exceptions.RequestException as error:

    status = "Request Failed"
    reason = str(error)

    print_report(url, status, reason)
    save_report(url, status, reason)

except Exception as error:

    status = "Unexpected Error"
    reason = str(error)

    print_report(url, status, reason)
    save_report(url, status, reason)