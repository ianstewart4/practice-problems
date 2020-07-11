# Printing an array in reverse in Python
def printReverse(arr):
	i = len(arr)
	for i in range(len(arr)-1, -1, -1):
		print(arr[i])
		

testArray = [1, 2, 3, 4, 5, 6, 7, 8]
# print(len(testArray))
printReverse(testArray)