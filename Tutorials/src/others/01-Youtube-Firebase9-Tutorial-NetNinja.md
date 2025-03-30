# FIREBASE 9 TUTORIAL - NET NINJA

## [COURSE](https://www.youtube.com/playlist?list=PL4cUxeGkcC9jERUGvbudErNCeSZHWUVlb)

# FIREBASE

+INTRODUCTION

<details>
  <summary>1. Setting up Webpack</summary>

```bs
dist -> index.html
src -> index.js
```

Create package.json file:

```bs
npm init -y
```

Install webpack:

```bs
npm i webpack webpack-cli -D
npm i webpack webpack-cli webpack-dev-server html-webpack-plugin -D
```

watch.config.js:

```js
const path = require("path");

module.exports = {
  mode: "development",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  watch: true,
};
```

```js
const path = require("path");

module.exports = {
  mode: "development",
  entry: "./src/index.js",
  output: {
    path: path.join(__dirname, "dist"),
    filename: "bundle.js",
    sourceMapFilename: "bundle.js.map",
  },
  devtool: "source-map",
  watch: true,
};
```

package.json:

```bs
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
},
```

```js
{
  "name": "firebase-netninja",
  "version": "1.0.0",
  "description": "",
  "main": "webpack.config.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "webpack": "^5.75.0",
    "webpack-cli": "^5.0.0"
  }
}
```

Run Webpack:

```bs
npm run build
```

index.html:

```bs
<script src="bundle.js"></script>
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Firebase 9</title>
  </head>
  <body>
    <h1>Getting started with firebase 9</h1>
    <script src="bundle.js"></script>
  </body>
</html>
```

</details>

<details>
  <summary>86. Create Firebase Project</summary>

Install Firebase:

```bs
npm install firebase
```

index.js:

```js
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
```

</details>

<details>
  <summary>87. Connect Firebase App</summary>

index.js:

```js
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// get collection data
getDocs(colRef)
  .then((snapshot) => {
    // console.log(snapshot.docs)
    let books = [];
    snapshot.docs.forEach((doc) => {
      books.push({ ...doc.data(), id: doc.id });
    });
    console.log(books);
  })
  .catch((err) => {
    console.log(err.message);
  });
```

```js
// author: "patrick bamford"
// id: "5t16O84fjMNOU73F1pC5"
// title: "the fall of snowden"

// author: "gary nerds"
// id: "OKNxNdBC2ncnpa16SjDB"
// title: "the cloud"
```

</details>

<details>
  <summary>88. Adding and Deleting Documents</summary>

index.html:

```js
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Firebase 9</title>
</head>
<body>
  <h1>Getting Started with Firebase 9</h1>

  <h2>Firebase Firestore</h2>

  <form class="add">
    <label for="title">Title:</label>
    <input type="text" name="title" required>
    <label for="author">Author:</label>
    <input type="text" name="author" required>

    <button>add a new book</button>
  </form>

  <form class="delete">
    <label for="id">Document id:</label>
    <input type="text" name="id" required>

    <button>delete a book</button>
  </form>

  <script src="bundle.js"></script>
</body>
</html>
```

index.js:

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  getDocs,
  addDoc,
  deleteDoc,
  doc,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// get collection data
getDocs(colRef)
  .then((snapshot) => {
    // console.log(snapshot.docs)
    let books = [];
    snapshot.docs.forEach((doc) => {
      books.push({ ...doc.data(), id: doc.id });
    });
    console.log(books);
  })
  .catch((err) => {
    console.log(err.message);
  });

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});
```

</details>

<details>
  <summary>89. Real Time onSnapshot Listener </summary>

index.js:

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// realtime collection data
onSnapshot(colRef, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});
```

</details>

<details>
  <summary>90. Firebase Where Queries</summary>

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(colRef, where("author", "==", "Ashley Stampley"));

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});
```

</details>

<details>
  <summary>91. Ordering by Property</summary>

```bs
// queries
const q = query(colRef, where("author", "==", "dave ramsey"), orderBy("title", "asc"))
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("title", "asc")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});
```

</details>

<details>
  <summary>92. Ordering by Timestamps</summary>

```bs
// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});
```

</details>

<details>
  <summary>93. Fetching a Single Document</summary>

```bs
// fetching a single document (& realtime)
const docRef = doc(db, "books", "M3bROLjs0pyabVoNvUaK");

// getDoc(docRef)
//   .then(doc => {
//     console.log(doc.data(), doc.id)
//   })

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  getDoc,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "M3bROLjs0pyabVoNvUaK");

