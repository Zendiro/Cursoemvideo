num = int(input('Digite um número: '))
print ('''Escolha uma das bases para conversão
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para hexadecimal''')
base = int(input('selecione uma opção: '))
if base == 1:
    print('O número {} em binário é: {}'.format(num, bin(num).lstrip('0b')))
elif base == 2:
    print('O número {} em octal é:{}'.format(num, oct(num).lstrip('0o')))
elif base == 3:
    print('O número {} em hexadecimal é:{}'.format(num, hex(num).lstrip('0x')))
else:
    print('Digite uma das 3 opções')