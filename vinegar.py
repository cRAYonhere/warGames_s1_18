import mmap
v = open('vinegar','a+')
vinegar = mmap.mmap(v.fileno(),0)
r = open('rotten','a+')
rotten = mmap.mmap(r.fileno(),0)
key = 'this is not the flag'

for i in key:
    print(i,' -> ',ord(i))
'''
for i in range(30):
    print(vinegar[i],rotten[i], vinegar[i] - rotten[i],chr( vinegar[i] - rotten[i]))
'''

for i in range(len(vinegar)):
    if vinegar[i] < ord(key[i%len(key)]):
        vinegar[i] = vinegar[i] +255 - ord(key[i%len(key)])
    else:
        vinegar[i] = vinegar[i] - ord(key[i%len(key)])
