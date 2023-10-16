import heapq

def busqueda_por_costo_uniforme(grafo, nodo_inicio, nodo_objetivo):
    # Inicializamos la cola de prioridad con el nodo de inicio y un costo inicial de 0
    cola_prioridad = [(0, nodo_inicio)]
    # Diccionario para realizar un seguimiento de los costos mínimos hasta cada nodo
    costos_minimos = {nodo_inicio: 0}
    # Diccionario para realizar un seguimiento de los padres de cada nodo en el camino
    padres = {nodo_inicio: None}

    while cola_prioridad:
        # Obtenemos el nodo con el costo mínimo de la cola de prioridad
        costo, nodo_actual = heapq.heappop(cola_prioridad)

        # Si hemos alcanzado el nodo objetivo, reconstruimos el camino y lo devolvemos
        if nodo_actual == nodo_objetivo:
            camino = []
            while nodo_actual is not None:
                camino.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino

        # Exploramos los nodos hijos del nodo actual
        for hijo, costo_hijo in grafo[nodo_actual]:
            costo_total = costo + costo_hijo

            # Si encontramos un camino más corto hacia el nodo hijo
            if costo_total < costos_minimos.get(hijo, float('inf')):
                costos_minimos[hijo] = costo_total
                padres[hijo] = nodo_actual
                heapq.heappush(cola_prioridad, (costo_total, hijo))

    # Si no se encuentra un camino, devolvemos None
    return None

# Grafo de ejemplo
grafo = {
    12: [(8, 1), (17, 2)],
    8: [(11, 3), (12, 4)],
    11: [(12, 5)],
    17: [(18, 6), (20, 7)],
    18: [(20, 8)],
    20: [(21, 9)]
}

nodo_inicio = 12
nodo_objetivo = 21

resultado = busqueda_por_costo_uniforme(grafo, nodo_inicio, nodo_objetivo)
print(resultado)
