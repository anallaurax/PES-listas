temperatura = float(input('Informe a temperatura do dia em ºC:'))
if temperatura < 10:
    print('Está muito frio! Use roupas quentes.')
elif  10 <= temperatura <= 20:
    print('Frio! Vista-se bem')
elif 20 > temperatura <= 25:
    print('Temperatura Agradável')
elif 25 > temperatura <= 30:
    print('Está ficando quente!')
else:
    print('Está muito quente! Fique hidradato.')