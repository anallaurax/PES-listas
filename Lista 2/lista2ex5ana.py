'''5 – Faça um programa que exiba na tela a tabuada de um número informado pelo
usuário. Vamos supor que o número informado seja o 2, então o programa deve exibir o
seguinte resultado na tela:'''

num = int(input("Informe o número:"))
for i in range(1, 11):
     resultado = num * i     # i é o contador de loops, no caso de 1 a 10
     print(f"{num} x {i} = {resultado}")    #f-string, que permite colocar variáveis dentro da string de forma mais organizada 
     