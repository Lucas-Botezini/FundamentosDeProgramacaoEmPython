soma = 0

inicio = int(input("Insira o inicio: "))
final = int(input("Insira o final: "))

if inicio < final:
    for index in range(inicio, final):
        if index % 3 == 0:
            print("Multiplo de 3: ", index)
        elif (index % 2 == 0) & (index % 5 == 0):
            soma += index

print("Soma dos numeros multiplos de 5 e 2: ", soma)

