# defining a tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        # first check if theres data in the root ,if its not htere then we m=insert
        if self.data==None:
            self.data=data
        else: #if there's data in the root, then check if its greater than root or less, if its less, we insert it on the left ad right wen its greater
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)


# function to print inorder
def inOrderPrint(root):
    if root is None:
        return
    else:
        inOrderPrint(root.left)
        print(root.data)
        inOrderPrint(root.right)

# function to print inorder
def preOrderPrint(root):
    if root is None:
        return
    else:
       print(root.data)
       preOrderPrint(root.left)
       preOrderPrint(root.right)


# function to print postorder
def postOrderPrint(root):
    if root is None:
        return
    else:
       postOrderPrint(root.left)
       postOrderPrint(root.right)
       print(root.data)

# main function  
if __name__=='__main__':
    
    root=Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
   
    # printing out all the nodes
    inOrderPrint(root)
    # preOrderPrint(root)
    # postOrderPrint(root)