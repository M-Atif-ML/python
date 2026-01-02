string = "pwwkew"

longest = 0
l = 0

set=set()

for r in range(0,len(string)):
    if r == 0 and l ==0:
        set.add(string[r])
        continue

    if string[r] != string[l]:
        set.add(string[r])
    else:
        set.remove(string[l])
        while string[r] != string[l]:
            l +=1
        set.add(string[r])
print(len(set))
