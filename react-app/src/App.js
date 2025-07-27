import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleTraceUrl = async () => {
    if (!url.trim()) {
      setError('Please enter a URL');
      return;
    }

    setLoading(true);
    setError('');
    setResults(null);

    try {
      const response = await axios.post('/', { url: url.trim() });
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data || 'An error occurred while tracing the URL');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleTraceUrl();
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>URL Follower</h1>
        <p>Tool to chase those pesky redirects so I dont have to</p>
      </header>
      
      <main className="App-main">
        <div className="input-section">
          <div className="input-group">
            <input
              type="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Enter a URL to trace (e.g., https://example.com)"
              className="url-input"
              disabled={loading}
            />
            <button
              onClick={handleTraceUrl}
              disabled={loading || !url.trim()}
              className="trace-button"
            >
              {loading ? 'Tracing...' : 'Trace URL'}
            </button>
          </div>
          
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}
        </div>

        {results && (
          <div className="results-section">
            <h2>Trace Results</h2>
            <div className="results-container">
              {results.map((result, index) => (
                <div key={index} className="result-item">
                  <div className="result-header">
                    <span className="step-number">Step {index + 1}</span>
                    <span className={`status ${result.Redirect ? 'redirect' : 'final'}`}>
                      {result.Redirect ? 'Redirect' : 'Final Destination'}
                    </span>
                  </div>
                  
                  <div className="result-details">
                    <div className="url-info">
                      <strong>URL:</strong> {result.OriginalURL}
                    </div>
                    <div className="status-info">
                      <strong>Status:</strong> {result.Status}
                    </div>
                    {result.Redirect && result.RedirectLocation && (
                      <div className="redirect-info">
                        <strong>Redirects to:</strong> {result.RedirectLocation}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App; 