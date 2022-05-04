'''
12. Escreva uma funcao que receba um numero inteiro maior do que zero e retorne a soma 
de todos os seus algarismos. Por enumemplo, ao numero 251 correspondera o valor 8 (2 
+ 5 + 1). Se o numero lido nao for maior do que zero, o programa terminara com a 
mensagem “Numero invalido”

'''

def soma(num):
    r = 0
    num = list(str(num))
    
    for i in range(len(num)):
        r += int(num[i])
    return r
print("Informe um numero inteiro: ", end=" ")
n = int(input())
if n < 1:
    print(f"{n} e invalido.")
else:
    print(f"Soma dos algoritimos de {n} e {soma(n)}")
