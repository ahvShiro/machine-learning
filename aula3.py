# Calcular a média de Desceu em cada classe

import pandas as pd

df = pd.read_csv('pedrinhas.csv')

lista_desceu = list(df['desceu'])
lista_classe = list(df['classificacao'])

contagem = [0, 0]
tamanho = [0, 0]

for desceu, classe in zip(lista_desceu, lista_classe):
    if classe == 1:
        contagem[0] += desceu
        tamanho[0] += 1
    elif classe == 2:
        contagem[1] += desceu
        tamanho[1] += 1

total_classes = len(lista_classe)  # Use a different variable name here

media = [(contagem[0] / tamanho[0]), (contagem[1] / tamanho[1])]

print(df)

print(tamanho[0])

print("media classe 1:", media[0])  # Corrected to print the actual media
print("media classe 2:", media[1])  # Corrected to print the actual media
