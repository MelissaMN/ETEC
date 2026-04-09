print("Classificador de Emissões de Veículos")

tipo = input("Tipo de veículo (carro, moto, elétrico): ")
km_mes = float(input("Quantos km o veículo percorre por mês? "))

if tipo == "elétrico":
    print("Emissão zero! Sustentabilidade total.")
elif tipo == "moto" and km_mes < 1000:
    print("Emissão baixa – uso leve e eficiente.")
elif tipo == "moto" or tipo == "carro" and km_mes <= 2500:
    print("Emissão moderada – dentro da média urbana.")
else:
    print("Emissão alta – avalie alternativas mais ecológicas.")