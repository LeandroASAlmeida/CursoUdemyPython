'''5. Faca uma funcao e um programa de teste para o calculo do volume de uma esfera. 
Sendo que o raio e passado por parametro. 
V = 4/3 ∗ π ∗ R3'''


# π = 3.14
def volume(raio):
    raio_parametro = float(input("Informe o raio da esfera: "))
    return (4/3) * 3.14 * (raio ** 3)

