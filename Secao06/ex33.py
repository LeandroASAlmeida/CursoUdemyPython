'''
Dados n e dois numeros inteiros positivos,  i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que sao multiplos de i ou de j e ou de ambos. Exemplo:
Para n = 6, i = 2 e j = 3 a saıda devera ser: 0,2,3,4,6,8.
'''
n = int(input('Digite um número inteiro e positivo para N: '))
i = int(input('Digite um número inteiro e positivo para I: '))
j = int(input('Digite um número inteiro e positivo para J: '))

num = 0
cont = 0

while cont < n:
    if num % i == 0 or num % j == 0 or num % i == 0 and num % j == 0:
        print(num)
        num +=1
        cont += 1
    else:
        num += 1