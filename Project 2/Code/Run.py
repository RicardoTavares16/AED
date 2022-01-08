from Graph import Graph
from Graph import bfs_paths
from Gerador import GeradorCidades
import time

g = Graph()
while True:
    print("1 - Gerar e Carregar Mapa")
    print("2 - Calcular caminho mais curto")
    print("3 - Imprimir Grafo")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        #nome = input("Nome do ficheiro: ")
        tarefa = input("Tarefa numero: ")
        if  tarefa == "1":
            numcidade = input("Numero de Cidades: ")
            nome = "tarefa_"+ tarefa +"_"+ numcidade +".txt"

            GeradorCidades(nome, numcidade,tarefa)
            with open(nome) as f:
                first_line = f.readline()

                start = first_line.split()[2]
                g.addVertex(start)

                for line in f:
                    linha = line.rstrip('\n').split(',')  # rstrip para ignorar o \n, split para ignorar as virgulas
                    g.addEdge(linha[0], linha[1], int(linha[2]))
                    last = linha[1]
            print("Mapa carregado")

        # Tenho de alterar algumas coisas ainda
        if tarefa == "2":
            numCidade = input("Numero de Cidades: ")
            nome = "tarefa_"+ tarefa +"_"+ numCidade +".txt"

            GeradorCidades(nome, numCidade,tarefa)
            with open(nome) as f:
                first_line = f.readline()

                start = first_line.split()[2]
                g.addVertex(start)

                for line in f:
                    linha = line.rstrip('\n').split(',')  # rstrip para ignorar o \n, split para ignorar as virgulas
                    g.addEdge2(linha[0], linha[1], int(linha[2]))
                    last = linha[1]
            print("Mapa carregado")

        if tarefa == "3":
            nome = "tarefa_" + tarefa + "_11.txt"

            GeradorCidades(nome, 11,tarefa)
            with open(nome) as f:
                first_line = f.readline()

                start = first_line.split()[2]
                g.addVertex(start)

                for line in f:
                    linha = line.rstrip('\n').split(',')  # rstrip para ignorar o \n, split para ignorar as virgulas
                    g.addEdge(linha[0], linha[1], int(linha[2]))
                    last = linha[1]
            print("Mapa carregado")

    if opcao == "2":
        init = time.time()
        lista = list(bfs_paths(g, start, last))

        n = g.getNumVertices()
        dist = 9999999999
        listtmp = {}
        for i in range(len(lista)):
            if len(lista[int(-i)]) == n:
                if dist > g.calcDist(lista[int(-i)]):
                    dist = g.calcDist(lista[int(-i)])
                    listtmp = lista[int(-i)]
                    # print("Path: " + str(lista[int(-i)]) + " -> Distance: " + str(g.calcDist(lista[int(-i)])))
        print("Caminho mais curto = " + str(listtmp) + ' -> Distância: ' + str(dist))
        end = time.time()
        print("Tempo: " + str(end-init) + " s")

    if opcao == "3":
        for i in g.getVertices():
            print(g.getVertex(i))

    if opcao == "0":
        break


