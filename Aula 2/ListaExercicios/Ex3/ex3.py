aluno = input("Qual o nome do aluno? ")

nota = 1
n1 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n2 = float(input(f"Informe a nota número {nota}: "))

nota+=1
n3 = float(input(f"Informe a nota número {nota}: "))

media = (n1 * 1 + n2 * 2 + n3 * 3)/(1+2+3)
print(f"A média ponderada do aluno {aluno} é: {media}")

