n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opção = 0

while opção != 5:
    print('=-' * 20)
    print('Digite umas seguintes opções:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos número\n[ 5 ] sair do programa\n')
    opção = int(input('>>>>> Qual é a sua opção? ')) 
    print('=-' * 20) 
    if opção == 1:
        soma = n1 + n2
        print('O resultado da soma de {} mais {} é igual a {} '.format(n1, n2, soma ))
    elif opção == 2:
        multi = n1 * n2
        print('O resultado multiplicação de {} mutiplicado por {} é igual a {}'.format(n1,n2, multi))
    elif opção == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
         print('Digite uma opção válida!')

if opção == 5:
        print('Você saiu do programa')