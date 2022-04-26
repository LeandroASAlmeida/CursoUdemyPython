'''
O funcionario chamado Carlos tem um colega chamado Joao que recebe um salario que 
equivale a um terco do seu salario. Carlos gosta de fazer aplicacoes na rend_carlos de 
poupanca e vai aplicar seu salario integralmente nela, pois esta rendendo 2% ao mes.
Joao aplicara seu salario integralmente no fundo de renda fixa, que esta rendendo 5% 
ao mes. Construa um programa que devera calcular e mostrar a quantidade de meses 
necessarios para que o valor pertencente a Joao iguale ou ultrapasse o valor pertencente 
a Carlos. Teste com outros valores para as taxas.

'''
sal_carlos=float(input('Informe o salário atual de Carlos : '))
sal_joao = sal_carlos / 3
meses = 0
rend_carlos = 0 #investimento Carlos
rend_joao = 0 #investimento João
rend_carlos = (rend_carlos + sal_carlos) * 1.02
rend_joao = (rend_joao + sal_joao) * 1.05

while rend_joao < rend_carlos:# Enquanto o investimento do joão for menor do que do Carlos
    rend_carlos = sal_carlos * (1.02 ** meses)
    rend_joao  = sal_joao *(1.05 ** meses)
    meses += 1

    if rend_joao >= rend_carlos:
        print(f'joão alcança carlos depois de {meses} meses.')
        break


