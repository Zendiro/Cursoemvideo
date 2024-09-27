sexo = str(input('Digite sexo:\n[M] para masculino\n[F] para feminino\n')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado inválido! Por favor, digite seu sexo novamente: ')).upper()
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print('Seu sexo é {}'.format(sexo))    
