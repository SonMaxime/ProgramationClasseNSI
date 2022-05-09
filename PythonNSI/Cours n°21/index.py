dic_auto = {
    "Porche": "Cayenne",
    "Renault": "Laguna",
    "Peugeot": "4008",
    "Audi": "Q5"
}
dic_auto["Aston Martin"] = "DBS"
print(dic_auto)
print(sorted(dic_auto.keys()))
print(len(dic_auto))
print(dic_auto.values())
print(dic_auto.keys())
if "Opel" in dic_auto:
    print("oui")
else:
    print("non")