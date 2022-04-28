'''
12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores
'''

valores=[]
media = 0

for n in range(0,5):
    num =int(input('Informe 5 valores: '))
    valores.append(num)
print(valores)

print(f'O maior elemento da lista é o {max(valores)}')
print(f'O menor elemento da lista é o {min(valores)}')
print(f'A média da lista é {(sum(valores) / 5):.2f}')

