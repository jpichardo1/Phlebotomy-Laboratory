# lib/helpers.py

from models.patient import Patient
from models.phlebotomist import Phlebotomist
from models.appointment import Appointment

def exit_program():
    print("Exiting program. Goodbye!")
    exit()

# Patient helpers
def add_patient():
    name = input("Enter patient name: ")
    address = input("Enter patient address: ")
    phone = input("Enter patient phone: ")
    date_of_birth = input("Enter patient date of birth (YYYY-MM-DD): ")
    is_sick = input("Is the patient sick? (1 for Yes, 0 for No): ")
    patient = Patient.create(name, address, phone, date_of_birth, bool(int(is_sick)))
    print(f"Added patient: {patient}")

def update_patient():
    patient_id = input("Enter patient ID to update: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.name = input(f"Enter new name ({patient.name}): ") or patient.name
        patient.address = input(f"Enter new address ({patient.address}): ") or patient.address
        patient.phone = input(f"Enter new phone ({patient.phone}): ") or patient.phone
        patient.date_of_birth = input(f"Enter new date of birth ({patient.date_of_birth}): ") or patient.date_of_birth
        patient.is_sick = bool(int(input(f"Is the patient sick? (1 for Yes, 0 for No, current {patient.is_sick}): ") or patient.is_sick))
        patient.save()
        print(f"Updated patient: {patient}")
    else:
        print("Patient not found.")

def delete_patient():
    patient_id = input("Enter patient ID to delete: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.delete()
        print(f"Deleted patient: {patient}")
    else:
        print("Patient not found.")

def view_all_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        print(patient)

def view_patient():
    patient_id = input("Enter patient ID to view: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        print(patient)
    else:
        print("Patient not found.")

# Phlebotomist helpers
def add_phlebotomist():
    name = input("Enter phlebotomist name: ")
    yrs_exp = input("Enter years of experience: ")
    phlebotomist = Phlebotomist.create(name, int(yrs_exp))
    print(f"Added phlebotomist: {phlebotomist}")

def update_phlebotomist():
    phlebotomist_id = input("Enter phlebotomist ID to update: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        phlebotomist.name = input(f"Enter new name ({phlebotomist.name}): ") or phlebotomist.name
        phlebotomist.yrs_exp = input(f"Enter new years of experience ({phlebotomist.yrs_exp}): ") or phlebotomist.yrs_exp
        phlebotomist.save()
        print(f"Updated phlebotomist: {phlebotomist}")
    else:
        print("Phlebotomist not found.")

def delete_phlebotomist():
    phlebotomist_id = input("Enter phlebotomist ID to delete: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        phlebotomist.delete()
        print(f"Deleted phlebotomist: {phlebotomist}")
    else:
        print("Phlebotomist not found.")

def view_all_phlebotomists():
    phlebotomists = Phlebotomist.get_all_phlebotomists()
    for phlebotomist in phlebotomists:
        print(phlebotomist)

def view_phlebotomist():
    phlebotomist_id = input("Enter phlebotomist ID to view: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        print(phlebotomist)
    else:
        print("Phlebotomist not found.")

# Appointment helpers
def add_appointment():
    date = input("Enter appointment date (YYYY-MM-DD HH:MM): ")
    phlebotomist_id = input("Enter phlebotomist ID: ")
    patient_id = input("Enter patient ID: ")
    appointment = Appointment.create(date, int(phlebotomist_id), int(patient_id))
    print(f"Added appointment: {appointment}")

def update_appointment():
    appointment_id = input("Enter appointment ID to update: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        appointment.date = input(f"Enter new date ({appointment.date}): ") or appointment.date
        appointment.phlebotomist_id = input(f"Enter new phlebotomist ID ({appointment.phlebotomist_id}): ") or appointment.phlebotomist_id
        appointment.patient_id = input(f"Enter new patient ID ({appointment.patient_id}): ") or appointment.patient_id
        appointment.save()
        print(f"Updated appointment: {appointment}")
    else:
        print("Appointment not found.")

def delete_appointment():
    appointment_id = input("Enter appointment ID to delete: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        appointment.delete()
        print(f"Deleted appointment: {appointment}")
    else:
        print("Appointment not found.")

def view_all_appointments():
    appointments = Appointment.get_all_appointments()
    for appointment in appointments:
        print(appointment)

def view_appointment():
    appointment_id = input("Enter appointment ID to view: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        print(appointment)
    else:
        print("Appointment not found.")
