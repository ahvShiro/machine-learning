import pandas as pd


def contagemLista(vetor: list[int]) -> dict[int, int]:

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

    contagem = contagemLista(df_list)

    contagem = dict(sorted(contagem.items()))

    return contagem


def main():
    vetor = [1, 1, 1, 1, 1, 
             2, 2, 2, 2, 2, 2, 2, 2, 
             3, 3, 3, 3, 3, 3, 3, 3, 3, 
             4, 4, 4, 4, 4, 4, 4, 
             "mar", "mar", 
             "1", "1", "1", 
             "banana", "banana", 
             "aula", "aula", 
             3.1415, 3.1415, 3.1415, 3.1415]
    
    print(contagemLista(vetor))

    # print(contagem_json("datasets/pessoas.json"))


main()
