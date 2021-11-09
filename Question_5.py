X = input("Please enter the elements of the first list separated by spaces:\n").split(" ")
Y = input("Please enter the elements of the second list separated by spaces:\n").split(" ")

count = 0

for x in X:
    for y in Y:
        if int(x) % int(y) == 0:
            count += 1
            break

print(True) if count >= len(X) else print(False)




