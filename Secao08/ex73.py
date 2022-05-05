from questao import question
from MMC import MMC
from collections import defaultdict
from pynput import keyboard
from fractions import Fraction
import math
import random
import numpy as np
import pandas as pd




question(1)
def dobro(n):
    return n * n
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"O dobro de {num} e {dobro(num)}")
question(2)
meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro"]
def data(x):
    if len(x) > 10:
        return "Data Invalida."
    
    elif int(x[3:5]) > 12 or int(x[:2]) > 31:
        return "Data Invalida."
    else:
        return f"Data: {x}   Data por extenso: {x[:2]} de {meses[int(x[3:5]) - 1]} de {x[6:10]}"
print("Informe a data: ", end=" ")
d = input()
print("\n", data(d))
question(3)
def verificar(n):
    if n > 0:
        return " 1"
    
    elif n < 0:
        return " -1"
    elif n == 0:
        return " 0"
print("Informe um numero: ", end=" ")
num = float(input())
print("\n",verificar(num))
question(4)
lista = [i * i for i in range(101)] 
def quad_perfeito(n):
    if n in lista:
        return "Quadrado perfeito"
    
    return "Não Quadrado Perfeito"
print("Informe um numero inteiro positivo: ", end=" ")
num = int(input())
print("\n", quad_perfeito(num))
question(5)
def vol_esfera(raio):
    if raio < 1:
        return "Raio Invalido"
    return (4 * 3.14 * (raio ** 3)) / 3
print("Informe o raio da esfera: ", end=" ")
r = float(input())
print(f"\n Volume: {vol_esfera(r):.2f}")
question(6)
def horas(h, m, s):
    h = h * 3600
    m = m * 60
    s = s + m + h
    return f"Segundos: {s}"
print("Informe as horas: ")
h = int(input())
print("Informe os minutos: ")
m = int(input())
print("Informe os segundos: ")
s = int(input())
print(f"{horas(h,m,s)}")
question(7)
def converte(c):
    return c * (9/5) + 32
print("Informe a temperatura em °C: ",end="")
grau = float(input())
print(f"\n Celsius: {grau}°C \n Fahrenheit: {converte(grau)}°F")
question(8)
def hipotenusa(a, b):
    h = math.sqrt((a**2 + b**2))
    return h
print("Informe o cateto A: ", end=" ")
a = int(input())
print("Informe o cateto b: ", end=" ")
b = int(input())
print(f"\n Hipotenusa = {hipotenusa(a, b)}")
question(9)
def volume(r, a):
    return 3.141592 * (r ** 2) * a
print("Informe a altura do cilindro: ", end=" ")
a = float(input())
print("Informe o raio do cilindro: ", end=" ")
r = float(input())
print(f"Volume: {volume(r, a)}")
question(10)
def maior(a, b):
    if a > b:
        return f"Maior: {a}"
    return f"Maior: {b}"
print("Informe o 1° numero: ", end=" ")
n1 = float(input())
print("Informe o 2° numero: ", end=" ")
n2 = float(input())
print("\n", maior(n1,n2))
question(11)
def nota(l, *args):
    if l == "p" or l == "P":
        return ((args[0] * 5) + (args[1] * 3) + (args[2] * 2)) / (5+3+2)
    
    elif l == "a" or l == "A":
        return sum(args) / 3
    else:
        return f"{l} invalido."
notas = []
for i in range(1,4):
    print(f"Informe a {i}° nota: ", end=" ")
    n = float(input())
    notas.append(n)
print("""\n
 Informe o tipo de media:
 P -> Media Ponderada
 A -> Media Aritmética
 Media: """, end=" ")
op = input()
print(f"\nNota: {nota(op, *notas)}")
question(12)
def soma(x):
    r = 0
    num = list(str(x))
    
    for i in range(len(num)):
        r += int(num[i])
    return r
print("Informe um numero inteiro: ", end=" ")
n = int(input())
if n < 1:
    print(f"{n} e invalido.")
else:
    print(f"Soma dos algoritimos de {n} e {soma(n)}")
