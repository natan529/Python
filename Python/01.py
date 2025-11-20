""" Calculadora basica python """

# Funcion principal
def calculadora(n1: int, n2: int, Opciones: str):
    match Opciones:
        case '+':
            suma = n1 + n2
            print(f"Suma: {suma}")
        case '-':
            resta = n1 - n2
            print(f"Resta: {resta}")
        case '*':
            multiplicacion = n1 * n2
            print(f"Multiplicacion: {multiplicacion}")
        case '/':
            if n2 != 0:
                division = n1 / n2
                print(f"Division: {(division):.2}")
            else:
                print("Error, ingrese un numero que no sea '0'")
        case _:
            print("Error, ingrese una de las Opciones previas")

# Opciones
print("(+) > sumar")
print("(-) > resta")
print("(*) > multiplicacion")
print("(/) > division")


# El usuario ingresa los numeros
n1 = int(input("Numero (1): "))
n2 = int(input("Numero (2): "))
opcion = str(input("Opcion a realizar: "))

# llamamos a la funcion
calculadora(n1, n2, opcion)