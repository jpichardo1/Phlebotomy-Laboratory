# Phlebotomy Laboratory Management System

## Overview

The Phlebotomy Laboratory Management System is a Python-based command-line application designed to manage patients, appointments, and phlebotomists in a healthcare setting. This system provides functionalities to add, view, update, and delete patient information, schedule appointments with specific phlebotomists, and manage the overall workflow efficiently.

## Directory Structure

```console
.
├── lib

    ├── models
    │   ├── __init__.py
    │   ├── appointment.py
    │   ├── patient.py
    │   ├── phlebotomist.py
    │   └── seeds.py
    ├── cli.py
    ├── debug..py
    └── helpers.py
├── Healthcare.db
├── Pipfile
├── Pipfile.lock
└── README.md

```

## Features

- **Patient Management:**
  - Add new patients with details such as name, date of birth, address, phone number, and sickness status.
  - View existing patient information.
  - Update patient details.
  - Delete patients from the system.

- **Appointment Scheduling:**
  - Schedule appointments for patients with specific dates and times.
  - Assign phlebotomists to appointments.
  - View upcoming appointments.
  - Update or cancel appointments as needed.

- **Phlebotomist Management:**
  - Add new phlebotomists with their names and specialization areas.
  - View existing phlebotomist information.
  - Update phlebotomist details.
  - Delete phlebotomists from the system.

## Install Dependencies
  Ensure you have Python and pipenv installed. Install the required Python packages using pipenv.
  - pipenv install
  - pipenv shell
  This will activate the virtual environment for your project.

## Set Up the Database
  Ensure SQLite is installed on your system. Create a SQLite database file named healthcare.db in the project directory.

## Seed the Database
  Run the seed script to populate the database with initial data.
  - python lib/models/seeds.py
  Wait for the script to finish executing to ensure all seed data is installed.

## Run the Application
  Start the command-line interface (CLI) application to begin using the Phlebotomy Laboratory Management System.
  - python lib/cli.py
  Follow the prompts in the terminal to interact with the application, manage patients, appointments, and phlebotomists as needed.

## 
Adjust the paths and commands based on your actual project structure and naming conventions. These instructions assume basic familiarity with Python, SQLite, and command-line interface operations.


