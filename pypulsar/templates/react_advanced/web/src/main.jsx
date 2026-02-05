import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';
import './index.css';

const waitForPyWebView = () => {
  return new Promise((resolve) => {
    if (window.pywebview && window.pywebview.ready) {
      resolve();
    } else {
      const interval = setInterval(() => {
        if (window.pywebview && window.pywebview.ready) {
          clearInterval(interval);
          resolve();
        }
      }, 100);
      // Timeout after 5 seconds to allow running in dev mode without pywebview
      setTimeout(() => {
        clearInterval(interval);
        resolve();
      }, 5000);
    }
  });
};

waitForPyWebView().then(() => {
  ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  );
});