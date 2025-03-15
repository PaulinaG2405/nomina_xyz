
print("1. Sura 2. Colsanitas 3. Savia Default Sisben")

select = int(input("Selecciona su eps, si no es ecriba 0 (cero)"))

match select:
    case 1:
        print("Sura")
    case 2:
        print("Colsanitas")
    case 3:
        print("Savia")
    case _:
        print("Sisben")

        