valor = float(input('Informe o valor do produto: '))
estado = int(input('Informe um estado : 0[MG] - 1[SP] - 2[RJ] - 3[MS] : '))

if estado == 0:
    valor_final= valor +(valor *(7/100)) #7%
    print("Estado escolhido: Minas Gerais - Taxa de imposto 7%\n")
    print('O valor total do produto vai ser {}'. format(valor_final))
if estado == 1:
    valor_final= valor +(valor *(12/100))#12%
    print("Estado escolhido: Minas Gerais - Taxa de imposto 12%\n")
    print('O valor total do produto vai ser {}'. format(valor_final))
if estado == 2:
    valor_final= valor +(valor *(15/100))#15%
    print("Estado escolhido: Minas Gerais - Taxa de imposto 15%\n")
    print('O valor total do produto vai ser {}'. format(valor_final))
if estado == 3:
    valor_final= valor +(valor *(8/100))#16%
    print("Estado escolhido: Minas Gerais - Taxa de imposto 8%\n")
    print('O valor total do produto vai ser {}'. format(valor_final))
else:
    print('Estado não cadastrado.')
    