# 

# \# Calculadora filtros RC – Pasa Bajo / Pasa Alto

# 

# \*\*Autor:\*\* Franco Dichiera

# 

# Este programa en Python permite:

# 

# \-   🔢 Calcular la frecuencia de corte de filtros RC pasa bajo y pasa alto.

# &nbsp;   

# \-   💾 Guardar los cálculos realizados en un archivo de texto con fecha y hora.

# &nbsp;   

# \-   📂 Consultar los datos guardados previamente.

# &nbsp;   

# \-   📊 Graficar la respuesta en frecuencia (ganancia en dB) del filtro seleccionado.

# &nbsp;   

# 

# ----------

# 

# \## \*\*Requisitos\*\*

# 

# \-   🐍 Python 3.8 o superior

# &nbsp;   

# \-   📦 Librerías necesarias:

# &nbsp;   

# &nbsp;   `pip install numpy matplotlib` 

# &nbsp;   

# 

# ----------

# 

# \## \*\*Características principales\*\*

# 

# 1\.  \*\*Cálculo interactivo\*\* ✏️

# &nbsp;   

# &nbsp;   -   Permite ingresar valores de resistencia (R) y capacitancia (C) en diferentes escalas (pF, nF, µF, mF).

# &nbsp;       

# &nbsp;   -   Calcula automáticamente la frecuencia de corte:  $$ f\_c = \\dfrac{1}{2 \\pi R C} $$

# 

# &nbsp;   -   Soporta filtros \*\*pasa bajo\*\* y \*\*pasa alto\*\*.

# &nbsp;       

# 2\.  \*\*Almacenamiento de resultados\*\* 💾

# &nbsp;   

# &nbsp;   -   Guarda cada cálculo en un archivo `filtro\_datos.txt` con la siguiente información:

# &nbsp;       

# &nbsp;       -   Fecha y hora del cálculo

# &nbsp;           

# &nbsp;       -   Valor de R y C

# &nbsp;           

# &nbsp;       -   Frecuencia de corte calculada

# &nbsp;           

# &nbsp;       -   Tipo de filtro seleccionado

# &nbsp;           

# 3\.  \*\*Consulta y graficado\*\* 📊

# &nbsp;   

# &nbsp;   -   Muestra la lista de datos previamente guardados.

# &nbsp;       

# &nbsp;   -   Permite seleccionar un cálculo y graficar su respuesta en frecuencia.

# &nbsp;       

# &nbsp;   -   Los gráficos muestran:

# &nbsp;       

# &nbsp;       -   La curva de ganancia (en dB)

# &nbsp;           

# &nbsp;       -   La frecuencia de corte marcada con una línea roja discontinua

# &nbsp;           

# &nbsp;       -   Escala logarítmica en el eje X (frecuencia)

# &nbsp;           

# 4\.  \*\*Interfaz de texto con colores\*\* 🎨

# &nbsp;   

# &nbsp;   -   Las opciones del menú se muestran con diferentes colores para facilitar su uso.

# &nbsp;       

# 

# ----------

# 

# \## \*\*Uso del programa\*\*

# 

# 1\.  Ejecuta el programa:

# &nbsp;   

# &nbsp;   `python filtro\_rc.py` 

# &nbsp;   

# 2\.  En el menú principal:

# &nbsp;   

# &nbsp;   -   \*\*Opción 1\*\* – Ingresar valores de R y C, calcular frecuencia de corte y graficar.

# &nbsp;       

# &nbsp;   -   \*\*Opción 2\*\* – Consultar los valores guardados.

# &nbsp;       

# &nbsp;   -   \*\*Opción 3\*\* – Seleccionar un dato guardado y graficar su respuesta.

# &nbsp;       

# &nbsp;   -   \*\*Opción 4\*\* – Salir del programa.

# &nbsp;       

# 3\.  Ejemplo de flujo:

# &nbsp;   

# &nbsp;   -   Seleccionar filtro \*\*pasa bajo\*\*

# &nbsp;       

# &nbsp;   -   Ingresar R = 1000 Ω

# &nbsp;       

# &nbsp;   -   Seleccionar escala \*\*µF\*\* e ingresar C = 0.1

# &nbsp;       

# &nbsp;   -   Se calcula y muestra la frecuencia de corte, se guarda y grafica automáticamente.

# &nbsp;       

# 

# ----------

# 

# \## \*\*Archivos generados\*\*

# 

# \-   `calculadora\_filtroRC.py` → Script principal.

# &nbsp;   

# \-   `filtro\_datos.txt` → Archivo de texto donde se almacenan los cálculos realizados.

# &nbsp;   

# 

# ----------



