def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

def main():
    # Definir una matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 5

    # Realizar la búsqueda
    resultado = buscar_en_matriz(matriz, valor_a_buscar)

    # Mostrar el resultado
    if resultado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()