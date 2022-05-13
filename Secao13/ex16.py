"""
16. Faça um programa que recebe um vetor de 10 números, converta cada um desses
números para binário e grave a sequência de Os e 1s em um arquivo texto. Cada número deve ser gravado em uma linha.

"""
vetor= []

for n in range(0,10):
            num =int(input(f'Informe {n+1}-[10] valores inteiros: '))
            vetor.append(num)

if len(vetor) != 10:
    with open("arquivos/binarios.txt", "w") as arquivo: #arquivos/binarios.txt
        for numero in vetor:
            elemento = str(numero)
            num = int(elemento)
            binario = format(num, "b")
            arquivo.write(f"{binario}\n")

        print("\nInformações inseridas no arquivo com sucesso!")


