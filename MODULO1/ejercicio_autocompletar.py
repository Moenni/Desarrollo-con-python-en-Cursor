def cuadrados_de_los_primeros_n(n: int) -> list[int]:
    """Devuelve una lista con los cuadrados de los primeros n números naturales (1..n).

    Args:
        n: Entero mayor o igual a 0.

    Returns:
        Lista de enteros con los cuadrados desde 1^2 hasta n^2.

    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("n debe ser un entero mayor o igual a 0")
    return [i * i for i in range(1, n + 1)]


if __name__ == "__main__":
    try:
        entrada = input("Ingrese n (entero >= 0): ")
        n = int(entrada.strip())
        resultado = cuadrados_de_los_primeros_n(n)
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")


    