def new_func(file):
    count = 0
    for i in file:
        count += 1
        if i.startswith("For"):
            print(i)
    return count
name = input("Enter File name:")
try:
    file = open(name)
    print("no of lines:",new_func(file))
except:
    print("File not found")