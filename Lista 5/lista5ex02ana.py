'''2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
resultado na tela.'''

def impar_par(valor):
    if valor % 2 == 0:
        return " O número é par"
    else:
       return "O número é impar"
    
num = int(input('Digite o numero para saber se ele é impar ou par:'))
resultado = impar_par(num)
print(resultado)