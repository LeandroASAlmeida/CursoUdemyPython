'''
Peca ao usuario para digitar dez valores numericos e ordene por ordem crescente esses 
valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
final na tela os valores em ordem.
'''


ordenado = []
cont = 0

while cont < 10:
    valor = int(input(f"Digite um valor para o vetor ({cont+1}/10): "))
    if valor in ordenado :
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        ordenado .append(valor)
        ordenado .sort()
        print(ordenado)
        cont += 1
    



