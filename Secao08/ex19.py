'''
19. Faca uma funcao que retorne o maior fator primo de um numero.

'''

"""
Como achar o maior fator primo de um número?
Para isso, basta dividir o número pelo seu menor divisor primo.
Na sequência, divide-se o quociente que foi obtido pelo mesmo número primo.
Caso não seja possível, você deve pular para o número primo seguinte e assim
sucessivamente, até obter o resto 1.
"""
import math
  
def maior_f_primo (n):

    mmaiorprimo = -1
    while n % 2 == 0:
        mmaiorprimo = 2
        n >>= 1   
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mmaiorprimo = i
            n = n / i
    if n > 2:
        mmaiorprimo = n
    return int(mmaiorprimo)

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe um numero: ", end=" ")
    n = int(input())
    print(f"O maior fator primo é {maior_f_primo(n)}")

    
