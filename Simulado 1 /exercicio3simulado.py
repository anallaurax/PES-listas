'''3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.'''

prod = input('Digite o produto comprado:')
quant = int(input('Digite a quantidade comprada:'))
preco = float(input('Digite o valor do produto:'))

total = preco * quant

if total >= 100:
    total =  total * 1.10
    print('Você ganhou 10 % de desconto, o valor a ser pago é:')
    print(total)

else:
    print('Você não tem direito ao desconto:')