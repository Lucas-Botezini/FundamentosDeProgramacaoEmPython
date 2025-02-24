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



