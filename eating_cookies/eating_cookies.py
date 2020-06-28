'''
Input: an integer
Returns: an integer
'''
# Caching /memoization: Let's save our work so we don't have
# to recompute it again

# Need some sort of data structure where we'll save the data
# arrays and dictionaries
# if we check our cache and see that he answer we're looking for 
# is already in there, just return the answer
# What if the cache doesn't have what we're looking for? Or how
# do we get answers in there?
# There's going to be a first time for calculating an answer, and we're
# going to do it the same way we're currently doing it

def eating_cookies(n):
    # Your code here
    # base case: when there are no more cookies
    if n == 0:
        return 1
    # check for negative n values
    elif n < 0:
        return 0

    # # represents Cookie Monster eating one cookie
    # eating_cookies(n-1)
    # # represents Cookie Monster eating one cookie
    # eating_cookies(n-2)
    # # represents Cookie Monster eating one cookie
    # eating_cookies(n-3)

    # # add them up will be the total no. of ways we can eat 'n' cookies
    # # this represents our recursive case where there's still some cookies to be eaten
    # return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    # init our cache if we don't have it yet
    # add a case to have us check the cache (if it's there AND if we've saved an answer at that position)
    # '0' means we haven't seen that answer before
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # cache = {i: 0 for i in range(n+1)}
            cache = [0 for _ in range(n+1)]
        # we can go ahead and save our answer to the cache
        # we're returning the same thing as previously but we're saving in our cache at index 'n'
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
