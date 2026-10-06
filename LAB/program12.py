def rob(nums):
    def f(a):
        x = y = 0
        for n in a:
            x, y = y, max(y, x+n)
        return y
    return max(f(nums[:-1]), f(nums[1:]))

print(rob([2,3,2]))    
print(rob([1,2,3,1]))  