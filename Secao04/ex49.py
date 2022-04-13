h = 15
m = 30
s = 10
duracao = 10800
horas = duracao / 3600
minutos = (duracao-(horas*3600))/60
segundos = duracao - (horas*3600)-(minutos*60)
hfinal= h + horas
mfinal= m + minutos
sfinal= s + segundos
print("A hora inicial eh: %d:%d:%d", h, m, s)---
print("\nA hora de duracao da experiencia em segundos eh: %d", duracao)
print("\nA experiencia terminara as: %d:%d:%d", hfinal, mfinal, sfinal )
