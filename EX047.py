print('Esses números são pares')
for p in range(2, 51,2):
    print('.', end = '')
    if (p%2) == 0:
        print('{}'.format(p), end= '  ')
print('FIM')