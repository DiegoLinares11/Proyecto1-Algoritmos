from Reader import Reader
from MT import MT

reader = Reader("MT/transformadora.yml")
# reader.printData()

mt = MT(reader.states, reader.initial_state, reader.final_state, reader.alphabet, reader.tape_alphabet, reader.function, machine_type= reader.machine_type)

for input_string in reader.simulation_strings:
    print(f"\nSimulando cadena: {input_string}")
    mt.initializeTape(input_string)
    
    if reader.machine_type == "reconocedora":
        if mt.simulateMT():
            print(f"Cadena {input_string} aceptada.")
        else:
            print(f"Cadena {input_string} rechazada.")
    elif reader.machine_type == "transformadora":
        mt.simulateMT() #No se trata de aceptar ni rechazar.

