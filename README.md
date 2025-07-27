# URL Follower

A full-stack web application that traces URL redirects. The backend is built with Flask and the frontend with React.

## Features

- **URL Tracing**: Enter any URL and see all the redirects it goes through
- **Beautiful UI**: Modern, responsive React interface with gradient backgrounds and smooth animations
- **Real-time Results**: See step-by-step redirect information with status codes
- **Error Handling**: Graceful error handling for invalid URLs and network issues

## Project Structure

```
URLFollower/
├── flask-app/          # Flask backend API
│   ├── app.py         # Main Flask application
│   ├── api/           # API modules
│   └── requirements.txt
├── src/               # React frontend
│   ├── App.js         # Main React component
│   ├── App.css        # Styling
│   └── index.js       # React entry point
├── public/            # Static files
├── package.json       # React dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js 14+
- npm or yarn

### Backend Setup (Flask)

1. Navigate to the flask-app directory:
   ```bash
   cd flask-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

The Flask API will be available at `http://localhost:5000`

### Frontend Setup (React)

1. Install React dependencies:
   ```bash
   npm install
   ```

2. Start the React development server:
   ```bash
   npm start
   ```

The React app will be available at `http://localhost:3000`

## API Usage

The Flask API accepts POST requests with JSON data:

```json
{
  "url": "https://example.com"
}
```

Response format:
```json
[
  {
    "OriginalURL": "https://example.com",
    "Redirect": true,
    "Status": 301,
    "RedirectLocation": "https://www.example.com"
  },
  {
    "OriginalURL": "https://www.example.com",
    "Redirect": false,
    "Status": 200
  }
]
```

## Features

### Frontend Features
- **Modern UI**: Beautiful gradient design with smooth animations
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Real-time Feedback**: Loading states and error handling
- **Keyboard Support**: Press Enter to trace URLs
- **Step-by-step Results**: Clear visualization of each redirect step

### Backend Features
- **URL Validation**: Proper URL format checking
- **Redirect Following**: Follows up to 10 redirects (configurable)
- **Error Handling**: Graceful handling of network errors and invalid URLs
- **User-Agent Spoofing**: Uses realistic browser headers
- **Status Code Support**: Handles all common redirect status codes (301, 302, 303, 307, 308)

## Development

### Running in Development Mode

1. Start the Flask backend:
   ```bash
   cd flask-app
   python app.py
   ```

2. In a new terminal, start the React frontend:
   ```bash
   npm start
   ```

The React app is configured with a proxy to forward API requests to the Flask backend at `http://localhost:5000`.

### Building for Production

1. Build the React app:
   ```bash
   npm run build
   ```

2. The built files will be in the `build/` directory, ready for deployment.

## Docker Support

The project includes Docker configuration for easy deployment:

```bash
docker-compose up
```

This will start both the Flask backend and nginx reverse proxy.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
