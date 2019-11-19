import math
import sys

args=sys.argv

if (len(args)==4):
    try:
        a=float(args[1])
        b=float(args[2])
        c=float(args[3])
    except:
        print("Wrong argument type. Please give 3 floating point arguments.")
        sys.exit()
    finally:
        o=(a+b+c)/2

        p=math.sqrt(o*(o-a)*(o-b)*(o-c))

        print("Triangle area =",round(p,3))
else:
    print("Wrong number of arguments. Please give 3 floating point arguments.")
    sys.exit()