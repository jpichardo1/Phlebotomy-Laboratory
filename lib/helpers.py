# lib/helpers.py

from models.patient import Patient
from models.phlebotomist import Phlebotomist
from models.appointment import Appointment
from colorama import Fore


def exit_program():
    print(Fore.MAGENTA + "Goodbye, Have a nice day!")
    exit()

# Patient helpers
def add_patient():
    name = input(f"{Fore.WHITE}Enter patient name {Fore.BLUE}(First Name & Last Name){Fore.WHITE}: ")
    date_of_birth = input(f"{Fore.WHITE}Enter patient date of birth {Fore.BLUE}(YYYY-MM-DD){Fore.WHITE}: ")
    address = input(f"{Fore.WHITE}Enter patient address {Fore.BLUE}(Number & Street){Fore.WHITE}: ")
    phone = input(f"{Fore.WHITE}Enter patient phone {Fore.BLUE}(1234567890){Fore.WHITE}: ")
    is_sick_input = input(f"{Fore.WHITE}Is the patient sick? {Fore.BLUE}({Fore.RED}1{Fore.BLUE} for {Fore.RED}Yes{Fore.BLUE}, {Fore.GREEN}0{Fore.BLUE} for {Fore.GREEN}No){Fore.BLUE}{Fore.WHITE}: ")
    is_sick = bool(int(is_sick_input))
    patient = Patient.create(name, date_of_birth, address, phone, is_sick)
    print(f"{Fore.GREEN}Added patient: {patient}")

def update_patient():
    patient_id = input(f"{Fore.WHITE}Enter patient ID to update: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.name = input(f"{Fore.WHITE}Enter new name {Fore.BLUE}(First Name & Last Name){Fore.WHITE}: ({patient.name}): ") or patient.name
        patient.date_of_birth = input(f"{Fore.WHITE}Enter new date of birth {Fore.BLUE}(YYYY-MM-DD){Fore.WHITE}: ({patient.date_of_birth}): ") or patient.date_of_birth
        patient.address = input(f"{Fore.WHITE}Enter new address {Fore.BLUE}(Number & Street){Fore.WHITE}: ({patient.address}): ") or patient.address
        patient.phone = input(f"{Fore.WHITE}Enter new phone {Fore.BLUE}(1234567890){Fore.WHITE}: ({patient.phone}){Fore.WHITE}: ") or patient.phone
        patient.is_sick = bool(int(input(f"{Fore.WHITE}Is the patient sick?: {Fore.BLUE}({Fore.RED}1{Fore.BLUE} for {Fore.RED}Yes{Fore.BLUE}, {Fore.GREEN}0{Fore.BLUE} for {Fore.GREEN}No{Fore.BLUE}, current {patient.is_sick}){Fore.BLUE}: ") or patient.is_sick))
        patient.save()
        print(f"{Fore.GREEN}Updated patient: {patient}")
    else:
        print(f"{Fore.RED}Patient not found.")

def delete_patient():
    patient_id = input(f"{Fore.RED}Enter patient ID to delete: ")
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.delete()
        print(f"{Fore.RED}Deleted patient: {patient}")
    else:
        print(f"{Fore.RED}Patient not found.")

def view_all_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        print(patient)

def view_patient():
    patient_id = input(f"{Fore.WHITE}Enter patient ID to view: ")
    patient, appointments = Patient.find_by_id_with_appointments(patient_id)
    if patient:
        print(patient)
        if appointments:
            print(F"{Fore.WHITE}Appointments:")
            for appointment in appointments:
                print(f"{Fore.WHITE}- Appointment ID - {appointment['appointment_id']} | Date: {appointment['date']} | Phlebotomist: {appointment['phlebotomist_name']}")
        else:
            print(f"{Fore.RED}No appointments found.")
    else:
        print(f"{Fore.RED}Patient not found.")

# Phlebotomist helpers
def add_phlebotomist():
    name = input(f"{Fore.WHITE}Enter phlebotomist name {Fore.BLUE}(First name & Last name){Fore.WHITE}: ")
    yrs_exp = input(f"{Fore.WHITE}Enter years of experience: ")
    phlebotomist = Phlebotomist.create(name, int(yrs_exp))
    print(f"{Fore.GREEN}Added phlebotomist: {phlebotomist}")

def update_phlebotomist():
    phlebotomist_id = input(f"{Fore.WHITE}Enter phlebotomist ID to update: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        phlebotomist.name = input(f"{Fore.WHITE}Enter new name ({phlebotomist.name}): ") or phlebotomist.name
        phlebotomist.yrs_exp = input(f"{Fore.WHITE}Enter new years of experience ({phlebotomist.yrs_exp}): ") or phlebotomist.yrs_exp
        phlebotomist.save()
        print(f"{Fore.GREEN}Updated phlebotomist: {phlebotomist}")
    else:
        print(f"{Fore.RED}Phlebotomist not found.")

def delete_phlebotomist():
    phlebotomist_id = input(f"{Fore.RED}Enter phlebotomist ID to delete: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        phlebotomist.delete()
        print(f"{Fore.RED}Deleted phlebotomist: {phlebotomist}")
    else:
        print(f"{Fore.RED}Phlebotomist not found.")

def view_all_phlebotomists():
    phlebotomists = Phlebotomist.get_all_phlebotomists()
    for phlebotomist in phlebotomists:
        print(phlebotomist)

def view_phlebotomist():
    phlebotomist_id = input(f"{Fore.WHITE}Enter phlebotomist ID to view: ")
    phlebotomist = Phlebotomist.find_by_id(phlebotomist_id)
    if phlebotomist:
        print(phlebotomist)
    else:
        print(f"{Fore.RED}Phlebotomist not found.")

# Appointment helpers
def add_appointment():
    date = input(f"{Fore.WHITE}Enter appointment date and time: {Fore.BLUE}(YYYY-MM-DD HH:MM:SS){Fore.WHITE}: ")
    phlebotomist_id = input(f"{Fore.WHITE}Enter phlebotomist ID: ")
    patient_id = input(F"{Fore.WHITE}Enter patient ID: ")
    appointment = Appointment.create(date, int(phlebotomist_id), int(patient_id))
    print(f"{Fore.GREEN}Added appointment: {appointment}")

def update_appointment():
    appointment_id = input(F"{Fore.WHITE}Enter appointment ID to update: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        appointment.date = input(f"{Fore.WHITE}Enter new date ({appointment.date}): ") or appointment.date
        appointment.phlebotomist_id = input(f"{Fore.WHITE}Enter new phlebotomist ID ({appointment.phlebotomist_id}): ") or appointment.phlebotomist_id
        appointment.patient_id = input(f"{Fore.WHITE}Enter new patient ID ({appointment.patient_id}): ") or appointment.patient_id
        appointment.save()
        print(f"{Fore.GREEN}Updated appointment: {appointment}")
    else:
        print(F"{Fore.RED}Appointment not found.")

def delete_appointment():
    appointment_id = input(F"{Fore.RED}Enter appointment ID to delete: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        appointment.delete()
        print(f"{Fore.RED}Deleted appointment: {appointment}")
    else:
        print(F"{Fore.RED}Appointment not found.")

def view_all_appointments():
    appointments = Appointment.get_all_appointments()
    for appointment in appointments:
        print(appointment)

def view_appointment():
    appointment_id = input(F"{Fore.WHITE}Enter appointment ID to view: ")
    appointment = Appointment.find_by_id(appointment_id)
    if appointment:
        print(appointment)
    else:
        print(F"{Fore.RED}Appointment not found.")
