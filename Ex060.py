n = int(input('Digite um número: '))

f = 1
c = n
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1
print('{}'.format(f))

