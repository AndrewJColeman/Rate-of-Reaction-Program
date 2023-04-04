import math

def printTable(coins):
    for i in range(len(coins)):
     print()
     for j in range(len(coins[i])):
         print(coins[i][j],end="  ")

         
def tableBuilder():
    
    x = int(input("How many reactants are there?> "))
    y = int(input("How many experiments are there?> "))
    table = []
    for j in range(y):
        table.append([])
        for i in range(x):
            if i == 0:
                react = str("A")
            elif i == 1:
                react = str("B")
            elif i == 2:
                react = str("C")
            elif i == 3:
                react = str("D")
            elif i >= 4:
                print("ERROR, too many reactants")
                end()
            else:
                print("ERROR, ERROR, ERROR")
                end()

            q = float(input("Input value for experiment number " + str(j+1) + " for reactant " + str(react)+ "> "))
            table[j].append(q)
    for i in range(y):
        q = float(input("What is the Reaction Rate for experiment number " + str(i+1) + "> "))
        table[i].append(q)
    constantBuilder(table)



def constantBuilder(table):
    
    rows = 5
    constants = [[]]
    for i in range(rows):
        constants.append([])
    for i in range(len(table[0])-1):
        constants[0].append(i)
    for i in range(len(constants)-1):
        y= i+1
        for j in range(len(constants[0])):
            constants[y].append([])
    constantFinder(table, constants)


def constantFinder(table, constants):
    
    for i in range(len(table[0])-1):
        for j in range(len(table)):
            for k in range(len(table)-(j+1)):
                q = k+(j+1)
                if table[q][i] == table[j][i]:
                    for L in range(len(constants)-1):
                        y = L+1
                        try:
                            if table[constants[y][i][0]][i] == table[j][i]:
                                count = 0
                                for b in range(len(constants[y][i])):
                                    if j != constants[y][i][b]:
                                        count +=1
                                        continue
                                    else:
                                        break
                                if count == len(constants[y][i]):
                                    constants[y][i].append(j)
                                    
                            if table[constants[y][i][0]][i] == table[q][i]:
                                count = 0
                                for b in range(len(constants[y][i])):
                                    if q != constants[y][i][b]:
                                        count +=1
                                        continue
                                    else:
                                        break
                                if count == len(constants[y][i]):
                                    constants[y][i].append(q)

                        except:
                            if y != 1:
                                if table[constants[y-1][i][0]][i] == table[j][i]:
                                    break
                                else:
                                    constants[y][i].append(q)
                                    constants[y][i].append(j)
                            else:
                                constants[y][i].append(q)
                                constants[y][i].append(j)
    print(constants)
    tableBuilder2(table, constants)

def tableBuilder2(table, constants):
    
    table2 = []
    for i in range(len(constants[0])):
        table2.append([])
    constantFinder2(table, constants, table2)


    
def constantFinder2(table, constants, table2):
    
    for i in range(len(constants[0])):
        for j in range(len(table)):
            for k in range(len(table)-(j+1)):
                q=k+(j+1)
                if table[j][i] != table[q][i]:
                    for L in range(len(constants[0])):
                        if constants[0][L] != constants[0][i]:
                            for z in range(len(constants)-1):
                                y = z+1
                                try:
                                    count = 0
                                    for b in range(len(constants[y][L])):
                                        if constants[y][L][b] == j:
                                            count +=1
                                        if constants[y][L][b] == q:
                                            count +=1
                                        if count == 2 and len(table2[i]) <2:
                                            table2[i].append(j)
                                            table2[i].append(q)
                                            break
                                except:
                                    break
    orders(table, table2)



def orders(table, table2):
    
    order = []
    for i in range(len(table2)):
        order.append(round(math.log(table[table2[i][1]][len(table2)]/table[table2[i][0]][len(table2)],table[table2[i][1]][i]/table[table2[i][0]][i])))
    kValue(table, order)



def kValue(table, order):

    listy = []
    for i in range(len(order)):
        listy.append(table[0][i]**order[i])
    k = listy[0]
    for i in range(len(listy)-1):
        k = k*listy[i+1]
    k = table[0][len(listy)]/k
    finish(table, order, k)



def finish(table, order, k):

    print("Your data table is:")
    printTable(table)
    print()
    print()
    for i in range(len(order)):
        if i == 0:
            react = str("A")
        elif i == 1:
            react = str("B")
        elif i == 2:
            react = str("C")
        elif i == 3:
            react = str("D")
        print("The order of reactant " + str(react) + " is " + str(order[i]))
    print("The k value for the reaction is " + str(k))
    
                            
                            
table = [ [5,2, .013], [10,2,.05], [10,4,.1],[10,4,.1]]
#table = [ [5,2, .013], [10,2,.05], [10,4,.1]]
#table = [ [1.67, 16.7, 6.67, 0.0000974], [3.33, 16.7, 6.67, 0.000228], [5.0, 16.7, 6.67, 0.000656], [1.67, 16.7, 15.3, 0.000284], [1.67, 16.7, 20.0, 0.000433], [1.67, 33.3, 6.67, 0.000412], [1.67, 50.0, 6.67, 0.00108], ]
constantBuilder(table)
#tableBuilder()
