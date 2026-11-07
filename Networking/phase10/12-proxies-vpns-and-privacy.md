
# Phase 10: Proxies, VPNs, and Privacy

## 24. Proxy Servers

### 24.1 What Is a Proxy Server?

A **proxy server** is an intermediary between a client and another server.

Instead of communicating directly with the destination, the client sends its request through a proxy.

Basic architecture:

```text
Client → Proxy Server → Destination Server
```

The proxy receives the request, processes or forwards it, and returns the response to the client.

Common purposes:
- Traffic filtering.
- Access control.
- Monitoring and logging.
- Caching.
- Hiding the client's IP address from the destination.
- Security testing.
- Load balancing and traffic routing.

A proxy does not automatically provide encryption or anonymity. Its protection depends on its type and configuration.

### 24.2 Forward Proxy

A **forward proxy** acts on behalf of clients.

Architecture:

```text
Client
   |
   v
Forward Proxy
   |
   v
Internet Server
```

Example:

An organization configures its employees' computers to access the internet through a corporate proxy.

The proxy can:
- Allow or block websites.
- Monitor outbound requests.
- Apply access policies.
- Cache frequently requested content.
- Hide internal client IP addresses from external servers.

Common uses:
- Corporate internet access.
- Network filtering.
- Privacy.
- Controlled outbound access.

### 24.3 Reverse Proxy

A **reverse proxy** acts on behalf of backend servers.

Architecture:

```text
             ┌── Application Server 1
Client → RP ─┼── Application Server 2
             └── Application Server 3
```

The client communicates with the reverse proxy instead of directly accessing the backend.

Common functions:
- Load balancing.
- TLS termination.
- Request routing.
- Caching.
- Compression.
- Rate limiting.
- Web application firewall integration.

Examples:
- Nginx.
- HAProxy.
- Envoy.
- Apache HTTP Server.

**Security relevance:**

A reverse proxy creates a trust boundary. The backend must know which headers and connection details genuinely come from the trusted proxy.

### 24.4 Transparent Proxy

A **transparent proxy** intercepts or forwards network traffic without requiring the client to explicitly configure a conventional proxy.

Architecture:

```text
Client → Network Gateway / Transparent Proxy → Internet
```

The client may not know that its traffic is passing through the proxy.

Common uses:
- Enterprise traffic monitoring.
- ISP traffic management.
- Content filtering.
- Network policy enforcement.

Transparent proxies may operate at different network layers.

Important: Transparent does not mean invisible in every circumstance. Applications and network diagnostics may detect interception or modified traffic.

### 24.5 HTTP Proxy

An HTTP proxy understands HTTP requests and can forward them to destination servers.

Example:

```text
Browser → HTTP Proxy → Web Server
```

A client can send an absolute URL to an HTTP proxy:

```http
GET http://example.com/page HTTP/1.1
Host: example.com
```

For HTTPS, clients commonly use the `CONNECT` method to establish a tunnel.

Example:

```http
CONNECT example.com:443 HTTP/1.1
Host: example.com:443
```

The proxy may respond:

```http
HTTP/1.1 200 Connection Established
```

The client can then perform the TLS handshake through the tunnel.

Without TLS interception, the proxy generally cannot read the encrypted HTTPS application content.

### 24.6 SOCKS4 vs SOCKS5

SOCKS is a protocol that allows clients to route connections through a proxy.

| Feature | SOCKS4 | SOCKS5 |
|---|---|---|
| TCP support | Yes | Yes |
| UDP support | No | Yes |
| Authentication | Basic limitations | Supports authentication methods |
| IPv4 | Yes | Yes |
| IPv6 | No | Yes |
| Domain-name support | Limited; SOCKS4a extension | Yes |
| Flexibility | Limited | More flexible |

**SOCKS4:**
- Primarily supports TCP connections.
- Does not natively support IPv6.
- Has limited authentication capabilities.

