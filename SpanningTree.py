#James Leon 00213782
#Nicolas Romero 00212949

import networkx as nx
import matplotlib.pyplot as plt

#Clase Nodo y Grafo
class Nodo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = {}

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)
        self.aristas[nodo.nombre] = []

    def agregar_arista(self, nodo1, nodo2):
        self.aristas[nodo1.nombre].append(nodo2.nombre)
        self.aristas[nodo2.nombre].append(nodo1.nombre)

def dibujar_spanning_tree(grafo):
    nx_grafo = nx.Graph()
    for nodo in grafo.nodos:
        if nodo.tipo == "switch":
            nx_grafo.add_node(nodo.nombre)
    for nodo in grafo.nodos:
        if nodo.tipo == "switch":
            for vecino in grafo.aristas[nodo.nombre]:
                if vecino in nx_grafo.nodes():
                    nx_grafo.add_edge(nodo.nombre, vecino)
    nx_tree = nx.algorithms.minimum_spanning_tree(nx_grafo)
    nx.draw(nx_tree, with_labels=True)
    plt.show()

def dibujar_grafo(grafo):
    nx_grafo = nx.Graph()
    for nodo in grafo.nodos:
        nx_grafo.add_node(nodo.nombre)
    for nodo in grafo.nodos:
        for vecino in grafo.aristas[nodo.nombre]:
            nx_grafo.add_edge(nodo.nombre, vecino)
    nx.draw(nx_grafo, with_labels=True)
    plt.show()

# Crear nodos y aristas
nodo1 = Nodo("S1", "switch")
nodo2 = Nodo("S2", "switch")
nodo3 = Nodo("S3", "switch")
nodo4 = Nodo("S4", "switch")
nodo5 = Nodo("S5", "switch")
nodo6 = Nodo("S6", "switch")
nodo7 = Nodo("S7", "switch")

nodo8 = Nodo("hostA", "ethernet")
nodo9 = Nodo("hostB", "ethernet")
nodo10 = Nodo("hostC", "ethernet")

grafo = Grafo()
grafo.agregar_nodo(nodo1)
grafo.agregar_nodo(nodo2)
grafo.agregar_nodo(nodo3)
grafo.agregar_nodo(nodo4)
grafo.agregar_nodo(nodo5)
grafo.agregar_nodo(nodo6)
grafo.agregar_nodo(nodo7)
grafo.agregar_nodo(nodo8)
grafo.agregar_nodo(nodo9)
grafo.agregar_nodo(nodo10)

grafo.agregar_arista(nodo1, nodo6)
grafo.agregar_arista(nodo1, nodo4)
grafo.agregar_arista(nodo1, nodo2)
grafo.agregar_arista(nodo1, nodo7)
grafo.agregar_arista(nodo1, nodo5)
#NODO S2
grafo.agregar_arista(nodo2, nodo3)
#NODO S3
grafo.agregar_arista(nodo3, nodo5)
#NODO S4
grafo.agregar_arista(nodo4, nodo6)
#NODO S5
grafo.agregar_arista(nodo5, nodo7)
#NODOS ETHRNET
grafo.agregar_arista(nodo3, nodo8)
grafo.agregar_arista(nodo7, nodo9)
grafo.agregar_arista(nodo4, nodo10)

dibujar_grafo(grafo)
dibujar_spanning_tree(grafo)