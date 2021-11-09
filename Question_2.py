# Write a programme that takes as input 2 finite sets of any size, A, B, and outputs the following:
# the truth value of B ⊆ A,
# the set A − B,
# the set A × B.

# noinspection PyUnresolvedReferences

import itertools

set_A = {"1", "2", "3", "4", "5", "6", "7", "8"}  # A set of natural number less that 10
set_B = {"2", "4", "6", "8"}  # A set of positive integers that are divisible by 2 and they are less than 10
print(sorted(set_A))
print(sorted(set_B))
print("B ⊆ A:", set_B.issubset(set_A))
print("A-B:", sorted(set_A.difference(set_B)))
for cartesianProduct in itertools.product(set_A, set_B):
   print(cartesianProduct)



