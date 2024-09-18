num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))
maior = num1
#Achando o maior número
if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3

print ('O maior número é: {} '.format(maior))
#Achando o menor número
menor = num1
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3
print ('O menor número é: {} '.format(menor))
