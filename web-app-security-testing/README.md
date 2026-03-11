Web Application Security Testing Lab
This project demonstrates hands-on testing of common web application vulnerabilities using an intentionally vulnerable application.
The testing environment uses OWASP Juice Shop together with security tools to analyze authentication flows and identify vulnerabilities.
Lab Environment
Tools used in this lab:
OWASP Juice Shop
Burp Suite
Kali Linux
Docker
Firefox Browser
Lab Architecture
Firefox (Kali Linux)
        ↓
Burp Suite Proxy (127.0.0.1:8080)
        ↓
OWASP Juice Shop
        ↓
Docker Container
1. Intercepting Login Requests
Using Burp Suite, the login request was intercepted to analyze how authentication data is transmitted between the browser and the server.
Example request:
POST /rest/user/login HTTP/1.1
Host: 192.168.x.x:3000
Content-Type: application/json
Request body:
{
 "email": "test@test.com",
 "password": "Password123!"
}
Evidence
2. SQL Injection – Authentication Bypass
A SQL injection payload was entered into the login form:
' OR 1=1 --
This payload manipulates the backend SQL query, allowing authentication to succeed without knowing the correct password.
Result:
The application logged in as the administrator account.
Evidence
