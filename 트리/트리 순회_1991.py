N=int(input())
sequence_preorder=''
sequence_postorder=''
sequence_inorder=''
tree={}
for _ in range(N):
    node,node1,node2=input().strip().split()
    tree[node]={'leftChild' : node1, 'rightChild' : node2}

def preorder(node): # 루트 -> leftChild -> rightChild
    global sequence_preorder
    sequence_preorder+=node

    if tree[node]['leftChild'] =='.' and tree[node]['rightChild']=='.':
        return

    if tree[node]['leftChild'] !='.':
        preorder(tree[node]['leftChild'])

    if tree[node]['rightChild'] !='.':
        preorder(tree[node]['rightChild'])

def inorder(node): # leftChild -> 루트 -> rightChild
    global sequence_inorder

    if tree[node]['leftChild'] =='.' and tree[node]['rightChild']=='.':
        sequence_inorder += node
        return

    if tree[node]['leftChild'] !='.' and tree[node]['rightChild']=='.': # 왼쪽자식만 있을 때
        inorder(tree[node]['leftChild'])
        sequence_inorder += node

    elif tree[node]['rightChild'] !='.' and tree[node]['leftChild']=='.': # 오른쪽 자식만 있을 때
        sequence_inorder += node
        inorder(tree[node]['rightChild'])
    else: # 왼,오 둘다 있을 때
        inorder(tree[node]['leftChild'])
        sequence_inorder += node
        inorder(tree[node]['rightChild'])

def postorder(node): # leftChild -> rightChild -> 루트
    global sequence_postorder

    if tree[node]['leftChild'] =='.' and tree[node]['rightChild']=='.':
        sequence_postorder += node
        return

    if tree[node]['leftChild'] != '.' and tree[node]['rightChild'] == '.':  # 왼쪽자식만 있을 때
        postorder(tree[node]['leftChild'])
        sequence_postorder += node

    elif tree[node]['rightChild'] !='.' and tree[node]['leftChild']=='.': # 오른쪽 자식만 있을 때
        postorder(tree[node]['rightChild'])
        sequence_postorder += node
    else:
        postorder(tree[node]['leftChild'])
        postorder(tree[node]['rightChild'])
        sequence_postorder += node

preorder('A')
inorder('A')
postorder('A')

print(sequence_preorder)
print(sequence_inorder)
print(sequence_postorder)