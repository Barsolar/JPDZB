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
            file = open(filename, 'a', encoding="utf8")

            done = False
            while not done:
                name=input("Type a city name you want to add a record for: (Type q to quit)")
                if name=='q':
                    file.close()
                    sys.exit()
                temp=input("Please input recorded temperature: ")
                try:
                    temp1=int(temp)
                except:
                    print("Temperature must be a number")
                    sys.exit()
                finally:
                    save='\n'+name+'\t'+str(temp1)
                    file.write((save))
        else:
            print("Wrong file type. Please use a .txt file.")
            sys.exit()
else:
    print("Wrong number of arguments. Please give 1 argument (filename or full file path).")
    sys.exit()