from random import choice

y = 's'
escolha = str((input('Escolha entre pedra, papel e tesoura: '))).lower()
while escolha == '' and y != 'n':
    opcaopc = ['pedra', 'papel', 'tesoura']
    escolhapc = choice(opcaopc) 
    if escolha == escolhapc:
        print('Vocês empataram!')
    elif escolha == 'pedra' and escolhapc == 'papel':
        print('Você perdeu! Você escolheu {} e o computador escolheu {}!'.format(escolha, escolhapc))
    elif escolha == 'tesoura' and escolhapc == 'pedra':
        print('Você perdeu! Você escolheu {} e o computador escolheu {}!'.format(escolha, escolhapc))
    elif escolha == 'papel' and escolhapc == 'tesoura':
        print('Você perdeu! Você escolheu {} e o computador escolheu {}!'.format(escolha, escolhapc))
    else:
        print('Parabéns você ganhou! Você escolheu {} e o computador escolheu {}!'.format(escolha, escolhapc))
    y = str(input('Escolha inválida!\n Deseja jogar novamente?: ')).lower()
print('Tudo bem! Estarei aqui a sua disposição ^^ ')
