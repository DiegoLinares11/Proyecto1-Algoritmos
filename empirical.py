import csv
import numpy as np
import matplotlib.pyplot as plt

# Listas para almacenar los datos
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
        times.append(float(row[2]))
        output_decoded.append(float(row[4]))

# Convertir a arrays de NumPy
times = np.array(times)
output_decoded = np.array(output_decoded)

# Ajuste polinómico de grado 2 (puedes cambiar el grado según lo que mejor se acople)
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
