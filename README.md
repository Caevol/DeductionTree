# DeductionTree
<p>Author: Logan Pedersen</p>
<p>Simple Tree that takes problems and tests for those problems, then finds possible causes/solutions</p>

<p>Define test functions and plug them into your problem_test() objects.</p>

<p>Current example tree is built as follows:</p>

<p>Root problem: 'server is broken'</p>
<p>tests (with associated problems): 'cpu test' [1,2,3], 'ip test'[3,5,6], 'computer test'[2,4,5,3]</p>

<p>Results:</p>
<p>cpu fails and ip fails: problem 3</p>
<p>cpu fails and computer fails: problems 2 and 3</p>
<p>computer fails: Problems 2, 4, 5, and 3</p>
