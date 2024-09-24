from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e está na categoria Júnior'.format(idade))
elif idade == 20:
    print('Você tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER'.format(idade))