ListA=[]
n=int(input("Nhap so luong phan tu "))

for i in range(n):
    c=int(input(f"nhap pt thu {i+1}: "))
    ListA.append(c)

print("Mang vua nhap la")
print(ListA)

if len(set(ListA))==1:
    print("True")
else:
    print("False")

