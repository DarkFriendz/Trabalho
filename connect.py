#Assets
import sqlite3 as sql
from datetime import datetime

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
            data = datetime.now()
            data = datetime.strftime(data, "%Y%m%d%H%M%S")
            tasks = cur.execute('SELECT * FROM todos').fetchall()
            
            for id, task in enumerate(tasks):
                if task[4] != None:
                    dataTask = task[4].replace("/","")
                    dataTask = dataTask.replace(" ", "")
                    dataTask = dataTask.replace(":", "")
                    if data >= dataTask:
                        tasks[id-1] = tasks[id-1]+('Expired',)
            cur.close()

        return tasks

    #Add Values in Table
    def addTask(self, request):
        with sql.connect(config[1]) as con:
            cur = con.cursor()
            data = datetime.now()
            data = datetime.strftime(data, "%Y/%m/%d %H:%M:%S")
            if request['description'] != '':
                if request['date'] != '':
                    cur.execute('INSERT INTO todos (title, description, due_date, created_at, update_at) VALUES (?, ?, ?, ?, ?)', (request['title'], request['description'], request['date'], data, data))
                else:
                    cur.execute('INSERT INTO todos (title, description, due_date, created_at, update_at) VALUES (?, ?, ?, ?, ?)', (request['title'], request['description'], None, data, data))
            else:
                if request['date'] != '':
                    cur.execute('INSERT INTO todos (title, description, due_date, created_at, update_at) VALUES (?, ?, ?, ?, ?)', (request['title'], None, request['date'], data, data))
                else:
                    cur.execute('INSERT INTO todos (title, description, due_date, created_at, update_at) VALUES (?, ?, ?, ?, ?)', (request['title'], None, None, data, data))
            cur.close()

    #Delet Values in Table
    def deletTask(self, request):
        with sql.connect(config[1]) as con:
            cur = con.cursor()
            cur.execute('DELETE FROM todos WHERE (id=?)', (request['id']))
            cur.close()

    #Task Done
    def doneTask(self, request):
        with sql.connect(config[1]) as con:
            cur = con.cursor()
            if request['done'] != "S":
                cur.execute('UPDATE todos SET done=? WHERE id=?', ("S", request['id']))
            else:
                cur.execute('UPDATE todos SET done=? WHERE id=?', ("N", request['id']))
            cur.close()

    #Get Task
    def getTask(self, id):
        with sql.connect(config[1]) as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM todos WHERE (id=?)', (id,))
            task = cur.fetchone()
            cur.close()
            
        return task