nota1 = float(input('Informe a primeira nota do aluno: '))
if (nota1 < 0.0 or nota1 > 10.0):
    print('use numero de 0 a 10')
    print('ENCERRANDO PROGRAMA')
    exit()
else:
    print('Nota1 válida')

nota2 = float(input('Informe a segunda nota do aluno: '))
if (nota2 < 0.0 or nota2 > 10.0):
    print('use numero de 0 a 10')
    print('ENCERRANDO PROGRAMA')
    exit()
else:
    print('Nota2 válida')

media= (nota1+nota2)/2

print('A média das notas é {}'.format(media))


    


  