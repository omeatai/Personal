# Client-Server Basics

[Back to TryHackMe](../../tryhackme.md)

<details>
  <summary>Client-Server Basics</summary>

## Introduction

Early computers mostly worked alone—local files, local programs, no communication with other machines. Organizations then interconnected systems for information exchange and resource sharing (precursors of the internet such as ARPANET, CYCLADES, NPL, and NSFNET). Interconnected systems specialized into roles that offer and consume services. This TryHackMe room explains how that works through the **client-server model**, using a pizza-takeaway analogy and a practical HTTP GET lab.

**Learning objectives (surface level):** client-server model, DNS, client, server, port, protocol, and network.

## Detailed Explanation

- [x] **From standalone machines to networks**
  - Early computers stored their own files and ran their own programs without talking to others
  - Interconnecting systems enabled exchange and sharing regardless of distance
  - Historical networks paved the way for the modern internet: ARPANET, CYCLADES, NPL, NSFNET
  - Systems began specializing—like people offering specific skills as services
- [x] **Pizza analogy — service, client, and server**
  - Alice and Bob order from Luigi’s Pizza: Alice chooses the order; Bob delivers the request and brings the response home
  - **Client** initiates the request (e.g. browser requesting a webpage)
  - **Server** provides the service / serves the resource
  - The client is always the one who initiates the request
- [x] **Request and response**
  - A correctly formed request for an available resource yields a successful response
  - Bad formatting or unavailable resources yield an error response (e.g. no pepperoni, or order not understood)
  - In computing: browser (client) requests a webpage; server sends the page (or an error) back
- [x] **Protocol**
  - A protocol defines how a client communicates with a server
  - Includes: commands both sides understand (e.g. GET), request structure, syntax/language, expected responses, and responses to faulty requests
  - Bob in the analogy is like the protocol that carries a shared language and order format between Alice and Luigi’s
- [x] **Port**
  - A **port** identifies a specific service running on a system
  - Clients must connect using the correct port for that service
  - Analogy: takeaway customers use a specific door; multiple services (takeaway, dine-in, delivery) use different doors
  - One server can run multiple services at once, each on a different port
- [x] **DNS (Domain Name Service)**
  - Names alone are not enough to reach a destination (like knowing “Luigi’s Pizza” without coordinates)
  - DNS resolves a name (e.g. a website) to a server location
  - That location is an **Internet Protocol (IP) address**—the “home address” for computer systems
- [x] **HTTP(S) — web communication in practice**
  - **HTTP(S)** is a **stateless** client-server protocol for the World Wide Web
  - Each request is processed independently; the protocol itself does not remember previous requests
  - Applications add state with session identifiers (cookies/tokens) so you stay logged in across requests
  - Without sessions, you would authenticate on every request
- [x] **HTTP methods (commands)**
  - RFCs define 9 core HTTP methods: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, CONNECT, TRACE
  - Room focus: **GET** — retrieve a resource from a web server (e.g. `GET https://tryhackme.com/index.php`)
  - Browsers construct GET messages behind the scenes when you type a URL
  - Server responds with a **status code** and the requested information
- [x] **Lab: inspect a GET request (DevTools Network)**
  - Start the lab machine; open Firefox; visit `http://httpdemo.local:8080`
  - Open Developer Tools (F12 or Inspect) → **Network** tab → reload the page
  - Click the first GET entry to inspect fields:
    - **Scheme** — HTTP or HTTPS
    - **Host** — name of the host you request from
    - **Filename** — file requested; `"/"` maps to `index.html`
    - **Address** — IP of the host (lab example: `127.0.0.1` when hosted locally)
    - **Status** — success indicator (example: **200 OK**)
  - Response has two parts: **header** (metadata) and **body** (requested content, e.g. HTML of the index page)
- [x] **Room Q&A answers**
  - Identify a specific service on a server → **Port**
  - Address of a server → **Internet Protocol address**
  - Host in `https://www.iamlearning.thm/contact` → **www.iamlearning.thm**
  - Scheme in that URL → **https**
