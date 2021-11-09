def check_set(input_list):
    count = 0
    result = 0

    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j]:
                count += 1
    result = 1 if count == 0 else result
    return result

def check_subset(A, R):
    list1 = []
    for i in R:
        for j in i:
            if j not in A and i not in list1:
                list1.append(i)
    return list1


def check_reflexive(A, R):
    list1 = []
    for i in A:
        if [i, i] not in R and i not in list1:
            list1.append(i)
    return list1


def check_symmetric(R):
    list1 = []
    for i in R:
        if i[1] != i[0] and [i[1], i[0]] not in R and i not in list1:
            list1.append(i)
    return list1


def check_transitive(R):
    list1 = []
    #[1,3][3,4]
    W = R.copy()
    for i in R:
        W.remove(i)
        for j in W:
            if i[1] == j[0] and [i[0], j[1]] not in R and i not in list1:
                list1.append(i)
                list1.append(j)
        W = R.copy()
    return list1

A = [1, 4, 2, 5]
R = [(4, 4), (5, 5), (5, 2), (2, 4),(4,2),(2,5),(5,4),(2,2)]

R = [list(i) for i in R]

x = check_set(R)
if x == 1:
    print("R is a set")
    y = check_subset(A, R)
    if len(y) > 0:
        print(f"R is not a subset of AxA because the following element is in R but not in AxA: {y}")
        print("R is not a relation on A")
    else:
        print("R is a subset of AxA\nR is a relation on A")
        a = check_reflexive(A, R)
        if len(a) == 0:
            print("R is reflexive")
        else:
            str1 = ""
            for i in a:
                str1 += str(i) + " "
            print(f"R is not reflexive:{str1}")
        b = check_symmetric(R)
        if len(b) == 0:
            print("R is symmetric")
        else:
            print(f"R is not symmetric: {b}")
        c = check_transitive(R)
        if len(c) == 0:
            print("R is transitive")
        else:
            str2 = ""
            for i in c:
                str2 += str(i) + " "
            print(f"R is not transitive:{str2}")
else:
    print("R is not a set")
