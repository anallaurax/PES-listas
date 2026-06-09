'''2 - Peça a idade de uma pessoa. Usando estruturas de decisão, exiba uma mensagem com a classificação indicativa permitida para essa pessoa: • Menor que 10 anos: "Você pode assistir apenas a filmes com classificação Livre." • Entre 10 e 11 anos: "Você pode assistir a filmes com classificação até 10 anos." • Entre 12 e 13 anos: "Você pode assistir a filmes com classificação até 12 anos." • Entre 14 e 15 anos: "Você pode assistir a filmes com classificação até 14 anos." • Entre 16 e 17 anos: "Você pode assistir a filmes com classificação até 16 anos." • 18 anos ou mais: "Você pode assistir a filmes com classificação até 18 anos."'''
idade = int(input('Digite sua idade'))
if idade<10 :
    print('Você pode assistir filmes de classificação livre')
elif  10 <= idade <= 11:
    print("Você pode assistir a filmes com classificação até 10 anos")
elif 12 <= idade <= 13:
    print("Você pode assistir a filmes com classificação até 12 anos")
elif 14 <= idade <= 15:
    print("Você pode assistir a filmes com classificação até 14 anos")
elif 16 <= idade <= 17:
    print("Você pode assistir a filmes com classificação até 16 anos")
else:
    print("Você pode assistir a filmes com classificação até 18 anos")
    