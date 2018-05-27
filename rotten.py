import mmap
f = open('rotten','a+')
m = mmap.mmap(f.fileno(),0)
for i in range(len(m)):
    if(m[i] < 128):
        m[i] = m[i] + 255 - 128
    else:
        m[i] = m[i] - 128
for i in range(len(m)):
    print(hex(m[i]))
