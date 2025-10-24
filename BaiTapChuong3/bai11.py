def ucln(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def bcnn(a, b):
    return int((a * b) / ucln(a, b))

def sntcn(a, b):
    if ucln(a,b) == 1:
        print (f'{a},{b} là nguyên tố cùng nhau')

a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
print (f'USCLN({a},{b}) = {ucln(a, b)}')
sntcn(a, b)
print (f'BSCNN({a},{b}) = {bcnn(a, b)}')
