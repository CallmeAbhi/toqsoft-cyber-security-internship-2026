const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();

// Serve static files (like your HTML) from the current folder
app.use(express.static(__dirname));

// Create an in-memory database (erases when the server stops)
const db = new sqlite3.Database(':memory:');

// Create a table and add a dummy admin user
db.serialize(() => {
    db.run("CREATE TABLE users (id INT, username TEXT, password TEXT)");
    db.run("INSERT INTO users VALUES (1, 'admin', 'supersecretpassword')");
});

// 🔴 VULNERABLE ENDPOINT: Direct String Concatenation
app.get('/vulnerable-login', (req, res) => {
    const user = req.query.username;
    
    // The Vulnerability: Pasting user input directly into the query
    const query = "SELECT * FROM users WHERE username = '" + user + "'";
    
    db.all(query, [], (err, rows) => {
        if (err) res.send("Database Error: " + err.message);
        else if (rows.length > 0) res.send("✅ Logged in successfully as: " + rows[0].username);
        else res.send("❌ Invalid username");
    });
});

// 🟢 SECURE ENDPOINT: Parameterized Queries
app.get('/secure-login', (req, res) => {
    const user = req.query.username;
    
    // The Fix: Using a '?' placeholder. The database treats input as pure text, not code.
    const query = "SELECT * FROM users WHERE username = ?";
    
    db.all(query, [user], (err, rows) => {
        if (err) res.send("Database Error: " + err.message);
        else if (rows.length > 0) res.send("✅ Logged in successfully as: " + rows[0].username);
        else res.send("❌ Invalid username");
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Backend server running on http://localhost:3000');
});