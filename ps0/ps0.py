#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    if T == None:
        return 0
    T.temp = 1 #root node adds 1 to size
    if T.left != None:
        T.temp = T.temp + calculate_size(T.left) #add size of proper subtree on the left
    if T.right != None:
        T.temp = T.temp + calculate_size(T.right) #add size of proper subtree on the right
    return T.temp #enables addition via recursion



#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T, L, U): 
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints
    if T == None: 
            return None
    # Your code goes here
    calculate_size(T) #this function is O(n), so can only be run once
    
    def auxfnc(T, L, U): 
        if T.left == None and T.right == None:
                return None #leaf node reached - may only happen if U, L improper, by theorem in #2
        else:
            if T.left != None and T.left.temp >= L:
                if T.left.temp <= U:
                    subtr = T.left 
                    T.left = None #removes subtree from tree
                    return subtr
                else:
                    return auxfnc(T.left, L, U)
            elif T.right != None and T.right.temp >= L:
                if T.right.temp <= U:
                    subtr = T.right 
                    T.right = None #removes subtree from tree
                    return subtr 
                else:
                    return auxfnc(T.right, L, U)
            else:
                return T 
    return auxfnc(T, L, U)
    

