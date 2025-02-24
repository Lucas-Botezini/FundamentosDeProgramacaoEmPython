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


