'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    a = 0
    b = k
    result = []
    
    while b <= len(nums):
        max = []
        for x in nums[a:b]:
            if not max or x > max:
                max = x
                
        result.append(max)
        a += 1
        b += 1
        
    return result

    # the below code runs in approx 15secs vs the above which is 30secs
    # however is still fails the 'large_input' test which requires sub 1sec!

    # win = []
    # small = [0] * k
    # for i in range(0, len(nums) - k + 1):
    #         small = nums[i:i + k]
    #         win.append(max(small))

    # return win


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
