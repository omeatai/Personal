# REACT TYPESCRIPT TUTORIAL FOR BEGINNERS

## [COURSE](https://www.youtube.com/playlist?list=PLC3y8-rFHvwi1AXijGTKM0BKtHzVC-LSK)

+TYPESCRIPT BASICS

<details>
  <summary>1. Introduction </summary>

# Introduction

<img width="1179" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/ba683c95-ea70-4c26-aa73-7d3ca27a5f7d">

# Check node version

```tsbs
node -v
```

# Install Typescript Globally

```tsbs
npm install -g typescript
```

# Check Typescript Version

```tsbs
tsc -v
```

# Compile Tupescript File

```tsbs
tsc main
tsc main --watch
```

### TS/learnTS/main.ts:

```ts
export {};
let message: string = "Hello World";

console.log(message);
```

### TS/learnTS/main.js:

```ts
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var message = "Hello World";
console.log(message);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/fbd7c71f-d997-47e8-bf15-91bf08a733e6">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/de893ff0-4e1f-4cca-b0cc-aa13387020b6">

# #END </details>

<details>
  <summary>2. Typescript Type Declaration </summary>

# Typescript Type Declaration

### TS/learnTS/main.ts:

```ts
export {};

// Boolean, Number, String
let isBeginner: boolean = true;
let total: number = 0;
let name: string = "Vishwas ";

let sentence: string = "My name is ${name} I am a beginner in Typescript";

console.log(sentence);

// Null, Undefined
let n: null = null;
let u: undefined = undefined;

let isNew: boolean = null;
let myName: string = undefined;

// Array
let list1: number[] = [1, 2, 3];
let list2: Array<number> = [1, 2, 3];

//Tuple
let person1: [string, number] = ["Chris", 22];

//ENUM
enum Color {
  Red,
  Green,
  Blue,
  White = "#fff",
}

let c: Color = Color.Green;
let w: Color = Color.White;

console.log(c); // 1
console.log(w); // #fff

//Any
let randomValue: any = 10;

randomValue = true;
randomValue = "Vishwas";

//Unknown
let myVariable: unknown = 10;

let res = (myVariable as string).toString();
console.log(typeof res);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/37807416-3b7a-4fc3-a545-4239e11b3318">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/90e9527a-d9f5-4cfc-8bbc-b3c5aebdf046">

# #END </details>

<details>
  <summary>3. Typescript MultiType Union </summary>

# Typescript MultiType Union

### TS/learnTS/main.ts:

```ts
export {};

let multiType: number | boolean;

multiType = 20;
multiType = true;
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/2e390237-8d9f-4390-b8e8-cb5065ffeaea">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/85d1240f-8d6c-4491-8f6d-1c8bde4da7c0">

# #END </details>

<details>
  <summary>4. Typescript Functions </summary>

# Typescript Functions

### TS/learnTS/main.ts:

```ts
export {};

//Functions
function add(num1: number, num2: number): number {
  return num1 + num2;
}

add(5, 10);

//Functions with optional parameters
function add2(num1: number, num2?: number): number {
  if (num2) return num1 + num2;
  else return num1;
}

add2(5, 10);
add2(5);

//Functions with default parameters
function add3(num1: number, num2: number = 10): number {
  if (num2) return num1 + num2;
  else return num1;
}

add3(5, 10);
add3(5);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e32cce17-313e-4c2c-96cb-43155d5298c8">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/c1f3f3fc-0001-46c1-a3c9-96a0c99f9552">

# #END </details>

<details>
  <summary>5. Typescript Interfaces </summary>

# Typescript Interfaces

### TS/learnTS/main.ts:

```ts
export {};

function fullName(person: { firstName: string; lastName: string }) {
  console.log(`${person.firstName} ${person.lastName}`);
}

let p = {
  firstName: "Bruce",
  lastName: "Wayne",
};

fullName(p);

//Function Interfaces
interface Person {
  firstName: string;
  lastName?: string;
}

function fullName2(person: Person) {
  console.log(`${person.firstName} ${person.lastName}`);
}

let p2 = {
  firstName: "Bruce",
  lastName: "Wayne",
};

fullName2(p2);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/34bcb64b-f6e1-42e5-bbde-d8360d3bdbf3">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/0424a72d-3554-45f3-9fd9-6ed56bde3407">

# #END </details>

<details>
  <summary>6. Typescript Classes </summary>

# Typescript Classes

### TS/learnTS/main.ts:

```ts
export {};

//Classes
class Employee {
  public employeeName: string; // public | private | protected

  constructor(name: string) {
    this.employeeName = name;
  }

  greet() {
    console.log(`Good Morning ${this.employeeName}`);
  }
}

let emp1 = new Employee("Vishwas ");
console.log(emp1.employeeName);
emp1.greet();

class Manager extends Employee {
  constructor(managerName: string) {
    super(managerName);
  }
  delegateWork() {
    console.log(`Manager delegating tasks`);
  }
}

let m1 = new Manager("Bruce");
m1.delegateWork();
m1.greet();
console.log(m1.employeeName);
```

<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/e959f2a0-ea8d-4630-8fc4-df5ba691047b">
<img width="910" alt="image" src="https://github.com/omeatai/My-Tutorials/assets/32337103/5541cd0d-2dfa-4145-8518-64ab90c1f884">

# #END </details>

+TYPESCRIPT IN REACT

<details>
  <summary>7. Typescript In React - Introduction </summary>

# Typescript React Introduction

```ts

```

```ts

```

# #END </details>
