'''
14. Faca uma funcao que receba a distancia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:

CONSUMO (Km/l) MENSAGEM
menor que 8 Venda o carro!
entre 8 e 14 Economico! 
maior que 12 Super economico! 

'''

def consumo(km, l):
    if km/l < 8:
        return "Venda o Carro!"
    
    elif km/l > 8 and km/l < 14:
        return "Econômico!"
    else:
        return "Super Econômico!"
    
if __name__ == '__main__': #checagem de escopo de execução

    print("Informe os Km : ", end=" ")
    km = float(input())
    print("Informe o quanto de gasolina foi gasto: ", end=" ")
    l = float(input())
    print("\n", consumo(km, l))

