mk = input("Nhập mật khẩu: ")
hoa = False
thuong = False
so = False
dacbiet = False
dacbiet = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
for ch in mk:
    if ch.isupper():
        hoa = True
    elif ch.islower():
        thuong = True
    elif ch.isdigit():
        so = True
    elif ch in dacbiet:
        dacbiet = True
if len(mk) > 6 and hoa and thuong and so and dacbiet:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")