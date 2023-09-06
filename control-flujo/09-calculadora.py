print("Bienvenidos a la calculadora")
print("Para salir escribe 'salir'")
print("Las operaciones son suma, resta, multi y div")

resultado = ""  # Initialize the resultado as an integer

while True:
    resultado = input("Ingrese numero: ")
    if resultado.lower() == "salir":
        break

    # Input for the operation
    op = input("Ingrese operacion: ").lower()
    
    if op == "salir":
        break
    
    # Input for the next number
    n2 = input("Ingrese siguiente numero: ")
    
    if n2.lower() == "salir":
        break
    
    n2 = float(n2)  # Convert n2 to a float to handle decimal values

    if op == "suma":
        resultado += n2
    elif op == "resta":
        resultado -= n2
    elif op == "multi":
        resultado *= n2
    elif op == "div":
        if n2 == 0:
            print("No se puede dividir por cero.")
        else:
            resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es {resultado}")
