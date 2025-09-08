
#Definimos las funciones matemáticas
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b==0:
        return "Error: División por cero"
    return a / b

#Creamos un diccionario con las funciones
operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}

#Creamos el bucle principal
while True:
    operacion = input("Ingrese la operación: ").lower()
    if operacion == "salir":
        print("Saliendo de la calculadora")
        break
    if operacion not in operaciones:
        print("Operacion no valida")
        continue
    
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
    except ValueError:
        print("Error: Ingrese numeros validos")
        continue
    resultado = operaciones[operacion](num1, num2)
    print(f"El resultado de la {operacion} es: {resultado}")
    
        