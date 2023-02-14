#Assets
from flask import Flask, render_template
import sqlite3 as sql

#Class Web
class web:
    #Config Web
    def __init__(self, config):
        #Property Settings
        self.config = config
        #Create Website
        self.app = Flask(__name__)
        #Website Secret Key
        self.app.secret_key = config[0]
        #Datebase
        self.db = sql.connect(self.config[1])
        self.db.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title CHAR(200) NOT NULL, description TEXT, done CHAR(1) NOT NULL DEFAULT "N", due_date DATETIME, created_at DATETIME NOT NULL, update_at DATETIME NOT NULL)')
        self.db.commit()

        #Index
        @self.app.route('/')
        def index():
            tasks = [
                {
                    'done': False,
                    'title': 'Task 1',
                    'description': 'Do something',
                    'created_at': '2023-02-14 10:00:00',
                },
                {
                    'done': True,
                    'title': 'Task 2',
                    'description': 'Do something else',
                    'created_at': '2023-02-13 15:00:00',
                },
                {
                    'done': False,
                    'title': 'Task 3',
                    'description': 'Do yet another thing',
                    'created_at': '2023-02-12 12:00:00',
                },
            ]
            return render_template('home.html', tasks=tasks)

    #Run Website
    def run(self, debug=False):
        self.app.run(debug=debug)

    #Close Aplication
    def __del__(self):
        self.db.close()