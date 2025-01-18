# LabTurn: A Lab Equipment Booking System
## Introduction
The Lab Equipment Booking System is a Python-based web application designed to streamline the process of reserving laboratory equipment. This system will provide an intuitive interface for users to check equipment availability, book resources, and manage reservations efficiently. Whether you are part of an academic institution, research facility, or a shared lab environment, this program simplifies equipment management, reduces scheduling conflicts, and ensures optimal resource utilization.

## Features
*User-Friendly Interface: Simple navigation and intuitive design for seamless booking.

*Real-Time Availability: View the current status of lab equipment in real-time.

*Flexible Scheduling: Reserve equipment for specific dates and times.

*Booking Management: View, update, or cancel reservations effortlessly.

## Input
The user-friendly interface permits easy booking by clicking on the desired hours to book. Additionally, each piece of equipment will show a different calendar that can be modified to reserve the desired time slots.

## Output
The respective calendar for each piece of equipment will show:
*The hours reserved
*The User's name
*The list of reservation

# Techincal Instruction
## If deployed locally
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

   
