from random import choice



while escolha :
    escolha = str((input('Escolha entre pedra, papel e tesoura: '))).lower()
    print('=-' * 20)
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
    elif escolha != 'pedra' or escolha != 'papel' or escolha != 'tesoura':
        print('Parabéns você ganhou! Você escolheu {} e o computador escolheu {}!'.format(escolha, escolhapc))
    else: 
        print('Escolha inválida\nEscolha novamente')
              
              

print('Tudo bem! Estarei aqui a sua disposição ^^ ')