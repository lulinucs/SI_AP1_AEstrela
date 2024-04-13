from queue import PriorityQueue
import jogo

def calcular_custo_heuristico(estado):
    count = 0
    for i, j in zip(estado, jogo.ESTADO_OBJETIVO):
        if i != j:
            count += 1
    return count

def buscaA(estado_inicial):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, 0, [estado_inicial]))
    visitados = set()

    while not fila_prioridade.empty():
        custo_total, custo_heuristico, caminho = fila_prioridade.get()
        estado_atual = caminho[-1]

        if estado_atual == jogo.ESTADO_OBJETIVO:
            return caminho, len(visitados)

        if tuple(estado_atual) not in visitados:
            visitados.add(tuple(estado_atual))

            for prox_estado in jogo.gerar_movimentos(estado_atual):
                if prox_estado not in caminho:
                    novo_caminho = caminho + [prox_estado] 
                    novo_custo_heuristico = calcular_custo_heuristico(prox_estado)
                    custo_caminho = len(novo_caminho)
                    fila_prioridade.put((custo_total + 1 + novo_custo_heuristico, novo_custo_heuristico, novo_caminho))

    return None, len(visitados)
