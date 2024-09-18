import random
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#####
num2 = int(input('Escolha um número: '))
numpc = random.randint(1, 10)
if num2 == numpc:
    print ('Parabéns você ganhou! O número que você escolheu foi {} e o computador escolheu {}'.format (num2, numpc))
else:
    print ('Você perdeu! O número que você escolheu foi {} e o computador escolheu{}'.format(num2, numpc))

