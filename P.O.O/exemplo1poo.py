
class Estudante:
    def __init__(self, nome, sobrenome, idade, cpf):  # seld significa ela mesmo, a propria classe
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    
    def Apresentar(self):
        return f'Olá meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos'



n1 = input('diigte o nome1:')
s1 = input('digite o sobre1:')
i1 = int(input('digite a idade1:'))
c1 = int(input('digite o cpf1:'))

n2 = input('diigte o nome2:')
s2 = input('digite o sobre2:')
i2= int(input('digite a idade2:'))
c2 = int(input('digite o cpf2:'))


n3 = input('diigte o nome3:')
s3 = input('digite o sobre3:')
i3= int(input('digite a idade3:'))
c3 = int(input('digite o cpf3:'))


estudante1 = Estudante(n1,s1,i1,c1)

estudante2 = Estudante(n2,s2,i2,c2)

estudante3 = Estudante(n3,s3,i3,c3)

print(estudante1.nome, estudante1.sobrenome, estudante1.idade, estudante1.cpf)
print(estudante2.nome, estudante2.sobrenome, estudante2.idade, estudante2.cpf)
print(estudante3.nome, estudante3.sobrenome, estudante3.idade, estudante3.cpf)

print(estudante1.apresentar())

print(estudante2.apresentar())

print(estudante3.apresentar())