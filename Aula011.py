#\033[0:30:41m
#\033[4:4:33:44m
#\033[1:35:43m
#\033[30:42m
#\033[m
#\033[7:30m

#a = 3
#b = 5
#print('Os valores são \033[1;34;45m{}\033[m e \033[1;32;43 m{}\033[m'.format(a, b))

nome = 'Guanabara'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[0;30m'}
print ('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))