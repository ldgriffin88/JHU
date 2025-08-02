"""
Filename: Red_Black_Tree.py

This file implements a red-black tree based on the pseudocode provided in 
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
Introduction to Algorithms (4th ed.). MIT Press.

Author: Logan Griffin
Created 3/3/25
Description: This file contains two classes: Node and RBT. The node class creates nodes for the red-black tree implementation. The RBT has the following methods: minimum, maximum, insert, insert_fixup, delete, delete_fixup, transplat, left_rotate, right_rotate, and print_tree.
"""

class Node:
    """
    This class creates nodes for the red-black tree implemented in this file.

    Attributes:
        dist: The Euclidean distance between p1 and p2. This serves as the key for the RBT.
        p1: A tuple representing an ordered pair.
        p2: A tuple representing an ordered pair.
        color: RED or BLACK for red-black tree implementation
        left: The node's left child.
        right: The node's right child.
        parent: The node's parent.
    """
    def __init__(self, dist, p1, p2, color="RED", left=None,
                 right=None, parent=None):
        """
        Constructs new instance of node with inital color RED and no family memebers.
        """
        self.dist = dist
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RBT:
    """
    This class implements methods for a red-black tree to store instances of the Node class.

    Attributes:
        root: The root node of the tree.
        size: The number of elements in the tree.
        NIL: The sentinel node.
    """
    def __init__(T):
        """
        Constructs new instance of RBT with sentinel node T.NIL as the root and size = 0.
        """

        # sentinel node
        T.NIL = Node(dist=None, p1=None, p2=None, color="Black")

        # sentinel children and parent are itself
        T.NIL.left = T.NIL.right = T.NIL.parent = T.NIL

        # initially set root as sentinel 
        T.root = T.NIL

        # track number of nodes in tree
        T.size = 0

    def minimum(T, x):
        """
        Finds the node with the minimum key (distance)

        @param T: The instance of RBT to search.
        @param x: The node to start the search at.
        @return: The node with smallest distance.

        """
        while x.left != T.NIL:
            x = x.left
        return x
    
    def maximum(T, x):
        """
        Finds the node with the maximum key (distance)

        @param T: The instance of RBT to search.
        @param x: The node to start the search at.
        @return: The node with largest distance.

        """
        while x.right != T.NIL:
            x = x.right
        return x

    def insert(T, dist, p1, p2):
        """
        Inserts a node with attributes dist, p1, and p2, into RBT T.

        @param T: The tree to insert node into.
        @param dist: The distance associated with the node being inserted.
        @param p1: The first point the distance was calculated from.
        @param p2: The second point the distance was calculated from.

        """
        # initialize new node
        z = Node(dist, p1, p2, color="RED", left=T.NIL, right=T.NIL, parent=T.NIL)

        # node being compared to z
        x = T.root
        # will be the parent of z
        y = T.NIL

        # descent until reaching sentinel
        while x != T.NIL:
            y = x

            if z.dist < x.dist:
                x = x.left
            else:
                x = x.right
        # set parent at location
        z.parent = y

        if y == T.NIL:
            # tree was empty
            T.root = z
        elif z.dist < y.dist:
            y.left = z
        else:
            y.right = z
        
        # both children are sentinel
        z.left = T.NIL
        z.right = T.NIL
        # new node starts red
        z.color = "RED" 

        # correct RBT violations
        T.size += 1
        T.insert_fixup(z)
        print(f"Tree size is now: {T.size}")

    def insert_fixup(T, z):
        """
        Restores red-black tree properties after insertion.

        @param T: The RBT to restore properties in.
        @param z: The node that was inserted.

        """
        while z != T.root and z.parent.color == "RED":
            # if z's parent is a left child
            if z.parent == z.parent.parent.left:
                # z's uncle
                y = z.parent.parent.right

                # are z's parent and uncle both red?
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    # uncle is black and z is right child
                    if z == z.parent.right:
                        z = z.parent
                        T.left_rotate(z)
                    # uncle z is black and z is left child
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    T.right_rotate(z.parent.parent)
            else:
                # same but with right and left exchanged
                y = z.parent.parent.left
                
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        T.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    T.left_rotate(z.parent.parent)
        T.root.color = "BLACK"

    def delete(T,z):
        """
        Deletes a node from the RBT and calls delete_fixup to restore the red-black tree properties.

        @param T: The tree to delete from.
        @param z: The node to delete.

        """        

        y = z
        y_original_color = y.color

        if z.left == T.NIL:
            x = z.right
            # replace z by right child
            T.transplant(z, z.right)
        elif z.right == T.NIL:
            x = z.left
            # replace z by left child
            T.transplant(z, z.left)
        else:
            # find z's successor
            y = T.minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            # if y is father down the tree
            if y != z.right:
                # replace y by its right child
                T.transplant(y, y.right)
                # z's right child becomes y's right child
                y.right = z.right
                y.right.parent = y
            else:
                # incase x is t.nil
                x.parent = y
            
            # replce z by successor y
            T.transplant(z, y)
            # give left child to y
            y.left = z.left
            # since y had no left child
            y.left.parent = y
            y.color = z.color
        
        T.size -= 1
        # if any violations occurred, correct them
        if y_original_color == "BLACK":
            T.delete_fixup(x)
    
    def delete_fixup(T, x):
        """
        Restores red-black tree properties after a node is deleted.

        @param T: The tree to restore properties in.
        @param x: The node to start restoration at.

        """
        while x != T.root and x.color =="BLACK":
            # if x is a left child
            if x == x.parent.left:
                # w is x's sibling
                w = x.parent.right

                # case 1: x's sibling w is red
                if w.color == "RED":
                    w.color == "BLACK"
                    x.parent.color == "RED"
                    T.left_rotate(x.parent)
                    w = x.parent.right
                # case 2: x's sibling w is black and both of w's children are black
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color == "RED"
                    x = x.parent
                else:
                    # case 3: x's sibling is black, w's left child is red,
                    # and w's right child is black
                    if w.right.color == "BLACK":
                        w.left.color == "BLACK"
                        w.color == "RED"
                        T.right_rotate(w)
                        w = x.parent.right
                    # case 4: x's sibling w is black and w's right child is red
                    w.color = x.parent.color
                    x.parent.color == "BLACK"
                    w.right.color == "BLACK"
                    T.left_rotate(x.parent)
                    x = T.root
            else:
                # same as above but with right and left exchanged
                w = x.parent.left
                if w.color =="RED":
                    w.color == "BLACK"
                    x.parent.color == "RED"
                    T.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color == "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color == "BLACK"
                        w.color == "RED"
                        T.left_rotate(w)
                        w = x.parent.left
                    
                    w.color == x.parent.color
                    x.parent.color == "BLACK"
                    w.left.color == "BLACK"
                    T.right_rotate(x.parent)
                    x = T.root
        x.color == "BLACK"

    def transplant(T, u, v):
        """
        Replaces subtree rooted at node u with subtree rooted at node v. Used when a node is deleted.

        @param T: The tree being worked on.
        @param u: A node within T.
        @param v: A node within T.

        """
        # if u is root of T
        if u.parent == T.NIL:
            T.root = v
        # if u is left child
        elif u == u.parent.left:
            u.parent.left = v
        # if u is right child
        else:
            u.parent.right = v
        
        v.parent = u.parent

    def left_rotate(T, x):
        """
        Rotates a subtree of nodes to the left.

        @param T: The tree to rotate in.
        @param x: The node that is rooted at the subtree to be rotated.

        """
        y = x.right
        # turn y's left subtree into x's right subtree
        x.right = y.left
        # if y's left subtree is not empty
        if y.left != T.NIL:
            # x becomes parent of subtree's root
            y.left.parent = x
        
        # x's parent becomes y's parent
        y.parent = x.parent

        # if x was the root
        if x.parent == T.NIL:
            # y becomes root
            T.root = y
        # otherwise x was left child
        elif x == x.parent.left:
            # y becomes left child
            x.parent.left = y
        # otherwise x was right child
        else:
            # now y is
            x.parent.right = y
        # x becomes y's left child
        y.left = x
        x.parent = y

    def right_rotate(T, y):
        """
        Rotates a subtree of nodes to the right.

        @param T: The tree to rotate in.
        @param x: The node that is rooted at the subtree to be rotated.

        """
        x = y.left
        # turn x's right subtree into y's left subtree
        y.left = x.right
        # if x's right subtree is not empty
        if x.right != T.NIL:
            # y becomes parent of subtree's root
            x.right.parent = y
        
        # y's parent becomes x's parent
        x.parent = y.parent

        # if y was the root
        if y.parent == T.NIL:
            # x becomes root
            T.root = x
        # otherwise y was right child
        elif y == y.parent.right:
            # x becomes right child
            y.parent.right = x
        # otherwise y was left child
        else:
            # now x is left child
            y.parent.left = x
        # y becomes x's right child
        x.right = y
        y.parent = x

    def print_tree(T, x):
        """
        Prints a tree by using an recursive in-order traversal.

        @param T: The tree to print.
        @param x: The node to start the traversal at.

        """
        if x != T.NIL:
            T.print_tree(x.left)
            # print value
            print(f"Distance: {x.dist:.4f}, Points: ({x.p1[0]:.4f},{x.p1[1]:.4f}), ({x.p2[0]:.4f},{x.p2[1]:.4f})")
            T.print_tree(x.right)
    
