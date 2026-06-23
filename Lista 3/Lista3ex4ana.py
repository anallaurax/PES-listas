'''4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
lista. Seu programa deve ter um menu com a seguinte estrutura:
1 – Cadastrar
2 - Excluir
3 - Listar
0 - Sair
A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve'''
placas = [0] * 15

while True:
    print("\nMENU")
    print("------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
        if 0 in placas:

            posicao = placas.index(0)
            placa = input("Digite a placa: ")

            if placa != "":
                if placa in placas:
                    placas[posicao] = placa
                    print("Placa cadastrada com sucesso!")
                else:
                    print("Placa já cadastrada!")
            else:
                print("Placa inválida!")
        else:
            print("Não é possível cadastrar mais placas!")

    elif opcao == 2:
        exclui = input("Qual placa você deseja excluir: ")

        if exclui in placas:
            indice = placas.index(exclui)
            placas[indice] = 0
            print("Placa excluída com sucesso!")
        else:
            print("Placa não encontrada!")

    elif opcao == 3:
        print("Placas cadastradas:")

        for placa in placas:
            if placa != 0:
                print(placa)

    else:
        print("Opção inválida!")