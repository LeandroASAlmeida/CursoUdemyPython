'''Faca um programa que calcule e mostre a area de um trapezio. Sabe-se que: 
A =
(basemaior + basemenor) ∗ altura
2'''


base_maior = float(input('Informe a maior base do trapezio: '))
base_menor = float(input('Informe a menor base do trapezio: '))
altura = float(input('Informe a altura trapezio: '))

if base_maior and base_menor > 0 :
    a=(base_maior + base_menor * altura)/2
    print('A area total do trapezio é de {}' .format(a))
else:
    print('Numero das bases está incorreto')