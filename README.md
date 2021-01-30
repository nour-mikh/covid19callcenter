# Purpose
This is a COVID-19 response guide. It can be used at the call center of a hospital, to guide callers on what to do and collect their information in a sqlite database.

# Logic used
As demanded in the prompt, the project is based on an "if-else" logic that depends on user input. Interface was kept simple using custom HTML Django template (found in layout.html).

# Setting up
Make sure you have Python, Django and Sqlite3 installed on your machine.

# Visiting website
cd into callcenter directory and run command:
- python manage.py runserver
- open browser on http://127.0.0.1:8000/covid19callcenter/

# Consult saved data
- http://127.0.0.1:8000/admin
- login with username and password
- username: admin
- password: 12345

