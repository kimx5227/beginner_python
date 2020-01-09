def printTable(list):
    colwidth = [0]*len(list)
    print(colwidth)
    colSpan = len(list)
    rowSpan = len(list[0])

    for col in range(len(list)):
        for index in range(len(list[col])):
            if len(list[col][index]) > colwidth[col]:
                colwidth[col] = len(list[col][index]) + 2

    for row in range(rowSpan):
        for col in range(colSpan):
            print(list[col][row].rjust(colwidth[col]), end = '')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
