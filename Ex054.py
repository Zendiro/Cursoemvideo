from datetime import date

datmaior = 0
datmenor = 0
for n in range(1, 8):
    ano = int(input('Digite o ano de nascimento:  '))
    idade = date.today().year - ano
    if idade >= 18:
        datmaior += 1
    else:
        datmenor += 1
print('São {} pessoas maiores de idade\nE {} menores de idade'.format(datmaior, datmenor))