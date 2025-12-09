c=input("nhap vao mot chuoi: ")
hoa= 0
thuong = 0
for ch in c:
    if ch.isupper():
        hoa +=1
    elif ch.lower():
        thuong +=1
print("số chữ hoa: ",hoa)
print("số chữ thường: ",thuong)