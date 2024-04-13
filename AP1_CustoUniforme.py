from queue import PriorityQueue
import jogo

def custo_uniforme(estado_inicial):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, [estado_inicial]))  
    visitados = set()

    while not fila_prioridade.empty():
        custo, caminho = fila_prioridade.get()
        estado_atual = caminho[-1]

        if estado_atual == jogo.ESTADO_OBJETIVO:
            return caminho, len(visitados)

        if tuple(estado_atual) not in visitados:
            visitados.add(tuple(estado_atual))

            for prox_estado in jogo.gerar_movimentos(estado_atual):
                if prox_estado not in caminho:
                    novo_caminho = caminho + [prox_estado]
                    custo_caminho = jogo.calcular_custo_caminho(novo_caminho)
                    fila_prioridade.put((custo_caminho, novo_caminho))

    return None, len(visitados)