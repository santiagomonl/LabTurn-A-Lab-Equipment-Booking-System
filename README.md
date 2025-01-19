# LabTurn: A Lab Equipment Booking System
## Introduction
The Lab Equipment Booking System is a Python-based web application designed to streamline the process of reserving laboratory equipment. This system will provide an intuitive interface for users to check equipment availability, book resources, and manage reservations efficiently. Whether you are part of an academic institution, research facility, or a shared lab environment, this program simplifies equipment management, reduces scheduling conflicts, and ensures optimal resource utilization.

## Features
- User-Friendly Interface: Simple navigation and intuitive design for seamless booking.

- Real-Time Availability: View the current status of lab equipment in real-time.

- Flexible Scheduling: Reserve equipment for specific dates and times.

- Booking Management: View, update, or cancel reservations effortlessly.

## Input
The user-friendly interface permits easy booking by clicking on the desired hours to book. Additionally, each piece of equipment will show a different calendar that can be modified to reserve the desired time slots.

## Output
The respective calendar for each piece of equipment will show:
- The hours reserved
- The User's name
- The list of reservation

# Technical Instruction
## If run locally
1. Need to install python on your computer
2. Need to install the following libraries
    ```bash
   pip install Flask Flask-SQLAlchemy os Flask-Migrate
   ```
3. Download the following folders that include HTML files that use Javascript and Jinja2 templating to convert Python objects into JSON format
   *app.py
   *template
   *migrations
4. Run the following code to create the Database tables:
   ```bash
   from app import db, app
   with app.app_context():
       db.create_all()
   exit()
   ```
5. Run the app
   ```bash
   python app.py
   ```
6. Finally, open the address shown in the terminal Ctrl+Click

## If accessed online
Assuming local functionality is used as a test to check the performance of the booking system we can continue to deploy the program online

1. Download and install the Heroku CLI
2. Login to Heroku
3. Create the new app
4. Set up the free online database (PostgreSQL) and provide a DATABASE_URL environment variable.
5. Initialize the Database on Heroku
6. Push Your Code to Heroku
7. Deploy the app to Heroku
8. Finally, check the app interface and functionality using the URL provided in Heruko

Heroku will generate a URL that can be access on any computer and will allow remote access to book the lab equipment

# Future Enhancements
- Conflict Prevention: Automatically checks for overlapping bookings and notifies users of conflicts.

- Booking Management Improvement: View, update, or cancel reservations effortlessly.

- Integration with email notifications for booking confirmations and reminders.

- Support for mobile-friendly interfaces.


