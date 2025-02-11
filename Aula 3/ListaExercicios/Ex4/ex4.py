# 4) Peça para o usuário informar um ano, e calcule se esse ano é Bissexto ou não, condições:
# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
# Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

ano = int(input('Ano: '))
# "%" representa o operador de módulo, que retorna o resto da divisão.
# Na condição ano % 4 == 0, verificamos se o ano é divisível por 4.
# No entanto, também é necessário garantir que ele NÃO seja divisível por 100 (ano % 100 != 0).
# Se o ano for múltiplo de 400, ele é automaticamente bissexto.
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')