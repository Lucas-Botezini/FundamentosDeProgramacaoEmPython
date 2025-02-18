# Exercício 2) Ler dois números inteiros e informar: a) Se ambos são divisíveis por 5. b) Se pelo menos um deles é divisível por 5. c) Se ambos são pares. d) Se ambos são ímpares. e) Se pelo menos um deles é ímpar.

num1 = int(input())
num2 = int(input())

if num1 % 5 == 0 and num2 % 5 == 0:
    print("Os dois números são divisíveis por 5")
else:
    if num1 % 5 == 0 or num2 % 5 == 0:
        print("Um dos números é divisível por 5")
    else:
        print("Nenhum dos números é divisível por 5")

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos são pares")
else:
    if num1 % 2 != 0 and num2 % 2 != 0:
        print("Ambos são ímpares")
    else:
        if num1 % 2 != 0 or num2 % 2 != 0:
            print("Um dos números é ímpar")
