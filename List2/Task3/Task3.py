from Polynomial import Polynomial

poly1 = Polynomial([5,2,2,4,8]);
poly2 = Polynomial([2,0,3]);
poly3 = Polynomial([0,7,2,0]);

print(poly1.degree())

poly1.add(poly2)
print(poly1)

poly2.subtract(poly3)
print(poly2)

x=5;
print(poly1.valueOf(x))


