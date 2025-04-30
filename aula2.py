import numpy as np

dados = np.genfromtxt("pedrinhas.csv", delimiter=",", skip_header=1)

joao = 0
maior_distancia_joao = 0.0
maria = 0
maior_desceu_maria = 0.0

for linha in dados:
    if linha[2] == 1:
        joao += 1
        if linha[0] > maior_distancia_joao:
            maior_distancia_joao = linha[0]

    elif linha[2] == 2:
        maria += 1
        if linha[1] > maior_desceu_maria:
            maior_desceu_maria = linha[1]

print("joao: ", joao)
print("maria: ", maria)
print("maior_distancia_joao: ", maior_distancia_joao)
print("maior_desceu_maria: ", maior_desceu_maria)
