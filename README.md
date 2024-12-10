> System Process Monitoring Application

Objective: This is a Django-based web application to monitor and display all running programs and processes on the current system.

The application includes a backend for fetching process details and a user-friendly frontend for visualization.

> Features:

- Displays system process details, including:
Process ID (PID)
Process Name
CPU Usage
Memory Usage
Start Time
User Running the Process

- Provides a table format for easy readability with the following functionalities:
Search/Filter: Search for specific processes by name or PID.
Sort: Sort processes by columns such as CPU usage or memory usage.
Refresh: Manually refresh the process list using a button.

- Implements RESTful APIs for fetching process details in JSON format.
- Error handling and logging to ensure stability and debugging ease.

> Tech Stack:

Backend: Django
Frontend: Django templates with HTML/CSS/JavaScript
Database: SQLite (default Django database for simplicity)
Library: psutil for fetching system process details

> Access the Application: Open your browser and navigate to http://127.0.0.1:8000
Environment: Platform-independent (works on Windows, Linux, Mac)

> Project Architecture:

- Backend:
views.py: Handles requests, fetches process details using psutil, and returns data in JSON format.
urls.py: Routes for the API and web pages.
models.py: Not used, as no data is persisted.

- Frontend:
home.html: Displays process details in a table with sorting, filtering, and refresh functionalities.

- REST API:
Endpoint: /api/processes/
Method: GET
Response: JSON containing all running processes.

- Utility:
psutil: Fetches system process details such as PID, name, CPU, and memory usage.
