# missao_espacial.py
# Programa para calcular o tempo de uma viagem espacial
# Desenvolvido por Marcio

# Saudação inicial
print("=== Simulador de Missão Espacial ===")

# Entrada de dados
nome = input("Digite seu nome completo, astronauta: ")

distancia = float(input("Digite a distância da viagem em km: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))

# Cálculos
tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

# Saída de dados
print("\nAstronauta", nome + ", bem-vindo à simulação!")
print("A viagem terá uma distância de", distancia, "km.")
print("Com velocidade média de", velocidade, "km/h, o tempo estimado é:")

print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")

print("Boa sorte na missão astronaura!!!")