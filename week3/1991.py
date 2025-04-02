import sys

N = int(sys.stdin.readline())
tree = {}

def preorder(v):
    if v == ".":
        return
    print(v, end="")
    preorder(tree[v][0])
    preorder(tree[v][1])
    
def inorder(v):
    if v == ".":
        return
    inorder(tree[v][0])
    print(v, end="")
    inorder(tree[v][1])

def postorder(v):
    if v == ".":
        return
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v, end="")


for i in range(N):
    node, left, right = map(str, sys.stdin.readline().split())
    tree[node] = [left, right]

# print(tree['A'][0])

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
