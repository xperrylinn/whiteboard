# Write a function that takes in a Binary tree and retuns a list of
# its branch sums ordered from leftmost branch to rightmost branch
# 
# A branch is the sum of all values in a Binary Tree branch. A 
# binary tree branch is a path of nodes in a tree that starts at the
# root and ends at any leaf

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	return branchSumsHelper(root, 0, [])

def branchSumsHelper(root, s=0, output=[]):
	if root == None:
		return
	else:
		if root.left == None and root.right == None:
			output.append(s + root.value)
		else:
			branchSumsHelper(root.left, s + root.value, output)
			branchSumsHelper(root.right, s + root.value, output)
	return output

# Notes:
#   -   O(n) Time | O(n) Space
#   --  time: we need to touch each of the n node. At every node constant time
#       operations.
#   --  space: aside from the recusrive calls on the stack, we are returning
#       a list sums and there are roughly 1/2 leaf nodes as there are nodes
#   -   The question is asking you determine the sum of node values from
#       root to each left, orderd left to right.
#   --  Left to right is achieved by choosing pre-order traversal of tree
  