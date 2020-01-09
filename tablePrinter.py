#! Python 3
#prints 2-D array with perfect entries as table

def printTable(list):
    colwidth = [0]*len(list)
    index = (len(list),len(list[0]))    #column and row position

    for col in range(len(list)):    #finds maximum colunn width for column
        for index in range(len(list[col])):
            if len(list[col][index]) > colwidth[col]:
                colwidth[col] = len(list[col][index]) + 2

    for row in range(index[0]): #prints each row for each column
        for col in range(index[1]):
            print(list[col][row].rjust(colwidth[col]), end = '')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
