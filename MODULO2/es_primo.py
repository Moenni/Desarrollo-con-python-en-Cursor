def es_Primo(valor):
    if not isinstance(valor, int):
        return None
    #Los numeros menores o igual a 1 no son primos
    if valor <= 1:
        return False
    #verificamos si tiene divisores de 1 y de si mismo
    for i in range(2,int( valor**0.5)+1):
        if valor % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        entrada = input("Ingresa un número entero: ")
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
    else:
        resultado = es_Primo(numero)
        if resultado is None:
            print("El valor no es un entero.")
        elif resultado:
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")
