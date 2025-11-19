def KeyLonNhat(a):
    return max(a, key=a.get)
dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(KeyLonNhat(dict))