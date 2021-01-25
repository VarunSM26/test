while True:
    name = input("Enter the string: ")
    if name[0] == '#':
        continue
    elif name == 'done':
        break
    print(name)
print("Done")