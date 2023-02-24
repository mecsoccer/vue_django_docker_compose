const express = require("express");
const http = require("http");
const dotenv = require("dotenv");
const cors = require("cors");
const path = require("path");

dotenv.config();

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

app.use(express.static(path.join(__dirname, "build")));

app.get("/*", (req, res) => {
    res.sendFile(path.join(__dirname, "dist", "index.html"));
});

const port = process.env.PORT || "8080";
app.set("port", port);

const server = http.createServer(app);
server.listen(port, "0.0.0.0");

console.log("server listening at:", port);

module.exports = server;
