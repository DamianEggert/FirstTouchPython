list = ["Damian", 23, True, "Agata", 21, False] #pojebane xd
print(list[2])
print(list[2:])
list[2] = False
print(list[2:5])
print(list)

data = ["Krystian", "Piotr", 18, 23, True, True]
data.extend(list)
print(data)
data.append("Nowy")
print(data)
data.insert(1,"Huehue")
print(data)
data.remove(18)
print(data)
print(data.index(23))

dataData = data.copy()
data.clear()
print(dataData)
print(data)