#Algoritmo de Splaying baseado em https://github.com/anoopj/pysplay/blob/master/splay.py
from Node import Node

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None,None,None)  # Início

    def insert(self, key,nick,list):
        if (self.root == None): #Se estiver vazia, cria no e sai
            self.root = Node(key,nick,list)
            return

        self.splay(key)
        if self.root.key == key:
            print("[" + str(key) + "] já está na Árvore.")
            return

        no = Node(key,nick,list)
        if key < self.root.key:
            no.left = self.root.left
            no.right = self.root
            self.root.left = None
        else:
            no.right = self.root.right
            no.left = self.root
            self.root.right = None
        self.root = no

    def remove(self, key):
        #Procura elemento
        self.splay(key)
        if key != self.root.key:
            print("Não encontrado")
            return

        #Apaga
        if self.root.left == None:
            self.root = self.root.right
        else:
            tmp = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = tmp
        #print("Removido")

    def getNode(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key and self.root.nick != key:
            return None
        return self.root

    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

    def printTree(self):
        def recursivePreorder(node):
            if not node:
                return

            yield from recursivePreorder(node.left)
            yield node.key + " " + node.nick + " " + ' '.join(node.years)
            yield from recursivePreorder(node.right)

        return recursivePreorder(self.root)