#Assets
from flask import Flask, render_template

#Datebase
from connect import db

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
        self.db = db()

        #Index
        @self.app.route('/')
        def index():
            return render_template('home.html', tasks=self.db.tasks())

    #Run Website
    def run(self, debug=False):
        self.app.run(debug=debug)