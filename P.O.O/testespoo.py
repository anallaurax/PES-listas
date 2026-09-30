
class Estudante:
    def __init__(self, nome, sobrenome, idade, cpf):  # seld significa ela mesmo, a propria classe
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf



n = input('diigte o nome:')
s = input('digite o sobre:')
i = int(input('digite a idade:'))
c = int(input('digite o cpf:'))

estudante2 = Estudante(n,s,i,c)
print(estudante2.nome, estudante2.sobrenome, estudante2.idade, estudante2.cpf)

# mudar atributo
#estudante2.nome = 'ricardo'


#printar ja colcado manualmente
#estudante1 = Estudante('Ana', 'Pereira', 17, '111.111.111.11')
#print(estudante1.nome, estudante1.sobrenome, estudante1.idade, estudante1.cpf)

# chamando o metodo e imprimindo o resultado


