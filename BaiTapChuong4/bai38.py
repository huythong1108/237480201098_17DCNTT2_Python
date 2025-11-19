SinhVien = []
def ThemSinhVien():
    print ('----------THÊM SINH VIÊN----------')
    msv  = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    sv = {'msv' : msv, 'ten' : ten}
    SinhVien.append(sv)

def XoaSinhVien():
    print ('----------XOÁ SINH VIÊN----------')
    msv = input("Nhập mã sinh viên cần xoá: ")
    for sv in SinhVien:
        if sv['msv'] == msv:
            SinhVien.remove(sv)
            print ("Xoá sinh viên thành công!")

def SuaSinhVien():
    print ('---------SỦA SINH VIÊN---------')
    msv = input('Nhập mã sinh viên cần sửa: ')
    for sv in SinhVien:
        if sv['msv'] == msv:
            TenMoi = input('Nhập tên mới: ')
            sv['ten'] = TenMoi

def XemDSSV():
    print ('------DANH SÁCH SINH VIÊN-------')
    if not SinhVien:
        print ('Danh sách rỗng')
    for sv in SinhVien:
        print (f'Mã sv: {sv['msv']} - Tên: {sv['ten']}')

while True:
    print ('=======QUẢN LÝ SINH VIÊN=======')
    print ('1. Thêm sinh viên')
    print ('2. Xoá sinh viên')
    print ('3. Sửa sinh viên')
    print ('4. Xem danh sách sinh viên')
    print ('0. Thoát')
    print ('===============================')

    yc = int(input("Nhập yêu cầu: "))
    if yc == 1:
        ThemSinhVien()
    elif yc == 2:
        XoaSinhVien()
    elif yc == 3:
        SuaSinhVien()
    elif yc == 4:
        XemDSSV()
    elif yc == 0:
        break
    elif yc > 4 or yc < 0 :
        print ('Vui lòng nhập đúng yêu cầu!!')