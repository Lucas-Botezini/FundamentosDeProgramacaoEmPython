# Crie duas matrizes, e some elas.
def soma_matrizes(matriz1, matriz2):
    # Verifica se as matrizes têm as mesmas dimensões
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "As matrizes devem ter as mesmas dimensões para a soma."

    resultado = []
    for i in range(len(matriz1)):
        linha_resultado = []
        for j in range(len(matriz1[0])):
            linha_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha_resultado)
    return resultado

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

soma = soma_matrizes(matriz1, matriz2)
print("Soma das Matrizes:")
for linha in soma:
    print(linha)