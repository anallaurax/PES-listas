'''4 – Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        if self.quantidade > 0:
            return True
        else:
            return False

    def vender(self):
        if self.quantidade > 0:
            self.quantidade -= 1


# teste

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))

produto = Produto(nome, quantidade)
produto2 = Produto("Caneta", 0)



print("\nProduto:", produto.nome   )
print("Quantidade:", produto.quantidade   )

if produto.esta_disponivel():
    print("Produto disponível!")
else:
    print("Produto indisponível!")

print("\nVendendo um produto...")
produto.vender()

print("Quantidade atual:", produto.quantidade)


