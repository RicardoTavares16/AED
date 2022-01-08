from AVL import AVLTree
import csv

l = AVLTree()

with open('dados.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    row = next(reader)
    for row in reader:
        l.insert(row[0],row[1],row[2:])
        row = next(reader)
        l.insert(row[0],row[1],row[2:])

while True:
    print("1 - Pesquisar")
    print("2 - Adicionar entrada")
    print("3 - Editar")
    print("4 - Eliminar")
    print("5 - Imprimir Lista")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
       nome = input("Nome/Abreviatura: ")
       no = l.getNode(nome)
       if (no != None):
           print(no.get_name() + " " + no.get_nick() + " " + ' '.join(no.get_years()))
       else:
           print("Não encontrado")

    if opcao== "2":
        print("Nova Entrada:")
        nome = input("Nome: ")
        nick = input("Abreviatura: ")
        ano = int(input("Ano: "))
        valor = input("Valor: ")

        listatmp = ["" for i in range (57)]
        listatmp[ano-1960] = valor
        l.insert(nome,nick,listatmp)
        print("Adicionado")

    if opcao == "3":
        nome = input("Entrada a editar: ")
        node = l.getNode(nome)
        if(node != None):
            print(node.get_name() + " " + node.get_nick() + " " + ' '.join(node.get_years()))
            edit = str.lower(input("Editar nome ou abreviatura ou dados? :"))
            if edit == "nome":
                nome = input("Novo nome: ")
                node.set_key(nome)
                print("Editado")
            elif edit == "abreviatura":
                nome = input("Nova abreviatura: ")
                node.set_nick(nome)
                print("Editado")
            elif edit == "dados":
                ano = int(input("Ano? :"))
                nome = input("Valor? :")
                lista = node.get_years()
                lista[ano-1960] = nome
                node.set_years(lista)
                print("Editado")
        else:
             print("Não Encontrado")

    if opcao == "4":
        nome = input("Entrada a remover: ")
        l.delete(nome)

    if opcao == "5":
        l.printTree()

    if opcao == "0":
        break