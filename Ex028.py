from random import randint
from time import sleep

num = int(input('Digite um número de 1 a 5: '))
print ('O computador está escolhendo:.....')
sleep(1)
numpc = randint(1,5)
if num == numpc:
    print('Você escolheu o número {}\nO númvero escolhido pelo computador foi {}\nLogo você venceu!'.format(num, numpc))
else:
    print('Você escolheu o número {}\nO número escolhido pelo computador foi {}\nLogo você perdeu!'.format(num, numpc))