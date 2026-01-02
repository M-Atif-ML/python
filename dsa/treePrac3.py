arr = [[1 , 2, 3, 4],
       [5 , 6, 7, 8],
       [9 ,10,11,12],
       [13,14,15,16]]
n = len(arr[0])
m= len(arr)
# 0 = left-right
# 1 = top-bottom
# 2 = right-left
# 3 = bottom-top

ans = []

top,bottom,left,right = 0,m-1,0,n-1
move= 0
while top <= bottom and left<=right:

    if move == 0:
        for i in range(left,right+1):
            ans.append(arr[top][i])
        top+=1
    elif move == 1:
        for i in range(top,bottom+1):
            ans.append(arr[i][right])
        right-=1
    elif move == 2:
        for i in range(right,left-1,-1):
            ans.append(arr[bottom][i])
        bottom-=1
    elif move == 3:
        for i in range(bottom,top-1,-1):
            ans.append(arr[i][left])
        left+=1

    move = (move+1) % 4
    # temp = []
print(ans)
