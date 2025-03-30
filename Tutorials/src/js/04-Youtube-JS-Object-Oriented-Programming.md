# JAVASCRIPT OBJECT ORIENTED PROGRAMMING TUTORIAL - PEDROTECH

## [COURSE]()

<details>
  <summary>1. OOP - Constructor and Getters </summary>

# Constructor and getters

### main.js:

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  getName = () => {
    return this.name;
  };
  getAge = () => {
    return this.age;
  };
}

let Person1 = new Person("Pedro", 19);

console.log(Person1.getName());
```

### output:

```js
// Pedro
```

</details>

<details>
  <summary>2. OOP - Dependent Objects </summary>

# Dependent Objects

### main.js:

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  getName = () => {
    return this.name;
  };

  getAge = () => {
    return this.age;
  };
}

class House {
  constructor(address, price, residents) {
    this.address = address;
    this.price = price;
    this.residents = residents;
  }

  getAddress = () => {
    return this.address;
  };

  getPrice = () => {
    return this.price;
  };

  getResident = () => {
    return this.residents;
  };
}

let pedro = new Person("Pedro", 19);
let david = new Person("David", 21);

let house = new House("hopeville", 280000, [pedro, david]);

console.log(house.getResident());
```

### output:

```js
// [
//   Person {
//     getName: [Function: getName],
//     getAge: [Function: getAge],
//     name: 'Pedro',
//     age: 19
//   },
//   Person {
//     getName: [Function: getName],
//     getAge: [Function: getAge],
//     name: 'David',
//     age: 21
//   }
// ]
```

</details>

<details>
  <summary>3. OOP - Setters </summary>

# Setters

### main.js:

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  getName = () => {
    return this.name;
  };

  getAge = () => {
    return this.age;
  };
}

class House {
  constructor(address, price, residents) {
    this.address = address;
    this.price = price;
    this.residents = residents;
  }

  getAddress = () => {
    return this.address;
  };

  getPrice = () => {
    return this.price;
  };

  getResident = () => {
    return this.residents;
  };

  setResident = (resident) => {
    this.residents.push(resident);
  };
}

let pedro = new Person("Pedro", 19);
let david = new Person("David", 21);

let house = new House("hopeville", 280000, [pedro, david]);

let mike = new Person("Mike", 30);

house.setResident(mike);

console.log(house.getResident());
```

### output:

```js
// [
//   Person {
//     getName: [Function: getName],
//     getAge: [Function: getAge],
//     name: 'Pedro',
//     age: 19
//   },
//   Person {
//     getName: [Function: getName],
//     getAge: [Function: getAge],
//     name: 'David',
//     age: 21
//   },
//   Person {
//     getName: [Function: getName],
//     getAge: [Function: getAge],
//     name: 'Mike',
//     age: 30
//   }
// ]
```

</details>

<details>
  <summary>4. OOP - Inheritance (extends) </summary>

# Inheritance (extends)

### main.js:

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  getName = () => {
    return this.name;
  };

  getAge = () => {
    return this.age;
  };
}

class Programmer extends Person {
  constructor(name, age, company, salary, language) {
    super(name, age);
    this.company = company;
    this.salary = salary;
    this.language = language;
  }

  sayHi = () => {
    console.log(
      `Hello, my name is ${this.getName()}. I am a programmer! I work for ${
        this.company
      }.`
    );
  };
}

let programmer = new Programmer("Ben", 32, "Twitch", 10000000, "JavaScript");
programmer.sayHi();
```

### output:

```js
// Hello, my name is Ben. I am a programmer! I work for Twitch.
```

</details>
