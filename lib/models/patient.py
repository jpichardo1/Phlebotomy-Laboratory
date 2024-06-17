from models.__init__ import CONN, CURSOR

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

    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.name}', date_of_birth='{self.date_of_birth}', address='{self.address}', phone={self.phone}, is_sick={self.is_sick})"
