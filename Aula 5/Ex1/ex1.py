# 1)  Fazer  uma  função  para  verificar  se  um  número  é  ou  não  primo. Elaborar um programa para usar essa função para:
# a) Verificar se um número informado pelo usuário é  ou não um número  primo. Validar a entrada para que o
# usuário informe um número positivo.

def ehPrimo (num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n1 = int(input("Informe um número para verificar se é primo: "))

if (ehPrimo(n1)):
    print(f"Numero ({n1}) é primo")
else:
    print(f"Numero ({n1}) não é primo")