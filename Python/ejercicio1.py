import math
import os
def sumar():
    print("-------------------------------------")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    resultado = n1 + n2
    print("El resultado de la suma es: ", resultado)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')



def area():
    print("-------------------------------------")
    radio = int(input("El radio de la circunferencia es: "))
    area =  math.pi*(radio)**2
    print("El area de la circunferencia de radio", radio, "es: ", area)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')



def calculo():
    print("-------------------------------------")
    numeroUno = int(input("Ingrese el primer numero: "))
    numeroDos = int(input("Ingrese el segundo numero: "))
    suma = numeroUno + numeroDos
    resta = numeroUno - numeroDos
    multiplicacion = numeroUno * numeroDos
    division = numeroUno / numeroDos
    print("El resultado de la suma de los numeros", numeroUno, "y ", numeroDos, "es: ", suma)
    print("El resultado de la resta de los numeros", numeroUno, "y ", numeroDos, "es: ", resta)
    print("El resultado de la multiplicacion de los numeros", numeroUno, "y ", numeroDos, "es: ", multiplicacion)
    print("El resultado de la division de los numeros", numeroUno, "y ", numeroDos, "es: ", division)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')



def sueldo():
    print("-------------------------------------")
    pagoHora = 10000
    horas = float(input("Ingrese la cantidad de horas trabajadas en el mes: "))
    sueldoBruto = pagoHora * horas
    print("El sueldo bruto del empleado es de: ", sueldoBruto)
    print("-------------------------------------")
    input("continuar")
    os.system('cls')



def temperatura():
    print("-------------------------------------")
    celcius = float(input("La temperatura el grados celcius es: "))
    farenheit = (9/5)*celcius + 32
    print("La temperatura en grados Farenheit es: ", farenheit)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')



def calculoAnidado():
    print("-------------------------------------")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    n3 = int(input("Ingrese el tercer numero: "))
    suma = n1 + n2
    multiplicacion = n2*n3
    division = suma / multiplicacion
    print("Valores: ", n1, n2, n3)
    print("Suma primeros 2 valores: ", suma )
    print("Multiplicacion ultimos 2 valores", multiplicacion)
    print("La división final de los valores es", suma, "y", multiplicacion, "es: ", division)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')

