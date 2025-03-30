# UDEMY-COMPLETE NODE DEVELOPER IN 2023 - ZTM

## [COURSE](https://www.udemy.com/course/complete-nodejs-developer-zero-to-mastery/)

<details>
  <summary>1. Introduction </summary>

# Install Node

```jsbs
https://nodejs.org/en/download
```

# Node Version

```js
node -v
node --version
```

### output:

```js
// v18.15.0
```

# Node REPL

```jsbs
node
```

### output:

```js
// MacBook-Air ~ % node
// Welcome to Node.js v18.15.0.
// Type ".help" for more information.
// > const cheer = "woo" + "hoo"
// undefined
// > cheer
// 'woohoo'
// > Boolean(0)
// false
// > 11 > 2
// true
```

# Node say Hello

### index.js:

```js
function sayHello() {
  return "Hello";
}

console.log(sayHello());
```

### run:

```jsbs
node index.js
```

### output:

```js
// nodejs % node index.js
//
// Hello
```

</details>

<details>
  <summary>2. Node with variables </summary>

# Node with variables

### index.js:

```js
const mission = "learn";

if (mission === "learn") {
  console.log("Time to write some Node code!");
} else {
  console.log(`Is ${mission} really more fun?`);
}
```

### run:

```jsbs
node index.js
```

### output:

```js
// nodejs % node index.js
//
// Time to write some Node code!
```

</details>

<details>
  <summary>3. Node process.argv </summary>

# process.argv

### index.js:

```js
const fpath = process.argv[1];
const firstValue = process.argv[2];
const secondValue = process.argv[3];

console.log("File Path:", fpath);
console.log("First Value:", firstValue);
console.log("Second Value:", secondValue);
```

### run:

```jsbs
node index Ifeanyi Omeata
```

### output:

```js
// MacBook-Air nodejs % node index Ifeanyi Omeata
// File Path: /Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/nodejs/index
// First Value: Ifeanyi
// Second Value: Omeata
```

</details>

<details>
  <summary>4. Callback Function (setTimeout) </summary>

# setTimeout

### race.js:

```js
setTimeout(() => {
  console.log("🐰 finishes");
}, 3000);
console.log("🐌 finishes");
```

### run:

```jsbs
node event.js
```

### output:

```js
// MacBook-Air nodejs % node race.js
// 🐌 finishes
// 🐰 finishes
```

</details>

<details>
  <summary>5. Event Emmitter Module 1 </summary>

# Event Emmitter Module 1

### event.js:

```js
const { EventEmitter } = require("events");

class Celebrity extends EventEmitter {}

const celebrity = new Celebrity();

// Subscribe to Celebrity Events for Observer 1
celebrity.on("race win", () => {
  console.log("Congratulations! You are the best!");
});

// Subscribe to Celebrity Events for Observer 2
celebrity.on("race win", () => {
  console.log("Boo I could have better than that!");
});

celebrity.emit("race win");
```

### run:

```jsbs
node event.js
```

### output:

```js
// MacBook-Air nodejs % node events
// Congratulations! You are the best!
// Boo I could have better than that!
```

</details>

<details>
  <summary>6. Event Emmitter Module 2 (with process)</summary>

# Event Emmitter Module 2

### event.js:

```js
const { EventEmitter } = require("events");

const celebrity = new EventEmitter();

// Subscribe to Celebrity Events for Observer 1
celebrity.on("race", (result) => {
  if (result === "win") {
    console.log("Congratulations! You are the best!");
  } else if (result === "lost") {
    console.log("Better luck next time!");
  }
});

// Subscribe to Celebrity Events for Observer 2
celebrity.on("race", (result) => {
  if (result === "win") {
    console.log("Boo I could have better than that!");
  }
});

process.on("exit", (code) => {
  console.log("Process exit event with code:", code);
});

celebrity.emit("race", "win");
celebrity.emit("race", "lost");
```

### run:

```jsbs
node event.js
```

### output:

```js
// Congratulations! You are the best!
// Boo I could have better than that!
// Better luck next time!
// Process exit event with code: 0
```

</details>

<details>
  <summary>7. Http Request Module </summary>

# Http Request Module

### main.js:

```js
const { request } = require("http");

const req = request("http://www.google.com", (res) => {
  res.on("data", (chunk) => {
    console.log(`Data Chunk: ${chunk}`);
  });
  res.on("end", () => {
    console.log("No more data");
  });
});

req.end();
```

### run:

```jsbs
node main
```

### output:

```js
// Data Chunk: <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-NG"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="_LLqGpC53VUupR6uO1wtAw">(function(){window.google={kEI:'fApZZN7cG4jd1sQP5bqioAM',kEXPI:'0,1359409,6058,207,4804,2316,383,246,5,1129120,1197790,611,198,379891,16115,28684,22431,1361,283,12035,2817,1929,12835,4998,13228,3847,3599,34845,887,1985,2891,4139,4209,3406,606,60690,15756,3,576,1014,1,16916,2642,4,1538,2304,42126,13659,4437,16786,5821,2536,4094,7596,1,39042,2,3110,2,14022,2715,21266,1758,5679,1021,31121,4568,6259,23418,1252,5835,14968,4332,16,7468,445,2,2,1,26632,8155,7381,2,15967,873,19634,7,1922,9779,20639,15515,6305,20199,20136,14,82,20206,4070,4307,18960,280,5123,2265,765,5628,483,2460,2580,4665,1804,7734,2738,2885,7654,12086,2171,5253,3534,44,2969,14,1252,380,3244,2563,2,2142,4471,2567,8018,514,98,666,4,922,224,1267,749,2608,3050,164,412,140,129,1710,2504,326,1,217,405,444,2,301,728,916,169,1235,1294,39,170,175,795,404,110,419,272,350,227,1094,2542,232,464,640,3,317,2,44,214,383,567,791,351,372,434,589,182,2,14,535,120,1878,230,174,5206236,262,5994420,2799834,4589,3311,141,795,19735,1,1,346,5093,2,45,1,453,44,56,47,23944744,577,2772317,1269248,1964,16673,2893,6250,14712,1028,2781,1349,1395547,15379,146986,57883,23554406,677,85,94,133,47,826,116,413,100,595,975,82,345,178,243,249,2,212,2,157,1375,8,34,167,362,1,1152,1247,583,410,487,197,9,124,469,286,412,120,241,218,461,560,722,14,550,818,313,31,537,240,10,604,253,99,962,523,1759,6',kBL:'Xw_a',kOPI:89978449};google.sn='webhp';google.kHL='en-NG';})();(function(){
// var h=this||self;function l(){return void 0!==window.google&&void 0!==window.google.kOPI&&0!==window.google.kOPI?window.google.kOPI:null};var m,n=[];function p(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||m}function q(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}function r(a){/^http:/i.test(a)&&"https:"===window.location.protocol&&(google.ml&&google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a}
```

</details>

<details>
  <summary>8. Http Get Module </summary>

# Http Get Module

### main.js:

```js
const { request, get } = require("http");

const req = get("http://www.google.com", (res) => {
  res.on("data", (chunk) => {
    console.log(`Data Chunk: ${chunk}`);
  });
  res.on("end", () => {
    console.log("No more data");
  });
});

// req.end();
```

### run:

```jsbs
node main
```

### output:

```js
// Data Chunk: <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-NG"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="_LLqGpC53VUupR6uO1wtAw">(function(){window.google={kEI:'fApZZN7cG4jd1sQP5bqioAM',kEXPI:'0,1359409,6058,207,4804,2316,383,246,5,1129120,1197790,611,198,379891,16115,28684,22431,1361,283,12035,2817,1929,12835,4998,13228,3847,3599,34845,887,1985,2891,4139,4209,3406,606,60690,15756,3,576,1014,1,16916,2642,4,1538,2304,42126,13659,4437,16786,5821,2536,4094,7596,1,39042,2,3110,2,14022,2715,21266,1758,5679,1021,31121,4568,6259,23418,1252,5835,14968,4332,16,7468,445,2,2,1,26632,8155,7381,2,15967,873,19634,7,1922,9779,20639,15515,6305,20199,20136,14,82,20206,4070,4307,18960,280,5123,2265,765,5628,483,2460,2580,4665,1804,7734,2738,2885,7654,12086,2171,5253,3534,44,2969,14,1252,380,3244,2563,2,2142,4471,2567,8018,514,98,666,4,922,224,1267,749,2608,3050,164,412,140,129,1710,2504,326,1,217,405,444,2,301,728,916,169,1235,1294,39,170,175,795,404,110,419,272,350,227,1094,2542,232,464,640,3,317,2,44,214,383,567,791,351,372,434,589,182,2,14,535,120,1878,230,174,5206236,262,5994420,2799834,4589,3311,141,795,19735,1,1,346,5093,2,45,1,453,44,56,47,23944744,577,2772317,1269248,1964,16673,2893,6250,14712,1028,2781,1349,1395547,15379,146986,57883,23554406,677,85,94,133,47,826,116,413,100,595,975,82,345,178,243,249,2,212,2,157,1375,8,34,167,362,1,1152,1247,583,410,487,197,9,124,469,286,412,120,241,218,461,560,722,14,550,818,313,31,537,240,10,604,253,99,962,523,1759,6',kBL:'Xw_a',kOPI:89978449};google.sn='webhp';google.kHL='en-NG';})();(function(){
// var h=this||self;function l(){return void 0!==window.google&&void 0!==window.google.kOPI&&0!==window.google.kOPI?window.google.kOPI:null};var m,n=[];function p(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||m}function q(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}function r(a){/^http:/i.test(a)&&"https:"===window.location.protocol&&(google.ml&&google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a}
```

</details>

<details>
  <summary>9. Simulating a request Module </summary>

# Simulating a request Module

### https.js:

```js
const { send } = require("./request");
const { read } = require("./response");

function request(url, data) {
  send(url, data);
  return read();
}

const res = request("http://www.google.com", "This is a Google test request.");
console.log(res);
```

### request.js:

```js
function encrypt(data) {
  return "encrypted data";
}

function send(url, data) {
  const encryptedData = encrypt(data);
  console.log(`sending ${encryptedData} to ${url}`);
}

module.exports = {
  send,
};
```

### response.js:

```js
function decrypt(data) {
  return "decrypted data";
}

function read() {
  return decrypt("data");
}

module.exports = {
  read,
};
```

### run:

```jsbs
node https
```

### output:

```js
// MacBook-Air nodejs % node https
// sending encrypted data to http://www.google.com
// decrypted data
```

</details>

<details>
  <summary>10. ECMAScript Modules (mjs) </summary>

# ECMAScript Modules (mjs)

### https.mjs:

```js
import { send } from "./request.mjs";
import { read } from "./response.mjs";

function request(url, data) {
  send(url, data);
  return read();
}

const res = request("http://www.google.com", "This is a Google test request.");
console.log(res);
```

### request.mjs:

```js
function encrypt(data) {
  return "encrypted data";
}

function send(url, data) {
  const encryptedData = encrypt(data);
  console.log(`sending ${encryptedData} to ${url}`);
}

// module.exports = {
//   send,
// };

export { send };
```

### response.mjs:

```js
function decrypt(data) {
  return "decrypted data";
}

function read() {
  return decrypt("data");
}

// module.exports = {
//   read,
// };

export { read };
```

### run:

```jsbs
node https.mjs
```

### output.mjs:

```js
// MacBook-Air nodejs % node https.mjs
// sending encrypted data to http://www.google.com
// decrypted data
```

</details>

<details>
  <summary>11. Exporting files with index.js </summary>

# Exporting files with index.js

### https.js:

```js
const { request, response } = require("./modules");

function requestData(url, data) {
  request.send(url, data);
  return response.read();
}

const res = requestData(
  "http://www.google.com",
  "This is a Google test request."
);
console.log(res);
```

### modules/index.js:

```js
module.exports = {
  request: require("./request"),
  response: require("./response"),
};
```

### modules/request.js:

```js
function encrypt(data) {
  return "encrypted data";
}

function send(url, data) {
  const encryptedData = encrypt(data);
  console.log(`sending ${encryptedData} to ${url}`);
}

module.exports = {
  send,
};
```

### modules/response.js:

```js
function decrypt(data) {
  return "decrypted data";
}

function read() {
  return decrypt("data");
}

module.exports = {
  read,
};
```

### run:

```jsbs
node https.js
```

### output:

```js
// MacBook-Air nodejs % node https.js
// sending encrypted data to http://www.google.com
// decrypted data
```

![](https://user-images.githubusercontent.com/32337103/236944500-01cde6c5-0a9b-4bb8-a0db-c1cb8e060cfc.png)

</details>

+NPM

<details>
  <summary>12. npm - axios module </summary>

# Initialize npm (node package manager)

```jsbs
npm init
npm init -y
```

# Install axios

```jsbs
npm install axios
```

### https.js:

```js
const { request, response } = require("./myModules");

function requestData(url, data) {
  request.send(url, data);
  return response.read();
}

const res = requestData(
  "http://www.google.com",
  "This is a Google test request."
);
// console.log(res);
console.log("Ready to Rumble!");
```

### package.json:

```js
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "",
  "main": "https.js",
  "scripts": {
    "start": "node https.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "axios": "^1.4.0"
  }
}

```

### run:

```jsbs
npm run start
```

### output:

```js
// MacBook-Air nodejs % npm run start

// > nodejs@1.0.0 start
// > node https.js

// sending encrypted data to http://www.google.com
// Ready to Rumble!
```

</details>

<details>
  <summary>13. npm - axios.get </summary>

# axios.get

### main.js:

```js
const axios = require("axios");

axios.get("https://www.google.com").then((response) => {
  console.log(response);
});
```

### run:

```jsbs
node main
```

### output:

```js
// MacBook-Air nodejs % node main
// {
//   status: 200,
//   statusText: 'OK',
//   headers: AxiosHeaders {
//     date: 'Tue, 09 May 2023 07:25:29 GMT',
//     expires: '-1',
//     'cache-control': 'private, max-age=0',
//     'content-type': 'text/html; charset=ISO-8859-1',
//     'content-security-policy-report-only': "object-src 'none';base-uri 'self';script-src 'nonce-YWLEAOtGbL9vn4B_XJvFaQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp",
//     p3p: 'CP="This is not a P3P policy! See g.co/p3phelp for more info."',
//     server: 'gws',
//     'x-xss-protection': '0',
//     'x-frame-options': 'SAMEORIGIN',
//     'set-cookie': [
//       '1P_JAR=2023-05-09-07; expires=Thu, 08-Jun-2023 07:25:29 GMT; path=/; domain=.google.com; Secure',
//       'AEC=AUEFqZdCAgSk9clXrVEZhET-OOIsqJfWDYOED0T-3d3UqvGs9IUcJyojZfA; expires=Sun, 05-Nov-2023 07:25:29 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax',
//       'NID=511=uTwfSwfEqNALn0uFwlDtK4yXsROpGkRn5w9gTQHTCpnz_uSSBkSJsU3BNKerjwnff0fBblfMPNvNDYz6T7yPb7gX5tS4Iz1HdZjZ6ET7_Yz4PyXG4tfuJKZ75VGCplYlw-6ej7-fXq5Gx4gHX-qmPlk95m3ynf_sso7fapeydhM; expires=Wed, 08-Nov-2023 07:25:29 GMT; path=/; domain=.google.com; HttpOnly'
//     ],
//     'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
//     connection: 'close',
//     'transfer-encoding': 'chunked'
//   },
//   config: {
//     transitional: {
//       silentJSONParsing: true,
//       forcedJSONParsing: true,
//       clarifyTimeoutError: false
//     },
//     adapter: [ 'xhr', 'http' ],
//     transformRequest: [ [Function: transformRequest] ],
//     transformResponse: [ [Function: transformResponse] ],
//     timeout: 0,
//     xsrfCookieName: 'XSRF-TOKEN',
//     xsrfHeaderName: 'X-XSRF-TOKEN',
//     maxContentLength: -1,
//     maxBodyLength: -1,
//     env: { FormData: [Function], Blob: [class Blob] },
//     validateStatus: [Function: validateStatus],
//     headers: AxiosHeaders {
//       Accept: 'application/json, text/plain, */*',
//       'User-Agent': 'axios/1.4.0',
//       'Accept-Encoding': 'gzip, compress, deflate, br'
//     },
//     method: 'get',
//     url: 'https://www.google.com',
//     data: undefined
//   },
```

</details>

<details>
  <summary>14. npm - axios.get with catch errors </summary>

# axios.get with catch errors

### main.js:

```js
const axios = require("axios");

axios
  .get("https://wwwwww.google.com")
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.log(err);
  });
```

### run:

```jsbs
node main.js
```

### output:

```js
// MacBook-Air nodejs % node main
// AxiosError: getaddrinfo ENOTFOUND wwwwww.google.com
//     at AxiosError.from (/Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/nodejs/node_modules/axios/dist/node/axios.cjs:836:14)
//     at RedirectableRequest.handleRequestError (/Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/nodejs/node_modules/axios/dist/node/axios.cjs:3010:25)
//     at RedirectableRequest.emit (node:events:513:28)
//     at eventHandlers.<computed> (/Users/ifeanyiomeata/Desktop/SERVER/Cloud/CODE/nodejs/node_modules/follow-redirects/index.js:14:24)
//     at ClientRequest.emit (node:events:513:28)
//     at TLSSocket.socketErrorListener (node:_http_client:502:9)
//     at TLSSocket.emit (node:events:513:28)
//     at emitErrorNT (node:internal/streams/destroy:151:8)
//     at emitErrorCloseNT (node:internal/streams/destroy:116:3)
//     at process.processTicksAndRejections (node:internal/process/task_queues:82:21) {
//   hostname: 'wwwwww.google.com',
//   syscall: 'getaddrinfo',
//   code: 'ENOTFOUND',
//   errno: -3008,
//   config: {
//     transitional: {
//       silentJSONParsing: true,
//       forcedJSONParsing: true,
//       clarifyTimeoutError: false
//     },
//     adapter: [ 'xhr', 'http' ],
//     transformRequest: [ [Function: transformRequest] ],
//     transformResponse: [ [Function: transformResponse] ],
//     timeout: 0,
//     xsrfCookieName: 'XSRF-TOKEN',
//     xsrfHeaderName: 'X-XSRF-TOKEN',
//     maxContentLength: -1,
//     maxBodyLength: -1,
//     env: { FormData: [Function], Blob: [class Blob] },
//     validateStatus: [Function: validateStatus],
//     headers: AxiosHeaders {
//       Accept: 'application/json, text/plain, */*',
//       'User-Agent': 'axios/1.4.0',
//       'Accept-Encoding': 'gzip, compress, deflate, br'
//     },
//     method: 'get',
//     url: 'https://wwwwww.google.com',
//     data: undefined
//   },
//   request: <ref *1> Writable {
//     _writableState: WritableState {
//       objectMode: false,
//       highWaterMark: 16384,
//       finalCalled: false,
//       needDrain: false,
//       ending: false,
//       ended: false,
//       finished: false,
//       destroyed: false,
//       decodeStrings: true,
//       defaultEncoding: 'utf8',
//       length: 0,
//       writing: false,
//       corked: 0,
//       sync: true,
//       bufferProcessing: false,
//       onwrite: [Function: bound onwrite],
//       writecb: null,
//       writelen: 0,
//       afterWriteTickInfo: null,
//       buffered: [],
//       bufferedIndex: 0,
//       allBuffers: true,
//       allNoop: true,
//       pendingcb: 0,
//       constructed: true,
//       prefinished: false,
//       errorEmitted: false,
//       emitClose: true,
//       autoDestroy: true,
//       errored: null,
//       closed: false,
//       closeEmitted: false,
//       [Symbol(kOnFinished)]: []
//     },
//     _events: [Object: null prototype] {
//       response: [Function: handleResponse],
//       error: [Function: handleRequestError],
//       socket: [Function: handleRequestSocket]
//     },
//     _eventsCount: 3,
//     _maxListeners: undefined,
//     _options: {
//       maxRedirects: 21,
//       maxBodyLength: Infinity,
//       protocol: 'https:',
//       path: '/',
//       method: 'GET',
//       headers: [Object: null prototype],
//       agents: [Object],
//       auth: undefined,
//       family: undefined,
//       lookup: undefined,
//       beforeRedirect: [Function: dispatchBeforeRedirect],
//       beforeRedirects: [Object],
//       hostname: 'wwwwww.google.com',
//       port: '',
//       agent: undefined,
//       nativeProtocols: [Object],
//       pathname: '/'
//     },
//     _ended: true,
//     _ending: true,
//     _redirectCount: 0,
//     _redirects: [],
//     _requestBodyLength: 0,
//     _requestBodyBuffers: [],
//     _onNativeResponse: [Function (anonymous)],
//     _currentRequest: ClientRequest {
//       _events: [Object: null prototype],
//       _eventsCount: 7,
//       _maxListeners: undefined,
//       outputData: [],
//       outputSize: 0,
//       writable: true,
//       destroyed: false,
//       _last: true,
//       chunkedEncoding: false,
//       shouldKeepAlive: false,
//       maxRequestsOnConnectionReached: false,
//       _defaultKeepAlive: true,
//       useChunkedEncodingByDefault: false,
//       sendDate: false,
//       _removedConnection: false,
//       _removedContLen: false,
//       _removedTE: false,
//       strictContentLength: false,
//       _contentLength: 0,
//       _hasBody: true,
//       _trailer: '',
//       finished: true,
//       _headerSent: true,
//       _closed: false,
//       socket: [TLSSocket],
//       _header: 'GET / HTTP/1.1\r\n' +
//         'Accept: application/json, text/plain, */*\r\n' +
//         'User-Agent: axios/1.4.0\r\n' +
//         'Accept-Encoding: gzip, compress, deflate, br\r\n' +
//         'Host: wwwwww.google.com\r\n' +
//         'Connection: close\r\n' +
//         '\r\n',
//       _keepAliveTimeout: 0,
//       _onPendingData: [Function: nop],
//       agent: [Agent],
//       socketPath: undefined,
//       method: 'GET',
//       maxHeaderSize: undefined,
//       insecureHTTPParser: undefined,
//       joinDuplicateHeaders: undefined,
//       path: '/',
//       _ended: false,
//       res: null,
//       aborted: false,
//       timeoutCb: null,
//       upgradeOrConnect: false,
//       parser: null,
//       maxHeadersCount: null,
//       reusedSocket: false,
//       host: 'wwwwww.google.com',
//       protocol: 'https:',
//       _redirectable: [Circular *1],
//       [Symbol(kCapture)]: false,
//       [Symbol(kBytesWritten)]: 0,
//       [Symbol(kEndCalled)]: true,
//       [Symbol(kNeedDrain)]: false,
//       [Symbol(corked)]: 0,
//       [Symbol(kOutHeaders)]: [Object: null prototype],
//       [Symbol(errored)]: null,
//       [Symbol(kUniqueHeaders)]: null
//     },
//     _currentUrl: 'https://wwwwww.google.com/',
//     [Symbol(kCapture)]: false
//   },
//   cause: Error: getaddrinfo ENOTFOUND wwwwww.google.com
//       at GetAddrInfoReqWrap.onlookup [as oncomplete] (node:dns:107:26) {
//     errno: -3008,
//     code: 'ENOTFOUND',
//     syscall: 'getaddrinfo',
//     hostname: 'wwwwww.google.com'
//   }
// }
```

</details>

<details>
  <summary>15. npm - axios.get with final then </summary>

# axios.get with final then

### main.js:

```js
const axios = require("axios");

axios
  .get("https://wwwwww.google.com")
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.log(err);
  })
  .then(() => {
    console.log("All done!");
  });
```

### run:

```jsbs
node main.js
```

### output:

```js
//       [Symbol(kNeedDrain)]: false,
//       [Symbol(corked)]: 0,
//       [Symbol(kOutHeaders)]: [Object: null prototype],
//       [Symbol(errored)]: null,
//       [Symbol(kUniqueHeaders)]: null
//     },
//     _currentUrl: 'https://wwwwww.google.com/',
//     [Symbol(kCapture)]: false
//   },
//   cause: Error: getaddrinfo ENOTFOUND wwwwww.google.com
//       at GetAddrInfoReqWrap.onlookup [as oncomplete] (node:dns:107:26) {
//     errno: -3008,
//     code: 'ENOTFOUND',
//     syscall: 'getaddrinfo',
//     hostname: 'wwwwww.google.com'
//   }
// }
// All done!
```

</details>

<details>
  <summary>16. npm - nodemon </summary>

# Install nodemon Locally

```jsbs
npm install nodemon
```

# Install nodemon Globally

```jsbs
npm install -g nodemon
```

# Setup nodemon in package.json

### package.json:

```js
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "start": "node main.js",
    "dev": "nodemon main.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "axios": "^1.4.0",
    "nodemon": "^2.0.22"
  }
}

```

# with nodemon

### main.js:

```js
const axios = require("axios");

axios
  .get("https://www.wikipedia.com")
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.log(err);
  })
  .then(() => {
    console.log("All done!");
  });
```

### run:

```jsbs
npm run dev
```

### output:

```js
// e{height:auto}}.central-featured{position:relative;height:325px;height:32.5rem;width:546px;width:54.6rem;max-width:100%;margin:0 auto;text-align:center;vertical-align:middle}.central-featured-lang{position:absolute;width:156px;width:15.6rem}.central-featured-lang .link-box{display:block;padding:0;text-decoration:none;white-space:normal}.central-featured-lang .link-box:hover strong{text-decoration:underline}.central-featured-lang :hover{background-color:#eaecf0}.central-feature'... 63722 more characters
// }
// All done!
// [nodemon] clean exit - waiting for changes before restart
```

</details>

+KEPLER PROJECT

<details>
  <summary>17. Kepler project - Introduction </summary>

# Initialize the npm project

```jsbs
npm init
```

# Install nodemon

```jsbs
npm install nodemon
```

### kepler-project/package.json:

```js
{
  "name": "kepler-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "csv-parse": "^5.3.10",
    "nodemon": "^2.0.22"
  }
}

```

### kepler-project/index.js:

```js
console.log("Hello world!");
```

### run:

```jsbs
npm run dev
```

### output:

```js
// MacBook-Air kepler-project % npm run dev

// > kepler-project@1.0.0 dev
// > nodemon index.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node index.js`
// Hello world!
// [nodemon] clean exit - waiting for changes before restart
```

</details>

<details>
  <summary>18. Kepler project - Reading Unparsed Data </summary>

# Install CSV Parser

```jsbs
npm install csv-parse
```

### kepler-project/index.js:

```js
const { parse } = require("csv-parse");
const fs = require("fs");

const results = [];

fs.createReadStream("kepler_data.csv")
  .on("data", (data) => {
    results.push(data);
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    console.log(results);
    console.log("done");
  });
```

### output:

```js
// [
//     <Buffer 31 2c 32 31 37 2e 30 2c 2c 2c 30 2e 35 32 2c 30 2e 36 30 2c 2d 30 2e 31 32 2c 31 31 2e 35 30 2c 31 2c 71 31 5f 71 31 37 5f 64 72 32 34 5f 74 63 65 2c ... 65486 more bytes>,
//   <Buffer 2e 30 30 2c 32 2e 37 35 39 2c 30 2e 31 32 38 2c 2d 30 2e 31 37 36 2c 36 2e 34 34 37 30 2c 31 2e 37 38 31 30 2c 2d 30 2e 38 32 32 30 2c 32 39 31 2e 39 ... 65486 more bytes>,
//   <Buffer 2e 30 30 2c 34 2e 34 34 36 2c 30 2e 30 35 36 2c 2d 30 2e 32 31 30 2c 31 2e 30 34 35 30 2c 30 2e 33 34 31 30 2c 2d 30 2e 31 31 34 30 2c 32 38 38 2e 37 ... 65486 more bytes>,
//   <Buffer 34 2c 4b 30 38 31 36 36 2e 30 31 2c 2c 46 41 4c 53 45 20 50 4f 53 49 54 49 56 45 2c 46 41 4c 53 45 20 50 4f 53 49 54 49 56 45 2c 30 2e 30 30 30 30 2c ... 45940 more bytes>
// ]
// done
// [nodemon] clean exit - waiting for changes before restart
```

</details>

<details>
  <summary>19. Kepler project - Parsing Data </summary>

# Parsing Data

### kepler-project/index.js:

```js
const { parse } = require("csv-parse");
const fs = require("fs");

const results = [];

fs.createReadStream("kepler_data.csv")
  .pipe(
    parse({
      comment: "#",
      columns: true,
    })
  )
  .on("data", (data) => {
    results.push(data);
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    console.log(results);
    console.log("done");
  });
```

### run:

```jsbs
node index
```

### output:

```js
//   },
//   {
//     kepid: '3832474',
//     kepoi_name: 'K00806.03',
//     kepler_name: 'Kepler-30 b',
//     koi_disposition: 'CONFIRMED',
//     koi_pdisposition: 'CANDIDATE',
//     koi_score: '',
//     koi_fpflag_nt: '0',
//     koi_fpflag_ss: '0',
//     koi_fpflag_co: '0',
//     koi_fpflag_ec: '0',
//     koi_period: '29.159861500',
//     koi_period_err1: '2.5340000e-04',
//     koi_period_err2: '-2.5340000e-04',
//     koi_time0bk: '150.6992200',
//     koi_time0bk_err1: '7.180000e-03',
//     koi_time0bk_err2: '-7.180000e-03',
//     koi_impact: '0.3619',
//     koi_impact_err1: '0.0945',
//     koi_impact_err2: '-0.3618',
//     koi_duration: '4.80300',
//     koi_duration_err1: '0.20000',
//     koi_duration_err2: '-0.20000',
//     koi_depth: '4.8800e+02',
//     koi_depth_err1: '4.350e+01',
//     koi_depth_err2: '-4.350e+01',
//     koi_prad: '1.91',
//     koi_prad_err1: '2.000e-01',
//     koi_prad_err2: '-7.000e-02',
//     koi_teq: '524.0',
//     koi_teq_err1: '',
//     koi_teq_err2: '',
//     koi_insol: '17.85',
//     koi_insol_err1: '5.61',
//     koi_insol_err2: '-2.68',
//     koi_model_snr: '11.60',
//     koi_tce_plnt_num: '',
//     koi_tce_delivname: '',
//     koi_steff: '5485.00',
//     koi_steff_err1: '99.00',
//     koi_steff_err2: '-112.00',
//     koi_slogg: '4.556',
//     koi_slogg_err1: '0.014',
//     koi_slogg_err2: '-0.094',
//     koi_srad: '0.8670',
//     koi_srad_err1: '0.0920',
//     koi_srad_err2: '-0.0340',
//     ra: '285.283630',
//     dec: '38.947281',
//     koi_kepmag: '15.403'
//   },
//   ... 9464 more items
// ]
// done
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/87cb2ee0-b4f4-4a81-a3a6-d49acca1f62d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/4fd301f4-effe-4b87-8db9-eb66e439480a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/913ec3f4-81b0-4e06-b3e5-60dcabc6ada4)

