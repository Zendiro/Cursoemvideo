ter = int(input('Primeiro termo: '))
raz = int(input('razão: '))
dec = ter + (10 - 1) * raz
for c in range(ter, dec + raz , raz):
    print('{}'.format(c), end=' > ')
print('FIM')