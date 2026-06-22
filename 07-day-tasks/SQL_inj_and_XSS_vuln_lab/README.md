# Local Vulnerability Sandbox: SQL Injection & XSS

This repository contains a local Node.js web application designed to demonstrate how common web vulnerabilities work at the code level, and how to properly remediate them.

## Prerequisites
* [Node.js](https://nodejs.org/) installed on your machine.

## Quick Start
1. Clone this repository.
2. Open a terminal in the project directory.
3. Install dependencies:
   ```bash
   npm install express sqlite3
   ```
4. Start the server:
   ```bash
   node server.js
   ```
5. Open your web browser and navigate to `http://localhost:3000`.

---

## Module 1: SQL Injection (SQLi)

This module demonstrates how unsanitized user input directly concatenated into SQL queries allows attackers to manipulate database logic. 

### Vulnerable Code Pattern (String Concatenation):
```javascript
const query = "SELECT * FROM users WHERE username = '" + userInput + "'";
```

### Educational Payloads Explained:

1. **Authentication Bypass (Tautologies):** By injecting an `OR` statement that is always true, the attacker forces the entire `WHERE` clause to evaluate to true, bypassing the intended logic.
   * *Payload:* `' OR 1=1 --`
   * *Payload:* `' OR 'a'='a`

2. **Logic Truncation (Commenting):**
   By injecting a known username followed by an SQL comment symbol (`--` or `#`), the database ignores the rest of the query (such as the password verification).
   * *Payload:* `admin' --`

### Remediation: Parameterized Queries
The secure endpoints demonstrate the industry standard fix: **Parameterized Queries** (or Prepared Statements).
```javascript
const query = "SELECT * FROM users WHERE username = ?";
db.all(query, [userInput], (err, rows) => { ... });
```
By using placeholders (`?`), the database strictly treats the user input as literal text, neutralizing any injected SQL commands.
