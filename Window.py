import sqlite3 as lite
import os
con = lite.connect(str(os.getcwd() + '\GIS.db'))
cur = con.cursor()
cur.execute("SELECT * FROM Sities_list")
data = cur.fetchall()
for i in data:
    print(i[0])