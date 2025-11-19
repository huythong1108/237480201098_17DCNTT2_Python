sinhvien = []
n = int(input('Nhập số lượng sinh viên: '))
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    sinhvien.append(ten)
TimKiem = input('Nhập tên muốn tìm kiếm: ')
x = 0
for ten in sinhvien:
    if ten.lower() == TimKiem.lower():
        x = 1
        break
if x == 0:
    print (f"Không tìm thấy sinh viên {TimKiem}!")
else:
    print (f"Đã tìm thấy sinh viên {TimKiem}")
