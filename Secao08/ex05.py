'''5. Faca uma funcao e um programa de teste para o calculo do volume de uma esfera. 
Sendo que o raio e passado por parametro. 
V = 4/3 ∗ π ∗ R3'''


# π = 3.14
def vol_esfera(raio):
    if raio < 1:
        return "Raio Invalido"
    return (4 * 3.14 * (raio ** 3)) / 3
print("Informe o raio da esfera: ", end=" ")
r = float(input())
print(f"\n Volume: {vol_esfera(r):.2f}")
