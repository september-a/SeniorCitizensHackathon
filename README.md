# SeniorCitizensHackathon
UAH Hackathon 2024

Authors:
David Tollet,
Caleb Boss,
September Abbott,
Ben Morgan,

# Introduction
Need information about UAH for your senior design project, personal use, or a HACKATHON? This is an API with various publically accessible data scraped directly from the UAH website.

# Technologies
Python
- FlaskAPI
- SQLAlchemy
- Selenium
- Beautiful Soup

# Installation
Download, solve dependencies, then run:
> python3 app_db.py

You can now access database from a separate terminal with curl requests
--- OR ---
Use our basic HTML GUI to view the api repsonses!

# Update Database Locally
If your project requires an update to the database, use the update.py script.
Using this script will require an [updated Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) installed on your local machine.

# Endpoints
/courses
/colleges
/majors
/departments
/faculty
/courselistings
