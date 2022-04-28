'''
14. Faça um programa que leia um vetor de 10 posições e verifique se existem valores
iguais e escreva-os no ecrã.

'''


valores=[]
valores_iguais =[]

for n in range(0,10):
    num =int(input('Informe 10 valores: '))
    valores.append(num)
    if valores.count(num) > 1 and num not in valores_iguais:
        valores_iguais.append(num)

print(valores)
print(end='\n')

print(f'Numeros iguais {valores_iguais}')



