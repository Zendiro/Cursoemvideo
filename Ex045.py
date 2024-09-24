from time import sleep
from random import choice
escolha = str(input('Escolha entre pedra, papel e tesoura: '))
opcaopc = ['pedra', 'papel', 'tesoura']
escolhapc = choice(opcaopc)
print('JÔ')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
if escolhapc == escolha:
    print('Você escolheu {} e o computador escolheu {}, por isso vocês empataram'.format(escolha, escolhapc))
elif escolhapc == 'pedra' and escolha == 'tesoura':
    print('Você escolheu {} e o computador escolheu {}, por isso você perdeu'.format(escolha, escolhapc))
elif escolhapc == 'papel' and escolha == 'pedra':
    print('Você escolheu {} e o computador escolheu {}, por isso você perdeu'.format(escolha, escolhapc))
elif escolhapc == 'tesoura' and escolha == 'papel':
    print('Você escolheu {} e o computador escolheu {}, por isso você perdeu'.format(escolha, escolhapc))
elif escolha == ' ':
    print('Escolha uma das opções')
else:
    print('Parabéns você ganhou! Você escolheu {} e o pc escolheu {}'.format(escolha, escolhapc))