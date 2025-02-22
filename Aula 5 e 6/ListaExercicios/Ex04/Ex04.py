##Fatorial
def fatorial(n):
    if n < 0:
        return "Erro! O fatorial não existe para números negativos."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = 5
print(f"O fatorial de {numero} é: {fatorial(numero)}")