**SOCKS5:**
- Supports TCP and UDP.
- Supports IPv4, IPv6, and domain names.
- Supports authentication negotiation.
- Can be used by many applications beyond web browsers.

SOCKS5 does not automatically encrypt traffic. It provides proxy routing, not VPN-style encryption.

### 24.7 Proxy Authentication

A proxy may require credentials before allowing a client to use it.

Example:

```http
HTTP/1.1 407 Proxy Authentication Required
Proxy-Authenticate: Basic realm="Corporate Proxy"
```

The client may respond with:

```http
Proxy-Authorization: Basic <base64-credentials>
```

Important headers:

| Header | Purpose |
|---|---|
| `Proxy-Authenticate` | Advertises proxy authentication methods |
| `Proxy-Authorization` | Carries credentials to the proxy |

The `407 Proxy Authentication Required` status is different from `401 Unauthorized`, which is used for origin-server authentication.

Security considerations:
- Use encrypted connections to the proxy when credentials need protection.
- Avoid hardcoding proxy credentials.
- Do not expose credentials in logs or scripts.
- Prefer secure authentication mechanisms over Basic authentication where possible.

### 24.8 Proxy Headers

Proxies may add headers to communicate information about the original client and request.

Common headers:

**X-Forwarded-For**

```http
X-Forwarded-For: 203.0.113.10
```

Can contain the original client IP address and intermediate proxy addresses.

**X-Forwarded-Host**

```http
X-Forwarded-Host: example.com
```

Indicates the original host requested by the client.

**X-Forwarded-Proto**

```http
X-Forwarded-Proto: https
```

Indicates the original request scheme.

**Forwarded**

The standardized `Forwarded` header can carry similar information:

```http
Forwarded: for=203.0.113.10;proto=https;host=example.com
```

Important security point:

These headers are not inherently trustworthy. A client can send them directly unless a trusted proxy removes or overwrites untrusted values.

### 24.9 Proxy Chaining — Concept

Proxy chaining means routing traffic through multiple proxies.

Example:

```text
Client
   |
   v
Proxy A
   |
   v
Proxy B
   |
   v
Proxy C
   |
   v
Destination
```

Possible purposes:
- Network routing.
- Layered filtering.
- Privacy experiments.
- Connecting through multiple network environments.

Potential disadvantages:
- Increased latency.
- More complex troubleshooting.
- More points of failure.
- Trust is distributed across multiple proxy operators.
- Misconfiguration may expose traffic or credentials.

Using several proxies does not guarantee anonymity.

### 24.10 TLS Interception — Authorized Lab Use

TLS interception occurs when a proxy terminates a client's TLS connection and creates another TLS connection to the destination.

Architecture:

```text
Browser
   |
   | TLS connection 1
   v
Intercepting Proxy
   |
   | TLS connection 2
   v
Destination Server
```

The proxy acts as a TLS intermediary.

For authorized inspection, a test environment may trust a certificate authority created by the proxy.

Example workflow:

1. Start an intercepting proxy.
2. Configure a browser to use it.
3. Install and trust the proxy's CA certificate in a dedicated test environment.
4. Visit an authorized test application.
5. Inspect HTTP requests and responses.
6. Modify requests in the lab to understand application behavior.

Security considerations:
- The proxy can see decrypted traffic.
- Sensitive credentials may pass through it.
- The proxy CA must be protected.
- Never install an untrusted interception certificate.
- Remove lab trust configuration when it is no longer needed.

Do not intercept traffic belonging to other people or organizations without explicit authorization.

### 24.11 Burp Suite Proxy Configuration

**Burp Suite** is a web security testing platform that includes an intercepting proxy.

It helps security testers inspect and modify HTTP and HTTPS traffic.

Basic architecture:

```text
Browser
   |
   | HTTP / HTTPS
   v
Burp Suite Proxy
   |
   v
Web Application
```

Typical setup:

