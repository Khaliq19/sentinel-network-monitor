import time
import ipaddress

from network import check_router
from database import setup_database, save_check
from reports import generate_report


def main():
    router_ip = input("Enter your router IP address: ").strip()

    try:
        ipaddress.ip_address(router_ip)
    except ValueError:
        print("Invalid IP address. Please enter a valid IPv4 or IPv6 address.")
        return

    connection = setup_database()

    print("\nStarting Sentinel network monitoring...")
    print("Results are being saved to sentinel.db.")
    print("Checking every 5 seconds. Press Ctrl+C to stop.\n")

    previous_status = None

    try:
        while True:
            status, elapsed_ms, timestamp = check_router(router_ip)

            save_check(
                connection,
                timestamp,
                router_ip,
                status,
                elapsed_ms
            )

            if previous_status is not None and status != previous_status:
                if status == "DOWN":
                    print("ALERT: Router connection lost!")
                else:
                    print("RECOVERY: Router connection restored!")

            previous_status = status
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nSentinel monitoring stopped.")
        generate_report(connection, router_ip)

    finally:
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()