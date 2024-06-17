# lib/cli.py

from models.seeds import seeds_database
from helpers import (
    exit_program,
    add_patient, update_patient, delete_patient, view_all_patients, view_patient,
    add_phlebotomist, update_phlebotomist, delete_phlebotomist, view_all_phlebotomists, view_phlebotomist,
    add_appointment, update_appointment, delete_appointment, view_all_appointments, view_appointment
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            patient_menu()
        elif choice == "2":
            phlebotomist_menu()
        elif choice == "3":
            appointment_menu()
        else:
            print("Invalid choice")

def menu():

    print("""

          |--------------------------------------------|
          |**| WELCOME TO THE PHLEBOTOMY LABORATORY |**|
          |--------------------------------------------|

          """)

    print("Please select an option:")
    print("0. Exit the program")
    print("1. Manage Patients")
    print("2. Manage Phlebotomists")
    print("3. Manage Appointments")

def patient_menu():

    print("""

            |-----------------------|
            |**| MANAGE PATIENTS |**|
            |-----------------------|

            """)

    print("1. Add a patient")
    print("2. Update a patient")
    print("3. Delete a patient")
    print("4. View all patients")
    print("5. View a patient")
    choice = input("> ")
    if choice == "1":
        add_patient()
    elif choice == "2":
        update_patient()
    elif choice == "3":
        delete_patient()
    elif choice == "4":
        view_all_patients()
    elif choice == "5":
        view_patient()
    else:
        print("Invalid choice")

def phlebotomist_menu():

    print("""

            |----------------------------|
            |**| MANAGE PHLEBOTOMISTS |**|
            |----------------------------|

            """)

    print("1. Add a phlebotomist")
    print("2. Update a phlebotomist")
    print("3. Delete a phlebotomist")
    print("4. View all phlebotomists")
    print("5. View a phlebotomist")
    choice = input("> ")
    if choice == "1":
        add_phlebotomist()
    elif choice == "2":
        update_phlebotomist()
    elif choice == "3":
        delete_phlebotomist()
    elif choice == "4":
        view_all_phlebotomists()
    elif choice == "5":
        view_phlebotomist()
    else:
        print("Invalid choice")

def appointment_menu():

    print("""

            |---------------------------|
            |**| MANAGE APPOINTMENTS |**|
            |---------------------------|

            """)

    print("1. Add an appointment")
    print("2. Update an appointment")
    print("3. Delete an appointment")
    print("4. View all appointments")
    print("5. View an appointment")
    choice = input("> ")
    if choice == "1":
        add_appointment()
    elif choice == "2":
        update_appointment()
    elif choice == "3":
        delete_appointment()
    elif choice == "4":
        view_all_appointments()
    elif choice == "5":
        view_appointment()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    seeds_database()
    main()
