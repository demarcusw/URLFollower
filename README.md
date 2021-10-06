[![Test](https://github.com/demarcusw/URLFollower/actions/workflows/python-test.yml/badge.svg)](https://github.com/demarcusw/URLFollower/actions/workflows/python-test.yml)
# URLFollower
Tool to chase those pesky redirects so I dont have to. Mostly to see where spam redirects go 😛

## Installation
The app is dockerized so all you need is docker installed. To run the app, run the following docker-compose command:

* `docker-compose up --build`

This will stand up an NGINX frontend (listening on port 8080) which forwards requests to the uWSGI backend which is running the Flask app (listening on port 5000)

## Usage
To use, simply make a POST request to the root index, `/`. See sample request and response below:

### Request
```http
POST / HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 41

{
    "url": "https://bit.ly/3DgboPq"
}
```

### Response
```json
[
    {
        "OriginalURL": "https://bit.ly/3DgboPq",
        "Redirect": true,
        "RedirectLocation": "https://www.youtube.com/",
        "Status": 301
    },
    {
        "OriginalURL": "https://www.youtube.com/",
        "Redirect": false,
        "Status": 200
    }
]
```

Feel free to parse the JSON output w/ something like `jq`!
