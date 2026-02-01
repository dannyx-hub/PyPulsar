function Home({ appState }) {
  return (
    <div>
      <h1>Welcome to Advanced PyPulsar React App</h1>
      <p>Current counter: {appState.counter}</p>
      <p>Theme: {appState.settings?.theme}</p>
    </div>
  );
}

export default Home;