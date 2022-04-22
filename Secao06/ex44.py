'''Leia um numero positivo do usuario, entao, calcule e imprima a sequencia Fibonacci ate
o primeiro numero superior ao numero lido. Exemplo: se o usuario informou o numero 
30, a sequencia a ser impressa ser a 0 1 1 2 3 5 8 13 21 34'''


num = int(input("Digite um número inteiro e positivo: "))
if num > 0:# se num for maior que zerto
    t1 = 0
    t2 = 1
    print(f'{t1} - {t2}',end='') # end'' = não pular linha
    while t2 < num:#enquanto o termo 2 for menor que o num
        t3 = t1 + t2 # o termos 3 vai ser o termos 1 + o termos2
        print(f' - {t3}',end='')
        t1 = t2 # vai modificando  as proximas casas para somar os proximos numeros.
        t2 = t3 # vai modificando  as proximas casas para somar os proximos numeros.
    print(' - FIM')
else:
    print('Número inválido.')

   

