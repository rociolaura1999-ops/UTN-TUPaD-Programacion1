#EJERCICIO 1

notas = []

for i in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)

print("\nLista de notas:")
for n in notas:
    print(n, end=" ")
print()  

suma = 0
for n in notas:
    suma += n
promedio = suma / len(notas)
print(f"\nPromedio de notas: {promedio:.2f}")

nota_max = notas[0]
for n in notas:
    if n > nota_max:
        nota_max = n
print(f"Nota más alta: {nota_max}")

nota_min = notas[0]
for n in notas:
    if n < nota_min:
        nota_min = n
print(f"Nota más baja: {nota_min}")


#_______________________________________

#EJERCICIO 2

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

print("\nLista de productos ingresados:")
for p in productos:
    print(p)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for p in productos_ordenados:
    print(p)

producto_eliminar = input("\nIngrese el producto que desea eliminar: ")

if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"\nProducto '{producto_eliminar}' eliminado.")
else:
    print(f"\nEl producto '{producto_eliminar}' no se encuentra en la lista.")

print("\nLista actualizada de productos:")
for p in productos:
    print(p)

#_________________________________________________________

#EJERCICIO 3

import random

numeros = []
for _ in range(15):
    numeros.append(random.randint(1, 100))

print("Lista completa de números:")
for n in numeros:
    print(n, end=" ")
print("\n")  

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Números pares ({len(pares)}):")
for p in pares:
    print(p, end=" ")
print("\n")

print(f"Números impares ({len(impares)}):")
for i in impares:
    print(i, end=" ")
print()

#_____________________________________________

#EJERCICIO 4

DATOS = [1, 3, 5, 3, 7, 1, 9, 5, 3]

DATOS_sin_repetidos = []

for elemento in DATOS:
    if elemento not in DATOS_sin_repetidos:
        DATOS_sin_repetidos.append(elemento)

print("Lista sin elementos repetidos:")
for e in DATOS_sin_repetidos:
    print(e, end=" ")
print()

#_______________________________________________

#EJERCICIO 5

estudiantes = ["Ana", "Luis", "Carla", "Pedro", "María", "Javier", "Lucía", "Tomás"]

print("Lista inicial de estudiantes:")
for e in estudiantes:
    print(e)

accion = input("\n¿Desea agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\n'{nuevo}' ha sido agregado a la lista.")
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\n'{eliminar}' ha sido eliminado de la lista.")
    else:
        print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")
else:
    print("\nAcción no reconocida. No se realizaron cambios.")

print("\nLista final de estudiantes:")
for e in estudiantes:
    print(e)

#___________________________________________________

#EJERCICIO 6

estudiantes = ["Ana", "Luis", "Carla", "Pedro", "María", "Javier", "Lucía", "Tomás"]

print("Lista inicial de estudiantes:")
for e in estudiantes:
    print(e)

accion = input("\n¿Desea agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\n'{nuevo}' ha sido agregado a la lista.")
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\n'{eliminar}' ha sido eliminado de la lista.")
    else:
        print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")
else:
    print("\nAcción no reconocida. No se realizaron cambios.")

print("\nLista final de estudiantes:")
for e in estudiantes:
    print(e)

#________________________________________________

#EJERCICIO 7

temperaturas = []

for dia in range(7):
    minima = float(input(f"Ingrese la temperatura mínima del día {dia+1}: "))
    maxima = float(input(f"Ingrese la temperatura máxima del día {dia+1}: "))
    temperaturas.append([minima, maxima])

suma_min = 0
suma_max = 0
for temp in temperaturas:
    suma_min += temp[0]  
    suma_max += temp[1] 

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"\nPromedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")

mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(7):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1  

print(f"Día con mayor amplitud térmica: Día {dia_mayor_amplitud} (Amplitud: {mayor_amplitud:.2f})")

#_________________________________________________________________________________________________

#EJERCICIO 8 
notas = []

for i in range(5):
    estudiante = []
    print(f"\nIngresar notas del estudiante {i+1}:")
    for j in range(3):
        nota = float(input(f"  Nota de la materia {j+1}: "))
        estudiante.append(nota)
    notas.append(estudiante)

print("\nPromedio de cada estudiante:")
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print(f"Estudiante {i+1}: {promedio:.2f}")

print("\nPromedio de cada materia:")
for j in range(3):
    suma_materia = 0
    for i in range(5):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / 5
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#_____________________________________________________________________________

#EJERCICIO 9

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tab):
    for fila in tab:
        for casilla in fila:
            print(casilla, end=" ")
        print()
    print()  

print("Tablero inicial:")
mostrar_tablero(tablero)

turno = "X"
jugadas = 0

while jugadas < 9:
    print(f"Turno del jugador {turno}")
    
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = turno
        jugadas += 1
        mostrar_tablero(tablero)
        
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada, elija otra.\n")

#_______________________________________________________

#EJERCICIO 10

ventas = []

for i in range(4):
    producto = []
    print(f"\nIngresar ventas del producto {i+1}:")
    for j in range(7):
        cantidad = float(input(f"  Ventas del día {j+1}: "))
        producto.append(cantidad)
    ventas.append(producto)

print("\nTotal vendido por cada producto:")
totales_productos = []
for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

totales_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

mayor_ventas = max(totales_dias)
dia_mayor_ventas = totales_dias.index(mayor_ventas) + 1
print(f"\nDía con mayores ventas totales: Día {dia_mayor_ventas} (Ventas: {mayor_ventas})")

mayor_producto = max(totales_productos)
producto_mas_vendido = totales_productos.index(mayor_producto) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} (Ventas: {mayor_producto})")
