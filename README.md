# Quine-McCluskey_Demo

This is a demo of Quine-McCluskey used Python.

## mind map

- input

  - A list of number, represents the logical expression to be simplified in Sum of Products form formula, like <img src="./pic/001.png" alt="001" style="zoom:10%;" />;

  - Another list of number, represents Don't Care term in the logical expression, like <img src="./pic/002.png" alt="001" style="zoom:10%;" />;

  - Then, the hole logical expression is: 

    <img src="./pic/003.png" alt="001" style="zoom:10%;" />

- output: a formula like <img src="./pic/004.png" alt="001" style="zoom:10%;" />;

## method

### Step 1: Search "Prime Implicant"

Finding all prime implicants of the function.

### Step 2: Search "Minimum Cover"

Use those prime implicants in a *prime implicant chart* to find the essential prime implicants of the function, as well as other prime implicants that are necessary to cover the function.