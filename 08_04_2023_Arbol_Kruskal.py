import networkx as nx
import matplotlib.pyplot as plt
import random 
#Se ordenan las aristas de de ascente a descendente, y la va recorriendo para encontrar el menor posible
def minimun_kruskal_algorithm(G):
    mst = []
    mst_weight = 0
    parent = {}
    
    for node in G.nodes:
        parent[node] = node
    
    edges = list(G.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])
    
    for edge in edges:
        node1, node2, weight = edge
        parent1 = parent[node1]
        parent2 = parent[node2]
        
        if parent1 != parent2:
            mst.append((node1, node2))
            mst_weight += weight['weight']
            
            for node in G.nodes:
                if parent[node] == parent2:
                    parent[node] = parent1
                    
    return mst, mst_weight
#Se ordenan las aristas de de ascente a descendente, y la va recorriendo para encontrar el mayor posible
def maximun_kruscal_algorithm(G):
    mast = []
    mast_weight = 0
    parent = {}
    
    for node in G.nodes:
        parent[node] = node
    
    edges = list(G.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'], reverse=True)
    
    for edge in edges:
        node1, node2, weight = edge
        parent1 = parent[node1]
        parent2 = parent[node2]
        
        if parent1 != parent2:
            mast.append((node1, node2))
            mast_weight += weight['weight']
            
            for node in G.nodes:
                if parent[node] == parent2:
                    parent[node] = parent1
                    
    return mast, mast_weight

# Se crea un grafo con nx.Graph y a los vertices se le da un valor random
G = nx.Graph()
vertices = [random.randint(1,10)for _ in range(15)]
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edge('A', 'B', weight=vertices[0])
G.add_edge('A', 'C', weight=vertices[1])
G.add_edge('A', 'D', weight=vertices[2])
G.add_edge('B', 'C', weight=vertices[3])
G.add_edge('B', 'F', weight=vertices[4])
G.add_edge('B', 'H', weight=vertices[5])
G.add_edge('C', 'D', weight=vertices[6])
G.add_edge('C', 'E', weight=vertices[7])
G.add_edge('C', 'H', weight=vertices[8])
G.add_edge('D', 'E', weight=vertices[9])
G.add_edge('E', 'H', weight=vertices[10])
G.add_edge('E', 'G', weight=vertices[11])
G.add_edge('F', 'H', weight=vertices[12])
G.add_edge('F', 'G', weight=vertices[13])
G.add_edge('H', 'G', weight=vertices[14])

mst, mst_weight = minimun_kruskal_algorithm(G)
mast, mast_weight = maximun_kruscal_algorithm(G)

# Graficamos los dos arboles de expansion, el minimo y maximo, gracias networkx nos ayuda a crear esto
pos = nx.spring_layout(G)
plt.subplot(121)
nx.draw_networkx_nodes(G, pos, node_color='#03ac13')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5,edge_color='#795c34')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos,edgelist=mast, edge_color='#795c34', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title('Árbol de expansión máximo')
plt.subplot(122)
nx.draw_networkx_nodes(G, pos, node_color='#03ac13')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5,edge_color='#795c34')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=mst, edge_color='#795c34', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title('Árbol de expansión mínimo')
plt.show()

#En esta parte del codigo se impreme las conexiones entre nodos y el peso de cada uno de los arboles
print("Árbol de Mínimo Coste de Kruskal")
print("MIST:", mst)
print("Peso del MIST:", mst_weight)

print("Árbol de Máximo Coste de Kruskal")
print("MAST:", mast)
print("Peso del MAST:", mast_weight)