</details>

<details>
  <summary>20. Kepler project - Searching Data </summary>

# Searching Data

### kepler-project/index.js:

```js
const { parse } = require("csv-parse");
const fs = require("fs");

const results = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

fs.createReadStream("kepler_data.csv")
  .pipe(
    parse({
      comment: "#",
      columns: true,
    })
  )
  .on("data", (data) => {
    if (isHabitablePlanet(data)) {
      results.push(data);
    }
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    console.log(results);
    console.log(`Done. ${results.length} habitable planets found.`);
  });
```

### run:

```jsbs
node index.js
```

### output:

```js
//   },
//   {
//     kepid: '8311864',
//     kepoi_name: 'K07016.01',
//     kepler_name: 'Kepler-452 b',
//     koi_disposition: 'CONFIRMED',
//     koi_pdisposition: 'CANDIDATE',
//     koi_score: '0.7710',
//     koi_fpflag_nt: '0',
//     koi_fpflag_ss: '0',
//     koi_fpflag_co: '0',
//     koi_fpflag_ec: '0',
//     koi_period: '384.847556000',
//     koi_period_err1: '7.1050000e-03',
//     koi_period_err2: '-7.1050000e-03',
//     koi_time0bk: '314.9700000',
//     koi_time0bk_err1: '1.520000e-02',
//     koi_time0bk_err2: '-1.520000e-02',
//     koi_impact: '0.0590',
//     koi_impact_err1: '0.3870',
//     koi_impact_err2: '-0.0590',
//     koi_duration: '9.96900',
//     koi_duration_err1: '0.44100',
//     koi_duration_err2: '-0.44100',
//     koi_depth: '1.8990e+02',
//     koi_depth_err1: '1.760e+01',
//     koi_depth_err2: '-1.760e+01',
//     koi_prad: '1.09',
//     koi_prad_err1: '2.000e-01',
//     koi_prad_err2: '-1.000e-01',
//     koi_teq: '220.0',
//     koi_teq_err1: '',
//     koi_teq_err2: '',
//     koi_insol: '0.56',
//     koi_insol_err1: '0.32',
//     koi_insol_err2: '-0.15',
//     koi_model_snr: '12.30',
//     koi_tce_plnt_num: '1',
//     koi_tce_delivname: 'q1_q17_dr25_tce',
//     koi_steff: '5579.00',
//     koi_steff_err1: '150.00',
//     koi_steff_err2: '-150.00',
//     koi_slogg: '4.580',
//     koi_slogg_err1: '0.034',
//     koi_slogg_err2: '-0.127',
//     koi_srad: '0.7980',
//     koi_srad_err1: '0.1500',
//     koi_srad_err2: '-0.0750',
//     ra: '296.003690',
//     dec: '44.277561',
//     koi_kepmag: '13.426'
//   }
// ]
// Done. 8 habitable planets found.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c8e537ca-1b0a-443e-8188-977fe622225d)

</details>

<details>
  <summary>21. Kepler project - Mapping Data </summary>

# Mapping Data

### kepler-project/index.js:

```js
const { parse } = require("csv-parse");
const fs = require("fs");

const habitablePlanets = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

fs.createReadStream("kepler_data.csv")
  .pipe(
    parse({
      comment: "#",
      columns: true,
    })
  )
  .on("data", (data) => {
    if (isHabitablePlanet(data)) {
      habitablePlanets.push(data);
    }
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    console.log(
      habitablePlanets.map((planets) => {
        return {
          id: planets["kepid"],
          name: planets["kepler_name"],
        };
      })
    );
    console.log(`Done. ${habitablePlanets.length} habitable planets found.`);
  });
```

### run:

```jsbs
node index.js
```

### output:

```js
// MacBook-Air kepler-project % node index
// [
//   { id: '11768142', name: 'Kepler-1652 b' },
//   { id: '3642335', name: 'Kepler-1410 b' },
//   { id: '11497958', name: 'Kepler-296 A f' },
//   { id: '4138008', name: 'Kepler-442 b' },
//   { id: '11497958', name: 'Kepler-296 A e' },
//   { id: '6444896', name: 'Kepler-1649 b' },
//   { id: '9002278', name: 'Kepler-62 f' },
//   { id: '8311864', name: 'Kepler-452 b' }
// ]
// Done. 8 habitable planets found.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/979c9157-d947-4c05-a110-8220de7cd30c)

</details>

+NODE SERVERS

<details>
  <summary>22. Node Servers - HTTP REQUEST Methods </summary>

# HTTP REQUEST Methods

```jsbs
//GET
-> GET/friends

//GET(DETAILS)
-> GET/friends/5

//POST
-> POST/messages

//PUT
-> PUT/messages/15

//DELETE
-> DELETE /messages/15
```

```jsbs
GET
The GET method requests a representation of the specified resource.
Requests using GET should only retrieve data.

HEAD
The HEAD method asks for a response identical to a GET request, but without the response body.

POST
The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

PUT
The PUT method replaces all current representations of the target resource with the request payload.

DELETE
The DELETE method deletes the specified resource.

CONNECT
The CONNECT method establishes a tunnel to the server identified by the target resource.

OPTIONS
The OPTIONS method describes the communication options for the target resource.

TRACE
The TRACE method performs a message loop-back test along the path to the target resource.

PATCH
The PATCH method applies partial modifications to a resource.
```

# HTTP REQUEST PARTS

```jsbs
METHOD -> POST
PATH -> /messages
BODY -> { text: "hello", photo: "smile.jpg"}
HEADERS -> Host: facebook.com
```

</details>

<details>
  <summary>23. Node Servers - HTTP RESPONSE </summary>

# HTTP RESPONSE PARTS

```jsbs
HEADERS -> Content-Type: application/json
BODY -> { text: "hi!", photo: "wave.jpg"}
STATUS CODE -> 200
```

</details>

<details>
  <summary>24. Node Servers - HTTP RESPONSE status codes </summary>

# HTTP response status codes

```jsbs
1. Informational responses (100–199)
2. Successful responses (200-299)
3. Redirects (300-399)
4. Client errors (400-499)
5. Server errors (500-599)
```

### 1. Informational responses (100–199)

```jsbs
100 - Continue
This interim response indicates that everything so far is OK and that the client should
continue the request, or ignore the response if the request is already finished.

101 - Switching Protocol
This code is sent in response to an Upgrade request header from the client, and
indicates the protocol the server is switching to.

102 - Processing (WebDAV)
This code indicates that the server has received and is processing the request, but no
response is available yet.
```

### 2. Successful responses (200-299)

```jsbs
200 - OK
The request has succeeded.
The meaning of the success depends on the HTTP method:
• GET: The resource has been fetched and is transmitted in the message body.
• HEAD: The entity headers are in the message body.
• PUT or POST: The resource describing the result of the action is transmitted in the message body.
• TRACE: The message body contains the request message as received by the server.

201 - Created
The request has succeeded and a new resource has been created as a result. This is
typically the response sent after POST requests, or some PUT requests.

202 - Accepted
The request has been eceived but not yet acted upon.
It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating
the outcome of the request. It is intended for cases where another process or server handles the request,
or for batch processing.

203 - Non-Authoritative Information
This response code means the returned meta-information is not exactly the same as is
available from the origin server, but is collected from a local or a third-party copy.
```

### 3. Redirects (300-399)

```jsbs
300 - Multiple Choice
The request has more than one possible response.
The user-agent or user should choose one of them.
(There is no standardized way of choosing one of the responses but HTML links to the
possibilities are recommended so the user can pick.)

301 - Moved Permanently
The URL of the requested resource has been changed permanently.
The new URL is given in the response.

302 - Found
This response code means that the URI of requested resource has been changed temporarily.
Further changes in the URI might be made in the future.

303 - See Other
The server sent this response to direct the client to get the requested resource at another URI with a GET request.

304 - Not Modified
This is used for caching purposes.
It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.
```

### 4. Client errors (400-499)

```jsbs
400 - Bad Request
The server could not understand the request due to invalid syntax.

401 - Unauthorized (unauthenticated)
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated".
That is, the client must authenticate itself to get the requested response.

402 - Payment Required
This response code is reserved for future use. The initial aim for creating this code was
using it for digital payment systems, however this status code is used very rarely and
no standard convention exists.

403 - Forbidden (unauthorized)
The client does not have access rights to the content; that is, it is unauthorized,
so the server is refusing to give the requested resource.
Unlike 401, the client's identity is known to the server.

404 - Not Found
The server can not find the requested resource.
In the browser, this means the URL is not recognized.
In an API, this can also mean that the endpoint is valid but the resource itself does not exist.
Servers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client.
This response code is probably the most famous one due to its frequent occurrence on the web.

405 - Method Not Allowed
The request method is known by the server but has been disabled and cannot be used.
For example, an API may forbid DELETE-ing a resource.
The two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.

406 - Not Acceptable
This response is sent when the web server, after performing server-driven content
negotiation, doesn't find any content that conforms to the criteria given by the user agent.

407 - Proxy Authentication Required
This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.

408 - Request Timeout
This response is sent on an idle connection by some servers, even without any previous request by the client.
It means that the server would like to shut down this unused connection.
This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing.
Also note that some servers merely shut down the connection without sending this message.

409 - Conflict
This response is sent when a request conflicts with the current state of the server.

410 - Gone
This response is sent when the requested content has been permanently deleted from server, with no forwarding address.
```

### 5. Server errors (500-599)

```jsbs
500 - Internal Server Error
The server has encountered a situation it does not know how to handle.

501 - Not Implemented
The request method is not supported by the server and cannot be handled.
The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.

502 - Bad Gateway
This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.

503 - Service Unavailable
The server is not ready to handle the request.
Common causes are a server that is down for maintenance or that is overloaded.
Note that together with this response, a user-friendly page explaining the problem should be sent.
This response should be used for temporary conditions and the Retry-After HTTP header should, if possible,
contain the estimated time before the recovery of the service.
The webmaster must also take care about the caching-related headers that are sent along with this response,
as these temporary condition responses should usually not be cached.

504 - Gateway Timeout
This error response is given when the server is acting as a gateway and cannot get a response in time.

505 - HTTP Version Not Supported
The HTTP version used in the request is not supported by the server.
```

</details>

<details>
  <summary>25. Node Servers - HTTP RESPONSE Headers Example </summary>

# HTTP response Headers Example

### General

```jsbs
Request URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
Request Method: GET
Status Code: 304
Remote Address: 34.111.97.67:443
Referrer Policy: strict-origin-when-cross-origin
```

### Response Headers

```jsbs
age: 24079
alt-svc: clear
cache-control: public, max-age=86400
date: Thu, 11 May 2023 00:50:05 GMT
etag: W/"084bfcc5adf2381d0e887bc50c0751a2"
expires: Fri, 12 May 2023 00:49:03 GMT
vary: Accept-Encoding
x-cache: hit
```

### Request Headers

```jsbs
:authority: developer.mozilla.org
:method: GET
:path: /en-US/docs/Web/HTTP/Status
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8
cache-control: max-age=0
cookie: _ga=GA1.2.637822769.1683616202; _gid=GA1.2.848816132.1683741254
if-modified-since: Wed, 10 May 2023 19:04:58 GMT
if-none-match: W/"084bfcc5adf2381d0e887bc50c0751a2"
referer: https://www.udemy.com/
sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?1
sec-ch-ua-platform: "Android"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0)
```

</details>

+HTTP WEBSERVER

<details>
  <summary>26. HTTP Webserver - Sending Text to Client </summary>

# Sending Text to Client

### kepler-project/index.js:

```js
const http = require("http");

const PORT = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/plain",
  });
  res.end("Hello, I have been sent this message!");
});

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
//127.0.0.1 => localhost
```

### run:

```jsbs
node index.js
```

### output:

```js
// MacBook-Air kepler-project % node index
// Listening on port 3000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/82ce5872-a788-41a0-9279-564be370c7a0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/4f08551d-3a98-4adf-af3e-0c1b326259cf)

</details>

<details>
  <summary>27. HTTP Webserver - Sending JSON Data to Client </summary>

# Sending JSON Data to Client

### kepler-project/index.js:

```js
const http = require("http");

const PORT = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Type": "application/json",
  });
  res.end(JSON.stringify({ id: 2, firstname: "Ifeanyi", lastname: "Omeata" }));
});

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
//127.0.0.1 => localhost
```

### run:

```jsbs
node index.js
```

### output:

```js
// MacBook-Air kepler-project % node index
// Listening on port 3000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/ff4a398a-6ce9-4bbc-81f0-8ffc7d01fc93)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/9c662dec-5929-4ccc-bbf7-2f034ec96087)

</details>

<details>
  <summary>28. HTTP Webserver - Sending multiple Data based on Routes </summary>

# Sending multiple Data based on Routes

### kepler-project/index.js:

