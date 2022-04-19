'''Leia uma data de nascimento de uma pessoa fornecida atraves de tres numeros inteiros:
Dia, Mes e Ano. Teste a validade desta data para saber se esta e uma data valida. Teste
se o dia fornecido e um dia valido: dia > 0, dia ≤ 28 para o mes de fevereiro (29 se o 
ano for bissexto), dia ≤ 30 em abril, junho, setembro e novembro, dia ≤ 31 nos outros
meses. Teste a validade do mes: mes > 0 e mes < 13. Teste a validade do ano: ano ≤
ano atual (use uma constante definida com o valor igual a 2008). Imprimir: “data valida” 
ou “data invalida” no final da execucao do programa.'''


dia_nasc = int(input('Informe o dia do seu nascimento: '))
mes_nasc = int(input('Informe o mês do seu nascimento: '))
ano_nasc = int(input('Informe o ano do seu nascimento: '))

valida = False

if mes_nasc == 2:
    if (dia_nasc > 0 and dia_nasc <= 28):
            if(dia_nasc <= 29):
              valida = True

if dia_nasc <= 30 and mes_nasc == 4 or mes_nasc == 6 or mes_nasc == 7 or mes_nasc == 11:
              valida = True

if dia_nasc <= 31 and mes_nasc == 1 or mes_nasc == 3 or mes_nasc == 5 or mes_nasc == 8 or mes_nasc == 9 or mes_nasc == 10 or mes_nasc == 12:
              valida = True

if mes_nasc > 0 and mes_nasc < 13:
              valida = True

if ano_nasc <= 2008:
              valida = True
              
if(valida):
        print('Data válida')
else:
        print('Inválida')