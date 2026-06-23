'''2 – Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela.'''

notas = []

quantidade = int(input("Digite a quantidade de notas: "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota: "))
    notas.append(nota)
    i = i + 1 

print("As notas são:", notas)