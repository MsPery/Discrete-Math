# Discrete-Math
1. Write a programme to test if a given list of elements constitutes a set. It should take as its input a
list of elements and should output a True or False value.
If the truth value is False then it must also output the list converted to a set or to a list which
represents the set.
As well as the code, submit an example in your write-up of a list of elements which is not a set
and the output that your code gives on this example.
 E.g. For the input [’Alex’, ’Bob’, ’Sam’, ’Brian’, ’Brian’, ’Sam’, ’Sam’] it should output
something like:
False, the set should be: [’Alex’, ’Bob’, ’Brian’, ’Sam’]
2. Write a programme that takes as input 2 finite sets of any size, A, B, and outputs the following:
a) the truth value of B ⊆ A,
b) the set A − B,
c) the set A × B.
You may need to investigate the use of sets in Python. Please see the following website for a short
introduction and then continue your learning by searching online for other resources if you need
them: https://www.w3schools.com/python/python_sets.asp.
As well as the code, submit 1 example in your write-up of sets A and B and the outputted values
for a)-c).
3. Write a programme that takes as input 2 finite lists of any size, A, B, and outputs the following:
a) the truth value of B ⊆ A,
b) a list representing the set A − B,
c) a list representing the set A × B.
This is the same question as Question 2 except you are not allowed to use the set environment in
Python nor are you allowed to use in-built or package Python functions specific to sets which output
the required sets immediately. You must use lists, for loops, if statements, and other basic Python
commands.
4.Write a programme that takes as input a finite set or list (you may decide) A and a list R where
R is of the form (written mathematically):
R = {(x1, y1),(x2, y2), ...,(xn, yn)}.
Your code should first check if R is a relation on A (that is, if R is a set and if R ⊆ A × A).
If R is not a relation on A, your programme should output a statement to this effect.
If R is a relation on A then your programme should output which of the following properties
the relation satisfies:
a) reflexive,
b) transitive, and/or
c) symmetric.
(Remember, a relation can have none, one, two, or all three of the above properties.) If the relation
R fails one of these properties, your code should output the element(s) which fail(s) this
property.
In addition to the code, submit 1 example in your write-up of an A and R where R is a relation
on A and 1 example where R is not a relation on A, along with the output of your code for these
examples
5.Write a programme that takes as input 2 finite sets or lists (you decide) X and Y , where X, Y ⊂ Z,
and outputs a truth value (’True’ or ’False’) for the following statement:
∀x ∈ X, ∃y ∈ Y such that y | x.
In addition to the code, give 1 example in your write-up of sets X, Y where this truth value is
True, and 1 example where the truth value is False.
