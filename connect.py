#Assets
import sqlite3 as sql

#Config
from config import config

#Class Datebase
class db:
    #Config Datebase
    def __init__(self):
        #Create Table NOT EXISTS
        with sql.connect(config[1]) as con:
            con.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title CHAR(200) NOT NULL, description TEXT, done CHAR(1) NOT NULL DEFAULT "N", due_date DATETIME, created_at DATETIME NOT NULL, update_at DATETIME NOT NULL)')
            #con.execute('INSERT INTO todos (title, description, due_date, created_at, update_at) VALUES (?, ?, ?, ?, ?)', ("Hospital", None, None, "2023/03/01 10:10:10", "2023/03/01 10:10:10"))
            con.commit()
        
    #Get Table All Values
    def tasks(self):
        with sql.connect(config[1]) as con:
            cur = con.cursor()
            tasks = cur.execute('SELECT * FROM todos').fetchall()
        return tasks