1. Open Burp Suite.
2. Start a temporary project or use the available project option.
3. Open the Proxy section.
4. Confirm that the proxy listener is running.
5. The default local listener is commonly `127.0.0.1:8080`.
6. Configure a browser to use that address and port.
7. For HTTPS inspection, configure the browser to trust Burp's CA certificate in the dedicated testing profile.
8. Visit an authorized test website.
9. Inspect the HTTP history.
10. Enable interception when you want to pause and examine requests.

Example browser proxy settings:

```text
Proxy host: 127.0.0.1
Proxy port: 8080
```

Useful Burp features:
- Proxy: Intercept and inspect traffic.
- HTTP history: Review requests and responses.
- Repeater: Manually resend and modify requests.
- Intruder: Automate controlled request variations.
- Decoder: Encode and decode data.
- Comparer: Compare responses.

**Security testing tip:**

When testing authentication or authorization, compare the same request under different user accounts in an authorized lab. Pay attention to object IDs, role information, cookies, and server responses.

### 24.12 Reverse-Proxy Trust Boundaries

A reverse proxy separates the public-facing network from internal application services.

Example:

```text
Internet
   |
   v
Reverse Proxy
   |
   | Trusted internal connection
   v
Backend Application
   |
   v
Database
```

A trust boundary defines where data changes from trusted to untrusted or vice versa.

Important considerations:
- Public clients are untrusted.
- The reverse proxy should validate incoming traffic.
- The backend should accept proxy metadata only from trusted proxy addresses.
- Internal services should not be exposed unnecessarily.
- Security checks must not be skipped merely because traffic came through a proxy.

### 24.13 Risks from Incorrectly Trusting Forwarded Headers

Consider an application that uses `X-Forwarded-For` to determine a user's IP address.

A client sends:

```http
GET /account HTTP/1.1
Host: example.com
X-Forwarded-For: 127.0.0.1
```

If the application blindly trusts this header, it may incorrectly believe the request came from localhost.

Potential vulnerabilities include:

1. IP-based access-control bypass.
2. Incorrect rate-limit enforcement.
3. False audit logs.
4. Host-header-related attacks.
5. Incorrect HTTPS detection.
6. Password-reset URL poisoning.
7. Incorrect redirect generation.

**Recommended protections:**

- Accept forwarded headers only from known proxy IP addresses.
- Configure the proxy to remove or overwrite client-supplied forwarded headers.
- Define trusted proxy ranges carefully.
- Validate hostnames against an allowlist.
- Do not use forwarded IP information as the only authentication mechanism.

---

## 25. VPNs

### 25.1 What Is a VPN?

A **Virtual Private Network (VPN)** creates a protected network connection over an existing network, such as the public internet.

It commonly uses tunneling and encryption to connect a user or network to another private network.

Basic architecture:

```text
Your Device
     |
     | Encrypted VPN Tunnel
     v
VPN Server
     |
     v
Private Network / Internet
```

Common purposes:
- Secure remote access.
- Connecting company networks.
- Protecting traffic on untrusted networks.
- Accessing private internal services.
- Connecting geographically separated offices.

A VPN does not make someone completely anonymous or automatically protect applications from vulnerabilities.

### 25.2 Remote-Access vs Site-to-Site VPN

| Feature | Remote-Access VPN | Site-to-Site VPN |
|---|---|---|
| Purpose | Connect an individual device to a network | Connect two or more networks |
| Typical users | Remote employees | Organizations and branches |
| Connection | Device to VPN gateway | Network gateway to network gateway |
| Example | Employee working from home | Office A connected to Office B |

**Remote-access VPN:**

```text
Laptop → VPN Gateway → Company Network
```

**Site-to-site VPN:**

```text
Office A Router
       |
       | VPN Tunnel
       |
Office B Router
```

### 25.3 VPN Tunneling

VPN tunneling encapsulates one network packet inside another packet.

Conceptual example:

