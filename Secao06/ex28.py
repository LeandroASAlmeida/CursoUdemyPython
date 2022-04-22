'''
Faca um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a formula a seguir 
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
'''

result = 1
numero=int(input("Digite o número (N):"))

#somamos 1 pois o range termina um número abaixo
fim_loop1=numero+1     

for i in range (1,fim_loop1):
    denominador=1

    #somamos 1 pois o range termina um número abaixo
    fim_loop2=i+1      

    for j in range (1,fim_loop2):
        denominador = denominador * j

    result = (result + (1/denominador))       #ou     #denominador**-1
    #result = result + (denominador)**-1

print (result)