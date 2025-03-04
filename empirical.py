import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

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

# Función para determinar la mejor regresión
def best_fit(x, y, max_degree=5):
    best_r2 = -np.inf
    best_poly = None
    best_degree = 0
    for degree in range(1, max_degree + 1):
        coeffs = np.polyfit(x, y, degree)
        poly = np.poly1d(coeffs)
        y_pred = poly(x)
        r2 = r2_score(y, y_pred)
        if r2 > best_r2:
            best_r2 = r2
            best_poly = poly
            best_degree = degree
    return best_poly, best_degree

# Determinar la mejor regresión para cada conjunto de datos
trend_poly_time_output, degree_time_output = best_fit(output_decoded, times)
trend_poly_time_input, degree_time_input = best_fit(input_decimals, times)
trend_poly_output_input, degree_output_input = best_fit(input_decimals, output_decoded)

# Generar puntos para la línea de ajuste
x_line_output = np.linspace(min(output_decoded), max(output_decoded), 100)
y_line_output = trend_poly_time_output(x_line_output)

x_line_input = np.linspace(min(input_decimals), max(input_decimals), 100)
y_line_input = trend_poly_time_input(x_line_input)

y_line_output_input = trend_poly_output_input(x_line_input)

# Crear el gráfico de dispersión con línea de ajuste
plt.figure(figsize=(8, 6))
plt.scatter(output_decoded, times, color='blue', marker='o', label="Datos")
plt.plot(x_line_output, y_line_output, color='red', label=f"Ajuste polinómico (grado {degree_time_output})")
plt.title("Salida Decodificada vs Tiempo de Ejecución")
plt.xlabel("Salida Decodificada (valor decimal)")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Tiempo de Ejecución
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, times, color='blue', marker='o', label="Datos")
plt.plot(x_line_input, y_line_input, color='red', label=f"Ajuste polinómico (grado {degree_time_input})")
plt.title("Entrada (decimal) vs Tiempo de Ejecución")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Salida (decimal)
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, output_decoded, color='green', marker='o', label="Datos")
plt.plot(x_line_input, y_line_output_input, color='red', label=f"Ajuste polinómico (grado {degree_output_input})")
plt.title("Entrada (decimal) vs Salida (decimal)")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Salida (decimal)")
plt.grid(True)
plt.legend()
plt.show()

# Crear el gráfico de Entrada (decimal) vs Salida (decimal) en escala logarítmica
plt.figure(figsize=(8, 6))
plt.scatter(input_decimals, output_decoded, color='purple', marker='o', label="Datos")
plt.plot(x_line_input, y_line_output_input, color='red', label=f"Ajuste polinómico (grado {degree_output_input})")
plt.yscale("log")
plt.title("Entrada (decimal) vs Salida (decimal) (Escala Log)")
plt.xlabel("Entrada (decimal)")
plt.ylabel("Salida (decimal)")
plt.grid(True)
plt.legend()
plt.show()

# Imprimimos los valores de ajuste
print(f"Mejor ajuste Salida-Tiempo: Grado {degree_time_output}, Función: {trend_poly_time_output}")
print(f"Mejor ajuste Entrada-Tiempo: Grado {degree_time_input}, Función: {trend_poly_time_input}")
print(f"Mejor ajuste Entrada-Salida: Grado {degree_output_input}, Función: {trend_poly_output_input}")