// getDoc(docRef)
//   .then(doc => {
//     console.log(doc.data(), doc.id)
//   })

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});
```

</details>

<details>
  <summary>94. Updating Documents</summary>

index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Firebase 9</title>
  </head>
  <body>
    <h1>Getting Started with Firebase 9</h1>

    <h2>Firebase Firestore</h2>

    <form class="add">
      <label for="title">Title:</label>
      <input type="text" name="title" required />
      <label for="author">Author:</label>
      <input type="text" name="author" required />

      <button>add a new book</button>
    </form>

    <form class="delete">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>delete a book</button>
    </form>

    <form class="update">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>update a book</button>
    </form>

    <script src="bundle.js"></script>
  </body>
</html>
```

index.js:

```bs
// updating a document
const updateForm = document.querySelector('.update')
updateForm.addEventListener('submit', (e) => {
  e.preventDefault()

  let docRef = doc(db, 'books', updateForm.id.value)

  updateDoc(docRef, {
    title: 'updated title'
  })
  .then(() => {
    updateForm.reset()
  })
})
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  getDoc,
  updateDoc,
} from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "M3bROLjs0pyabVoNvUaK");

// getDoc(docRef)
//   .then(doc => {
//     console.log(doc.data(), doc.id)
//   })

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});

// updating a document
const updateForm = document.querySelector(".update");
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let docRef = doc(db, "books", updateForm.id.value);

  updateDoc(docRef, {
    title: "updated title",
  }).then(() => {
    updateForm.reset();
  });
});
```

</details>

<details>
  <summary>95. Signing up Users</summary>

index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Firebase 9</title>
  </head>
  <body>
    <h1>Getting Started with Firebase 9</h1>

    <h2>Firebase Firestore</h2>

    <form class="add">
      <label for="title">Title:</label>
      <input type="text" name="title" required />
      <label for="author">Author:</label>
      <input type="text" name="author" required />

      <button>add a new book</button>
    </form>

    <form class="delete">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>delete a book</button>
    </form>

    <form class="update">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>update a book</button>
    </form>

    <h2>Firebase Auth</h2>

    <form class="signup">
      <label for="email">email:</label>
      <input type="email" name="email" />
      <label for="password">password:</label>
      <input type="password" name="password" />
      <button>signup</button>
    </form>

    <script src="bundle.js"></script>
  </body>
</html>
```

index.js:

```bs
import {
  getAuth,
  createUserWithEmailAndPassword,
} from 'firebase/auth'
```

```bs
// init db services
const db = getFirestore()
const auth = getAuth()
```

```bs
// signing users up
const signupForm = document.querySelector('.signup')
signupForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const email = signupForm.email.value
  const password = signupForm.password.value

  createUserWithEmailAndPassword(auth, email, password)
    .then(cred => {
      console.log('user created:', cred.user)
      signupForm.reset()
    })
    .catch(err => {
      console.log(err.message)
    })
})
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  getDoc,
  updateDoc,
} from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();
const auth = getAuth();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "gGu4P9x0ZHK9SspA1d9j");

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});

// updating a document
const updateForm = document.querySelector(".update");
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let docRef = doc(db, "books", updateForm.id.value);

  updateDoc(docRef, {
    title: "updated title",
  }).then(() => {
    updateForm.reset();
  });
});

// signing users up
const signupForm = document.querySelector(".signup");
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = signupForm.email.value;
  const password = signupForm.password.value;

  createUserWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user created:", cred.user);
      signupForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});
```

</details>

<details>
  <summary>96. Logging in and out </summary>

index.html:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Firebase 9</title>
  </head>
  <body>
    <h1>Getting Started with Firebase 9</h1>

    <h2>Firebase Firestore</h2>

    <form class="add">
      <label for="title">Title:</label>
      <input type="text" name="title" required />
      <label for="author">Author:</label>
      <input type="text" name="author" required />

      <button>add a new book</button>
    </form>

    <form class="delete">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>delete a book</button>
    </form>

    <form class="update">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>update a book</button>
    </form>

    <h2>Firebase Auth</h2>

    <form class="signup">
      <label for="email">email:</label>
      <input type="email" name="email" />
      <label for="password">password:</label>
      <input type="password" name="password" />
      <button>signup</button>
    </form>

    <form class="login">
      <label for="email">email:</label>
      <input type="email" name="email" />
      <label for="password">password:</label>
      <input type="password" name="password" />
      <button>login</button>
    </form>

    <button class="logout">logout</button>

    <script src="bundle.js"></script>
  </body>
</html>
```

index.js:

```bs
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword, signOut
} from 'firebase/auth'
```