question(13)
def operacao(x, y, op):
    if op == "+":
        return f"Soma: {x+y}"
    elif op == "-":
        return f"Subtração: {x+y}"
    elif op == "*":
        return f"Multiplicação: {x*y}"
    elif op == "/":
        return f"Divisão: {x/y}"
    else:
        return "Operador Invalido"
    
print("Informe o 1° numero: ", end=" ")
n1 = float(input())
print("Informe o 2° numero: ", end=" ")
n2 = float(input())
print("""\n
 Informe a operação:
 + -> Soma
 - -> Subtração
 * -> Multiplicação
 / -> Divisão
 Operação: """, end=" ")
op = input()
print("\n", operacao(n1, n2, op))
question(14)
def consumo(km, l):
    if km/l < 8:
        return "Venda o Carro!"
    
    elif km/l > 8 and km/l < 14:
        return "Econômico!"
    else:
        return "Super Econômico!"
print("Informe os Km percorridos: ", end=" ")
km = float(input())
print("Informe a quantidade de gasolina gasta: ", end=" ")
l = float(input())
print("\n", consumo(km, l))
question(15)
def triangulo(a, b, c):
    if a - b < c < b + a:
        if a == b == c:
            return 'Equilátero'
        
        elif a == b or c == a:
            return 'Isósceles'
        else:
            return 'Escaleno'
    return "triangulo invalido."
print("Lado A: ", end=" ")
n1 = int(input())
print("Lado B: ", end=" ")
n2 = int(input())
print("Lado C: ", end=" ")
n3 = int(input())
print(f"\n Triangulo {n1} {n2} {n3} e {triangulo(n1,n2,n3)}")
question(16)
def desenhaLinha(n):
    return '='*n
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print("\n",desenhaLinha(num))
question(17)
def soma2(x, y):
    soma = 0
    
    if x > y:
        for i in range(y+1, x):
            soma += i
            
    else:
        for i in range(x+1, y):
            soma += i 
    return soma
print("Informe N1: ", end=" ")
n1 = int(input())
print("Informe N2: ", end=" ")
n2 = int(input())
print(f"Soma: {soma2(n1,n2)}")
question(18)
def potencia(x, z):
    return x ** z
print("Informe o numero: ", end=" ")
num = float(input())
print("Informe a potenciação : ", end=" ")
pot = int(input())
print(f"Potenciação: {potencia(num, pot)}")
question(19)
def primo(n):
    c = 2
    num = 0
    primos = {2,2,2}
    
    while True:
        if n % c != 0:
            c += 1
        else:
            num = n // c
            n = num
            primos.add(c)
            
            if n // c == 1:
                primos.add(n)
                break
    return max(primos)
print("Informe um numero: ", end=" ")
num = int(input())
print(f"\nMaior fator primo de {num} e {primo(num)} ")
question(20)
def fatorial(n):
    fat = 1
    
    for i in range(1, n+1):
        fat = fat * i
    return fat
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"Fatorial de {num} e {fatorial(num)}")
question(21)
def primos(n):
    numeros = set()
    
    for x in range(1, n):
        for y in range(1, x+1):
            if y == 1 or y == x:
                if y != 1: numeros.add(y)
            elif x % y == 0:
                break
	    
    return numeros
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print("Lista de Numeros Primos: ")
for item in primos(num):
    print(item, end=" ")
question(22)
def espaco(n):
    lista = list()
    for i in range(n+1):
        lista.append("!"*i)
    return lista
print("Informe um numero inteiro: ", end=" ")
num = int(input())
for item in espaco(num):
    print(item)
question(23)
def lateral(n):
    for i in range(n):
        print("*" * i)
        
    for i in range(n):
        print("*" * (n - i) )
    return "\n"
print("Informe um numero: ", end=" ")
num = int(input())
print(lateral(num))
question(24)
def meio(n):
    for i in range(-1,n*2+1,2):
        print(" " * int(((n*2)-i)/2),end=" ")
        print("*" * i)
    return "\n"
