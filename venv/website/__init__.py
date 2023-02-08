#Assets
from flask import Flask, render_template, redirect, request
import sqlite3 as sql
from datetime import datetime, timedelta

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

            data = datetime.now()
            dataNow = int(datetime.strftime(data, "%Y%m%d%H%M%S"))

            lines = []

            for dbList in db.fetchall():
                dataconfirm = datetime.strptime(dbList[5], "%Y/%m/%d %H:%M:%S")
                dataconfirm = int(datetime.strftime(dataconfirm, "%Y%m%d%H%M%S"))
                if dataNow >= dataconfirm:
                    lines.append([dbList[0], dbList[1], dbList[2], dbList[3], dbList[4], dbList[5], dbList[6], 1])
                else:
                    lines.append([dbList[0], dbList[1], dbList[2], dbList[3], dbList[4], dbList[5], dbList[6], 0])

            dataMin = datetime.now()+timedelta(days=1)
            dataMin = datetime.strftime(dataMin, "%Y-%m-%dT%H:%M:%S")

            dataMax = datetime.now()+timedelta(weeks=4)
            dataMax = datetime.strftime(dataMax, "%Y-%m-%dT%H:%M:%S")

            return render_template('home.html', list=lines, dataMin=dataMin, dataMax=dataMax)

        #Execute Page
        @self.website.route('/execute/', methods=["POST"])
        def execute():
            print(request.form['Select'])
            if request.form['Form'][0] == "0":
                select = request.form["Select"].split(":")
                select = select[:-1]
                con = sql.connect(self.config[1])
                DBW = con.cursor()
                for line in select:
                    DBW.execute(f"UPDATE tarefas set Done=1 WHERE Id={line}")
                con.commit()
                con.close()
                return redirect("/")
            elif request.form['Form'][0] == "1":
                return "Deletar Tarefa"
            elif request.form['Form'][0] == "2":
                return "Adcionar Tarefa"
            elif request.form['Form'][0] == "3":
                return "Editar"
            elif request.form['Form'][0] == "4":
                return "Remover"
            else:
                return redirect("/")

        #Run Website
        self.website.run(debug=True)