
# Phase 9: HTTP, HTTPS, and Web Networking

## 20. HTTP Fundamentals

### 20.1 What Is HTTP?

**HTTP (Hypertext Transfer Protocol)** is an application-layer protocol used for communication between clients and servers.

It defines:
- How a client requests a resource.
- How a server responds.
- How data is represented using headers and bodies.
- How status and errors are communicated.

HTTP is stateless by default: each request is independent. Applications can maintain state using cookies, sessions, tokens, or other mechanisms.

Example:

```text
Browser → HTTP request → Web server
Browser ← HTTP response ← Web server
```

HTTP commonly operates over:
- HTTP/1.1 and HTTP/2: usually TCP.
- HTTP/3: QUIC, which runs over UDP.

### 20.2 Client-Server Request-Response Model

The client initiates a request. The server processes it and returns a response.

Example:

```http
GET /products HTTP/1.1
Host: example.com
Accept: application/json
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 35

{"products":["Laptop","Keyboard"]}
```

Typical sequence:

1. Client resolves the server hostname using DNS.
2. Client establishes a transport connection.
3. For HTTPS, the client negotiates TLS.
4. Client sends an HTTP request.
5. Server processes the request.
6. Server returns an HTTP response.
7. Client interprets the response.

### 20.3 HTTP Versions

| Version | Main characteristics |
|---|---|
| HTTP/1.0 | Typically one TCP connection per request; connection reuse was not the default |
| HTTP/1.1 | Persistent connections, `Host` header, chunked transfer encoding |
| HTTP/2 | Binary framing, multiplexed streams, header compression |
| HTTP/3 | Uses QUIC over UDP; streams avoid TCP-level head-of-line blocking between independent streams |

**HTTP/1.1:** Multiple requests may reuse a connection, but pipelining was rarely used in practice.

**HTTP/2:** Multiple streams can share one connection. It reduces overhead but still runs over TCP.

**HTTP/3:** Uses QUIC, which incorporates transport security through TLS 1.3. It can improve performance on changing or lossy networks.

The protocol version alone does not determine whether a site is secure. Security also depends on TLS, application configuration, and implementation.

### 20.4 HTTP Methods

HTTP methods indicate the intended action on a resource.

| Method | Purpose | Typical use |
|---|---|---|
| `GET` | Retrieve a resource | View a profile |
| `POST` | Submit data or perform an operation | Login, create an order |
| `PUT` | Replace a resource representation | Replace profile data |
| `PATCH` | Partially modify a resource | Update one profile field |
| `DELETE` | Remove a resource | Delete a comment |
| `HEAD` | Retrieve headers without response body | Check resource metadata |
| `OPTIONS` | Discover communication options | CORS preflight, allowed methods |

Example:

```http
GET /api/users/42 HTTP/1.1
Host: example.com
```

```http
PATCH /api/users/42 HTTP/1.1
Host: example.com
Content-Type: application/json

{"displayName":"Alex"}
```

The server's actual behavior matters more than the method name. A poorly designed application might modify data through a `GET` request, which is unsafe.

### 20.5 HTTP Status Codes

Status codes are grouped by their first digit.

| Range | Category | Meaning |
|---|---|---|
| 1xx | Informational | Request processing continues |
| 2xx | Success | Request succeeded |
| 3xx | Redirection | Client may need another request |
| 4xx | Client error | Request is invalid or not permitted |
| 5xx | Server error | Server failed to fulfill a valid request |

Common codes:

| Code | Meaning |
|---|---|
| `200 OK` | Request succeeded |
| `201 Created` | Resource created |
| `202 Accepted` | Accepted for processing |
| `204 No Content` | Success without response body |
| `301 Moved Permanently` | Permanent redirect |
| `302 Found` | Temporary redirect |
| `304 Not Modified` | Cached representation can be reused |
| `400 Bad Request` | Invalid request |
| `401 Unauthorized` | Authentication is required or failed |
| `403 Forbidden` | Server refuses the request |
| `404 Not Found` | Resource not found or intentionally concealed |
| `405 Method Not Allowed` | Method not supported for the resource |
| `409 Conflict` | Request conflicts with current state |
| `415 Unsupported Media Type` | Unsupported request content type |
| `429 Too Many Requests` | Rate limit exceeded |
| `500 Internal Server Error` | Unexpected server error |
| `502 Bad Gateway` | Gateway received an invalid upstream response |
| `503 Service Unavailable` | Service temporarily unavailable |
| `504 Gateway Timeout` | Gateway timed out waiting for upstream |

A `401` does not always mean the user has no account. A `403` does not always mean the user is authenticated. Implementations can use these codes differently.

### 20.6 Request Line and Status Line

HTTP/1.1 request line:

```http
GET /login HTTP/1.1
```

It contains:
- Method: `GET`
- Request target: `/login`
- HTTP version: `HTTP/1.1`

HTTP/1.1 status line:

```http
HTTP/1.1 200 OK
```

It contains:
- HTTP version.
- Status code.
- Reason phrase.

The reason phrase is optional in newer HTTP versions and should not be relied on by applications.

### 20.7 Request and Response Headers

Headers carry metadata about a request or response.

Request example:

```http
GET /dashboard HTTP/1.1
Host: example.com
Accept: text/html
User-Agent: ExampleBrowser/1.0
Cookie: session=abc123
```

Response example:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-store
X-Content-Type-Options: nosniff
```

Headers may describe:
- Content type and length.
- Authentication.
- Caching.
- Browser behavior.
- Proxy behavior.
- Security policy.

Header names are case-insensitive. Header values may have their own case rules.

### 20.8 Request Body and Response Body

The **request body** contains data sent to the server. The **response body** contains data returned to the client.

Example request:

```http
POST /api/login HTTP/1.1
Host: example.com
Content-Type: application/json

