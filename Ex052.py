num = int(input('Digite um número: '))
tot = 0
for n in range (1, num+1):
    if num % n == 0:
        tot += 1
        print('\033[m', end='')
    else:
        print('\033[34m', end='')
    print('{}'.format(n), end='')
print ('\n\033[mO número {}, é divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo!')
else: print('E por isso ele não é primo!')
