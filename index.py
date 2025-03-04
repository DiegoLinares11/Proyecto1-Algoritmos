import time
import csv
from Reader import Reader
from MT import MT

# Cargar configuración desde YAML
reader = Reader("MT/transformadora.yml")
mt = MT(
    reader.states,
    reader.initial_state,
    reader.final_state,
    reader.alphabet,
    reader.tape_alphabet,
    reader.function,
    machine_type=reader.machine_type
)

# Abrir archivo CSV para guardar resultados (se agregan columnas para entrada, salida unaria y salida decimal)
with open('resultados_simulacion.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Cadena de entrada', 'Tiempo (s)', 'Salida (unaria)', 'Salida (decimal)'])

    # Para cada cadena de simulación definida en el YAML
    for input_string in reader.simulation_strings:
                # Decodificar la entrada: si es "Z", se interpreta como 0; de lo contrario, se cuenta la longitud.
        if input_string == "Z":
            input_decimal = 0
        else:
            input_decimal = len(input_string)
            
        print(f"\nCadena de entrada: {input_string}")
        print(f"Cadena de entrada (decimal): {input_decimal}")
        mt.initializeTape(input_string)
        start_time = time.perf_counter()
        mt.simulateMT()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        # Convertir la cinta final a una cadena (ignorando los blanks)
        output = "".join([char for char in mt.tape if char != "B"])
        
        # Decodificar la salida: si es "Z", se interpreta como 0; de lo contrario, se cuenta la longitud.
        if output == "Z":
            decimal_value = 0
        else:
            decimal_value = len(output)
        
        print(f"Salida (unaria): {output}")
        print(f"Salida (decimal): {decimal_value}")
        print(f"Tiempo: {elapsed_time:.6f} segundos")
        
        csv_writer.writerow([input_string, input_decimal, elapsed_time, output, decimal_value])
