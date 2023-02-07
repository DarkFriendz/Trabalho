import sqlite3 as sql
from datetime import datetime

data = datetime.now()

con = sql.connect('database/Database.db')

DBW = con.cursor()

try:
    DBW.execute("CREATE TABLE tarefas(Id integer PRIMARY KEY, Title varchar(200), Description text(350), Done tinyint, Data datetime, Prazo datetime, Edit datetime)")
except:
    pass
    #DBW.execute("DELETE FROM tarefas WHERE Title='Hospital'")


con.commit()

con.close()