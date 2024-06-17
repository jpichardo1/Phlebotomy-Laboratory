from models.__init__ import CONN, CURSOR

class Appointment:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                date DATETIME,
                phlebotomist_id INTEGER,
                patient_id INTEGER,
                FOREIGN KEY (phlebotomist_id) REFERENCES phlebotomists(id),
                FOREIGN KEY (patient_id) REFERENCES patients(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS appointments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, date, phlebotomist_id, patient_id, id=None):
        self.id = id
        self.date = date
        self.phlebotomist_id = phlebotomist_id
        self.patient_id = patient_id

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO appointments (date, phlebotomist_id, patient_id)
                VALUES (?, ?, ?);
            """
            CURSOR.execute(sql, (self.date, self.phlebotomist_id, self.patient_id))
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE appointments
                SET date = ?, phlebotomist_id = ?, patient_id = ?
                WHERE id = ?;
            """
            CURSOR.execute(sql, (self.date, self.phlebotomist_id, self.patient_id, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, appointment_id):
        sql = """
            SELECT * FROM appointments WHERE id = ?;
        """
        CURSOR.execute(sql, (appointment_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], date=row[1], phlebotomist_id=row[2], patient_id=row[3])
        return None

    @classmethod
    def get_all_appointments(cls):
        sql = """
            SELECT * FROM appointments;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], date=row[1], phlebotomist_id=row[2], patient_id=row[3]) for row in rows]

    @classmethod
    def create(cls, date, phlebotomist_id, patient_id):
        appointment = cls(date, phlebotomist_id, patient_id)
        appointment.save()
        return appointment

    def update(self):
        sql = """
            UPDATE appointments
            SET date = ?, phlebotomist_id = ?, patient_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.date, self.phlebotomist_id, self.patient_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM appointments WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def __repr__(self):
        return f"Appointment(id={self.id}, date='{self.date}', phlebotomist_id={self.phlebotomist_id}, patient_id={self.patient_id})"
