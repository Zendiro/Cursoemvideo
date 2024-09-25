s = 0
print('Esses números são ímpares')
for n in range(1, 500):
    if (n%3) == 0:
       print(n)
       s += n
print('A soma total dos números é {}'.format(s))