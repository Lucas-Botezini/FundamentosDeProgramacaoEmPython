# 3) Um professor atribui pesos de 1 a 3 para as notas de três avaliações, respectivamente. Faça um programa que receba as notas e calcule e mostre a média ponderada. A média e as notas serão valores do tipo float.
# Média Ponderada = (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3)

nota = 1
n1 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n2 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n3 = float(input(f"Informe a nota número {nota}: "))

media = (n1 * 1 + n2 * 2 + n3 * 3)/(1+2+3)
print(f"Media ponderada: {media}")