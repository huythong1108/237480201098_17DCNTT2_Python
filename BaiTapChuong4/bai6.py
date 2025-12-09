c=input("nhập chuỗi: ")
s= 0
for ch in c:
    if ch.isdigit():
        s+=int(ch)
print("tổng các chữ số: ",s)