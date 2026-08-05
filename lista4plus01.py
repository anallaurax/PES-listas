'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
Implemente um algoritmo de acordo com os requisitos listados abaixo:
A – Serão utilizados 6 laboratórios com as nomenclaturas Lab102, Lab103, Lab104,
Lab105, Lab106, Lab107.
B – Os professores autorizados de acordo com cada laboratório:
• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.
C – O programa deverá ter uma opção para cadastrar as listas por laboratório e a
lista de professores. Deverá ter opção de imprimir todos os cadastros de cada laboratório,
bem como a lista de professores com seu código de crachá.
D - O sistema de identificação de liberação da porta será feito através do fecho
eletrônico através do Crachá do Servidor, conforme a tabela de crachás abaixo. Vamos
simular que a autorização se dará por meio do teclado dos dispositivos na porta. Você
deve criar no seu programa, uma chamada que permita digitar o código do crachá.
Cadastro de Professores
001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profª Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo'''

profs = {'001' : "Prof Thiago Paes",
'002' : "Prof Schalata",
'003' : "Prof Ignácio",
'004' : "Prof Ryan",
'005' : "Prof André",
'006' : "Profª Fabiana",
'007' : "Prof Alberto",
'008' : "Prof Juliano",
'009' : "Prof Thiago Waltrik",
'010' : "Prof João Eduardo"}

lab102 = ['001', '003', '004', '005', '006']
lab103 = ['007']
lab104 = ['004', '008', '002', '005']
lab105 = ['001', '003', '009', '007']
lab106 = ['001', '009', '003', '002']
lab107 = ['001', '002', '009', '005']


while True:
    print(' == sistema de laboratórios:','\n')
    print(' 1 - Cadastrar Professores:')
    print(' 2 - Listar Professores:')
    print(' 3 - Excluir Professor')
    print(' 4 - Alterar Professor')
    print(' 5 - Cadastrar Laboratórios( já cadastrados automaticamente.)')
    print(' 6 - Listar acessos do Laboratórios')
    print(' 7 - Excluir acesso')
    print(' 8 - Alterar acesso')
    print(' 0 - Sair')
    print(' Opção:')

    opcao = int(input("Digite a opção:"))

    if opcao == 0:
        print("Programa encerrado!")
        break
# CADASTRAR
    elif opcao == 1:
        codprof = input('Digite o codigo do professor:')
        nomeprof = input('Digite o nome do professor:')

        profs[codprof] = nomeprof  # Serve para adicionar um elemento no final da lista/espaço livre na lista
        print("Cadastro realizado com sucesso!")
# LISTAR
    elif opcao == 2:
        for codprof, nomeprof in profs.items():
         print('Esses são os professdores cadastrados:')
         print(f'{codprof} - {nomeprof}')

# EXCLUIR
    elif opcao == 3:
       codexcluir = input('Digite o codigo que deseja excluir:')
       if codexcluir in profs:
          del profs[codexcluir]
          print(' Codigo excluido com sucesso:')
       else:
          print(f' Erro, o {codexcluir} não existe:')

    elif opcao == 4:
       codalterar = input('Digite o codigo que deseja alterar')

       if codalterar in profs:
        nomealterar = input('Digite o nome alterado:')
        profs[codalterar] = nomealterar
        print('Professor alterado com sucesso:')
       else:
          print('Professor não encontrado:')

    elif opcao == 5:
       lab102 = ['001', '003', '004', '005', '006']
       lab103 = ['007']
       lab104 = ['004', '008', '002', '005']
       lab105 = ['001', '003', '009', '007']
       lab106 = ['001', '009', '003', '002']
       lab107 = ['001', '002', '009', '005']

       print(' Cadastros realizados com sucesso!:')
    

    elif opcao == 6:
        lab = input('Digite o nome do lab que você deseja ver a lista:')
        if lab == "lab102":
            print('Esses são os professdores cadastrados no lab102:')
            for i in lab102:
                print(f' {i} - {profs[i]}')

        if lab == "lab103":
            print('Esses são os professdores cadastrados no lab103:')
            for i in lab103:
                print(f' {i} - {profs[i]}')

        if lab == "lab104":
            print('Esses são os professdores cadastrados no lab104:')
            for i in lab104:
              print(f' {i} - {profs[i]}')

        if lab == "lab105":
           print('Esses são os professdores cadastrados no lab105:')
           for i in lab105:
             print(f' {i} - {profs[i]}')

        if lab == "lab106":
             print('Esses são os professdores cadastrados no lab106:')
             for i in lab106:
              print(f' {i} - {profs[i]}')

        if lab == "lab107":
             print('Esses são os professdores cadastrados no lab107:')
             for i in lab107:
              print(f' {i} - {profs[i]}')



    elif opcao == 7:
      acessoex = input('Digite o codigo que deseja excluir:')
      if acessoex in lab102:
        del lab102[acessoex]
        print(' Codigo excluido com sucesso:')
      else:
        print(f' Erro, o {acessoex} não existe:')

      if acessoex in lab103:
              del lab103[acessoex]
              print(' Codigo excluido com sucesso:')
      else:
              print(f' Erro, o {acessoex} não existe:')


      if acessoex in lab104:
             del lab104[acessoex]
             print(' Codigo excluido com sucesso:')
      else:
             print(f' Erro, o {acessoex} não existe:')

      if acessoex in lab105:
            del lab105[acessoex]
            print(' Codigo excluido com sucesso:')
      else:
            print(f' Erro, o {acessoex} não existe:')

      if acessoex in lab106:
              del lab106[acessoex]
              print(' Codigo excluido com sucesso:')
      else:
              print(f' Erro, o {acessoex} não existe:')


      if acessoex in lab107:
             del lab107[acessoex]
             print(' Codigo excluido com sucesso:')
      else:
             print(f' Erro, o {acessoex} não existe:')


    elif opcao == 8:
        acessoalt = input('Digite o codigo que deseja alterar')

        if acessoalt in lab102:
         nacessoalt = input('Digite o nome alterado:')
         lab102[acessoalt] = nacessoalt
         print('Acesso alterado com sucesso:')
        else:
         print('Professor não encontrado:')

        if acessoalt in lab103:
         nacessoalt = input('Digite o nome alterado:')
         lab103[acessoalt] = nacessoalt
         print('Acesso alterado com sucesso:')
        else:
         print('Professor não encontrado:')

        if acessoalt in lab102:
                 nacessoalt = input('Digite o nome alterado:')
                 lab102[acessoalt] = nacessoalt
                 print('Acesso alterado com sucesso:')
                else:
                 print('Professor não encontrado:')
        
        

        
             
     
      
    
     
      

      
            
                        
                                
                        
                        
                       
                     
                   
                 



       





    
       

