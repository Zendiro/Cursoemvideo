num = int(input('Digite um número: '))
print('-' * 20)
for n in range(1, 10+1):
    m = num * n
    print('{} x {} = {}'.format(num, n, m))
print('-' * 20)