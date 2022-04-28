'''
Faca um programa que leia dois numeros a e b (positivos menores que 10000) e:
• Crie um vetor onde cada posicao e um algarismo do numero. A primeira posicao e
o algarismo menos significativo;
• Crie um vetor que seja a soma de a e b, mas faca-o usando apenas os vetores
construidos anteriormente.

Dica: some as posicoes correspondentes. Se a soma ultrapassar 10, subtraia 10 do 
resultado e some 1 a proxima posicao

'''
vetor_a =[]
vetor_b =[] 
soma =[]


a= int(input('Informe um numero de 0 á 10000: '))
while a < 0 or a > 10_000:
    a= int(input('Informe um numero de 0 á 10000: '))

b=int(input('Informe outro numero de 0 á 10000: '))
while b < 0 or b > 10_000:
    b=int(input('Informe outro numero de 0 á 10000: '))

string_a = str(a)
string_b = str(b)

for i in range(1, len(string_a)+1):
    vetor_a.append(int(string_a[-i]))

for i in range(1, len(string_b)+1):
    vetor_b.append(int(string_b[-i]))

print(f'Vetor A: {vetor_a}')
print(f'Vetor B: {vetor_b}')

while len(vetor_a) < 5:
    vetor_a.append(0)

while len(vetor_b) < 5:
    vetor_b.append(0)

for i in range(5):
    if vetor_a[i] + vetor_b[i] < 10:
        soma.append(vetor_a[i] + vetor_b[i])
    else:
        soma.append((vetor_a[i] + vetor_b[i]) - 10)
        vetor_a[i+1] += 1

print(f'Soma entre Vetor A e B: {soma}')