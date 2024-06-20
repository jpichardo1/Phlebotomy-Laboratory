# import random
# from faker import Faker # type: ignore
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
     
    # Create 5 patients
    patients = [
        Patient.create("Brian Turtle", "2000-05-15", "123 Main St", 1234567890, True),
        Patient.create("Nicolas Flower", "1990-02-05", "456 Oak St", 2345678901, False),
        Patient.create("Chris Notnotchris", "1970-11-29", "789 Pine St", 3456789012, True),
        Patient.create("Lantz Captain", "1969-09-24", "101 Maple St", 4567890123, False),
        Patient.create("Jessica Pichardo", "1997-10-31", "202 Birch St", 5678901234, True),
    ]

    # Create 5 phlebotomists
    phlebotomists = [
        Phlebotomist.create("Yennifer Medina", 3),
        Phlebotomist.create("Dana Ventura", 20),
        Phlebotomist.create("Xuzuelle Borja", 4),
        Phlebotomist.create("Angelina Flores", 12),
        Phlebotomist.create("Brent Williams", 9),
    ]

    # Create 5 appointments
    appointments = [
        Appointment.create("06-01-2024 09:00:00", phlebotomists[1].id, patients[1].id),
        Appointment.create("06-08-2024 10:30:00", phlebotomists[2].id, patients[2].id),
        Appointment.create("06-14-2024 11:15:00", phlebotomists[3].id, patients[3].id),
        Appointment.create("06-19-2024 12:45:00", phlebotomists[4].id, patients[4].id),
        Appointment.create("06-27-2024 13:15:00", phlebotomists[5].id, patients[5].id),
    ]

    print("Populating finished...")

# Call the seeds_database function to execute it
seeds_database()


    # patient1 = Patient.create("name", "0000-00-00", "address", 0, True)
    # appointment1 = Appointment.create("2024-06-19 12:45:00", phlebotomists[0].id, 1)



    # fake = Faker()

    # print("Making patients...")

    # patients = []

    # for _ in range(50):
    #     patient = Patient(
    #         name=f"{fake.first_name()} {fake.last_name()}",
    #         phone=random.randint(1000000000, 9999999999),
    #         address=fake.address(),
    #         is_sick=random.choice([True, False])
    #     )
    #     patient.save()
    #     patients.append(patient)

    # print("Making phlebotomists...")

    # phlebotomist = []

    # for _ in range(20):
    #     phlebotomist = Phlebotomist(
    #         name=f"{fake.first_name()} {fake.last_name()}",
    #         yrs_exp=random.randint(1, 20)
    #     )
    #     phlebotomist.save()
    #     phlebotomist.append(phlebotomist)

    # print("Making appointments...")

    # appointments = []

    # for _ in range(100):
    #     appointment = Appointment(
    #         date=fake.date_this_year(),
    #         phlebotomist_id=random.choice(phlebotomist).id,
    #         patient_id=random.choice(patients).id
    #     )
    #     appointment.save()
    #     appointments.append(appointment)

    # print("Seeding complete!")