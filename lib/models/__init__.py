import sqlite3

CONN = sqlite3.connect('healthcare.db')
CURSOR = CONN.cursor()
