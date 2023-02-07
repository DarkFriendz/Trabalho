import sqlite3

con = sqlite3.connect('database/teste.db')

DBW = con.cursor()

DBW.execute("CREATE TABLE tarefas (Id int primary key, Title varchar(200), Description text(350), Done tinyint, Data datetime, Prazo datetime, Edit datetime)")