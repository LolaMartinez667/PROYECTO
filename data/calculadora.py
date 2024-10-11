def calculos(operador, num1, num2, historial):
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "/":
        resultado = num1 / num2
    elif operador == "*":
        resultado = num1 * num2
    else:
        return print("Operacion no valida")
    operacion = (f"{num1} {operador} {num2} = {resultado}")
    guardar_operacion(operacion)
    return operacion
def guardar_operacion(operacion):
    with open("historial.txt", "a") as historial:
        historial.write(operacion + "/n")
def mostrar_historial():
    try:
        with open("historial.txt", "r") as historial:
            return historial.read()
    except:
        return "El historial esta vacio"
def calculadora():
    historial = []

    while True:
        print("\n1.Suma")
        print("2.Resta")
        print("3.Dividir")
        print("4.Multiplicar")
        print("5.Ver historial")
        print("6.Salir")
        opcion = input("Elige una opcion: ")

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer numero: "))
                num2 = float(input("Ingrese el segundo numero: "))
                
                if opcion == "1":
                    operador = "+"
                elif opcion == "2":
                    operador = "-"
                elif opcion == "3":
                    operador = "/"
                elif opcion == "4":
                    operador = "*"
                print(calculos(operador, num1, num2, historial))
                continue
            except:
                print("Por favor ingrese numeros.")
        elif opcion == "5":
            print("\nHistorial de operaciones:")
            print(mostrar_historial())
        elif opcion == "6":
            print("Saliste de la calculadora")
            break
        else:
            print("Opcion invalida")

    

