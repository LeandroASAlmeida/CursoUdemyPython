'''
31. Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a uniao
entre os 2 vetores anteriores, ou seja, que contem os numeros dos dois vetores. Nao
deve conter numeros repetidos. 

'''

vetor1=[]
vetor2=[]
vetor_union= []
cont1=0
cont2=0

print('VETOR 1:')
while cont1 < 10:
    valor = int(input(f"Digite um valor para o vetor1 ({cont1+1}/10): "))
    if valor in vetor1:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        vetor1.append(valor)
        cont1 += 1

print('VETOR 2:')
while cont2 < 10:
    valor = int(input(f"Digite um valor para o vetor2 ({cont2+1}/10): "))
    if valor in vetor2:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        vetor2.append(valor)
        cont2 += 1

vetor1 = set(vetor1)
vetor2 = set(vetor2)
vetor_union = vetor1.union(vetor2)

print(vetor_union)
