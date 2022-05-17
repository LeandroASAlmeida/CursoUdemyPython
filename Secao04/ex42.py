salario = float(input('Informe seu salario base : '))
gratificacao = salario * 0.05
imposto = salario * 0.07
desconto = salario - imposto
novo_salario = salario + gratificacao
print(f'Parabens! Seu salário com a bonificação ficou em R$ {novo_salario}')
print(f'Porem com os impostos vai ficar em R$ {desconto}')
