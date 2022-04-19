'''Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se 
aposentar. As condicoes para aposentadoria sao
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.'''

idade = float(input('Digite a idade do trabalhador: '))
tempo = float(input('Digite o tempo de serviço: '))

if idade > 65:
    print('Pode se aposentar!')

elif tempo > 30:
    print('Pode se aposentar!')

elif idade > 60 and tempo > 25:
    print('Pode se aposentar!')

else:
    print('Não pode se aposentar!')
