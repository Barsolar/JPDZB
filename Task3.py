import sys

args=sys.argv

def MultiplicationTable(n):
    table = [[0 for i in range(n)] for j in range(n)]
    i = 0
    j = 0
    while i < n:
        i += 1
        while j < n:
            j += 1
            table[i - 1][j - 1] = i * j
        j = 0
    return table

if (len(args)==2):
    try:
        n=int(args[1])
    except:
        print("Wrong argument type. Please give one integer argument.")
        sys.exit()
    finally:
        if n==0:
            print("n=0, Am I not supposed to calculate anything?")
        table = MultiplicationTable(n)
        i = 0
        j = 0
        while i < n:
            i += 1
            while j < n:
                j += 1
                print(table[i - 1][j - 1], end='\t')
            print("\n")
            j = 0
else:
    print("Wrong number of arguments. Please give one integer argument.")
    sys.exit()

