# Quine-McCluskey_Demo

This is a demo of Quine-McCluskey used Python.

## mind map

- input

  - A list of number, represents the logical expression to be simplified in Sum of Products form formula, like <img src="http://chart.googleapis.com/chart?cht=tx&chl=[4,8,10,11,12,15]" style="border:none;">;

  - Another list of number, represents Don't Care term in the logical expression, like <img src="http://chart.googleapis.com/chart?cht=tx&chl=[9,14]" style="border:none;">;

  - Then, the hole logical expression is: 

    <img src="http://chart.googleapis.com/chart?cht=tx&chl=f(A,B,C,D,...)=\sum m(4,8,10,11,12,15) + d(9,14)" style="border:none;">

- output: a formula like <img src="http://chart.googleapis.com/chart?cht=tx&chl=f(A, B, C, D) = BC'D' + AC + AB'" style="border:none;">;

## method

### Step 1: Search "Prime Implicant"

Finding all prime implicants of the function.

### Step 2: Search "Minimum Cover"

Use those prime implicants in a *prime implicant chart* to find the essential prime implicants of the function, as well as other prime implicants that are necessary to cover the function.