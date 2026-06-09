'''Exercício 09: Implemente um algoritmo que solicite ao usuário a
quantidade de salgados consumidos na cantina e o valor do
salgado (considere que todos possuem o mesmo preço).
Lembre-se que o preço é um número de ponto flutuante e não
um inteiro. Em seguida, exiba o valor total da compra.'''
salgado = 5
qnt_salgados= int(input('Digite a quantidade de salgados'))
tot = salgado*qnt_salgados
print('O valor total da compra é', tot, 'reais')
