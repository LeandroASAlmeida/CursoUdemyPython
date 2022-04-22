'''
Escreve um programa que verifique quais numeros entre 1000 e 9999 (inclusive) pos- 
suem a propriedade seguinte: a soma dos dois dıgitos de mais baixa ordem com os dois
dıgitos de mais alta ordem elevada ao quadrado e igual ao proprio numero. Por exemplo, 
para o inteiro 3025, temos que:
30 + 25 = 55
552 = 3025

'''
n1 =0
n2=0

for i in range(1000, 10000):
    n1 = int(str(i)[0:2])
    n2 = int(str(i)[2:4])
    if (n1 + n2)**2 == i:
        print(i)
        print('O numero {},possui essa caracteristica:'.format(i))
