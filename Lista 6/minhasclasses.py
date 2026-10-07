class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    
    def descrição(self):
        return f'O livro {self.titulo} foi escrito por {self.autor}'
    
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor 


    def pintar(self, novacor):
        self.cor = novacor

    def mostar_cor(self):
        return f'A cor atual do carro é {self.cor}'
    

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor2):
        self.saldo = self.saldo - valor2

    def mostar_saldo(self):
        return f' O saldo atual é {self.saldo}'
    


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
            print("Produto vendido!")
        else:
            print("Produto esgotado!")


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




class Estudante1:
    def __init__(self, nome, sobrenome, idade, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.matricula = matricula

    def apresentar(self):
        return f'Nome: {self.nome}, Sobrenome: {self.sobrenome}, Idade: {self.idade}, Matrícula: {self.matricula}'

    
class Professor:
    def __init__(self, nome, sobrenome, idade, matricula, especializacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.matricula = matricula
        self.especializacao = especializacao

    def apresentar(self):
        return f'Nome: {self.nome}, Sobrenome: {self.sobrenome}, Idade: {self.idade}, Matrícula: {self.matricula}, Especialização: {self.especializacao}'
