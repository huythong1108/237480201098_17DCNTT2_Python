ListA=[]
n=int(input("Nhap so luong phan tu "))

for i in range(n):
    c=int(input(f"nhap pt thu {i+1}: "))
    ListA.append(c)

print("Mang vua nhap la")
print(ListA)

x=int(input("nhap vao gia tri x: "))
vitri=1
for a in ListA:
    if a==x:
        vitri=vitri+ListA.index(a)
        break

if(vitri>(len(ListA)/2)):
    print(f"gia tri xa x nhat la {ListA[0]}")
else:
    print(f"gia tri xa x nhat la {ListA[n-1]}")