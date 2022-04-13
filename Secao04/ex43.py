valor = float(input('Informe o valor da venda a ser calculado : '))
desconto = valor - (valor * 0.10)
parcela = valor / 3
com_avista = 0.05 * desconto
com_parc = 0.05 * valor



print('O valor total com desconto de 10 % é : {}'. format(desconto))
print('Valor de cada parcela será de:{}'.format(parcela))
print('O Valor da comissão se venda a vista é de :{}' .format(com_avista))
print('O Valor da comissão se venda parcelada vai ser der :{}' .format(com_parc))

