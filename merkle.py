import itertools
import hashlib
passPhrases = []
for string in itertools.imap(''.join, itertools.product('merkl', repeat=10)):
    passPhrases.append(string)
with open("salt_hash") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
for i in range(len(content)):
    content[i] = content[i].split()
    content[i] = [content[i][1][5:],content[i][2][5:]]
plausible_answers = []
f = open('workfile_2.txt', 'w')
for i in passPhrases:
    for j in content:
        hash_string = 'COMP3441{'+i+':'+j[0]+'}'
        hash_object = hashlib.sha1(hash_string)
        hex_dig = hash_object.hexdigest()
        if hex_dig == j[1]:
            f.write(hash_string)
            f.write("\n")
            temp = hashlib.sha256(hash_string)
            temp = temp.hexdigest()
            if temp == '0449f93d9bb16b9657d7c6350ec77d7f577d276743b714af0272c503a2eb01cc':
                print(i,j[0])
f.close()
COMP3441{kmrleekelm:RoHWTfrusLxboxm5AOlb}
