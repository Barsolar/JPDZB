import sys

args=sys.argv

if (len(args)==4):
    try:
        a0=float(args[1])
        q=float(args[2])
        n=int(args[3])
        if n==0:
            print("n=0, Am I not supposed to calculate anything?")
    except:
        print("Wrong argument type. Please give 2 floating point arguments and 1 integer argument.")
        sys.exit()
    finally:
        i=0
        a=a0;
        while i<n:
            i+=1
            a=a*q;
            print("A[",i,"] = ",a,sep="")
else:
    print("Wrong number of arguments. Please give 2 floating point arguments and 1 integer argument.")
    sys.exit()