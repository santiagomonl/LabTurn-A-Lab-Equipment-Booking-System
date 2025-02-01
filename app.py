from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://santiagoml:t6cP6VgnMG8Xa9l8yNozRxKVF9EtTGcP@dpg-cuf6i9tumphs73aunut0-a.frankfurt-postgres.render.com/labturn_database')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database Models
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(5), nullable=False)  # 'HH:MM' format (e.g., '09:00')
    end_time = db.Column(db.String(5), nullable=False)    # 'HH:MM' format (e.g., '10:00')

# Routes
@app.route('/')
def index():
    equipment = Equipment.query.all()
    return render_template('index.html', equipment=equipment)

@app.route('/equipment/<int:equipment_id>', methods=['GET', 'POST'])
def equipment_page(equipment_id):
    equipment = Equipment.query.get_or_404(equipment_id)
    
    # Fetch all reservations for this equipment
    reservations = Reservation.query.filter_by(equipment_id=equipment_id).all()

    # Format reservations for FullCalendar
    formatted_reservations = [
        {
            'title': f"{res.user_name}",
            'start': f"{res.date}T{res.start_time}",
            'end': f"{res.date}T{res.end_time}"
        } for res in reservations
    ]

    # Get available time slots for this equipment
    available_time_slots = get_available_time_slots()

    if request.method == 'POST':
        user_name = request.form['user_name']
        date = request.form['date']
        selected_slots = request.form.getlist('selected_slots')

        for slot in selected_slots:
            start_time, end_time = slot.split('-')
            # Create a new reservation
            new_reservation = Reservation(user_name=user_name, equipment_id=equipment_id, date=date, start_time=start_time, end_time=end_time)
            db.session.add(new_reservation)
            db.session.commit()
            flash(f'Reservation successful for {start_time} - {end_time}!', 'success')

        return redirect(url_for('equipment_page', equipment_id=equipment.id))

    return render_template(
        'equipment_page.html',
        equipment=equipment,
        reservations=formatted_reservations,
        time_slots=available_time_slots
    )


def get_available_time_slots():
    """
    Generate available time slots from 08:00 to 19:00 in hourly intervals.
    """
    time_slots = []
    start_hour = 8  # 08:00
    end_hour = 19   # 19:00

    for hour in range(start_hour, end_hour):
        start_time = f"{hour:02d}:00"
        end_time = f"{hour + 1:02d}:00"
        time_slots.append({'start_time': start_time, 'end_time': end_time})

    return time_slots

# Temporary route to run migrations
# @app.route('/run-migrations')
# def run_migrations():
#     try:
#         from flask_migrate import upgrade
#         upgrade()
#         return "Migrations applied successfully!"
#     except Exception as e:
#         app.logger.error(f"Error applying migrations: {e}")
#         return f"Error applying migrations: {e}", 500

# Create sample data
@app.before_request
def create_sample_data():
    if not Equipment.query.first():
        sample_equipment = [
            Equipment(name='Confocal Microscope', is_available=True),
            Equipment(name='Scanner Microscope', is_available=True),
            Equipment(name='Biohood', is_available=True)
        ]
        db.session.bulk_save_objects(sample_equipment)
        db.session.commit()

# Run the Application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
