'''
Faca um programa para ler 10 numeros DIFERENTES a serem armazenados em um 
vetor. Os dados deverao ser armazenados no vetor na ordem que forem sendo lidos, 
sendo que caso o usuario digite um numero que ja foi digitado anteriormente, o programa 
devera pedir para ele digitar outro numero. Note que cada valor digitado pelo usuario 
deve ser pesquisado no vetor, verificando se ele existe entre os numeros que ja foram 
fornecidos. Exibir na tela o vetor final que foi digitado.
'''

vetor = []
cont = 0

while cont < 10:
    valor = int(input(f"Digite um valor para o vetor ({cont+1}/10): "))
    if valor in vetor:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        vetor.append(valor)
        cont += 1

print(vetor)