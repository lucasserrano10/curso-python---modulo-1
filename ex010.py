import random
alu1 = input('aluno 1:')
alu2 = input('aluno 2:')
alu3 = input('aluno 3:')

alunos = [alu1,alu2,alu3]
random.shuffle(alunos)
print(alunos)