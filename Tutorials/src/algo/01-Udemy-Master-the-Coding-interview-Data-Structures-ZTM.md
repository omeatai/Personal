# UDEMY-MASTER THE CODING INTERVIEW: DATA STRUCTURES + ALGORITHMS - ZERO TO MASTERY

## [COURSES](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/)

<details>
  <summary>1. Introduction </summary>

# Introduction

```jsbs
Data Structures:
- Arrays
- Stacks
- Queues
- Linked List
- Trees
- Tries
- Graphs
- Hash Tables

Algorithms:
- Sorting
- Dynamic Programming
- BFS and DFS (Searching)
- Recursion
```

<img width="1089" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7f5ca60c-29c8-4305-8efe-856328fe0b11">
<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c1a27b98-e0a5-465c-8315-67904460777c">

# Interview Session - https://youtu.be/XKu_SEDAykw

<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/d6495736-8b0c-428e-9d35-8287b0ef0466">

# Interview Cheat Sheet

<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/6c7edd7c-d636-4ed6-b786-6f046e76b9ac">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/79fc2d87-1f5d-4526-ba41-f68ebda852d7">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/85f19476-bd23-4cf7-9997-14cda646d6ae">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1a8c0813-356b-428f-b78a-56bf24be1910">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ffb24457-7309-4972-8e29-aebe709c87d2">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/57f75417-f507-4642-834f-b28e8312fe65">
<img width="1157" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/1a8f742e-a883-4df1-85e8-ee9c2a8d3634">

# #END </details>

<details>
  <summary>2. Measuring the Big O </summary>

# Measuring the Big O

<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dda2dee4-a8bd-4936-80b2-03c460f2205b">

# Example 1:

```js
const nemo = ['nemo'];

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

findNemo(nemo);
```

<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2c40ecbb-8a35-492a-a9ea-b83f2c691341">

# Example 2: Big O and Scalabnility

```js
const nemo = ['nemo'];

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

function findNemo2(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
  let t1 = performance.now();
  console.log('Call to find Nemo took ' + (t1 - t0) + ' milliseconds');
}

findNemo2(nemo);
```

<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/3cc3cc12-9d4a-4dd1-bb4d-d0edea9e631a">

# Example 3:

```js
const nemo = ['nemo'];

const large = new Array(1000).fill('nemo');

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

function findNemo2(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
  let t1 = performance.now();
  console.log('Call to find Nemo took ' + (t1 - t0) + ' milliseconds');
}

findNemo2(large);
```

<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/7530a16e-44f7-4ded-8671-734a2cedd0c6">

# #END </details>

<details>
  <summary>3. O(n) - Linear Time </summary>

# O(n) - Linear Time

# Example 1:

```js
const nemo = ['nemo'];

const large = new Array(5).fill('nemo');

function findNemo(array) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
    count += 1;
  }
  console.log(`O(${count})`)
}

findNemo(large); // O(n) ----> Linear Time
```

<img width="1266" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/4d49bd0d-69f6-4dc6-acb7-8eb1e194448b">

# Example 2:

```js
// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
  let a = 10; // O(1)
  a = 50 + 3; // O(1)

  for (let i = 0; i < input.length; i++) { // O(n)
    anotherFunction(); // O(n)
    let stranger = true; // O(n)
    a++; // O(n)
  }
  return a; // O(1)
}

function anotherFunction() {
  return 60 + 5;
}

console.log(funChallenge([1, 2, 3, 4, 5])) // O(3 + 4n) ---> O(n)
```

<img width="1316" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/f1e8e60b-548f-4d0d-aac2-1ec992d5a533">

# Example 3:

```js
// What is the Big O of the below function? (Hint, you may want to go line by line)
function anotherFunChallenge(input) {
  let a = 5; // O(1)
  let b = 10; // O(1)
  let c = 50; // O(1)
  for (let i = 0; i < input; i++) { // O(n)
    let x = i + 1; // O(n)
    let y = i + 2; // O(n)
    let z = i + 3; // O(n)
  }
  for (let j = 0; j < input; j++) { // O(n)
    let p = j * 2; // O(n)
    let q = j * 2; // O(n)
  }
  let whoAmI = "I don't know"; // O(1)
}

anotherFunChallenge([1, 2, 3, 4, 5]) // O(4 + 7n) ----> O(n)
```

# #END </details>

<details>
  <summary>4. O(1) - Constant Time </summary>

# O(1) - Constant Time

