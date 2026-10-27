import sqlite3

from database import setup_database, save_check
from reports import generate_report


def test_database_creates_checks_table():
    connection = setup_database()

    try:
        result = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'checks'"
        )

        assert result.fetchone() is not None

    finally:
        connection.close()


def test_save_check_stores_record():
    connection = sqlite3.connect(":memory:")

    try:
        connection.execute("""
            CREATE TABLE checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                router_ip TEXT NOT NULL,
                status TEXT NOT NULL,
                duration_ms REAL NOT NULL
            )
        """)

        save_check(
            connection,
            "2026-10-27 12:00:00",
            "192.168.1.1",
            "UP",
            15.5
        )

        result = connection.execute(
            "SELECT timestamp, router_ip, status, duration_ms FROM checks"
        )

        record = result.fetchone()

        assert record == (
            "2026-10-27 12:00:00",
            "192.168.1.1",
            "UP",
            15.5
        )

    finally:
        connection.close()


def test_report_calculates_uptime(capsys):
    connection = sqlite3.connect(":memory:")

    try:
        connection.execute("""
            CREATE TABLE checks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                router_ip TEXT NOT NULL,
                status TEXT NOT NULL,
                duration_ms REAL NOT NULL
            )
        """)

        save_check(
            connection, "2026-10-27 12:00:00",
            "192.168.1.1", "UP", 10.0
        )

        save_check(
            connection, "2026-10-27 12:00:05",
            "192.168.1.1", "UP", 20.0
        )

        save_check(
            connection, "2026-10-27 12:00:10",
            "192.168.1.1", "DOWN", 2000.0
        )

        generate_report(connection, "192.168.1.1")

        output = capsys.readouterr().out

        assert "Total checks: 3" in output
        assert "Successful checks: 2" in output
        assert "Failed checks: 1" in output
        assert "Observed uptime: 66.67%" in output
        assert "Average check duration: 676.67 ms" in output

    finally:
        connection.close()