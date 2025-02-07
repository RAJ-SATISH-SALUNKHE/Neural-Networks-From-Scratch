class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
    def inorder(self, root):
        myStack = []
        current  = root

        while myStack != [] or current is not None:
            while current is not None:
                myStack.append(current)
                current = current.left

            # now current is none

            current = myStack.pop()
            print(current.data, end = ' ')
            current = current.right

    def preorder(self, root):
        myStack = []
        current = root

        while myStack != [] or current is not None:
            while current is not None:
                print(current.data, end = ' ')
                myStack.append(current)
                current = current.left    

            current = myStack.pop()
            current = current.right        
        
    def levelorder(self, root):
        current = root
        myqueue = [root]

        while myqueue != []:
            if current is not None:
                current = myqueue.pop(0)
                print(current.data, end = ' ')
                if current.left is not None:
                    myqueue.append(current.left)
                if current.right is not None:
                    myqueue.append(current.right)    

    def postorder(self, root):
        current = root
        stack1 = [current]
        stack2 = []

        while stack1 != []:
            current = stack1.pop()
            stack2.append(current)
            if current.left is not None:
                stack1.append(current.left)
            if current.right is not None:
                stack1.append(current.right)
            
        for element in reversed(stack2):
            print(element.data, end= ' ')

      



root = Node(1) 
root_left = Node(12) 
root_left_left = Node(3) 
root_left_right = Node(-1) 
root_right = Node(15) 
root_right_left = Node(10) 
root_right_left_left = Node(8) 
root_right_left_right = Node(11) 
root_right_right = Node(20) 
root_left_right_left = Node(5)
root_left_right_right = Node(7)

root.left = root_left
root.right = root_right
root_left.right = root_left_right
root_left.left = root_left_left
root_right.left = root_right_left
root_right.right = root_right_right
root_left_left.left = None
root_left_left.right = None
root_left_right.left = root_left_right_left
root_left_right.right = root_left_right_right
root_right_left.left = root_right_left_left
root_right_left.right = root_right_left_right
root_right_left_left.left = None
root_right_left_left.right = None
root_right_left_right.left = None
root_right_left_right.right = None
root_right_right.left = None
root_right_right.right = None
root_left_right_left.left = None
root_left_right_left.right = None
root_left_right_right.left = None
root_left_right_right.right = None



print("===================================== TREE TRAVERSALS =====================================")
print(" 1. PREORDER")
print(" 2. INORDER")
print(" 3. POSTORDER")
print(" 4. LEVEL-ORDER")

print("Enter : " , end = ' ')
inp = int(input())
if inp == 1:
    print("Preorder Traversal: " , end = ' ')
    root.preorder(root)
elif inp == 2:
    print("Inorder Traversal: " , end = ' ')
    root.inorder(root)
elif inp == 3:
    print("Postorder Traversal: " , end = ' ')
    root.postorder(root)
elif inp == 4:
    print("LevelOrder Traversal: " , end = ' ')
    root.levelorder(root)
else:
    print("Preorder Traversal: " , end = ' ')
    root.preorder(root)
    print(' ')
    print("Inorder Traversal: " , end = ' ')
    root.inorder(root)
    print(' ')
    print("Postorder Traversal: " , end = ' ')
    root.postorder(root)
    print(' ')
    print("LevelOrder Traversal: " , end = ' ')
    root.levelorder(root)



