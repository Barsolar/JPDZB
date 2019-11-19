

filename="D:\miasta.txt"
filename=r"C:\Users\Bartek\PycharmProjects\learning\miasta.txt"
filename.encode('unicodeescape')
file=open(filename, 'r', encoding="utf8")
list=file.read().split('\n')

print(list)

table = ['' for str in list]
print(len(table), len(table[0]))

i=0
for str in list:
    temp=str.split('\t')
    print(temp)
    table[i]=temp
    i+=1

table2=sorted(table, key= lambda table:table[1], reverse=True)

print(table2)