print("Informe um numero: ", end=" ")
num = int(input())
print(meio(num))
question(25)
def serie(n):
    d = defaultdict(list)
    res = 0
    print("\n")
    for i in range(1, n+1):
        print((i**2) + 1,"/",(i + 3))
        d["num"].append((i**2) + 1)
        d["deno"].append((i + 3))
    print("\n")
    x = MMC(d["deno"])
    for i in range(n):
        foo = (x / d["deno"][i]) * d["num"][i]
        d["soma"].append(foo)
    res = sum(d["soma"]) / x
    return res
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"S: {serie(num):.2f}")
question(26)
def soma(n):
    r = 0
    for i in range(1, n+1):
        r += i
    return r
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"Somatoria: {soma(num)}")
question(27)
def taylor(n, t):
    serie = defaultdict(list)
    foo = 1
    rad = (n * (2 * 3.141593)) / 360
    rad = int(rad) if int(rad) < 5 else 5
    if t == "1" or t == "3": # questoes 27 e 29
        for i in range(1, rad+1):
            serie["num"].append(i ** (2 * i + 1))
            for x in range(1, (2 * i + 1)+1):
                foo *= x
                
            serie["deno"].append(foo)
            foo = 1
    elif t == "2" or t == "4": # questoes 28 e 30
        for i in range(1, rad+1):
            serie["num"].append(i ** (2*i))
            for x in range(1, (2*i)+1):
                foo *= x
            serie["deno"].append(foo)
            foo = 1
    else:
        return "error"
    x = MMC(serie["deno"])
    
    for i in range(rad):
        foo = (x / serie["deno"][i]) * serie["num"][i]
        serie["soma"].append(foo)
    res = sum(serie["soma"]) / x
    if t == "1" or t == "3": # questoes 27 ou 29
        return rad - res if t == "1" else rad + res
    
    elif t == "2" or t == "4": # questoes 28 ou 30
        return 1 - res if t == "2" else 1 + res
print("Informe o angulo: ", end=" ")
seno = int(input())
print(f"{taylor(seno, str(1)):.2f} sen")
question(28)
print("Informe o angulo: ", end=" ")
coss = int(input())
print(f"{taylor(coss, str(2)):.2f} coss")
question(29)
print("Informe o angulo: ", end=" ")
seno = int(input())
print(f"{taylor(seno, str(3)):.2f} seno hiperbólico")
question(30)
print("Informe o angulo: ", end=" ")
coss = int(input())
print(f"{taylor(coss, str(4)):.2f} cosseno hiperbólico")
question(31)
def neperiano(n):
    nap = 0
    serie = defaultdict(list)
    foo = 1
    
    for i in range(n+1):
        if i == 0:
            serie["deno"].append(1)
            
        else:
           
            for x in range(1, i+1):
                foo *= x
            serie["deno"].append(foo)
            foo = 1
        
    x = MMC(serie["deno"])
    for i in range(n+1):
        nep = (x / serie["deno"][i]) * 1
        serie["soma"].append(nep)
    nep = sum(serie["soma"]) / x
    return nep
print("Informe um numero: ", end=" ")
num = int(input())
print(f"Neperiano: {neperiano(num)}")
question(32)
def simples(a,b):
    c = 2
    while a > 1:
        if a % c != 0 and b % c != 0:
            c += 1
        elif c > a or c > b:
            c = 2
        else:
            a = a / c
            b = b / c
            if a / c < 1 or b / c < 2:
                return  a, b
print("Informe o numerador: ", end=" ")
num = int(input())
print("Informe o denomiador: ", end=" ")
deno = int(input())
foo = simples(num, deno)
print(f"Fração: {num} / {deno} \n Simlificado: {foo[0]} / {foo[1]}")
question(33)
def somar(n):
    num = 1
    soma = 0
    for i in range(1, n+1):
        num *= i
    num = list(str(num))
    
    for i in range(len(num)):
        soma += int(num[i])
        
    return soma
print("Informe um numero inteiro: ", end=" ")
num = int(input())
print(f"Soma: {somar(num)}")
question(34)
def fatduplo(n):
    soma = 1
    for i in range(1, n+1,2):
        soma *= i
    return soma
print("Informe um numero: ", end=" ")
num = int(input())
print(f"Fatorial duplo: {fatduplo(num)}", end=" ")
question(35)
def fatquad(n):
    soma = 1
    foo = 2 * n
    for i in range(1 , foo+1):
        soma *= i
    foo = 1
    for i in range(1, n+1):
        foo *= i
    return soma / foo
