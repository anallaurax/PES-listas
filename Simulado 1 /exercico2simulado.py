'''2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.'''

bingo = []*15

indice = 0 

while indice <15:
    valor_bingo = int(input('Digite o valor que deseja armazenar (O valor deve ser de 1 até 75):'))

    if valor_bingo in bingo:
        print('Valor já existente:')
    else:
        if  1 <= valor_bingo <= 75:
          bingo.append(valor_bingo)
          indice = indice + 1
          print('Número armazenado com sucesso:')
        else:
            print('Número invalido;')

print(sorted(bingo))

        

   




  

