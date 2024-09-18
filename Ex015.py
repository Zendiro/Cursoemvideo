alu = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
vdias = alu * 60
vkm = km * 0.15
alutotal = vdias + vkm
print ('Você irá pagar R${}'.format(alutotal)) 