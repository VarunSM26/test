file = open("ftest.txt",'r')
iter = 0
for i in file:
    if i.startswith("Philosophy"):
        print(i)
    iter += 1
print("No of lines:",iter)