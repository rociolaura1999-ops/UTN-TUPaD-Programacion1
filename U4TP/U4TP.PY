
# EJERCICIO 1

for numero in range(0, 101): 
    print(numero)

#____________________________________

#EJERCICIO 2

numero = input("Ingrese un número entero: ")

cantidad_digitos = len(numero_sin_signo)

print(f"El número tiene {cantidad_digitos} dígitos.")

#____________________________________

#EJERCICIO 3

inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0

for numero in range(inicio + 1, fin):
    suma += numero

print(f"La suma de los números entre {inicio} y {fin} (excluyendo los extremos) es: {suma}")

#______________________________________

#EJERCICIO 4 

suma_total = 0  

while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))
    
    if numero == 0:
        break      
    suma_total += numero  

print(f"La suma total de los números ingresados es: {suma_total}")

#__________________________________________________

#EJERCICIO 5

numero_secreto = random.randint(0, 9)

intentos = 0
acertado = False

print("Adivina el número (entre 0 y 9)")

while not acertado:
    numero_usuario = int(input("Ingrese su número: "))
    intentos += 1
    
    if numero_usuario == numero_secreto:
        acertado = True
      
 print(f" Adivinaste el número {numero_secreto} en {intentos} intentos.")
    else:
        print(" No es el número, intenta de nuevo.")
#____________________________________________________

#EJERCICIO 6

numero=(INT(input"Ingrese un numero: "))

for numero in range(100, -1, -2): 
    print(numero)

#_____________________________________________________

#EJERCICIO 7

n = int(input("Ingrese un número: "))

suma = 0
for i in range(n + 1):  
    suma += i

print("La suma de los números de 0 a", n, "es:", suma)

#_______________________________________________________

#EJERCICIO 8

N = 100  
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(N):
    numero = int(input(f"Ingrese el número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

#_______________________________________________________________

#EJERCICIO 9

N = 100  
suma = 0

for i in range(N):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / N

print("La media de los", N, "números ingresados es:", media)

#____________________________________________________________

#EJERCICIO 10

numero = input("Ingrese un número entero: ")

invertido = numero[::-1] 

print("El número invertido es:", invertido)



