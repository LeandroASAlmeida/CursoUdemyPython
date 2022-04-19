'''A nota final de um estudante e calculada a partir de tres notas atribuidas entre o intervalo
de 0 ate 10, respectivamente, a um trabalho de laboratorio, a uma avaliacao semestral 
e a um exame final. A media das tres notas mencionadas anteriormente obedece aos 
pesos: Trabalho de Laboratorio: 2; Avaliacao Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno esta reprovado (media entre 0 e 2,9), de 
recuperacao (entre 3 e 4,9) ou se foi aprovado. Faca todas as verificacoes necessarias. '''


nota_lab = float(input('Informe a nota de trabalho de Laboratório: '))
peso1 = float(input('Informe o peso dessa nota: '))
nota_sem= float(input('Informe a nota da Avaliação Semestral: '))
peso2 = float(input('Informe o peso dessa nota: '))
nota_final = float(input('Informe a nota do Exame final: '))
peso3 = float(input('Informe o peso dessa nota: '))

mp = (nota_lab*peso1+nota_sem*peso2+nota_final*peso3) / (peso1+peso2+peso3)

if  mp == 0 and mp <= 2.9:
    print('A média final do Aluno é {} e o aluno está Reprovado' .format(mp))
elif mp == 3 and mp <= 4.9:
    print('A média final do Aluno é {} e o aluno está em Recuperação' .format(mp))
else:
    print('A média final do Aluno é {} e o aluno está Aprovado' .format(mp))

    