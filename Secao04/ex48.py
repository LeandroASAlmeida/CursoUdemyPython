conversao = (86400, 3600, 60) #Segundos por: dia, hora, minuto

segundoUsuario = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horasRestantes = (segundoUsuario % conversao[0])
minutosRestantes = (horasRestantes % conversao[1])

horas = horasRestantes // conversao[1]
minutos = minutosRestantes // conversao[2]
segundos = minutosRestantes % conversao[2]

print("{} horas, {} minutos e {} segundos.".format(horas, minutos, segundos))

 

