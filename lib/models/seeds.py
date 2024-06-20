from patient import Patient
from appointment import Appointment
from phlebotomist import Phlebotomist

def seeds_database():

    print("Resetting tables...")

    Patient.drop_table()
    Appointment.drop_table()
    Phlebotomist.drop_table()
    Patient.create_table()
    Appointment.create_table()
    Phlebotomist.create_table()
    
    print("Resetting complete...")
    print("Populating tables...")
     
    patients = [
        Patient.create("Brian Turtle", "2000-05-15", "123 Main St", 1234567890, True),
        Patient.create("Nicolas Flower", "1990-02-05", "456 Oak St", 2345678901, False),
        Patient.create("Chris Notnotchris", "1970-11-29", "789 Pine St", 3456789012, True),
        Patient.create("Lantz Captain", "1969-09-24", "101 Maple St", 4567890123, False),
        Patient.create("Jessica Pichardo", "1997-10-31", "202 Birch St", 5678901234, True),
    ]

    phlebotomists = [
        Phlebotomist.create("Yennifer Medina", 3),
        Phlebotomist.create("Dana Ventura", 20),
        Phlebotomist.create("Xuzuelle Borja", 4),
        Phlebotomist.create("Angelina Flores", 12),
        Phlebotomist.create("Brent Williams", 9),
    ]

    appointments = [
        Appointment.create("06-01-2024 09:00:00", phlebotomists[0].id, patients[0].id),
        Appointment.create("06-08-2024 10:30:00", phlebotomists[1].id, patients[1].id),
        Appointment.create("06-14-2024 11:15:00", phlebotomists[2].id, patients[2].id),
        Appointment.create("06-19-2024 12:45:00", phlebotomists[3].id, patients[3].id),
        Appointment.create("06-27-2024 13:15:00", phlebotomists[4].id, patients[4].id),
    ]

    print("Populating finished...")

seeds_database()