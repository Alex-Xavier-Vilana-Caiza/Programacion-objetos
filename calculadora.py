import sys

n1 = 0
n2 = 0

menu = """
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Salir
"""

def Sumar():
    print("Ingresa el primer sumando: ")
    n1 = float(input())
    print("Ingresa el segundo sumando: ")
    n2 = float(input())
    print("El resultado es: ", n1 + n2)

def Restar():
    print("Ingresa el minuendo: ")
    n1 = float(input())
    print("Ingresa el sustraendo: ")
    n2 = float(input())
    print("El resultado es: ", n1 - n2)

def Multiplicar():
    print("Ingresa el primer coeficiente: ")
    n1 = float(input())
    print("Ingresa el segundo coeficiente: ")
    n2 = float(input())
    print("El resultado es: ", n1 * n2)

def Dividir():
    print("Ingresa el dividendo: ")
    n1 = float(input())
    print("Ingresa el divisor: ")
    n2 = float(input())
    print("El resultado es: ", n1 / n2)


print("Bienvenido, Calculadora Basica...")
while True:
    print(menu)
    opc = int(input())
    if opc == 1:
        Sumar()
    elif opc == 2:
        Restar()
    elif opc == 3:
        Multiplicar()
    elif opc == 4:
        Dividir()

    elif opc == 5:
        sys.exit()
    