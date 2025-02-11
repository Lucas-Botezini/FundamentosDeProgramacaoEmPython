# 1) Faça um Programa que peça dois números e imprima o maior deles,
# se os números forem imprima os dois números informando que eles são iguais

n1 = int(input("Informe o 1° número: "))
n2 = int(input("Informe o 2° número: "))

if n1 > n2:
    print("Numero 1 é maior! ", n1)
elif n1 < n2:
    print("Numero 2 é maior! ", n2)
else:
    print("Os numeros são iguais! ", n1, " = " , n2)

