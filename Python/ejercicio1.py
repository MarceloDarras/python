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

def volumenArea():
    print("-------------------------------------")
    radio = int(input("Ingrese el radio de la esfera: "))
    V = round((4/3)*math.pi*radio**3)
    A = round(4*math.pi*radio**2)
    print("El volumen de la esfera de radio", radio, "es: ", V)
    print("El area de la esfera de radio", radio, "es: ", A)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')

def conversionMoneda():
    print("-------------------------------------")
    dolares = int(input("Ingrese la cantidad de dolares a convertir: "))
    pesos = round(dolares * 794.56)
    print("La cantidad de", dolares, "ingresada en pesos es de: ", pesos)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')

def areaTriangulo():
    print("-------------------------------------")
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    area = (base*altura)/2
    print("El area del triangulo es: ", area)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')

def promedio():
    print("-------------------------------------")
    nota1 = int(input("Nota 1 alumno: "))
    nota2 = int(input("Nota 2 alumno: "))
    nota3 = int(input("Nota 3 alumno: "))
    nota4 = int(input("Nota 4 alumno: "))

    p1 = nota1 * 0.30
    p2 = nota2 * 0.25
    p3 = nota3 * 0.25
    p4 = nota4 * 0.20

    promedio = p1+p2+p3+p4
    print("El promedio del alumno es: ", promedio)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')


def perimetroArea():
    print("-------------------------------------")
    lado1 = int(input("Ingrese el primer lado del rectangulo: "))
    lado2 = int(input("Ingrese el segundo lado del rectangulo: "))
    perimetro = (lado1*2) + (lado2*2)
    area = lado1*lado2
    print("El perimetro del rectangulo de lados", lado1, "y", lado2, "es: ", perimetro)
    print("El area del rectangulo de lados", lado1, "y", lado2, "es: ", area)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')


def IMC():
    print("-------------------------------------")
    altura = float(input("Ingrese su altura: "))
    peso = float(input("Ingrese su peso: "))
    imc = round(peso/(altura)**2)
    print("El IMC de la persona que mide", altura, "y pesa", peso, "kg, es: ", imc)
    print("-------------------------------------")
    input("Para continuar presione Enter")
    os.system('cls')
IMC()
