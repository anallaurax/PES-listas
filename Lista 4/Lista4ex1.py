'''1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
programa deve exibir o nome de todos os bairros cadastrados na tela.'''

nomes = [0] * 6 

nomes[0] = ("Campo D'una")
nomes[1] = (input("Digite o nome do bairro 2 :"))
nomes[2] = (input("Digite o nome do bairro 3:"))
nomes[3] = (input("Digite o nome do bairro 4::"))
nomes[4] = (input("Digite o nome do bairro 5:"))
nomes[5] = (input("Digite o nome do bairro 6:"))


for elemento in nomes:
     print("Nomes dos bairros:", elemento)