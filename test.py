import numpy as np


class Node():
    def __init__(self,data=None,lchild=None,rchild=None,l=None):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild
        self.l=l

x=None

def fun():
    global x
    x=Node()

fun()
print(x)

