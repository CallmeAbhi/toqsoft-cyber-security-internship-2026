const express = require('express');
const app = express();

// 1. Vulnerable Route
app.get('/vulnerable', (req, res) => {
    // It takes what you type in the URL, and puts it directly into the HTML
    const name = req.query.name || "Guest";
    res.send(`<h1>Hello, ${name}</h1>`); 
});

// 2. Secure Route
app.get('/secure', (req, res) => {
    const name = req.query.name || "Guest";
    // This replaces dangerous characters with safe HTML codes
    const safeName = String(name).replace(/</g, '&lt;').replace(/>/g, '&gt;');
    res.send(`<h1>Hello, ${safeName}</h1>`); 
});

app.listen(3001, () => {
    console.log('XSS Server running on http://localhost:3001');
});