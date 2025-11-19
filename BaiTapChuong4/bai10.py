a=input("nhập chuỗi a: ")
b=input("nhập chuỗi b: ")
s= ""
index = a.find(b)
if index != -1:
    s= a[:index] + a[index + len(b) : ]
else:
    s=a
print("chuoi sau khi xoa la: ",s.strip())