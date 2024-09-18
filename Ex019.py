from random import choice

alu1 = str(input('Digite o nome do primeiro aluno: ')) 
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
alunos = [alu1, alu2, alu3, alu4]
escolha = choice(alunos)
print('Parabéns {}!\nVocê foi o(a) escolhido(a)'.format(escolha))