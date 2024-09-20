#Aula
#n1 = (5 + 3 * 2)
#n2 = (3 * 5 + 4 ** 2)
#n3 = (3 * (5 + 4) ** 2)
#print ('O valor do número 1 é {}, valor do número 2 é {} e o valor do numero 3 é {} '.format(n1,n2, n3 ))

# Prática
#n1 = (5+3*2)
#n2 = (5**2)
#n3 = (5**3)
#n4 = (19//2)
#n5 = (19/2)
#n6 = (365**522)
#n7 = (18%2)
#n8 = (122%3)
#n9 = (4**3)
#n10 = pow (4,3)
#n11 = 81**(1/2)
#n12 = 25**(1/2)
#n13 = 127**(1/3)

nome = input('Qual é o seu nome? ')
print ('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input(' Um valor:   '))
n2 = int(input (' Outro valor:   '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(s, m, d, di, e), end=' ')
print ('Essas são as operações requisitadas')
