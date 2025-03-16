def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

def main():
    # Definir una matriz 3x3
    matriz = [
        [9, 8, 7],
        [5, 6, 4],
        [3, 2, 1]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Fila a ordenar (0-based index)
    fila_a_ordenar = 1

    # Ordenar la fila específica
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()