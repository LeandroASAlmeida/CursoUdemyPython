salario = float(input('Informe seu salário: '))
prestacao = float(input('Informe o valor da prestação do emprestimo desejada: '))
limite = (salario * 0.20)

if prestacao > limite:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

