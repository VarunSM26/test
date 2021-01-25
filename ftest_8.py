"""Word Counter"""
# file = open('ftest.txt')
# z = file.read()
z = input("Enter the string:")
name = dict()
names = []
for i in z.split(" "):
    # if i not in name:
    #     name[i] = 1
    # else:
    #     name[i] += 1 
    name[i] = name.get(i,0) + 1
print(name)
#print(name['jai'])