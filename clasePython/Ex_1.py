


user = [] #List

headers = ("Id", "nombre", "apellido", "email", "salario", "estado") #Tuple NO CAMBIAN DESPUES DE CREARSE 

i = 0
while i < 5:
    item = input(f"Ingrese el dato {i}")
    user.append(item)
    i += 1

j = 0 
while j < len(user):
    print(headers[j],user[j])
    j = 0



