'''
43. Faca uma funcao que receba como parametro um vetor X de 30 elementos inteiros e 
retorne, tambem por parametro, dois vetores A e B. O vetor A deve conter os elementos 
pares de X e o vetor B, os elementos ımpares.

'''
def par_impar(x):
    vetor_par= []
    vetor_impar= []

    for num in x:
        if (num % 2 == 0):
            vetor_par.append(num)
        else:
            vetor_impar.append(num)
    print(f'Vetor Par = {vetor_par}\nVetor Impar = {vetor_impar}')
        
if __name__ == '__main__':
    
    cont = 0
    x=[]
    while (len(x) < 30):
        cont +=1
        n=int(input(f'Informe o {cont}° numero do VetorX :'))
        x.append(n)
   
   
