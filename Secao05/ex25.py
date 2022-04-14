a = float(input('Digite o valor de a (x²): '))---

if (a == 0):#variavel diferente de zero
    print('Não é uma equação do segundo grau')
    
else:
    b = float(input('Digite o valor de b(x): '))
    c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)
raiz_1 = ((-(b)) + (delta) ** 0.5) / (2 * a)
raiz_2 = ((-(b)) - ((delta) ** 0.5)) / (2 * a)
raiz_3 = (raiz_1 == raiz_2)

print('O valor de deltá é {:.2f}'.format(delta)) # 0.000000	{:.2f}	0.00	Format float 2 decimal places

if (delta == 0):
    print('A equação possui apenas uma raíz real, sendo ela = {}' .format(raiz_1))
elif (delta >= 1):
    print('A equação possui duas raízes reais, sendo elas: {} e {}'.format(raiz_1,raiz_2))
else:
    print ('A equação não possui raízes')
