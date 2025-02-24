idade = int(input("Digite a idade: "))

if idade < 0:
    print("OPCAO INVALIDA!")
elif idade <= 4:
    print("AINDA EH CEDO PARA JOGAR FUTEBOL!")
elif idade <= 10:
    print(f"{idade} anos Sub-10")
elif idade <= 17:
    print(f"{idade} anos Sub-17")
elif idade <= 20:
    print(f"{idade} anos Sub-20")
elif idade <= 35:
    print(f"{idade} anos Profissional")
elif idade <= 55:
    print(f"{idade} anos Master")
else:
    print(f"{idade} anos MELHOR APOSENTAR AS CHUTEIRAS!")
