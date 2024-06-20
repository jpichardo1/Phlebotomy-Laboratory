from . import CONN, CURSOR
from colorama import Fore, Back, Style

class Patient:

    @classmethod
    def create_table(cls):
        sql = """
             CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                date_of_birth DATE,
                address TEXT,
                phone INTEGER,
                is_sick BOOL
             );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def __init__(self, name, date_of_birth, address, phone, is_sick, id=None):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.is_sick = is_sick

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO patients (name, date_of_birth, address, phone, is_sick)
                VALUES (?, ?, ?, ?, ?);
            """
            CURSOR.execute(sql, (self.name, self.date_of_birth, self.address, self.phone, self.is_sick))
            self.id = CURSOR.lastrowid
            CONN.commit()

    @classmethod
    def find_by_id(cls, patient_id):
        sql = """
            SELECT * FROM patients WHERE id = ?;
        """
        CURSOR.execute(sql, (patient_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], date_of_birth=row[2], address=row[3], phone=row[4], is_sick=row[5])
        return None

    @classmethod
    def get_all_patients(cls):
        sql = """
            SELECT * FROM patients;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], date_of_birth=row[2], address=row[3], phone=row[4], is_sick=row[5]) for row in rows]
    
    @classmethod
    def create(cls, name, date_of_birth, address, phone, is_sick):
        patient = cls(name, date_of_birth, address, phone, is_sick)
        patient.save()
        return patient

    def update(self):
        sql = """
            UPDATE patients
            SET name = ?, date_of_birth = ?, address = ?, phone = ?, is_sick = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.date_of_birth, self.address, self.phone, self.is_sick, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM patients WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def find_by_id_with_appointments(cls, patient_id):
        sql = """
            SELECT 
                patients.id, patients.name, patients.date_of_birth, patients.address, patients.phone, patients.is_sick,
                appointments.id, appointments.date, phlebotomists.name
            FROM 
                patients
            LEFT JOIN 
                appointments 
            ON 
                patients.id = appointments.patient_id
            LEFT JOIN 
                phlebotomists
            ON 
                appointments.phlebotomist_id = phlebotomists.id
            WHERE 
                patients.id = ?;
        """
        CURSOR.execute(sql, (patient_id,))
        rows = CURSOR.fetchall()

        if rows:
            patient_data = rows[0]
            patient = cls(id=patient_data[0], name=patient_data[1], date_of_birth=patient_data[2], address=patient_data[3], phone=patient_data[4], is_sick=patient_data[5])
            appointments = []
            for row in rows:
                if row[6]:  # Check if there is an appointment
                    appointment = {
                        'appointment_id': row[6],
                        'date': row[7],
                        'phlebotomist_name': row[8]
                    }
                    appointments.append(appointment)
            return patient, appointments
        return None, None   

    def is_sick_status(self):
        return f"{Fore.RED}Yes{Fore.RESET}" if self.is_sick else f"{Fore.GREEN}No{Fore.RESET}"    

    def __repr__(self):
        return f"{Fore.WHITE}Patient(ID - {self.id} | {self.name} | {self.date_of_birth} | {self.address} | {self.phone} | Is sick? - {self.is_sick_status()})"
