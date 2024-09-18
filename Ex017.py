from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(catop, catad)
print('O comprimento do cateto oposto é {}\nO comprimento do cateto adjacente é {}\nA hipotenusa é {}\n'.format(catop, catad, hipo))