```bs
// logging in and out
const logoutButton = document.querySelector('.logout')
logoutButton.addEventListener('click', () => {
  signOut(auth)
    .then(() => {
      console.log('user signed out')
    })
    .catch(err => {
      console.log(err.message)
    })
})

const loginForm = document.querySelector('.login')
loginForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const email = loginForm.email.value
  const password = loginForm.password.value

  signInWithEmailAndPassword(auth, email, password)
    .then(cred => {
      console.log('user logged in:', cred.user)
      loginForm.reset()
    })
    .catch(err => {
      console.log(err.message)
    })
})
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  updateDoc,
} from "firebase/firestore";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
} from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDmXgb_58lO7aK_ujN37pGlNxzWGEU0YpI",
  authDomain: "fb9-sandbox.firebaseapp.com",
  projectId: "fb9-sandbox",
  storageBucket: "fb9-sandbox.appspot.com",
  messagingSenderId: "867529587246",
  appId: "1:867529587246:web:dc754ab7840c737f47bdbf",
};

// init firebase
initializeApp(firebaseConfig);

// init services
const db = getFirestore();
const auth = getAuth();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "patrick rothfuss"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "gGu4P9x0ZHK9SspA1d9j");

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});

// updating a document
const updateForm = document.querySelector(".update");
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let docRef = doc(db, "books", updateForm.id.value);

  updateDoc(docRef, {
    title: "updated title",
  }).then(() => {
    updateForm.reset();
  });
});

// signing users up
const signupForm = document.querySelector(".signup");
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = signupForm.email.value;
  const password = signupForm.password.value;

  createUserWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user created:", cred.user);
      signupForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});

// logging in and out
const logoutButton = document.querySelector(".logout");
logoutButton.addEventListener("click", () => {
  signOut(auth)
    .then(() => {
      console.log("user signed out");
    })
    .catch((err) => {
      console.log(err.message);
    });
});

const loginForm = document.querySelector(".login");
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = loginForm.email.value;
  const password = loginForm.password.value;

  signInWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user logged in:", cred.user);
      loginForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});
```

</details>

<details>
  <summary>97. Subscribing to Auth Changes</summary>

index.js:

```bs
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword, signOut, onAuthStateChanged
} from 'firebase/auth'
```

```bs
// subscribing to auth changes
onAuthStateChanged(auth, (user) => {
  console.log('user status changed:', user)
})
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  getDoc,
  updateDoc,
} from "firebase/firestore";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
} from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAkkJyg-3xzVITPx6FU3wDaRKR4OGpmzSs",
  authDomain: "fir-9-ninja-30222.firebaseapp.com",
  projectId: "fir-9-ninja-30222",
  storageBucket: "fir-9-ninja-30222.appspot.com",
  messagingSenderId: "700813053129",
  appId: "1:700813053129:web:165552244a3a57a0775118",
};

// Initialize Firebase App
initializeApp(firebaseConfig);

// init db services
const db = getFirestore();
const auth = getAuth();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "dave ramsey"),
  orderBy("createdAt")
);

// realtime collection data
onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "gGu4P9x0ZHK9SspA1d9j");

onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});

// updating a document
const updateForm = document.querySelector(".update");
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let docRef = doc(db, "books", updateForm.id.value);

  updateDoc(docRef, {
    title: "updated title",
  }).then(() => {
    updateForm.reset();
  });
});

// signing users up
const signupForm = document.querySelector(".signup");
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = signupForm.email.value;
  const password = signupForm.password.value;

  createUserWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user created:", cred.user);
      signupForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});

// logging in and out
const logoutButton = document.querySelector(".logout");
logoutButton.addEventListener("click", () => {
  signOut(auth)
    .then(() => {
      console.log("user signed out");
    })
    .catch((err) => {
      console.log(err.message);
    });
});

const loginForm = document.querySelector(".login");
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = loginForm.email.value;
  const password = loginForm.password.value;

  signInWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user logged in:", cred.user);
      loginForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});

// subscribing to auth changes
onAuthStateChanged(auth, (user) => {
  console.log("user status changed:", user);
});
```

</details>

<details>
  <summary>98. Unsubscribing from Changes</summary>

index.html:

