with open('fluff', 'rb') as f:
    s = f.read()
print(s)
for i in b'flag.txt':
    print(chr(i) + ' -> ' + hex(s.find(i)))
