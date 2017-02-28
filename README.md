# DeductionTree
Author: Logan Pedersen
Simple Tree that takes problems and tests for those problems, then finds possible causes/solutions

Define test functions and plug them into your problem_test() objects.

Current example tree is built as follows:

Root problem: 'server is broken'
tests (with associated problems): 'cpu test' [1,2,3], 'ip test'[3,5,6], 'computer test'[2,4,5,3]

Results:
cpu fails and ip fails: problem 3
cpu fails and computer fails: problems 2 and 3
computer fails: Problems 2, 4, 5, and 3
