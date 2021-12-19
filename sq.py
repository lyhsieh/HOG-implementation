from math import sqrt
for i in range(1, 18):
    a = 2 ** i
    app = 1 + (a-1)/2 + ((a-1)^2)/8 + (3*(a-1)^3)/48 + (15*(a-1)^4)/(16*24)
    print(f"val = {a}, sqrt = {sqrt(a)}, app = {app}, diff = {abs(app - sqrt(a))}")