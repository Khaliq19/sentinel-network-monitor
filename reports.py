def generate_report(connection, router_ip):
    """Calculate reliability statistics for a router."""

    result = connection.execute(
        """
        SELECT
            COUNT(*),
            SUM(CASE WHEN status = 'UP' THEN 1 ELSE 0 END),
            SUM(CASE WHEN status = 'DOWN' THEN 1 ELSE 0 END),
            AVG(duration_ms)
        FROM checks
        WHERE router_ip = ?
        """,
        (router_ip,)
    )

    total, successful, failed, average_duration = result.fetchone()

    if total == 0:
        print("\nNo monitoring records found.")
        return

    uptime_percentage = (successful / total) * 100

    print("\n===== SENTINEL RELIABILITY REPORT =====")
    print(f"Router IP: {router_ip}")
    print(f"Total checks: {total}")
    print(f"Successful checks: {successful}")
    print(f"Failed checks: {failed}")
    print(f"Observed uptime: {uptime_percentage:.2f}%")
    print(f"Average check duration: {average_duration:.2f} ms")
    print("=======================================")
