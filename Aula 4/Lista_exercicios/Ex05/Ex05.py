#Exercício 5) Ler uma série de números indicados pelo usuário até ser informado o valor zero. Encontrar e mostrar o maior e o menor dos valores informados pelo usuário. O valor zero indica o final da leitura e não deve ser considerado.
maior = 0
menor = 0

while True:
    numero = int(input("Digite um número (digite 0 para parar): "))

    if numero == 0:
        break

    if maior == 0 and menor == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

if maior != 0 and menor != 0:
    print(f"O maior número informado foi: {maior}")
    print(f"O menor número informado foi: {menor}")
else:
    print("Nenhum número válido foi informado.")
