# Find the closest value in a BST

# Convert tree to list, find left most closest value in list
def findClosestValueInBst(tree, target):
	# 	BST to array by tree traversal
	#		traverse the tree, put nodes into a list
	#		calc delta b/t abs of target minus list elem
	# 		return the min most left elem
	l = pre_order_traversal(tree, target)
	print(l)
	l2 = [abs(val - target) for val in l]
	min_val = min(l2)
	for i in range(0, len(l2)):
		if l2[i] == min_val:
			return l[i]
	return min(l)
	
def pre_order_traversal(tree, target, l=[]):
	if tree:
		l.append(tree.value)
        # Use BST property to avoid considering all parts of the tree
		if target < tree.value:
			pre_order_traversal(tree.left, target, l)
		if target > tree.value:
			pre_order_traversal(tree.right, target, l)
	return l

# Recurisve helper fxn approach, no array, keep track of closest while traversing
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space -- linear tree
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

# Helper function traverses tree and keeps track of closest value
def findClosestValueInBstHelper(tree, target, closest):
	# Check if current Node is None
	if tree == None:
		return closest
	# Check if current Node has the new closest
	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest

# Iterative approach
def findClosestValueInBst(tree, target):
    closest = tree.value
	while tree != None:
		delta = abs(tree.value - target)
		if delta < abs(target - closest):
			closest = tree.value
		if target < tree.value:
			tree = tree.left
		elif target > tree.value:
			tree = tree.right
		else:
			break
	return closest
