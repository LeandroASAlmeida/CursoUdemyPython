'''Leia a nota e o numero de faltas de um aluno, e escreva seu conceito. De acordo com a 
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reducao de conceito.'''

nota = float(input('Qual a nota do aluno?'))
falta = float(input('Quantas faltas teve o aluno?'))

if nota >= 9 and falta < 20:
    print('Seu conceito é A')
if nota >= 9 and falta > 20:
    print('Seu conceito é B')
if 7.5 < nota < 8.9 and falta < 20:
    print('Seu conceito é B')
if 7.5 < nota < 8.9 and falta > 20:
    print('Seu conceito é C')
if 5 < nota < 7.4 and falta < 20:
    print('Seu conceito é C')
if 5 < nota < 7.4 and falta > 20:
    print('Seu conceito é D')
if 4 < nota < 4.9 and falta < 20:
    print('Seu conceito é D')
if 4 < nota < 4.9 and falta > 20:
    print('Seu conceito é E')
if 0 < nota < 3.9 and falta < 20:
    print('Seu conceito é E')
if 0 < nota < 3.9 and falta > 20:
    print('Seu conceito é B')
