class BinarySearchTree:
    def __init__(self, value):
        #these are nodes
        self.value = value
        self.left = None
        self.right = None

    # # Insert the given value into the tree / Recursive
    # #Does not return anything
    # def insert(self, value):
    #     #need base case
    #     if self is None: #in an empty spot in the tree
    #         self = BinarySearchTreeNode(value)

    #     else: #Self is a node with a value
    #         #compare value to the value at this node
    #         if value < self.value:
    #             #move to the left
    #             self.left.insert(value)
    #     #if we are not at base case, move toward base case

    def insert(self, value):
        #Self.left and/or self.right need to be valid nodes for us to call insert

        if value < self.value:
            #check to see if valid node
            if self.left:
                self.left.insert(value)
                #left side is empty
            else:
                #we have found a valid parking spot
                self.left = BinarySearchTree(value)
        #otherwise, value >= self.value
        else: 
            #check if right is valid node
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Is equal to root
        if target == self.value:
            return True

        #is less than root
        elif target < self.value:
            #If there is nothing to the left of root. Not in BST
            if self.left is None:
                return False
            #select value to the left and start over
            return self.left.contains(target)

        #is greater than root
        elif target > self.value:
            #if nothing to the right, NOt in BST
            if self.right is None:
                return False
            #select value to the right and start over
            return self.right.contains(target)