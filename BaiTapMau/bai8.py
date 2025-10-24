a,b,c = eval(input('nhap vao 3 so cach nhau boi dau phay:  '))
if (a+b>c) and (b+c>a) and (c+a>b):
    if a*a+b*b == c*c or a*a+c*c==b*b or c*c + b*b ==a*a:
        print('đây là tam giác vuông')
    elif a==b==c:
        print('đây là tam giác đều')
    elif a==b or a==c or c==b:
        print('đây là tam giác cân')
    else :
        print ('Đây là tam giác thường')
else:
    print ('Đây không phải ba cạnh của tam giác')
         