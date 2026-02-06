function App() {
  return (
    <div className="container">
      <div className="logo">P</div>

      <h1>PyPulsar</h1>
      <p className="tagline">Modern Python desktop framework</p>

      <div className="features">
        <div className="feature">
          <div className="feature-icon">⚡</div>
          <h3>Blazing Fast</h3>
          <p>pywebview + aiohttp</p>
        </div>
        <div className="feature">
          <div className="feature-icon">🔒</div>
          <h3>Secure by Default</h3>
          <p>Built-in ACL system</p>
        </div>
        <div className="feature">
          <div className="feature-icon">💻</div>
          <h3>Truly Native</h3>
          <p>No Electron overhead</p>
        </div>
      </div>

      <div className="cta">
        Start building by editing<br />
        <span className="code">web/src/App.jsx</span>
      </div>

      <div className="footer">
        Made with Python • <a href="https://github.com/dannyx-hub/pypulsar" target="_blank">github.com/dannyx-hub/pypulsar</a>
      </div>
    </div>
  );
}

export default App;
