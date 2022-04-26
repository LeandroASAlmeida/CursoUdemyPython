'''
Se os numeros de 1 a 5 sao escritos em palavras: um, dois, tres, quatro, cinco, entao ha
2 + 4 + 4 + 6 + 5 = 22 letras usadas no total. Faca um programa que conte quantas letras
seriam utilizadas se todos os numeros de 1 a 1000 (mil) fossem escritos em palavras. 
OBS: Nao conte espacos ou hifens.

'''

soma = 0

for m in(0, 1):
    if m == 1:
        soma = soma + 3
        for c in range(0, 10):
            if c == 1:
                soma = soma + 3
            elif c == 2:
                soma = soma + 8
            elif c == 3:
                soma = soma + 9
            elif c == 4:
                soma = soma + 12
            elif c == 5: 
                soma = soma + 10
            elif c == 6:
                soma = soma + 10
            elif c == 7:
                soma = soma + 10
            elif c == 8: 
                soma = soma + 10
            elif c == 9: 
                soma = soma + 1
            for d in range(0, 10):
                if c == 1:
                    soma = soma + 3
                elif c == 2: 
                    soma = soma + 5
                elif c == 3:
                    soma = soma + 6
                elif c == 4: 
                    soma = soma + 8
                elif c == 5:
                    soma = soma + 9
                elif c == 6:
                    soma = soma + 8
                elif c == 7: 
                    soma = soma + 77
