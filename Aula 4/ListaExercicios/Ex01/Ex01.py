numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for index in numeros:
    if index % 2 == 0:
        print("Par :", index)
    else:
        soma += index

print("Soma dos ímpares: ", soma)