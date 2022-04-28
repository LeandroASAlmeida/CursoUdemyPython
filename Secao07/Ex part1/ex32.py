'''Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuario nao
informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso
abaixo:
• Soma entre x e y: soma de cada elemento de x com o elemento da mesma posicao
em y.
• Produto entre x e y: multiplicacao de cada elemento de x com o elemento da mesma
posicao em y.
• Diferenca entre x e y: todos os elementos de x que nao existam em  y.
• Intersecao entre x e y: apenas os elementos que aparecem nos dois vetores.
• Uniao entre  x e y: todos os elementos de x, e todos os elementos de y que nao
estao em x.'''

x=[]
y=[]
soma=[]
prod=[]
contx =0
conty =0


print('VETOR X:')
while contx < 5:
    num = int(input(f"Digite um valor para o vetor ({contx+1}/5): "))
    if num in x:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        x.append(num)
        contx += 1

print('VETOR Y:')
while conty < 5:
    num = int(input(f"Digite um valor para o vetor ({conty+1}/5): "))
    if num in y:
        print("Este número já foi digitado anteriomente! Digite outro número.")
    else:
        y.append(num)
        conty += 1

for calculo in range(5):
    vlr_soma = x[calculo] + y[calculo]
    soma.append(vlr_soma)
    vlr_prod = x[calculo] * y[calculo]
    prod.append(vlr_prod)


x = set(x)
y = set(y)

dif = x.difference(y)
union = x.union(y)
inter = x.intersection()

print(f'A Soma entre elementos na mesma posição: {soma}')
print(f'Produto entre elementos de mesma posição: {prod}')
print(f'Diferença de x para y: {dif}')
print(f'União entre os vetores: {union}')
print(f'Intersecção entre os vetores: {inter}')





