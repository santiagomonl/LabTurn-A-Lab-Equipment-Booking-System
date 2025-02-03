![previous_logo](https://github.com/user-attachments/assets/41fa7aed-9e84-4ca5-b3e8-152c4397d1af)

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

## If accessed online
local functionality was used as a test to check the performance of the booking system to continue with deploying the app online

1. Create a GitHub repository with all the files require to run the app
2. Login to Render
3. Create the respective files for deploying the Labturn app on Render:
   * requirements.txt
   * Procfile
4. Create the new app
5. Set up the free online database (PostgreSQL) and provide a DATABASE_URL environment variable.
6. Initialize the Database on Render
7. Push the Code to Render
8. Deploy the app in Render
9. Finally, check the app interface and functionality using the URL provided in Render

Render will generate a URL that can be access on any computer and will allow remote access to book the lab equipment: [LabTurn Website](https://labturn-a-lab-equipment-booking-system.onrender.com)

**This intuitive online interface does not need any installation or setting on your computer. Simply access the website and the interface will load in your browser for your to start booking your lab equipment.**

## If run locally
1. Need to install python on your computer
2. Need to install the following libraries
    ```bash
   pip install Flask Flask-SQLAlchemy os Flask-Migrate
   ```
3. Download the following folders that include HTML files that use Javascript and Jinja2 templating to convert Python objects into JSON format
   * app.py
   * template
   * migrations
   * static
   * requirements.txt
   * Procfile.txt
4. Change the URL in the app file as follow: 

```bash
# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///lab_equipment.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

5. Run the following code to create the Database tables:
   ```bash
   from app import db, app
   with app.app_context():
       db.create_all()
   exit()
   ```
6. Run the app
   ```bash
   python app.py
   ```
7. Finally, open the address shown in the terminal Ctrl+Click

# Future Enhancements
- Conflict Prevention: Automatically checks for overlapping bookings and notifies users of conflicts.

- Booking Management Improvement: View, update, or cancel reservations effortlessly.

- Integration with email notifications for booking confirmations and reminders.

- Support for mobile-friendly interfaces.


