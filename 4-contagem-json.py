import json


def contagem_lista(vetor: list[int]) -> dict[int, int]:

    contagem = {}

    for i in range(len(vetor)):
        if vetor[i] not in contagem:
            contagem[vetor[i]] = 0
        contagem[vetor[i]] += 1

    return contagem

def contagem_itens_totais(vetor: list[int]) -> int:
    return len(vetor)

def contagem_itens_distintos(vetor: list[int]) -> dict[int, int]:
    
    return contagem_lista(vetor)
    
def carregar_json(filepath: str):
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    except IOError:
        print("Não foi possível carregar o arquivo")
    
    return data


def main():    
    dict_dataset = carregar_json("datasets/pessoas.json")

    distintos = contagem_itens_distintos(dict_dataset['nomes-pessoas'])
    
    totais = contagem_itens_totais(dict_dataset['nomes-pessoas'])
    
    print("distintos: ", distintos)
    
    print("totais: ", totais)
    
    
    # print(contagem_json("datasets/pessoas.json"))


main()
