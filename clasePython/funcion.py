##Una funcion es un bloque de codigo que ejecuta instrucciones y las permite reutilizar y adicionalmente puede recibir argumento

######Entre más comentarios tenga un codigo se considera SUCIO



def result_addition_two_numbers ():
    num1 = int(input("Ingrese el primer num"))
    num2 = int(input("Ingrese el segundo num"))

    sum = num1 + num2
    return sum

addition = result_addition_two_numbers
print(addition)

def result_addition_two_numbers_with_parameters(num1, num2):
    sum = num1 + num2
    return sum

addition2 = result_addition_two_numbers_with_parameters
print(addition2)