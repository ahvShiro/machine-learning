import pandas as pd

df = pd.read_csv('pedrinhas.csv')

lista_desceu = list(df['desceu'])
lista_distancia = list(df['distancia'])
lista_classe = list(df['classificacao'])

joao = 0
maior_distancia_joao = 0.0
maria = 0
maior_desceu_maria = 0.0

for desceu, distancia, classe in zip(lista_desceu, lista_distancia, lista_classe):
    if classe == 1:
        joao += 1
        if distancia > maior_distancia_joao:
            maior_distancia_joao = distancia
    elif classe == 2:
        maria += 1
        if desceu > maior_desceu_maria:
            maior_desceu_maria = desceu

print("joao: ", joao)
print("maria: ", maria)
print("maior_distancia_joao: ", maior_distancia_joao)
print("maior_desceu_maria: ", maior_desceu_maria)

