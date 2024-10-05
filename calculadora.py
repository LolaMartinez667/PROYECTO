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
    historial.append(operacion)
    return operacion
def mostrar_historial(historial):
    return "/n".join(historial)
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
        if opcion == "5":
            print("\nHistorial de operaciones:")
            print(mostrar_historial(historial))
        elif opcion == "6":
            print("Saliste de la calculadora")
            break
        else:
            print("Opcion invalida")
if __name__ == "__main__":
    calculadora()
    