```js
const http = require("http");
const PORT = 3000;

const server = http.createServer((req, res) => {
  if (req.url === "/friends") {
    // res.writeHead(200, {
    //   "Content-Type": "application/json",
    // });
    res.statusCode = 200;
    res.setHeader("Content-Type", "application/json");
    res.end(
      JSON.stringify([
        { id: 1, firstname: "James", lastname: "Corby" },
        { id: 2, firstname: "Ifeanyi", lastname: "Omeata" },
        { id: 3, firstname: "Bob", lastname: "Richy" },
      ])
    );
  } else if (req.url === "/fruits") {
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    res.write("<html>");
    res.write("<head>");
    res.write("<title>My Fruits</title>");
    res.write("</head>");
    res.write("<body>");
    res.write("<h1>My Favorite Fruits</h1>");
    res.write("</h2>This is the list of my favorites fruits.</h2>");
    res.write("<ul>");
    res.write("<li>Apples</li>");
    res.write("<li>Bananas</li>");
    res.write("<li>Mangoes</li>");
    res.write("<li>Oranges</li>");
    res.write("</ul>");
    res.write("</body>");
    res.write("</html>");
    res.end();
  } else {
    res.statusCode = 404;
    res.end();
  }
});

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
//127.0.0.1 => localhost
```

### run Nodemon:

```jsbs
npm run dev
```

### output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node index.js`
// Listening on port 3000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b302c5d8-616b-4de6-8c86-f32592454032)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/352f1617-b932-4d3a-bd83-817b8cc75466)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/250bc0f1-a579-44f2-b86f-13308abeb45f)

</details>

<details>
  <summary>29. HTTP Webserver - Query Data from URL Params </summary>

# Query Data from URL Params

### kepler-project/index.js:

```js
const http = require("http");
const PORT = 3000;

const FRIENDS = [
  { id: 1, firstname: "James", lastname: "Corby" },
  { id: 2, firstname: "Ifeanyi", lastname: "Omeata" },
  { id: 3, firstname: "Bob", lastname: "Richy" },
];

const error404 = (req, res) => {
  res.statusCode = 404;
  res.setHeader("Content-Type", "text/html");
  res.write("<html>");
  res.write("<head>");
  res.write("<title>No Query Found</title>");
  res.write("</head>");
  res.write("<body>");
  res.write("<h1>No Query Found!</h1>");
  res.write("</body>");
  res.write("</html>");
  res.end();
};

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  const URL = req.url.split("/");
  const numOfURLParams = URL.length;
  const searchQuery = URL[1];
  if (searchQuery === "friends") {
    if (numOfURLParams === 2) {
      //show all friends in JSON format
      res.end(JSON.stringify(FRIENDS));
    } else if (numOfURLParams === 3) {
      const numOfFriends = FRIENDS.length;
      const searchId = URL[2];
      const searchIdIndex = Number(searchId) - 1; // +searchId - 1;
      if (searchId > 0 && searchId <= numOfFriends) {
        //show friend with ID searchId
        res.end(JSON.stringify(FRIENDS[searchIdIndex]));
      } else {
        error404(req, res);
      }
    } else {
      error404(req, res);
    }
  } else if (searchQuery === "fruits") {
    res.setHeader("Content-Type", "text/html");
    res.write("<html>");
    res.write("<head>");
    res.write("<title>My Fruits</title>");
    res.write("</head>");
    res.write("<body>");
    res.write("<h1>My Favorite Fruits</h1>");
    res.write("</h2>This is the list of my favorites fruits.</h2>");
    res.write("<ul>");
    res.write("<li>Apples</li>");
    res.write("<li>Bananas</li>");
    res.write("<li>Mangoes</li>");
    res.write("<li>Oranges</li>");
    res.write("</ul>");
    res.write("</body>");
    res.write("</html>");
    res.end();
  } else {
    res.statusCode = 404;
    res.end();
  }
});

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
```

### run:

```jsbs
npm run dev
```

### output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node index.js`
// Listening on port 3000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/79c9e9d3-fef6-4955-866f-2b35524bebe0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f62b55a4-bdb5-4eb4-b822-980519ddac23)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/7b11b67a-dfd8-4095-8fee-c50ce631d379)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/ea81a47d-2bb6-4074-927f-b7163f2ca93f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/23b2598b-fa67-43b0-a0c3-dd48de517cfc)

</details>

<details>
  <summary>30. HTTP Webserver - POST Data with req.method </summary>

# POST Data with req.method

### kepler-project/index.js:

```js
const http = require("http");
const PORT = 3000;

const FRIENDS = [
  { id: 1, firstname: "James", lastname: "Corby" },
  { id: 2, firstname: "Ifeanyi", lastname: "Omeata" },
  { id: 3, firstname: "Bob", lastname: "Richy" },
];

const error404 = (req, res) => {
  res.statusCode = 404;
  res.setHeader("Content-Type", "text/html");
  res.write("<html>");
  res.write("<head>");
  res.write("<title>No Query Found</title>");
  res.write("</head>");
  res.write("<body>");
  res.write("<h1>No Query Found!</h1>");
  res.write("</body>");
  res.write("</html>");
  res.end();
};

// server.on('request', (req, res) => {
const server = http.createServer((req, res) => {
  //   res.setHeader("Access-Control-Allow-Origin", "http://google.com");
  res.setHeader("Content-Type", "application/json");
  res.statusCode = 200;
  const URL = req.url.split("/");
  const numOfURLParams = URL.length;
  const searchQuery = URL[1];

  if (req.method === "POST" && searchQuery === "friends") {
    req.on("data", (data) => {
      const friend = data.toString();
      console.log("Request:", friend);
      FRIENDS.push(JSON.parse(friend));
      res.end(friend);
    });
    // req.pipe(res);
  }

  if (req.method === "GET") {
    if (searchQuery === "friends") {
      if (numOfURLParams === 2) {
        //show all friends in JSON format
        res.end(JSON.stringify(FRIENDS));
      } else if (numOfURLParams === 3) {
        const numOfFriends = FRIENDS.length;
        const searchId = URL[2];
        const searchIdIndex = Number(searchId) - 1; // +searchId - 1;
        if (searchId > 0 && searchId <= numOfFriends) {
          //show friend with ID searchId
          res.end(JSON.stringify(FRIENDS[searchIdIndex]));
        } else {
          error404(req, res);
        }
      } else {
        error404(req, res);
      }
    } else if (searchQuery === "fruits") {
      res.setHeader("Content-Type", "text/html");
      res.write("<html>");
      res.write("<head>");
      res.write("<title>My Fruits</title>");
      res.write("</head>");
      res.write("<body>");
      res.write("<h1>My Favorite Fruits</h1>");
      res.write("</h2>This is the list of my favorites fruits.</h2>");
      res.write("<ul>");
      res.write("<li>Apples</li>");
      res.write("<li>Bananas</li>");
      res.write("<li>Mangoes</li>");
      res.write("<li>Oranges</li>");
      res.write("</ul>");
      res.write("</body>");
      res.write("</html>");
      res.end();
    } else {
      res.statusCode = 404;
      res.end();
    }
  }
});

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
```

### run with nodemon:

```jsbs
npm run dev
```

### output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node index.js`
// Listening on port 3000...
```

### POST with javascript console:

```js
fetch("http://localhost:3000/friends", {
  method: "POST",
  body: JSON.stringify({ id: 4, firstname: "Alex", lastname: "Dahl" }),
});
```

### POST (using Pipe) with javascript console:

```js
fetch("http://localhost:3000/friends", {
  method: "POST",
  body: JSON.stringify({ id: 3, name: "Grace Hopper" }),
})
  .then((response) => response.json())
  .then((friend) => console.log(friend));
```

### POST with Postman:

![](https://github.com/omeatai/React-Tutorial/assets/32337103/3094bf05-f4b9-4dbc-8f1f-7775dcfb81f3)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b9f3b081-c07e-4222-b552-ca32cd880f03)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/739d1a9e-c58a-4a0b-9917-6d0dc9cbe9fd)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2f5f0682-6c67-4e3c-96b5-613a68fccb46)

</details>

+EXPRESS.js

<details>
  <summary>31. Express.js - Introduction </summary>

# Install Express.js

```jsbs
 npm init -y
```

```jsbs
npm install express
```

# Install Nodemon

```jsbs
npm install nodemon --save-dev
npm install nodemon
```

### express-project/package.json:

```js
{
  "name": "express-project",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  }
}


```

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### run on default:

```jsbs
npm start
```

### run on nodemon:

```jsbs
npm run dev
```

### output:

```js
// MacBook-Air express-project % npm run dev

// > express-project@1.0.0 dev
// > nodemon server.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node server.js`
// Listening on 3000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/de86a5c0-3150-456c-b135-7839c5aeb295)

</details>

<details>
  <summary>32. Express.js - Sending basic Data with GET and POST </summary>

# Sending basic Data with GET and POST

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
  res.send({ id: 1, name: "Jonny" });
});

app.get("/messages", (req, res) => {
  res.send("<h1>Hey! You have got 1 Message!</h1>");
});

app.post("/messages", (req, res) => {
  console.log("Updating messages...");
  res.send({ id: 2, message: "Sent Successfully!" });
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1f338eee-5f75-499c-b585-0b061679593e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/6f344d6d-ae6b-4e4b-b5e3-13c39b124400)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a0ba5aa7-0139-4b55-ad61-e4d42e28f63e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/987ecaa0-143f-4739-8d72-672c4110b7c5)

</details>

<details>
  <summary>33. Express.js - Passing Data as JSON </summary>

# Passing Data as JSON

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

const friends = [
  { id: 0, name: "Manny Paul" },
  { id: 1, name: "Sir Isaac Newton" },
  { id: 2, name: "Bob Zelinksy" },
  { id: 3, name: "Dave Gray" },
];

app.get("/", (req, res) => {
  res.json({ id: 1, name: "Jonny" });
});

app.get("/friends", (req, res) => {
  res.json(friends);
});

app.get("/messages", (req, res) => {
  res.send("<h1>Hey! You have got 1 Message!</h1>");
});

app.post("/messages", (req, res) => {
  console.log("Updating messages...");
  res.send({ id: 2, message: "Sent Successfully!" });
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/69349309-7fa6-4327-95a4-fa5465984dec)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/9b4a24f0-0835-4cf7-887f-4d26fc70da57)

</details>

<details>
  <summary>34. Express.js - Passing ID Params to Route </summary>

# Passing ID Params to Route

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

const friends = [
  { id: 0, name: "Manny Paul" },
  { id: 1, name: "Sir Isaac Newton" },
  { id: 2, name: "Bob Zelinksy" },
  { id: 3, name: "Dave Gray" },
];

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.get("/friends", (req, res) => {
  res.status(200).json(friends);
});

app.get("/friends/:friendsId", (req, res) => {
  const friendId = +req.params.friendsId; // Number(req.params.friendsId)
  const friend = friends[friendId];
  if (friend) {
    res.status(200).json(friend);
  } else {
    // res.sendStatus(404);
    res.status(404).json({ error: { message: "The friend does not exist." } });
  }
});

app.get("/messages", (req, res) => {
  res.status(200).send("<h1>Hey! You have got 1 Message!</h1>");
});

app.post("/messages", (req, res) => {
  console.log("Updating messages...");
  res.status(200).json({ id: 2, message: "Sent Successfully!" });
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/6f288551-aab4-4920-8a79-fad696d0c17d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/11405122-e89a-4ee0-ae87-1064abda745f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2e1ebae5-5dd0-4f96-bc64-b15f2a0d63ea)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/30b12d49-7c92-4068-8441-9e156c8a5430)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e7bf14b8-d827-4913-91c0-96a29bbbe32f)

</details>

<details>
  <summary>35. Express.js - Writing Middleware </summary>

# Writing Middleware

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

const friends = [
  { id: 0, name: "Manny Paul" },
  { id: 1, name: "Sir Isaac Newton" },
  { id: 2, name: "Bob Zelinksy" },
  { id: 3, name: "Dave Gray" },
];

//Middleware to handle logging of request Method and URL parameters
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

//Middleware to handle logging of time taken to process request
app.use((req, res, next) => {
  const start = Date.now();
  next();
  const end = Date.now();
  console.log(`It took ${end - start}ms to process request.`);
});

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.get("/friends", (req, res) => {
  res.status(200).json(friends);
});

app.get("/friends/:friendsId", (req, res) => {
  const friendId = +req.params.friendsId; // Number(req.params.friendsId)
  const friend = friends[friendId];
  if (friend) {
    res.status(200).json(friend);
  } else {
    // res.sendStatus(404);
    res.status(404).json({ error: { message: "The friend does not exist." } });
  }
});

app.get("/messages", (req, res) => {
  res.status(200).send("<h1>Hey! You have got 1 Message!</h1>");
});

app.post("/messages", (req, res) => {
  console.log("Updating messages...");
  res.status(200).json({ id: 2, message: "Sent Successfully!" });
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node server.js`
// Listening on 3000...
// GET /friends/2
// It took 64ms to process request.
// GET /friends
// It took 2ms to process request.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f8e6c25c-d290-440b-911e-48bbf0871a11)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c58a6a65-e59d-43a4-ab34-200fa1fa740b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2896e8a6-e781-4541-92f3-bcea54cc366b)

</details>

<details>
  <summary>36. Express.js - POST JSON data to server </summary>

# POST JSON data to server

### express-project/server.js:

```js
const express = require("express");
const app = express();

const PORT = 3000;

const friends = [
  { id: 0, name: "Manny Paul" },
  { id: 1, name: "Sir Isaac Newton" },
  { id: 2, name: "Bob Zelinksy" },
  { id: 3, name: "Dave Gray" },
];

//Middleware to handle logging of request Method and URL parameters
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

//Middleware to handle logging of time taken to process request
app.use((req, res, next) => {
  const start = Date.now();
  next();
  const end = Date.now();
  console.log(`It took ${end - start}ms to process request.`);
});

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

app.post("/friends", (req, res) => {
  if (!req.body.name) {
    return res.status(400).json({ error: "Missing friend name." });
  }

  const newFriend = {
    id: friends[friends.length - 1].id + 1,
    name: req.body.name,
  };
  friends.push(newFriend);
  res.json(newFriend);
});

app.get("/friends", (req, res) => {
  res.status(200).json(friends);
});

app.get("/friends/:friendsId", (req, res) => {
  const friendId = +req.params.friendsId; // Number(req.params.friendsId)
  const friend = friends[friendId];
  if (friend) {
    res.status(200).json(friend);
  } else {
    // res.sendStatus(404);
    res.status(404).json({ error: { message: "The friend does not exist." } });
  }
});

app.get("/messages", (req, res) => {
  res.status(200).send("<h1>Hey! You have got 1 Message!</h1>");
});

app.post("/messages", (req, res) => {
  console.log("Updating messages...");
  res.status(200).json({ id: 2, message: "Sent Successfully!" });
});

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f62e550b-8c92-43bd-9bbe-8cffceec33da)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b2805e54-81b2-40da-99dd-0e8615093d1e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c996c216-cfb3-4d9c-80bd-3d86ade69f1f)

</details>

<details>
  <summary>37. Express.js - MVC in Express.js </summary>

# MVC in Express.js

### express-project/server.js:

```js
const express = require("express");
const app = express();

const friendsController = require("./controllers/friendsController");
const messagesController = require("./controllers/messagesController");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

app.post("/friends", friendsController.postFriend);
app.get("/friends/:friendsId", friendsController.getFriend);
app.get("/friends", friendsController.getFriends);

app.get("/messages", messagesController.getMessages);
app.post("/messages", messagesController.postMessage);

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/middlewares/loggerMiddleware.js:

```js
function logRequest(req, res, next) {
  console.log(`${req.method} ${req.url}`);
  next();
}

function logTime(req, res, next) {
  const start = Date.now();
  next();
  const end = Date.now();
  console.log(
    `It took ${req.baseUrl}${req.url} ${end - start}ms to process request.`
  );
}

module.exports = { logRequest, logTime };
```

### express-project/models/friendsModel.js:

```js
const friends = [
  { id: 0, name: "Manny Paul" },
  { id: 1, name: "Sir Isaac Newton" },
  { id: 2, name: "Bob Zelinksy" },
  { id: 3, name: "Dave Gray" },
];

module.exports = { friends };
```

### express-project/controllers/friendsController.js:

```js
const { friends: model } = require("../models/friendsModel");

function postFriend(req, res) {
  if (!req.body.name) {
    return res.status(400).json({ error: "Missing friend name." });
  }

  const newFriend = {
    id: model[model.length - 1].id + 1,
    name: req.body.name,
  };
  model.push(newFriend);
  res.json(newFriend);
}

function getFriend(req, res) {
  const friendId = +req.params.friendsId; // Number(req.params.friendsId)
  const friend = model[friendId];
  if (friend) {
    res.status(200).json(friend);
  } else {
    // res.sendStatus(404);
    res.status(404).json({ error: { message: "The friend does not exist." } });
  }
}

function getFriends(req, res) {
  res.status(200).json(model);
}

module.exports = { postFriend, getFriend, getFriends };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/97bb7ac9-ef58-4970-aaf0-788b1abad5f9)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5f8aa9eb-f0a5-4faa-aaaa-88b34a3702bd)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2b2dbe81-a2ea-4972-ab98-3e613a7d021b)

### output:

```js
// MacBook-Air express-project % npm run dev

// > express-project@1.0.0 dev
// > nodemon server.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node server.js`
// Listening on 3000...
// POST /friends
// It took 15ms to process request.
// GET /friends
// It took 2ms to process request.
// [nodemon] restarting due to changes...
// [nodemon] starting `node server.js`
// Listening on 3000...
```

</details>

<details>
  <summary>38. Express.js - Routing in Express </summary>

# Routing in Express

### express-project/server.js:

```js
const express = require("express");
const app = express();

const friendsRouter = require("./routes/friendsRouter");
const messagesRouter = require("./routes/messagesRouter");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

//ROUTES
app.use("/friends", friendsRouter);
app.use("/messages", messagesRouter);

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/routes/friendsRouter.js:

```js
const express = require("express");

const friendsController = require("../controllers/friendsController");

//Set Router for friends children routes
const friendsRouter = express.Router();

//Middleware for getting ip address of request
friendsRouter.use((req, res, next) => {
  console.log("ip address:", req.ip);
  next();
});

//friendsRouter ROUTES
friendsRouter.post("/", friendsController.postFriend);
friendsRouter.get("/:friendsId", friendsController.getFriend);
friendsRouter.get("/", friendsController.getFriends);

module.exports = friendsRouter;
```

### express-project/routes/messagesRouter.js:

```js
const express = require("express");

const messagesController = require("../controllers/messagesController");

//Set Router for messages children routes
const messagesRouter = express.Router();

//messagesRouter ROUTES
messagesRouter.get("/", messagesController.getMessages);
messagesRouter.post("/", messagesController.postMessage);

module.exports = messagesRouter;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/ce5fa179-0284-449d-b38b-60f9c173e11b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/7a5062dc-3978-4a88-91d7-7be7dcf2ffb8)

### output:

```js
// MacBook-Air express-project % npm run dev

// > express-project@1.0.0 dev
// > nodemon server.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node server.js`
// Listening on 3000...
// GET /friends
// It took 15ms to process request.
// ip address: ::1
```

</details>

<details>
  <summary>39. Express.js - Using HTTP Methods for RESTful Services </summary>

# Using HTTP Methods for RESTful Services

### HTTP Verb = POST

```jsbs
HTTP Verb	= POST
CRUD	= Create
Entire Collection (e.g. /customers)	= 201 (Created), 'Location' header with link to /customers/{id} containing new ID.
Specific Item (e.g. /customers/{id}) = 404 (Not Found), 409 (Conflict) if resource already exists..

Examples:
POST http://www.example.com/customers
POST http://www.example.com/customers/12345/orders
```

### HTTP Verb = GET

```jsbs
HTTP Verb	= GET
CRUD	= Read
Entire Collection (e.g. /customers)	= 200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists.
Specific Item (e.g. /customers/{id}) = 200 (OK), single customer. 404 (Not Found), if ID not found or invalid.

Examples:
GET http://www.example.com/customers/12345
GET http://www.example.com/customers/12345/orders
GET http://www.example.com/buckets/sample
```

### HTTP Verb = PUT

```jsbs
HTTP Verb	= PUT
CRUD	= Update/Replace
Entire Collection (e.g. /customers)	= 405 (Method Not Allowed), unless you want to update/replace every resource in the entire collection.
Specific Item (e.g. /customers/{id}) = 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.

Examples:
PUT http://www.example.com/customers/12345
PUT http://www.example.com/customers/12345/orders/98765
PUT http://www.example.com/buckets/secret_stuff
```

### HTTP Verb = PATCH

```jsbs
HTTP Verb	= PATCH
CRUD	= Update/Modify
Entire Collection (e.g. /customers)	= 405 (Method Not Allowed), unless you want to modify the collection itself.
Specific Item (e.g. /customers/{id}) = 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.

Examples:
PATCH http://www.example.com/customers/12345
PATCH http://www.example.com/customers/12345/orders/98765
PATCH http://www.example.com/buckets/secret_stuff
```

### HTTP Verb = DELETE

```jsbs
HTTP Verb	=  DELETE
CRUD	= Delete
Entire Collection (e.g. /customers)	= 405 (Method Not Allowed), unless you want to delete the whole collection—not often desirable.
Specific Item (e.g. /customers/{id}) = 200 (OK). 404 (Not Found), if ID not found or invalid.

Examples:
DELETE http://www.example.com/customers/12345
DELETE http://www.example.com/customers/12345/orders
DELETE http://www.example.com/bucket/sample
```

</details>

<details>
  <summary>40. Express.js - Sending Files </summary>

# Sending Files

### express-project/server.js:

```js
const express = require("express");
const app = express();

const friendsRouter = require("./routes/friendsRouter");
const messagesRouter = require("./routes/messagesRouter");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

//ROUTES
app.use("/friends", friendsRouter);
app.use("/messages", messagesRouter);

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/routes/messagesRouter.js:

```js
const express = require("express");

const messagesController = require("../controllers/messagesController");

//Set Router for messages children routes
const messagesRouter = express.Router();

//messagesRouter ROUTES
messagesRouter.get("/photo", messagesController.getPhoto);
messagesRouter.get("/", messagesController.getMessages);
messagesRouter.post("/", messagesController.postMessage);

module.exports = messagesRouter;
```

### express-project/controllers/messagesController.js:

