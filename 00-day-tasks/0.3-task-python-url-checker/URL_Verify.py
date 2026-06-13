import requests
import time

url = input("Enter URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    start = time.time()
    response = requests.get(url, timeout=10)
    elapsed = round(time.time() - start, 2)

    print(f"\n{url}")
    print(f"Status: {response.status_code}")
    print(f"Time: {elapsed} seconds")

    with open("results.txt", "w") as f:
        f.write(f"{url}\nStatus: {response.status_code}\nTime: {elapsed} seconds\n")

    print("\nResults saved to results.txt")

except requests.exceptions.ConnectionError:
    print("Unreachable — could not connect to host")
except requests.exceptions.Timeout:
    print("Unreachable — request timed out")