'''4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
remoção dela e imprima a lista novamente.'''


qntcidade = int(input("Digite a quantidade de cidades para o cadastro:"))
cidades = [] 

while True:

    print("\nOPÇÕES")
    print("1 - Cadastrar ")
    print("2 - Excluir")
    print("0 - Sair")

    opcao = int(input("Digite a opção:"))
    

    if opcao == 0:
        print("Programa encerrado!")
        break


    elif opcao == 1:
        
        cidade = input("Digite as cidades: ")

        if cidade in cidades:
            print("Essa cidade já está cadastrada!")
        else:
            cidades.append(cidade)                              # Serve para adicionar um elemento no final da lista/espaço livre na lista                                           
            print("Cadastro realizado com sucesso!")
            print("PESSOAS CADASTRADAS")
            print("--------------------")

            for i in range(len(cidades)):
                print(f"Cidades:", cidades )

                print("--------------------")

    # EXCLUIR
    elif opcao == 2:
        cidade = input("Digite o nome da cidade que deseja excluir: ")

        if cidade in cidades:
            indice = cidades.index(cidade)

            cidades.pop(indice)    # o pop serve para excluir o elemento que esta no indice

            print("Cadastro excluído com sucesso!")
            print("PESSOAS CADASTRADAS")
            print("--------------------")

            for i in range(len(cidades)):
                print(f"Cidades:", cidades )

                print("--------------------")
        else:
            print("Cidade não encontrada!")
            




