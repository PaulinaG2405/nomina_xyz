##Crear un menú que persista y solo salga cuando seleccionamos la opcion

while True:
    print("     Generos")
    print("1. Misterio")
    print("2. Policiaco")
    print("3. Novela negra")
    print("4. Salir")
    select = int(input("ESCOGE UN GENERO"))

    match select:
        case 1: 
            print("Digite un autor")
        case 2: 
            print("Te recomiendo Agatha Cristie")
        case 3:
            print("Edgar Allan Poe es el padre de la novela negra")
        case 4:
            select= False
            break
        case _:
            print ("Escoja una opción")


    init = int(input("Presione 1 para salir"))

    while init !=0: 
        opc = int(input("Seleccione 1.Registra 2. Ingresar 3. Salir"))
        match opc: 
            case 1:
                print("Registre su usario")
            case 2: 
                print("Digite su usuario")
            case 3: 
                print("salir")
                init = 0 
            case _:
                print("Seleccione una opcion")
    

