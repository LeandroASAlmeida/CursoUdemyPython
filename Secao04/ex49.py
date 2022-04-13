
h = 9--
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
print('A hora inicial é:{}:{}:{} '.format (h, m, s))
print('A hora de duracao da experiencia em segundos eh: {}'.format(duracao))
print('A experiencia terminara as:{}:{}:{} '.format(hfinal, mfinal, sfinal))


'''from datetime import datetime, timedelta

inicio = input('Informe o horario de inicio do experimento (formato Horas:Minutos:Segundos): ')
data_inicio = datetime.strptime(inicio, "%H:%M:%S") # transforma a string em data

duracao = input('Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
horas, minutos, segundos = map(int, duracao.split(':'))
# transforma a string em timedelta
duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)
# soma a data à duração
termino = data_inicio + duracao

# formata o resultado
print(termino.strftime('%H:%M:%S'))'''
