dist = float(input('Qual é a distância da viagem em KM?: '))
if dist <= 200:
    calckm1 = dist * 0.50
    print('Você irá pagar R${:.2f}'.format(calckm1))
else:
    calckm2 = dist * 0.45
    print('Você irá pagar R${:.2f}'.format(calckm2))