num = int(input('Digite um número: '))
for n in range (1, num+1):
    if num % n == 0:
        print('\033[m', end='')
    else:
        print('\033[34m', end= '')
    print('{}'.format(n), end='')
