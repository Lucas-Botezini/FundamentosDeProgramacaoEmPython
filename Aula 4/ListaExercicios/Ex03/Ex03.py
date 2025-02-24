listaOperacoes = []

opcao = 1
valor = 0
while opcao != 0:
    opcao = int(input("1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair\nDigite: "))

    match(opcao):
        case 1:
            deposito = float(input("Informe o valor de depósito: "))
            valor += deposito
            print("Valor atualizado: R$", valor)
            listaOperacoes.append("Deposito : "+ str(deposito) +" - Valor: " + str(valor))
        case 2:
            saque = float(input("Informe o valor de depósito: "))
            if saque > valor:
                print("O valor do saque é maior que o valor disponível na conta\nDisponível R$", valor)
            else:
                valor -= saque
                print("Valor atualizado: R$", valor)
                listaOperacoes.append("Saque :"+ str(saque) +" - Valor: "+ str(valor))
        case 3:
            print("Valor disponível: R$", valor)
            for index in listaOperacoes:
                print(index)
        case 0:
            print("Saindo...Obrigado")