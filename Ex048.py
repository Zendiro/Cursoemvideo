s = 0
cont = 0
print('Esses números são ímpares')
for n in range(1, 501, 2):
    if (n%3) == 0:
       cont += 1
       s += n
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))