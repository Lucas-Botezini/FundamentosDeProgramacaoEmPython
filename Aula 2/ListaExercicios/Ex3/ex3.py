# 3) Um professor atribui pesos de 1 a 3 para as notas de três avaliações, respectivamente.
# Faça um programa que receba o nome do aluno, as notas e calcule e mostre a média ponderada junto ao nome do aluno.
# A média e as notas são valores do tipo float.
# Média Ponderada = (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3)

# Desafio: Pesquise uma forma de exibir somente dois números decimais no momento da impressão da média

aluno = input("Qual o nome do aluno? ")

nota = 1
n1 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n2 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n3 = float(input(f"Informe a nota número {nota}: "))

media = (n1 * 1 + n2 * 2 + n3 * 3)/(1+2+3)
print(f"A média ponderada do aluno {aluno} é: {media}")

