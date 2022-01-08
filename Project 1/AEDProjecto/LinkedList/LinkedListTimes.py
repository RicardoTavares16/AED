import csv
import time
import random
import string

from LinkedList import LinkedList

l = LinkedList()

"""
#Carrega o ficheiro .csv na abertura do programa
with open('dados.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    row = next(reader)
    for row in reader:
        l.add(row[0], row[1], row[2:])
        row = next(reader)
        l.add(row[0], row[1], row[2:])

"""
#Insere países:


with open("dados_10000.txt") as f:
    for line in f:
        cleanedLine = line.strip()
        l.add(cleanedLine," "," ")

"""
sum = 0
for x in range(0,10):
    start = time.time()
    with open("dados_10000.txt") as f:
        for line in f:
            cleanedLine = line.strip()
            no = l.getNode(cleanedLine)

    end = time.time()
    sum += (end-start)

print("final: " + str(sum/10))

"""

"""
start = time.time()
for x in range(0,10000):

    nome = "Aruba"
    no = l.getNode(nome)

end = time.time()
print(end-start)
"""

"""
sum = 0
for x in range(0,10):
    start = time.time()
    with open("dados_10000.txt") as f:
        for line in f:
            cleanedLine = line.strip()
            node = l.getNode(cleanedLine)
            if(node != None):
                tmp = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
                node.set_data(tmp)

    end = time.time()
    sum += (end - start)

print("final: " + str(sum / 10))
"""

start = time.time()
with open("dados_10000.txt") as f:
    for line in f:
        cleanedLine = line.strip()
        l.remove(cleanedLine)

end = time.time()
print(end-start)
