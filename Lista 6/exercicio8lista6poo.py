'''8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
deve ter um menu com as seguintes opções:
Sistema de Cadastro
-------------------
1 – Cadastrar estudante
2 – Cadastrar professor
3 – Listar estudantes
4 – Listar professores
5 – Alterar estudante pela matrícula
6 – Alterar estudante pelo nome
7 – Alterar professor pela matrícula
8 – Alterar professor pelo nome
9 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
0 – Sair
Opção: '''


cadastroestudantes = []
cadastroprofessores = []

from minhasclasses import Estudante1, Professor


while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar estudante")
    print("2 - Cadastrar professor")
    print("3 - Listar estudantes")
    print("4 - Listar professores")
    print("5 - Alterar estudante pela matrícula")
    print("6 - Alterar estudante pelo nome")
    print("7 - Alterar professor pela matrícula")
    print("8 - Alterar professor pelo nome")
    print("9 - Excluir estudante pela matrícula")
    print("10 - Excluir professor pela matrícula")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    # SAIR
    if opcao == 0:
        print("Programa encerrado.")
        break
    

    # CADASTRAR ESTUDANTE
    if opcao == 1:
        nome = input("Digite o nome do estudante: ")
        sobrenome = input("Digite o sobrenome do estudante: ")
        idade = int(input("Digite a idade do estudante: "))
        matricula = input("Digite a matrícula do estudante: ")

        estudante = Estudante1(nome, sobrenome, idade, matricula)

        cadastroestudantes.append(estudante)

        print("Estudante cadastrado com sucesso!")

    # CADASTRAR PROFESSOR
    elif opcao == 2:
        nome = input("Digite o nome do professor: ")
        sobrenome = input("Digite o sobrenome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        matricula = input("Digite a matrícula do professor: ")
        especializacao = input("Digite a especialização do professor: ")

        professor = Professor(nome, sobrenome, idade, matricula, especializacao)

        cadastroprofessores.append(professor)

        print("Professor cadastrado com sucesso!")

    # LISTAR ESTUDANTES
    elif opcao == 3:
        if len(cadastroestudantes) == 0:
            print("Nenhum estudante cadastrado.")
        else:
            print("\n--- Estudantes cadastrados ---")

            for estudante in cadastroestudantes:
                print(estudante.apresentar())

    # LISTAR PROFESSORES
    elif opcao == 4:
        if len(cadastroprofessores) == 0:
            print("Nenhum professor cadastrado.")
        else:
            print("\n--- Professores cadastrados ---")

            for professor in cadastroprofessores:
                print(professor.apresentar())   

    # ATUALIZAR estudante pela matrícula
    elif opcao == 5:
        matricula = input("Digite a matrícula do estudante que deseja atualizar: ")

        encontrada = False

        for estudante in cadastroestudantes:
            if estudante.matricula == matricula:
                estudante.nome = input("Digite o novo nome: ")
                estudante.sobrenome = input("Digite o novo sobrenome: ")
                estudante.idade = int(input("Digite a nova idade: "))
                encontrada = True
                print("Estudante atualizado com sucesso!")
                break
            else:
                print("Estudante não encontrado.")

    # ATUALIZAR estudante pelo nome
    elif opcao == 6:
        nome = input("Digite o nome do estudante que deseja atualizar: ")

        encontrada = False

        for estudante in cadastroestudantes:
            if estudante.nome == nome:
                estudante.sobrenome = input("Digite o novo sobrenome: ")
                estudante.idade = int(input("Digite a nova idade: "))
                estudante.matricula = input("Digite a nova matrícula: ")
                encontrada = True
                print("Estudante atualizado com sucesso!")
                break
            else:
                print("Estudante não encontrado.")

    # ATUALIZAR professor pela matrícula

    elif opcao == 7:
        matricula = input("Digite a matrícula do professor que deseja atualizar: ")

        encontrada = False

        for professor in cadastroprofessores:
            if professor.matricula == matricula:
                professor.nome = input("Digite o novo nome: ")
                professor.sobrenome = input("Digite o novo sobrenome: ")
                professor.idade = int(input("Digite a nova idade: "))
                professor.especializacao = input("Digite a nova especialização: ")
                encontrada = True
                print("Professor atualizado com sucesso!")
                break
            else:
                print("Professor não encontrado.")

    # ATUALIZAR professor pelo nome
    elif opcao == 8:
        nome = input("Digite o nome do professor que deseja atualizar: ")

        encontrada = False

        for professor in cadastroprofessores:
            if professor.nome == nome:
                professor.sobrenome = input("Digite o novo sobrenome: ")
                professor.idade = int(input("Digite a nova idade: "))
                professor.matricula = input("Digite a nova matrícula: ")
                professor.especializacao = input("Digite a nova especialização: ")
                encontrada = True
                print("Professor atualizado com sucesso!")
                break
            else:
                print("Professor não encontrado.")

    # EXCLUIR estudante pela matrícula
    elif opcao == 9:
        matricula = input("Digite a matrícula do estudante que deseja excluir: ")

        encontrada = False

        for estudante in cadastroestudantes:
            if estudante.matricula == matricula:
                cadastroestudantes.remove(estudante)
                encontrada = True
                print("Estudante excluído com sucesso!")
                break
            else:
                print("Estudante não encontrado.")

    
    # EXCLUIR professor pela matrícula
    elif opcao == 10:
        matricula = input("Digite a matrícula do professor que deseja excluir: ")

        encontrada = False

        for professor in cadastroprofessores:
            if professor.matricula == matricula:
                cadastroprofessores.remove(professor)
                encontrada = True
                print("Professor excluído com sucesso!")
                break
            else:
                print("Professor não encontrado.")
