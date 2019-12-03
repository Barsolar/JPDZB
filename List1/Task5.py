import numpy
import sys

args=sys.argv

if (len(args)==5):
    try:
        a1=float(args[1])
        b1=float(args[2])
        a2=float(args[3])
        b2=float(args[4])

        if a1 == a2:
            print("Lines are parallel.")
        else:
            if a1*a2 == -1:
                print("Lines are perpendicular.")
            else:
                rad=numpy.arctan((a2-a1)/(1+a1*a2))
                deg=numpy.degrees(rad)
                print("The angle between lines is equal to:", round(rad,2), "radians or", round(deg,2), "degrees.")
    except ValueError:
        print("Wrong argument type. Please give 4 floating point arguments. Order: a1, b1, a2, b2")
else:
    print("Wrong number of arguments. Please give 4 floating point arguments. Order: a1, b1, a2, b2")