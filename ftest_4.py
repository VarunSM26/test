temp = -1
sum = 0
iter = 0
for i in range(1,101,10):
    sum = sum + i
    temp = max(temp,i)
    iter += 1
    print(i,end = " ")
print("\nMax number:",temp)
print("Total:",sum)
print("Avg:",int(sum/iter))