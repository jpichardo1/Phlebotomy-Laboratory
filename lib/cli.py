# lib/cli.py

from colorama import Fore
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
            print(Fore.RED + "Invalid choice")

def menu():

    print(Fore.MAGENTA + """
_ _ _ ____ _    ____ ____ _  _ ____    ___ ____    ___ _  _ ____ 
| | | |___ |    |    |  | |\/| |___     |  |  |     |  |__| |___
|_|_| |___ |___ |___ |__| |  | |___     |  |__|     |  |  | |___  

___  _  _ _    ____ ___  ____ ___ ____ _  _ _   _    _    ____ ___  ____ ____ ____ ___ ____ ____ _   _  
|__] |__| |    |___ |__] |  |  |  |  | |\/|  \_/     |    |__| |__] |  | |__/ |__|  |  |  | |__/  \_/  
|    |  | |___ |___ |__] |__|  |  |__| |  |   |      |___ |  | |__] |__| |  \ |  |  |  |__| |  \   |     

      |___________________________________
|-----|- - -|''''|''''|''''|''''|''''|'##\|__
|- -  |  cc 6    5    4    3    2    1 ### __]==----------------------
|-----|________________________________##/|
      |

          """)

    print(Fore.WHITE + "Please select an option:")
    print(Fore.RED + "0. Exit the program")
    print(Fore.WHITE + "1. Manage Patients")
    print(Fore.WHITE + "2. Manage Phlebotomists")
    print(Fore.WHITE + "3. Manage Appointments")

def patient_menu():

    print(Fore.MAGENTA + """
 _       __    _       __    __    ____      ___    __   _____  _   ____  _     _____  __  
| |\/|  / /\  | |\ |  / /\  / /`_ | |_      | |_)  / /\   | |  | | | |_  | |\ |  | |  ( (` 
|_|  | /_/--\ |_| \| /_/--\ \_\_/ |_|__     |_|   /_/--\  |_|  |_| |_|__ |_| \|  |_|  _)_) 

            """)

    print(Fore.WHITE + "1. Add a patient")
    print(Fore.WHITE + "2. Update a patient")
    print(Fore.RED + "3. Delete a patient")
    print(Fore.WHITE + "4. View all patients")
    print(Fore.WHITE + "5. View a patient")
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
        print(Fore.RED + "Invalid choice")

def phlebotomist_menu():

    print(Fore.MAGENTA + """    
 _       __    _       __    __    ____      ___   _     _     ____  ___   ___  _____  ___   _      _   __  _____  __  
| |\/|  / /\  | |\ |  / /\  / /`_ | |_      | |_) | |_| | |   | |_  | |_) / / \  | |  / / \ | |\/| | | ( (`  | |  ( (` 
|_|  | /_/--\ |_| \| /_/--\ \_\_/ |_|__     |_|   |_| | |_|__ |_|__ |_|_) \_\_/  |_|  \_\_/ |_|  | |_| _)_)  |_|  _)_) 
          
            """)

    print(Fore.WHITE + "1. Add a phlebotomist")
    print(Fore.WHITE + "2. Update a phlebotomist")
    print(Fore.RED + "3. Delete a phlebotomist")
    print(Fore.WHITE + "4. View all phlebotomists")
    print(Fore.WHITE + "5. View a phlebotomist")
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
        print(Fore.RED + "Invalid choice")

def appointment_menu():

    print(Fore.MAGENTA + """
 _       __    _       __    __    ____       __    ___   ___   ___   _   _     _____  _      ____  _     _____  __  
| |\/|  / /\  | |\ |  / /\  / /`_ | |_       / /\  | |_) | |_) / / \ | | | |\ |  | |  | |\/| | |_  | |\ |  | |  ( (` 
|_|  | /_/--\ |_| \| /_/--\ \_\_/ |_|__     /_/--\ |_|   |_|   \_\_/ |_| |_| \|  |_|  |_|  | |_|__ |_| \|  |_|  _)_) 

            """)

    print(Fore.WHITE + "1. Add an appointment")
    print(Fore.WHITE + "2. Update an appointment")
    print(Fore.RED + "3. Delete an appointment")
    print(Fore.WHITE + "4. View all appointments")
    print(Fore.WHITE + "5. View an appointment")
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
        print(Fore.RED + "Invalid choice")

if __name__ == "__main__":
    main()
