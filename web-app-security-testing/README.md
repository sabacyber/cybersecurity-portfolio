Web Application Security Testing Lab
This project demonstrates hands-on testing of common web application vulnerabilities using an intentionally vulnerable application.
The lab environment uses OWASP Juice Shop and security testing tools to analyze authentication flows and identify vulnerabilities.
Lab Environment
Tools used in this lab:
OWASP Juice Shop
Burp Suite
Kali Linux
Docker
Firefox browser
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
3. Cross-Site Scripting (XSS)
A malicious script was injected through the search feature.
Payload used:
<script>alert("XSS")</script>
Result:
The browser executed the injected script, demonstrating a Cross-Site Scripting vulnerability.
Evidence
4. JWT Authentication Token Analysis
After successful login, the server returned a JSON Web Token (JWT) used for authentication.
Example response:
{
 "authentication": {
   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
 }
}
Evidence
Security Impact
These vulnerabilities can allow attackers to:
bypass authentication
execute malicious scripts in user browsers
intercept authentication data
manipulate application requests
Skills Demonstrated
This project demonstrates practical skills in:
web application security testing
HTTP request interception
vulnerability analysis
authentication flow analysis
security documentation
Outcome
This lab provides hands-on experience with common web application vulnerabilities and demonstrates how security professionals test and document security flaws.
