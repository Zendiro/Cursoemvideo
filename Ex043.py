peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
alt2 = alt ** 2
imc = peso / alt2
if imc < 18.5:
    print('Seu imc é {:.2f}, você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.2f}, você está com o peso ideal'.forma(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.2f}, você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é {:.2f}, você está com obesidade'.format(imc))
else:
    print('Seu imc é {:.2f}, você está com obesidade mórbida'.format(imc))