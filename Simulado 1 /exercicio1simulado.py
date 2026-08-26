'''1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.'''

def ano_bi(valor):
    if valor %4 == 0:
        print('O ano é bissexto!')
    else:
        print('O ano não é bissexto!')


ano = int(input('Digite o ano que desejas saber:'))
resultado = ano_bi(ano)
print(resultado)