jogador1 = str(input(' Jogador 1, escolha uma opção: pedra, papel ou tesoura:'))
jogador2 =  str(input(' Jogador 2, escolha uma opção: pedra, papel ou tesoura:'))
if jogador1 == jogador2:
    print('Empate!')
elif jogador1 == "pedra" and jogador2 == "tesoura":
    print('Jogador 1 venceu!')
elif jogador1 == "tesoura" and jogador2 == 'papel':
    print('Jogador 1 venceu!')
elif jogador1 == "papel" and jogador2 == "pedra":
    print('Jogador 1 venceu!')
else:
    print('Jogador 2 venceu!')