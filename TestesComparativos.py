import time
import jogo
import AP1_CustoUniforme
import AP1_HeuristicaSimples
import AP1_HeuristicaManhattan

estado_inicial = jogo.gerar_estado_inicial()
print("Estado inicial desordenado:")
jogo.imprimir_estado(estado_inicial)

# Testando Custo Uniforme
start_time = time.time()
sequencia_movimentos, total_nodos = AP1_CustoUniforme.custo_uniforme(estado_inicial)
end_time = time.time()
exec_time = end_time - start_time

print("\nAlgoritmo: Custo Uniforme")
print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    print(f"\nPasso {i+1}:")
    jogo.imprimir_estado(estado)
print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")

# Testando Heurística Simples
start_time = time.time()
sequencia_movimentos, total_nodos = AP1_HeuristicaSimples.buscaA(estado_inicial)
end_time = time.time()
exec_time = end_time - start_time

print("\nAlgoritmo: Heurística Simples")
print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    valor_heuristico_atual = AP1_HeuristicaSimples.calcular_custo_heuristico(estado)
    print(f"\nPasso {i+1}: Valor heurístico atual: {valor_heuristico_atual}")
    jogo.imprimir_estado(estado)
print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")

# Testando Heurística de Manhattan
start_time = time.time()
sequencia_movimentos, total_nodos = AP1_HeuristicaManhattan.busca_a_estrela(estado_inicial)
end_time = time.time()
exec_time = end_time - start_time

print("\nAlgoritmo: Heurística de Manhattan")
print("\nSequência de movimentos para chegar ao estado objetivo:")
for i, estado in enumerate(sequencia_movimentos):
    valor_heuristico_atual = AP1_HeuristicaManhattan.distancia_manhattan(estado)
    print(f"\nPasso {i+1} - Valor heurístico atual: {valor_heuristico_atual}")
    jogo.imprimir_estado(estado)
print("\nTotal de nodos visitados:", total_nodos)
print("Tamanho do caminho:", len(sequencia_movimentos))
print("Tempo de execução:", exec_time, "segundos")
