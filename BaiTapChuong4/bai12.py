ListA=[]
n=int(input("Nhap so luong phan tu "))
for i in range(n):
    c=int(input(f"nhap pt thu {i+1}: "))
    ListA.append(c)
print("Mang vua nhap la")
print(ListA)
a=int(input("nhap so nguyen a: "))
b=int(input("nhap so nguyen b: "))
in_range=[x for x in ListA if a<= x <=b]
if in_range:
    print("so nhp nhat trong khoang",min(in_range))
else:
    print("ko co so trong khoang")