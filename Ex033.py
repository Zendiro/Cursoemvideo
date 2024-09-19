a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a

#Verificando que é maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print ('O maior número é: {} '.format(maior))

#Verificando que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b  :
    menor = c
print ('O menor número é: {} '.format(menor))
