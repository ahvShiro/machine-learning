import numpy as np

tabela = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tabela = np.array(tabela)

print(tabela)
print("ndim:", tabela.ndim)

print("get by index:", tabela[1, 1])

print("get last line:", tabela[-1])

print("get backwards:", tabela[::-1])

print("get column:", tabela[:, 1])

# diagonal = []
# for i in range(tabela):
#     diagonal.append(tabela[i, i])

# print("get diagonal:", diagonal)

# [0, 2]
# [1, 1]
# [2, 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = np.array(lista)

lista = lista.reshape(-1, 5)

print(lista)

