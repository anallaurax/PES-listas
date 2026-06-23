'''5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas. '''

nomes = []
idades = []
alts = []
pesos = []

while True:

    print("\nMENU")
    print("------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break

    # CADASTRAR
    elif opcao == 1:
        nome = input("Digite o nome: ")

        if nome in nomes:
            print("Essa pessoa já está cadastrada!")
        else:
            idade = int(input("Digite a idade: "))
            altura = float(input("Digite a altura (m): "))
            peso = float(input("Digite o peso (kg): "))

            nomes.append(nome)
            idades.append(idade)    # Serve para adicionar um elemento no final da lista.
            alts.append(altura)
            pesos.append(peso)

            print("Cadastro realizado com sucesso!")

    # EXCLUIR
    elif opcao == 2:
        nome = input("Digite o nome da pessoa que deseja excluir: ")

        if nome in nomes:
            indice = nomes.index(nome)

            nomes.pop(indice)    # o pop serve para excluir o elemento que esta no indice
            idades.pop(indice)
            alts.pop(indice)
            pesos.pop(indice)

            print("Cadastro excluído com sucesso!")
        else:
            print("Pessoa não encontrada!")

    # ALTERAR
    elif opcao == 3:
        nome = input("Digite o nome da pessoa que deseja alterar: ")

        if nome in nomes:
            indice = nomes.index(nome)

            nomes[indice] = input("Novo nome: ")
            idades[indice] = int(input("Nova idade: "))
            alts[indice] = float(input("Nova altura (m): "))
            pesos[indice] = float(input("Novo peso (kg): "))

            print("Cadastro alterado com sucesso!")
        else:
            print("Pessoa não encontrada!")

    # LISTAR
    
    elif opcao == 4:
        if len(nomes) == 0:                         # len Serve para descobrir quantos elementos existem na lista.
            print("Nenhum cadastro encontrado.")
        else:
            print("\nPESSOAS CADASTRADAS")
            print("--------------------")

            for i in range(len(nomes)):
                print(f"Nome: {nomes[i]}")
                print(f"Idade: {idades[i]} anos")
                print(f"Altura: {alts[i]} m")
                print(f"Peso: {pesos[i]} kg")
                print("--------------------")

    else:
        print("Opção inválida!")

