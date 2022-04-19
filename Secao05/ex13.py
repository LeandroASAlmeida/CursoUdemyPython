'''Faca um algoritmo que calcule a media ponderada das notas de 3 provas. A primeira e 
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a media do aluno 
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovacao deve ser igual ou 
superior a 60 pontos'''

nota1 = float(input('Informe a primeira nota: '))
peso1 = float(input('Informe o peso dessa nota: '))
nota2 = float(input('Informe a segunda nota: '))
peso2 = float(input('Informe o peso dessa nota: '))
nota3 = float(input('Informe a terceira nota: '))
peso3 = float(input('Informe o peso dessa nota: '))
mp = (nota1*peso1+nota2*peso2+nota3*peso3) / (peso1+peso2+peso3)
print('A media ponderada do aluno é {}'.format(mp))

if mp >= 6.0:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')