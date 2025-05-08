# Calcular a média de Desceu em cada classe

import pandas as pd

df = pd.read_csv('pedrinhas.csv')

lista_desceu = list(df['desceu'])
lista_classe = list(df['classificacao'])
lista_distancia = list(df['distancia'])

contagem_desceu = [0, 0]
contagem_distancia = [0, 0]
tamanho = [0, 0]

for desceu, distancia, classe in zip(lista_desceu, lista_distancia, lista_classe):
    if classe == 1:
        contagem_desceu[0] += desceu
        contagem_distancia[0] += distancia
        tamanho[0] += 1
    elif classe == 2:
        contagem_desceu[1] += desceu
        contagem_distancia[1] += distancia
        tamanho[1] += 1

total_classes = len(lista_classe)  # Use a different variable name here

media_desceu = [(contagem_desceu[0] / tamanho[0]), (contagem_desceu[1] / tamanho[1])]
media_distancia = [(contagem_distancia[0] / tamanho[0]), (contagem_distancia[1] / tamanho[1])]

print(df)

print("Tamanho:", tamanho[0])

print("[1] Média Desceu:", round(media_desceu[0], 1), "- Média Distancia:", round(media_distancia[0], 1))  # Corrected to print the actual media
print("[2] Média Desceu:", round(media_desceu[1], 1), "- Média Distancia:", round(media_distancia[1], 1))  # Corrected to print the actual media