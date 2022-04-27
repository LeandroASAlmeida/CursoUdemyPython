'''
Faca um programa que calcule o desvio padrao de um vetor v contendo n = 10 numeros,
onde m e a media do vetor. 

'''

v=[]
media=0

for n in range(0,10):
    num =float(input(f'Digite um numero:[{n}]: '))
    v.append(num)
media += v[n]

media = media/len(v)

print(v)
print(media)