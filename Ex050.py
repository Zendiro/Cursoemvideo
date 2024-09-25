s = 0
for n in range(0, 6):
    num = int(input('Digite um número: '))
    if (num%2) == 0: 
        s += num
print('O total das somas dos valores pares são: {}'.format(s))