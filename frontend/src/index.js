import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from "react-router-dom";
import { initializeApp } from "firebase/app";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCxwjbILiOqLY-iCaosYCxLxDa36kAhzNI",
  authDomain: "bc3409-react.firebaseapp.com",
  projectId: "bc3409-react",
  storageBucket: "bc3409-react.appspot.com",
  messagingSenderId: "565717303456",
  appId: "1:565717303456:web:6dfc9da7fe20d235c6c9c5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

ReactDOM.render(
      <BrowserRouter>
          <App />
      </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
