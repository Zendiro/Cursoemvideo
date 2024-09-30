from random import randint
from time import sleep

tentotal = 0
num = 0
numpc = randint(1,10)
ten = 3

while numpc != num and ten != 0:
    ten -= 1 
    num = int(input('Digite um número de 1 a 10: '))
    print('Você tem {} tentativas'.format(ten))       
    tentotal += 1
if num == numpc and tentotal == 1:
    print('<' * 10, '>' * 10)
    print ('O computador está processando sua escolha:.....')
    print('<' * 10, '>' * 10)
    sleep(1)
    print('Você escolheu o número {}\nO número escolhido pelo computador foi {}\nLogo você venceu!\nFoi feita {} tentativa '.format(num, numpc, tentotal))
elif num == numpc and tentotal < 1:
    print('<' * 10, '>' * 10)
    print ('O computador está processando sua escolha:.....')
    print('<' * 10, '>' * 10)
    sleep(1)
    print('Você escolheu o número {}\nO número escolhido pelo computador foi {}\nLogo você venceu!\nFoi feita {} tentativa '.format(num, numpc, tentotal))
elif ten == 0:
    print('Você perdeu! Seu número de tentativas esgotou')