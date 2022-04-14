altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))


if altura < 1.20 and peso < 60:
    print('Classificação A')
elif (altura < 1.20 and peso >= 60 and peso <= 90):
        print('Categoria D')
elif (altura < 1.20 and peso > 90):
        print('Categoria G')

if altura >= 1.20 and altura <= 1.70 and peso < 60:
    print('Classificação B')
elif (altura >= 1.20 and altura <= 1.70 and peso >= 60 and peso <= 90):
        print('Categoria E')
elif (altura >= 1.20 and altura <= 1.70 and peso > 90):
        print('Categoria H')

if altura > 1.70 and peso < 60:
    print('Classificação C')
elif (altura > 1.70 and peso >= 60 and peso <= 90):
        print('Categoria F')
elif (altura > 1.70 and peso > 90):
        print('Categoria I')