import time
import jogo
import AP1_CustoUniforme
import AP1_HeuristicaSimples
import AP1_HeuristicaManhattan

def executar_algoritmo(algoritmo, estado_inicial):
    start_time = time.time()
    sequencia_movimentos, total_nodos = algoritmo(estado_inicial)
    end_time = time.time()
    exec_time = end_time - start_time
    
    print(f"\nAlgoritmo: {algoritmo.__name__}")
    print("\nSequência de movimentos para chegar ao estado objetivo:")
    for i, estado in enumerate(sequencia_movimentos):
        print(f"\nPasso {i+1}:")
        jogo.imprimir_estado(estado)
        
        # Se for a heurística simples, imprime também o valor heurístico
        if algoritmo == AP1_HeuristicaSimples.buscaA:
            valor_heuristico_atual = AP1_HeuristicaSimples.calcular_custo_heuristico(estado)
            print(f"Valor heurístico atual: {valor_heuristico_atual}")
        # Se for a heurística de Manhattan, imprime também a distância de Manhattan
        elif algoritmo == AP1_HeuristicaManhattan.busca_a_estrela:
            valor_heuristico_atual = AP1_HeuristicaManhattan.distancia_manhattan(estado)
            print(f"Valor heurístico atual: {valor_heuristico_atual}")
    
    print("\nTotal de nodos visitados:", total_nodos)
    print("Tamanho do caminho:", len(sequencia_movimentos))
    print("Tempo de execução:", exec_time, "segundos")
    
    return len(sequencia_movimentos), total_nodos, exec_time

estado_inicial = jogo.gerar_estado_inicial()

# Imprimir estado inicial
print("Estado inicial desordenado:")
jogo.imprimir_estado(estado_inicial)

# Testar algoritmos
resultados_custo_uniforme = executar_algoritmo(AP1_CustoUniforme.custo_uniforme, estado_inicial)
resultados_heuristica_simples = executar_algoritmo(AP1_HeuristicaSimples.buscaA, estado_inicial)
resultados_heuristica_manhattan = executar_algoritmo(AP1_HeuristicaManhattan.busca_a_estrela, estado_inicial)

# Imprimir tabela de resultados
print("\nTabela de Resultados:")
print("-" * 65)
print("| Algoritmo               | Tamanho do Caminho | Total de Nodos Visitados | Tempo de Execução |")
print("-" * 65)
print(f"| Custo Uniforme          | {resultados_custo_uniforme[0]:<18} | {resultados_custo_uniforme[1]:<24} | {resultados_custo_uniforme[2]:<18.6f} |")
print(f"| Heurística Simples      | {resultados_heuristica_simples[0]:<18} | {resultados_heuristica_simples[1]:<24} | {resultados_heuristica_simples[2]:<18.6f} |")
print(f"| Heurística de Manhattan | {resultados_heuristica_manhattan[0]:<18} | {resultados_heuristica_manhattan[1]:<24} | {resultados_heuristica_manhattan[2]:<18.6f} |")
print("-" * 65)
