'''Leia o salario de um trabalhador e o valor da prestacao de um emprestimo. Se a 
prestacao for maior que 20% do salario imprima: Emprestimo nao concedido, caso
contrario imprima:Emprestimo concedido'''

salario = float(input('Informe seu salário: '))
prestacao = float(input('Informe o valor da prestação do emprestimo desejada: '))
limite = (salario * 0.20)

if prestacao > limite:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

