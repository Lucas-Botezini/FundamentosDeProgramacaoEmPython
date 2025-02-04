# Exercício 1 - Adivinhe um número aleatório escolhido pelo computador.
# Dica: utilize biblioteca "random" do python para esse exercício

import random
from numbers import Number

n1 = random.randint(0, 10)
nTentativas = 1

print("=== Acerte o número escolhido pelo computador ===")
guess = int(input("Digite o número: "))

while guess != n1:
    print("Número incorreto!")

    if n1 > guess:
        print("Número escolhido pelo computador é maior que a sua escolha: ")
    elif n1 < guess:
        print("Número escolhido pelo computador é menor que a sua escolha: ")

    guess = int(input("\nDigite o número: "))
    nTentativas += 1

print(f"\n\nVocê acertou !!! Número de tentativas: {nTentativas}. O número escolhido pelo computador é: {n1}")