
login = False
user_name = "Luis"

if login:
    print(f"Bienvenido: {user_name}")
else:
    print(f"Valide la información")

## Elif 
print("1. Sura 2. Colsanitas 3. Savia Default Sisben")

select = int(input("Selecciona su eps, si no es ecriba 0 (cero)"))

if select == 1:
    print("Sura")
elif select == 2:
    print("Colsanitas")
elif select == 3:
    print("Savia")
else:
    print("Savia")

