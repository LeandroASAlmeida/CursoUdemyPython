'''O custo ao consumidor de um carro novo e a soma do custo de fabrica, da comissao
do distribuidor, e dos impostos. A comissao e os impostos sao calculados sobre o custo
de fabrica, de acordo com a tabela abaixo. Leia o custo de fabrica e escreva o custo ao 
consumidor.'''



custo_fab = float(input("Qual o custo de fábrica do carro que você deseja comprar? "))

if custo_fab < 12_000:
    print(f"O preço será de R${custo_fab * 1.05}")
elif custo_fab >= 12_000 and custo_fab <= 25_000:
    print(f"O preço será de R${custo_fab * 1.25}")
elif custo_fab > 25_000:
    print(f"O preço será de R${custo_fab * 1.35}")