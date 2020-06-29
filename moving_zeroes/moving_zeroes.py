'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here


	# this solution is a single pass through the input array
	# with O(1) space
    for i in range(len(arr)):
        if arr[i] == 0:
            x = arr[i]
            arr.remove(x)
            arr.append(x)
    return arr

    # this is an alternative solution, single pass through
    # the input array in O(1) space because as n increases
    # we still only store one value in 'count'

	# count = arr.count(0)
	# for i in range(0, count):
	# 	arr.remove(0)
	# 	arr.append(0)
	# return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")