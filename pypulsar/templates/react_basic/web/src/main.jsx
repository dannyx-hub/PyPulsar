import React from 'react';
import ReactDOM from 'react-dom/client';
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
    }
  });
};

waitForPyWebView().then(() => {
  ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
});
