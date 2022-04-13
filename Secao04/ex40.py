
dias = int(input('Quantos dias foram trabalhados esse mês: '))
valor_dia = 30 * dias
desconto = (8 * valor_dia) / 100
valor_real = (valor_dia - desconto)

print('O valor recebido com o desconto do IR será de: R$ {}'.format(valor_real))