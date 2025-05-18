## Use as a library

Install the package using npm:

```bash
npm install hyperdata-wstore
```

1. Create a `.env` file in your project root with configuration:

```env
PORT=4500
STORAGE_DIR=./storage
AUTH_USERNAME=admin
AUTH_PASSWORD=password
```

2. Create a server file (e.g., `server.js`):


```javascript
import { app, config } from 'hyperdata-wstore'

// Optionally override configuration
// process.env.PORT = '4500'
// process.env.STORAGE_DIR = './storage'
// process.env.AUTH_USERNAME = 'admin'
// process.env.AUTH_PASSWORD = 'password'

// Start the server
const server = app.listen(config.port, config.host, () => {
    console.log(`WebStore server running at http://${config.host}:${config.port}`)
    console.log(`Storage directory: ${config.storageDir}`)
    console.log(`Authentication: ${config.auth.username}/${config.auth.password}`)
})

export { server }
```

3. Run your server:

```bash
node server.js
```

## Configuration

The WebStore server can be configured using environment variables. The package will automatically load a `.env` file from your project root directory.

Available configuration options:

```env
# Server configuration
PORT=4500         # Port to listen on
HOST=localhost    # Host to bind to

# Storage directory (relative to project root)
STORAGE_DIR=storage

# Authentication credentials
AUTH_USERNAME=admin
AUTH_PASSWORD=password

# Logging configuration
LOG_LEVEL=info    # loglevel severity: trace, debug, info, warn, error, silent

# Optional: Database configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=webstore
DB_USER=webstore
DB_PASSWORD=webstore
```

## CLI Usage

The package also provides a command-line interface:

```bash
# Start the server
hyperdata-wstore

# Start with custom configuration
PORT=4500 hyperdata-wstore
```
