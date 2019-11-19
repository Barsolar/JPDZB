import sys

args=sys.argv

if (len(args)==2):
    try:
        word=str(args[1]).lower()
    except:
        print("Wrong argument type. Please give 1 string argument.")
        sys.exit()
    finally:
        n=0
        vowels="aeiouyąę"
        for char in word:
            if char in vowels:
                n+=1
        print("There are", n, "vowels in this word.")
else:
    print("Wrong number of arguments. Please give 1 string argument.")
    sys.exit()