```js
const path = require("path");

function getPhoto(req, res) {
  res.sendFile(path.join(__dirname, "..", "public", "skimountain.jpeg"));
}

function getMessages(req, res) {
  res.status(200).send("<h1>Hey! You have got 1 Message!</h1>");
}

function postMessage(req, res) {
  console.log("Updating messages...");
  res.status(200).json({ message: "Sent Successfully!" });
}

module.exports = { getMessages, postMessage, getPhoto };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1c74b29d-2421-43f1-b1ab-a111e6cebeb6)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/13184f0d-19b7-4769-85d7-5467345a98eb)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5ef00957-49c2-4506-88c7-a4fd5c33e387)

</details>

<details>
  <summary>41. Express.js - Serving HTML Static site </summary>

# Serving HTML Static site

### express-project/server.js:

```js
const path = require("path");
const express = require("express");
const app = express();

const friendsRouter = require("./routes/friendsRouter");
const messagesRouter = require("./routes/messagesRouter");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

//Serving static html files to frontend routes
app.use("/web", express.static(path.join(__dirname, "public")));

//ROUTES
app.use("/friends", friendsRouter);
app.use("/messages", messagesRouter);

app.get("/", (req, res) => {
  res.status(200).send("Welcome to the HomePage!");
});

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/public/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Skiing Trip</title>
    <link rel="stylesheet" href="./css/style.css" />
  </head>
  <body>
    <h1>France is beautiful!</h1>
    <img src="./images/skimountain.jpeg" alt="Ski mountain" />
  </body>
</html>
```

### express-project/public/css/style.css:

```css
body {
  padding: 50px;
  font: 14px "Lucida Grande", Helvetica, Arial, sans-serif;
}

h1 {
  color: royalblue;
}

a {
  color: #00b7ff;
}
```

### express-project/controllers/messagesController.js:

```js
const path = require("path");

function getPhoto(req, res) {
  res.sendFile(
    path.join(__dirname, "..", "public", "images", "skimountain.jpeg")
  );
}

function getMessages(req, res) {
  res.status(200).send("<h1>Hey! You have got 1 Message!</h1>");
}

function postMessage(req, res) {
  console.log("Updating messages...");
  res.status(200).json({ message: "Sent Successfully!" });
}

module.exports = { getMessages, postMessage, getPhoto };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d699989a-d275-4f2c-b62a-7f711b2d9ac4)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a9d50e54-fb8c-458a-9ff9-b362c0f85806)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/77136d10-f7bd-4aa9-b122-1c8e2952edbb)

</details>

<details>
  <summary>42. Express.js - Dynamic HTML Templating </summary>

# Install hbs template module

```jsbs
npm install hbs --save
```

### express-project/package.json:

```js
{
  "name": "express-project",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "hbs": "^4.2.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  }
}
```

# Serving Dynamic hbs files

### express-project/server.js:

```jsbs
app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "views"));

//Serving Dynamic hbs files to frontend routes
app.get("/", (req, res) => {
  res.render("index", {
    title: "My Europe Skiing Trip",
    caption: "Europe is really great",
  });
});
```

```js
const path = require("path");
const express = require("express");
const app = express();

app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "views"));

const friendsRouter = require("./routes/friendsRouter");
const messagesRouter = require("./routes/messagesRouter");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

//Serving static html files to frontend routes
app.use("/web", express.static(path.join(__dirname, "public")));

//Serving Dynamic hbs files to frontend routes
app.get("/", (req, res) => {
  res.render("index", {
    title: "My Europe Skiing Trip",
    caption: "Europe is really great",
  });
});

//ROUTES
app.use("/friends", friendsRouter);
app.use("/messages", messagesRouter);

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/views/index.hbs:

```js
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ title }}</title>
    <link rel="stylesheet" href="web/css/style.css" />
  </head>
  <body>
    <h1>{{ caption }}</h1>
    <img src="web/images/skimountain.jpeg" alt="Ski mountain" />
  </body>
</html>
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/ea63c7ad-b2d9-499d-aa16-040a64c0bdd7)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/492917e4-ece6-440f-aab6-492a6ed601ba)

</details>

<details>
  <summary>43. Express.js - Layout for HTML Templating </summary>

# Layout for HTML Templating

### express-project/server.js:

```js
const path = require("path");
const express = require("express");
const app = express();

app.set("view engine", "hbs");
app.set("views", path.join(__dirname, "views"));

const friendsRouter = require("./routes/friendsRouter");
const messagesRouter = require("./routes/messagesRouter");
const { logRequest, logTime } = require("./middlewares/loggerMiddleware");

const PORT = 3000;

//Middleware to handle logging of request Method and URL parameters
app.use(logRequest);

//Middleware to handle logging of time taken to process request
app.use(logTime);

//Middleware to handle setting of request.body fields to JavaScript objects
app.use(express.json());

//Serving static html files to frontend routes
app.use("/web", express.static(path.join(__dirname, "public")));

//Serving Dynamic hbs files to frontend routes
app.get("/", (req, res) => {
  res.render("index", {
    title: "My Europe Skiing Trip",
    caption: "Europe is really great",
  });
});

//ROUTES
app.use("/friends", friendsRouter);
app.use("/messages", messagesRouter);

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}...`);
});
```

### express-project/controllers/messagesController.js:

```js
const path = require("path");

function getPhoto(req, res) {
  res.sendFile(
    path.join(__dirname, "..", "public", "images", "skimountain.jpeg")
  );
}

function getMessages(req, res) {
  res.render("messages", {
    title: "My messages",
    friend: "Elon Musk",
  });
}

function postMessage(req, res) {
  console.log("Updating messages...");
  res.status(200).json({ message: "Sent Successfully!" });
}

module.exports = { getMessages, postMessage, getPhoto };
```

### express-project/views/layout.hbs:

```hbs
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{title}}</title>
    <link rel="stylesheet" href="web/css/style.css" />
  </head>
  <body>
    {{{body}}}
  </body>
</html>
```

### express-project/views/index.hbs:

```hbs
<h1>{{caption}}</h1>
<img src="web/images/skimountain.jpeg" alt="Ski mountain" />
```

### express-project/views/messages.hbs:

```hbs
<h1>My Messages</h1>
<ul>
  <li>Hello {{friend}}!</li>
  <li>What are your thoughts on black holes?</li>
</ul>
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/99a38da7-78e0-4367-bcfe-de98ddef828d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/da6e2f6e-e2c0-4f2d-b31b-4ac758d9008b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/68b3bfe7-dacf-46a6-badf-3a88f03081be)

</details>

+NASA PROJECT

<details>
  <summary>44. NASA Project - Introduction  </summary>

# Lucidchart sketch of API design

![](https://github.com/omeatai/React-Tutorial/assets/32337103/16052252-57f2-4451-9c5e-917793f8a982)

# Install dependencies for Client

```jsbs
npm install
npm install --save
```

# run client

```jsbs
npm run start
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/988ea7d8-1554-4467-801a-eed3e3e902cf)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/7764feda-7cc2-44f0-ba7b-2b7806ce265d)

# Setup Package.json for Server

```jsbs
npm init -y
```

# Install nodemon

```jsbs
npm install nodemon --save-dev
```

# Install express server

```jsbs
npm install express --save
```

# Setup Server with Express

### nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "PORT=5000 node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}

```

# run server

```jsbs
npm run watch
```

### nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
```

### nasa-project/server/src/app.js:

```js
const express = require("express");
const app = express();

app.use(express.json());

module.exports = app;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/2365f88e-626b-4850-bf46-c397e0663e59)

</details>

<details>
  <summary>45. NASA Project - Setup Server for GET/ planets  </summary>

# Setup Server for GET/ planets

### nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
```

### nasa-project/server/src/app.js:

```js
const express = require("express");

const planetsRouter = require("./routes/planetsRouter");

const app = express();

app.use(express.json());
app.use(planetsRouter);

module.exports = app;
```

### nasa-project/server/src/routes/planetsRouter.js:

```js
const express = require("express");

const planetsController = require("../controllers/planetsController");
const planetsRouter = express.Router();

planetsRouter.get("/planets", planetsController.getAllPlanets);

module.exports = planetsRouter;
```

### nasa-project/server/src/controllers/planetsController.js:

```js
const planets = require("../models/planetsModel");

function getAllPlanets(req, res) {
  return res.status(200).json(planets);
}

module.exports = { getAllPlanets };
```

### nasa-project/server/src/models/planetsModel.js:

```js
const planets = [];

module.exports = planets;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/ab556214-90c1-4eab-9a61-d4d543a29f1c)

</details>

<details>
  <summary>46. NASA Project - Setup Client for GET/ planets  </summary>

# Setup Client for GET/ planets

### nasa-project/client/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
```

### nasa-project/client/src/App.js:

```js
import { BrowserRouter as Router } from "react-router-dom";
import {
  Arwes,
  SoundsProvider,
  ThemeProvider,
  createSounds,
  createTheme,
} from "arwes";

import AppLayout from "./pages/AppLayout";

import { theme, resources, sounds } from "./settings";

const App = () => {
  return (
    <ThemeProvider theme={createTheme(theme)}>
      <SoundsProvider sounds={createSounds(sounds)}>
        <Arwes
          animate
          background={resources.background.large}
          pattern={resources.pattern}
        >
          {(anim) => (
            <Router>
              <AppLayout show={anim.entered} />
            </Router>
          )}
        </Arwes>
      </SoundsProvider>
    </ThemeProvider>
  );
};

export default App;
```

### nasa-project/client/src/hooks/usePlanets.js:

```js
import { useCallback, useEffect, useState } from "react";

import { httpGetPlanets } from "./requests";

function usePlanets() {
  const [planets, savePlanets] = useState([]);

  const getPlanets = useCallback(async () => {
    const fetchedPlanets = await httpGetPlanets();
    savePlanets(fetchedPlanets);
  }, []);

  useEffect(() => {
    getPlanets();
  }, [getPlanets]);

  return planets;
}

export default usePlanets;
```

### nasa-project/client/src/hooks/requests.js:

```js
const apiURL = "http://localhost:8000";

async function httpGetPlanets() {
  // TODO: Once API is ready.
  // Load planets and return as JSON.
  const response = await fetch(`${apiURL}/planets`);
  return await response.json();
}

async function httpGetLaunches() {
  // TODO: Once API is ready.
  // Load launches, sort by flight number, and return as JSON.
}

async function httpSubmitLaunch(launch) {
  // TODO: Once API is ready.
  // Submit given launch data to launch system.
}

async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
}

export { httpGetPlanets, httpGetLaunches, httpSubmitLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e15a84e0-a4d5-416a-9e37-ee6396c8e382)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5598cea5-7fd1-4cd5-8cb3-b8c34e96006d)

</details>

<details>
  <summary>47. NASA Project - CORS WhiteListing </summary>

# Install CORS

```jsbs
npm install cors
```

### nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Listening on port ${PORT}...`);
});
```

### nasa-project/server/src/app.js:

```js
const express = require("express");
const cors = require("cors");

const planetsRouter = require("./routes/planetsRouter");

const app = express();

app.use(
  cors({
    origin: "http://localhost:3000",
    // maxAge: 0,
  })
);
app.use(express.json());
app.use(planetsRouter);

module.exports = app;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f3d8d1dd-e50d-4685-b759-6c7ce2e1f82c)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/8e04e478-d75e-4e7d-a7d2-78022389f308)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/10f57d71-2fdc-44ed-b452-de55532a58ce)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2ebf9634-9e72-4afc-82e2-72ce01cc6ede)

</details>

<details>
  <summary>48. NASA Project - Importing Kepler Data </summary>

# Install csv parser

```jsbs
 npm install csv-parse
```

### nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "PORT=5000 node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2"
  }
}

```

# Promise Logic

```js
/*
const promise = new Promise ((resolve, reject) => {
  resolve (42);
});
promise.then((result) => {
  //console.log(result);
});
const result = await promise;
console.log(result);
*/
```

### nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const habitablePlanets = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", (data) => {
        if (isHabitablePlanet(data)) {
          habitablePlanets.push(data);
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", () => {
        // console.log(habitablePlanets.map((planet) => {
        //     return planet["kepler_name"];
        //   })
        // );
        console.log(`${habitablePlanets.length} habitable planets found!`);
        resolve();
      });
  });
}

module.exports = { loadPlanetsData, planets: habitablePlanets };
```

### nasa-project/server/src/app.js:

```js
const express = require("express");
const cors = require("cors");

const planetsRouter = require("./routes/planetsRouter");

const app = express();

app.use(
  cors({
    origin: "http://localhost:3000",
    // maxAge: 0,
  })
);
app.use(express.json());
app.use(planetsRouter);

module.exports = app;
```

### nasa-project/server/src/routes/planetsRouter.js:

```js
const express = require("express");

const planetsController = require("../controllers/planetsController");
const planetsRouter = express.Router();

planetsRouter.get("/planets", planetsController.getAllPlanets);

module.exports = planetsRouter;
```

### nasa-project/server/src/controllers/planetsController.js:

```js
const { planets } = require("../models/planetsKeplerModel");

function getAllPlanets(req, res) {
  return res.status(200).json(planets);
}

module.exports = { getAllPlanets };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/36944df4-26d9-4f75-872b-8aaf26911141)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/d95d1773-4b6e-4514-886f-3a34eec454aa)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/1f23813d-be42-402c-bea3-4d01a84a9f69)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/94138e1c-3efa-4ef4-97c0-c137dae5461c)

</details>

<details>
  <summary>49. NASA Project - Automating running of Client and Server </summary>

### nasa-project/server/.gitignore:

# Initialise npm at root

```jsbs
npm init -y
```

### nasa-project/package.json:

```js
{
  "name": "nasa-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "install-server": "npm install --prefix server",
    "install-client": "npm install --prefix client",
    "install": "npm run install-server && npm run install-client",
    "server": "npm run watch --prefix server",
    "client": "npm run start --prefix client",
    "server2": "cd server && npm run watch",
    "client2": "cd client && npm run start",
    "watch": "npm run server & npm run client",
    "test": "npm run test --prefix server && npm run test --prefix client"
  },
  "author": "",
  "license": "ISC"
}
```

# setup .gitignore in server

```jsbs
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local
.eslintcache

npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

### run both client and server:

```jsbs
npm run watch
```

### Install modules in both client and server:

```jsbs
npm run install
```

### run tests in both client and server:

```jsbs
npm run test
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1fd29e84-e53a-4504-89f8-dc743ea0004a)

</details>

<details>
  <summary>50. NASA Project - Serving Frontend in Production (from Server) </summary>

# change build path to point to server

### nasa-project/client/package.json:

```jsbs
"build": "BUILD_PATH=../server/public react-scripts build",
```

```js
{
  "name": "nasa-fe",
  "version": "1.0.1",
  "private": true,
  "dependencies": {
    "arwes": "^1.0.0-alpha.5",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.3.0",
    "react-scripts": "^5.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "BUILD_PATH=../server/public react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "overrides": {
    "nth-check@1.0.2": "2.0.1"
  }
}
```

# run build from client

```jsbs
cd client
npm run build
```

```jsbs
Alternatively, You may serve it with a static server:

npm install -g serve
serve -s ../server/public
```

# Serve frontend static public files from server

### nasa-project/server/src/app.js:

```jsbs
const path = require("path");

app.use(express.static(path.join(__dirname, "..", "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});
```

```js
const path = require("path");
const express = require("express");
const cors = require("cors");

const planetsRouter = require("./routes/planetsRouter");

const app = express();

app.use(
  cors({
    origin: "http://localhost:3000",
    // maxAge: 0,
  })
);
app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use(planetsRouter);
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "PORT=8000 node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2"
  }
}
```

### nasa-project/package.json:

```js
{
  "name": "nasa-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "install-server": "npm install --prefix server",
    "install-client": "npm install --prefix client",
    "install": "npm run install-server && npm run install-client",
    "server": "npm run watch --prefix server",
    "client": "npm run start --prefix client",
    "server2": "cd server && npm run watch",
    "client2": "cd client && npm run start",
    "watch": "npm run server & npm run client",
    "deploy": "npm run build --prefix client && npm start --prefix server",
    "test": "npm run test --prefix server && npm run test --prefix client"
  },
  "author": "",
  "license": "ISC"
}

```

# from root deploy server with static public frontend

```jsbs
npm run deploy
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/5e85298f-e13e-4b4d-a48f-ad7498ea13d1)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bad91bf0-6e34-450f-97d0-e97450bd9183)

</details>

<details>
  <summary>51. NASA Project - Logging Requests with Morgan </summary>

# Install morgan

```jsbs
npm install morgan
```

### nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "PORT=8000 node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2",
    "morgan": "^1.10.0"
  }
}

```

### nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use(planetsRouter);
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/118a9b56-66cd-4b1a-ba54-cc2e59db3bed)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/44f24044-7305-4fec-ad0e-d3d4b4c18c3e)

</details>

<details>
  <summary>52. NASA Project - Launches Model with mapping </summary>

# Launches Model with mapping

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  destination: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

module.exports = {
  launches,
};
```

![](ttps://github.com/omeatai/React-Tutorial/assets/32337103/933e24b0-5f35-48f0-8e14-990552243203)

</details>

<details>
  <summary>53. NASA Project - GET/ launches </summary>

# GET/ launches

### nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use(planetsRouter);
app.use(launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  destination: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

module.exports = {
  launches,
};
```

### nasa-project/server/src/routes/launchesRouter.js:

```js
const express = require("express");

const launchesController = require("../controllers/launchesController");
const launchesRouter = express.Router();

launchesRouter.get("/launches", launchesController.getAllLaunches);

module.exports = launchesRouter;
```

### nasa-project/server/src/controllers/launchesController.js:

```js
const { launches } = require("../models/launchesModel");

function getAllLaunches(req, res) {
  return res.status(200).json(Array.from(launches.values()));
}

module.exports = { getAllLaunches };
```

### nasa-project/client/src/hooks/requests.js:

```js
const apiURL = "http://localhost:8000";

async function httpGetPlanets() {
  // TODO: Once API is ready.
  // Load planets and return as JSON.
  const response = await fetch(`${apiURL}/planets`);
  return await response.json();
}

async function httpGetLaunches() {
  // TODO: Once API is ready.
  // Load launches, sort by flight number, and return as JSON.
  const response = await fetch(`${apiURL}/launches`);
  const fetchedLaunches = await response.json();
  return fetchedLaunches.sort((a, b) => {
    return a.flightNumbert - b.flightNumber;
  });
}

async function httpSubmitLaunch(launch) {
  // TODO: Once API is ready.
  // Submit given launch data to launch system.
}

async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
}

export { httpGetPlanets, httpGetLaunches, httpSubmitLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/5027412a-4adc-4d6f-ba02-066014786120)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/9d43dcda-b154-44cc-a736-98a3ffc433b4)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/df0d376f-569e-45bf-8fac-5c1a54cb6c67)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/50c7896d-c9a3-4cd1-9011-9af0e53d1392)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/59e4ddf0-9ace-4080-868f-5e7a5761dec4)

</details>

<details>
  <summary>54. NASA Project - Refactor with Data Access Functions && http requests with http prefix</summary>

# Refactor with Data Access Functions && http requests with http prefix

### nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use(planetsRouter);
app.use(launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### nasa-project/server/src/routes/launchesRouter.js:

```js
const express = require("express");

const launchesController = require("../controllers/launchesController");
const launchesRouter = express.Router();

launchesRouter.get("/launches", launchesController.httpGetAllLaunches);

module.exports = launchesRouter;
```

### nasa-project/server/src/controllers/launchesController.js:

```js
const { getAllLaunches } = require("../models/launchesModel");

function httpGetAllLaunches(req, res) {
  return res.status(200).json(getAllLaunches());
}

module.exports = { httpGetAllLaunches };
```

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  destination: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function getAllLaunches() {
  return Array.from(launches.values());
}

module.exports = {
  getAllLaunches,
};
```

### nasa-project/server/src/routes/planetsRouter.js:

```js
const express = require("express");

const planetsController = require("../controllers/planetsController");
const planetsRouter = express.Router();

planetsRouter.get("/planets", planetsController.httpGetAllPlanets);

module.exports = planetsRouter;
```

### nasa-project/server/src/controllers/planetsController.js:

```js
const { getAllPlanets } = require("../models/planetsKeplerModel");

function httpGetAllPlanets(req, res) {
  return res.status(200).json(getAllPlanets());
}

module.exports = { httpGetAllPlanets };
```

### nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const habitablePlanets = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", (data) => {
        if (isHabitablePlanet(data)) {
          habitablePlanets.push(data);
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", () => {
        console.log(`${habitablePlanets.length} habitable planets found!`);
        resolve();
      });
  });
}

function getAllPlanets() {
  return habitablePlanets;
}

module.exports = { loadPlanetsData, getAllPlanets };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/8d46874f-899c-4b83-9a2b-e5f0e5900221)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5b010e31-e67e-4382-9dcc-7f2cf1dd4e52)

</details>

<details>
  <summary>55. NASA Project - POST/ launches </summary>

# POST/ launches

### nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use("/planets", planetsRouter);
app.use("/launches", launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### nasa-project/server/src/routes/launchesRouter.js:

```js
const express = require("express");

const launchesController = require("../controllers/launchesController");
const launchesRouter = express.Router();

launchesRouter.get("/", launchesController.httpGetAllLaunches);
launchesRouter.post("/", launchesController.httpAddNewLaunch);

module.exports = launchesRouter;
```

### nasa-project/server/src/controllers/launchesController.js:

```js
const { getAllLaunches, addNewLaunch } = require("../models/launchesModel");

function httpGetAllLaunches(req, res) {
  return res.status(200).json(getAllLaunches());
}

function httpAddNewLaunch(req, res) {
  const launch = req.body;
  launch.launchDate = new Date(launch.launchDate);
  addNewLaunch(launch);
  return res.status(201).json(launch);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch };
```

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  destination: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

module.exports = {
  getAllLaunches,
  addNewLaunch,
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/3d22df34-e73f-424b-9a3f-9796ea171f63)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/49cad76f-b62d-4548-ae15-432b749cc08b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/1f0c0e75-f819-4483-ad6b-42141e35563d)

</details>

<details>
  <summary>56. NASA Project - Validation for POST/ launches </summary>

# Validation for POST/ launches

### nasa-project/server/src/controllers/launchesController.js:

```js
const { getAllLaunches, addNewLaunch } = require("../models/launchesModel");

function httpGetAllLaunches(req, res) {
  return res.status(200).json(getAllLaunches());
}

function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.destination
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  addNewLaunch(launch);
  return res.status(201).json(launch);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch };
