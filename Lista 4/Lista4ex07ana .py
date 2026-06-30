'''7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
0 - Sair
Opção:'''


notas = []

while True:
    print("\nOPÇÕES")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular média")
    print("5 - Mostrar maior nota")
    print("6 - Mostrar menor nota")
    print("0 - Sair")
    print("Opção:")

    opcao = int(input("Digite a opção:"))

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao == 1:

        cadastro = input("Digite a nota: ")
        notas.append(cadastro)  # Serve para adicionar um elemento no final da lista/espaço livre na lista
        print("Cadastro realizado com sucesso!")

    # EXCLUIR
    elif opcao == 2:

        if len(notas) == 0:
            print("Não há notas cadastradas!")
        else:
            indice = int(input("Digite o índice da nota que deseja excluir: "))

            if indice >= 0 and indice < len(notas):
                notas.pop(indice)
                print("Nota excluída com sucesso!")
            else:
                print("Índice inválido!")

    # LISTAR
    elif opcao == 3:
        print("\nNOTAS CADASTRADAS")
        print("--------------------")

        if len(notas) == 0:
            print("Nenhuma nota cadastrada!")
        else:
            print("Notas Cadastradas:", notas)

    # CALCULAR MÉDIA
    elif opcao == 4:

        if len(notas) == 0:
            print("Nenhuma nota cadastrada!")
        else:
            soma = 0

            for i in range(len(notas)):
                soma = soma + float(notas[i])  # float força a saida a ser decimal, caso a soma dos valores seja decimal

            media = soma / len(notas)

            print("Média:", media)

            if media >= 6:
                print("Situação: Aprovado!")
            else:
                print("Situação: Reprovado!")
    
    # MOSTRAR A MAIOR NOTA

    elif opcao == 5:
  
     if len(notas) == 0:
        print("Nenhuma nota cadastrada!")
     else:
        maior = float(notas[0])

        for i in range(len(notas)):
            if float(notas[i]) > maior:
                maior = float(notas[i])

        print("Maior nota:", maior)

    # MENOR NOTA
    elif opcao == 6:

     if len(notas) == 0:
        print("Nenhuma nota cadastrada!")
     else:
        menor = float(notas[0])

        for i in range(len(notas)):
            if float(notas[i]) < menor:
                menor = float(notas[i])

        print("Menor nota:", menor)