total_caixa = 0

while True:
    codigo = int(input("Digite o código do produto (0 para encerrar): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade comprada: "))

    if codigo == 1:
        nome = "Suco"
        preco = 6.00
    elif codigo == 2:
        nome = "Pão de queijo"
        preco = 3.00
    elif codigo == 3:
        nome = "Pastel"
        preco = 7.00
    elif codigo == 4:
        nome = "Salada de frutas"
        preco = 9.00
    elif codigo == 5:
        nome = "Café com leite"
        preco = 3.50
    elif codigo == 6:
        nome = "Caputino"
        preco = 4.50
    elif codigo == 7:
        nome = "Iogurte"
        preco = 6.50
    elif codigo == 8:
        nome = "Água"
        preco = 2.50
    else:
        print("Código inválido!")
        continue

    total_compra = preco * quantidade
    total_caixa += total_compra

    print("Produto:", nome)
    print("Valor da compra: R$", total_compra)

print("Valor total acumulado no caixa: R$", total_caixa)