```bs
  <button class="unsub">unsubscribe from db/auth changes</button>
```

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Firebase 9</title>
  </head>
  <body>
    <h1>Getting Started with Firebase 9</h1>

    <h2>Firebase Firestore</h2>

    <form class="add">
      <label for="title">Title:</label>
      <input type="text" name="title" required />
      <label for="author">Author:</label>
      <input type="text" name="author" required />

      <button>add a new book</button>
    </form>

    <form class="delete">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>delete a book</button>
    </form>

    <form class="update">
      <label for="id">Document id:</label>
      <input type="text" name="id" required />

      <button>update a book</button>
    </form>

    <h2>Firebase Auth</h2>

    <form class="signup">
      <label for="email">email:</label>
      <input type="email" name="email" />
      <label for="password">password:</label>
      <input type="password" name="password" />
      <button>signup</button>
    </form>

    <form class="login">
      <label for="email">email:</label>
      <input type="email" name="email" />
      <label for="password">password:</label>
      <input type="password" name="password" />
      <button>login</button>
    </form>

    <button class="logout">logout</button>

    <h2>Unsubscribing</h2>
    <button class="unsub">unsubscribe from db/auth changes</button>

    <script src="bundle.js"></script>
  </body>
</html>
```

index.js:

```bs
// realtime collection data
const unsubCol = onSnapshot(q, (snapshot) => {
  let books = []
  snapshot.docs.forEach(doc => {
    books.push({ ...doc.data(), id: doc.id })
  })
  console.log(books)
})

// fetching a single document (& realtime)
const docRef = doc(db, 'books', 'gGu4P9x0ZHK9SspA1d9j')

const unsubDoc = onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id)
})

// subscribing to auth changes
const unsubAuth = onAuthStateChanged(auth, (user) => {
  console.log('user status changed:', user)
})

// unsubscribing from changes (auth & db)
const unsubButton = document.querySelector('.unsub')
unsubButton.addEventListener('click', () => {
  console.log('unsubscribing')
  unsubCol()
  unsubDoc()
  unsubAuth()
})
```

```js
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  onSnapshot,
  addDoc,
  deleteDoc,
  doc,
  query,
  where,
  orderBy,
  serverTimestamp,
  updateDoc,
} from "firebase/firestore";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
} from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDmXgb_58lO7aK_ujN37pGlNxzWGEU0YpI",
  authDomain: "fb9-sandbox.firebaseapp.com",
  projectId: "fb9-sandbox",
  storageBucket: "fb9-sandbox.appspot.com",
  messagingSenderId: "867529587246",
  appId: "1:867529587246:web:dc754ab7840c737f47bdbf",
};

// init firebase
initializeApp(firebaseConfig);

// init services
const db = getFirestore();
const auth = getAuth();

// collection ref
const colRef = collection(db, "books");

// queries
const q = query(
  colRef,
  where("author", "==", "patrick rothfuss"),
  orderBy("createdAt")
);

// realtime collection data
const unsubCol = onSnapshot(q, (snapshot) => {
  let books = [];
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id });
  });
  console.log(books);
});

// adding docs
const addBookForm = document.querySelector(".add");
addBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp(),
  }).then(() => {
    addBookForm.reset();
  });
});

// deleting docs
const deleteBookForm = document.querySelector(".delete");
deleteBookForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const docRef = doc(db, "books", deleteBookForm.id.value);

  deleteDoc(docRef).then(() => {
    deleteBookForm.reset();
  });
});

// fetching a single document (& realtime)
const docRef = doc(db, "books", "gGu4P9x0ZHK9SspA1d9j");

const unsubDoc = onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id);
});

// updating a document
const updateForm = document.querySelector(".update");
updateForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let docRef = doc(db, "books", updateForm.id.value);

  updateDoc(docRef, {
    title: "updated title",
  }).then(() => {
    updateForm.reset();
  });
});

// signing users up
const signupForm = document.querySelector(".signup");
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = signupForm.email.value;
  const password = signupForm.password.value;

  createUserWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user created:", cred.user);
      signupForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});

// logging in and out
const logoutButton = document.querySelector(".logout");
logoutButton.addEventListener("click", () => {
  signOut(auth)
    .then(() => {
      console.log("user signed out");
    })
    .catch((err) => {
      console.log(err.message);
    });
});

const loginForm = document.querySelector(".login");
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = loginForm.email.value;
  const password = loginForm.password.value;

  signInWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      console.log("user logged in:", cred.user);
      loginForm.reset();
    })
    .catch((err) => {
      console.log(err.message);
    });
});

// subscribing to auth changes
const unsubAuth = onAuthStateChanged(auth, (user) => {
  console.log("user status changed:", user);
});

// unsubscribing from changes (auth & db)
const unsubButton = document.querySelector(".unsub");
unsubButton.addEventListener("click", () => {
  console.log("unsubscribing");
  unsubCol();
  unsubDoc();
  unsubAuth();
});
```

</details>

# #END