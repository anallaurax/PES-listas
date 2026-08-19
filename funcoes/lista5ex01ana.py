'''1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.'''

def media_arit(a,b,c):
    print('A média aritmética simples é:')
    print((a+b+c)/3)

v1 = int(input('Digite v1:'))
v2 = int(input('Digite v2:'))
v3 = int(input('Digite v3:'))

media_arit(v1,v2,v3)
