'''7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
peso, baseado, também, no nome informado.'''

cadastro = []

from minhasclasses import Pessoa


while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Atualizar")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    # SAIR
    if opcao == 0:
        print("Programa encerrado.")
        break
    

    # CADASTRAR
    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura em metros: "))
        peso = float(input("Digite o peso em kg: "))

        pessoa = Pessoa(nome, idade, altura, peso)

        cadastro.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    # LISTAR
    elif opcao == 2:
        if len(cadastro) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("\n--- Pessoas cadastradas ---")

            for pessoa in cadastro:
                print(pessoa.exibir_dados())

    # EXCLUIR
    elif opcao == 3:
        nome = input("Digite o nome da pessoa que deseja excluir: ")

        encontrada = False

        for pessoa in cadastro:
            if pessoa.nome == nome:
                cadastro.remove(pessoa)
                encontrada = True
                print("Pessoa excluída com sucesso!")
                break

        if encontrada == False:
            print("Pessoa não encontrada.")

    # ATUALIZAR
    elif opcao == 4:
        nome = input("Digite o nome da pessoa que deseja atualizar: ")

        encontrada = False

        for pessoa in cadastro:
            if pessoa.nome == nome:
                pessoa.idade = int(input("Digite a nova idade: "))
                pessoa.altura = float(input("Digite a nova altura em metros: "))
                pessoa.peso = float(input("Digite o novo peso em kg: "))

                encontrada = True
                print("Pessoa atualizada com sucesso!")
                break

        if encontrada == False:
            print("Pessoa não encontrada.")

    
