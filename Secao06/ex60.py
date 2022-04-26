'''
Faca um programa que leia varios numeros, calcule e mostre: 
(a) A soma dos numeros digitados 
(b) A quantidade de numeros digitados 
(c) A media dos numeros digitados 
(d) O maior numero digitado 
(e) O menor numero digitado 
(f) A media dos numeros pares

Finalize a entrada de dados caso o usuario informe o valor 0.

'''

lido_maior = 0
lido_menor = 0
soma=0
quant =0
total = 0
soma_pares = 0
total_pares = 0


while True:
    num = int(input('Digite um número: '))
    if num == 0:
        print('A soma dos numeros digitados : {}'.format(soma))
        print('A quantidade de numeros digitados:{}'.format(total))
        print('A media dos numeros digitados: {}'.format(soma/total))
        print('O maior numero digitado: {}'.format(lido_maior))
        print('O menor numero digitado: {}'.format(lido_menor))
        print('A media dos numeros pares: {}'.format(soma_pares/total_pares))
        break
    else:
        if total == 0:
            lido_maior, lido_menor = num, num
        else:
            if lido_maior < num:
                lido_maior = num
            if lido_menor > num:
                lido_menor = num
        soma += num
        total += 1
        if num % 2 == 0:
            soma_pares += num
            total_pares += 1



