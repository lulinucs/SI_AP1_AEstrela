import jogo
import time
from queue import PriorityQueue

def distancia_manhattan(estado):
    distancia = 0
    for i in range(len(estado)):
        if estado[i] != 0:
            linha_atual, coluna_atual = i // 3, i % 3
            linha_objetivo, coluna_objetivo = (estado[i] - 1) // 3, (estado[i] - 1) % 3
            distancia += abs(linha_atual - linha_objetivo) + abs(coluna_atual - coluna_objetivo)
    return distancia

def busca_a_estrela(estado_inicial):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, 0, [estado_inicial]))  # Tupla (custo total, custo heurístico, caminho)
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
                    novo_custo_heuristico = distancia_manhattan(prox_estado)
                    custo_caminho = len(novo_caminho)
                    fila_prioridade.put((custo_caminho + novo_custo_heuristico, novo_custo_heuristico, novo_caminho))

    return None, len(visitados)

estado_inicial = jogo.gerar_estado_inicial()

print("Estado inicial desordenado:")
jogo.imprimir_estado(estado_inicial)

start_time = time.time()  
sequencia_movimentos, total_nodos = busca_a_estrela(estado_inicial)

end_time = time.time()  
exec_time = end_time - start_time  

print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    print(f"\nPasso {i+1}:")
    jogo.imprimir_estado(estado)

print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")