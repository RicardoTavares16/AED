import random

def GeradorCidades(nome, numCidades,tarefa):
    if tarefa != "2":
        n = int(numCidades)
        with open(nome, "w") as txt:
            a = 1
            txt.write("start in City" + str(a) + "\n")
            print ("start in City" + str(a) + "\n")

            m = n-1
            tmp = 2

            for i in range(n):
                for j in range(m):
                    txt.write("City" + str(a)+','+"City" + str(tmp)+','+str(random.randint(1,50))+'\n')
                    print("City" + str(a)+','+"City" + str(tmp)+','+str(random.randint(1,50))+'\n')
                    tmp += 1

                a += 1
                tmp = a+1
                m = m - 1

    else:
        n = int(numCidades)
        with open(nome, "w") as txt:
            a = 1
            txt.write("start in City" + str(a) + "\n")
            print("start in City" + str(a) + "\n")

            tmp = 1

            for i in range(n):
                for j in range(n):
                    if i != j:
                        txt.write("City" + str(a) + ',' + "City" + str(tmp) + ',' + str(random.randint(1, 50)) + '\n')
                        print("City" + str(a) + ',' + "City" + str(tmp) + ',' + str(random.randint(1, 50)) + '\n')
                    tmp += 1

                a += 1
                tmp = 1