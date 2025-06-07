import os
import random
import time
from busquedaBinaria import busqueda_binaria
from busquedaSecuencial import busqueda_secuencial
from ordenamientoBurbuja import ordenamiento_burbuja
from ordenamientoQuicksort import ordenamiento_quick

def generar_estudiantes(n):
    nombres = [
        "Ana", "Luis", "Carlos", "María", "Jorge", "Sofía", "Pedro", "Valentina", "Martín", "Camila",
        "Lucía", "Mateo", "Paula", "Diego", "Julieta", "Agustín", "Micaela", "Tomás", "Florencia", "Santiago",
        "Emilia", "Benjamín", "Victoria", "Juan", "Josefina", "Lucas", "Milagros", "Facundo", "Rocío", "Nicolás",
        "Malena", "Gabriel", "Renata", "Franco", "Martina", "Simón", "Guadalupe", "Ramiro", "Lara", "Axel",
        "Candelaria", "Bruno", "Ailén", "Iván", "Abril", "Federico", "Luz", "Sebastián", "Bianca", "Gonzalo",
        "Ariana", "Matías", "Elena", "Leandro", "Agustina", "Delfina", "Maximiliano", "Carolina", "Emmanuel", "Sol",
        "Valeria", "Ignacio", "Celeste", "Esteban", "Juliana", "Lautaro", "Pilar", "Thiago", "Aitana", "Ezequiel",
        "Mara", "Lisandro", "Ariadna", "Damián", "Aldana", "Joaquín", "Catalina", "Alan", "Mara", "Enzo",
        "Noelia", "Ulises", "Tamara", "Kevin", "Melina", "Oscar", "Aixa", "Ricardo", "Brenda", "Eduardo",
        "Selena", "Raúl", "Miriam", "Hugo", "Patricia", "Rubén", "Lorena", "Marcos", "Daniela", "Fernando"
    ]
    estudiantes = [(random.choice(nombres), round(random.uniform(0.0, 10.0), 1)) for _ in range(n)]
    return estudiantes

def busqueda(lista, lista_ordenada):
    dato = input("Ingrese el nombre del estudiante a buscar: ")
    respuesta = None
    if (len(lista_ordenada) == 0):
        respuesta = busqueda_secuencial(lista, dato)
    else:
        respuesta = busqueda_binaria(lista_ordenada, dato)
    return respuesta

def ordenar(lista, lista_ordenada):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seleccione el método de ordenamiento:")
        print("1. Descendente (Burbuja)")
        print("2. Ascendente (Quicksort)")
        print("3. Atrás")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            inicio = time.time()
            lista_ordenada = ordenamiento_burbuja(lista)
            fin = time.time()
            print(f"Demora: {fin - inicio:.6f} segundos")
            break
        elif opcion == "2":
            inicio = time.time()
            lista_ordenada = ordenamiento_quick(lista)
            fin = time.time()
            print(f"Demora: {fin - inicio:.6f} segundos")
            break
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")
    
    return lista_ordenada

n = 100  # Número de estudiantes a generar
estudiantes = generar_estudiantes(n)
lista_ordenada = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------")
    print("TP INTEGRADOR PROGRAMACIÓN I - BUSQUEDA Y ORDENAMIENTO")
    print("------------------------------------------")
    print("1. Busqueda")
    print("2. Ordenamiento")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dato = busqueda(estudiantes, lista_ordenada)
        if dato is not None:
            print(f"Estudiante encontrado:\nNombre: {dato[0]}, Nota: {dato[1]}")
            input("Presione Enter para continuar...")
        else:
            print("Estudiante no encontrado.")
    elif opcion == "2":
        lista_ordenada = ordenar(estudiantes, lista_ordenada)
        input("Presione Enter para continuar...")
    elif opcion == "3":
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
