'''Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
8%). Faca um programa em que o usuario entre com o valor e o estado destino do 
produto e o programa retorne o preco final do produto acrescido do imposto do estado
em que ele sera vendido. Se o estado digitado nao for valido, mostrar uma mensagem 
de erro'''


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
    