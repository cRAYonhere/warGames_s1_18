#!/usr/bin/python
passPhraseses = []
def cmpr(a,b):
    for i in passPhraseses:
        if a in i and b in i:
            if i.index(a) > i.index(b):
                return 1
            else:
                return 0
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if cmpr(data,self.data) == 0:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data,end=''),
        if self.right:
            self.right.PrintTree()
mega_string = ''
fragments = set()
with open("password.txt",'r') as f:
    for line in f:
        for word in line.split():
           fragments.add(word)
           mega_string += word
mega_string_set = set()
for i in mega_string:
    mega_string_set.add(i)
passPhraseses = []
for i in fragments:
    passPhraseses.append(i)
uniq_chars = len(mega_string_set)
root = Node(mega_string_set.pop())
uniq_chars -= 1
for _ in range(uniq_chars):
    root.insert(mega_string_set.pop())

root.PrintTree()
