pri = int(input('Primeiro termo: '))
raz = int(input('razão: '))
termo = pri
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')