premio = float(input('Qual o valor do prêmio?'))
valor_amigo1 = float(input('Quanto vai investir o apostador 1?'))
valor_amigo2= float(input('Quanto vai investir  o apostador 2?'))
valor_amigo3 = float(input('Quanto vai investir o apostador 3?'))

res_valor_amigo1 = 0.5 * premio
res_valor_amigo2 = 0.35 * premio
res_valor_amigo3= 0.15 * premio

print('Proporcionalmente alinhado com o valor apostado o apostador A ganhou R${}'.format(res_valor_amigo1) + 'reais.')
print('Proporcionalmente alinhado com o valor apostado o apostador B ganhou R${}'.format(res_valor_amigo2) + ' reais.')
print('Proporcionalmente alinhado com o valor apostado o apostador C ganhou R${}'.format(res_valor_amigo3) + ' reais.')