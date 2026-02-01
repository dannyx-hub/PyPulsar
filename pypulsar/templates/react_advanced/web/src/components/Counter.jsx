import { useState } from 'react';
import { api } from '../utils/api';

function Counter({ appState }) {
  const [step, setStep] = useState(1);

  const handleUpdate = (action) => {
    api.call('update_counter', { action, step })
      .catch((err) => console.error('Update error:', err));
  };

  const handleReset = () => {
    api.call('reset_counter')
      .catch((err) => console.error('Reset error:', err));
  };

  return (
    <div>
      <h1>Counter</h1>
      <p>Count: {appState.counter}</p>
      <input 
        type="number" 
        value={step} 
        onChange={(e) => setStep(Number(e.target.value))} 
      />
      <button onClick={() => handleUpdate('increment')}>Increment</button>
      <button onClick={() => handleUpdate('decrement')}>Decrement</button>
      <button onClick={handleReset}>Reset</button>
    </div>
  );
}

export default Counter;