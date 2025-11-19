L = list(map(int, input( 'nhap cac so:').split()))
so_chan = []
so_khong = []
so_le = []
for x in L:
    if x == 0:
        so_khong.append(x)
    elif x % 2 == 0:
        so_chan.append(x)
    else:
        so_le.append(x)
L = so_chan + so_khong + so_le
print(L)