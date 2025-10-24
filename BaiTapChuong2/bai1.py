def sosanh(a, b):
    if a > b:
        max = a
    else:
        max = b
    for i in range (1,11):
        s = max * i
        print (f"{max} x {i} = {s}")
a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
sosanh(a,b)