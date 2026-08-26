'''4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.'''

dicio = {"Apelar " : "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados",
         }

for i in range(4):
    palavra = input('Digite a  palavra;')
    sign = input('Digite seu significado;')
    dicio[palavra] = sign

while True:
    result = input('Digite a palavra que deseja ver o significado:')

    if result in dicio:
         print('Aqui esta o significado da palavra')
         print(dicio[result])
    else:
        print('Palavra não encontrada;')
    
   