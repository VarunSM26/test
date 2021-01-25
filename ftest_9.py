dictt = dict()
names = ['Jhon','Bob','Walker','Tom','Bob']
for i in names:
    # if i not in dictt:
    #     dictt[i] = 1
    # else:
    #     dictt[i] += 1
    dictt[i] = dictt.get(i,0) + 1
print(dictt)