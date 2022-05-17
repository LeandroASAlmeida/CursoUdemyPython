'''
16. Faca uma funcao chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando 
varios sımbolos de igual (Ex: ========). A funcao recebe por parametro quantos sinais 
de igual serao mostrados. 

'''

def desenha_linha(igual):
    return '=' * igual

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe quantos sinais de '=', devem ser impressos: ", end=" ")
    quant = int(input())
    print(desenha_linha(quant))

