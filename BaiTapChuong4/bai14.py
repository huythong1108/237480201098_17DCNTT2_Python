ListA=[]
n=int(input("Nhap so luong phan tu "))
for i in range(n):
    c=int(input(f"nhap pt thu {i+1}: "))
    ListA.append(c)
print("Mang vua nhap la")
print(ListA)
t=0
for a in ListA:
    if a>0:
        t=1
        print(f"gia tri duong dau tien la {a}")
        break
if(t==0):
    print(" ko co gia tri duong nao")