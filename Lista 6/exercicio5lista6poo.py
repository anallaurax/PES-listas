'''– Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__(self, nome, idade, altura, peso): 
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso


    def exibir_dados(self):
        imc = self.calcular_imc()
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m, Peso: {self.peso}kg,  IMC: {imc:.2f}'

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def exibir_nome_imc(self):
        imc = self.calcular_imc()
        return (f'Nome: {self.nome}, IMC: {imc:.2f}')


n = input('Digite o nome da pessoa: ')
i = int(input('Digite a idade da pessoa: '))
a = float(input('Digite a altura da pessoa (em metros): '))
p = float(input('Digite o peso da pessoa (em kg): '))
pessoa = Pessoa(n, i, a, p)

n2 = input('Digite o nome da segunda pessoa: ')
i2 = int(input('Digite a idade da segunda pessoa: '))
a2 = float(input('Digite a altura da segunda pessoa (em metros): '))
p2 = float(input('Digite o peso da segunda pessoa (em kg): '))
pessoa2 = Pessoa(n2, i2, a2, p2)

n3 = input('Digite o nome da terceira pessoa: ')
i3 = int(input('Digite a idade da terceira pessoa: '))  
a3 = float(input('Digite a altura da terceira pessoa (em metros): '))
p3 = float(input('Digite o peso da terceira pessoa (em kg): '))
pessoa3 = Pessoa(n3, i3, a3, p3)

print(pessoa.exibir_dados())

print(pessoa2.exibir_dados())

print(pessoa3.exibir_dados())
