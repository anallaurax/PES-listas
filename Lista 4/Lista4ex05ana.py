'''5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair
Instituto Federal de Santa Catarina – Reitoria
Rua: 14 de julho, 150 | Coqueiros | Florianópolis /SC | CEP: 88.075-010
Fone: (48) 3877-9000 | www.ifsc.edu.br | CNPJ 11.402.887/0001-60
Opção:'''

amigos = []

while True:
    print("\nOPÇÕES")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")
    print("Opção:")

    opcao = int(input("Digite a opção:"))

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao == 1:
        
        cadastro= input("Digite o nome do amigo próximo: ")

        if cadastro in amigos:
            print("Esse amigo já está cadastrado!")
        else:
            amigos.append(cadastro)                              # Serve para adicionar um elemento no final da lista/espaço livre na lista                                           
            print("Cadastro realizado com sucesso!")

    # EXCLUIR
    elif opcao == 2:
        cadastro = input("Digite o nome do amigo que deseja excluir: ")

        if cadastro in amigos:
            indice = amigos.index(cadastro)

            amigos.pop(indice)    # o pop serve para excluir o elemento que esta no indice

            print("Cadastro excluído com sucesso!")
        else:
            print("Amigo não encontrado!")
            
    
    # LISTAR
    
    elif opcao == 3:
        if len(amigos) == 0:                         # len Serve para descobrir quantos elementos existem na lista.
            print("Nenhum cadastro encontrado.")
        else:
            print("\nPESSOAS CADASTRADAS")
            print("--------------------")

            for i in range(len(amigos)):
                print(f"Amigos cadastrados:", amigos )
                