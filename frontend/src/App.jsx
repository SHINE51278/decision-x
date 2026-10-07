import "./App.css";

function App() {
  return (
    <div className="app">
      <nav className="navbar">
        <div className="logo">
          <span className="logo-mark">D</span>
          <span>Decision-X</span>
        </div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#analyze">Analyze</a>
          <a href="#about">About</a>
        </div>
      </nav>

      <main>
        <section className="hero" id="home">
          <div className="hero-content">
            <p className="eyebrow">AI-POWERED DECISION SUPPORT</p>

            <h1>
              Make better
              <br />
              <span>decisions.</span>
            </h1>

            <p className="hero-text">
              Decision-X helps you analyze complex situations,
              compare options, and understand the factors behind
              important decisions.
            </p>

            <button
              className="primary-button"
              onClick={() =>
                document
                  .getElementById("analyze")
                  .scrollIntoView({ behavior: "smooth" })
              }
            >
              Start Analysis →
            </button>
          </div>

          <div className="hero-card">
            <div className="card-header">
              <span>DECISION ANALYSIS</span>
              <span className="status">● READY</span>
            </div>

            <div className="decision-preview">
              <div className="preview-line large"></div>
              <div className="preview-line"></div>
              <div className="preview-line"></div>

              <div className="score">
                <span>Decision Score</span>
                <strong>--</strong>
              </div>
            </div>
          </div>
        </section>

        <section className="analyze-section" id="analyze">
          <p className="eyebrow">ANALYSIS</p>

          <h2>What decision are you facing?</h2>

          <p className="section-text">
            Describe your situation and we'll analyze it using the
            Decision-X engine.
          </p>

          <textarea
            placeholder="Example: Should our team choose technology A or technology B for our project?"
          />

          <button
            className="primary-button"
            onClick={() =>
              alert("Backend analysis will be connected here.")
            }
          >
            Analyze Decision
          </button>
        </section>
      </main>

      <footer id="about">
        <p>© 2026 Decision-X</p>
        <p>AI-powered decision support platform</p>
      </footer>
    </div>
  );
}

export default App;