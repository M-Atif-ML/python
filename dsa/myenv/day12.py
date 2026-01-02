# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     l_part = arr[:mid]
#     r_part = arr[mid:]
#
#     l_part = merge_sort(l_part)
#     r_part = merge_sort(r_part)
#
#     return merge(l_part,r_part)
#
# def merge(left,right):
#     new_list = []
#     i,j = 0,0
#
#     while i< len(left) and j < len(right):
#         if left[i] < right[j]:
#             new_list.append(left[i])
#             i+=1
#         else:
#             new_list.append(right[j])
#             j+=1
#     new_list.extend(left[i:])
#     new_list.extend(right[j:])
#     return new_list
#            # [-4, -1, 0] [1,2,2]
#
#
# l = [12,2,4,2,31,-2]
# print(merge_sort(l))

arr = [16,1,0,9,100,1,23,1,23,12,312,3,12412,3,12,312,3123]

i = 0
j = len(arr)-1
new_arr = list()
while i <= j:
    if arr[i] <= arr[j]:
        new_arr.append(arr[j])
        j-=1
    if arr[i] >= arr[j]:
        new_arr.append(arr[i])
        i+=1
print(new_arr)
