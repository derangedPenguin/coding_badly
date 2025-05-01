##
x = float(input('Enter x0: '))
px = float(input('Enter p(x0): '))
y = float(input('Enter x1: '))
py = float(input('Enter p(x1): '))
z = float(input('Enter x2: '))
pz = float(input('Enter p(x2): '))

d = (py-px)/(y-x)
e = (pz-px)/(z-x)

a = (e-d)/(z-y)

b = e - (a * (z+x))

c = pz - (z**2 * a) - (z * b)

print(f"a = {a}; b = {b}; c = {c}")
