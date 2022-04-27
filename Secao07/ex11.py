'''

11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre
a quantidade de números negativos e a soma dos números positivos desse vetor.

'''

indice = 0
valores = []
contador =0 
soma=0

while indice < 10:
    num = float(input(f'Insira um numero({indice+1}/10): '))
    valores.append(num)
    indice += 1
    if num < 0:
        contador += 1
    if num > 0:
        soma += num
print(valores)

print(f'Nessa lista existem {contador} números negativos e a soma entre seus valores positivos é {soma}')