```

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  destination: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

module.exports = {
  getAllLaunches,
  addNewLaunch,
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/537bd723-03be-49a6-b1eb-a033fd10d773)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e9a95801-ca0e-47a7-a591-3fab28d09328)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/ba0cfaeb-c710-4f4f-b096-ca58aa189f22)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e42e247d-8bb4-4b8f-b0fc-54f3939449b5)

</details>

<details>
  <summary>57. NASA Project - Executing POST/ launches from Frontend </summary>

# Executing POST/ launches from Frontend

### nasa-project/client/src/hooks/requests.js:

```js
const apiURL = "http://localhost:8000";

async function httpGetPlanets() {
  // TODO: Once API is ready.
  // Load planets and return as JSON.
  const response = await fetch(`${apiURL}/planets`);
  return await response.json();
}

async function httpGetLaunches() {
  // TODO: Once API is ready.
  // Load launches, sort by flight number, and return as JSON.
  const response = await fetch(`${apiURL}/launches`);
  const fetchedLaunches = await response.json();
  return fetchedLaunches.sort((a, b) => {
    return a.flightNumbert - b.flightNumber;
  });
}

async function httpSubmitLaunch(launch) {
  // TODO: Once API is ready.
  // Submit given launch data to launch system.
  try {
    return await fetch(`${apiURL}/launches`, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(launch),
    });
  } catch (err) {
    return {
      ok: false,
    };
  }
}

async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
}

export { httpGetPlanets, httpGetLaunches, httpSubmitLaunch, httpAbortLaunch };
```

### nasa-project/client/src/hooks/useLaunches.js:

```js
import { useCallback, useEffect, useState } from "react";

import { httpGetLaunches, httpSubmitLaunch, httpAbortLaunch } from "./requests";

function useLaunches(onSuccessSound, onAbortSound, onFailureSound) {
  const [launches, saveLaunches] = useState([]);
  const [isPendingLaunch, setPendingLaunch] = useState(false);

  const getLaunches = useCallback(async () => {
    const fetchedLaunches = await httpGetLaunches();
    saveLaunches(fetchedLaunches);
  }, []);

  useEffect(() => {
    getLaunches();
  }, [getLaunches]);

  const submitLaunch = useCallback(
    async (e) => {
      e.preventDefault();
      setPendingLaunch(true);
      const data = new FormData(e.target);
      const launchDate = new Date(data.get("launch-day"));
      const mission = data.get("mission-name");
      const rocket = data.get("rocket-name");
      const target = data.get("planets-selector");
      const response = await httpSubmitLaunch({
        launchDate,
        mission,
        rocket,
        target,
      });

      // TODO: Set success based on response.
      const success = response.ok;
      if (success) {
        getLaunches();
        setTimeout(() => {
          setPendingLaunch(false);
          onSuccessSound();
        }, 800);
      } else {
        onFailureSound();
      }
    },
    [getLaunches, onSuccessSound, onFailureSound]
  );

  const abortLaunch = useCallback(
    async (id) => {
      const response = await httpAbortLaunch(id);

      // TODO: Set success based on response.
      const success = false;
      if (success) {
        getLaunches();
        onAbortSound();
      } else {
        onFailureSound();
      }
    },
    [getLaunches, onAbortSound, onFailureSound]
  );

  return {
    launches,
    isPendingLaunch,
    submitLaunch,
    abortLaunch,
  };
}

export default useLaunches;
```

### nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

module.exports = {
  getAllLaunches,
  addNewLaunch,
};
```

### nasa-project/server/src/controllers/launchesController.js:

```js
const { getAllLaunches, addNewLaunch } = require("../models/launchesModel");

function httpGetAllLaunches(req, res) {
  return res.status(200).json(getAllLaunches());
}

function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  addNewLaunch(launch);
  return res.status(201).json(launch);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/4d92b812-cb88-4d87-8514-69cd0117e0e0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/cf0ed1cf-84f3-4ebb-809f-6c6e22816489)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b599fa4e-24d1-422d-a42e-f3132e375878)

</details>

<details>
  <summary>58. NASA Project - DELETE/ launches </summary>

# DELETE/ launches

### nasa-project/client/src/hooks/requests.js:

```jsbs
async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
  try {
    return await fetch(`${apiURL}/launches/${id}`, {
      method: "delete",
    });
  } catch (err) {
    console.log(err);
    return {
      ok: false,
    };
  }
}
```

```js
const apiURL = "http://localhost:8000";

async function httpGetPlanets() {
  // TODO: Once API is ready.
  // Load planets and return as JSON.
  const response = await fetch(`${apiURL}/planets`);
  return await response.json();
}

async function httpGetLaunches() {
  // TODO: Once API is ready.
  // Load launches, sort by flight number, and return as JSON.
  const response = await fetch(`${apiURL}/launches`);
  const fetchedLaunches = await response.json();
  return fetchedLaunches.sort((a, b) => {
    return a.flightNumbert - b.flightNumber;
  });
}

async function httpSubmitLaunch(launch) {
  // TODO: Once API is ready.
  // Submit given launch data to launch system.
  try {
    return await fetch(`${apiURL}/launches`, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(launch),
    });
  } catch (err) {
    return {
      ok: false,
    };
  }
}

async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
  try {
    return await fetch(`${apiURL}/launches/${id}`, {
      method: "delete",
    });
  } catch (err) {
    console.log(err);
    return {
      ok: false,
    };
  }
}

export { httpGetPlanets, httpGetLaunches, httpSubmitLaunch, httpAbortLaunch };
```

### nasa-project/client/src/hooks/useLaunches.js:

```js
import { useCallback, useEffect, useState } from "react";

import { httpGetLaunches, httpSubmitLaunch, httpAbortLaunch } from "./requests";

function useLaunches(onSuccessSound, onAbortSound, onFailureSound) {
  const [launches, saveLaunches] = useState([]);
  const [isPendingLaunch, setPendingLaunch] = useState(false);

  const getLaunches = useCallback(async () => {
    const fetchedLaunches = await httpGetLaunches();
    saveLaunches(fetchedLaunches);
  }, []);

  useEffect(() => {
    getLaunches();
  }, [getLaunches]);

  const submitLaunch = useCallback(
    async (e) => {
      e.preventDefault();
      setPendingLaunch(true);
      const data = new FormData(e.target);
      const launchDate = new Date(data.get("launch-day"));
      const mission = data.get("mission-name");
      const rocket = data.get("rocket-name");
      const target = data.get("planets-selector");
      const response = await httpSubmitLaunch({
        launchDate,
        mission,
        rocket,
        target,
      });

      // TODO: Set success based on response.
      const success = response.ok;
      if (success) {
        getLaunches();
        setTimeout(() => {
          setPendingLaunch(false);
          onSuccessSound();
        }, 800);
      } else {
        onFailureSound();
      }
    },
    [getLaunches, onSuccessSound, onFailureSound]
  );

  const abortLaunch = useCallback(
    async (id) => {
      const response = await httpAbortLaunch(id);

      // TODO: Set success based on response.
      const success = response.ok;
      if (success) {
        getLaunches();
        onAbortSound();
      } else {
        onFailureSound();
      }
    },
    [getLaunches, onAbortSound, onFailureSound]
  );

  return {
    launches,
    isPendingLaunch,
    submitLaunch,
    abortLaunch,
  };
}

export default useLaunches;
```

### nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use("/planets", planetsRouter);
app.use("/launches", launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### nasa-project/server/src/routes/launchesRouter.js:

```js
const express = require("express");

const launchesController = require("../controllers/launchesController");
const launchesRouter = express.Router();

launchesRouter.get("/", launchesController.httpGetAllLaunches);
launchesRouter.post("/", launchesController.httpAddNewLaunch);
launchesRouter.delete("/:id", launchesController.httpAbortLaunch);

module.exports = launchesRouter;
```

### nasa-project/server/src/controllers/launchesController.js:

```jsbs
function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  //if launch doesn't exist
  if (!existsLaunchWithId(launchId)) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = abortLaunchById(launchId);
  return res.status(200).json(aborted);
}
```

```js
const {
  getAllLaunches,
  addNewLaunch,
  existsLaunchWithId,
  abortLaunchById,
} = require("../models/launchesModel");

function httpGetAllLaunches(req, res) {
  return res.status(200).json(getAllLaunches());
}

function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  addNewLaunch(launch);
  return res.status(201).json(launch);
}

function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  //if launch doesn't exist
  if (!existsLaunchWithId(launchId)) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = abortLaunchById(launchId);
  return res.status(200).json(aborted);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch, httpAbortLaunch };
```

### nasa-project/server/src/models/launchesModel.js:

```jsbs
function abortLaunchById(launchId) {
  // launches.delete(launchId);
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}
```

```js
const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customer: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  // launches.delete(launchId);
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/cabab179-0128-4397-887d-2c6a1c6e379d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/d6014559-a51e-4994-8a4e-c1ab01f696be)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0032f42f-f0d4-4675-83e9-eb0eff918d61)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f85a2e1e-0cfb-4d2c-93c6-8844e91b04ce)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3d291634-17ef-4d65-aa24-4ef8741f58be)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0edfaacd-3839-4ad8-a688-d5f5d8fa7cab)

</details>

+API TESTING

<details>
  <summary>59. API Testing - Testing APIs with Jest </summary>

# Install Jest

```jsbs
cd server
npm install jest --save-dev
```

### nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "jest",
    "test-watch": "jest --watchAll",
    "start": "PORT=8000 node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^29.5.0",
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2",
    "morgan": "^1.10.0"
  }
}

```

### nasa-project/package.json:

```js
{
  "name": "nasa-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "install-server": "npm install --prefix server",
    "install-client": "npm install --prefix client",
    "install": "npm run install-server && npm run install-client",
    "server": "npm run watch --prefix server",
    "client": "npm run start --prefix client",
    "server2": "cd server && npm run watch",
    "client2": "cd client && npm run start",
    "watch": "npm run server & npm run client",
    "deploy": "npm run build --prefix client && npm start --prefix server",
    "test": "npm run test --prefix server && npm run test --prefix client"
  },
  "author": "",
  "license": "ISC"
}

```

# Jest Testing for the following

```jsbs
1. Files in __test__ folder
2. Files ending with ".test.js" or ".spec.js"
```

### nasa-project/server/**tests**/launches.test.js:

```js
describe("Test GET /launches", () => {
  test("It should respond with 200 success", () => {
    const response = 200;
    expect(response).toBe(200);
  });
});

describe("Test POST /launch", () => {
  test("It should respond with 200 success", () => {});
  test("It should catch missing required properties", () => {});
  test("It should catch invalid dates", () => {});
});
```

# To run Test

```jsbs
npm run test
npm run test-watch
```

### output:

```js
// MacBook-Air server % npm run test

// > nasa-project-api@1.0.0 test
// > jest

//  PASS  __tests__/launches.test.js
//   Test GET /launches
//     ✓ It should respond with 200 success (1 ms)
//   Test POST /launch
//     ✓ It should respond with 200 success (1 ms)
//     ✓ It should catch missing required properties
//     ✓ It should catch invalid dates

// Test Suites: 1 passed, 1 total
// Tests:       4 passed, 4 total
// Snapshots:   0 total
// Time:        0.169 s, estimated 1 s
// Ran all test suites.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/248a7f3a-39aa-473b-a6e2-fd0a82c27bb8)

</details>

<details>
  <summary>60. API Testing - Testing GET/ launches API endpoints with Supertest</summary>

# Install supertest

```jsbs
npm install supertest --save-dev
```

# Sample with supertest

```js
const request = require("supertest");
const assert = require("assert");
const express = require("express");

const app = express();

app.get("/user", function (req, res) {
  res.status(200).json({ name: "john" });
});

request(app)
  .get("/user")
  .expect("Content-Type", /json/)
  .expect("Content-Length", "15")
  .expect(200)
  .end(function (err, res) {
    if (err) throw err;
  });
```

```js
const request = require("supertest");
const express = require("express");

const app = express();

app.get("/user", function (req, res) {
  res.status(200).json({ name: "john" });
});

request(app, { http2: true })
  .get("/user")
  .expect("Content-Type", /json/)
  .expect("Content-Length", "15")
  .expect(200)
  .end(function (err, res) {
    if (err) throw err;
  });

request
  .agent(app, { http2: true })
  .get("/user")
  .expect("Content-Type", /json/)
  .expect("Content-Length", "15")
  .expect(200)
  .end(function (err, res) {
    if (err) throw err;
  });
```

```js
describe("GET /user", function () {
  it("responds with json", function (done) {
    request(app)
      .get("/user")
      .auth("username", "password")
      .set("Accept", "application/json")
      .expect("Content-Type", /json/)
      .expect(200, done);
  });
});
```

### nasa-project/server/**tests**/launches.test.js:

```js
const request = require("supertest");
const app = require("../src/app");

describe("Test GET /launches", () => {
  test("It should respond with 200 success", async () => {
    const response = await request(app)
      .get("/launches")
      .expect("Content-Type", /json/)
      .expect(200);
    // expect(response.statusCode).toBe(200);
  });
});

describe("Test POST /launches", () => {
  test("It should respond with 200 success", () => {});
  test("It should catch missing required properties", () => {});
  test("It should catch invalid dates", () => {});
});
```

### output:

```js
//  PASS  __tests__/launches.test.js
//   Test GET /launches
//     ✓ It should respond with 200 success (9 ms)
//   Test POST /launches
//     ✓ It should respond with 200 success
//     ✓ It should catch missing required properties
//     ✓ It should catch invalid dates

// Test Suites: 1 passed, 1 total
// Tests:       4 passed, 4 total
// Snapshots:   0 total
// Time:        0.283 s, estimated 1 s
// Ran all test suites.

// Watch Usage: Press w to show more.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/da2cf95e-a1d4-4c7a-a67c-9f2c9ec3ad3c)

</details>

<details>
  <summary>61. API Testing - Testing POST/ launches API endpoints with Supertest</summary>

# Testing POST/ launches API endpoints with Supertest

### nasa-project/server/**tests**/launches.test.js:

```js
const request = require("supertest");
const app = require("../src/app");

describe("Test GET /launches", () => {
  test("It should respond with 200 success", async () => {
    const response = await request(app)
      .get("/launches")
      .expect("Content-Type", /json/)
      .expect(200);
    // expect(response.statusCode).toBe(200);
  });
});

describe("Test POST /launches", () => {
  const completeLaunchData = {
    mission: "USS Enterprise",
    rocket: "NCC 1701-D",
    target: "Kepler-186 f",
    launchDate: "January 4, 2028",
  };

  const LaunchDataWithoutDate = {
    mission: "USS Enterprise",
    rocket: "NCC 1701-D",
    target: "Kepler-186 f",
  };

  test("It should respond with 201 created", async () => {
    const response = await request(app)
      .post("/launches")
      .send(completeLaunchData)
      .expect("Content-Type", /json/)
      .expect(201);

    const requestDate = new Date(completeLaunchData.launchDate).valueOf();
    const responseDate = new Date(response.body.launchDate).valueOf();
    expect(responseDate).toBe(requestDate);

    expect(response.body).toMatchObject(LaunchDataWithoutDate);
  });
  test("It should catch missing required properties", () => {});
  test("It should catch invalid dates", () => {});
});
```

### output:

```js
// ::ffff:127.0.0.1 - - [18/May/2023:14:21:38 +0000] "GET /launches HTTP/1.1" 200 200 "-" "-"
// ::ffff:127.0.0.1 - - [18/May/2023:14:21:38 +0000] "POST /launches HTTP/1.1" 201 203 "-" "-"
//  PASS  __tests__/launches.test.js
//   Test GET /launches
//     ✓ It should respond with 200 success (9 ms)
//   Test POST /launches
//     ✓ It should respond with 201 created (13 ms)
//     ✓ It should catch missing required properties
//     ✓ It should catch invalid dates

// Test Suites: 1 passed, 1 total
// Tests:       4 passed, 4 total
// Snapshots:   0 total
// Time:        0.215 s, estimated 1 s
// Ran all test suites.

// Watch Usage: Press w to show more.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/44791ac6-6a17-4acb-86dc-2da574e5a53c)

</details>

<details>
  <summary>62. API Testing - Testing POST/ launches API endpoints for "Error Cases" with Supertest</summary>

# Testing POST/ launches API endpoints for "Error Cases" with Supertest

### nasa-project/server/**tests**/launches.test.js:

```js
const request = require("supertest");
const app = require("../src/app");

describe("Test GET /launches", () => {
  test("It should respond with 200 success", async () => {
    const response = await request(app)
      .get("/launches")
      .expect("Content-Type", /json/)
      .expect(200);
    // expect(response.statusCode).toBe(200);
  });
});

describe("Test POST /launches", () => {
  const completeLaunchData = {
    mission: "USS Enterprise",
    rocket: "NCC 1701-D",
    target: "Kepler-186 f",
    launchDate: "January 4, 2028",
  };

  const LaunchDataWithoutDate = {
    mission: "USS Enterprise",
    rocket: "NCC 1701-D",
    target: "Kepler-186 f",
  };

  const launchDataWithInvalidDate = {
    mission: "USS Enterprise",
    rocket: "NCC 1701-D",
    target: "Kepler-186 f",
    launchDate: "zoot",
  };

  test("It should respond with 201 created", async () => {
    const response = await request(app)
      .post("/launches")
      .send(completeLaunchData)
      .expect("Content-Type", /json/)
      .expect(201);

    const requestDate = new Date(completeLaunchData.launchDate).valueOf();
    const responseDate = new Date(response.body.launchDate).valueOf();
    expect(responseDate).toBe(requestDate);

    expect(response.body).toMatchObject(LaunchDataWithoutDate);
  });

  test("It should catch missing required properties", async () => {
    const response = await request(app)
      .post("/launches")
      .send(LaunchDataWithoutDate)
      .expect("Content-Type", /json/)
      .expect(400);

    expect(response.body).toStrictEqual({
      error: "Missing required launch property",
    });
  });

  test("It should catch invalid dates", async () => {
    const response = await request(app)
      .post("/launches")
      .send(launchDataWithInvalidDate)
      .expect("Content-Type", /json/)
      .expect(400);

    expect(response.body).toStrictEqual({
      error: "Invalid launch date",
    });
  });
});
```

### output:

```js
// ::ffff:127.0.0.1 - - [18/May/2023:16:07:07 +0000] "GET /launches HTTP/1.1" 200 200 "-" "-"
// ::ffff:127.0.0.1 - - [18/May/2023:16:07:07 +0000] "POST /launches HTTP/1.1" 201 203 "-" "-"
// ::ffff:127.0.0.1 - - [18/May/2023:16:07:07 +0000] "POST /launches HTTP/1.1" 400 44 "-" "-"
// ::ffff:127.0.0.1 - - [18/May/2023:16:07:07 +0000] "POST /launches HTTP/1.1" 400 31 "-" "-"
//  PASS  __tests__/launches.test.js
//   Test GET /launches
//     ✓ It should respond with 200 success (15 ms)
//   Test POST /launches
//     ✓ It should respond with 201 created (11 ms)
//     ✓ It should catch missing required properties (3 ms)
//     ✓ It should catch invalid dates (2 ms)

// Test Suites: 1 passed, 1 total
// Tests:       4 passed, 4 total
// Snapshots:   0 total
// Time:        0.753 s, estimated 1 s
// Ran all test suites.

// Watch Usage: Press w to show more.
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/75b20dd6-db5a-4c66-9892-5f2710ff54a7)

</details>

+NODE SERVER PERFORMANCE

<details>
  <summary>63. Node Server Performance - Simple Blocking Server </summary>

# Initialize npm

```jsbs
npm init -y
```

# Install express

```jsbs
npm install express
```

# Install nodemon

```jsbs
npm install nodemon
```

### x-blocking-server/package.json:

```js
{
  "name": "x-blocking-server",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "nodemon": "^2.0.22"
  }
}

```

### x-blocking-server/server.js:

```js
const express = require("express");

const app = express();

PORT = 8000;

function delay(duration) {
  const startTime = Date.now();
  while (Date.now() - startTime < duration) {
    //event loop is blocked...
  }
}

app.get("/", (req, res) => {
  res.send("Performance example");
});

app.get("/timer", (req, res) => {
  //delay the response
  delay(9000);
  res.send("Ding ding ding!");
});

app.listen(8000, (err) => {
  if (err) {
    throw err;
  }
  console.log("Listening on port " + PORT);
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/de0f6b1a-df31-4f22-985e-98bdfed99af9)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bb1d7776-c59f-40a8-ae2a-9702503d9bbe)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/8eeba68e-df30-4724-aa2b-193ee84d1b57)

</details>

<details>
  <summary>64. Node Server Performance - Using Node Clusters </summary>

# Using Node Clusters

### x-blocking-server/server.js:

```js
const express = require("express");
const cluster = require("cluster");

const app = express();

PORT = 8000;

function delay(duration) {
  const startTime = Date.now();
  while (Date.now() - startTime < duration) {
    //event loop is blocked...
  }
}

app.get("/", (req, res) => {
  res.send(`Performance example - ${process.pid}`);
});

app.get("/timer", (req, res) => {
  //delay the response
  delay(9000);
  res.send(`Ding ding ding! ${process.pid}`);
});

console.log("Running server.js...");
if (cluster.isMaster) {
  console.log("Master has been started...");
  //create a new cluster worker
  cluster.fork();
  cluster.fork();
} else {
  console.log("Worker process started...");
  app.listen(8000, (err) => {
    if (err) {
      throw err;
    }
    console.log("Listening on port " + PORT);
  });
}
```

### output:

```js
// x-blocking-server % npm run dev

// > x-blocking-server@1.0.0 dev
// > nodemon server.js

// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node server.js`
// Running server.js...
// Master has been started...
// Running server.js...
// Worker process started...
// Listening on port 8000
// Running server.js...
// Worker process started...
// Listening on port 8000
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/bfdbb29a-fc7a-489b-b240-e9751c40512c)

