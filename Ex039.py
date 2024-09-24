from datetime import date

ano = int(input('Digite o ano de nascimento: '))
anoali = date.today().year - ano
if anoali > 18:
    print('Faz {} anos que você já passou da hora de se alistar'.format(anoali - 18))
elif anoali < 18:
    print('Ainda faltam {} anos para você se alistar'.format(anoali))
else:
    print('Você tem {} anos já está na hora de se alistar!'.format(anoali))