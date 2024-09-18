vel = int(input('Qual é a velocidade?: '))
if vel > 80:
    print('Você foi multado!')
    multcal = vel - 80
    total = multcal * 7.0
    print('Você irá pagar R${} reais de multa'.format(total))
else:
    print('Tenha uma boa viagem')