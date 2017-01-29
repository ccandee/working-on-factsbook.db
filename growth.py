import pandas,sqlite3,math
conn = sqlite3.connect("factbook.db")
query = "select * from facts;"
dataframe = pandas.read_sql_query(query, conn)
data = dataframe.dropna(axis=0)
print(data.iloc[0])
def predict_row(row):
    y = row.loc["updated_at"]
    y1 = int(y[0:4])
    n = row["population"]*pow(math.e, (2050-y1)*row["population_growth"]/100)
    return n
data["current"]= data.apply(predict_row, axis = 1)
data.sort_values("current",ascending = False, inplace = True)
print(data.iloc[0:10])