```text
Original Packet
      |
      v
VPN Encapsulation
      |
      v
Encrypted Outer Packet
      |
      v
Internet
      |
      v
VPN Gateway
      |
      v
Original Packet Recovered
```

The tunnel provides a logical connection between endpoints.

Depending on the VPN protocol and configuration, it may protect:
- Confidentiality.
- Integrity.
- Authentication.
- Network traffic routing.

### 25.4 IPsec VPN

**IPsec (Internet Protocol Security)** is a collection of protocols that secures IP communication.

It is commonly used for site-to-site VPNs and remote-access VPNs.

Important components:

**AH (Authentication Header):**
- Provides integrity and authentication.
- Does not provide encryption.
- Less commonly used in modern VPN deployments.

**ESP (Encapsulating Security Payload):**
- Provides encryption and can provide integrity and authentication.
- Commonly used for IPsec VPNs.

**IKE (Internet Key Exchange):**
- Negotiates security associations.
- Establishes cryptographic keys and parameters.

IPsec modes:

| Mode | Description |
|---|---|
| Transport mode | Protects the payload of the original IP packet |
| Tunnel mode | Encapsulates the entire original IP packet inside a new IP packet |

Simplified tunnel-mode architecture:

```text
Original IP Packet
       |
       v
IPsec Encapsulation
       |
       v
New IP Packet
       |
       v
VPN Network
```

### 25.5 WireGuard

**WireGuard** is a modern VPN protocol designed to be relatively simple, fast, and easy to configure.

Characteristics:
- Uses modern cryptographic primitives.
- Uses UDP for transport.
- Uses public/private key pairs for peer authentication.
- Has a relatively small codebase compared with many traditional VPN implementations.
- Supports roaming between network addresses.

Typical architecture:

```text
Client A ←→ WireGuard Tunnel ←→ Client B
```

Example configuration concept:

```ini
[Interface]
PrivateKey = <private-key>
Address = 10.0.0.2/24

[Peer]
PublicKey = <peer-public-key>
Endpoint = vpn.example.com:51820
AllowedIPs = 10.0.0.0/24
PersistentKeepalive = 25
```

Explanation:
- `PrivateKey`: Local peer's private key.
- `Address`: VPN interface address.
- `PublicKey`: Remote peer's public key.
- `Endpoint`: Remote peer address and port.
- `AllowedIPs`: Defines which destination IP ranges are associated with the peer.
- `PersistentKeepalive`: Sends periodic packets when configured, useful in some NAT environments.

Never share a real WireGuard private key. The values above are placeholders.

### 25.6 OpenVPN

**OpenVPN** is a VPN solution based on TLS-based authentication and secure tunneling.

Characteristics:
- Supports UDP and TCP transport.
- Uses certificates and keys for authentication.
- Supports remote-access and site-to-site configurations.
- Offers flexible configuration options.

Simplified architecture:

```text
VPN Client
    |
    | Encrypted OpenVPN Tunnel
    |
OpenVPN Server
    |
Private Network
```

Common components:
- Client configuration.
- Server configuration.
- CA certificate.
- Client and server certificates.
- Private keys.
- TLS authentication or control-channel protection options.

OpenVPN can operate over UDP or TCP. UDP is often preferred for VPN transport because TCP-over-TCP can cause performance problems in some situations.

### 25.7 Split Tunneling

Split tunneling allows only selected traffic to pass through the VPN.

Example:

```text
                    ┌→ Company Network
Laptop → VPN Tunnel ┤
                    └→ Other Internet Traffic → ISP
```

With full tunneling:

```text
Laptop → VPN Tunnel → VPN Gateway → Internet
```

Comparison:

| Split tunneling | Full tunneling |
|---|---|
| Selected traffic uses VPN | Most or all traffic uses VPN |
| Can reduce VPN bandwidth usage | Centralizes traffic routing |
| Can improve performance | Provides more consistent network policy |
| May expose non-VPN traffic to local networks | May increase VPN server load |

Security concern:

