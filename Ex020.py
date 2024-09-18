from random import shuffle
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
alunos = [n1, n2, n3, n4]
shuffle (alunos)
print('A lista da ordem de apresentação é:{}'.format(alunos))