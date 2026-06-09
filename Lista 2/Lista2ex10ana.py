qnt_num = 0
soma = 0

while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break

    qnt_num = qnt_num + 1
    soma = soma + num

if qnt_num > 0:
    media = soma / qnt_num
    print("Média =", media)
else:
    print("Nenhum número digitado")

print("Quantidade de números digitados:", qnt_num)
print("A soma dos números:", soma)