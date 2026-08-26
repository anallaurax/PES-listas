'''5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.
Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.'''


while True:
    
    print('== CALCULADORA==')
    print('1 - Adição;')
    print('2 - Subtração;')
    print('3 - Multiplicaçao;')
    print('4 - Divisão;')
    print('0 - Sair.')

    opcao = int(input('Digite uma opção;'))

    if opcao == 0:
        print('Programa encerrado!')
        break

    num1 = int(input('Digite o primeiro numero:'))
    num2 = int(input('Digite o segundo numero:'))

    if opcao == 1:
        total = num1 + num2
        print('Aqui está a soma dos valores;')
        print(total)

    elif opcao == 2:
        total = num1 - num2
        print('Aqui está a subtração dos valores;')
        print(total)

    elif opcao == 3:
        total = num1 * num2
        print('Aqui está a multiplicação dos valores;')
        print(total)

    elif opcao == 4:
        if num2 == 0:
            print('Esse número não é divisivel;')
            break
        else:
            total = num1/num2
            print('Aqui está a divisão dos valores;')
            print(total)
    else:
        print('Opção inválida!')