- [x] **What comes next**
  - Next room covers the basics of **virtualization**—the infrastructure that supports internet services

<details>
  <summary>Lab</summary>

## Lab

This is a **browser Network-inspector** walkthrough on the TryHackMe lab machine. Pause until the machine is on and the split view is visible.

### **Overview**

- [ ] Inspect a real **GET** request and its response on the demo site.
- [ ] You will:
  - [ ] Start the lab machine and open Firefox.
  - [ ] Open Developer Tools → **Network** and reload the page.
  - [ ] Read scheme, host, filename, address, and status on the first GET.
  - [ ] Open the **Response** tab to see the HTML body.
- [ ] Success: you can name the host and scheme in `https://www.iamlearning.thm/contact` and you have seen a **200 OK** GET.

### **Task 1: Start the lab machine**

- [ ] Click **Start Lab Machine** (or **Start Split-screen** if the pane is hidden).
- [ ] Wait until the machine status is **On**.
- [ ] Confirm the desktop is visible in the split view.

### **Task 2: Open the demo site in Firefox**

- [ ] Click the **Firefox** icon on the lab desktop.
- [ ] Confirm the address bar shows `http://httpdemo.local:8080`.
- [ ] If it does not, type that URL and press Enter.

### **Task 3: Open Developer Tools on the Network tab**

- [ ] Press **F12**, or right-click the page and choose **Inspect**.
- [ ] Click the **Network** tab.
- [ ] Reload the page (circular reload control next to the address bar).
- [ ] Confirm multiple **GET** rows appear in the Network list.

### **Task 4: Inspect the first GET**

- [ ] Click the **first GET** entry.
- [ ] In the right-hand panel, note:
  - [ ] **Scheme** — HTTP or HTTPS
  - [ ] **Host** — name of the host you requested
  - [ ] **Filename** — file requested; `"/"` maps to `index.html`
  - [ ] **Address** — IP of the host (lab example: `127.0.0.1` when hosted locally)
  - [ ] **Status** — success indicator (example: **200 OK**)

### **Task 5: Read the response body**

- [ ] With the same GET selected, open the **Response** tab.
- [ ] Confirm the body is the **HTML** of the index page.
- [ ] Remember: the response has a **header** (metadata) and a **body** (content).

Successfully inspected a client GET and a server response in Firefox Developer Tools.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

This room uses a browser lab and Firefox Developer Tools (Network tab). There are no primary CLI tools; inspection is done in the UI.

```bash
# No primary terminal commands — inspect GET traffic via Firefox DevTools → Network on http://httpdemo.local:8080
```

</details>

<details>
  <summary>Code</summary>

## Code

No programming component. HTTP GET requests and HTML responses are inspected in the browser.

