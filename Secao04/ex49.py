
h = 9
m = 20
s = 10
hora_seg= h * 3600
minuto_seg = m *60
duracao = hora_seg + minuto_seg + s
horas = duracao / 3600
minutos = (duracao-(horas*3600))/60
segundos = duracao - (horas*3600)-(minutos*60)
hfinal= h + horas
mfinal= m + minutos
sfinal= s + segundos
print(f'A hora inicial é:{h}:{m}:{s}')
print(f'A hora de duracao da experiencia em segundos eh: {duracao}')
print(f'A experiencia terminara as:{hfinal}:{mfinal}:{sfinal} ')


