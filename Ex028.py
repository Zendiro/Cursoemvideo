from random import randint
from time import sleep

num = int(input('Digite um número de 1 a 5: '))
print ('O computador está escolhendo:.....')
sleep(1)
cores = {'limpa':'\033[m', 
         'vermelho':'\033[1;31m',
         'azul': '\033[1;34m'}
numpc = randint(1,5)
if num == numpc:
    print('Você escolheu o número {}\nO número escolhido pelo computador foi {}\nLogo você venceu!'.format(cores['azul'], num, cores['limpa'], cores['azul'], numpc, cores['limpa']))
else:
    print('Você escolheu o número {}\nO número escolhido pelo computador foi {}\nLogo você perdeu!'.format(cores['vermelho'], num, cores['limpa'], cores['vermelho'] ,numpc, cores['vermelho']))