### Cluster-1

![](https://github.com/omeatai/React-Tutorial/assets/32337103/93590855-4a7c-4aea-a0b0-633ca1c03fd2)

### Cluster-2

![](https://github.com/omeatai/React-Tutorial/assets/32337103/500ab9a1-5859-4cf8-88ab-3276fbed27c4)

### Cluster-3

![](https://github.com/omeatai/React-Tutorial/assets/32337103/bb99ff85-854e-43a0-8098-c85978183259)

</details>

<details>
  <summary>65. Node Server Performance - Maximizing Clusters on all cores </summary>

# Maximizing Clusters on all cores

### x-blocking-server/server.js:

```js
const express = require("express");
const cluster = require("cluster");
const os = require("os");

const app = express();

PORT = 8000;

function delay(duration) {
  const startTime = Date.now();
  while (Date.now() - startTime < duration) {
    //event loop is blocked...
  }
}

app.get("/", (req, res) => {
  res.send(`Performance example - ${process.pid}`);
});

app.get("/timer", (req, res) => {
  //delay the response
  delay(9000);
  res.send(`Ding ding ding! ${process.pid}`);
});

console.log("Running server.js...");
if (cluster.isMaster) {
  console.log("Master has been started...");
  //get amount of logical cores available
  const NUM_WORKERS = os.cpus().length;
  console.log(`You have ${NUM_WORKERS} Logical Cores available.`);
  //create a new cluster worker
  for (let i = 0; i < NUM_WORKERS; i++) {
    cluster.fork();
  }
} else {
  console.log("Worker process started...");
  app.listen(8000, (err) => {
    if (err) {
      throw err;
    }
    console.log("Listening on port " + PORT);
  });
}
```

### output:

```js
// [nodemon] 2.0.22
// [nodemon] to restart at any time, enter `rs`
// [nodemon] watching path(s): *.*
// [nodemon] watching extensions: js,mjs,json
// [nodemon] starting `node server.js`
// Running server.js...
// Master has been started...
// You have 8 Logical Cores available.
// Running server.js...
// Worker process started...
// Running server.js...
// Worker process started...
// Listening on port 8000
// Listening on port 8000
// Running server.js...
// Worker process started...
// Running server.js...
// Worker process started...
// Running server.js...
// Worker process started...
// Listening on port 8000
// Running server.js...
// Listening on port 8000
// Worker process started...
// Listening on port 8000
// Listening on port 8000
// Running server.js...
// Worker process started...
// Listening on port 8000
// Running server.js...
// Worker process started...
// Listening on port 8000
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/e651ff1d-06f4-47f2-8c56-de9ec8c8aabc)

### Cluster-1

![](https://github.com/omeatai/React-Tutorial/assets/32337103/98abb210-2307-413a-afa5-96721a84aee4)

### Cluster-2

![](https://github.com/omeatai/React-Tutorial/assets/32337103/2f177a27-db4b-419b-af07-3d8145ed8a07)

### Cluster-3

![](https://github.com/omeatai/React-Tutorial/assets/32337103/f22bb719-ad0f-4b5f-a956-85c4bbdd3ab3)

### Cluster-4

![](https://github.com/omeatai/React-Tutorial/assets/32337103/32f72c62-b940-4433-b43e-0e703cdce528)

</details>

<details>
  <summary>66. Node Server Performance - Using PM2 to create Clusters  </summary>

# Install PM2

```jsbs
npm install pm2
npm install pm2@latest -g
yarn global add pm2
```

### x-blocking-server/package.json:

```js
{
  "name": "x-blocking-server",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "nodemon": "^2.0.22",
    "pm2": "^5.3.0"
  }
}

```

### x-blocking-server/server.js:

```js
const express = require("express");
const app = express();

PORT = 8000;

function delay(duration) {
  const startTime = Date.now();
  while (Date.now() - startTime < duration) {
    //event loop is blocked...
  }
}

app.get("/", (req, res) => {
  res.send(`Performance example - ${process.pid}`);
});

app.get("/timer", (req, res) => {
  //delay the response
  delay(9000);
  res.send(`Ding ding ding! ${process.pid}`);
});

console.log("Running server.js...");
console.log("Worker process started...");
app.listen(8000, (err) => {
  if (err) {
    throw err;
  }
  console.log("Listening on port " + PORT);
});
```

# Start Server on PM2:

```jsbs
pm2 start server.js
pm2 start server.js --name my-api # Name process
```

# Start Server in PM2 Cluster mode:

```jsbs
pm2 start server.js -i 8
pm2 start server.js -i 0 #(max)
pm2 start server.js -l logs.txt -i 0 #(Send Logs to txt file)
```

# Scale Server in PM2 Cluster mode:

```jsbs
pm2 scale app +3   # Scales `app` up by 3 workers
pm2 scale app 2    # Scales `app` up or down to 2 workers total
```

# Reload Server on PM2:

```jsbs
pm2 restart server.js
pm2 reload server.js
pm2 restart all        # Restart all processes
pm2 restart 0          # Restart specific process id
pm2 reload all         # Will 0s downtime reload (for NETWORKED apps)
```

# Stop Server on PM2:

```jsbs
pm2 stop server.js
pm2 stop all           # Stop all processes
pm2 stop 4             # Stop specific process id
```

# Delete Server on PM2:

```jsbs
pm2 delete server.js
pm2 delete 0           # Will remove process from pm2 list
pm2 delete all         # Will remove all processes from pm2 list
```

# Display Server Logs:

```jsbs
pm2 logs
pm2 logs --lines 200
pm2 logs [--raw]       # Display all processes logs in streaming
pm2 flush              # Empty all log files
pm2 reloadLogs         # Reload all logs
```

# Get PM2 status:

```jsbs
pm2 ls
pm2 list
pm2 status             # Display all processes status
pm2 jlist              # Print process list in raw JSON
pm2 prettylist         # Print process list in beautified JSON
pm2 show 0
pm2 show server.js
```

# Terminal Based Dashboard

```jsbs
pm2 monit
```

# Monitoring & Diagnostic Web Interface

```jsbs
pm2 plus
```

# Others

```jsbs
pm2 reset <process>           # Reset meta data (restarted time...)
pm2 updatePM2                 # Update in memory pm2
pm2 ping                      # Ensure pm2 daemon has been launched
pm2 sendSignal SIGUSR2 my-app # Send system signal to script
npm install pm2@latest -g     # npm install pm2@latest -g
pm2 update                    # update the in-memory PM2
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/7e0ce510-3cd9-48d0-aeee-f14c0d89014f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c78e4f82-3cc3-422a-bd0c-4d1ae90a60ed)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/85d3d939-5daf-41ae-93bf-d0e2a89c0688)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2740274a-6bc8-4fa5-aa2b-d583ac4775b1)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0ce2d750-6dd1-40e3-965e-e8da6c247829)

### Cluster-1

![](https://github.com/omeatai/React-Tutorial/assets/32337103/b8df4af7-0666-4211-93d2-aa6e5ac13dab)

### Cluster-2

![](https://github.com/omeatai/React-Tutorial/assets/32337103/c28d97b7-9bf3-448f-a258-fd06f4e1f645)

### Cluster-3

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d99a0e4d-808a-4e80-ab1b-65e8998e8e19)

</details>

<details>
  <summary>67. Node Server Performance - Improving NASA-Project Performance with PM2  </summary>

# Install PM2

```jsbs
npm install pm2
```

### x-nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "jest",
    "test-watch": "jest --watchAll",
    "start": "PORT=8000 node src/server.js",
    "cluster": "PORT=8000 pm2 start src/server.js -i 0"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^29.5.0",
    "nodemon": "^2.0.22",
    "supertest": "^6.3.3"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2",
    "morgan": "^1.10.0",
    "pm2": "^5.3.0"
  }
}

```

### x-nasa-project/package.json:

```js
{
  "name": "nasa-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "install-server": "npm install --prefix server",
    "install-client": "npm install --prefix client",
    "install": "npm run install-server && npm run install-client",
    "server": "npm run watch --prefix server",
    "client": "npm run start --prefix client",
    "server2": "cd server && npm run watch",
    "client2": "cd client && npm run start",
    "watch": "npm run server & npm run client",
    "deploy": "npm run build --prefix client && npm start --prefix server",
    "deploy-cluster": "npm run build --prefix client && npm run cluster --prefix server",
    "test": "npm run test --prefix server && npm run test --prefix client"
  },
  "author": "",
  "license": "ISC"
}

```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use("/planets", planetsRouter);
app.use("/launches", launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/867d825c-b3b5-46e4-a7cc-dbb97b29f709)

### run:

```jsbs
npm run deploy-cluster
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/cc2d6bcb-731a-4fa4-ab48-497990b033de)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b690083b-966f-4e55-acda-8d1f44aa424e)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/7e994950-9537-494e-b639-f6e0317da304)

</details>

<details>
  <summary>68. Node Server Performance - Using Worker Threads  </summary>

# Using Worker Threads

### x-worker-threads/threads.js:

```js
const { isMainThread, workerData, Worker } = require("worker_threads");

if (isMainThread) {
  console.log(`Main Thread! Process ID: ${process.pid}`);
  new Worker(__filename, {
    workerData: [7, 6, 2, 3],
  });
  new Worker(__filename, {
    workerData: [1, 3, 4, 3],
  });
} else {
  console.log(`Worker! Process ID: ${process.pid}`);
  console.log(`${workerData} sorted is ${workerData.sort()}`);
}
```

### output:

```js
// x-worker-threads % node threads.js
// Main Thread! Process ID: 32584
// Worker! Process ID: 32584
// 1,3,4,3 sorted is 1,3,3,4
// Worker! Process ID: 32584
// 7,6,2,3 sorted is 2,3,6,7
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/fa337baf-fd08-43a3-982f-0e8ff826e7ab)

</details>

+DATABASES

<details>
  <summary>69. Databases - Setting up MongoDB Atlas </summary>

# Install your driver

```jsbs
npm install mongodb
```

# Add your connection string into your application code

```jsbs
mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority
```

```jsbs

const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);

```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/88a81eae-d181-4822-920b-43cfc69e130d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b3bfc671-606d-4777-bd83-54dd6fa7825b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f4720e9c-ba41-4d95-a667-012ad8b2d3b0)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/24713d67-028f-43d4-b066-2253ec0d7302)

</details>

<details>
  <summary>70. Databases - Connecting to MongoDB with Mongoose  </summary>

# Install Mongoose

```jsbs
npm install mongoose
```

### x-nasa-project/server/package.json:

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    "test": "jest",
    "test-watch": "jest --watchAll",
    "start": "PORT=8000 node src/server.js",
    "cluster": "PORT=8000 pm2 start src/server.js -i 0"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^29.5.0",
    "nodemon": "^2.0.22",
    "supertest": "^6.3.3"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2",
    "mongoose": "^7.2.0",
    "morgan": "^1.10.0",
    "pm2": "^5.3.0"
  }
}

```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const mongoose = require("mongoose");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const MONGO_URL =
  "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

const server = http.createServer(app);

mongoose.connection.once("open", () => {
  console.log("MongoDB connection ready!");
});

mongoose.connection.on("error", (err) => {
  console.error(err);
});

async function startServer() {
  await mongoose.connect(MONGO_URL);
  // await mongoose.connect(MONGO_URL, {
  //   useNewUrlParser: true,
  //   useFindAndModify: false,
  //   useCreateIndex: true,
  //   useUnifiedTopology: true,
  // });
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### run:

```jsbs
npm run cluster
npm pm2 log
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/613958c3-d49f-4d8a-b384-98a78aece3f8)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/38d2968b-7509-4049-affd-b0ed6eb2bf8d)

</details>

<details>
  <summary>71. Databases - Mongoose Schema for Launches </summary>

# Mongoose Schema for Launches

```jsbs
Node App:[queries] -> Model:[uses] -> Schema:[maps to] -> Collections:[has many] (tables) -> Documents (records)
```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const mongoose = require("mongoose");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const MONGO_URL =
  "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

const server = http.createServer(app);

mongoose.connection.once("open", () => {
  console.log("MongoDB connection ready!");
});

mongoose.connection.on("error", (err) => {
  console.error(err);
});

async function startServer() {
  await mongoose.connect(MONGO_URL);
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/models/launchesModel.js:

```js
const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  // launches.delete(launchId);
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/models/launchesSchema.js:

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    // type: mongoose.ObjectId,
    // ref: "Planet",
    type: String,
    required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/aed8cdaf-d28f-4ab1-a64c-a0c9ea29d374)

</details>

<details>
  <summary>72. Databases - Mongoose Schema for Planets </summary>

# Mongoose Schema for Planets

### x-nasa-project/client/src/pages/Launch.js:

```js
import { useMemo } from "react";
import { Appear, Button, Loading, Paragraph } from "arwes";
import Clickable from "../components/Clickable";

const Launch = (props) => {
  const selectorBody = useMemo(() => {
    return props.planets?.map((planet) => (
      <option value={planet.keplerName} key={planet.keplerName}>
        {planet.keplerName}
      </option>
    ));
  }, [props.planets]);

  const today = new Date().toISOString().split("T")[0];

  return (
    <Appear id="launch" animate show={props.entered}>
      <Paragraph>
        Schedule a mission launch for interstellar travel to one of the Kepler
        Exoplanets.
      </Paragraph>
      <Paragraph>
        Only confirmed planets matching the following criteria are available for
        the earliest scheduled missions:
      </Paragraph>
      <ul>
        <li>Planetary radius &lt; 1.6 times Earth's radius</li>
        <li>
          Effective stellar flux &gt; 0.36 times Earth's value and &lt; 1.11
          times Earth's value
        </li>
      </ul>

      <form
        onSubmit={props.submitLaunch}
        style={{
          display: "inline-grid",
          gridTemplateColumns: "auto auto",
          gridGap: "10px 20px",
        }}
      >
        <label htmlFor="launch-day">Launch Date</label>
        <input
          type="date"
          id="launch-day"
          name="launch-day"
          min={today}
          max="2040-12-31"
          defaultValue={today}
        />
        <label htmlFor="mission-name">Mission Name</label>
        <input type="text" id="mission-name" name="mission-name" />
        <label htmlFor="rocket-name">Rocket Type</label>
        <input
          type="text"
          id="rocket-name"
          name="rocket-name"
          defaultValue="Explorer IS1"
        />
        <label htmlFor="planets-selector">Destination Exoplanet</label>
        <select id="planets-selector" name="planets-selector">
          {selectorBody}
        </select>
        <Clickable>
          <Button
            animate
            show={props.entered}
            type="submit"
            layer="success"
            disabled={props.isPendingLaunch}
          >
            Launch Mission ✔
          </Button>
        </Clickable>
        {props.isPendingLaunch && <Loading animate small />}
      </form>
    </Appear>
  );
};

export default Launch;
```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const mongoose = require("mongoose");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const MONGO_URL =
  "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

const server = http.createServer(app);

mongoose.connection.once("open", () => {
  console.log("MongoDB connection ready!");
});

mongoose.connection.on("error", (err) => {
  console.error(err);
});

async function startServer() {
  await mongoose.connect(MONGO_URL);
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const habitablePlanets = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", (data) => {
        if (isHabitablePlanet(data)) {
          habitablePlanets.push(data);
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", () => {
        console.log(`${habitablePlanets.length} habitable planets found!`);
        resolve();
      });
  });
}

function getAllPlanets() {
  return habitablePlanets;
}

module.exports = { loadPlanetsData, getAllPlanets };
```

### x-nasa-project/server/src/models/planetsSchema.js:

```js
const mongoose = require("mongoose");

const planetSchema = new mongoose.Schema({
  keplerName: {
    type: String,
    required: true,
  },
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/8ed2aeff-e8f1-457b-8d63-1658d21d6961)

</details>

<details>
  <summary>73. Databases - Creating Models from Schemas </summary>

# Creating Models from Schemas

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const mongoose = require("mongoose");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const MONGO_URL =
  "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

const server = http.createServer(app);

mongoose.connection.once("open", () => {
  console.log("MongoDB connection ready!");
});

mongoose.connection.on("error", (err) => {
  console.error(err);
});

async function startServer() {
  await mongoose.connect(MONGO_URL);
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const planetsRouter = require("./routes/planetsRouter");
const launchesRouter = require("./routes/launchesRouter");

const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use("/planets", planetsRouter);
app.use("/launches", launchesRouter);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### x-nasa-project/server/src/models/launchesSchema.js:

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    // type: mongoose.ObjectId,
    // ref: "Planet",
    type: String,
    required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});

// Connects launchesSchema with the "launches" collection
module.exports = mongoose.model("Launch", launchesSchema);
```

### x-nasa-project/server/src/models/launchesModel.js:

```js
const launches = require("./launchesSchema");

// const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

launches.set(launch.flightNumber, launch);
// launches.get(100)

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  // launches.delete(launchId);
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/models/planetsSchema.js:

```js
const mongoose = require("mongoose");

const planetSchema = new mongoose.Schema({
  keplerName: {
    type: String,
    required: true,
  },
});

// Connects planetSchema with the "planets" collection
module.exports = mongoose.model("Planet", planetSchema);
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/d7c65920-2e28-49b8-8f76-6bf0cfed7d04)

</details>

<details>
  <summary>74. Databases - Finding Planet Documents (Records) </summary>

# Finding Planet Documents (Records)

### Mongoose find example

https://mongoosejs.com/docs/api/model.html#Model.find()

```js
// find all documents
await MyModel.find({});

// find all documents named john and at least 18
await MyModel.find({ name: "john", age: { $gte: 18 } }).exec();

// executes, name LIKE john and only selecting the "name" and "friends" fields
await MyModel.find({ name: /john/i }, "name friends").exec();

// passing options
await MyModel.find({ name: /john/i }, null, { skip: 10 }).exec();

function getAllPlanets() {
  // return habitablePlanets;
  return planets.find(
    {
      keplerName: "Kepler-62 f",
    }
    //https://mongoosejs.com/docs/api/model.html
    // "-keplerName anotherField" //exclude keplerName field and show the other
    // "keplerName anotherField" //show both fields
    // { 'keplerName': 1 } //show only 'keplerName' field
    // { keplerName: 0 } //show all fields but exclude 'keplerName' field
  );
}
```

### x-nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const planets = require("./planetsSchema");

const habitablePlanets = [];

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", async (data) => {
        if (isHabitablePlanet(data)) {
          // habitablePlanets.push(data);
          // insert + update = upsert
          // await planets.create({
          //   keplerName: data.kepler_name,
          // });
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", () => {
        console.log(`${habitablePlanets.length} habitable planets found!`);
        resolve();
      });
  });
}

async function getAllPlanets() {
  // return habitablePlanets;
  return await planets.find({});
}

module.exports = { loadPlanetsData, getAllPlanets };
```

### x-nasa-project/server/src/controllers/planetsController.js:

```js
const { getAllPlanets } = require("../models/planetsKeplerModel");

async function httpGetAllPlanets(req, res) {
  return res.status(200).json(await getAllPlanets());
}

module.exports = { httpGetAllPlanets };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/32ae64f7-cf52-4478-a24d-90e011db2ab1)

</details>

<details>
  <summary>75. Databases - Creating and Inserting Planet Documents (Records) </summary>

# Creating and Inserting Planet Documents (Records)

### x-nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const planets = require("./planetsSchema");

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", async (data) => {
        if (isHabitablePlanet(data)) {
          savePlanets(data);
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", async () => {
        const countPlanetsFound = (await getAllPlanets()).length;
        console.log(`${countPlanetsFound} habitable planets found!`);
        resolve();
      });
  });
}

async function savePlanets(planet) {
  // insert + update = upsert
  try {
    // await planets.updateOne(
    await planets.findOneAndUpdate(
      {
        keplerName: planet.kepler_name,
      },
      {
        keplerName: planet.kepler_name,
      },
      {
        upsert: true,
      }
    );
  } catch (err) {
    console.log(`Could not save planet. Error: ${err}`);
  }
}

async function getAllPlanets() {
  return await planets.find({});
}

module.exports = { loadPlanetsData, getAllPlanets };
```

### x-nasa-project/server/src/models/planetsSchema.js:

```js
const mongoose = require("mongoose");

const planetSchema = new mongoose.Schema({
  keplerName: {
    type: String,
    required: true,
  },
});

// Connects planetSchema with the "planets" collection
module.exports = mongoose.model("Planet", planetSchema);
```

### x-nasa-project/server/src/controllers/planetsController.js:

```js
const { getAllPlanets } = require("../models/planetsKeplerModel");

async function httpGetAllPlanets(req, res) {
  return res.status(200).json(await getAllPlanets());
}

module.exports = { httpGetAllPlanets };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/62967534-759d-4695-b52a-58d42449a4cb)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/05e81108-7951-445a-8184-b8a81e473007)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/bdc04c18-56a4-42a4-8b23-ba0a02061ec9)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/0d325c36-16a4-44c6-9da1-2fe3bd471832)

</details>

<details>
  <summary>76. Databases - Excluding fields from returned planet data </summary>

# Excluding fields from returned planet data

### x-nasa-project/server/src/models/planetsKeplerModel.js:

```js
const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const planets = require("./planetsSchema");

function isHabitablePlanet(planet) {
  return (
    planet["koi_disposition"] === "CONFIRMED" &&
    planet["koi_insol"] > 0.36 &&
    planet["koi_insol"] < 1.11 &&
    planet["koi_prad"] < 1.6
  );
}

function loadPlanetsData() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(
      path.join(__dirname, "..", "..", "data", "kepler_data.csv")
    )
      .pipe(
        parse({
          comment: "#",
          columns: true,
        })
      )
      .on("data", async (data) => {
        if (isHabitablePlanet(data)) {
          savePlanets(data);
        }
      })
      .on("error", (err) => {
        console.log(err);
        reject(err);
      })
      .on("end", async () => {
        const countPlanetsFound = (await getAllPlanets()).length;
        console.log(`${countPlanetsFound} habitable planets found!`);
        resolve();
      });
  });
}

