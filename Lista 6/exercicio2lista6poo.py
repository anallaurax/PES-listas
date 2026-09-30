'''2 – Crie uma classe chamada Carro com:
• Atributos: marca e cor.
• Um método chamado pintar que recebe uma nova cor como argumento e altera o
atributo cor para essa nova cor.
• Um método chamado mostrar_cor que retorna a cor atual do carro.
Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
com mostrar_cor.'''


class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor 


    def pintar(self, novacor):
        self.cor = novacor

    def mostar_cor(self):
        return f'A cor atual do carro é {self.cor}'
    

m = input('Digite a marca do carro:')
c = input('Digite a cor do carro:')
carro1 = Carro(m,c)
carro1.pintar(input('Digite a nova cor do carro:')) 

print(f' A marca do carro é {carro1.marca} e a cor é {carro1.cor}')
print(carro1.mostar_cor())


