def gt(n, a, arr):
    arr.sort(reverse=True)
    print ('Giá trị lớn thứ',a,':',arr[a-1])

arr = []
a = int(input('Nhập số nguyên dương a: '))
n = int(input('Nhập số phần tử: '))
for i in range(n):
    phantu = int(input(f"Nhập pt thứ {i+1}: "))
    arr.append(phantu)
gt(n, a, arr)