from app import db, Equipment

equipment = Equipment.query.all()
print(equipment)  # Should print a list of Equipment objects
