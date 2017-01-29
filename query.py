import sqlite3,pandas
conn = sqlite3.connect("factbook.db")

c = conn.cursor()
query = "select name from facts order by population desc limit 10;"
c.execute(query)
print (c.fetchall())
