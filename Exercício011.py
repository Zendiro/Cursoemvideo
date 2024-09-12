altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
tinta = area / 2
print ('Você irá precisar de {:.2f} litros de tinta para pintar toda a parede'.format(tinta))