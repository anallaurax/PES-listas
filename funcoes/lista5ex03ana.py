'''3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
e exibir o resultado na tela.'''

from math import pi

alt = float(input('Digite o valor da altura:'))

raio = float(input('Digite o valor do raio:'))

def vol_cili(alt, r):
    return pi*(r**2) *alt

result = vol_cili(alt,raio)
print('O valor do volume do cilindro é:')
print( result)