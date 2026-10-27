import sqlite3


def setup_database():
    """Create the database and monitoring table if needed."""

    connection = sqlite3.connect("sentinel.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            router_ip TEXT NOT NULL,
            status TEXT NOT NULL,
            duration_ms REAL NOT NULL
        )
    """)

    connection.commit()
    return connection


def save_check(connection, timestamp, router_ip, status, duration_ms):
    """Save one monitoring result to the database."""

    connection.execute(
        """
        INSERT INTO checks (timestamp, router_ip, status, duration_ms)
        VALUES (?, ?, ?, ?)
        """,
        (timestamp, router_ip, status, duration_ms)
    )

    connection.commit()
