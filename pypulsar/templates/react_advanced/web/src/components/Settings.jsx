import { useState } from 'react';
import { api } from '../utils/api';

function Settings({ appState, setAppState }) {
  const [theme, setTheme] = useState(appState.settings?.theme || 'light');
  const [language, setLanguage] = useState(appState.settings?.language || 'en');

  const handleSave = () => {
    api.call('save_settings', { theme, language })
      .then((data) => setAppState(prev => ({ ...prev, settings: data.settings })))
      .catch((err) => console.error('Save error:', err));
  };

  return (
    <div>
      <h1>Settings</h1>
      <label>
        Theme:
        <select value={theme} onChange={(e) => setTheme(e.target.value)}>
          <option value="light">Light</option>
          <option value="dark">Dark</option>
        </select>
      </label>
      <label>
        Language:
        <select value={language} onChange={(e) => setLanguage(e.target.value)}>
          <option value="en">English</option>
          <option value="pl">Polski</option>
        </select>
      </label>
      <button onClick={handleSave}>Save</button>
    </div>
  );
}

export default Settings;