async function savePlanets(planet) {
  // insert + update = upsert
  try {
    // await planets.updateOne(
    await planets.findOneAndUpdate(
      {
        keplerName: planet.kepler_name,
      },
      {
        keplerName: planet.kepler_name,
      },
      {
        upsert: true,
      }
    );
  } catch (err) {
    console.log(`Could not save planet. Error: ${err}`);
  }
}

async function getAllPlanets() {
  return await planets.find(
    {},
    {
      _id: 0, //Exclude ID from returned planet data
      __v: 0, //Exclude Version number from returned planet data
    }
  );
}

module.exports = { loadPlanetsData, getAllPlanets };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/7fd44cba-f6bb-4b35-88ac-e642d013bfdb)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/109bbbef-2ac3-4933-b858-8e6aeb1a7446)

</details>

<details>
  <summary>77. Databases -  Creating and Inserting Launches Documents (Records) </summary>

# Creating and Inserting Launches Documents (Records)

### x-nasa-project/server/src/models/launchesModel.js:

```js
const launchesDB = require("./launchesSchema");

const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

// launches.set(launch.flightNumber, launch);
saveLaunch(launch);

async function saveLaunch(launch) {
  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function getAllLaunches() {
  return Array.from(launches.values());
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/models/launchesSchema.js:

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    // type: mongoose.ObjectId,
    // ref: "Planet",
    type: String,
    required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});

// Connects launchesSchema with the "launches" collection
module.exports = mongoose.model("Launch", launchesSchema);
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/21b29fcd-904e-409d-a02d-ac67e992ee06)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/90467c20-5c4f-417e-bf98-a52b7dd3b603)

</details>

<details>
  <summary>78. Databases -  Finding Launches Documents (Records) </summary>

# Finding Launches Documents (Records)

### x-nasa-project/server/src/models/launchesModel.js:

```js
const launchesDB = require("./launchesSchema");

const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

// launches.set(launch.flightNumber, launch);
saveLaunch(launch);

async function saveLaunch(launch) {
  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  // return Array.from(launches.values());
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/models/launchesSchema.js:

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    // type: mongoose.ObjectId,
    // ref: "Planet",
    type: String,
    required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});

// Connects launchesSchema with the "launches" collection
module.exports = mongoose.model("Launch", launchesSchema);
```

### x-nasa-project/server/src/controllers/launchesController.js:

```js
const {
  getAllLaunches,
  addNewLaunch,
  existsLaunchWithId,
  abortLaunchById,
} = require("../models/launchesModel");

async function httpGetAllLaunches(req, res) {
  return res.status(200).json(await getAllLaunches());
}

function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  addNewLaunch(launch);
  return res.status(201).json(launch);
}

function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  //if launch doesn't exist
  if (!existsLaunchWithId(launchId)) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = abortLaunchById(launchId);
  return res.status(200).json(aborted);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/9e152d57-e49c-42d8-ad23-d5c65bbf76e4)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/92a28c3f-d9b8-490c-a07e-034450d6fda6)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/cc9e5049-d6ab-4f54-93bb-df060dd43848)

</details>

<details>
  <summary>79. Databases -  Check for referential Integrity </summary>

# Check Referential Integrity

### x-nasa-project/server/src/models/launchesModel.js:

```js
const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const launches = new Map();

let latestFlightNumber = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

// launches.set(launch.flightNumber, launch);
saveLaunch(launch);

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  // return Array.from(launches.values());
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1a3891ed-7bad-4d0e-9116-1437938e4371)

</details>

<details>
  <summary>80. Databases -  Get Latest Flight Number </summary>

# Get Latest Flight Number

### x-nasa-project/server/src/models/launchesModel.js:

```jsbs
async function getLatestFlightNumber() {
  const latestLaunch = await launchesDatabase.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}
```

```js
const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const launches = new Map();

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

saveLaunch(launch);

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  // return Array.from(launches.values());
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDatabase.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function addNewLaunch(launch) {
  latestFlightNumber++;
  launches.set(
    latestFlightNumber,
    Object.assign(launch, {
      success: true,
      upcoming: true,
      customers: ["Zero to Mastery", "NASA"],
      flightNumber: latestFlightNumber,
    })
  );
}

function abortLaunchById(launchId) {
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  addNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/models/launchesSchema.js:

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    // type: mongoose.ObjectId,
    // ref: "Planet",
    type: String,
    required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});

// Connects launchesSchema with the "launches" collection
module.exports = mongoose.model("Launch", launchesSchema);
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/173b3700-c753-4e13-9ea7-5d2171d15a65)

</details>

<details>
  <summary>81. Databases -  Adding (Scheduling) New Launches </summary>

# Adding (Scheduling) New Launches

### x-nasa-project/server/src/models/launchesModel.js:

```jsbs
async function scheduleNewLaunch(launch) {
  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}
```

```js
const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const launches = new Map();

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

saveLaunch(launch);

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  // return Array.from(launches.values());
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDB.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

async function scheduleNewLaunch(launch) {
  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}

// function addNewLaunch(launch) {
//   latestFlightNumber++;
//   launches.set(
//     latestFlightNumber,
//     Object.assign(launch, {
//       success: true,
//       upcoming: true,
//       customers: ["Zero to Mastery", "NASA"],
//       flightNumber: latestFlightNumber,
//     })
//   );
// }

function existsLaunchWithId(launchId) {
  return launches.has(launchId);
}

function abortLaunchById(launchId) {
  const aborted = launches.get(launchId); // undefined or value
  aborted.upcoming = false;
  aborted.success = false;
  return aborted;
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  scheduleNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/controllers/launchesController.js:

```js
const {
  getAllLaunches,
  scheduleNewLaunch,
  existsLaunchWithId,
  abortLaunchById,
} = require("../models/launchesModel");

async function httpGetAllLaunches(req, res) {
  return res.status(200).json(await getAllLaunches());
}

async function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  await scheduleNewLaunch(launch);
  return res.status(201).json(launch);
}

function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  //if launch doesn't exist
  if (!existsLaunchWithId(launchId)) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = abortLaunchById(launchId);
  return res.status(200).json(aborted);
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/7a5185c5-d004-454e-baa7-db99d8b878a9)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/da765239-6140-4423-87b2-d76bb9a350cc)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2a326c28-2f33-44eb-b933-710efa5f520f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/6288e4dc-9228-4732-bef3-e2995436fd7d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3dc508b3-d973-4514-a5e2-7f6236c1f5b5)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/c3cd2f91-3fc5-4012-a005-159bf516783a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/26a515f4-5d78-4185-b44d-6de4a1681f76)

</details>

<details>
  <summary>82. Databases -  Aborting Launches </summary>

# Aborting Launches

### x-nasa-project/server/src/models/launchesModel.js:

```jsbs
async function abortLaunchById(launchId) {
  const aborted = await launchesDB.updateOne(
    {
      flightNumber: launchId,
    },
    {
      upcoming: false,
      success: false,
    }
  );
  return {
    success: aborted.acknowledged && aborted.matchedCount === 1,
    message: aborted,
  };

  // const aborted = launches.get(launchId); // undefined or value
  // aborted.upcoming = false;
  // aborted.success = false;
  // return aborted;
}
```

```js
const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const launches = new Map();

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100,
  mission: "Kepler Exploration X",
  rocket: "Explorer IS1",
  launchDate: new Date("December 27, 2030"),
  target: "Kepler-442 b",
  customers: ["ZTM", "NASA"],
  upcoming: true,
  success: true,
};

saveLaunch(launch);

// function existsLaunchWithId(launchId) {
//   return launches.has(launchId);
// }

async function existsLaunchWithId(launchId) {
  return await launchesDB.findOne({
    flightNumber: launchId,
  });
}

async function abortLaunchById(launchId) {
  const aborted = await launchesDB.updateOne(
    {
      flightNumber: launchId,
    },
    {
      upcoming: false,
      success: false,
    }
  );
  return {
    success: aborted.acknowledged && aborted.matchedCount === 1,
    message: aborted,
  };

  // const aborted = launches.get(launchId); // undefined or value
  // aborted.upcoming = false;
  // aborted.success = false;
  // return aborted;
}

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  // await launchesDB.updateOne(
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  // return Array.from(launches.values());
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDB.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

async function scheduleNewLaunch(launch) {
  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}

module.exports = {
  existsLaunchWithId,
  getAllLaunches,
  scheduleNewLaunch,
  abortLaunchById,
};
```

### x-nasa-project/server/src/controllers/launchesController.js:

```jsbs
async function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  const existsLaunch = await existsLaunchWithId(launchId);

  //if launch doesn't exist
  if (!existsLaunch) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = await abortLaunchById(launchId);
  if (!aborted.success) {
    return res.status(400).json({
      error: "Launch not aborted",
      message: aborted.message,
    });
  }
  return res.status(200).json({ ok: true });
}
```

```js
const {
  getAllLaunches,
  scheduleNewLaunch,
  existsLaunchWithId,
  abortLaunchById,
} = require("../models/launchesModel");

async function httpGetAllLaunches(req, res) {
  return res.status(200).json(await getAllLaunches());
}

async function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  await scheduleNewLaunch(launch);
  return res.status(201).json(launch);
}

async function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  const existsLaunch = await existsLaunchWithId(launchId);

  //if launch doesn't exist
  if (!existsLaunch) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = await abortLaunchById(launchId);
  if (!aborted.success) {
    return res.status(400).json({
      error: "Launch not aborted",
      message: aborted.message,
    });
  }
  return res.status(200).json({ ok: true });
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/9bd057aa-2ca7-4f7c-b5c4-6633df0a4af2)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/525f8782-c0be-4550-95e9-462d0d2f6827)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b3433259-bbca-4dc0-a9fc-dc2187f2423f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/5334d1fe-37ad-4b4e-8b00-be1a9bbd9f98)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/2169fdc7-9884-47f2-9397-f9ebd46565be)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f4bd467b-5179-4340-aa94-75b16b237693)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/af8cf2c9-6e18-46e4-8df8-c91b0f5bb993)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/dcb810e3-c4f2-4600-8d88-ac92183ef5c4)

</details>

<details>
  <summary>83. Databases -  Testing with Jest </summary>

# Testing with Jest

### x-nasa-project/server/package.json:

```jsbs
"jest": {
    "testEnvironment": "node"
  },
```

```js
{
  "name": "nasa-project-api",
  "version": "1.0.0",
  "description": "NASA Mission Control API",
  "main": "src/server.js",
  "scripts": {
    "watch": "nodemon src/server.js",
    // "test": "jest --detectOpenHandles",
    "test": "jest",
    "test-watch": "jest --watchAll",
    "start": "PORT=8000 node src/server.js",
    "cluster": "PORT=8000 pm2 start src/server.js -i 0"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "jest": {
    "testEnvironment": "node"
  },
  "devDependencies": {
    "jest": "^29.5.0",
    "nodemon": "^2.0.22",
    "supertest": "^6.3.3"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "csv-parse": "^5.3.10",
    "express": "^4.18.2",
    "mongoose": "^7.2.0",
    "morgan": "^1.10.0",
    "pm2": "^5.3.0"
  }
}

```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const { mongoConnect } = require("./services/mongoDB");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await mongoConnect();
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/services/mongoDB.js:

```js
const mongoose = require("mongoose");

const MONGO_URL =
  "mongodb+srv://<username>:<password>@nasacluster.0p5vet9.mongodb.net/<dbname>?retryWrites=true&w=majority";

mongoose.connection.once("open", () => {
  console.log("MongoDB connection ready!");
});

mongoose.connection.on("error", (err) => {
  console.error(err);
});

async function mongoConnect() {
  await mongoose.connect(MONGO_URL);
}

async function mongoDisconnect() {
  await mongoose.disconnect();
}

module.exports = {
  mongoConnect,
  mongoDisconnect,
};
```

### x-nasa-project/server/**tests**/launches.test.js:

```js
const request = require("supertest");
const app = require("../src/app");
const { mongoConnect, mongoDisconnect } = require("../src/services/mongoDB");

describe("Launches API Tests", () => {
  beforeAll(async () => {
    await mongoConnect();
  });

  describe("Test GET /launches", () => {
    test("It should respond with 200 success", async () => {
      const response = await request(app)
        .get("/launches")
        .expect("Content-Type", /json/)
        .expect(200);
      // expect(response.statusCode).toBe(200);
    });
  });

  describe("Test POST /launches", () => {
    const completeLaunchData = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
      launchDate: "January 4, 2028",
    };

    const LaunchDataWithoutDate = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
    };

    const launchDataWithInvalidDate = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
      launchDate: "zoot",
    };

    test("It should respond with 201 created", async () => {
      const response = await request(app)
        .post("/launches")
        .send(completeLaunchData)
        .expect("Content-Type", /json/)
        .expect(201);

      const requestDate = new Date(completeLaunchData.launchDate).valueOf();
      const responseDate = new Date(response.body.launchDate).valueOf();
      expect(responseDate).toBe(requestDate);

      expect(response.body).toMatchObject(LaunchDataWithoutDate);
    });

    test("It should catch missing required properties", async () => {
      const response = await request(app)
        .post("/launches")
        .send(LaunchDataWithoutDate)
        .expect("Content-Type", /json/)
        .expect(400);

      expect(response.body).toStrictEqual({
        error: "Missing required launch property",
      });
    });

    test("It should catch invalid dates", async () => {
      const response = await request(app)
        .post("/launches")
        .send(launchDataWithInvalidDate)
        .expect("Content-Type", /json/)
        .expect(400);

      expect(response.body).toStrictEqual({
        error: "Invalid launch date",
      });
    });
  });

  afterAll(async () => {
    await mongoDisconnect();
  });
});
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/2413262b-4e81-499b-9f23-fc52c7d562ea)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e66eb307-1a94-4d98-9b91-ab8116d7edc6)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/05f9afa5-2347-48d8-b4c0-42b9946bf068)

</details>

+SPACEX REST-API PROJECT

<details>
  <summary>84. SPACEX REST-API Project -  Versioning Node API </summary>

# Versioning Node API

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");
const { mongoConnect } = require("./services/mongoDB");

