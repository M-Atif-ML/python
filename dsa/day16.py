arr = [8,3,-2,4,10,-1,0,5,3]
prefix = [0]*(len(arr)+1)
prefix[0] = arr[0]

for i in range(1,len(arr)+1):
    prefix[i] = prefix[i-1] + arr[i-1]

print(prefix)
range_sum = prefix[8]-prefix[2]
print(range_sum)


check= 0
