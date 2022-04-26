''''
Um funcionario recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 
recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao
dobro do ano anterior. Faca programa que determine o salario atual do funcionario
'''


aumento = 0.015
salario = 2000
ano= 1995


for ano in range(1996, 2022):
        if ano == 1995:
            salario = 2000
        elif ano == 1996:
            salario *= 1.015
        else:
            salario *= 2
        print(f'{ano} R$ {salario:.2f}')
        ano += 1