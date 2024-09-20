emp = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Quanto é o seu salário? R$ '))
anos = int(input('Em quanto anos você irá pagar? '))
pres = emp / (anos * 12)
min = sal * 30 / 100
if pres >= (sal - (sal * 30 / 100)):
    print('Não foi dessa vez! A parcela ultrapassa 30% do seu salário, a parcela que vc iria pagar é de R${:.2f} por mês'.format(pres))
else:
    print('Parabéns! você pode fazer o financiamento, a parcela que vc irá pagar é de R${:.2f} por mês'.format(pres))


    

