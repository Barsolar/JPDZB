import sys

args=sys.argv

if (len(args)==2):
    try:
        filename=str(args[1])

        if filename.endswith('txt'):
            filename.encode('unicode_escape')
            file = open(filename, 'r', encoding="utf8")
            list = file.read().split('\n')
            file.close()

            table = ['' for str in list]

            i = 0
            for str in list:
                temp = str.split('\t')
                temp[1]=temp[1].strip(';')
                temp[1]=int(temp[1])
                table[i] = temp
                #table[i][1]= int(temp[1])
                i += 1

            table2 = sorted(table, key=lambda table:table[1], reverse=True)

            for str in table2:
                print(str)
        else:
            print("Wrong file type. Please use a .txt file.")
            sys.exit()
    except ValueError:
        print("Wrong argument type. Please give 1 argument (filename or full file path).")
    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Error in file format. Did you use spaces instead of tabulators?")
else:
    print("Wrong number of arguments. Please give 1 argument (filename or full file path).")