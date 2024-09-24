prd = float(input('Qual é o valor do produto? '))
form = int(input('''Qual é a forma de pagamento?
          [1] - À vista dinheiro/cheque:
          [2] - À vista no cartão: 
          [3] - Em até 2x no cartão: 
          [4] - 3x ou mais no cartão:\n'''))
diche = prd - (prd * 10 / 100)
avica = prd - (prd * 5 / 100)
duas = prd / 2
tres =  prd + (prd * 20 / 100)
if form == 1:
    print('O valor do produto é R${}, à vista no dinheiro/cheque fica R${}'.format(prd, diche))
elif form == 2:
    print('O valor do produto é R${}, à vista no cartão fica R${}'.format(prd, avica))
elif form == 3:
    print('O valor do produto é R${}, em até 2x ficam duas de R${}'.format(prd, duas))
elif form == 4:
    totalparc = int(input('Quantas parcelas? '))
    parcela = prd / totalparc
    print('O valor do produto é R${}, será parcelado em {} vezes, valor do produto fica de R${:.2f} por mês e o valor total será de R${}'.format(prd, totalparc, parcela, tres ))
else:
    print('Opção de pagamento inválida. Tente novamente')