Split tunneling can create a path between a less-trusted network and a protected network. Organizations must define which routes are permitted.

### 25.8 VPN Routes and DNS

VPN routing determines which traffic enters the tunnel.

Example:

```text
VPN interface: 10.8.0.2
VPN network:   10.8.0.0/24
Private route: 192.168.10.0/24
```

A route may direct traffic for `192.168.10.0/24` through the VPN interface.

DNS determines how domain names are resolved.

A VPN may:
- Use the VPN provider's DNS servers.
- Use corporate internal DNS.
- Route DNS requests through the tunnel.
- Apply split-DNS rules.

Potential DNS leaks occur when DNS queries use an unintended resolver outside the VPN tunnel.

Troubleshooting should include checking:
- Routing tables.
- DNS server settings.
- IPv4 and IPv6 behavior.
- Split-tunnel configuration.
- Firewall rules.

### 25.9 VPN vs Proxy

| Feature | VPN | Proxy |
|---|---|---|
| Main purpose | Protected network connection | Forwarding application or network traffic |
| Traffic coverage | Can route much or all device traffic | Often specific application traffic |
| Encryption | Usually provides encrypted tunneling | Not guaranteed |
| Network layer | Often operates at Layer 3 or through virtual interfaces | Depends on proxy type |
| IP visibility | Destination sees VPN exit IP for routed traffic | Destination sees proxy exit IP |
| Common use | Remote access and network privacy | Filtering, routing, inspection, debugging |

A proxy and a VPN are not interchangeable in every situation.

A SOCKS proxy does not automatically encrypt traffic. A VPN does not guarantee anonymity.

### 25.10 VPN Limitations

A VPN does not:
- Make users completely anonymous.
- Prevent phishing.
- Prevent malware infection.
- Fix insecure websites.
- Protect against every form of tracking.
- Stop an application from leaking information.
- Prevent account compromise.
- Guarantee that a VPN provider cannot observe metadata or traffic.

Other parties may still identify or track users through:
- Cookies.
- Browser fingerprinting.
- Account logins.
- DNS behavior.
- Device information.
- Application telemetry.
- Payment and registration information.

A VPN shifts some network trust from the local network or ISP to the VPN provider.

### 25.11 Common VPN Configuration Errors

Common issues include:

1. Incorrect server address.
2. Wrong port or transport protocol.
3. Invalid credentials.
4. Incorrect certificates or keys.
5. Expired certificates.
6. Incorrect routing rules.
7. DNS configuration errors.
8. Firewall blocking VPN traffic.
9. IP address conflicts.
10. MTU problems.
11. Missing NAT configuration.
12. Incorrect AllowedIPs in WireGuard.
13. Mismatched IPsec security parameters.
14. Incorrect system time affecting certificate validation.
15. Split-tunnel routes that omit required networks.

Troubleshooting checklist:

```text
1. Confirm internet connectivity.
2. Verify VPN server hostname and port.
3. Check credentials and certificates.
4. Inspect VPN client logs.
5. Check routing table.
6. Verify DNS resolution.
7. Test access to the intended private IP.
8. Check firewall and NAT rules.
9. Inspect MTU-related problems.
10. Confirm that traffic follows the intended tunnel.
```

---

## Practical Labs

Perform these exercises using your own devices, local virtual machines, and authorized test environments.

### Lab 1: Configure a Local HTTP Proxy

Start a local proxy tool such as Burp Suite and configure a browser to use:

```text
Host: 127.0.0.1
Port: 8080
```

Visit a local test application or an authorized website.

Observe:
- HTTP requests.
- Response headers.
- Cookies.
- Redirects.
- Request methods.

### Lab 2: Inspect Proxy Headers

Send a request to a local test server with a forwarded header:

```bash
curl -i \
  http://127.0.0.1:8000 \
  -H "X-Forwarded-For: 203.0.113.10"
```

Observe whether the application uses the header.

