valor = float(input('Informe o valor da venda a ser calculado : '))
desconto = valor - (valor * 0.10)
parcela = valor / 3
com_avista = 0.05 * desconto
com_parc = 0.05 * valor



print(f'O valor total com desconto de 10 % é : {desconto}')
print(f'Valor de cada parcela será de:{parcela}')
print(f'O Valor da comissão se venda a vista é de :{com_avista}')
print(f'O Valor da comissão se venda parcelada vai ser der :{com_parc}')

