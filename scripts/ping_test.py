import subprocess
import time

def ping(host="8.8.8.8"):
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    with open("ping_results.log", "a") as f:
        f.write(f"\n--- {time.ctime()} ---\n")
        f.write(result.stdout)

if __name__ == "__main__":
    ping()
