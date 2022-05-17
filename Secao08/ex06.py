'''
6. Faca uma funcao que receba 3 numeros inteiros como parametro, representando horas, 
minutos e segundos, e os converta em segundos

'''

def horas(h, m, s):
    h = h * 3600
    m = m * 60
    s = s + m + h
    return f"Segundos: {s}"

if __name__ == '__main__': #checagem de escopo de execução
    
    print("Informe as horas: ")
    h = int(input())
    print("Informe os minutos: ")
    m = int(input())
    print("Informe os segundos: ")
    s = int(input())
    print(f"{horas(h,m,s)}")
