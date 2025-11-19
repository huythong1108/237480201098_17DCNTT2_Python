L = list(map(int, input( 'nhap cac so:').split()))
pos = -1
for i in range(1, len(L)-1):
    if L[i] == L[i-1] * L[i+1]:
        pos = i
        break
print(pos)