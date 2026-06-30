'''1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
apresentar apenas as idades que forem maiores ou iguais a 16.'''

idades = [0] * 6 

idades[0] = int(input("Digite a idade do aluno 1:"))
idades[1] = int(input("Digite a idade do aluno 2:"))
idades[2] = int(input("Digite a idade do aluno 3:"))
idades[3] = int(input("Digite a idade do aluno 4:"))
idades[4] = int(input("Digite a idade do aluno 5:"))
idades[5] = int(input("Digite a idade do aluno 6:"))

for elemento in idades:
    if elemento >= 16: 
     print("Idade:", elemento)