import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Listas para almacenar los datos
input_decimals = []
output_decoded = []
times = []

# Abrir y leer el archivo CSV
with open("resultados_simulacion.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Saltar la cabecera
    # Se asume que las columnas son: 
    # [0]: Cadena entrada (unaria)
    # [1]: Cadena entrada (decimal)
    # [2]: Tiempo (s)
    # [3]: Salida (unaria)
    # [4]: Salida (decimal)
    for row in reader:
        input_decimals.append(float(row[1]))
        times.append(float(row[2]))
        output_decoded.append(float(row[4]))

# Convertir a arrays de NumPy
times = np.array(times)
output_decoded = np.array(output_decoded)
input_decimals = np.array(input_decimals)

# Ajuste polinómico de grado 2
degree = 2
coeffs = np.polyfit(output_decoded, times, degree)
trend_poly = np.poly1d(coeffs)

# Generar puntos para la línea de ajuste
x_line = np.linspace(min(output_decoded), max(output_decoded), 100)
y_line = trend_poly(x_line)

# Crear el gráfico de dispersión con línea de ajuste
plt.figure(figsize=(8, 6))
plt.scatter(output_decoded, times, color='blue', marker='o', label="Datos")
plt.plot(x_line, y_line, color='red', label=f"Ajuste polinómico (grado {degree})")
plt.title("Salida Decodificada vs Tiempo de Ejecución")
plt.xlabel("Salida Decodificada (valor decimal)")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Tiempo de Ejecución
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, times, color='blue', marker='o', label="Datos")
plt.title("Entrada (decimal) vs Tiempo de Ejecución")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Salida (decimal)
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, output_decoded, color='green', marker='o', label="Datos")
plt.title("Entrada (decimal) vs Salida (decimal)")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Salida (decimal)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Salida (decimal) en escala logarítmica
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, output_decoded, color='purple', marker='o', label="Datos")
plt.yscale("log")
plt.title("Entrada (decimal) vs Salida (decimal) (Escala Log)")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Salida (decimal)")
plt.grid(True)
plt.legend()
plt.show()

# Imprimimos los valores de ajuste
print(f"Ajuste obtenido: T(n) ≈ {coeffs[0]:.2f}n^2 + {coeffs[1]:.2f}n + {coeffs[2]:.2f}")
