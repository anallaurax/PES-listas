'''6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
o nome da pessoa como critério de busca.'''

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
    print("5 - Pesquisar")
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
            idades.append(idade)    # Serve para adicionar um elemento no final da lista/espaço livre na lista
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

    

   # PESQUISAR 
    elif opcao == 5:
     nome = input("Digite o nome chave: ")

     if nome in nomes:
         for i in range(len(nomes)):
             if nomes[i] == nome:
                 print(f"Nome: {nomes[i]}")
                 print(f"Idade: {idades[i]} anos")
                 print(f"Altura: {alts[i]} m")
                 print(f"Peso: {pesos[i]} kg")
                 print("--------------------")
     else:
         print("Nome não encontrado.")

 
            


 



