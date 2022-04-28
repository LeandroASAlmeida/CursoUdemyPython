'''
Faca um programa que calcule o desvio padrao de um vetor v contendo n = 10 numeros,
onde m e a media do vetor. 

'''

from statistics import variance


v=[]
media=0
soma_xq= 0
soma_x=0
varian = 0
desvio=0

for n in range(0,10):
    num =int(input(f'Digite um numero:[{n}]: '))
    v.append(num)

media = sum(v)/10
varian= variance(soma_x)/media
desvio = (soma_xq - soma_x*2/n)/(n-1)

print(desvio)
print(media)
