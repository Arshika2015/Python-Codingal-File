l = [8,4,3,7,6,10,20]
print(l)
sum = 0
for i in l:
    sum=sum+i
average = sum/len(l)
print("sum is",sum)
print("average is ",average)
l.sort()
print("the smallest element is",l[0])
print("the largest element is ",l[-1])
