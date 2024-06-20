from . import CONN, CURSOR
from colorama import Fore


class Phlebotomist:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS phlebotomists (
                id INTEGER PRIMARY KEY,
                name TEXT,
                yrs_exp INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS phlebotomists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, name, yrs_exp, id=None):
        self.id = id
        self.name = name
        self.yrs_exp = yrs_exp

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO phlebotomists (name, yrs_exp)
                VALUES (?, ?);
            """
            CURSOR.execute(sql, (self.name, self.yrs_exp))
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE phlebotomists
                SET name = ?, yrs_exp = ?
                WHERE id = ?;
            """
            CURSOR.execute(sql, (self.name, self.yrs_exp, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, phlebotomist_id):
        sql = """
            SELECT * FROM phlebotomists WHERE id = ?;
        """
        CURSOR.execute(sql, (phlebotomist_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], yrs_exp=row[2])
        return None

    @classmethod
    def get_all_phlebotomists(cls):
        sql = """
            SELECT * FROM phlebotomists;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], yrs_exp=row[2]) for row in rows]

    @classmethod
    def create(cls, name, yrs_exp):
        phlebotomist = cls(name, yrs_exp)
        phlebotomist.save()
        return phlebotomist

    def update(self):
        sql = """
            UPDATE phlebotomists
            SET name = ?, yrs_exp = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.yrs_exp, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM phlebotomists WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    def __repr__(self):
        return f"{Fore.WHITE}Phlebotomist(ID - {self.id} | {self.name} | Years of experience - {self.yrs_exp})"
