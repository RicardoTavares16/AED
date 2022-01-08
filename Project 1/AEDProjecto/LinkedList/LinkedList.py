#Adaptado dos slides da cadeira
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    #Adicionar novo nó à lista composto por nome do país, abreviatura e valores
    def add(self, item, nick, years):
        temp = Node(item, nick, years)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    #Percorre a lista à procura do nó por nome ou abreviatura, se encontrar, retorna o nó
    def getNode(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_name() == item or current.get_nick() == item:
                found = True
                return current
            else:
                current = current.get_next()
        return None

    #Remove o nó por nome ou abreviatura
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.get_name() == item or current.get_nick() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        return found

    #Imprime os dados de cada país
    def print_list(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        print(currentNode.get_name() + " " + currentNode.get_nick() + " " + ' '.join(currentNode.get_years()))
        while currentNode != None:
            currentNode = currentNode.get_next()
            if currentNode != None:
                print(currentNode.get_name() + " " + currentNode.get_nick() + " " + ' '.join(currentNode.get_years()))

    def del_duplicados(self):
        current = self.head
        while current != None and current.next != None:
            if current.get_data() == current.get_next().get_data():
                current.set_next(current.get_next().get_next())
            else:
                current = current.get_next()
        return self.head

