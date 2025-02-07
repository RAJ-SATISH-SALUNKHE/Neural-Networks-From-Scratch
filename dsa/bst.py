class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, root): # Just to verify if the BST property is not hampered after performing some operations (because we know inorder traversal of BST is in sorted order)
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


    def deleteNode(self, root, val): # val is the value of the node to be deleted
        if root is None:
            return root
        
        if val < root.data:
            root.left = self.deleteNode(root.left, val)
        elif val > root.data:
            root.right = self.deleteNode(root.right, val)
        else:
            if root.left is None:

                """
                    Explaination for this condition
                       7
                        \
                         8
                          \ 
                           9
                    Suppose the value to be deleted is 8
                    Here, 8's left child is None , right child is 9, so according to this condition, we will return  9.
                    Where 9 will be returned ?
                    => 9 will be returned to 7, because we are calling deleteNode() for 7 in the previous function call (at line 22 for reference)

                    Similarly, suppose we want to delete 9 (assuming 9 is a leaf Node , a leaf node has no  children), None will be returned to 8

                """


                return root.right

            elif root.right is None:

                """
                    Explaination for this condition is similar to that of the above condition
                """
                return root.left
            
            # Now if none of the above conditions are satisfied, it would mean that the node which we want to delete has 2 children
            # In this case, we will find the node with the minimum value in the right subtree
            """
                Explaination for this condition

                Assume that we want to delete 10 from this BST
                                    10
                                    /\
                                  5   15
                                  /\   /\
                                3   7 12 20
                               /           \
                              1             30

                As discussed we will get the minimum value of the right subtree (U can also take the max value of the left subtree if u want)
                The minimum value of the right subtree is 12
                Now we will replace the value of the node to be deleted (10) with the minimum value of the right subtree (12)
            """
            current  = root.right  # here root is 10 for this example
            while current.left is not None:
                current = current.left
                
            root.data = current.data
            # As a result of the above while loop and above statement, the value of 12 wil be copied in 10
            """
                Now, since we have copied 12 in the place of 10, we can now delete 12 (leaf node wala 12) safely
                our current control is still at root, we know this 12 which we want to delete lies in the right subtree of the root
                So we will call deleteNode() for the right child of the root to delete the node having value = 12 (root.val = 12)
            """
            root.right = self.deleteNode(root.right, root.data)  # root.val is 12 in this case
            # from here onwards you can try to dry run this step, the tree size is small, so that can be done with ease

        return root # finally we return root
    

    def insert(self,root, val): # Try to dry run this code
        if root is None:
            return Node(val) # We insert always at the leaf node, so here once we reach the leaf, we are just creating a node with the value and returnig it
                             # This value will be returned to the previous function call

        if val < root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data:
            root.right = self.insert(root.right, val)

        return root # finally we return root
                
            

            

root                            = Node(10)
root_left                       = Node(5)
root_right                      = Node(15)
root_left_left                  = Node(3)
root_left_right                 = Node(7)
root_right_left                 = Node(12)
root_right_right                = Node(20)
root_right_right_right          = Node(30)
root_left_left_left             = Node(1)

root.left                       = root_left
root.right                      = root_right
root_left.left                  = root_left_left
root_left.right                 = root_left_right
root_right.left                 = root_right_left
root_right.right                = root_right_right
root_right_right.right          = root_right_right_right
root_left_left.left             = root_left_left_left


root.inorder(root)
root.deleteNode(root, 20) ; print('')
root.inorder(root)
root.insert(root, 11) ; print('')
root.inorder(root)
root.insert(root, 9) ; print('')
root.inorder(root)
root.deleteNode(root, 5) ; print('')
root.inorder(root)

