a, b, c = eval(input('Nhập vào 3 số cách nhau bởi dấu phảy'))
if (a>b):
    if(a>c):
        if(b>c):
            print (c,b,a)
        else:
            print (b,c,a)
    else:
        print (b,a,c)
else:
    if(b>c):
        if(a>c):
            print (c,a,b)
        else:
            print (a,c,b)
    else:
        print (a,b,c)