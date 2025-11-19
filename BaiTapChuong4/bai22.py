L = list(map(int, input( 'nhap cac so:').split()))
so_chan = False
so_le = False
for x in L:
    if x % 2 == 0:
        so_chan = True
    else:
        so_le = True
if so_chan and so_le:
    print('list chan le')
else:
    print('khong phai list chan le')