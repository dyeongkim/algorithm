# 백준 2914 - 크로아티아 알파벳
croalpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in croalpha:
    word = word.replace(i,'*')
print(len(word))
