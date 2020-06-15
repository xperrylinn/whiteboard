const express = require('express');
const { inherits } = require('util');
const app = express();

app.use(express.json());

app.listen(3000, () => console.log('Listening on port 3000.'));

// Endpoints:
app.get('/hello', (req, res) => {
    console.log('Headers: ', req.headers);
    console.log('Method: ', req.method);
    res.send('Received GET request!\n');
});

app.post('/hello', (req, res) => {
    console.log('Headers: ', req.headers);
    console.log('Method: ', req.method);
    console.log('Body: ', req.body);
    res.send('Received POST request!\n');
});

// GET request example, using curl
// curl --header 'content-type: application/js' localhost:3000/hello --data '{"foo": "bar"}'
// POST example using curl
// curl --header 'content-type: application/js' localhost:3000/hello --data '{"foo": "bar"}'
// 
// npm init
// {
//     "name": "http_server",
//     "version": "1.0.0",
//     "description": "",
//     "main": "server.js",
//     "scripts": {
//       "test": "echo \"Error: no test specified\" && exit 1",
//       "start": "node server.js"
//     },
//     "author": "",
//     "license": "ISC"
//   }
 