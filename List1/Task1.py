import math
import sys

args=sys.argv

if (len(args)==4):
    try:
        a=float(args[1])
        b=float(args[2])
        c=float(args[3])

        table = [a, b, c]
        sorted(table)

        if table[0] < (table[1] + table[2]):

            o = (a + b + c) / 2

            p = math.sqrt(o * (o - a) * (o - b) * (o - c))

            print("Triangle area =", round(p, 3))
        else:
            print("Not a  triangle.")
            sys.exit()
    except ValueError:
        print("Wrong argument type. Please give 3 floating point arguments.")
else:
    print("Wrong number of arguments. Please give 3 floating point arguments.")