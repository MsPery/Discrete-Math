def check_subset(A, B):
    """
    function to check whether B is a subset of A
    :param A: The first list
    :param B: The second list
    """
    for i in B:
        if i not in A:
            print("B is not a subset of A")
            return
    print("B is a subset of A")


def set_difference(A,B):
    """
    function to calculate the set difference of A and B
    :param A: First List
    :param B: Second List
    :return: The set difference of A and B
    """
    set_diff = []
    for i in A:
        if i not in B:
            set_diff.append(i)
    print(f"A - B = {set_diff}")


def cartesian_prod(A,B):
    """
    :param A: first list
    :param B: second list
    :return: cross_product of A and B
    """
    cartesian_prod=[]
    for i in A:
        for j in B:
            cartesian_prod.append((i,j))
    print(f"A X B = {cartesian_prod}")

A = [1, 4, 2, 5,11]
B = [1, 2, 5, 7]

check_subset(A,B)
set_difference(A,B)
cartesian_prod(A,B)


