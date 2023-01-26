i = 1
maxV = 0
minV = 0
sum = 0
tlist = []
while i != 0:
    i = int(input())
    if i == 0:
        break
    sum += i
    tlist.append(i)
setU = set(tlist)
maxV = max(tlist)
minV = min(tlist)

for c in setU:
    print(f"{c} = {tlist.count(c)}")

print("Sum = ", sum)
print("Average = ", sum/len(tlist))
print("Max = ", maxV)
print("Min = ", minV)
print("Uniques = ", setU)

