'''Escrever um programa que leia o codigo do produto escolhido do cardapio de uma lan- 
chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execucao somente ser a calculado um pedido. O cardapio da lan- 
chonete segue o padrao abaixo:'''

cod = int(input('Código:'))
quant = int(input('Quantidade:'))
if cod == 100:
    print('Cachorro Quente')
    print(f'Preço: R${(quant * 1.2):.2f}')
elif cod == 101:
    print('Bauru Simples')
    print(f'Preço: R${(quant * 1.3):.2f}')
elif cod == 102:
    print('Bauru com Ovo.')
    print(f'Preço: R${(quant * 1.5):.2f}')
elif cod == 103:
    print('Hamburguer.')
    print(f'Preço: R${(quant * 1.2):.2f}')
elif cod == 104:
    print('Cheesburguer.')
    print(f'Preço: R${(quant * 1.7):.2f}')
elif cod == 105:
    print('Suco.')
    print(f'Preço: R${(quant * 2.2):.2f}')
elif cod == 106:
    print('Refrigerante.')
    print(f'Preço: R${(quant * 1):.2f}')