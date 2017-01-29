import sqlite3, pandas
conn = sqlite3.connect("factbook.db")
query1 = "select sum(area_land) from facts where area_land!= 0;"
query2 = "select sum(area_water) from facts where area_water!= 0;"
area_land = conn.execute(query1).fetchone()
area_water = conn.execute(query2).fetchone()
res = area_land[0]/area_water[0]
print(res)