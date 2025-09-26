#EJERCICIO 1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#__________________________________________________-

#EJERCICIO 2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#___________________________________________________

#EJERCICIO 3

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#____________________________________________________

#EJERCICIO 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#____________________________________________________

#EJERCICIO 5

contraseña = input("Ingrese su contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#______________________________________________________

#EJERCICIO 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media:.2f}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#______________________________________________________

#EJERCICIO 7

texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)

#________________________________________________________

#EJERCICIO 8

nombre = input("Ingrese su nombre: ")

opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: ")

if opcion == "1":
    print(nombre.upper())   
elif opcion == "2":
    print(nombre.lower())  
elif opcion == "3":
    print(nombre.title())  
else:
    print("Opción inválida. Por favor ingrese 1, 2 o 3.")

#_________________________________________________________

#Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))


if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  
    print("Extremo (puede causar graves daños a gran escala)")

#__________________________________________________________

#Ejercicio 10

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))


if hemisferio == "N":  
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:  
        estacion = "Otoño"
elif hemisferio == "S": 
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:  
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print(f"En el hemisferio {hemisferio}, la estación actual es: {estacion}")