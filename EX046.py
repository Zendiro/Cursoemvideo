from emoji import emojize
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('FOGOS ESTOURANDO!:fireworks:',language='en'))
