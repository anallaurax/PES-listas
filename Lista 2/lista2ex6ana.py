
'''6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
tabuada, em vez de começar iniciar no 1 e terminar no 10.'''


num = int(input("Informe o número:"))
pausa = int(input("Informe quem qual número você quer parar:"))
for i in range(1, pausa +1):
     resultado = num * i     # i é o contador de loops, no caso de 1 a 10
     print(f"{num} x {i} = {resultado}")    #f-string, que permite colocar variáveis dentro da string de forma mais organizada 
     