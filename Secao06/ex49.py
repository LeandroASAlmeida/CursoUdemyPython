'''
O funcionario chamado Carlos tem um colega chamado Joao que recebe um salario que 
equivale a um terco do seu salario. Carlos gosta de fazer aplicacoes na rend_carlos de 
poupanca e vai aplicar seu salario integralmente nela, pois esta rendendo 2% ao mes.
Joao aplicara seu salario integralmente no fundo de renda fixa, que esta rendendo 5% 
ao mes. Construa um programa que devera calcular e mostrar a quantidade de meses 
necessarios para que o valor pertencente a Joao iguale ou ultrapasse o valor pertencente 
a Carlos. Teste com outros valores para as taxas.

'''
salario_carlos = float(input('Informe o salário de Carlos: '))
salario_joao = salario_carlos / 3

for i in range(1, 100):
    salario_carlos += salario_carlos * 0.02
    salario_joao += salario_joao * 0.05

    if salario_joao >= salario_carlos:
        print('João: R$%.2f' % salario_joao) #2f um espaço reservado para o número de ponto flutuante 
        print('Carlos: R$%.2f' % salario_carlos)
        print(f"Leva {i} meses para o salário de João igualar ou exceder"
              f" o de Carlos")
        break

