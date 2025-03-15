##Comentario

name = "Maria"

avios: float = 1.2 #manera correcta de tipado

users = ["Luis", "Laura", "Luisa"]

headers = ("User", "Salary", "State")

print(type(headers))

Data_user = {"User": "Maria", "Salary": 1200000, "is_active": True }

print(type(Data_user))

is_active = True

my_set ={19, 43, 53, 67}

#Concatenar 

print("Nombre usuario ", name , " ")

print(f"Usuario : {name} \n Estado: {is_active}")

#Operadores 

#Aritméticos (+, -, *, /, %)

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))

result = num1 + num2
print(f"El resultado de la suma es: {result}")

##Laboratory -> crea una calculadora con las distintas operaciones

# Comparation <, >, >=, =>, ==, !=

junior_salary = 3000000
semi_senior_salary = 4500000

which_is_higher = junior_salary > semi_senior_salary

print(f"Es mayor{which_is_higher}")

##Laboratory -> Cree un caso de uso para cada uno de los operadores de comparacion 

# Logic comparators and or not

mail = True
phone = False
user = mail or phone
password = False

session = user and password
print(user)

print(f"user : {user}")
print(f"Inicio de sesion {session}")

##Asing Operator

salary = salary + 200000
salary += 200000

##Laboratory, investigue que pasa si coloco el =+
salary =+ 350000