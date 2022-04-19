'''As tarifas de certo parque de estacionamento sao as seguintes: 
• 1
a e 2a hora - R$ 1,00 cada
• 3
a e 4a hora - R$ 1,40 cada
• 5
a hora e seguintes - R$ 2,00 cada
O numero de horas a pagar e sempre inteiro e arredondado por excesso. Deste modo, 
quem estacionar durante 61 minutos pagara por duas horas, que  e o mesmo que pagaria 
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida
deste sao apresentados na forma de pares de inteiros, representando horas e minutos. 
Por exemplo, o par 12 50 representara “dez para a uma da tarde”. Pretende-se criar um 
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preco cobrado pelo estacionamento. Admite-se que a chegada e a partida se dao com 
intervalo nao superior a 24 horas. Portanto, se uma dada hora de chegada for superior 
a da partida, isso nao e uma situacao de erro, antes significar  a que a partida ocorreu no 
dia seguinte ao da chegada'''


h_entrada = int(input("Digite a hora de entrada \n"))
m_entrada = int(input("Digite os minutos de entrada \n"))
h_saida = int(input("Digite a hora de saída \n"))
m_saida = int(input("Digite os minutos de saída \n"))

# cálculo da permanência

if h_entrada > h_saida:
    hora_final = (h_saida + 24) - h_entrada
else:
    hora_final = h_saida - h_entrada

if m_entrada > m_saida:
    minuto_final = (m_saida + 60) - m_entrada
else:
    minuto_final = m_saida - m_entrada

print(f"A permanência foi de: {hora_final} horas e {minuto_final} minutos \n")

# cálculo do valor

tempo_minutos = hora_final * 60 + minuto_final

if 1 <= tempo_minutos <= 60:
    preco = 1
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 60 < tempo_minutos <= 120:
    preco = 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 120 < tempo_minutos <= 180:
    preco = 4.2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 180 < tempo_minutos <= 240:
    preco = 5.6
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif tempo_minutos > 240:
    preco = hora_final * 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
else:
    print(f"Tempo de permanência mínimo, não será necessário pagar!")

