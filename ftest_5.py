name = input("Enter string:")
iter = 0
#for i in name:
#    iter += 1
while iter < len(name):
    #print(iter,name[iter])
    iter += 1
if 'a' in name:
    print("It is present")
#print(iter)
#print(name.lower())
#x = type(name)
#print(dir(name))
print(name.find("ar"))
print(name.replace("ar","**"))
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(name.startswith("v"))
#print(name[:3],name[3:])