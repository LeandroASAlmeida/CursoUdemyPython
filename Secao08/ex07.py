'''
7. Faca uma funcao que receba uma temperatura em graus Celsius e retorne-a convertida 
em graus Fahrenheit. A formula de conversaoe:F = C ∗ (9.0/5.0) + 32.0, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius.

'''

def converte(c):
    return c * (9/5) + 32

if __name__ == '__main__': #checagem de escopo de execução

    print("Informe a temperatura em °C: ",end="")
    grau = float(input())
    print(f"\n Celsius: {grau}°C \n Fahrenheit: {converte(grau)}°F")
