import pandas
data = pandas.read_csv("titanic.csv")
print(data.groupby(["classe", "sexe"]).mean())