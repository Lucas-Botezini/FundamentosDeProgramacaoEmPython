# 4) Tendo como entrada dois valores inteiros, elaborar um programa para calcular e mostrar:
# a) A soma desses valores
# b) A subtração do primeiro pelo segundo
# c) A multiplicação entre eles
# d) A divisão inteira do primeiro pelo segundo
# e) A divisão float do primeiro pelo segundo
# f) O resto da divisão do primeiro pelo segundo.

n1 = float(input(f"Digite o primeiro numero: "))
n2 = float(input(f"Digite o segundo numero: "))

# Adicao
calc = n1 + n2
print("\n%d + %d = %d", n1, n2, calc)

# Subtracao
calc = n1 - n2
print("\n%d - %d = %d", n1, n2, calc)

# Multiplicao
calc = n1 * n2
print("\n%d * %d = %d", n1, n2, calc)

# Divisao
calc = n1 / n2
print("\n%d / %d = %d", n1, n2, calc)

# Divisao
calcu = n1 / n2
print("\n%d / %d = %.2f", n1, n2, calcu)

# Resto
calc = n1 % n2
print("\n%d %% %d = %d", n1, n2, calc)


