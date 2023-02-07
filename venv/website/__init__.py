#Assets
from flask import Flask, render_template
import sqlite3 

#Class Website
class web():
    #Config Website
    def __init__(self, config):
        #Created Website
        self.website = Flask(__name__)

        #Secret Key Website
        self.website.config["secret_key"] = config[0]
        self.website.secret_key = config[0]

        #Datebase
        self.db = sqlite3.connect

    def run(self):
        
        #Index Page
        @self.website.route('/')
        def index():
            return render_template('home.html')

        #Run Website
        self.website.run(debug=True)