""" Pedir 3 numero al usuario y retornar el mayor """

# Definimos la funcion principal
def numero_mayor(numero1: int, numero2: int, numero3: int):
    lista = [numero1, numero2, numero3]
    return max(lista)

# Pedimos los 3 numero al usuario
n1 = int(input("Numero (1): "))
n2 = int(input("Numero (2): "))
n3 = int(input("Numero (3): "))

# llamamos a la funcion
print("El numero mayor es:",numero_mayor(n1, n2, n3))

# Esto no va en le codigo, esto es una actualizacion para ver como andamos con el control de versiones git