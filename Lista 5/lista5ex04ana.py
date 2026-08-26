'''4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
números ao usuário, chamar a função e exibir o resultado da soma na tela.'''

def soma_list(valores):
    total = 0 
    for numero in valores:
        total = total + numero
    return total

lista = []

lista.append(int(input('Digite o valor 1: ')))
lista.append(int(input('Digite o valor 2: ')))
lista.append(int(input('Digite o valor 3: ')))
lista.append(int(input('Digite o valor 4: ')))

print('A soma dos elementos é:')
print(soma_list(lista))