# Example 1:

```js
const boxes = [0, 1, 2, 3, 4, 5];

function logFirstTwoBoxes(boxes) {
  console.log(boxes[0]); // 0(1)
  console.log(boxes[1]); // 0(1)
}

logFirstTwoBoxes(boxes)  // O(1) ----> Constant Time
```

<img width="1316" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0b9d7f2d-d4d4-4934-8b75-40943d0951ac">

# #END </details>

<details>
  <summary>5. Rule Book for Simplifying Big O </summary>

# Rule Book for Simplifying Big O

- Rule 1: Worst Case - Big O always looks for the worse case scenerio.
- Rule 2: Remove Constants - Always drop the contants
- Rule 3: Different terms for inputs - Always keep loops for different Arrays as different O notations eg. O(n + a)
- Rule 4: Drop Non Dominants - Dominants are notations with higher occurence compared to its Big O counterpart.

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5d405b0e-80c7-4a0c-9581-3532258ed2a0">

# Cheat Sheet

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/310fc765-7f75-4f91-98a0-f4e1bab31bdf">
<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0925db37-c7e0-4553-a255-dc9bfe591871">

# #END </details>

<details>
  <summary>6. O(n^2) - Quadratic Time </summary>

# O(n^2) - Quadratic Time

# Example 1:

```js
//Log all pairs of array

const boxes = ['a', 'b', 'c', 'd', 'e'];
function logAllPairsOfArray(array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      console.log(array[i], array[j])
    }
  }
}

logAllPairsOfArray(boxes) // O(n * n) ----> O(n^2)
```

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/dd0d468a-62ca-4186-a9fd-de9392d2414b">

# Example 2:

```js
function printAllNumbersThenAllPairSums(numbers) {

  console.log('these are the numbers:'); // O(1)
  numbers.forEach(function(number) { // O(n)
    console.log(number);
  });

  console.log('and these are their sums:'); // O(1)
  numbers.forEach(function(firstNumber) { // O(n^2)
    numbers.forEach(function(secondNumber) {
      console.log(firstNumber + secondNumber);
    });
  });
}

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5]) // O(n^2 + n + 2) ---> O(n^2)
```

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e2cee019-165c-46f9-ae59-c7b88f458b7a">

# #END </details>

<details>
  <summary>7. O(n!) - Factorial Time </summary>

# O(n!) - Factorial Time

```java
void nFacRuntimeFunc(int n) {
  for(int i=0; i<n; i++) {
    nFacRuntimeFunc(n-1);
  }
}
```

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/84e47905-2477-450c-9d88-6ad0d06f12fc">

# #END </details>

<details>
  <summary>8. Space Complexity </summary>

# Space Complexity

# 3 Bigs in Coding

- Readable
- Memory (Space Complexity)
- Speed (Time Complexity)

# Heap vs Stack

- Heap: Where we store variables that we assign values to.
- Stack: Where we keep track of our function calls.

# What causes Space complexity?

- Variables
- Data Structures
- Function Call
- Allocations

# Example 1:

```js
function boooo(n) {
  for (let i = 0; i < n; i++) {
    console.log('booooo');
  }
}
//Time complexity - O(n)
//Space complexity - O(1)

function arrayOfHiNTimes(n) {
  var hiArray = [];
  for (let i = 0; i < n; i++) {
    hiArray[i] = 'hi';
  }
  return hiArray;
}
// Time complexity O(n)
// Space complexity O(n)

console.log(arrayOfHiNTimes(6))
```

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c74130a4-33f0-4700-a948-6da3d96466ad">

# #END </details>

<details>
  <summary>9. For vs ForEach vs For of </summary>

# For vs ForEach vs For of

```js
const nemo = ['nemo'];

const large = new Array(5).fill('nemo');

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('1-Found NEMO!');
    }
  }
}

const findNemo2 = array => {
  array.forEach(fish => {
    if (fish === 'nemo') {
      console.log('2-Found NEMO!');
    }
  })
}

const findNemo3 = array => {
  for (let fish of array) {
    if (fish === 'nemo') {
      console.log('3-Found NEMO!');
    }
  }
}

findNemo(large); // O(n) ----> Linear Time
findNemo2(large);
findNemo3(large);
```

<img width="1313" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/897a7adf-ba37-4384-836a-5223e28ef149">

# #END </details>

<details>
  <summary>10. For </summary>

# For

```js

```

```js

```


# #END </details>
