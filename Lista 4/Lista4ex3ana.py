'''3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.
Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0
Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0'''

notas = []

quantidade = int(input("Digite a quantidade de notas: "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota: "))
    notas.append(nota)
    i = i + 1 

print("As notas são:", notas)

indice = 0 

while indice < quantidade:
    print("As notas são: ", notas[indice])
    indice = indice + 1