{"username":"alex","password":"example-password"}
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"message":"Login successful"}
```

A request body is commonly used with `POST`, `PUT`, and `PATCH`. A `GET` request generally should not rely on a body because its semantics and support are not consistently defined.

### 20.9 Content-Type and Content-Length

`Content-Type` describes the media type of the message body.

Examples:

```http
Content-Type: application/json
Content-Type: text/html; charset=utf-8
Content-Type: application/x-www-form-urlencoded
Content-Type: multipart/form-data; boundary=----abc
```

`Content-Length` specifies the body length in bytes.

```http
Content-Length: 28
```

Important:
- Length is measured in bytes, not characters.
- It may be omitted when the body length is not known in advance.
- HTTP/2 and HTTP/3 do not use HTTP/1.1 chunked transfer encoding.

### 20.10 Host Header

The `Host` header identifies the target hostname and optional port in HTTP/1.1.

```http
GET / HTTP/1.1
Host: example.com
```

It allows multiple websites to share one IP address through virtual hosting.

Security relevance:
- Incorrect host validation can lead to host-header injection.
- Applications may build password-reset links from untrusted host values.
- Reverse proxies and application servers should agree on trusted hostnames.

Test only authorized targets and avoid sending malicious host values to systems you do not own.

### 20.11 Authorization Header

The `Authorization` header carries credentials or authentication information.

Basic authentication:

```http
Authorization: Basic <base64-encoded-credentials>
```

Bearer token:

```http
Authorization: Bearer <access-token>
```

Basic authentication is only Base64-encoded, not encrypted. HTTPS is essential when using it.

Bearer tokens act like credentials: anyone who obtains a valid token may be able to use it. Protect tokens from logs, URLs, screenshots, and public repositories.

### 20.12 Cookie and Set-Cookie Headers

A server sends a cookie using `Set-Cookie`:

```http
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Lax
```

The browser later sends it using `Cookie`:

```http
Cookie: session=abc123
```

`Set-Cookie` is a response header. `Cookie` is a request header.

The browser normally does not send cookie attributes such as `Secure` or `HttpOnly` back to the server.

### 20.13 Origin and Referer Headers

An **origin** is the combination of:

```text
scheme + hostname + port
```

Example:

```text
https://app.example.com:443
```

An origin does not include the path or query string.

The `Origin` header is used in cross-origin requests and security checks:

```http
Origin: https://app.example.com
```

The `Referer` header may identify the page that initiated a request:

```http
Referer: https://example.com/products
```

A browser may omit or reduce the `Referer` value because of privacy policies and the `Referrer-Policy` header.

Neither header should be treated as reliable authentication. Non-browser clients can often forge them.

### 20.14 Accept and User-Agent Headers

`Accept` describes the response media types the client can process:

```http
Accept: application/json
```

Multiple formats can be listed:

```http
Accept: text/html, application/json;q=0.9, */*;q=0.5
```

`User-Agent` identifies the client software:

```http
User-Agent: Mozilla/5.0 ...
```

User-Agent strings are not trustworthy proof of a browser, device, or user identity. They can be modified or spoofed.

### 20.15 Redirects

A redirect response tells the client to request another URL, usually through the `Location` header.

```http
HTTP/1.1 302 Found
Location: https://example.com/new-path
```

Common redirects:

| Code | Typical meaning |
|---|---|
| `301` | Permanent redirect |
| `302` | Temporary redirect |
| `303` | Redirect using a retrieval request, typically `GET` |
| `307` | Temporary redirect preserving method |
| `308` | Permanent redirect preserving method |

Security concerns:
- Open redirects can send users to attacker-controlled destinations.
- Redirect chains can leak information through URLs or referrers.
- Redirecting from HTTPS to HTTP can expose traffic.

### 20.16 Keep-Alive and Connection Reuse

Persistent connections allow multiple HTTP requests to reuse one transport connection.

HTTP/1.1 uses persistent connections by default unless the connection is closed.

```http
Connection: keep-alive
```

Connection reuse reduces:
- TCP handshake overhead.
- TLS handshake overhead.
- Latency for repeated requests.

HTTP/2 and HTTP/3 use their own connection management mechanisms; HTTP/1.1 `Connection` headers are not used in the same way.

### 20.17 Compression

HTTP responses can be compressed to reduce transferred data.

```http
Accept-Encoding: gzip, br
```

The server may respond:

```http
Content-Encoding: gzip
```

Common compression algorithms:
- gzip
- Brotli (`br`)
- Deflate

Compression can improve performance. However, compressing secrets together with attacker-controlled content in certain contexts can create side-channel risks. Security-sensitive applications should consider compression carefully.

### 20.18 Chunked Transfer Encoding

HTTP/1.1 can send a body in chunks when its total size is not known in advance.

```http
Transfer-Encoding: chunked
```

Conceptual wire format:

```text
4
Wiki
5
pedia
0
```

Each chunk begins with its size in hexadecimal. A zero-length chunk ends the body.

Important:
- Chunked transfer encoding is specific to HTTP/1.1.
- It is not used in HTTP/2 or HTTP/3.
- `Transfer-Encoding` and `Content-Length` should not be combined in conflicting ways.
- Conflicting message-length interpretations between proxies and servers can contribute to request-smuggling vulnerabilities.

### 20.19 Caching Headers

Caching stores a response so it can be reused later.

Important headers:

| Header | Purpose |
|---|---|
| `Cache-Control` | Controls caching behavior |
| `Expires` | Gives an expiration date |
| `Age` | Approximate time a response has been in a shared cache |
| `Vary` | Identifies request headers that affect the response |
| `Pragma` | Legacy cache directive |

Examples:

```http
Cache-Control: public, max-age=3600
```

Allows a response to be cached publicly for up to 3600 seconds.

```http
Cache-Control: no-store
```

Instructs caches not to store the response.

```http
Cache-Control: private, max-age=600
```

Allows private browser caching but prevents shared-cache storage.

For sensitive responses, a carefully chosen `no-store` policy is often appropriate.

### 20.20 ETags and Conditional Requests

An **ETag** is a validator for a particular representation.

```http
ETag: "v123"
```

A client can ask whether its cached representation is still current:

```http
If-None-Match: "v123"
```

If unchanged, the server can return:

```http
HTTP/1.1 304 Not Modified
```

This saves bandwidth because the body does not need to be retransmitted.

ETags should not be assumed to be secret or secure identifiers. Some applications have historically exposed information through predictable or user-specific ETags.

### 20.21 Content Negotiation

Content negotiation lets the client and server choose a representation.

Examples:

```http
Accept: application/json
Accept-Language: en-US
Accept-Encoding: br, gzip
```

The server may select:
- JSON or HTML.
- A language.
- A compression format.

The response may include:

```http
Vary: Accept, Accept-Language
```

`Vary` helps caches distinguish responses based on relevant request headers.

### 20.22 Safe vs Idempotent Methods

**Safe method:** Intended not to change the server's state.

**Idempotent method:** Repeating the same request has the same intended effect as making it once.

| Method | Safe? | Idempotent? |
|---|---|---|
| GET | Yes | Yes |
| HEAD | Yes | Yes |
| OPTIONS | Yes | Yes |
| POST | No | Not generally |
| PUT | No | Yes |
| PATCH | No, generally | Not generally |
| DELETE | No | Yes |

Idempotency does not mean that repeated responses must be identical. For example, repeated `DELETE` requests may return different status codes while leaving the resource deleted.

### 20.23 HTTP Proxies

A forward proxy acts on behalf of a client.

```text
Client → Forward Proxy → Internet Server
```

Uses:
- Network filtering.
- Traffic inspection.
- Access control.
- Privacy or routing.
- Debugging.

An HTTP proxy may receive absolute-form request targets, such as:

```http
GET http://example.com/page HTTP/1.1
```

For HTTPS, clients commonly use the `CONNECT` method to establish a tunnel through the proxy.

### 20.24 Reverse Proxies

A reverse proxy acts on behalf of one or more servers.

```text
Client → Reverse Proxy → Application Server
```

Common functions:
- TLS termination.
- Load balancing.
- Caching.
- Compression.
- Request filtering.
- Routing to backend services.

Examples of reverse-proxy software include Nginx, HAProxy, and Envoy.

Security concern: applications must correctly distinguish trusted proxy headers from headers supplied directly by clients.

### 20.25 Load Balancing

A load balancer distributes traffic among multiple servers.

```text
                 ┌→ Server A
Client → LB ─────┼→ Server B
                 └→ Server C
```

Common approaches:
- Round robin.
- Least connections.
- Weighted distribution.
- Consistent hashing.

Load balancers may use:
- Layer 4: TCP/UDP connections.
- Layer 7: HTTP requests and application information.

Session persistence, also called sticky sessions, can direct a user to the same backend. Shared session storage is often more flexible for scalable applications.

### 20.26 CDN Behavior

A **Content Delivery Network (CDN)** serves content from geographically distributed edge locations.

```text
User → CDN Edge → Origin Server
```

CDNs may cache:
- Images.
- JavaScript and CSS.
- Videos.
- Public API responses.
- Other cacheable content.

A CDN can improve latency and reduce origin-server load.

Security concerns:
- Incorrect cache rules may expose private content.
- Cache-key mistakes may mix responses between users.
- Origin servers should be protected from unauthorized direct access when appropriate.
- Cache behavior should be tested carefully for authenticated content.

---

## 21. HTTPS and TLS

### 21.1 Why HTTPS Is Needed

HTTPS is HTTP carried over a secure TLS connection.

It provides:
- Confidentiality: prevents passive observers from reading protected traffic.
- Integrity: detects unauthorized changes to protected traffic.
- Authentication: helps the client verify the server's identity.

Without HTTPS, network attackers may be able to observe or modify traffic, especially on untrusted networks.

HTTPS does not hide all metadata. An observer may still learn information such as the server IP address, connection timing, and traffic volume.

### 21.2 HTTP vs HTTPS

| HTTP | HTTPS |
|---|---|
| No TLS protection | TLS protection |
| Traffic may be readable in transit | Traffic is encrypted in transit |
| No TLS-based server authentication | Server certificate is validated |
| Commonly uses port 80 | Commonly uses port 443 |

HTTPS does not mean that the website itself is trustworthy. A phishing site can also use a valid HTTPS certificate.

### 21.3 Encryption, Integrity, and Authentication

**Encryption:** Makes data unreadable to parties without the appropriate key.

**Integrity:** Helps detect whether protected data has been changed.

**Authentication:** Verifies the identity of a communicating party, usually the server in ordinary HTTPS.

TLS normally authenticates the server. Client authentication with certificates is possible but less common on public websites.

### 21.4 Symmetric vs Asymmetric Cryptography

| Type | Description | Typical use |
|---|---|---|
| Symmetric | Same secret key is used for encryption and decryption | Efficient protection of application data |
| Asymmetric | Uses a public/private key pair | Authentication, signatures, and key establishment |

Symmetric cryptography is efficient for large amounts of data.

Asymmetric cryptography helps establish trust and secure key exchange. TLS does not normally encrypt all application data directly with a public key.

### 21.5 Public-Key Infrastructure (PKI)

PKI is a system for creating, distributing, validating, and managing digital certificates and public keys.

Main components:
- Certificate authorities (CAs).
- Digital certificates.
- Public/private key pairs.
- Trust stores.
- Certificate validation rules.
- Revocation and expiration processes.

Browsers and operating systems contain trusted root CA certificates.

### 21.6 Digital Certificates

A digital certificate binds a public key to an identity, such as a hostname.

A certificate typically includes:
- Subject or subject alternative names.
- Public key.
- Issuer.
- Validity period.
- Signature from the issuing CA.
- Key usage and extended key usage information.

Modern hostname verification primarily relies on the **Subject Alternative Name (SAN)** extension.

### 21.7 Certificate Authorities

A Certificate Authority (CA) signs certificates to establish a trust relationship.

The browser trusts a certificate when:
- The certificate is valid for the requested hostname.
- The certificate is within its validity period.
- The chain reaches a trusted root.
- The certificate's usage is appropriate.
- Other validation checks succeed.

A CA does not guarantee that a website is honest, safe, or free from vulnerabilities.

### 21.8 Certificate Chains

A typical chain:

```text
Website Certificate
       ↓ signed by
Intermediate CA
       ↓ signed by
Root CA
       ↓
Trusted by Browser / Operating System
```

The server usually sends its certificate and required intermediate certificates. The client already has or otherwise obtains a trusted root.

A missing intermediate certificate can cause certificate validation failures on some clients.

### 21.9 Certificate Expiration

Certificates have a validity period:

```text
Not Before: 2026-01-01
Not After:  2026-12-31
```

Expired certificates can cause browser warnings or connection failures.

Certificate renewal should be automated where possible and monitored.

### 21.10 Hostname Verification

The hostname in the URL must match the certificate's valid hostname entries.

Example:

```text
URL:         https://shop.example.com
Certificate: shop.example.com
```

A certificate for `example.com` does not automatically cover every subdomain. A wildcard such as `*.example.com` typically covers one subdomain level, not `a.b.example.com`.

Disabling hostname verification removes an important security control and should not be used as a production workaround.

### 21.11 TLS Handshake — Overview

A simplified TLS 1.3 handshake:

```text
Client                              Server
  |                                  |
  | -------- ClientHello ----------> |
  |                                  |
  | <------- ServerHello ----------- |
  | <--- Encrypted handshake data -- |
  |                                  |
  | -------- Finished ------------> |
  | <------- Finished ------------- |
  |                                  |
  | ===== Encrypted HTTP data ===== |
```

The handshake:
1. Negotiates protocol parameters.
2. Establishes shared cryptographic secrets.
3. Authenticates the server using its certificate and proof of private-key possession.
4. Confirms that both parties derived the correct session keys.
5. Protects subsequent application data.

This is a simplified illustration; the exact message sequence depends on TLS version and configuration.

### 21.12 TLS Versions and Secure Configurations

| Version | Notes |
|---|---|
| SSL 2.0 / SSL 3.0 | Obsolete and insecure |
| TLS 1.0 / TLS 1.1 | Deprecated; should be disabled |
| TLS 1.2 | Still widely supported when configured securely |
| TLS 1.3 | Modern version with a simplified handshake and strong default design |

Secure configuration generally means:
- Prefer TLS 1.3.
- Support TLS 1.2 when compatibility requires it.
- Disable SSL and TLS 1.0/1.1.
- Use modern cipher suites.
- Keep server and TLS libraries updated.
- Avoid insecure certificate-validation workarounds.

### 21.13 Cipher Suites — Basic Concepts

A cipher suite describes cryptographic algorithms used by a TLS connection.

In TLS 1.2, a cipher suite can specify key exchange, authentication, encryption, and integrity algorithms.

Example:

```text
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
```

Conceptually:
- `ECDHE`: ephemeral key exchange.
- `RSA`: certificate authentication.
- `AES_128_GCM`: authenticated encryption.
- `SHA256`: hash used in the suite's key derivation or related functions.

TLS 1.3 cipher-suite names are simpler because key exchange and authentication are negotiated separately.

### 21.14 Key Exchange and Forward Secrecy

Key exchange allows client and server to derive shared secrets.

**Forward secrecy** means that compromise of a server's long-term private key does not normally allow an attacker to decrypt previously recorded sessions.

Ephemeral Diffie-Hellman methods such as ECDHE are commonly used to provide forward secrecy.

### 21.15 SNI — Server Name Indication

SNI is a TLS extension that lets the client indicate the hostname it wants to connect to during the TLS handshake.

This allows multiple HTTPS websites to share an IP address while presenting the correct certificate.

SNI is traditionally sent in the ClientHello and may be visible to network observers. Encrypted ClientHello (ECH) is designed to protect more of this information where supported.

### 21.16 ALPN — Application-Layer Protocol Negotiation

ALPN allows the client and server to negotiate the application protocol during TLS setup.

Examples:

```text
http/1.1
h2
```

ALPN allows a server to choose HTTP/1.1 or HTTP/2 without a separate application-layer negotiation.

HTTP/3 uses QUIC and negotiates its protocol through mechanisms associated with QUIC and TLS 1.3.

### 21.17 HSTS

**HTTP Strict Transport Security (HSTS)** instructs browsers to use HTTPS for a site.

Example:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

Meaning:
- `max-age`: duration in seconds.
- `includeSubDomains`: applies to subdomains.

HSTS helps prevent downgrade attacks and accidental HTTP access.

Important:
- Browsers only learn HSTS from a secure HTTPS response.
- HSTS does not fix application vulnerabilities.
- `includeSubDomains` should be used only when all covered subdomains support HTTPS.
- HSTS preload is a separate browser-list mechanism.

### 21.18 Mixed Content

Mixed content occurs when an HTTPS page loads resources over HTTP.

Examples:
- An HTTPS page loading an HTTP image.
- An HTTPS page loading an HTTP script.
- An HTTPS page submitting data to an HTTP endpoint.

Active mixed content, such as scripts, is especially dangerous because it can compromise the secure page.

Browsers block many forms of mixed content or attempt to upgrade certain requests to HTTPS.

### 21.19 Certificate Errors and Troubleshooting

Common causes:
- Expired certificate.
- Hostname mismatch.
- Missing intermediate certificate.
- Untrusted CA.
- Incorrect system clock.
- TLS version or cipher mismatch.
- Intercepting proxy using an untrusted certificate.

Troubleshooting checklist:

1. Confirm the URL hostname.
2. Check system date and time.
3. Inspect the certificate's validity period.
4. Verify the hostname against SAN entries.
5. Inspect the certificate chain.
6. Check supported TLS versions.
7. Review server and proxy configuration.
8. Avoid disabling certificate validation as a workaround.

### 21.20 TLS Termination at Reverse Proxies

TLS may terminate at a reverse proxy:

```text
Browser
   | HTTPS
   v
Reverse Proxy
   | HTTP or HTTPS
   v
Application Server
```

If the proxy uses HTTP to communicate with the backend, traffic inside that network is not encrypted.

Security considerations:
- Use HTTPS between proxy and backend when appropriate.
- Restrict backend access.
- Trust forwarded headers only from known proxies.
- Ensure the application knows the original request scheme.
- Prevent users from directly accessing internal application servers.

### 21.21 Why HTTPS Does Not Automatically Make an Application Secure

HTTPS protects data in transit. It does not prevent:
- SQL injection.
- Cross-site scripting (XSS).
- Broken access control.
- Insecure direct object references (IDOR).
- Weak authentication.
- Session fixation.
- Business logic flaws.
- Insecure file uploads.
- Sensitive data exposure by the application.

A secure application needs transport security plus secure coding, authentication, authorization, validation, and configuration.

---

## 22. Cookies, Sessions, and Browser Networking

### 22.1 Cookies vs Server-Side Sessions

A cookie is a small value stored by the browser and sent with matching requests.

A server-side session stores user state on the server. The browser commonly stores only a session identifier.

```text
Browser Cookie: session_id=abc123
                  |
                  v
Server Session Store:
abc123 → user_id=42, authenticated=true
```

Cookies are not necessarily sessions. They can store preferences or other small values.

### 22.2 Session IDs

A session ID identifies a session.

Good session IDs should:
- Be generated using a cryptographically secure random generator.
- Have sufficient entropy.
- Be unpredictable.
- Be transmitted over HTTPS.
- Be invalidated at logout or expiration.
- Be rotated after authentication or privilege changes.

Do not place session IDs in URLs because URLs can leak through logs, browser history, and referrer information.

### 22.3 Secure Cookie Attribute

```http
Set-Cookie: session=abc; Secure
```

`Secure` tells the browser to send the cookie only over secure channels, normally HTTPS.

It helps prevent session cookies from being sent over plaintext HTTP.

### 22.4 HttpOnly Cookie Attribute

```http
Set-Cookie: session=abc; HttpOnly
```

`HttpOnly` prevents JavaScript from reading the cookie through browser APIs such as `document.cookie`.

It reduces the risk of session-cookie theft through certain XSS attacks, but it does not prevent XSS itself. Malicious JavaScript may still perform actions as the user.

### 22.5 SameSite Cookie Attribute

`SameSite` controls when cookies are sent in cross-site contexts.

| Value | General behavior |
|---|---|
| `Strict` | Cookie is withheld from most cross-site requests |
| `Lax` | Cookie is sent in some top-level cross-site navigations |
| `None` | Cookie can be sent in cross-site contexts; requires `Secure` in modern browsers |

Example:

```http
Set-Cookie: session=abc; Secure; HttpOnly; SameSite=Lax
```

`SameSite` can help reduce CSRF risk, but it is not a complete replacement for CSRF protections.

### 22.6 Cookie Scope and Domain

Example:

```http
Set-Cookie: session=abc; Path=/; Domain=example.com
```

- `Domain` controls which hosts may receive the cookie.
- `Path` limits the URL path scope.
- Omitting `Domain` creates a host-only cookie.
- A cookie with `Domain=example.com` may be sent to eligible subdomains.

Broad domain scope can increase risk if subdomains are less trusted.

The `__Host-` cookie prefix imposes stricter browser requirements: the cookie must be `Secure`, have `Path=/`, and must not have a `Domain` attribute.

### 22.7 Browser Origin

An origin consists of:

```text
scheme + hostname + port
```

Examples:

```text
https://example.com
https://example.com:8443
http://example.com
```

These are different origins because the scheme or port differs.

The origin is not the same as the site's registrable domain. Browser concepts of “site” and “origin” are distinct and affect cookies, CORS, and CSRF.

### 22.8 Same-Origin Policy (SOP)

The Same-Origin Policy is a browser security mechanism that restricts how documents and scripts from one origin interact with resources from another.

It helps prevent a malicious website from freely reading sensitive data from another website in the victim's browser.

SOP does not block every cross-origin request. For example, browsers can load images or submit some forms cross-origin. It primarily controls access to cross-origin responses and documents.

### 22.9 CORS

**Cross-Origin Resource Sharing (CORS)** is a browser mechanism that allows a server to specify which origins may read its responses.

Example response:

```http
Access-Control-Allow-Origin: https://app.example.com
```

A server may allow certain methods:

```http
Access-Control-Allow-Methods: GET, POST, PUT
```

CORS is not authentication or authorization. It primarily governs browser access to cross-origin responses.

A non-browser client such as `curl` is not constrained by browser CORS enforcement.

### 22.10 Preflight Requests

A browser may send a preflight request before a cross-origin request that does not qualify as a simple request.

Example:

```http
OPTIONS /api/profile HTTP/1.1
Host: api.example.com
Origin: https://app.example.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type, authorization
```

The server may respond:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, PUT
Access-Control-Allow-Headers: Content-Type, Authorization
```

The browser then decides whether to send the actual request.

Preflight behavior depends on the method, headers, and content type.

### 22.11 CSRF Fundamentals

**Cross-Site Request Forgery (CSRF)** tricks a browser into sending an unwanted request to a site where the user is already authenticated.

Example:
1. User logs in to a banking website.
2. The browser stores an authentication cookie.
3. User visits an attacker-controlled page.
4. The page causes a request to the bank.
5. If the browser sends the cookie and the bank lacks suitable defenses, the action may succeed.

Common defenses:
- CSRF tokens.
- `SameSite` cookies.
- Origin or Referer validation.
- Re-authentication for sensitive actions.
- Avoiding state-changing operations through `GET`.

CSRF is primarily relevant when browsers automatically attach authentication credentials, such as cookies.

### 22.12 Browser Cache

The browser cache stores resources for reuse.

Common cached resources:
- Images.
- CSS.
- JavaScript.
- Fonts.
- Some API responses.

Cache policy can be controlled through headers such as:

```http
Cache-Control: max-age=3600
```

For sensitive pages, developers should avoid unintentionally storing private information in shared or persistent caches.

### 22.13 Local Storage vs Session Storage

| Feature | Local Storage | Session Storage |
|---|---|---|
| Lifetime | Persists until cleared | Usually lasts for the tab's page session |
| Scope | Origin | Origin and top-level browsing context |
| Automatically sent to server? | No | No |
| Accessible to JavaScript? | Yes | Yes |

Security considerations:
- JavaScript can read both.
- XSS may expose stored tokens or sensitive data.
- Do not assume storage is encrypted.
- Cookie-based sessions with suitable attributes may be more appropriate for some applications.

### 22.14 WebSockets and the Upgrade Handshake

WebSockets provide persistent, bidirectional communication.

A typical connection begins with an HTTP/1.1 upgrade request:

```http
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <random-value>
Sec-WebSocket-Version: 13
Origin: https://app.example.com
```

The server accepts the upgrade:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: <computed-value>
```

After the handshake, the connection carries WebSocket frames.

Secure WebSockets use `wss://`, while unencrypted WebSockets use `ws://`.

HTTP/2 and HTTP/3 support WebSockets through mechanisms different from the classic HTTP/1.1 upgrade flow.

### 22.15 WebSockets Security Basics

Important controls:
- Validate the `Origin` header for browser clients.
- Authenticate the connection.
- Authorize each sensitive message or operation.
- Validate message format and size.
- Apply rate limits.
- Handle session expiration and logout.
- Avoid logging tokens or sensitive message content.

A successful WebSocket handshake does not mean every message is authorized.

### 22.16 Browser Developer Tools: Network Tab

The browser Network tab helps inspect HTTP traffic.

Useful information:
- Request URL and method.
- Status code.
- Request and response headers.
- Cookies.
- Request and response bodies.
- Timing.
- Initiator.
- Redirects.
- Cached responses.

Practical workflow:

1. Open browser developer tools.
2. Select the Network tab.
3. Enable Preserve log if needed.
4. Reload the page.
5. Select a request.
6. Inspect Headers, Payload, Response, and Timing.
7. Compare requests before and after an action.

For security testing, inspect only applications and accounts you are authorized to test.

### 22.17 Request Timing and Waterfall Diagrams

A waterfall shows how requests occur over time.

Typical stages may include:
- Queueing or stalled time.
- DNS lookup.
- TCP connection.
- TLS handshake.
- Request transmission.
- Waiting for response (often called TTFB).
- Response download.

Example:

```text
Request A: | DNS | TCP | TLS | Request | Wait | Download |
Request B:                         | Request | Wait | Download |
```

Waterfalls help identify:
- Slow DNS.
- Connection setup delays.
- Backend latency.
- Large response bodies.
- Blocking or sequential dependencies.

Exact timing categories vary by browser and protocol.

### 22.18 Redirect Chains

A redirect chain contains multiple redirects before the final response.

```text
/page
  → /login
  → /auth
  → /dashboard
```

Long chains can:
- Increase latency.
- Complicate authentication.
- Create confusing caching behavior.
- Reveal sensitive information if URLs contain secrets.

Inspect each response's status code and `Location` header.

### 22.19 Third-Party Requests and External Resources

A webpage may load resources from other origins:
- Analytics.
- Advertising.
- Fonts.
- JavaScript libraries.
- Video platforms.
- Payment providers.

Risks:
- Third-party scripts may execute with the page's privileges.
- Requests may reveal browsing metadata.
- External resources may be compromised.
- Incorrect CORS or CSP configuration may increase exposure.

Useful defenses:
- Minimize third-party dependencies.
- Use Content Security Policy (CSP).
- Keep dependencies updated.
- Use Subresource Integrity (SRI) for suitable static resources.
- Avoid sending unnecessary personal data to third parties.

---

## 23. Web Architecture and API Networking

### 23.1 Frontend vs Backend

**Frontend:**
- Runs in the browser or client.
- Displays UI.
- Collects user input.
- Sends requests to backend services.

**Backend:**
- Runs on servers.
- Applies business logic.
- Performs authentication and authorization.
- Reads or writes data.
- Communicates with other services.

```text
Browser / Frontend
        |
        | HTTPS / API
        v
Backend Application
        |
        v
Database
```

Frontend validation improves user experience but is not a security boundary. The backend must validate and authorize requests independently.

### 23.2 Web Server vs Application Server

A **web server** commonly handles HTTP connections and serves static files or forwards requests.

An **application server** executes application logic.

Example:

```text
Client
  |
  v
Nginx (Web Server / Reverse Proxy)
  |
  v
Python Application (Flask / Django / FastAPI)
  |
  v
Database
```

The roles may overlap. Many application frameworks include their own HTTP servers, while production deployments often use a reverse proxy or gateway in front.

### 23.3 Reverse Proxy Architecture

A reverse proxy receives client requests and routes them to backend services.

```text
                  ┌→ Frontend Service
Browser → Proxy ──┼→ API Service
                  └→ Authentication Service
```

Benefits:
- Centralized TLS.
- Routing.
- Load balancing.
- Rate limiting.
- Request filtering.
- Logging and monitoring.

Security concerns:
- Trust boundaries must be clear.
- Forwarded headers must be sanitized or trusted only from known proxies.
- Internal services should not be unnecessarily exposed.
- Authentication and authorization must still be enforced by the application.

### 23.4 Application-to-Database Communication

The backend typically communicates with the database over a private network or local connection.

```text
Client → API → Application → Database
```

The browser should not connect directly to a private application database.

Security practices:
- Use parameterized queries.
- Apply least-privilege database accounts.
- Keep credentials out of source code.
- Encrypt connections when needed.
- Restrict database network access.
- Avoid returning raw database errors to clients.

### 23.5 REST APIs

REST is an architectural style often used for HTTP APIs.

Example resource:

```text
/api/users/42
```

Common operations:

| Method | Endpoint | Example intent |
|---|---|---|
| GET | `/api/users` | List users |
| GET | `/api/users/42` | Retrieve user 42 |
| POST | `/api/users` | Create a user |
| PUT | `/api/users/42` | Replace user 42 |
| PATCH | `/api/users/42` | Update part of user 42 |
| DELETE | `/api/users/42` | Delete user 42 |

REST does not automatically make an API secure. Each operation needs proper authentication, authorization, validation, and rate limiting.

### 23.6 JSON and XML Payloads

JSON example:

```json
{
  "userId": 42,
  "name": "Alex",
  "active": true
}
```

Request header:

```http
Content-Type: application/json
```

XML example:

```xml
<user>
  <userId>42</userId>
  <name>Alex</name>
  <active>true</active>
</user>
```

XML uses tags and attributes. JSON uses objects, arrays, and primitive values.

Security concerns:
- Validate data types and lengths.
- Reject unexpected fields where appropriate.
- Avoid unsafe XML external entity processing (XXE).
- Do not assume JSON input is trustworthy simply because it is structured.

### 23.7 API Authentication

APIs commonly authenticate requests using:
- Session cookies.
- API keys.
- Bearer access tokens.
- OAuth access tokens.
- Mutual TLS in some service environments.

Authentication asks:

> Who or what is making this request?

Authorization asks:

> Is this identity allowed to perform this action on this resource?

Authentication without authorization can still result in broken access control.

### 23.8 API Keys and Bearer Tokens

API key example:

```http
X-API-Key: <api-key>
```

Bearer token example:

```http
Authorization: Bearer <access-token>
```

API keys often identify an application or client. Bearer tokens commonly represent delegated access or an authenticated session.

Security practices:
- Use HTTPS.
- Store secrets securely.
- Rotate credentials when needed.
- Apply scopes and permissions.
- Avoid embedding secret keys in public frontend code.
- Avoid placing tokens in URLs.
- Redact credentials from logs.

A key embedded in browser JavaScript cannot be treated as secret.

### 23.9 OAuth 2.0 and OpenID Connect — Fundamentals

**OAuth 2.0** is an authorization framework. It allows a client to obtain limited access to resources.

Common roles:
- Resource owner.
- Client.
- Authorization server.
- Resource server.

**OpenID Connect (OIDC)** is an identity layer built on OAuth 2.0. It provides authentication information, including an ID token.

Important distinction:
- OAuth access token: used to access protected resources.
- OIDC ID token: conveys authentication information to the client.

For browser and mobile applications, Authorization Code Flow with PKCE is commonly recommended.

Security concepts:
- `state` helps protect against request forgery in the authorization flow.
- `nonce` helps bind an ID token to an authentication request.
- PKCE protects authorization-code exchange from interception.
- Redirect URIs must be validated strictly.

### 23.10 JWT Structure and Validation — Fundamentals

A JSON Web Token (JWT) commonly has three Base64URL-encoded parts:

```text
header.payload.signature
```

Example structure:

```text
xxxxx.yyyyy.zzzzz
```

Header example:

```json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

Payload example:

```json
{
  "sub": "42",
  "role": "user",
  "exp": 1900000000
}
```

A JWT payload is usually encoded, not encrypted. Anyone holding the token may be able to decode its contents.

Validation should include:
- Verify the signature.
- Allow only expected algorithms.
- Validate issuer (`iss`).
- Validate audience (`aud`).
- Validate expiration (`exp`).
- Validate not-before (`nbf`) when present.
- Apply appropriate application authorization checks.

Do not trust a token's payload merely because it is syntactically valid.

### 23.11 GraphQL — Basic Networking and Request Structure

GraphQL APIs commonly expose one endpoint, such as:

```text
/graphql
```

A query may be sent using a JSON POST body:

```http
POST /graphql HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "query": "query { user(id: 42) { id name } }"
}
```

GraphQL allows clients to request selected fields.

Security considerations:
- Authorization must be checked for each relevant object and field.
- Limit query depth and complexity.
- Apply rate limits.
- Avoid exposing unnecessary schema information in production.
- Prevent expensive nested queries from exhausting resources.

### 23.12 Rate Limiting

Rate limiting restricts how often a client can perform an operation.

Example response:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
```

Rate limits may be based on:
- IP address.
- User account.
- API key.
- Endpoint.
- Resource or operation.

Rate limiting helps protect against abuse, brute force, and resource exhaustion. It should be designed carefully to avoid unfairly blocking legitimate users behind shared IP addresses.

### 23.13 API Gateways

An API gateway is an entry point for API traffic.

Common responsibilities:
- Routing.
- Authentication integration.
- Rate limiting.
- Request and response transformation.
- Logging.
- API version routing.
- Monitoring.

A gateway can centralize some controls, but the backend should not assume every request is safe simply because it passed through the gateway.

### 23.14 Webhooks

A webhook is an HTTP request sent by one service to notify another service about an event.

Example:

```http
POST /webhooks/payment HTTP/1.1
Host: merchant.example
Content-Type: application/json

{
  "event": "payment.completed",
  "paymentId": "p_123"
}
```

Security practices:
- Verify the sender's signature.
- Use a timestamp to reduce replay risk.
- Validate the payload.
- Make event processing idempotent.
- Avoid trusting a webhook solely because it contains a particular event name.
- Keep webhook secrets private.

### 23.15 Service-to-Service Communication

Backend services communicate using protocols such as:
- HTTP/HTTPS.
- gRPC.
- Message queues.
- Database protocols.

Security measures:
- Authenticate services.
- Authorize service actions.
- Use TLS or mutual TLS where appropriate.
- Apply least privilege.
- Validate incoming data.
- Monitor service identity and access.

Internal network location alone should not be considered sufficient proof of trust.

### 23.16 API Versioning

API versioning helps manage changes without breaking existing clients.

Common patterns:

```text
/api/v1/users
/api/v2/users
```

Or through headers:

```http
Accept: application/vnd.example.v2+json
```

Versioning considerations:
- Avoid maintaining insecure old versions indefinitely.
- Document deprecation schedules.
- Apply security fixes consistently.
- Ensure old endpoints do not bypass newer authorization rules.

### 23.17 Timeouts and Retries

A timeout limits how long a client waits for a response.

Common timeout types:
- Connection timeout.
- TLS handshake timeout.
- Request or response timeout.
- Read timeout.
- Overall deadline.

Retries can improve reliability but may cause duplicate operations.

For operations that create payments, orders, or other state, use idempotency mechanisms where appropriate.

Example:

```http
POST /api/payments HTTP/1.1
Idempotency-Key: 9c3d-example-key
```

A server can use the key to recognize repeated attempts and avoid processing the same operation more than once.

### 23.18 Connection Pooling

Connection pooling reuses established connections instead of creating a new connection for every request.

Benefits:
- Reduced connection setup overhead.
- Lower latency.
- Reduced resource consumption.

Pools may be used for:
- Database connections.
- HTTP client connections.
- Service-to-service communication.

Security and reliability considerations:
- Set pool limits.
- Use appropriate timeouts.
- Avoid leaking connections.
- Ensure connections are not reused across incompatible security contexts.

### 23.19 Common API Security Misconfigurations

Common problems include:

1. Missing authentication.
2. Broken object-level authorization.
3. Broken function-level authorization.
4. Excessive data exposure.
5. Mass assignment.
6. Weak rate limiting.
7. Incorrect CORS configuration.
8. API keys exposed in frontend code.
9. Debug endpoints exposed publicly.
10. Verbose error messages.
11. Unsafe file uploads.
12. Missing input validation.
13. Insecure JWT validation.
14. Unrestricted GraphQL queries.
15. Webhook signature not verified.
16. Sensitive data stored in URLs or logs.
17. Old API versions left unprotected.
18. Trusting client-supplied role or user IDs.

For authorized testing, focus on identifying the security boundary and verifying whether the server enforces it—not merely whether the frontend hides a feature.

---

## Practical Lab: Inspect HTTP and HTTPS

Use a website or local lab that you are authorized to inspect.

### Lab 1: Inspect HTTP Headers with curl

```bash
curl -I https://example.com
```

`-I` requests headers only.

Follow redirects:

```bash
curl -I -L https://example.com
```

Verbose TLS and connection information:

```bash
curl -v https://example.com
```

### Lab 2: Send a JSON Request

```bash
curl -i \
  -X POST \
  https://example.com/api/test \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex"}'
```

Replace the URL with an endpoint you are authorized to test.

### Lab 3: Inspect TLS Certificate Information

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Useful observations:
- Certificate subject and issuer.
- Certificate chain.
- Negotiated TLS version.
- Negotiated cipher.
- Verification result.

### Lab 4: Use Browser Developer Tools

1. Open a website you are allowed to inspect.
2. Open Developer Tools → Network.
3. Reload the page.
4. Select the main document request.
5. Inspect the request and response headers.
6. Inspect cookies and redirects.
7. Open the Timing tab.
8. Identify which requests are cached.

### Lab 5: Understand a Cookie

Inspect a response containing:

```http
Set-Cookie: session=abc; Secure; HttpOnly; SameSite=Lax; Path=/
```

Explain:
- Why `Secure` matters.
- Why `HttpOnly` matters.
- How `SameSite` affects cross-site requests.
- Why a session ID should be unpredictable.
- Why a cookie should not be treated as authorization by itself.

### Lab 6: Build a Local HTTP Request

Create a local Python HTTP server:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"Hello from the server"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = HTTPServer(("127.0.0.1", 8000), Handler)
print("Listening on http://127.0.0.1:8000")
server.serve_forever()
```

Run it:

```bash
python server.py
```

Then:

```bash
curl -i http://127.0.0.1:8000
```

Observe the status line, headers, and response body.

---

## Quick Revision

- HTTP is an application-layer request-response protocol.
- HTTP/1.1 uses persistent connections; HTTP/2 multiplexes streams over TCP; HTTP/3 uses QUIC over UDP.
- Methods describe intended operations; status codes describe the outcome.
- Headers carry metadata; bodies carry content.
- `Content-Type` describes body format; `Content-Length` describes its byte length.
- Cookies are browser-stored values; sessions commonly store state on the server.
- HTTPS uses TLS to provide confidentiality, integrity, and server authentication.
- Certificates bind public keys to hostnames through a CA trust chain.
- HSTS instructs browsers to use HTTPS.
- SOP restricts cross-origin access; CORS grants controlled browser access to selected cross-origin responses.
- CSRF exploits automatically attached credentials; XSS can execute attacker-controlled scripts in a page.
- JWTs are commonly signed, not encrypted.
- Authentication identifies a user; authorization determines what the user may do.
- A reverse proxy routes requests to backend services.
- API security requires server-side validation, authorization, rate limiting, and secure configuration.

## Interview Questions

1. What is HTTP, and why is it stateless?
2. Explain the client-server request-response model.
3. What are the differences between HTTP/1.1, HTTP/2, and HTTP/3?
4. Explain GET vs POST.
5. What is the difference between safe and idempotent methods?
6. What is the difference between `401` and `403`?
7. What are request and response headers?
8. What is the purpose of the `Host` header?
9. Explain cookies and server-side sessions.
10. What is the difference between `Secure` and `HttpOnly`?
11. Explain `SameSite` cookie behavior.
12. What is the Same-Origin Policy?
13. What is CORS, and why is it not authentication?
14. What is a CORS preflight request?
15. Explain CSRF and common defenses.
16. What is HTTPS, and what does TLS provide?
17. What is a certificate chain?
18. What are SNI and ALPN?
19. What is HSTS?
20. What is TLS termination at a reverse proxy?
21. What is a JWT, and how should it be validated?
22. Explain OAuth 2.0 vs OpenID Connect.
23. What is an API gateway?
24. What is a webhook, and how can it be secured?
25. What is broken object-level authorization?
26. How would you inspect an HTTP request in browser developer tools?
27. What is HTTP request smuggling at a high level?
28. Why does HTTPS not make an application automatically secure?
