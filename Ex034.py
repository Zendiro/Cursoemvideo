sal = float(input('Qual é o salário do funcionário?: '))
if sal > 1250.00:
    aum1 = sal + (sal * 10 / 100)
    print('Seu aumento foi de 10%, seu novo salário é R${}'.format(aum1))
else:
    aum2 = sal + (sal * 15 / 100)
    print('Seu aumento foi de 15%, seu novo salário é R${}'.format(aum2))