somaidade = 0
maioridadehomem = 0
maioridademulher = 0
nomevelho = ''
totmulher20 = 0
for dados in range(1, 5):
    print('-' * 5,'{}ª PESSOA'.format(dados), '-' * 5)
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade 
    if dados == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print ('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print ('Ao todo são {} com menos de 20 anos'.format(totmulher20))