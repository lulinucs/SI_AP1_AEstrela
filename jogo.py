import random

ESTADO_OBJETIVO = list(range(1, 9)) + [0]

def gerar_estado_inicial():
    while True:
        estado_inicial = list(range(9))
        random.shuffle(estado_inicial)
        if verificar_paridade(estado_inicial):
            return estado_inicial

def verificar_paridade(estado):
    inversion_count = 0
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            if estado[i] > estado[j] and estado[i] != 0 and estado[j] != 0:
                inversion_count += 1
    return inversion_count % 2 == 0

def encontrar_posicao_vazia(estado):
    return estado.index(0)

def gerar_movimentos(estado):
    posicao_vazia = encontrar_posicao_vazia(estado)
    movimentos = []

    # Cima
    if posicao_vazia > 2:
        novo_estado = estado[:]
        novo_estado[posicao_vazia], novo_estado[posicao_vazia - 3] = novo_estado[posicao_vazia - 3], novo_estado[posicao_vazia]
        movimentos.append(novo_estado)

    # Baixo
    if posicao_vazia < 6:
        novo_estado = estado[:]
        novo_estado[posicao_vazia], novo_estado[posicao_vazia + 3] = novo_estado[posicao_vazia + 3], novo_estado[posicao_vazia]
        movimentos.append(novo_estado)

    # Esquerda
    if posicao_vazia % 3 != 0:
        novo_estado = estado[:]
        novo_estado[posicao_vazia], novo_estado[posicao_vazia - 1] = novo_estado[posicao_vazia - 1], novo_estado[posicao_vazia]
        movimentos.append(novo_estado)

    # Direita
    if posicao_vazia % 3 != 2:
        novo_estado = estado[:]
        novo_estado[posicao_vazia], novo_estado[posicao_vazia + 1] = novo_estado[posicao_vazia + 1], novo_estado[posicao_vazia]
        movimentos.append(novo_estado)

    return movimentos

def calcular_custo_caminho(caminho):
    return len(caminho)

def imprimir_estado(estado):
    for i in range(0, 9, 3):
        linha = " ".join([("\033[94m" if estado[i+j] == 0 else "\033[91m" if estado[i+j] != ESTADO_OBJETIVO[i+j] else "\033[92m") + str(estado[i+j]) + "\033[0m" for j in range(3)])
        print(linha)
