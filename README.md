# Algorithm Strategy Small Project 2

## Bezier Curve Constructor

Constructing Bezier Curve with Middle Point Algorithm based on Divide and Conquer

## Requirements

Note:  
The program will most likely still run properly if a newer version is already installed

- Python 3.12.2  
  Install Python 3.12.2 from [here](https://www.python.org/downloads/release/python-3122/)

  Python packages:

  - NumPy 1.26.4 and its dependencies  
    Install NumPy 1.26.4 with pip:
    ```
    pip install numpy==1.26.4
    ```
  - Matplotlib 3.8.3 and its dependencies  
    Install Matplotlib 3.8.3 with pip:

    ```
    pip install matplotlib==3.8.3
    ```

## How to run

1. Clone this repository

   ```
   git clone https://github.com/bastianhs/Tucil2_13522034.git
   ```

2. Change directory to the main directory

   ```
   cd Tucil2_13522034
   ```

3. Run main.py

   ```
   python src/main.py
   ```

   or

   ```
   python3 src/main.py
   ```

## Input points format

You can input points from terminal or .txt file.  
The .txt file must be placed in the **test** folder.  
You need **at least 2 points** to construct a bezier curve.  
Point format:

```
x_coordinate, y_coordinate
```

For example:

```
3, 7
4.5, 8.0
2, 2.3
-0.5, -11
```

## Iteration

You can input the number of iterations when the terminal ask you to do so.

Iteration will determine how smooth the result.  
More iterations will produce smoother graph.  
But, it will take more time to get the result.

The number of iterations in divide and conquer will not produce the same result as in brute force.  
To achieve the same result, use the following equation:

$iteration_{bf} = 2^{iteration_{dnc}} + 1$

$iteration_{bf}$ is the number of iterations when using brute force  
$iteration_{dnc}$ is the number of iterations when using divide and conquer

So, if you use 5 iterations for divide and conquer, you will need 33 iterations for brute force to achieve the same result.

## Visualization

WARNING !  
Visualization with more than 10 iterations for divide and conquer could potentially make the program lag.

## Creator

Bastian H. Suryapratama  
13522034  
K-02
