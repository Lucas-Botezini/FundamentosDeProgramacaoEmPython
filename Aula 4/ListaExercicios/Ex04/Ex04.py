numero = int(input("Digite um número maior que 2: "))

if numero <= 2:
    print("Por favor, digite um número maior que 2.")
else:
    soma_pares = 0
    produto_impares_div_9 = 1
    soma_todos = 0
    count_todos = 0

    for i in range(2, numero + 1):
        if i % 2 == 0:  # Números pares
            print(i)
            soma_pares += i
        if i % 2 != 0 and i % 9 == 0:
            produto_impares_div_9 *= i

        soma_todos += i
        count_todos += 1

    print(f"\nSoma dos números pares: {soma_pares}")

    if produto_impares_div_9 == 1:
        print("Não existem ímpares divisíveis por 9.")
    else:
        print(f"Produto dos ímpares divisíveis por 9: {produto_impares_div_9}")

    media = soma_todos / count_todos
    print(f"Média de todos os números no intervalo: {media:.2f}")
