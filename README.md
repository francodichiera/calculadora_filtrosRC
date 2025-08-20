
# Calculadora filtros RC – Pasa Bajo / Pasa Alto

**Autor:** Franco Dichiera

Este programa en Python permite:

-   🔢 Calcular la frecuencia de corte de filtros RC pasa bajo y pasa alto.
    
-   💾 Guardar los cálculos realizados en un archivo de texto con fecha y hora.
    
-   📂 Consultar los datos guardados previamente.
    
-   📊 Graficar la respuesta en frecuencia (ganancia en dB) del filtro seleccionado.
    

----------

## **Requisitos**

-   🐍 Python 3.8 o superior
    
-   📦 Librerías necesarias:
    
    `pip install numpy matplotlib` 
    

----------

## **Características principales**

1.  **Cálculo interactivo** ✏️
    
    -   Permite ingresar valores de resistencia (R) y capacitancia (C) en diferentes escalas (pF, nF, µF, mF).
        
    -   Calcula automáticamente la frecuencia de corte:  $$ f_c = \dfrac{1}{2 \pi R C} $$

    -   Soporta filtros **pasa bajo** y **pasa alto**.
        
2.  **Almacenamiento de resultados** 💾
    
    -   Guarda cada cálculo en un archivo `filtro_datos.txt` con la siguiente información:
        
        -   Fecha y hora del cálculo
            
        -   Valor de R y C
            
        -   Frecuencia de corte calculada
            
        -   Tipo de filtro seleccionado
            
3.  **Consulta y graficado** 📊
    
    -   Muestra la lista de datos previamente guardados.
        
    -   Permite seleccionar un cálculo y graficar su respuesta en frecuencia.
        
    -   Los gráficos muestran:
        
        -   La curva de ganancia (en dB)
            
        -   La frecuencia de corte marcada con una línea roja discontinua
            
        -   Escala logarítmica en el eje X (frecuencia)
            
4.  **Interfaz de texto con colores** 🎨
    
    -   Las opciones del menú se muestran con diferentes colores para facilitar su uso.
        

----------

## **Uso del programa**

1.  Ejecuta el programa:
    
    `python filtro_rc.py` 
    
2.  En el menú principal:
    
    -   **Opción 1** – Ingresar valores de R y C, calcular frecuencia de corte y graficar.
        
    -   **Opción 2** – Consultar los valores guardados.
        
    -   **Opción 3** – Seleccionar un dato guardado y graficar su respuesta.
        
    -   **Opción 4** – Salir del programa.
        
3.  Ejemplo de flujo:
    
    -   Seleccionar filtro **pasa bajo**
        
    -   Ingresar R = 1000 Ω
        
    -   Seleccionar escala **µF** e ingresar C = 0.1
        
    -   Se calcula y muestra la frecuencia de corte, se guarda y grafica automáticamente.
        

----------

## **Archivos generados**

-   `calculadora_filtroRC.py` → Script principal.
    
-   `filtro_datos.txt` → Archivo de texto donde se almacenan los cálculos realizados.
    
