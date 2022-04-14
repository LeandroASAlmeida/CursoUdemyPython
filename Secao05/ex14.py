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

    