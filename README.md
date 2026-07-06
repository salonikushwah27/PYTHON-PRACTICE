Variables & Conditional Statements
10 Python practice questions covering variable creation, conditional statements (if/elif/else), and logical operators.
Topics Covered
Variable creation & printing
Comparison operators (>, <, ==)
if / elif / else conditions
Logical operators (and, or)
Modulus operator for even/odd & divisibility checks
type() function
Multi-condition comparisons (finding largest of 3 numbers)


Errors Faced & Fixes
Q19 (Triangle classification using Pythagoras theorem): Had trouble understanding which index represented which side after sorting the values.
Fix: Used sorted() on the three sides so they are arranged in ascending order. This way, the largest side always ends up at index [2] (the hypotenuse), and the two smaller sides at [0] and [1]. Then applied the condition sides[0]**2 + sides[1]**2 == sides[2]**2 to check if it's a right-angled triangle.
Took some time to figure out, but resolved it by tracing through the sorted list manually.



