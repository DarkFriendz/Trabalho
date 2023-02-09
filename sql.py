import sqlite3 as sql
from datetime import datetime

data = datetime.now()
data = datetime.strftime(data, "%Y/%m/%d %H:%M:%S")
data = "2023/01/01 10:10:10"

con = sql.connect('database/Database.db')

DBW = con.cursor()

try:
    DBW.execute("CREATE TABLE tarefas(Id integer PRIMARY KEY, Title varchar(200), Description text(350), Done tinyint, Data SmallDateTime, Prazo SmallDateTime, Edit SmallDateTime)")
except:
    #DBW.execute("DELETE FROM tarefas WHERE Title='Hospital'")
    DBW.execute(f"INSERT INTO tarefas (Title, Description, Done, Data, Prazo, Edit) VALUES ('Hospital da Cruz', 'Enviar PDFS e XMLS para o Hospital', 0, '{data}', '{data}', null)")


con.commit()

con.close()