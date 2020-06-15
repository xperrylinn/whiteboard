def isValidSubsequence(array, sequence):
	i, j = len(sequence)-1, len(array)-1 # assing the last index of each list
	while (i > -1 and j > -1): # Keep searching for matches until you are out of elements in either list
		num, curr = sequence[i], array[j]
		if num == curr: # only consider the next element of sequence if you found a match
			i -= 1
		j-=1 # regardles of match, consider next element
	if i < 0: # if all elements of sequence were matched, the index iterator of sequence will be negative
		return True
	else:
		return False

# Notes:
# - O(n) time | O(1) space - where n is the length of the array 
# - The goal of the problen is to return True or False
# -- determine the minimal condition(s) for returning True/False: 
#    when you have matched all elements in with elements in array
# -- in terms of the implementation how is that condition expressed?: 
#    when the iterator index of sequence is out of bounds, i.e. you matched all elements

