'''2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
reprovado(a)).'''

notas = [0] * 4
soma = 0 

notas[0] = float(input("Digite a nota1 do aluno:"))
notas[1] = float(input("Digite a nota2 do aluno:"))
notas[2] = float(input("Digite a nota3 do aluno:"))
notas[3] = float(input("Digite a nota4 do aluno:"))

for elemento in notas:
    soma = soma + elemento

    media = soma/4

if media >= 6:
    print(media, "Aprovado:")
else:
    print(media, "Reprovado")