```py
# No code snippets for the Client-Server Basics room.
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What problem did early interconnected networks aim to solve?

<details>
<summary>Answer</summary>

- [x] Information exchange and resource sharing regardless of distance
- [x] Precursors of the internet include ARPANET, CYCLADES, NPL, and NSFNET

</details>

### Question 2: In the client-server model, who initiates communication?

<details>
<summary>Answer</summary>

- [x] The **client** always initiates the request
- [x] The **server** replies by providing the service or resource

</details>

### Question 3: In the pizza analogy, what do Alice, Bob, and Luigi’s represent?

<details>
<summary>Answer</summary>

- [x] **Alice / browser** — client that wants a service (webpage / pizza order)
- [x] **Bob / protocol** — carries the request and response in a shared language and format
- [x] **Luigi’s / server** — system that serves the resource

</details>

### Question 4: What happens if a request is malformed or the resource is unavailable?

<details>
<summary>Answer</summary>

- [x] You get an error response
- [x] Example: no pepperoni available, or the server does not understand the order

</details>

### Question 5: What does a protocol define?

<details>
<summary>Answer</summary>

- [x] Commands the client and server understand (e.g. GET)
- [x] How a request is structured
- [x] What syntax/language is used
- [x] What response to give for successful and faulty requests

</details>

### Question 6: What do we use to identify a specific service on a server?

<details>
<summary>Answer</summary>

- [x] **Port**

</details>

### Question 7: Can one server run multiple services, and how are they distinguished?

<details>
<summary>Answer</summary>

- [x] Yes — one server can run multiple services at the same time
- [x] Each service listens on a different port (like different doors for takeaway, dine-in, delivery)

</details>

### Question 8: What does DNS stand for, and what does it do?

<details>
<summary>Answer</summary>

- [x] **Domain Name Service**
- [x] Resolves a name (e.g. a website) to a server location
- [x] That location is an **Internet Protocol (IP) address**

</details>

### Question 9: What do we call the address of a server?

<details>
<summary>Answer</summary>

- [x] **Internet Protocol address** (IP address)

</details>

### Question 10: What does it mean that HTTP(S) is stateless?

<details>
<summary>Answer</summary>

- [x] Each request is processed independently
- [x] The protocol itself does not retain information about previous requests
- [x] Apps add state with session IDs (cookies/tokens) so login can persist across requests

</details>

### Question 11: Name the nine core HTTP methods listed in the room.

<details>
<summary>Answer</summary>

- [x] GET
- [x] POST
- [x] PUT
- [x] DELETE
- [x] PATCH
- [x] HEAD
- [x] OPTIONS
- [x] CONNECT
- [x] TRACE

</details>

### Question 12: What is the GET method used for?

<details>
<summary>Answer</summary>

- [x] Retrieve a resource from a web server
- [x] Example: `GET https://tryhackme.com/index.php` retrieves the homepage
- [x] The browser builds the request when you navigate to a URL

</details>

### Question 13: In DevTools, what do Scheme, Host, Filename, Address, and Status tell you?

<details>
<summary>Answer</summary>

- [x] **Scheme** — HTTP or HTTPS
- [x] **Host** — name of the host requested
- [x] **Filename** — file requested; `"/"` means `index.html`
- [x] **Address** — IP where the site is hosted (lab example: `127.0.0.1`)
- [x] **Status** — whether the request succeeded (e.g. **200 OK**)

</details>

### Question 14: What are the two parts of an HTTP response?

<details>
<summary>Answer</summary>

- [x] **Response header** — metadata about the response
- [x] **Response body** — the requested content (e.g. HTML)

</details>

### Question 15: What would be the host in `https://www.iamlearning.thm/contact`?

<details>
<summary>Answer</summary>

- [x] `www.iamlearning.thm`

</details>

### Question 16: What would be the scheme in `https://www.iamlearning.thm/contact`?

<details>
<summary>Answer</summary>

- [x] `https`

</details>

### Question 17: How do you open the Network inspector in the Firefox lab?

<details>
<summary>Answer</summary>

- [x] Press **F12** or right-click → **Inspect**
- [x] Open the **Network** tab, reload the page, then click the first GET entry

</details>

### Question 18: What topic does the room say comes next after client-server basics?

<details>
<summary>Answer</summary>

- [x] Basics of **virtualization** — infrastructure that supports internet services

</details>

</details>

## Summary

Client-Server Basics explains how networked machines offer and consume services: the client initiates requests, the server responds, protocols define the shared rules, ports identify services, and DNS maps names to IP addresses. A pizza analogy makes the model concrete; an HTTP GET lab in Firefox DevTools shows scheme, host, path, IP, status codes, and response headers/bodies. Room answers include Port, Internet Protocol address, host `www.iamlearning.thm`, and scheme `https`. Next up: virtualization.

## References

- [Client-Server Basics – TryHackMe](https://tryhackme.com/room/clientserverbasics)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 1034 — Domain Names (concepts and facilities)](https://www.rfc-editor.org/rfc/rfc1034.html)
- [MDN — HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MDN — URL](https://developer.mozilla.org/en-US/docs/Web/API/URL)

</details>
