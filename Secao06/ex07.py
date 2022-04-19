'''
Faca um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua
media
'''


soma = 0
valor_valido = 0

valor = int(input("Insira um valor: "))

while True: # enquanto o numero o for maior que 0, faça o processo de somar
    if valor > 0:
        soma = soma + valor
        valor_valido = valor_valido + 1
        if valor_valido == 10: # se chegar em 10 numeros validos  pare.
            break
        valor = int(input("Insira um valor: "))
    else: # senão se valor for < 0  imprima valor inválido e solicite outro valor
        print("Valor inválido")
        valor = int(input("Insira um valor: "))

print(f"A média entre estes valores é {soma/10}")

