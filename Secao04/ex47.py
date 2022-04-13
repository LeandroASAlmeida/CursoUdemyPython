n = int(input('Informe um numero inteiro de 4 digitos de 1000 a 9999: '))
print (f' {str(n % 10000)[0]:>}\n'
      f' {str(n % 1000)[0]:>}\n'
      f' {str(n % 100)[0]:>}\n'
      f' {str(n % 10)[0]:>}\n\n')
      
