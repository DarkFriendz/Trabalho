#Assets
from flask import Flask, render_template
import sqlite3 as sql

#Class Website
class web():
    #Config Website
    def __init__(self, config):
        #Created Website
        self.website = Flask(__name__)

        #Secret Key Website
        self.website.config["secret_key"] = config[0]
        self.website.secret_key = config[0]

        #Config
        self.config = config

    def run(self):
        
        #Index Page
        @self.website.route('/')
        def index():
            con = sql.connect(self.config[1])
            db = con.cursor()

            db.execute("SELECT * FROM tarefas")

            return render_template('home.html', db=db.fetchall())

        #Run Website
        self.website.run(debug=True)