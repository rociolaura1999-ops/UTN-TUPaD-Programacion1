#HOLA MUNDO
print ("Hola mundo!")

#_________________________________________________

#SALUDO NOMBRE
nombre = input ("Como te llamas?")
print("Hola ",nombre)

#__________________________________________________

#SALUDOS DATOS

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("¿Cuantos años tenes?: ")
lugar = input("¿Donde vivis?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#____________________________________________________

#AREA

import math  


radio = float(input("Ingresa el radio del círculo: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#_______________________________________________________

#HORAS

segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#_________________________________________________________

#TABLA MULTIPLICAR

numero = int(input("Ingresa un número: "))


print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#___________________________________________________________

#OPERACIONES

num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
 
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2   


print(f"\nResultados con {num1} y {num2}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")

#______________________________________________________________

#IMC

altura = float(input("Ingrese aquí su altura en metros: "))
peso = float(input("Ingrese aquí su peso en kilogramos: "))

imc = peso / (altura ** 2)


print(f"Su Índice de Masa Corporal (IMC) es de {imc:.2f}")

#__________________________________________________________________

#Fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#___________________________________________________________________

#Promedio

nota1= input("Ingrese la nota aqui:")
nota2= input("Ingrese la nota aqui")
nota3= input("Ingrese la nota aqui")

Prom = (nota1 + nota2 + nota3) /3

print ("Su promedio es de ",Prom)
