'''Faca um programa que leia um numero indeterminado de idades de indivıduos (pare
quando for informada a idade 0), e calcule a idade media desse grupo.'''




idade = int(input("Insira uma idade:"))
soma = 0
cont = 0

while idade != 0:
    if idade < 0:
        print("Idade inválida")
        idade = int(input("Insira uma idade: "))
    soma += idade
    cont += 1
    idade = int(input("Insira uma idade: "))


print(f"A media entre as idades será {soma / cont}.")

    

