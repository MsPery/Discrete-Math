def check_sets(list_1=[]):
   # list_1.sort()
   list_2 = set(list_1)
   list_2 = list(list_2)
   list_2.sort()
   if list_1 == list_2:
       print("True")
   else:
       print("False", "the set should be :", list_2)


check_sets(['Joycelyn', 'Peris', 'Jeanne', 'Jeanne', 'Mercy', 'Mercy'])

