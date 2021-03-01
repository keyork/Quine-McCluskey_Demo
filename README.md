# Quine-McCluskey_Demo

This is a demo of Quine-McCluskey used Python.

## mind map

- input

  - A list of number, represents the logical expression to be simplified in Sum of Products form formula, like <a href="https://www.codecogs.com/eqnedit.php?latex=[4,8,10,11,12,15]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?[4,8,10,11,12,15]" title="[4,8,10,11,12,15]" /></a>;

  - Another list of number, represents Don't Care term in the logical expression, like <a href="https://www.codecogs.com/eqnedit.php?latex=[9,14]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?[9,14]" title="[9,14]" /></a>;

  - Then, the hole logical expression is: 

    <a href="https://www.codecogs.com/eqnedit.php?latex=f(A,B,C,D,...)=\sum&space;m(4,8,10,11,12,15)&space;&plus;&space;d(9,14)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(A,B,C,D,...)=\sum&space;m(4,8,10,11,12,15)&space;&plus;&space;d(9,14)" title="f(A,B,C,D,...)=\sum m(4,8,10,11,12,15) + d(9,14)" /></a>

- output: a formula like <a href="https://www.codecogs.com/eqnedit.php?latex=f(A,&space;B,&space;C,&space;D)&space;=&space;BC'D'&space;&plus;&space;AC&space;&plus;&space;AB'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(A,&space;B,&space;C,&space;D)&space;=&space;BC'D'&space;&plus;&space;AC&space;&plus;&space;AB'" title="f(A, B, C, D) = BC'D' + AC + AB'" /></a>;

## method

### Step 1: Search "Prime Implicant"

Finding all prime implicants of the function.

### Step 2: Search "Minimum Cover"

Use those prime implicants in a *prime implicant chart* to find the essential prime implicants of the function, as well as other prime implicants that are necessary to cover the function.