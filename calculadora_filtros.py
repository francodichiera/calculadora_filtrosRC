# FRANCO DICHIERA 5to Electronica (Evaluación - 2do Cuatrimestre - 25/11/2024)

import datetime  # Para registrar fecha y hora actuales en los datos guardados
import numpy as np  
import matplotlib.pyplot as plt 
import os  # Para verificar la existencia del archivo de datos

# Función para validar la entrada de números positivos
def validar_entrada_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número mayor a cero.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

# Función para seleccionar la escala del capacitor y convertir a Faradios
def elegir_escala_capacitor():
    while True:
        print("\nSeleccione la escala del capacitor:")
        print("1. PicoFaradios (pF)")
        print("2. NanoFaradios (nF)")
        print("3. MicroFaradios (µF)")
        print("4. MiliFaradios (mF)")
        opcion = input("Ingrese una opción (1-4): ")
        
        if opcion == "1":
            return 1e-12  # Conversión de picoFaradios a Faradios
        elif opcion == "2":
            return 1e-9   # Conversión de nanoFaradios a Faradios
        elif opcion == "3":
            return 1e-6   # Conversión de microFaradios a Faradios
        elif opcion == "4":
            return 1e-3   # Conversión de miliFaradios a Faradios
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para calcular la frecuencia de corte en Hz
def calcular_frecuencia_corte(R, C):
    return 1 / (2 * np.pi * R * C)

# Función para guardar datos en un archivo, con marca de fecha y tipo de filtro
def guardar_datos(R, C, frecuencia_corte, tipo_filtro):
    with open("filtro_datos.txt", "a") as archivo:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actuales
        archivo.write(f"{fecha}, R: {R:.2f} ohm, C: {C:.2e}F, Frecuencia de Corte: {frecuencia_corte:.2f} Hz, Tipo de filtro: {tipo_filtro}\n")

# Función para leer y mostrar los datos guardados en el archivo
def consultar_datos():
    if not os.path.exists("filtro_datos.txt"):
        print("No hay datos guardados.")
        return []
    with open("filtro_datos.txt", "r") as archivo:
        print("\nDatos guardados:")
        datos = archivo.readlines()
        for i, linea in enumerate(datos, 1):
            print(f"{i}. {linea.strip()}")
        return datos  # Devuelve los datos leídos

# Función para graficar la respuesta en frecuencia del filtro con ganancia en dB
def graficar_filtro(R, C, tipo_filtro):
    frecuencia_corte = calcular_frecuencia_corte(R, C)  # Calculamos la frecuencia de corte
    frecuencias = np.logspace(1, 5, 1000)  # Arreglo de frecuencias en escala logarítmica (10 Hz a 100,000 Hz)
    
    # Calculamos la ganancia en dB dependiendo del tipo de filtro
    if tipo_filtro.lower() == "pasa bajo":
        ganancia_lineal = 1 / np.sqrt(1 + (frecuencias / frecuencia_corte) ** 2)
    elif tipo_filtro.lower() == "pasa alto":
        ganancia_lineal = (frecuencias / frecuencia_corte) / np.sqrt(1 + (frecuencias / frecuencia_corte) ** 2)

    ganancia_db = 20 * np.log10(ganancia_lineal)  # Convertimos la ganancia a dB

    # Configuración del gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(frecuencias, ganancia_db, label=f"Filtro {tipo_filtro.capitalize()}")
    plt.axvline(frecuencia_corte, color='red', linestyle='--', label=f"Fc = {frecuencia_corte:.2f} Hz")  # Línea en frecuencia de corte
    plt.xscale("log")  # Escala logarítmica en el eje X
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Ganancia (dB)")
    plt.title(f"Respuesta en frecuencia - Filtro {tipo_filtro.capitalize()}")
    plt.legend()
    plt.grid(which="both", linestyle="--", linewidth=0.5)
    plt.show()  # Muestra el gráfico

# Función para graficar los datos guardados
def graficar_dato_guardado(dato):
    try:
        partes = dato.strip().split(", ")
        R = float(partes[1].split(":")[1].strip().replace("ohm", ""))
        C = float(partes[2].split(":")[1].strip().replace("F", ""))
        tipo_filtro = partes[4].split(":")[1].strip()
        graficar_filtro(R, C, tipo_filtro)
    except Exception as e:
        print(f"Error al procesar los datos guardados: {e}")

# Función para pedir un número válido para seleccionar un dato guardado
def seleccionar_dato_guardado(datos):
    while True:
        try:
            num = int(input("Ingrese el número de los datos que desea graficar: "))
            if num < 1 or num > len(datos):
                print(f"Por favor, ingrese un número entre 1 y {len(datos)}.")
            else:
                return num - 1  # Retorna el índice de la selección (0 basado)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")

# Menú principal del programa con colores
def menu():
    while True:
        print("\n\033[1;34m==== Franco Dichiera (TP Filtro Pasa Bajo/Pasa Alto) ====\033[0m\n")  # Azul para el título
        print("\033[1;32m1. Ingresar valores de R y C\033[0m")  # Verde para opción 1
        print("\033[1;33m2. Consultar valores guardados\033[0m")  # Amarillo para opción 2
        print("\033[1;35m3. Graficar filtro de datos guardados\033[0m")  # Violeta para opción 3
        print("\033[1;31m4. Salir\033[0m")  # Rojo para opción 4
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                tipo_filtro = input("Seleccione el tipo de filtro (pasa bajo/pasa alto): ").strip().lower()
                if tipo_filtro in ["pasa bajo", "pasa alto"]:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

            R = validar_entrada_float("Ingrese el valor de R en ohms: ")
            escala_C = elegir_escala_capacitor()
            C_valor = validar_entrada_float("Ingrese el valor de C en la escala seleccionada: ")
            C = C_valor * escala_C
            frecuencia_corte = calcular_frecuencia_corte(R, C)
            print(f"Frecuencia de corte calculada: {frecuencia_corte:.2f} Hz")
            guardar_datos(R, C, frecuencia_corte, tipo_filtro)
            graficar_filtro(R, C, tipo_filtro)

        elif opcion == "2":
            datos = consultar_datos()

        elif opcion == "3":
            datos = consultar_datos()
            if datos:
                num = seleccionar_dato_guardado(datos)
                graficar_dato_guardado(datos[num])

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("\033[1;31mOpción no válida. Intente de nuevo.\033[0m")

# Ejecución del programa principal
menu()


