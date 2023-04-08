import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDpyGIbJXOHc53qTMGdG9XS8tnFeREcxNY",
    authDomain: "anaglyph-letter-game.firebaseapp.com",
    projectId: "anaglyph-letter-game",
    storageBucket: "anaglyph-letter-game.appspot.com",
    messagingSenderId: "370658729206",
    appId: "1:370658729206:web:93a8b30502aaa30ab2a0d7",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);

export default app;
