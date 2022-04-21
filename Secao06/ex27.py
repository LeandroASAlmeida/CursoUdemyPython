'''
Em Matematica, o numero harmonico designado por H(n) define-se como sendo a soma
da serie harmonica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Faca um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
'''
h_n = float()

print('Encontrando o número harmônico H(n):')
print('H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n\n')
n = int(input('Digite o valor de n: '))

for i in range(1, n+1):
    h_n += (1 / i)

print(f'H(n) = {h_n}')