print("Informe um numero: ", end=" ")
num = int(input())
print(f"Fatorial quaduplo: {fatquad(num)}")
question(36) # superfatorial
def sf(n):
    fat = 1
    for i in range(1, n+1):
        for a in range(1, i+1):
            fat *= a
    return fat
print(sf(5))
question(37)
def hf(n): # hiperfatorial
    x = 1
    for i in range(1, n+1):
        x = x * (i ** i)
    return x
print("Informe um numero: ", end=" ")
num = int(input())
print(hf(num))
question(38)
def fat_exp(n):
    res = 1
    for i in range(n-1):
        res *= n ** (n-i)
    return res
                
print("Informe um numero: ",end=" ")
num = int(input())
print(fat_exp(num))
question(39)
def Troque(x, y):
    global a, b
    a = y
    b = x
    
print("Informe o valor de A : ", end=" ")
a = int(input())
print("Informe o valor de B : ", end=" ")
b = int(input())
print("\nOriginais: A -> ", a," / B -> ", b)
Troque(a, b)
print("\nInversos: A -> ", a," / B -> ", b)
question(40)
def pares(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
    return count
print("Informe o tamanho do vetor: ", end=" ")
tam = int(input())
vetor = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° valor do vetor: ", end=" ")
    valor = int(input())
    vetor.append(valor)
print("\nExiste(m) ", pares(vetor), " Valor(es) Par(es) no Vetor")
question(41)
def maior(list):
    maior = 0
    for i in list:
        if  i > maior:
            maior = i
    return maior
print("Informe o tamanho do vetor: ", end=" ")
tam = int(input())
vetor = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° valor do vetor: ", end=" ")
    valor = int(input())
    vetor.append(valor)
print("\nO maior valor do vetor e", maior(vetor))
question(42)
def media(list):
    media = 0
    for i in list:
        media += i
    return media / len(list)
print("Informe o tamanho do vetor: ", end=" ")
tam = int(input())
vetor = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° valor do vetor: ", end=" ")
    valor = float(input())
    vetor.append(valor)
print("\nA media do vetor e", media(vetor))
question(43)
def rng(lst):
    print("\nOriginal: ", lst)
    lst2 = lst.copy()
    length = len(lst)
    lst.clear()
    while len(lst) != length:
        num = random.randrange(0,100)
        if num not in lst and num not in lst2:
            lst.append(num)
    return lst
print("Informe o tamanho do vetor: ", end=" ")
tam = int(input())
vetor = []
print("\n")
for i in range(tam):
    print("Informe o ", i+1 ,"° valor do vetor: ", end=" ")
    valor = int(input())
    vetor.append(valor)
print("\nRandom: ", rng(vetor))
question(44)
def p_i(lst):
    
    lst.sort()
    pares = []
    impares = []
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return [pares,impares]
        
vetor = []
while len(vetor) != 30:
    num = random.randrange(0,100)
    if num not in vetor:
        vetor.append(num)
x = p_i(vetor)
vetor.sort()
print("\n Vetor Orginal: ", vetor,
      "\n\n Pares: ", x[0],
      "\n\n Impares: ", x[1])
question(45)
vetor = []
num = 0
while len(vetor) != 10:
    num = random.randrange(1,100)
    if num not in vetor:
        vetor.append(num)
print("Desvio Padrao: ", np.std(vetor))
question(46)
vetor = []
vet2 = []
def menu():
    global vetor
    global vet2
    
    
    print("Escolha a função: " +
          "\n 1. Impressão normal do vetor." +
          "\n 2. Imperssao Inversa. " +
          "\n 3. Média Aritmetica. " +
          "\n Escolha: ", end=" ")
    esc = int(input())
    if esc == 1:
        print("\nVetor: ", vet())
    elif esc == 2:
        vet2.reverse()
        print("\nVetor Inverso: ", vet2)
        
    elif esc == 3:
        print("\nMedia Aritimetica: ", media(vetor))
    else:
        print("Opção desconhecida.")
    print("\n\n")
def vet():
    num = random.randrange(4,11)
    global vetor
    global vet2
    if len(vetor) == 0:
        for i in range(num):
            num = random.randrange(1,50)
            vetor.append(num)
   
    vet2 = list(vetor.copy())
    return vetor
def media(lst):
    return sum(lst) / len(lst)
vet()
while True:
    menu()
question(47)
matriz = []
count = 0
for a in range(4):
    matriz.append([])
    
    for b in range(4):
        num = random.randrange(50)
        if num > 10: count += 1
        
        matriz[a].append(num)
print(matriz,"\n\n",count)
question(48)
matriz = []
for a in range(3):
    matriz.append([])
    for b in range(3):
        num = random.randrange(0,50)
        matriz[a].append(num)
print("Matriz:\n", matriz[0], "\n", matriz[1], "\n", matriz[2])
print("\n Soma Acima: ",sum([matriz[0][1], matriz[0][2],matriz[1][2]]))
question(49)
print("\n Soma Abaixo: ",sum([matriz[1][0], matriz[2][0],matriz[2][1]]))
question(50)
print("\n SOma Diagonal principal: ",sum([matriz[0][0], matriz[1][1],matriz[2][2]]))
question(51)
print("\n SOma Diagonal principal: ",sum([matriz[0][2], matriz[1][1],matriz[2][0]]))
question(52)
def transposta(matriz):
    print("Matriz: \n")
    print(matriz[0])
    print(matriz[1])
    print(matriz[2],"\n")
    trs = []
    
    for a in range(len(matriz)):
        trs.append([])
        
        for b in range(len(matriz)):
            trs[a].append(matriz[b][a])
    print("\n")
    return trs
N = 3 #random.randrange(1,4)
matriz = []
for a in range(N):
    matriz.append([])
    for b in range(N):
        num = random.randrange(1,10)
        matriz[a].append(num)
matriz = transposta(matriz)
print("Transposta: \n")
for i in range(N):
    print(matriz[i])
question(53)
def identidade(matriz):
    for a in range(len(matriz)):
        if matriz[a][a] == 1:
            pass
        else:
            return "Matriz não identidade"
            
            
        for b in range(len(matriz)):
            if matriz[a][b] != 0:
                if a == b:
                    pass
                else:
                    return "Matriz não e identidade"
            
    return "Matriz é identidade"
                    
matriz = [[1,0,0],[0,1,0],[0,0,1]]
print(identidade(matriz))
for i in range(3):
    print(matriz[i])
question(54)
def soma(matriz):
    res = 0
    resD = 0 # Diagonais
    
    for a in range(len(matriz)):
        resD += matriz[a][a] + matriz[a][-a - 1]
        for b in range(len(matriz[a])):
            res  += matriz[a][b]
    return res, resD
N = 4 #random.randrange(2,4)
matriz = []
for i in range(N):
    matriz.append([])
    for j in range(N):
        matriz[i].append(random.randrange(1,10))
x = soma(matriz)
print("Soma dos elements: ", x[0])
print("\nMatriz: ")
for i in range(N):
    print(matriz[i])
question(55)
print("\nSoma das Diagonais: ", x[1])
question(56)
def soma(matriz, lin):
    l = 0
    c = 0
    
    for i in range(7):
        l += matriz[i][lin]
        if i != 6: c += matriz[lin][i]
    return [l,c]
matriz = []
N = random.randrange(0,6)
for i in range(7):
    matriz.append([])
    for j in range(6):
        matriz[i].append(random.randrange(1,10))
print("Matriz: ")
x = pd.DataFrame(matriz)
print(x)
r = soma(matriz, N)
print("\nSoma da linha", N, "° :", r[0])
question(57)
print("\nSoma da coluna", N,"° : ", r[1])
question(58)
def produto(x, y):
    matriz = np.matmul(x,y)
    return matriz
N = 2
mat1 = []
mat2 = []
for i in range(N):
    mat1.append([])
    mat2.append([])
    for j in range(N):
        mat1[i].append(random.randrange(1,11))
        mat2[i].append(random.randrange(1,11))
print("Matriz A: ", pd.DataFrame(mat1).to_string(index=False),"\n\n")
print("Matriz B: ", pd.DataFrame(mat2).to_string(index=False),"\n\n")
print("Produto: ", pd.DataFrame(produto(mat1, mat2)).to_string(index=False))
question(59)
def uniao(a,b):
    c = set(a+b)
    return list(c)
A = []
B = []
for i in range(10):
    A.append(random.randrange(1,100))
    B.append(random.randrange(1,100))
print("Vetor A: ", A,"\n\n")
print("Vetor B: ", B,"\n\n")
print("União: ",uniao(A,B))
question(60)
def sub(pal):
    
    if type(pal) != str:
        return -1
    return pal[0:1]
print("Informe uma palavra: ", end=" ")
p = input()
print(f"\n\n Sub-String: {sub(p)}")
question(61)
def anagrama(pA, pB):
    
    if len(pA) != len(pB):
        return "Não e Anagrama"
    elif set(pA) == set(pB):
        return "É Anagrama"
    else:
        return "Não e Anagrama"
while True:
    print("Informe a palavra A: ", end=" ")
    A = input()
    print("Informe a palavra B: ", end=" ")
    B = input()
    print(anagrama(A,B))
question(62)
def tam(a):
    #void tamanho(char *str, int *strsize)
    return len(a)
print("Informe uma palavra: ", end=" ")
pal = input()
print(f"\n\nTamanho da palavra e {tam(pal)}")
print(tam.__doc__)
question(63)
def iguais(a, b):
    if a == b:
        return "As palavras são iguais"
    else:
        return "As palavras são diferentes"
print("Informe a primeira palavras: ", end=" ")
a = input()
print("\n\nInforme a segunda palavra: ", end=" ")
b = input()
print(f"\n\nR: {iguais(a,b)}")
question(64)
def foo(str1, str2):
    x = str1 + " " + str2
    y = str2 + " " + str1
    return [x,y]
print("Informe a primeira palavra: ",end=" ")
a = input()
print("\nInforme a segunda palavra: ", end=" ")
b = input()
print(f"\nStr 1 : {foo(a,b)[0]}")
print(f"\nStr 2 : {foo(a,b)[1]}")
question(65)
def somar(str1, str2, n):
    if n > len(str1):
        str2 += str1[::]
        str1 = None
        
    else:
        str2 += str1[0:n]
        str1 = None
    return [str1,str2]
print("Informe um numero inteiro positivo: ", end=" ")
num = int(input())
print("\nPrimeira palavras: ", end=" ")
a = input()
print("\nSegunda Palavra: ", end=" ")
b = input()
print(f"\n\nStr1: {somar(a,b,num)[0]}")
print(f"\n\nStr2: {somar(a,b,num)[1]}")
question(66)
def maiusculo(x):
    return x.upper()
print("Informe uma letra: ", end=" ")
a = input()
print(maiusculo(a[:1]))
question(67)
def getchar():
    vetor = []
    x = ""
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.enter:
                break
            else:
                if len(vetor) == 12 or len(vetor) > 12:
                    break
                else:
                    x = str(event)[11:12]
                    if x == "=":
                        pass
                    else:
                        vetor.append(x)
            #print(event)
    print(vetor)  
getchar()
question(68)
def intercala(str1, str2):
    c = 0
    str3 = []
    while True:
        try:
            str3.append(str1[c] + str2[c])
            c += 1
        except IndexError:
            break
    if len(str1) > len(str2):
        for i in range(len(str1)-c):
            str3.append(str1[c])
            c += 1
    if len(str2) > len(str1):
        for i in range(len(str2)-c):
            str3.append(str2[c])
            c += 1
    
    return str(str3)
print("Informe a primeira palavra: ", end=" ")
s1 = input()
print("Informe a segunda palavra: ", end=" ")
s2 = input()
s1 = intercala(s1, s2)
print(f"Intercalaçõ: {s1}")
question(69)
p = [] #numeradores
q = [] #demoninadores
def fracao():
    global p
    global q
    print("Informe o numerador da primeira fração : ", end=" ")
    p.append(int(input()))
    print("\nInforme o denominador da primeira fração : ", end=" ")
    q.append(int(input()))
    print("\nInforme o numerador da segunda fração : ", end=" ")
    p.append(int(input()))
    print("\nInforme o denominador da segunda fração : ", end=" ")
    q.append(int(input()))
def simplificar():
    global p
    global q
    mdc = math.gcd(q[0], q[1])
    print(f"\n\nSimplificado Fração 1:\n {p[0]/mdc} / {q[0]/mdc}\n")
    print(f"Simplificado Fração 2:\n {p[1]/mdc} / {q[1]/mdc} \n")
def operacoes():
    soma = Fraction(p[0], q[0]) + Fraction(p[1], q[1])
    print(f"Soma: {soma} \n\n")
    sub = Fraction(p[0], q[0]) - Fraction(p[1], q[1])
    print(f"Subtração: {sub} \n\n")
    mult = Fraction(p[0], q[0]) * Fraction(p[1], q[1])
    print(f"Multiplicação: {mult} \n\n")
    quo = sub = Fraction(p[0], q[0]) / Fraction(p[1], q[1])
    print(f"Divisão: {quo}\n\n")
    
fracao()
simplificar()
operacoes()
question(70)
def reduz(a,b):
    return a / b
print("Informe a: ", end=" ")
a = float(input())
print("\nInforme b: ", end=" ")
b = float(input())
print(f"\nReduz: {reduz(a,b):.4f}")
def neg(a):
    return a * (-1)
print("\nInforme um numero inteiro positivo: ", end=" ")
num = int(input())
print(f"\nNegativo: {neg(num)}")
def soma(a,b):
    return a + b
print(f"\nSoma: {soma(a, b)}")
def produto(a, b):
    return a * b
print(f"\nProduto: {produto(a, b):.3f}")
def divisao(a, b):
    return a / b
print(f"\nDivisao: {divisao(a, b):.3f}")
question(71)
coord = [2, 4]
def dentroRet(v1, v2):
    cX = [0,0]
    cY = [10, 10]
    dentro = 0
    if v1 > cX[0] and v2 > cX[1]:
        if v2 < cY[0] and v2 < cY[1]:
            dentro = 1
    return dentro
print(f"Ponto: {dentroRet(coord[0], coord[1])}")
question(72)
vetor = [[1,2,3], [1,1,1], []]
def soma(v1, v2, res):
    res.append(sum(v1))
    res.append(sum(v2))
    return res
print(soma(vetor[0], vetor[1], vetor[2]))
question(73)
# pessoa = {0:["M", "A", "L", 15],1:["F", "C", "P", 22],2:["F","A","L",25],3:["M","C","C",33],4:["M","A","C",40]}
pessoa = {0:[],1:[],2:[],3:[],4:[]}
def leitor():
    global pessoa
    print("Adiciona as informçoes a seguir: " +
          "\n 1. Sexo " +
          "\n 2. Cor dos Olhos (A = Azuis ou C = Castanhos) " +
          "\n 3. Cor dos Cabelos (L = Louros, P = Pretos ou C = Castanhos)" +
          "\n 4. Idade\n")
    for i in range(5):
        print(f"\nInformações do {i+1}° Habitante: \n")
        for j in range(4):
            print(f"\n Adicione a {j+1}° informação: ", end=" ")
            if j < 3:
                info = input().lower()
            else:
                info = int(input())
            pessoa[i].append(info)
    return pessoa
def media(lst):
    media = []
    for i in range(len(lst)):
        if lst[i][1].casefold() == "c" and lst[i][2].casefold() == "p":
            media.append(lst[i][3])
    if len(media) > 0:
        media = sum(media) / len(media)
        return f"Media = {media}"
    
    else:
        return "Media = 0"
def maior(lst):
    mir = 0
    for i in range(len(lst)):
        if lst[i][3] > mir:
            mir = lst[i][3]
    return mir
def test_(lst):
    count = 0
    # Mulher, entre 18 e 35, olhos azuis e cabelos loiros
    
    for i,k in lst.items():
        if k[0].casefold() == "f" and 35 >= k[3] >= 18 and k[1].casefold() == "a" and k[2].casefold() == "l":
            count += 1
    return count
    return
print(leitor())
print(media(pessoa))
print(maior(pessoa))
print(test_(pessoa))
