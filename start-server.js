import WebStore from 'hyperdata-wstore'
import { config } from './server-config.js'

// Optionally override configuration
// process.env.PORT = '4500'
// process.env.STORAGE_DIR = './storage'
// process.env.AUTH_USERNAME = 'admin'
// process.env.AUTH_PASSWORD = 'password'

// Start the server
const server = WebStore.listen(config.port, config.host, () => {
  console.log(`WebStore server running at http://${config.host}:${config.port}`)
  console.log(`Storage directory: ${config.storageDir}`)
  console.log(`Authentication: ${config.auth.username}/${config.auth.password}`)
})

// export { server }