const { loadPlanetsData } = require("./models/planetsKeplerModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await mongoConnect();
  await loadPlanetsData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/app.js:

```js
const path = require("path");
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const apiv1 = require("./apis/apiv1");
const app = express();

app.use(cors({ origin: "http://localhost:3000" }));
app.use(morgan("combined")); //combined | common | dev | short

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "public")));

app.use("/v1", apiv1);

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "public", "index.html"));
});

module.exports = app;
```

### x-nasa-project/server/src/apis/apiv1.js:

```js
const express = require("express");

const planetsRouter = require("../routes/planetsRouter");
const launchesRouter = require("../routes/launchesRouter");

const apiv1 = express.Router();

apiv1.use("/planets", planetsRouter);
apiv1.use("/launches", launchesRouter);

module.exports = apiv1;
```

### x-nasa-project/server/**tests**/launches.test.js:

```js
const request = require("supertest");
const app = require("../src/app");
const { mongoConnect, mongoDisconnect } = require("../src/services/mongoDB");

describe("Launches API Tests", () => {
  beforeAll(async () => {
    await mongoConnect();
  });

  describe("Test GET /v1/launches", () => {
    test("It should respond with 200 success", async () => {
      const response = await request(app)
        .get("/v1/launches")
        .expect("Content-Type", /json/)
        .expect(200);
      // expect(response.statusCode).toBe(200);
    });
  });

  describe("Test POST /v1/launches", () => {
    const completeLaunchData = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
      launchDate: "January 4, 2028",
    };

    const LaunchDataWithoutDate = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
    };

    const launchDataWithInvalidDate = {
      mission: "USS Enterprise",
      rocket: "NCC 1701-D",
      target: "Kepler-62 f",
      launchDate: "zoot",
    };

    test("It should respond with 201 created", async () => {
      const response = await request(app)
        .post("/v1/launches")
        .send(completeLaunchData)
        .expect("Content-Type", /json/)
        .expect(201);

      const requestDate = new Date(completeLaunchData.launchDate).valueOf();
      const responseDate = new Date(response.body.launchDate).valueOf();
      expect(responseDate).toBe(requestDate);

      expect(response.body).toMatchObject(LaunchDataWithoutDate);
    });

    test("It should catch missing required properties", async () => {
      const response = await request(app)
        .post("/v1/launches")
        .send(LaunchDataWithoutDate)
        .expect("Content-Type", /json/)
        .expect(400);

      expect(response.body).toStrictEqual({
        error: "Missing required launch property",
      });
    });

    test("It should catch invalid dates", async () => {
      const response = await request(app)
        .post("/v1/launches")
        .send(launchDataWithInvalidDate)
        .expect("Content-Type", /json/)
        .expect(400);

      expect(response.body).toStrictEqual({
        error: "Invalid launch date",
      });
    });
  });

  afterAll(async () => {
    await mongoDisconnect();
  });
});
```

### x-nasa-project/client/src/hooks/requests.js:

```jsbs
const apiURL = "http://localhost:8000/v1";
```

```js
const apiURL = "http://localhost:8000/v1";

async function httpGetPlanets() {
  // TODO: Once API is ready.
  // Load planets and return as JSON.
  const response = await fetch(`${apiURL}/planets`);
  return await response.json();
}

async function httpGetLaunches() {
  // TODO: Once API is ready.
  // Load launches, sort by flight number, and return as JSON.
  const response = await fetch(`${apiURL}/launches`);
  const fetchedLaunches = await response.json();
  return fetchedLaunches.sort((a, b) => {
    return a.flightNumbert - b.flightNumber;
  });
}

async function httpSubmitLaunch(launch) {
  // TODO: Once API is ready.
  // Submit given launch data to launch system.
  try {
    return await fetch(`${apiURL}/launches`, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(launch),
    });
  } catch (err) {
    return {
      ok: false,
    };
  }
}

async function httpAbortLaunch(id) {
  // TODO: Once API is ready.
  // Delete launch with given ID.
  try {
    return await fetch(`${apiURL}/launches/${id}`, {
      method: "delete",
    });
  } catch (err) {
    console.log(err);
    return {
      ok: false,
    };
  }
}

export { httpGetPlanets, httpGetLaunches, httpSubmitLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/25f46518-7cf3-4771-b66c-fb27ff2b974a)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/4c7b1f62-aa43-4f65-8305-eff23c5b6d58)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/fde05d48-40f2-4dc1-83d2-cf04f2a96c0a)

</details>

<details>
  <summary>85. SPACEX REST-API Project - Getting SpaceX Data from API </summary>

# Getting SpaceX Data from API

### POST: https://api.spacexdata.com/v4/launches/query

### Body:

```js
{
    "query": {},
    "options": {
      "populate": [
        {
          "path": "rocket",
          "select": {
            "name": 1
          }
        },
        {
          "path": "payloads",
          "select": {
          "customers": 1
          }
        }
      ]
    }
}
```

### Response:

```js
{
    "docs": [
        {
            "fairings": {
                "reused": false,
                "recovery_attempt": false,
                "recovered": false,
                "ships": []
            },
            "links": {
                "patch": {
                    "small": "https://images2.imgbox.com/94/f2/NN6Ph45r_o.png",
                    "large": "https://images2.imgbox.com/5b/02/QcxHUb5V_o.png"
                },
                "reddit": {
                    "campaign": null,
                    "launch": null,
                    "media": null,
                    "recovery": null
                },
                "flickr": {
                    "small": [],
                    "original": []
                },
                "presskit": null,
                "webcast": "https://www.youtube.com/watch?v=0a_00nJ_Y88",
                "youtube_id": "0a_00nJ_Y88",
                "article": "https://www.space.com/2196-spacex-inaugural-falcon-1-rocket-lost-launch.html",
                "wikipedia": "https://en.wikipedia.org/wiki/DemoSat"
            },
            "static_fire_date_utc": "2006-03-17T00:00:00.000Z",
            "static_fire_date_unix": 1142553600,
            "net": false,
            "window": 0,
            "rocket": {
                "name": "Falcon 1",
                "id": "5e9d0d95eda69955f709d1eb"
            },
            "success": false,
            "failures": [
                {
                    "time": 33,
                    "altitude": null,
                    "reason": "merlin engine failure"
                }
            ],
            "details": "Engine failure at 33 seconds and loss of vehicle",
            "crew": [],
            "ships": [],
            "capsules": [],
            "payloads": [
                {
                    "customers": [
                        "DARPA"
                    ],
                    "id": "5eb0e4b5b6c3bb0006eeb1e1"
                }
            ],
            "launchpad": "5e9e4502f5090995de566f86",
            "flight_number": 1,
            "name": "FalconSat",
            "date_utc": "2006-03-24T22:30:00.000Z",
            "date_unix": 1143239400,
            "date_local": "2006-03-25T10:30:00+12:00",
            "date_precision": "hour",
            "upcoming": false,
            "cores": [
                {
                    "core": "5e9e289df35918033d3b2623",
                    "flight": 1,
                    "gridfins": false,
                    "legs": false,
                    "reused": false,
                    "landing_attempt": false,
                    "landing_success": null,
                    "landing_type": null,
                    "landpad": null
                }
            ],
            "auto_update": true,
            "tbd": false,
            "launch_library_id": null,
            "id": "5eb87cd9ffd86e000604b32a"
        },
        {
            "fairings": {
                "reused": false,
                "recovery_attempt": false,
                "recovered": false,
                "ships": []
            },
            "links": {
                "patch": {
                    "small": "https://images2.imgbox.com/f9/4a/ZboXReNb_o.png",
                    "large": "https://images2.imgbox.com/80/a2/bkWotCIS_o.png"
                },
                "reddit": {
                    "campaign": null,
                    "launch": null,
                    "media": null,
                    "recovery": null
                },
                "flickr": {
                    "small": [],
                    "original": []
                },
                "presskit": null,
                "webcast": "https://www.youtube.com/watch?v=Lk4zQ2wP-Nc",
                "youtube_id": "Lk4zQ2wP-Nc",
                "article": "https://www.space.com/3590-spacex-falcon-1-rocket-fails-reach-orbit.html",
                "wikipedia": "https://en.wikipedia.org/wiki/DemoSat"
            },
            "static_fire_date_utc": null,
            "static_fire_date_unix": null,
            "net": false,
            "window": 0,
            "rocket": {
                "name": "Falcon 1",
                "id": "5e9d0d95eda69955f709d1eb"
            },
            "success": false,
            "failures": [
                {
                    "time": 301,
                    "altitude": 289,
                    "reason": "harmonic oscillation leading to premature engine shutdown"
                }
            ],
            "details": "Successful first stage burn and transition to second stage, maximum altitude 289 km, Premature engine shutdown at T+7 min 30 s, Failed to reach orbit, Failed to recover first stage",
            "crew": [],
            "ships": [],
            "capsules": [],
            "payloads": [
                {
                    "customers": [
                        "DARPA"
                    ],
                    "id": "5eb0e4b6b6c3bb0006eeb1e2"
                }
            ],
            "launchpad": "5e9e4502f5090995de566f86",
            "flight_number": 2,
            "name": "DemoSat",
            "date_utc": "2007-03-21T01:10:00.000Z",
            "date_unix": 1174439400,
            "date_local": "2007-03-21T13:10:00+12:00",
            "date_precision": "hour",
            "upcoming": false,
            "cores": [
                {
                    "core": "5e9e289ef35918416a3b2624",
                    "flight": 1,
                    "gridfins": false,
                    "legs": false,
                    "reused": false,
                    "landing_attempt": false,
                    "landing_success": null,
                    "landing_type": null,
                    "landpad": null
                }
            ],
            "auto_update": true,
            "tbd": false,
            "launch_library_id": null,
            "id": "5eb87cdaffd86e000604b32b"
        },
        {
            "fairings": {
                "reused": false,
                "recovery_attempt": false,
                "recovered": false,
                "ships": []
            },
            "links": {
                "patch": {
                    "small": "https://images2.imgbox.com/6c/cb/na1tzhHs_o.png",
                    "large": "https://images2.imgbox.com/4a/80/k1oAkY0k_o.png"
                },
                "reddit": {
                    "campaign": null,
                    "launch": null,
                    "media": null,
                    "recovery": null
                },
                "flickr": {
                    "small": [],
                    "original": []
                },
                "presskit": null,
                "webcast": "https://www.youtube.com/watch?v=v0w9p3U8860",
                "youtube_id": "v0w9p3U8860",
                "article": "http://www.spacex.com/news/2013/02/11/falcon-1-flight-3-mission-summary",
                "wikipedia": "https://en.wikipedia.org/wiki/Trailblazer_(satellite)"
            },
            "static_fire_date_utc": null,
            "static_fire_date_unix": null,
            "net": false,
            "window": 0,
            "rocket": {
                "name": "Falcon 1",
                "id": "5e9d0d95eda69955f709d1eb"
            },
            "success": false,
            "failures": [
                {
                    "time": 140,
                    "altitude": 35,
                    "reason": "residual stage-1 thrust led to collision between stage 1 and stage 2"
                }
            ],
            "details": "Residual stage 1 thrust led to collision between stage 1 and stage 2",
            "crew": [],
            "ships": [],
            "capsules": [],
            "payloads": [
                {
                    "customers": [
                        "NASA"
                    ],
                    "id": "5eb0e4b6b6c3bb0006eeb1e3"
                },
                {
                    "customers": [
                        "ORS"
                    ],
                    "id": "5eb0e4b6b6c3bb0006eeb1e4"
                }
            ],
            "launchpad": "5e9e4502f5090995de566f86",
            "flight_number": 3,
            "name": "Trailblazer",
            "date_utc": "2008-08-03T03:34:00.000Z",
            "date_unix": 1217734440,
            "date_local": "2008-08-03T15:34:00+12:00",
            "date_precision": "hour",
            "upcoming": false,
            "cores": [
                {
                    "core": "5e9e289ef3591814873b2625",
                    "flight": 1,
                    "gridfins": false,
                    "legs": false,
                    "reused": false,
                    "landing_attempt": false,
                    "landing_success": null,
                    "landing_type": null,
                    "landpad": null
                }
            ],
            "auto_update": true,
            "tbd": false,
            "launch_library_id": null,
            "id": "5eb87cdbffd86e000604b32c"
        }
    ],
    "totalDocs": 205,
    "offset": 0,
    "limit": 10,
    "totalPages": 21,
    "page": 1,
    "pagingCounter": 1,
    "hasPrevPage": false,
    "hasNextPage": true,
    "prevPage": null,
    "nextPage": 2
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/dd15c746-f77b-4838-941a-442c23ce0c7b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/b87be9f9-bd5c-4ab3-812d-5dc8ff1e6730)

</details>

<details>
  <summary>86. SPACEX REST-API Project -  Mapping SpaceX Data to Databae with Axios </summary>

# Install Axios

```jsbs
npm install axios
```

# flatMap function

```js
function duplicate(n) {
  return [n, n];
}
// [1,2].flatMap(duplicate);
// [1,1,2,2]
```

```js
let arr1 = [1, 2, 3, 4];

arr1.map((x) => [x * 2]);
// [[2], [4], [6], [8]]

arr1.flatMap((x) => [x * 2]);
// [2, 4, 6, 8]

// выравнивается только один уровень
arr1.flatMap((x) => [[x * 2]]);
// [[2], [4], [6], [8]]
```

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const { mongoConnect } = require("./services/mongoDB");
const { loadPlanetsData } = require("./models/planetsKeplerModel");
const { loadLaunchData } = require("./models/launchesModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await mongoConnect();
  await loadPlanetsData();
  await loadLaunchData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/models/launchesModel.js:

```jsbs
async function loadLaunchData() {
  const SPACEX_API_URL = "https://api.spacexdata.com/v4/launches/query";
  console.log("Downloading launch data...");
  const response = await axios.post(SPACEX_API_URL, {
    query: {},
    options: {
      populate: [
        {
          path: "rocket",
          select: {
            name: 1,
          },
        },
        {
          path: "payloads",
          select: {
            customers: 1,
          },
        },
      ],
    },
  });

  const launchDocs = response.data.docs;
  for (const launchDoc of launchDocs) {
    const payloads = launchDoc["payloads"];
    const customers = payloads.flatMap((payload) => {
      return payload["customers"];
    });

    const launch = {
      flightNumber: launchDoc["flight_number"],
      mission: launchDoc["name"],
      rocket: launchDoc["rocket"]["name"],
      launchDate: launchDoc["date_local"],
      upcoming: launchDoc["upcoming"],
      success: launchDoc["success"],
      customers,
    };

    console.log(launch.flightNumber, launch.customers);
  }
}
```

```js
const axios = require("axios");

const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100, // flight_number
  mission: "Kepler Exploration X", //name
  rocket: "Explorer IS1", //rocket.name
  launchDate: new Date("December 27, 2030"), //date_local
  target: "Kepler-442 b", //N/A
  customers: ["ZTM", "NASA"], //payload.customers for each payload
  upcoming: true, //upcoming
  success: true, //success
};

saveLaunch(launch);

async function loadLaunchData() {
  const SPACEX_API_URL = "https://api.spacexdata.com/v4/launches/query";
  console.log("Downloading launch data...");
  const response = await axios.post(SPACEX_API_URL, {
    query: {},
    options: {
      populate: [
        {
          path: "rocket",
          select: {
            name: 1,
          },
        },
        {
          path: "payloads",
          select: {
            customers: 1,
          },
        },
      ],
    },
  });

  const launchDocs = response.data.docs;
  for (const launchDoc of launchDocs) {
    const payloads = launchDoc["payloads"];
    const customers = payloads.flatMap((payload) => {
      return payload["customers"];
    });

    const launch = {
      flightNumber: launchDoc["flight_number"],
      mission: launchDoc["name"],
      rocket: launchDoc["rocket"]["name"],
      launchDate: launchDoc["date_local"],
      upcoming: launchDoc["upcoming"],
      success: launchDoc["success"],
      customers,
    };

    console.log(launch.flightNumber, launch.customers);
  }
}

async function existsLaunchWithId(launchId) {
  return await launchesDB.findOne({
    flightNumber: launchId,
  });
}

async function abortLaunchById(launchId) {
  const aborted = await launchesDB.updateOne(
    {
      flightNumber: launchId,
    },
    {
      upcoming: false,
      success: false,
    }
  );
  return {
    success: aborted.acknowledged && aborted.matchedCount === 1,
    message: aborted,
  };
}

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

async function getAllLaunches() {
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDB.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

async function scheduleNewLaunch(launch) {
  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}

module.exports = {
  loadLaunchData,
  existsLaunchWithId,
  getAllLaunches,
  scheduleNewLaunch,
  abortLaunchById,
};
```

# output:

```js
// [nodemon] restarting due to changes...
// [nodemon] starting `node src/server.js`
// MongoDB connection ready!
// 8 habitable planets found!
// Downloading launch data...
// 1 [ 'DARPA' ]
// 2 [ 'DARPA' ]
// 3 [ 'NASA', 'ORS' ]
// 4 [ 'SpaceX' ]
// 5 [ 'ATSB' ]
// 6 [ 'SpaceX' ]
// 7 [ 'NASA(COTS)', 'NRO' ]
// 8 [ 'NASA(COTS)' ]
// 9 [ 'NASA (CRS)', 'Orbcomm' ]
// 10 [ 'NASA (CRS)' ]
// Listening on port 8000...
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/5f6d86a9-bbd2-4f16-8141-0d8860bbdfea)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/405a2614-c3cf-46e1-8997-1ae3ce5643fb)

</details>

<details>
  <summary>87. SPACEX REST-API Project -  Configuring Paginated APIs </summary>

# Setting page number and limit(how many per page)

```jsbs
"page": 5,
"limit": 10,
```

# Removing limits (fetching all data)

```jsbs
"pagination": false,
```

# POST https://api.spacexdata.com/v4/launches/query

```js
{
    "query": {},
    "options": {
        // "page": 5,
        // "limit": 10,
        "pagination": false,
      "populate": [
        {
          "path": "rocket",
          "select": {
            "name": 1
          }
        },
        {
          "path": "payloads",
          "select": {
          "customers": 1
          }
        }
      ]
    }
}

```

# output:

```jsbs
------------------------truncated------------------
                    "landing_attempt": null,
                    "landing_success": null,
                    "landing_type": null,
                    "landpad": null
                }
            ],
            "auto_update": true,
            "tbd": false,
            "launch_library_id": null,
            "id": "633f72580531f07b4fdf59c6"
        }
    ],
    "totalDocs": 205,
    "offset": 0,
    "limit": 205,
    "totalPages": 1,
    "page": 1,
    "pagingCounter": 1,
    "hasPrevPage": false,
    "hasNextPage": false,
    "prevPage": null,
    "nextPage": null
}
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/1129e6be-05f6-472b-ad79-6dd41d460b35)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/e132c176-75d0-4e42-ad03-caf7467ce710)

</details>

<details>
  <summary>88. SPACEX REST-API Project -  Minimizing API Load </summary>

# Minimizing API Load

### x-nasa-project/server/src/server.js:

```js
const http = require("http");
const app = require("./app");

const { mongoConnect } = require("./services/mongoDB");
const { loadPlanetsData } = require("./models/planetsKeplerModel");
const { loadLaunchData } = require("./models/launchesModel");

const PORT = process.env.PORT || 8000;

const server = http.createServer(app);

async function startServer() {
  await mongoConnect();
  await loadPlanetsData();
  await loadLaunchData();

  server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}...`);
  });
}

startServer();
```

### x-nasa-project/server/src/models/launchesModel.js:

```js
const axios = require("axios");

const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100, // flight_number
  mission: "Kepler Exploration X", //name
  rocket: "Explorer IS1", //rocket.name
  launchDate: new Date("December 27, 2030"), //date_local
  target: "Kepler-442 b", //N/A
  customers: ["ZTM", "NASA"], //payload.customers for each payload
  upcoming: true, //upcoming
  success: true, //success
};

saveLaunch(launch);

// #####################################
//            populateLaunches
// #####################################

async function populateLaunches() {
  const SPACEX_API_URL = "https://api.spacexdata.com/v4/launches/query";

  console.log("Downloading launch data...");
  const response = await axios.post(SPACEX_API_URL, {
    query: {},
    options: {
      // page: 2,
      // limit: 10,
      pagination: false,
      populate: [
        {
          path: "rocket",
          select: {
            name: 1,
          },
        },
        {
          path: "payloads",
          select: {
            customers: 1,
          },
        },
      ],
    },
  });

  const launchDocs = response.data.docs;
  for (const launchDoc of launchDocs) {
    const payloads = launchDoc["payloads"];
    const customers = payloads.flatMap((payload) => {
      return payload["customers"];
    });

    const launch = {
      flightNumber: launchDoc["flight_number"],
      mission: launchDoc["name"],
      rocket: launchDoc["rocket"]["name"],
      launchDate: launchDoc["date_local"],
      upcoming: launchDoc["upcoming"],
      success: launchDoc["success"],
      customers,
    };

    console.log(launch.flightNumber, launch.mission);

    //TODO: populate launches collection...
  }
}

// #####################################
//            loadLaunchData
// #####################################

async function loadLaunchData() {
  const firstLaunch = await findLaunch({
    flightNumber: 1,
    rocket: "Falcon 1",
    mission: "FalconSat",
  });

  if (firstLaunch) {
    console.log("Launch data already loaded");
    // return;
  } else {
    await populateLaunches();
  }
}

// #####################################
//            findLaunch
// #####################################

async function findLaunch(filter) {
  return await launchesDB.findOne(filter);
}

// #####################################
//            existsLaunchWithId
// #####################################

async function existsLaunchWithId(launchId) {
  return await findLaunch({
    flightNumber: launchId,
  });
}

// #####################################
//            abortLaunchById
// #####################################

async function abortLaunchById(launchId) {
  const aborted = await launchesDB.updateOne(
    {
      flightNumber: launchId,
    },
    {
      upcoming: false,
      success: false,
    }
  );
  return {
    success: aborted.acknowledged && aborted.matchedCount === 1,
    message: aborted,
  };
}

// #####################################
//            saveLaunch
// #####################################

async function saveLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

// #####################################
//            getAllLaunches
// #####################################

async function getAllLaunches() {
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

// #####################################
//            getLatestFlightNumber
// #####################################

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDB.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

// #####################################
//            scheduleNewLaunch
// #####################################

async function scheduleNewLaunch(launch) {
  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}

module.exports = {
  loadLaunchData,
  existsLaunchWithId,
  abortLaunchById,
  getAllLaunches,
  scheduleNewLaunch,
};
```

### x-nasa-project/server/src/controllers/launchesController.js:

```js
const {
  getAllLaunches,
  scheduleNewLaunch,
  existsLaunchWithId,
  abortLaunchById,
} = require("../models/launchesModel");

// ####################################
//         httpGetAllLaunches
// ####################################

async function httpGetAllLaunches(req, res) {
  return res.status(200).json(await getAllLaunches());
}

// ####################################
//         httpAddNewLaunch
// ####################################

async function httpAddNewLaunch(req, res) {
  const launch = req.body;

  if (
    !launch.mission ||
    !launch.rocket ||
    !launch.launchDate ||
    !launch.target
  ) {
    return res.status(400).json({
      error: "Missing required launch property",
    });
  }

  launch.launchDate = new Date(launch.launchDate);
  // if (isNaN(launch.launchDate)) {}
  if (launch.launchDate.toString() === "Invalid Date") {
    return res.status(400).json({
      error: "Invalid launch date",
    });
  }

  await scheduleNewLaunch(launch);
  return res.status(201).json(launch);
}

// ####################################
//         httpAbortLaunch
// ####################################

async function httpAbortLaunch(req, res) {
  const launchId = +req.params.id; // Number(req.params.id)

  const existsLaunch = await existsLaunchWithId(launchId);

  //if launch doesn't exist
  if (!existsLaunch) {
    return res.status(404).json({
      error: "Launch not found",
    });
  }

  //if launch does exist
  const aborted = await abortLaunchById(launchId);
  if (!aborted.success) {
    return res.status(400).json({
      error: "Launch not aborted",
      message: aborted.message,
    });
  }
  return res.status(200).json({ ok: true });
}

module.exports = { httpGetAllLaunches, httpAddNewLaunch, httpAbortLaunch };
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/140dd0a0-3d38-4316-a753-aa3e4f30148b)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/7e7d750c-3752-4666-906c-ef9ab3577034)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/9415521a-1f8d-4861-b6a1-9a7361005e72)

</details>

<details>
  <summary>89. SPACEX REST-API Project -  Persisting SpaceX Launches </summary>

# Persisting SpaceX Launches

### x-nasa-project/server/src/models/launchesSchema.js:

```jsbs
  target: {
    type: String,
    // required: true,
  },
```

```js
const mongoose = require("mongoose");

const launchesSchema = new mongoose.Schema({
  flightNumber: {
    type: Number,
    required: true,
    // default: 100,
    // min: 100,
    // max: 999,
  },
  launchDate: {
    type: Date,
    required: true,
  },
  mission: {
    type: String,
    required: true,
  },
  rocket: {
    type: String,
    required: true,
  },
  target: {
    type: String,
    // required: true,
  },
  customers: [String],
  upcoming: {
    type: Boolean,
    required: true,
  },
  success: {
    type: Boolean,
    required: true,
    default: true,
  },
});

// Connects launchesSchema with the "launches" collection
module.exports = mongoose.model("Launch", launchesSchema);
```

### x-nasa-project/server/src/models/launchesModel.js:

```js
const axios = require("axios");

const launchesDB = require("./launchesSchema");
const planetsDB = require("./planetsSchema");

const DEFAULT_FLIGHT_NUMBER = 100;

const launch = {
  flightNumber: 100, // flight_number
  mission: "Kepler Exploration X", //name
  rocket: "Explorer IS1", //rocket.name
  launchDate: new Date("December 27, 2030"), //date_local
  target: "Kepler-442 b", //N/A
  customers: ["ZTM", "NASA"], //payload.customers for each payload
  upcoming: true, //upcoming
  success: true, //success
};

saveLaunch(launch);

// #####################################
//            populateLaunches
// #####################################

async function populateLaunches() {
  const SPACEX_API_URL = "https://api.spacexdata.com/v4/launches/query";

  console.log("Downloading launch data...");
  const response = await axios.post(SPACEX_API_URL, {
    query: {},
    options: {
      // page: 2,
      // limit: 10,
      pagination: false,
      populate: [
        {
          path: "rocket",
          select: {
            name: 1,
          },
        },
        {
          path: "payloads",
          select: {
            customers: 1,
          },
        },
      ],
    },
  });

  if (response.status !== 200) {
    console.log("Problem downloading launch data");
    throw new Error("Launch data download failed");
  }

  const launchDocs = response.data.docs;
  for (const launchDoc of launchDocs) {
    const payloads = launchDoc["payloads"];
    const customers = payloads.flatMap((payload) => {
      return payload["customers"];
    });

    const launch = {
      flightNumber: launchDoc["flight_number"],
      mission: launchDoc["name"],
      rocket: launchDoc["rocket"]["name"],
      launchDate: launchDoc["date_local"],
      upcoming: launchDoc["upcoming"],
      success: launchDoc["success"],
      customers,
    };

    console.log(launch.flightNumber, launch.mission);

    //TODO: populate launches collection...
    await saveLaunch(launch);
  }
}

// #####################################
//            loadLaunchData
// #####################################

async function loadLaunchData() {
  const firstLaunch = await findLaunch({
    flightNumber: 1,
    rocket: "Falcon 1",
    mission: "FalconSat",
  });

  if (firstLaunch) {
    console.log("Launch data already loaded");
    // return;
  } else {
    await populateLaunches();
  }
}

// #####################################
//            findLaunch
// #####################################

async function findLaunch(filter) {
  return await launchesDB.findOne(filter);
}

// #####################################
//            existsLaunchWithId
// #####################################

async function existsLaunchWithId(launchId) {
  return await findLaunch({
    flightNumber: launchId,
  });
}

// #####################################
//            abortLaunchById
// #####################################

async function abortLaunchById(launchId) {
  const aborted = await launchesDB.updateOne(
    {
      flightNumber: launchId,
    },
    {
      upcoming: false,
      success: false,
    }
  );
  return {
    success: aborted.acknowledged && aborted.matchedCount === 1,
    message: aborted,
  };
}

// #####################################
//            saveLaunch
// #####################################

async function saveLaunch(launch) {
  await launchesDB.findOneAndUpdate(
    {
      flightNumber: launch.flightNumber,
    },
    launch,
    { upsert: true }
  );
}

// #####################################
//            getAllLaunches
// #####################################

async function getAllLaunches() {
  return await launchesDB.find(
    {},
    {
      _id: 0,
      __v: 0,
    }
  );
}

// #####################################
//            getLatestFlightNumber
// #####################################

async function getLatestFlightNumber() {
  const latestLaunch = await launchesDB.findOne().sort("-flightNumber");
  if (!latestLaunch) {
    return DEFAULT_FLIGHT_NUMBER;
  }

  return latestLaunch.flightNumber;
}

// #####################################
//            scheduleNewLaunch
// #####################################

async function scheduleNewLaunch(launch) {
  // Check for referential Integrity
  const planet = await planetsDB.findOne({
    keplerName: launch.target,
  });

  if (!planet) {
    throw new Error("No matching planet found.");
  }

  const newFlightNumber = (await getLatestFlightNumber()) + 1;

  const newLaunch = Object.assign(launch, {
    success: true,
    upcoming: true,
    customers: ["Zero to Mastery", "NASA"],
    flightNumber: newFlightNumber,
  });

  await saveLaunch(newLaunch);
}

module.exports = {
  loadLaunchData,
  existsLaunchWithId,
  abortLaunchById,
  getAllLaunches,
  scheduleNewLaunch,
};
```

![](https://github.com/omeatai/React-Tutorial/assets/32337103/97cb558a-a7e1-4ca4-80aa-5c62da9f252f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/a1c4e96b-fe85-48d2-8554-f9e301a2002d)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/f57e1353-02c2-4549-8cc3-1c419054064f)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/3d0e5855-ddfb-4830-b75c-ed7024b6fe94)
![](https://github.com/omeatai/React-Tutorial/assets/32337103/ec4d23e1-5754-467a-a04a-85332744addc)

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```

</details>
