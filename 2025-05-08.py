import pandas as pd

def contagemLista(vetor: list[int]) -> dict[int, int]:
    '''
    - Itera por cada item na lista
    - Se um item ainda não é uma chave no dicionario, adiciona ele como chave no dicionario
    - Adiciona 1 nessa chave
    '''

    contagem = {}

    for i in range(len(vetor)):
        if vetor[i] not in contagem:
            contagem[vetor[i]] = 1
        else:
            contagem[vetor[i]] += 1

    return contagem


def contagem_json(filepath: str) -> dict[int, int]:
    df = pd.read_json(str(filepath))
    df_list = df.iloc[:, 0].to_list()

    contagem = {}

    for i in range(len(df_list)):
        if df_list[i] not in contagem:
            contagem[df_list[i]] = 1
        else:
            contagem[df_list[i]] += 1

    contagem = dict(sorted(contagem.items()))

    return contagem


vetor = ["mar", "maca", "banana", "mar", "aula", "aula"]
print(contagemLista(vetor))

print(contagem_json("datasets/pessoas.json"))


