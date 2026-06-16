
placas = [0] * 15

posicao = 0

while True:
    print("\nMENU")
    print("------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")


    opcao =int(input("Digite a opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
        if posicao < 15:
            placa = (input("Digite a placa: "))

            if placa != 0:
                placas[posicao] = placa
                posicao = posicao + 1
                print("Placa cadastrada com sucesso!")
            else:
                print("Placa inválida!")
        else:
            print("Não é possível cadastrar mais placas!")

    elif opcao == 2:
        exclui = input("Qual placa você deseja excluir")
        for placa in placas:
            if placa == exclui:
                placas[placa] = 0 
    
    elif opcao == 3:
        print("Placas cadastradas:")
        for placa in placas:
            if placa != -1:
                print(placa)
    else:
        print("Opção inválida!")
         