Sentinel — A Network Reliability Monitor

Overview:

Sentinel is a Python-based network monitoring tool that checks router connectivity, records monitoring results, detects connection status changes, and generates basic network reliability reports.

This project was built to practice Python programming, network diagnostics, SQL database operations, automated testing, and modular software design.

Features:

- Connectivity monitoring: Checks whether a router responds to a ping.

- Status-change detection: Identifies when the router changes between UP and DOWN.

- Persistent storage: Saves monitoring results in an SQLite database.

- Reliability reporting: Calculates successful checks, failed checks, observed uptime percentage, and average check duration.

- Input validation: Validates the router IP address before monitoring.

- Automated testing: Uses pytest to test database operations and reporting calculations.

Technology Stack:

Python

SQLite

pytest

Windows command-line networking tools

IntelliJ IDEA

Project Structure:


sentinel-network-monitor/

├── sentinel.py

├── network.py

├── database.py

├── reports.py

├── test_sentinel.py

├── sentinel.db

└── README.md

Requirements:

Python 3

Windows operating system

pytest for running automated tests

The monitoring application uses Python's built-in libraries for networking commands, timing, date and time handling, and SQLite database operations.

Getting Started

1. Install pytest

Open a terminal in the project directory and run:

python -m pip install pytest

2. Start Sentinel

Run the main program:

python sentinel.py

Enter your router's IP address when prompted.

Sentinel will begin checking connectivity every five seconds and save the results to sentinel.db.

3. Stop monitoring

Press Ctrl+C or select "Stop" in the terminal to stop monitoring and display the reliability report.

4. Run automated tests

Run:

python -m pytest -v

Pytest will execute the project's automated tests and report whether they pass or fail.

Reliability Metrics

Sentinel calculates observed uptime using:

Observed uptime = Successful checks / Total checks × 100

The average check duration is calculated from the recorded durations of the ping commands.

These measurements are estimates based on individual checks. A router that does not respond to ping may still be reachable through other network services, and the measured command duration includes operating-system and process overhead rather than representing pure network latency.

Current Limitations:

Monitoring currently targets one router at a time.

Results depend on the router responding to ping requests.

Monitoring is limited to the period when the application is running.

Reliability statistics are based on recorded checks rather than continuous observation between checks.

Future Improvements:

Add more detailed outage and recovery history.

Separate monitoring sessions and generate date-range reports.

Improve error handling and logging.

Add more automated tests.

Add command-line options for the router IP and monitoring interval.

Set up automated testing with GitHub Actions.

Purpose:

Sentinel is a learning and portfolio project focused on practical Python development, network monitoring, database design, and software testing.