Remember: `203.0.113.0/24` is reserved for documentation and examples.

### Lab 3: Inspect a SOCKS5 Proxy

If you have a SOCKS5 proxy running locally:

```bash
curl --socks5-hostname 127.0.0.1:1080 https://example.com
```

The `--socks5-hostname` option allows hostname resolution through the proxy.

Only use a proxy you control or are authorized to use.

### Lab 4: Inspect VPN Routes on Linux

Display network interfaces:

```bash
ip addr
```

Display routing table:

```bash
ip route
```

Display DNS configuration:

```bash
resolvectl status
```

Observe the changes before and after connecting to a VPN.

### Lab 5: Understand WireGuard Configuration

Inspect an existing WireGuard configuration without exposing private keys:

```bash
sudo wg show
```

Check the interface:

```bash
ip addr show
```

Check routes:

```bash
ip route
```

Do not share private keys or complete VPN configuration files containing credentials.

### Lab 6: Compare VPN and Proxy Traffic

Using a test environment:

1. Record your normal public IP address.
2. Connect through a proxy and check the destination-visible IP.
3. Disconnect the proxy.
4. Connect through a VPN.
5. Check the destination-visible IP again.
6. Compare DNS and routing behavior.

The visible IP may change depending on the proxy or VPN configuration.

---

## Quick Revision

- A proxy acts as an intermediary between a client and a destination.
- A forward proxy represents clients; a reverse proxy represents servers.
- A transparent proxy can intercept traffic without conventional client configuration.
- HTTP proxies understand HTTP; SOCKS proxies can route other types of connections.
- SOCKS5 supports TCP, UDP, IPv4, IPv6, and authentication negotiation.
- Proxy authentication commonly uses `407 Proxy Authentication Required`.
- `X-Forwarded-For`, `X-Forwarded-Host`, and `X-Forwarded-Proto` carry proxy-related metadata.
- Forwarded headers must only be trusted from known proxies.
- Proxy chaining routes traffic through multiple proxies.
- TLS interception creates separate TLS connections and requires a trusted interception CA in the test environment.
- Burp Suite is commonly used to inspect and modify web traffic in authorized security testing.
- A VPN creates a protected tunnel over another network.
- Remote-access VPN connects an individual device to a private network.
- Site-to-site VPN connects separate networks.
- IPsec commonly uses ESP and IKE.
- WireGuard uses modern cryptography and public/private peer keys.
- OpenVPN uses TLS-based security and supports UDP or TCP.
- Split tunneling routes only selected traffic through the VPN.
- DNS and routing configuration determine whether traffic actually uses the VPN.
- A VPN does not guarantee anonymity or protect against application vulnerabilities.

## Interview Questions

1. What is a proxy server?
2. Explain forward proxy vs reverse proxy.
3. What is a transparent proxy?
4. What is the difference between an HTTP proxy and a SOCKS proxy?
5. Compare SOCKS4 and SOCKS5.
6. What is proxy authentication?
7. What is the difference between `401` and `407`?
8. Explain `X-Forwarded-For`.
9. Why should applications not blindly trust forwarded headers?
10. What is proxy chaining?
11. What is TLS interception?
12. How does Burp Suite intercept HTTPS traffic?
13. What is a reverse-proxy trust boundary?
14. What is a VPN?
15. Explain remote-access vs site-to-site VPN.
16. What is VPN tunneling?
17. What is IPsec?
18. Explain the roles of ESP and IKE.
19. What is the difference between transport mode and tunnel mode?
20. What is WireGuard?
21. What is OpenVPN?
22. Explain split tunneling vs full tunneling.
23. How can DNS leaks happen when using a VPN?
24. What is the difference between a VPN and a proxy?
25. Does a VPN make a user completely anonymous?
26. How would you troubleshoot a VPN connection that connects successfully but cannot access an internal server?
27. How can incorrect proxy configuration create security vulnerabilities?
28. Why is a VPN not a substitute for HTTPS?
