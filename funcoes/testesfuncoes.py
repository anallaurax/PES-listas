#função com retorno

def fahr_em_cel(temp):
    return ((temp - 32) * (5/9))



'''tcel = fahr_em_cel(float(input('Digite o valor em fahr:')))
print("A temperatura em celsius é:", tcel)'''


#função sem retorno
def bom_dia(nome):
    print(f"Sou uma função que apenas diz...")
    print(f"Bom Dia, {nome}")


'''n = input("Digite o seu nome:")
bom_dia(n)'''


# função sem retorno

def soma(a, b):
    print(a+b)

'''v1 = int(input("Digite um valor para v1:"))
v2 = int(input("Digite um valor para v2:"))
soma(v1, v2)'''


def soma_list(valores):
    total = 0 
    for numero in valores:
        total = total + numero
    return total