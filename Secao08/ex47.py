'''
46. Faca uma funcao que receba uma matriz 4 x 4 e retorne quantos valores maiores do que 
10 ela possui.
'''


def maior_dez(args):

    tam = True
    quant = 0

    if len(args) == 4:
        for i in range(len(args)):
            if len(args[i]) == 4:
                for j in range(len(args[i])):
                    if args[i][j] > 10:
                        quant += 1
            else:
                tam = False  
        if tam:
            return quant


matriz = [[-112, 7, 89, 9], [3, 354, -23, -78], [232, 133, 789, -568], [678, 357, 990, 567]]
print(f"Quantidade de valores maiores que 10: {maior_dez(matriz)}")