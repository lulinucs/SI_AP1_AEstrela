import jogo
from queue import PriorityQueue
import time

def calcular_custo_heuristico(estado):
    count = 0
    for i, j in zip(estado, jogo.ESTADO_OBJETIVO):
        if i != j:
            count += 1
    return count

def buscaA(estado_inicial):
    # Inicializa a fila de prioridade
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, 0, [estado_inicial]))  # Insere o estado inicial com custo 0
    visitados = set()  # Conjunto de estados visitados

    while not fila_prioridade.empty():
        custo_total, custo_heuristico, caminho = fila_prioridade.get()
        estado_atual = caminho[-1]  # Estado atual é o último estado no caminho

        if estado_atual == jogo.ESTADO_OBJETIVO:
            return caminho, len(visitados)  # Se encontrou o estado objetivo, retorna o caminho e o número de nodos visitados

        if tuple(estado_atual) not in visitados:
            visitados.add(tuple(estado_atual))  # Adiciona o estado atual aos visitados

            # Para cada próximo estado gerado a partir do estado atual
            for prox_estado in jogo.gerar_movimentos(estado_atual):
                if prox_estado not in caminho:
                    novo_caminho = caminho + [prox_estado]  # Adiciona o próximo estado ao caminho
                    novo_custo_heuristico = calcular_custo_heuristico(prox_estado)  # Calcula o custo heurístico do próximo estado
                    custo_caminho = len(novo_caminho)  # Calcula o custo do caminho até o momento
                    # Adiciona o próximo estado à fila de prioridade com o custo total estimado
                    fila_prioridade.put((custo_total + 1 + novo_custo_heuristico, novo_custo_heuristico, novo_caminho))

    return None, len(visitados)  # Se não encontrou solução, retorna None e o número de nodos visitados

# Gera o estado inicial
estado_inicial = jogo.gerar_estado_inicial()

# Imprime o estado inicial
print("Estado inicial desordenado:")
jogo.imprimir_estado(estado_inicial)

start_time = time.time()  # Inicia a contagem de tempo

# Executa o algoritmo A*
sequencia_movimentos, total_nodos = buscaA(estado_inicial)

end_time = time.time()  # Finaliza a contagem de tempo
exec_time = end_time - start_time  # Calcula o tempo de execução

# Imprime a sequência de movimentos para alcançar o estado objetivo
print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    print(f"\nPasso {i+1}:")
    jogo.imprimir_estado(estado)

# Imprime o total de nodos visitados, o tamanho do caminho e o tempo de execução
print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")
