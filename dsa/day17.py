nums = [2,1,3,9]
n = len(nums)
temp =1

ans = [1]*n
for i in range(n):
    ans[i] = temp
    temp *= nums[i]
temp = 1
print(ans)
for i in range(n-1,-1,-1):
    ans[i] *= temp
    temp *= nums[i]
    # temp


print(ans)