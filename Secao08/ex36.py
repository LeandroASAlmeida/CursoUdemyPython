
'''
36. Faca uma funcao nao-recursiva que receba um numero inteiro positivo N e retorne o 
superfatorial desse numero. O superfatorial de um numero Ne definida pelo produto dos 
N primeiros fatoriais de N. Assim, o superfatorial de 4 e sf(4) = 1! * 2! * 3! * 4! = 288.

'''

def super_fat(n):
    fat = 1
    for i in range(1, n+1):# fatorial principal
        for a in range(1, i+1):
            fat *= a
    return fat

if __name__ == '__main__':

    print("Informe um numero inteiro e positivo: ", end=" ")
    num = int(input())
    print(f"Super Fatorial: {super_fat(num)}")


