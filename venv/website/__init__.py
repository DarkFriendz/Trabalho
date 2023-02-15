#Assets
from flask import Flask, render_template, request, redirect

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

        #Add Work
        @self.app.route('/addWork')
        def addWork():
            return render_template('addWork.html')

        #Actions
        @self.app.route('/actions', methods=["POST"])
        def actions():
            if request.form['form'] == "Edit":
                return "editar"
            elif request.form['form'] == "Delet":
                self.db.deletTask(request.form)
                return redirect("/")
                
        #Execute
        @self.app.route('/execute', methods=["POST"])
        def execute():
            if request.form['form'] == "add":
                self.db.addTask(request.form)
                return redirect("/")
            

    #Run Website
    def run(self, debug=False):
        self.app.run(debug=debug)