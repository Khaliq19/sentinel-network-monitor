import subprocess
import time
from datetime import datetime


def check_router(router_ip):
    """Check whether the router responds to a ping."""

    start_time = time.perf_counter()

    result = subprocess.run(
        ["ping", "-n", "1", "-w", "2000", router_ip],
        capture_output=True,
        text=True
    )

    elapsed_ms = (time.perf_counter() - start_time) * 1000
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if result.returncode == 0:
        status = "UP"
    else:
        status = "DOWN"

    print(f"[{timestamp}] Router: {router_ip} | Status: {status}")
    print(f"Check duration: {elapsed_ms:.2f} ms")

    return status, elapsed_ms, timestamp
