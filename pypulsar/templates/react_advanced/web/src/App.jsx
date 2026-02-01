import { useState, useEffect } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { api } from './utils/api';
import Home from './components/Home';
import Counter from './components/Counter';
import Settings from './components/Settings';
import Files from './components/Files';

function App() {
  const [appState, setAppState] = useState({});

  useEffect(() => {
    api.call('get_app_state')
      .then((data) => setAppState(data))
      .catch((err) => console.error('API error:', err));

    api.on('state_updated', (data) => {
      setAppState(prev => ({ ...prev, ...data }));
    });
  }, []);

  return (
    <div>
      <nav>
        <Link to="/">Home</Link> | 
        <Link to="/counter">Counter</Link> | 
        <Link to="/settings">Settings</Link> | 
        <Link to="/files">Files</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home appState={appState} />} />
        <Route path="/counter" element={<Counter appState={appState} />} />
        <Route path="/settings" element={<Settings appState={appState} setAppState={setAppState} />} />
        <Route path="/files" element={<Files />} />
      </Routes>
    </div>
  );
}

export default App;