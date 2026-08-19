'''6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
usuário para inserir as horas e minutos, e exiba o tempo total em minutos'''

def tempo_total(horas, minutos):
   total = (horas* 60) + minutos
   return total

h = int(input('Digite a quantidade de horas que o jovem passou jogando:'))
min = int(input('Digite a quantidade de minutos que o jovem passou jogando:'))

resultado = tempo_total(h, min)
print(resultado)