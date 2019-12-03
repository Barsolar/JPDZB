class Polynomial:

    def __init__(self, coefficientList):
        if all(isinstance(x, (int,float)) for x in coefficientList):
            for i in range(0, len(coefficientList)):
                if coefficientList[-1]==0:
                    del coefficientList[-1]
            self._coefs=list(reversed(coefficientList))
        else:
            self._coefs=[];
            print("Something wrong with your list (need a list of integers).")

    def get_coefs(self):
        return self._coefs

    def set_coefs(self, coefficientList):
        self._coefs=coefficientList

    def degree(self):
        return (len(self._coefs)-1)

    def subtract(self, poly):
        if isinstance(poly, Polynomial):
            if self.degree() >= poly.degree():
                bigpoly=self
                smallpoly=poly
            else:
                bigpoly=poly
                smallpoly=self

            addedcoefs=[];

            for i in range(0, len(bigpoly.get_coefs())):
                if (i < len(smallpoly.get_coefs())):
                    addedcoefs.append(bigpoly.get_coefs()[i] - smallpoly.get_coefs()[i]);
                else:
                    addedcoefs.append(bigpoly.get_coefs()[i])
            self.set_coefs(addedcoefs)
        else:
            print("Please give an argument of class Polynomial")

    def add(self, poly):
        if isinstance(poly, Polynomial):
            if self.degree() >= poly.degree():
                bigpoly = self
                smallpoly = poly
            else:
                bigpoly = poly
                smallpoly = self

            addedcoefs = [];

            for i in range(0, len(bigpoly.get_coefs())):
                if (i < len(smallpoly.get_coefs())):
                    addedcoefs.append(bigpoly.get_coefs()[i] + smallpoly.get_coefs()[i]);
                else:
                    addedcoefs.append(bigpoly.get_coefs()[i])
            self.set_coefs(addedcoefs)
        else:
            print("Please give an argument of class Polynomial")

    def valueOf(self, x):
        if isinstance(x, (int, float)):
            value=0
            for i in range(0, len(self.get_coefs())):
                value=value+(self.get_coefs()[i]*(x**i))
            return value
        else:
            print("Error! X must be a numeric value.")
            return 0

    def __str__(self):
        a=list(reversed(self.get_coefs()))
        myPoly=''
        deg=self.degree()
        for i in range(0,len(a)):
            myPoly=myPoly+str(a[i])+"*x^"+str(deg)+"+"
            deg=deg-1
        myPoly=myPoly[:-5]
        return myPoly