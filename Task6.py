import sys

args=sys.argv

if (len(args)==2):
    try:
        filename=str(args[1])
    except:
        print("Wrong argument type. Please give 1 argument (filename or full file path).")
        sys.exit()
    finally:
        namecheck=filename.split('.')
        if namecheck[1]=='txt':
            filename.encode('unicode_escape')
            file = open(filename, 'r', encoding="utf8")
            list = file.read().split('\n')

            table = ['' for str in list]

            i = 0
            for str in list:
                temp = str.split('\t')
                table[i] = temp
                i += 1

            table2 = sorted(table, key=lambda table:table[1], reverse=True)

            for str in table2:
                print(str)
            file.close()
        else:
            print("Wrong file type. Please use a .txt file.")
            sys.exit()
else:
    print("Wrong number of arguments. Please give 1 argument (filename or full file path).")
    sys.exit()