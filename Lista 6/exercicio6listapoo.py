'''6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:
Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção:
'''

cadastro = []

from minhasclasses import Pessoa


while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
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
