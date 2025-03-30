// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {
  getAuth,
  signInWithRedirect,
  signInWithPopup,
  GoogleAuthProvider,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
} from "firebase/auth";

import {
  getFirestore,
  doc,
  getDoc,
  setDoc,
  collection,
  writeBatch,
  query,
  getDocs,
} from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID,
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.REACT_APP_FIREBASE_APP_ID,
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);

// Google Provider Authentication
const googleProvider = new GoogleAuthProvider();

googleProvider.setCustomParameters({
  prompt: "select_account",
});

export const auth = getAuth();

//Sign in with Google Auth
export const signInWithGooglePopup = () =>
  signInWithPopup(auth, googleProvider);
export const signInWithGoogleRedirect = () =>
  signInWithRedirect(auth, googleProvider);

//Check if the user record (document) exists in Firebase
export const db = getFirestore();

//Create a new table/collection and add records (documents) to it
export const addCollectionAndDocuments = async (
  collectionKey,
  objectsToAdd,
  field = "title"
) => {
  const collectionRef = collection(db, collectionKey);
  const batch = writeBatch(db);

  objectsToAdd.forEach((object) => {
    const docRef = doc(collectionRef, object[field].toLowerCase());
    batch.set(docRef, object);
  });

  await batch.commit();
  console.log("done....");
};

//Get categories and documents from DB collection
export const getCategoriesAndDocuments = async () => {
  const collectionRef = collection(db, "categories");

  const q = query(collectionRef);
  const querySnapshot = await getDocs(q);

  // const categoryMap = querySnapshot.docs.reduce((acc, docSnapshot) => {
  //   const { title, items } = docSnapshot.data();
  //   acc[title.toLowerCase()] = items;
  //   return acc;
  // }, {});

  // return categoryMap;

  return querySnapshot.docs.map((docSnapshot) => docSnapshot.data());
};

//Create a new user record (document) in the "users" table/collection
export const createUserDocumentFromAuth = async (userAuth) => {
  if (!userAuth) {
    return;
  }

  // Get reference to user uid in the "users" table/collection
  const userDocRef = doc(db, "users", userAuth.uid);

  // get the user record (document) in the "users" table/collection
  const userSnapshot = await getDoc(userDocRef);

  if (!userSnapshot.exists()) {
    //create a new user record (document) in the "users" table/collection
    const { displayName, email } = userAuth;
    const createdAt = new Date();
    try {
      await setDoc(userDocRef, {
        displayName,
        email,
        createdAt,
      });
    } catch (error) {
      console.log("error creating the user", error.message);
    }
  } else {
    // console.log(userSnapshot);
  }
  return userDocRef;
};

//Create a new user record in Google Auth with Username and Password
export const createAuthUserWithEmailAndPassword = async (email, password) => {
  if (!email || !password) {
    return;
  }
  return await createUserWithEmailAndPassword(auth, email, password);
};

//Sign in with Username and Password
export const signInAuthUserWithEmailAndPassword = async (email, password) => {
  if (!email || !password) {
    return;
  }
  return await signInWithEmailAndPassword(auth, email, password);
};

//Sign out With Google Auth
export const signOutUser = async () => await signOut(auth);

//Auth Listener Event Handler
export const onAuthStateChangedListener = (callback) =>
  onAuthStateChanged(auth, callback);
