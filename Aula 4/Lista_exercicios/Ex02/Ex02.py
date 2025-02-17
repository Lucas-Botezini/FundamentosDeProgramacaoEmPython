## Faça um loop que receba de um input um início e um final, verifique se o incio é menor que o final
## percorra esse intervalo, imprima os multiplos de 3, e some todos os numeros que são
## multiplos de 5 e 2 ao mesmo tempo.

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

