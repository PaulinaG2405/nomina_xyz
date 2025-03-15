

user = [1, "Pedro", "pp@gmail.com", 2500000, True]

user.append(9.5) #Así se agrega más items
user.insert(2, "Peréz")
user[4] = 2400000 #Asi se sobreescribe
user.remove(True) #Elimina 
user.pop() #Elimina el ultimo
user.pop(4) #Elimina el item de la posición 4

print(user)
