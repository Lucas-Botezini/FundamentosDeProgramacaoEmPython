# Exercício 3) O Índice de Massa Corporal (IMC) é uma fórmula que indica se um adulto está acima do peso,
# se está  obeso  ou  abaixo  do  peso  ideal  considerado  saudável.
# A  fórmula  para  calcular  o  Índice  de  Massa Corporal  é:  IMC  =  peso/(altura * altura).
# A  Organização  Mundial  de Saúde usa um  critério  simples  para  considerar quem  está  acima  do
# peso  e  quem  é  obeso:  Desenvolva  um  programa  que  leia  o  peso  (em  kg,  tipo  float) e
# altura (em metros, tipo float) e em seguida calcule o IMC e mostre qual a situação do adulto de acordo com a tabela:

# IMC Calculado
# Menos de 20   = Abaixo do peso
# 20 ≤ IMC < 25 = Peso normal
# 25 ≤ IMC < 30 = Acima do peso
# 30 ≤ IMC < 34 = Obeso
# Acima de 34   = Muito obeso

peso = float(input("Digite o seu peso em Kg:"))
altura = float(input("Digite o seu altura em cm:"))

altura = altura / 100

IMC = peso / altura * altura

if IMC < 20:
    print("IMC = ", IMC)
    print("\nAbaixo do Peso")
elif IMC >= 20 and IMC < 25:
    print("IMC = ", IMC)
    print("\nPeso Normal")
elif IMC >= 25 and IMC < 30:
    print("IMC = ", IMC)
    print("\nAcima do Peso")
elif IMC >= 30 and IMC < 34:
    print("IMC = ", IMC)
    print("\nObeso")
else:
    print("IMC = ", IMC)
    print("\nMuito Obeso")


