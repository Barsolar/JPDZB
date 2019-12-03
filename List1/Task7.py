import sys

args=sys.argv

if (len(args)==2):
    try:
        filename=str(args[1])

        if filename.endswith('txt'):
            filename.encode('unicode_escape')
            file = open(filename, 'a', encoding="utf8")
            done = False
            while not done:
                name = input("Type a city name you want to add a record for: (Type q to quit)")
                if name == 'q':
                    file.close()
                    sys.exit()
                temp = input("Please input recorded temperature: ")
                try:
                    temp1 = int(temp)
                    save = '\n' + name + '\t' + temp + ";"
                    file.write((save))
                except ValueError:
                    print("Temperature must be a number.")
        else:
            print("Wrong file type. Please use a .txt file.")
    except ValueError:
        print("Wrong argument type. Please give 1 argument (filename or full file path).")
    except FileNotFoundError:
        print("File not found.")
else:
    print("Wrong number of arguments. Please give 1 argument (filename or full file path).")