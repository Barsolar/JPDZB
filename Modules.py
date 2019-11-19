def LoadFile(filename):
        filename.encode('unicode_escape')
        file = open(filename, 'r', encoding="utf8")
        list = file.read().split('\n')
        table = ['' for str in list]
        i = 0
        for str in list:
            temp = str.split('\t')
            table[i] = temp
            i += 1
        file.close()
        return table

def SortTable(table):
    sortedTable = sorted(table, key=lambda table:table[1], reverse=True)
    return sortedTable

def SaveToFile(filename,data):
    filename.encode('unicode_escape')
    file = open(filename, 'a', encoding="utf8")
    file.write((data))
    return 0