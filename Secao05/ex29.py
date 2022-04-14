a= int(input('Escolha um numero aleatório entre 1 e 100 : '))---
b= int(input('Escolha outro numero aleatório entre 1 e 100 : '))
print('Você escolheu o numero {} e o numero {}.'.format(a,b))
result = int(input(' Qual o resultado de {} + {} ?: '.format(a,b)))
soma = a + b

if result == soma:
    print('Parabens você acertou')
else:
    print('O Valor da sua resposta está errado')


