import sys
import Modules

args=sys.argv

if (len(args)==3):
    try:
        filename=str(args[1])
        mode=int(args[2])
    except:
        print("Wrong argument type. Please give 2 arguments: \n First argument should be a string (filename or full file path). \n Second argument selects a mode (1 for read, 2 for write).")
        sys.exit()
    finally:
        namecheck=filename.split('.')
        if namecheck[1]=='txt':
            if mode==1:
                table=Modules.LoadFile(filename)
                sortedTable=Modules.SortTable(table)
                for str in sortedTable:
                    print(str)
            else:
                    if mode==2:
                        done = False
                        while not done:
                            name = input("Type a city name you want to add a record for: (Type q to quit)")
                            if name == 'q':
                                sys.exit()
                            temp = input("Please input recorded temperature: ")
                            try:
                                temp1 = int(temp)
                            except:
                                print("Temperature must be a number")
                                sys.exit()
                            finally:
                                save = '\n' + name + '\t' + str(temp1)
                                Modules.SaveToFile(filename,save)
                        else:
                            print("Only 1 (read) are 2 (write) are valid modes. Stop trolling.")
                            sys.exit()
        else:
            print("Wrong file type. Please use a .txt file.")
            sys.exit()
else:
    print("Wrong number of arguments. Please give 1 argument (filename or full file path).")
    sys.exit()
