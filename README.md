# Python Algorithms and Data Structures

This repository contains implementations of popular data structures and interview questions in Python.

Each data structure has its own separate README
with related explanations and links for further reading (including ones
to YouTube videos).


The explanations of the data structures are from <a href="https://github.com/trekhleb/javascript-algorithms"> Oleksii Trekhleb Project</a>

*This project is meant to help you on your job interview journey. I will be updating it as I embark on my own journey*

<br>
## Data Structures

A data structure is a particular way of organizing and storing data in a computer so that it can
be accessed and modified efficiently. More precisely, a data structure is a collection of data
values, the relationships among them, and the functions or operations that can be applied to
the data.

`B` - Beginner, `A` - Advanced

* `B` [Linked List](src/data-structures/linked-list)

## Interview Questions

Below is a list of interview questions. Will keep on adding as I encounter them

`E` - Easy, `M` - Medium, `H` - Hard, `VH` - Very Hard

### Questions by Topic

* **Recursion & Dynamic Programming**
  * `E` [Capitalize First](src/interview_questions/recursionAndDynamicProgramming/easy/capitalizeFirst) - Given an array of words write a recursive function to capitalize the first letter of every word in the array.
  * `E` [Collect Strings](src/interview_questions/recursionAndDynamicProgramming/easy/collectStrings) - Write a function that accepts objects and returns an array of all the values in the object that have a typeof string.
  * `E` [Decimal to Binary](src/interview_questions/recursionAndDynamicProgramming/easy/decToBinary) - Write a recursive function that converts a decimal number to binary.
  * `E` [Factorial](src/interview_questions/recursionAndDynamicProgramming/easy/factorial) - Write a recursive function that computes the factorial of a given number
  * `E` [Fibonacci](src/interview_questions/recursionAndDynamicProgramming/easy/fibonacci) - Given a  value 'n' Write a recursive function to compute the fibonacci number at position 'n' 
  * `E` [Flatten](src/interview_questions/recursionAndDynamicProgramming/easy/flatten) - write a recursion function called flatten which accepts an array of arrays and returns a new array with all the values flattened.
  * `E` [Greatest Common Divisor](src/interview_questions/recursionAndDynamicProgramming/easy/greatestCommonDivisor) - Write a recursive function that computes the greatest common divisor of number.
  * `E` [isPalindrome](src/interview_questions/recursionAndDynamicProgramming/easy/isPalindrome) - Write a recursive function if the string passed to is a palindrome, otherwise return false.
  * `E` [nestedEvenSum](src/interview_questions/recursionAndDynamicProgramming/easy/nestedEvenSum) - Write a recursive function to return the sum of all even numbers in an object which may contain nested objects.
  * `E` [Power of Number](src/interview_questions/recursionAndDynamicProgramming/easy/powerOfNumber) - Write a recursive function that computes the power of a number
  * `E` [Product of Array](src/interview_questions/recursionAndDynamicProgramming/easy/productOfArray) - Write a recursive function that takes an array of numbers and returns a product of all the elements
  * `E` [Recursive Range](src/interview_questions/recursionAndDynamicProgramming/easy/recursiveRange) - Write a recursive function that accepts a number and adds all the number from 0 to the number passed
  * `E` [Reverse](src/interview_questions/recursionAndDynamicProgramming/easy/reverse) -  Write a recursive function that accepts a string and returns a new string in reverse
  * `E` [Some Recursive](src/interview_questions/recursionAndDynamicProgramming/easy/someRecursive) - Write a recursive function which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the callback, otherwise it returns false
  * `E` [Stringify Numbers](src/interview_questions/recursionAndDynamicProgramming/easy/stringifyNumbers) - Write a function that takes in an object and finds all the values which are numbers and converts them to strings. 
# them to strings. 
  * `E` [Sum of digits](src/interview_questions/recursionAndDynamicProgramming/easy/sumOfDigits) - Write a function that sums up a number recursively

* **Arrays**
  * `E` [Two Number Sum](src/interview_questions/arrays/easy/twoNumberSum) - Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
  If any two numbers in the input array sum up to the target sum, the function should return them in an array



### Interview Questions By Company

Here is a list of popular interview questions given asked by Big Companies


* **Google**


## Useful Information

### References

[▶ Data Structures and Algorithms on YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)

### Big O Notation

*Big O notation* is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
On the chart below you may find most common orders of growth of algorithms specified in Big O notation.

![Big O graphs](./assets/big-o-graph.png)

Source: [Big O Cheat Sheet](http://bigocheatsheet.com/).

Below is the list of some of the most used Big O notations and their performance comparisons against different sizes of the input data.

| Big O Notation | Computations for 10 elements | Computations for 100 elements | Computations for 1000 elements  |
| -------------- | ---------------------------- | ----------------------------- | ------------------------------- |
| **O(1)**       | 1                            | 1                             | 1                               |
| **O(log N)**   | 3                            | 6                             | 9                               |
| **O(N)**       | 10                           | 100                           | 1000                            |
| **O(N log N)** | 30                           | 600                           | 9000                            |
| **O(N^2)**     | 100                          | 10000                         | 1000000                         |
| **O(2^N)**     | 1024                         | 1.26e+29                      | 1.07e+301                       |
| **O(N!)**      | 3628800                      | 9.3e+157                      | 4.02e+2567                      |

### Data Structure Operations Complexity

| Data Structure          | Access    | Search    | Insertion | Deletion  | Comments  |
| ----------------------- | :-------: | :-------: | :-------: | :-------: | :-------- |
| **Array**               | 1         | n         | n         | n         |           |
| **Stack**               | n         | n         | 1         | 1         |           |
| **Queue**               | n         | n         | 1         | 1         |           |
| **Linked List**         | n         | n         | 1         | n         |           |
| **Hash Table**          | -         | n         | n         | n         | In case of perfect hash function costs would be O(1) |
| **Binary Search Tree**  | n         | n         | n         | n         | In case of balanced tree costs would be O(log(n)) |
| **B-Tree**              | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Red-Black Tree**      | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **AVL Tree**            | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Bloom Filter**        | -         | 1         | 1         | -         | False positives are possible while searching |

### Array Sorting Algorithms Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bubble sort**       | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Insertion sort**    | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Selection sort**    | n<sup>2</sup>   | n<sup>2</sup>       | n<sup>2</sup>       | 1         | No        |           |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | No        |           |
| **Merge sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | n         | Yes       |           |
| **Quick sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n<sup>2</sup>       | log(n)    | No        | Quicksort is usually done in-place with O(log(n)) stack space |
| **Shell sort**        | n&nbsp;log(n)   | depends on gap sequence   | n&nbsp;(log(n))<sup>2</sup>  | 1         | No         |           |
| **Counting sort**     | n + r           | n + r               | n + r               | n + r     | Yes       | r - biggest number in array |
| **Radix sort**        | n * k           | n * k               | n * k               | n + k     | Yes       | k - length of longest key |


