import jogo
import time
from queue import PriorityQueue

def custo_uniforme(estado_inicial):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, [estado_inicial]))  # Tupla (custo, caminho)
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

estado_inicial = jogo.gerar_estado_inicial()
print("Estado inicial desordenado:")
jogo.imprimir_estado(estado_inicial)

start_time = time.time()

sequencia_movimentos, total_nodos = custo_uniforme(estado_inicial)

end_time = time.time()
exec_time = end_time - start_time

print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    print(f"\nPasso {i+1}:")
    jogo.imprimir_estado(estado)
print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")

