'''7 - Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
valores fora da faixa forem informados, eles devem ser modificados para valores dentro
da faixa de forma elegante.'''

def moldura(linhas=1, colunas=1):

    if linhas < 1:
        linhas = 1

    if linhas > 20:
      linhas = 20

    if colunas < 1:
        colunas = 1

    if colunas > 20:
     colunas = 20

    print('+' + '-' * (colunas - 2) + '+')

    for i in range(linhas - 2):
     print('|' + ' ' * (colunas - 2) + '|')

    if linhas > 1:
        print('+' + '-' * (colunas - 2) + '+')


linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

moldura(linhas, colunas)
