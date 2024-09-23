n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5.0:
    print('Sua média é {}, por isso você foi REPROVADO'.format(med))
elif med >= 5.0 and med <= 6.9:
    print('Sua média é {}, você está de RECUPERAÇÃO'.format(med))
else:
    print('Parabéns! Sua média é {}, você foi aprovado'.format(med))