
# Phase 12: Network Security Concepts

# 27. Threats and Defenses

## 1. Threat, Vulnerability, Exploit, and Risk

These four terms are fundamental to cybersecurity. They are related, but they do not mean the same thing.

### Threat

A threat is anything that has the potential to cause harm to a system, network, application, or organization.

Examples:
- A cybercriminal attempting to steal customer information.
- Malware infecting a company's computer.
- An attacker trying to gain unauthorized access to a server.
- An employee accidentally exposing confidential information.
- A natural disaster damaging a data center.

### Vulnerability

A vulnerability is a weakness in a system that could be exploited to cause damage.

Examples:
- An outdated server running vulnerable software.
- A website using weak authentication.
- An exposed database without proper access controls.
- An incorrectly configured firewall.
- An application that does not validate user input properly.

### Exploit

An exploit is a technique, piece of code, or procedure used to take advantage of a vulnerability.

Example:

1. A web server runs an outdated version of software.
2. That version contains a known security vulnerability.
3. An attacker uses a publicly known exploit to abuse the vulnerability.
4. The attacker gains unauthorized access or causes disruption.

### Risk

Risk is the possibility of loss or damage when a threat takes advantage of a vulnerability.

Risk depends on factors such as:
- Likelihood of an attack.
- Potential impact.
- Value of the affected asset.
- Existing security controls.

A simplified model:

`Risk = Likelihood × Impact`

### Comparison

| Term | Meaning | Example |
|---|---|---|
| Threat | Potential danger | Cybercriminal |
| Vulnerability | Weakness | Unpatched server |
| Exploit | Method of abusing weakness | Exploit code |
| Risk | Potential loss or damage | Data breach |

**Remember:** A vulnerability is a weakness, an exploit takes advantage of it, a threat represents potential danger, and risk describes the possible consequences.

---

## 2. Attack Surface

An attack surface is the complete set of points through which an attacker might attempt to access, attack, or compromise a system.

Every exposed service, application, device, account, and interface can increase the attack surface.

### Types of attack surfaces

**1. Network attack surface**
- Open ports.
- Exposed SSH services.
- Publicly accessible servers.
- Misconfigured routers.
- Unnecessary network services.

**2. Application attack surface**
- Login pages.
- Registration forms.
- APIs.
- File upload functionality.
- Password reset functionality.
- Admin panels.

**3. Human attack surface**
- Phishing emails.
- Weak passwords.
- Social engineering.
- Accidental disclosure of information.

**4. Cloud attack surface**
- Public storage buckets.
- Exposed cloud databases.
- Misconfigured permissions.
- Publicly accessible management interfaces.

### Example

Imagine a company has:

- A public website.
- An API server.
- An SSH server.
- A database.
- An employee login portal.

Each exposed component may provide an opportunity for an attacker.

### Attack surface reduction

- Disable unnecessary services.
- Close unused ports.
- Remove unused accounts.
- Apply security patches.
- Restrict administrative access.
- Use strong authentication.
- Avoid exposing internal services directly to the internet.
- Review cloud and application configurations regularly.

**Cybersecurity relevance:** During security assessments and bug bounty programs, identifying the attack surface is an important early step.

---

## 3. Threat Modeling Basics

Threat modeling is a structured process used to identify possible threats, understand how an attacker might target a system, and decide which security controls are needed.

It helps developers and security professionals think about security before an attack happens.

### Basic threat modeling process

1. Identify the system and its important assets.
2. Identify entry points and trust boundaries.
3. Understand how data moves through the system.
4. Identify possible threats.
5. Evaluate the likelihood and impact of each threat.
6. Select appropriate security controls.
7. Review and update the model when the system changes.

### Example: Online banking application

Suppose a banking application contains:

- User login.
- Account information.
- Money transfers.
- Transaction history.
- Database.
- Payment API.

Possible threats:

| Component | Possible threat | Defense |
|---|---|---|
| Login | Credential theft | MFA, rate limiting |
| Session | Session hijacking | Secure cookies, HTTPS |
| API | Unauthorized access | Authorization checks |
| Database | Data exposure | Encryption, access controls |
| Transactions | Replay or manipulation | Transaction validation, idempotency |

### STRIDE threat modeling

STRIDE is a popular threat modeling framework.

| Letter | Threat | Meaning |
|---|---|---|
| S | Spoofing | Pretending to be another identity |
| T | Tampering | Modifying data without authorization |
| R | Repudiation | Denying an action without sufficient evidence |
| I | Information Disclosure | Exposing confidential information |
| D | Denial of Service | Making a service unavailable |
| E | Elevation of Privilege | Gaining higher permissions |

### Trust boundaries

A trust boundary is a point where data crosses between components with different levels of trust.

Example:

`Internet → Firewall → Web Server → Internal Database`

The internet is generally untrusted. The database should not automatically trust incoming requests just because they came through the web server.

**Cybersecurity relevance:** Threat modeling is useful in both network security and web application security because it helps identify weaknesses before implementation or testing.

---

## 4. Spoofing

Spoofing is an attack technique in which an attacker disguises their identity or the origin of data to make it appear legitimate.

The attacker pretends to be another device, user, server, or network address.

### Common types

- IP spoofing.
- MAC spoofing.
- DNS spoofing.
- Email spoofing.
- ARP spoofing.
- Website spoofing.

### Example

An attacker sends a network packet with a forged source IP address.

The receiving system may see an IP address that does not represent the actual sender.

### Defenses

- Use network filtering.
- Apply ingress and egress filtering.
- Use authentication.
- Validate identities rather than trusting addresses alone.
- Use secure DNS configurations.
- Monitor suspicious traffic.

**Important:** Spoofing an address does not automatically give an attacker access to the device or its account.

---

## 5. Sniffing

Sniffing is the process of capturing and inspecting network traffic.

Network administrators use sniffing for:
- Troubleshooting.
- Network performance analysis.
- Security monitoring.
- Protocol investigation.

Attackers may also use sniffing to capture sensitive information when traffic is insufficiently protected.

### Types of sniffing

**Passive sniffing**

The attacker observes traffic without actively modifying or interfering with it.

**Active sniffing**

The attacker manipulates or influences network communication to observe traffic. Techniques may include ARP spoofing in an inadequately protected network.

### Example

Suppose a user sends login credentials over an unencrypted HTTP connection.

A person able to capture that traffic may be able to read the credentials.

HTTPS protects the application data through TLS encryption.

### Common sniffing tools

| Tool | Purpose |
|---|---|
| Wireshark | GUI-based packet analysis |
| tcpdump | Command-line packet capture |
| TShark | Command-line Wireshark analysis |
| Zeek | Network security monitoring |
| Suricata | Network threat detection |

### Basic packet capture with tcpdump

Capture traffic on a network interface:

```bash
sudo tcpdump -i eth0
```

Capture traffic involving a particular host:

```bash
sudo tcpdump -i eth0 host 192.168.1.10
```

Capture DNS traffic:

```bash
sudo tcpdump -i eth0 port 53
```

Save captured packets to a PCAP file:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Read an existing PCAP file:

```bash
tcpdump -r capture.pcap
```

Use only on networks and systems where you have permission to capture traffic.

---

## 6. Man-in-the-Middle (MITM) Attacks

A Man-in-the-Middle attack occurs when an attacker secretly positions themselves between two communicating parties and intercepts or potentially modifies their communication.

### Normal communication

```text
Client  <---------------->  Server
```

The client communicates directly with the server.

### MITM communication

```text
Client  <------>  Attacker  <------>  Server
```

The attacker may:
- Observe communication.
- Modify messages.
- Steal sensitive information.
- Redirect requests.
- Impersonate a communication endpoint.

### Example

A user connects to an unsecured public Wi-Fi network.

An attacker on that network attempts to intercept communication between the user's device and a website.

If the user visits a properly configured HTTPS website and certificate validation succeeds, TLS provides protection against reading or modifying the protected connection.

### Common MITM techniques

- ARP spoofing.
- DNS spoofing.
- Rogue Wi-Fi access points.
- Malicious proxies.
- Compromised network devices.

### Defenses

- Use HTTPS everywhere.
- Validate TLS certificates.
- Avoid ignoring browser certificate warnings.
- Use secure Wi-Fi encryption.
- Use a trusted VPN when appropriate.
- Enable HSTS on websites.
- Use strong authentication.
- Avoid transmitting credentials over unencrypted connections.

**Important:** A VPN does not automatically protect against every MITM attack. The security of the destination connection and the VPN provider still matters.

---

## 7. Replay Attacks

A replay attack occurs when an attacker captures a legitimate communication and retransmits it later to repeat an action or gain unauthorized access.

### Example

Imagine a system sends a request:

```text
Transfer ₹500 from Account A to Account B
```

An attacker captures the request and sends the same request again.

If the system does not properly prevent repeated requests, the transaction might execute more than once.

### Another example

An attacker captures an authentication message and attempts to reuse it later.

### Defenses

- Use unique nonces.
- Use timestamps with appropriate validation.
- Use sequence numbers.
- Use cryptographic challenge-response authentication.
- Implement transaction IDs.
- Implement idempotency for sensitive APIs.
- Reject expired or previously used authentication tokens where appropriate.

### Nonce

A nonce is a value used only once in a particular protocol exchange or operation.

It helps ensure that an old captured message cannot simply be reused as a valid new message.

**Cybersecurity relevance:** Replay protection matters in authentication systems, payment APIs, network protocols, and session management.

---

## 8. DNS Spoofing — Concept

DNS spoofing is an attack in which an attacker causes a DNS lookup to return an incorrect or malicious IP address.

DNS normally translates domain names into IP addresses.

Example:

```text
example.com → 93.184.216.34
```

In a DNS spoofing attack, the victim may receive an attacker-controlled address instead.

### How it can affect users

1. A user enters a legitimate website address.
2. The DNS response is manipulated.
3. The browser receives an incorrect IP address.
4. The user may be redirected to a malicious website.

### Possible consequences

- Phishing.
- Credential theft.
- Malware distribution.
- Traffic redirection.
- Fake websites.

### Defenses

- Use DNSSEC where supported.
- Use trusted DNS resolvers.
- Keep DNS infrastructure updated.
- Monitor unexpected DNS changes.
- Use HTTPS and validate certificates.
- Protect DNS server configurations.

### DNSSEC

DNS Security Extensions help authenticate DNS data using digital signatures.

DNSSEC helps verify that DNS responses have not been improperly modified.

**Important:** DNSSEC does not encrypt DNS queries. It provides authenticity and integrity protection for signed DNS data.

---

## 9. ARP Spoofing — Concept

ARP stands for Address Resolution Protocol.

ARP is used in IPv4 local networks to discover the MAC address associated with an IPv4 address.

### Normal ARP process

Suppose a computer wants to communicate with:

```text
IP Address: 192.168.1.1
```

It broadcasts an ARP request:

```text
Who has 192.168.1.1?
```

The device owning that IP address replies with its MAC address.

The computer stores the IP-to-MAC mapping in its ARP cache.

### ARP spoofing

ARP spoofing occurs when an attacker sends forged ARP messages to associate their MAC address with another device's IP address.

For example:

```text
Gateway IP: 192.168.1.1
Attacker MAC: AA:BB:CC:DD:EE:FF
```

The victim may incorrectly associate the gateway's IP address with the attacker's MAC address.

### Possible consequences

- Traffic interception.
- Man-in-the-middle attacks.
- Traffic redirection.
- Network disruption.

### Defenses

- Dynamic ARP Inspection (DAI).
- DHCP snooping.
- Static ARP entries in limited situations.
- Network segmentation.
- Secure switch configuration.
- Monitoring unusual ARP changes.
- Encryption through HTTPS and other secure protocols.

**Important:** ARP operates within IPv4 local network segments. IPv6 uses Neighbor Discovery Protocol (NDP), not ARP.

---

## 10. DoS vs DDoS

### DoS — Denial of Service

A Denial-of-Service attack attempts to make a system, server, or network service unavailable to legitimate users.

Usually, a DoS attack originates from a single attacking source or a relatively limited number of sources.

### DDoS — Distributed Denial of Service

A Distributed Denial-of-Service attack attempts to overwhelm a target using traffic from multiple distributed systems.

These systems may be compromised computers, servers, or IoT devices.

### Comparison

| Feature | DoS | DDoS |
|---|---|---|
| Full form | Denial of Service | Distributed Denial of Service |
| Sources | Usually one or few | Many distributed sources |
| Traffic | Limited source distribution | Distributed traffic |
| Mitigation | May be simpler | Often more complex |
| Scale | Can be smaller | Often larger |

### Common DDoS categories

**1. Volumetric attacks**

Attempt to consume available bandwidth using large volumes of traffic.

**2. Protocol attacks**

Abuse network protocol behavior or exhaust resources such as connection state tables.

**3. Application-layer attacks**

Target application resources, such as web server request handling.

### Defenses

- DDoS protection services.
- Traffic filtering.
- Rate limiting.
- Load balancing.
- Web Application Firewalls (WAFs).
- CDN-based protection.
- Network monitoring.
- Upstream traffic scrubbing.
- Incident response procedures.

**Important:** A DDoS attack cannot always be stopped by simply blocking one IP address because traffic may originate from many different sources.

---

## 11. SYN Flood — Concept and Defenses

A SYN flood is a type of denial-of-service attack that abuses the TCP three-way handshake.

### Normal TCP three-way handshake

```text
Client                  Server
  |                        |
  |------ SYN ------------>|
  |                        |
  |<----- SYN-ACK ----------|
  |                        |
  |------ ACK ------------>|
  |                        |
  |   Connection established
```

### SYN flood behavior

In a SYN flood, an attacker sends many TCP SYN packets but does not complete the handshake.

The server may allocate resources for incomplete connections.

If enough resources are consumed, legitimate users may have difficulty connecting.

### Defenses

- SYN cookies.
- Connection rate limiting.
- Firewall filtering.
- Load balancing.
- Connection timeout tuning.
- DDoS protection services.
- Monitoring abnormal SYN traffic.

### SYN cookies

SYN cookies are a defensive technique that helps a server avoid allocating substantial connection state until the client completes the handshake.

They help reduce the impact of SYN flood attacks.

**Practical concept:** A sudden increase in incoming SYN packets combined with many incomplete connections may indicate a SYN flood.

---

## 12. Amplification Attacks — Concept and Defenses

An amplification attack occurs when an attacker exploits a protocol or service to generate a much larger response than the original request.

The attacker may use spoofed source IP addresses so that the amplified responses are sent to a victim.

### Example

Imagine:

- Attacker sends a small request.
- A public server generates a much larger response.
- The victim receives the response.
- Many such servers generate traffic toward the victim.

This can create a large traffic flood.

### Common amplification vectors

- DNS amplification.
- NTP amplification.
- SSDP amplification.
- Memcached amplification.

### Amplification factor

The amplification factor describes how much larger the response is compared with the request.

For example:

```text
Request size: 100 bytes
Response size: 1,000 bytes

Amplification factor = 10
```

### Defenses

- Disable unnecessary publicly accessible services.
- Prevent open DNS resolvers.
- Restrict recursive DNS access.
- Apply response rate limiting.
- Use ingress and egress filtering.
- Use network-level DDoS protection.
- Configure services securely.

### BCP 38

BCP 38 recommends ingress filtering to prevent packets with spoofed source addresses from leaving a network.

This helps reduce IP spoofing and reflection attacks.

---

## 13. Session Hijacking — Concept and Defenses

Session hijacking occurs when an attacker obtains or takes control of a valid user's session.

A session allows a website or application to recognize an authenticated user across multiple requests.

### How sessions work

1. User logs in.
2. Server authenticates the user.
3. Server creates a session.
4. Browser receives a session identifier.
5. Browser sends that identifier with future requests.
6. Server recognizes the authenticated session.

### Example

A website uses a session cookie:

```http
Set-Cookie: sessionid=abc123
```

If an attacker steals a valid session identifier, they may be able to impersonate the user until the session expires or is invalidated.

### Common causes

- Session token theft.
- Cross-site scripting (XSS).
- Unencrypted HTTP traffic.
- Malware.
- Weak session management.
- Predictable session identifiers.

### Defenses

Use secure cookie attributes:

```http
Set-Cookie: sessionid=RANDOM_VALUE; Secure; HttpOnly; SameSite=Lax
```

**Secure**
- Sends the cookie only over HTTPS.

**HttpOnly**
- Prevents ordinary JavaScript access to the cookie.

**SameSite**
- Helps control cross-site cookie sending.

Additional defenses:

- Generate unpredictable session IDs.
- Regenerate session IDs after login and privilege changes.
- Set appropriate session expiration.
- Invalidate sessions after logout.
- Use HTTPS everywhere.
- Protect against XSS.
- Use MFA for sensitive accounts.
- Monitor suspicious session activity.

**Important:** HttpOnly helps protect cookies from JavaScript-based theft, but it does not prevent every session-related attack. An XSS vulnerability may still allow an attacker to perform actions through the victim's browser.

---

## 14. IP Spoofing and Its Limitations

IP spoofing means forging the source IP address in an IP packet.

Normally, an IP packet contains:

- Source IP address.
- Destination IP address.
- Other protocol information.
- Payload.

In IP spoofing, the sender changes the source address to make the packet appear to originate from another IP.

### Example

Actual sender:

```text
192.168.1.50
```

Forged source address:

```text
10.0.0.20
```

The packet may appear to come from `10.0.0.20`.

### Why attackers use it

- Reflection attacks.
- Traffic obfuscation.
- Certain denial-of-service attacks.
- Attempts to bypass weak source-IP-based filters.

### Limitations

IP spoofing does not automatically allow an attacker to:

- Receive responses sent to the forged IP.
- Complete normal TCP communication without receiving the return traffic.
- Authenticate as the owner of the forged address.
- Bypass application-level authentication.
- Read encrypted network traffic.

### TCP vs UDP

**TCP:**

TCP uses a connection-oriented handshake. If an attacker cannot receive the server's replies, completing a normal TCP connection becomes difficult.

**UDP:**

UDP is connectionless. A sender can transmit packets without establishing a connection first, making source spoofing more practical in some scenarios.

### Defenses

- Ingress filtering.
- Egress filtering.
- BCP 38.
- Network ACLs.
- Stateful firewalls.
- Authentication beyond IP addresses.

**Remember:** An IP address is not proof of identity.

---

## 15. Port Scanning

Port scanning is the process of checking a target system to identify which network ports are open, closed, or filtered.

A port represents a communication endpoint associated with a network service.

### Common port states

| State | Meaning |
|---|---|
| Open | A service is accepting connections |
| Closed | The host is reachable, but no service is listening |
| Filtered | A firewall or filter prevents determining the state |
| Open/Filtered | The scanner cannot distinguish between the two |
| Closed/Filtered | The result is ambiguous for the scanning method |

### Why port scanning is used

Legitimate uses:
- Network administration.
- Asset discovery.
- Security audits.
- Firewall testing.
- Vulnerability assessments.

Potential malicious uses:
- Reconnaissance.
- Discovering exposed services.
- Identifying possible attack paths.

### Nmap

Nmap is a widely used network discovery and port scanning tool.

Check its version:

```bash
nmap --version
```

Scan a system you own or are authorized to test:

```bash
nmap 192.168.1.10
```

Scan a specific port:

```bash
nmap -p 80 192.168.1.10
```

Scan several ports:

```bash
nmap -p 22,80,443 192.168.1.10
```

Scan all TCP ports:

```bash
nmap -p- 192.168.1.10
```

Detect service versions:

```bash
nmap -sV 192.168.1.10
```

Perform operating system detection:

```bash
sudo nmap -O 192.168.1.10
```

### Security relevance

Port scanning helps identify unnecessary exposed services.

For example:

```text
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
3306/tcp open   mysql
```

If a database port is exposed publicly without a valid business requirement, it may increase the attack surface.

**Important:** Open ports are not automatically vulnerabilities. You must investigate the service, configuration, exposure, and access controls.

---

## 16. Service Enumeration

Service enumeration is the process of identifying details about services running on a target system.

Port scanning identifies possible open ports. Service enumeration investigates what is running behind those ports.

### Information collected

- Service name.
- Software version.
- Operating system details.
- Protocol information.
- Server configuration.
- Supported authentication methods.
- Available network resources.

### Example

A port scan reports:

```text
80/tcp open http
```

Service enumeration may identify:

```text
Service: Apache HTTP Server
Version: 2.4.x
Protocol: HTTP
```

### Common tools

| Tool | Purpose |
|---|---|
| Nmap | Service and version detection |
| Netcat | Network connection testing |
| curl | HTTP request testing |
| WhatWeb | Website technology identification |
| enum4linux-ng | SMB information enumeration |
| dig | DNS record investigation |

### Examples

Check HTTP response headers:

```bash
curl -I https://example.com
```

Check a DNS record:

```bash
dig example.com
```

Check a service connection:

```bash
nc -vz 192.168.1.10 22
```

Identify services using Nmap:

```bash
nmap -sV 192.168.1.10
```

**Cybersecurity relevance:** Enumeration is an important part of authorized security assessments and helps defenders understand which services are exposed.

---

## 17. Network Segmentation

Network segmentation means dividing a larger network into smaller, separate network sections.

Each section can have different access rules and security controls.

### Example

A company may divide its network into:

```text
                 Company Network
                        |
          +-------------+-------------+
          |             |             |
       HR Network   Finance Network  Guest Network
          |             |             |
       HR PCs       Finance PCs    Guest Devices
```

### Why segmentation matters

- Limits unauthorized access.
- Reduces the spread of malware.
- Protects sensitive systems.
- Separates guest devices from internal resources.
- Reduces the impact of a compromised machine.

### Common segmentation methods

**VLANs**

Virtual LANs logically separate devices within a switched network.

**Subnets**

IP subnetting divides a network into smaller address ranges.

**Firewalls**

Firewalls enforce communication rules between network segments.

**Access Control Lists (ACLs)**

ACLs define which traffic is allowed or denied.

### Example

A guest network should normally not be allowed to access the internal database network.

```text
Guest Network  ----X---->  Database Network
```

### Zero Trust

Zero Trust is a security approach based on the principle:

"Never trust automatically; always verify."

It emphasizes:
- Identity verification.
- Least privilege.
- Continuous monitoring.
- Explicit access control.
- Limiting unnecessary network access.

---

## 18. Rate Limiting

Rate limiting controls how many requests a user, device, or IP address can make within a specified period.

It helps protect services from excessive requests and automated abuse.

### Example

An API allows:

```text
100 requests per minute per user
```

If a user exceeds the limit, the server may temporarily reject additional requests.

### HTTP response

A server may respond with:

```http
HTTP/1.1 429 Too Many Requests
```

### Where rate limiting is useful

- Login endpoints.
- Password reset endpoints.
- OTP verification.
- Registration forms.
- Public APIs.
- Search endpoints.
- Payment-related APIs.

### Common rate-limiting algorithms

**1. Fixed Window**

Allows a fixed number of requests within a defined time window.

**2. Sliding Window**

Tracks requests over a moving time period.

**3. Token Bucket**

Requests consume tokens. Tokens are added back at a defined rate.

**4. Leaky Bucket**

Processes requests at a controlled rate.

### Important considerations

- Rate-limit by appropriate identifiers.
- Consider users, IPs, API keys, and devices.
- Avoid relying only on IP addresses.
- Use different limits for sensitive endpoints.
- Return clear retry information.
- Monitor abuse without blocking legitimate users unnecessarily.

**Cybersecurity relevance:** Rate limiting helps reduce brute-force attempts, automated abuse, and some forms of application-layer denial of service. It is not a complete DDoS defense.

---

## 19. IDS vs IPS

IDS and IPS are security technologies used to identify suspicious network activity.

### IDS — Intrusion Detection System

An IDS monitors network traffic or system activity and generates alerts when it identifies suspicious behavior.

An IDS primarily detects and reports.

### IPS — Intrusion Prevention System

An IPS monitors traffic and can automatically block or prevent traffic that matches configured security rules.

An IPS actively takes preventive action.

### Comparison

| Feature | IDS | IPS |
|---|---|---|
| Full form | Intrusion Detection System | Intrusion Prevention System |
| Main purpose | Detect threats | Detect and prevent threats |
| Action | Generates alerts | Can block traffic |
| Deployment | Often out-of-band | Often inline |
| Risk | May miss attacks | May block legitimate traffic |
| Example | Alert on suspicious traffic | Drop malicious packets |

### Simple diagram

```text
IDS:

Network Traffic → IDS Monitoring → Alert


IPS:

Network Traffic → IPS Inspection → Allow or Block
```

### Deployment types

**Network IDS (NIDS)**

Monitors network traffic.

**Host IDS (HIDS)**

Monitors activity on an individual system.

**Network IPS (NIPS)**

Inspects network traffic and can block suspicious packets.

**Host IPS (HIPS)**

Monitors and may prevent suspicious activity on a host.

---

## 20. Network Detection and Response (NDR)

Network Detection and Response (NDR) is a security approach that monitors network activity to identify suspicious behavior and support investigation and response.

It uses network traffic analysis, behavioral analytics, and sometimes machine learning to identify threats.

### What NDR can detect

- Unusual communication patterns.
- Suspicious connections to external servers.
- Lateral movement.
- Command-and-control communication.
- Unusual data transfers.
- Possible malware activity.
- Abnormal DNS requests.

### Example

An employee's computer normally communicates with a few internal servers.

Suddenly, it begins making repeated connections to an unfamiliar external IP address and transferring unusual amounts of data.

An NDR solution may identify this behavior as suspicious.

### NDR capabilities

- Traffic monitoring.
- Behavioral analysis.
- Threat detection.
- Investigation support.
- Network visibility.
- Incident response integration.

### IDS vs IPS vs NDR

| Technology | Main focus |
|---|---|
| IDS | Detect suspicious activity |
| IPS | Detect and block suspicious traffic |
| NDR | Analyze network behavior and support investigation and response |

---

## 21. Secure Configuration and Patching

Secure configuration means setting up systems, applications, and network devices according to security best practices.

Patching means applying software updates that fix bugs, security vulnerabilities, and other issues.

### Secure configuration practices

- Change default passwords.
- Disable unused services.
- Close unnecessary ports.
- Use strong authentication.
- Restrict administrative access.
- Configure firewalls correctly.
- Disable insecure protocols.
- Use secure encryption.
- Apply least privilege.
- Maintain configuration backups.

### Patching

Software vendors regularly release security updates.

For example, an operating system update may fix a vulnerability that could allow unauthorized access.

### Linux update example

On Debian-based systems such as Kali Linux:

```bash
sudo apt update
sudo apt upgrade
```

To check the operating system:

```bash
cat /etc/os-release
```

### Patch management process

1. Identify installed software and assets.
2. Monitor vendor security advisories.
3. Identify relevant vulnerabilities.
4. Prioritize updates according to risk.
5. Test updates where appropriate.
6. Apply patches.
7. Verify that updates were successful.
8. Document the changes.

### Common security resources

- CVE: Common Vulnerabilities and Exposures.
- CVSS: Common Vulnerability Scoring System.
- Vendor security advisories.
- CISA Known Exploited Vulnerabilities (KEV) catalog.

**Important:** Patching is not just installing updates. It also involves asset inventory, risk prioritization, testing, and verification.

---

## 22. Incident Response Fundamentals

Incident response is the structured process of identifying, managing, containing, and recovering from cybersecurity incidents.

A security incident may include:
- Malware infection.
- Unauthorized access.
- Data breach.
- Ransomware.
- DDoS attack.
- Compromised credentials.
- Suspicious network activity.

### Common incident response phases

The NIST incident response guidance describes a broader incident response lifecycle. A commonly taught operational sequence is:

**1. Preparation**

- Create an incident response plan.
- Define responsibilities.
- Configure monitoring.
- Maintain backups.
- Train security staff.

**2. Detection and Analysis**

- Identify suspicious activity.
- Review logs.
- Investigate alerts.
- Determine the scope and severity.

**3. Containment**

- Isolate affected systems.
- Disable compromised accounts.
- Block malicious communication.
- Prevent further damage.

**4. Eradication**

- Remove malware.
- Fix vulnerabilities.
- Remove unauthorized access.
- Apply necessary patches.

**5. Recovery**

- Restore systems.
- Verify system integrity.
- Monitor for recurring attacks.
- Return services to normal operation.

**6. Lessons Learned**

- Document what happened.
- Identify weaknesses.
- Improve security controls.
- Update incident response procedures.

### Incident response example

Suppose a company detects malware on an employee's computer.

A possible response:

1. The monitoring system generates an alert.
2. The security team investigates the alert.
3. The infected computer is isolated from the network.
4. Analysts identify the malware and its entry point.
5. The malware is removed.
6. The system is restored from a trusted state.
7. The team reviews the incident and improves defenses.

### Important evidence to preserve

- System logs.
- Firewall logs.
- Authentication logs.
- Network flow records.
- PCAP files.
- Endpoint alerts.
- Relevant timestamps.
- File hashes.

**Important:** Preserve evidence and follow your organization's incident response procedures. Do not immediately wipe or rebuild a system before collecting necessary forensic evidence.

---

# 28. IDS, IPS, and Network Monitoring

## 1. Intrusion Detection System (IDS)

An Intrusion Detection System is a security solution that monitors network traffic or system activity to identify possible attacks, suspicious behavior, and policy violations.

Its main job is detection and alerting.

### How IDS works

1. Collects network packets or system events.
2. Inspects the collected information.
3. Compares activity against detection rules or behavioral models.
4. Identifies suspicious patterns.
5. Generates alerts for security analysts.

### Types of IDS

**Network-based IDS (NIDS)**

Monitors traffic passing through a network segment.

**Host-based IDS (HIDS)**

Monitors activities on a particular computer or server.

### Example

An IDS detects repeated connection attempts against several ports on a server.

It generates an alert indicating possible port scanning.

### Benefits

- Network visibility.
- Suspicious activity detection.
- Security alerting.
- Investigation support.
- Policy violation detection.

### Limitations

- May generate false positives.
- May miss unknown attacks.
- Encrypted traffic limits visibility into application content.
- Requires proper configuration and maintenance.

---

## 2. Intrusion Prevention System (IPS)

An Intrusion Prevention System monitors network traffic and can automatically take action to stop detected threats.

Unlike a traditional IDS, an IPS is commonly deployed inline so that traffic passes through it.

### How IPS works

1. Receives network traffic.
2. Inspects packets and connections.
3. Compares traffic against security rules.
4. Identifies suspicious or malicious activity.
5. Allows, blocks, or otherwise handles the traffic according to policy.

### Possible actions

- Drop malicious packets.
- Block suspicious connections.
- Reject traffic.
- Temporarily block an IP address.
- Generate alerts.
- Apply configured prevention rules.

### Example

An IPS identifies traffic matching a known exploit signature and drops the suspicious packets.

### Limitations

- False positives may interrupt legitimate traffic.
- Incorrect rules can cause outages.
- Inline inspection may introduce latency.
- Encrypted traffic may limit inspection.

---

## 3. Signature-Based Detection

Signature-based detection identifies threats by comparing network activity with known patterns or signatures.

A signature represents a recognizable pattern associated with a known attack or suspicious activity.

### Example

A security system has a signature that detects a known malicious network request.

When matching traffic appears, the system generates an alert or takes action.

### Advantages

- Effective against known threats.
- Easy to understand and investigate.
- Often produces useful, specific alerts.
- Can be efficient for recognizable attack patterns.

### Limitations

- May not detect completely new attacks.
- Requires updated signatures.
- Attackers may modify traffic to avoid known patterns.
- Encrypted traffic can limit inspection.

### Example detection logic

```text
IF traffic matches a known malicious signature:
    Generate security alert
```

---

## 4. Anomaly-Based Detection

Anomaly-based detection identifies activity that differs significantly from an established normal behavior or baseline.

Instead of looking only for known attack signatures, it looks for unusual patterns.

### Example

A company normally transfers 500 MB of data per day from a particular server.

Suddenly, the server transfers 20 GB of data to an unfamiliar external destination.

This unusual behavior may generate an alert.

### Advantages

- Can detect previously unknown threats.
- Identifies unusual behavior.
- Helps detect compromised accounts and devices.
- Useful for behavioral monitoring.

### Limitations

- Normal behavior can change.
- May produce false positives.
- Requires good baseline data.
- Needs careful tuning.

### Comparison

| Feature | Signature-Based | Anomaly-Based |
|---|---|---|
| Detection method | Known patterns | Unusual behavior |
| Best for | Known threats | Unexpected activity |
| Unknown attacks | May miss them | May detect unusual behavior |
| False positives | Often lower with good signatures | Can be higher |
| Maintenance | Update signatures | Maintain baselines and models |

---

## 5. False Positives and False Negatives

These terms describe two important detection errors.

### False Positive

A false positive occurs when a security system identifies legitimate activity as malicious.

Example:

An employee performs a legitimate file transfer, but the monitoring system incorrectly flags it as suspicious.

### False Negative

A false negative occurs when a security system fails to identify malicious activity.

Example:

An attacker successfully transfers stolen data, but the monitoring system does not generate an alert.

### Comparison

| Term | Meaning | Example |
|---|---|---|
| True Positive | Correctly detects an attack | Malware detected |
| True Negative | Correctly identifies normal activity | Normal traffic allowed |
| False Positive | Normal activity flagged as malicious | Legitimate login blocked |
| False Negative | Attack goes undetected | Malware activity missed |

### Why these matter

Too many false positives:
- Waste analyst time.
- Cause alert fatigue.
- May interrupt legitimate operations.

Too many false negatives:
- Allow attacks to continue.
- Delay incident detection.
- Increase potential damage.

### Improving detection quality

- Tune detection rules.
- Maintain accurate baselines.
- Correlate multiple events.
- Review alert history.
- Update signatures.
- Use threat intelligence carefully.
- Continuously evaluate detection performance.

---

## 6. Network Traffic Baselines

A network traffic baseline represents the normal or expected behavior of a network over a period of time.

Security teams use baselines to identify unusual activity.

### What a baseline can include

- Average bandwidth usage.
- Normal connection counts.
- Common communication protocols.
- Typical DNS query volume.
- Common external destinations.
- Normal login patterns.
- Regular working hours.
- Typical data transfer sizes.

### Example

A company normally has:

```text
Average daily traffic: 2 GB
Typical DNS queries: 5,000/day
Common protocols: HTTPS, DNS, SSH
Normal active hours: 9 AM – 6 PM
```

One day, the company observes:

```text
Daily traffic: 25 GB
Unexpected external connections: High
DNS queries: 50,000/day
```

This difference may indicate suspicious activity.

### How to create a baseline

1. Collect network traffic data.
2. Observe normal behavior over time.
3. Identify regular communication patterns.
4. Document normal traffic volumes.
5. Account for weekends and business cycles.
6. Update the baseline when infrastructure changes.
7. Compare new activity against the baseline.

**Important:** Unusual traffic is not automatically malicious. Investigate the context before declaring an incident.

---

## 7. Centralized Logging

Centralized logging means collecting logs from multiple systems and storing them in a common location.

Instead of investigating each device separately, security analysts can review related events in one place.

### Sources of logs

- Firewalls.
- Routers.
- Switches.
- Servers.
- Endpoints.
- IDS/IPS systems.
- Applications.
- Authentication systems.
- DNS servers.
- Cloud services.

### Example architecture

```text
Firewall Logs ---------+
Server Logs -----------+
Endpoint Logs ---------+----> Central Log Platform
DNS Logs --------------+             |
IDS/IPS Alerts --------+             |
                                      |
                              Security Analysts
```

### Benefits

- Easier investigation.
- Better event correlation.
- Centralized visibility.
- Faster incident detection.
- Long-term log retention.
- Improved auditability.

### Common logging formats and protocols

**Syslog**

A widely used standard for transmitting and collecting log messages.

**JSON**

A structured format frequently used by applications and modern logging platforms.

**Windows Event Logs**

Logs generated by Windows operating systems and applications.

### Basic Linux log investigation

View recent system logs:

```bash
sudo journalctl -n 50
```

Follow system logs:

```bash
sudo journalctl -f
```

View authentication-related logs on many Debian-based systems:

```bash
sudo tail -f /var/log/auth.log
```

View system messages where available:

```bash
sudo tail -f /var/log/syslog
```

### Best practices

- Synchronize system clocks.
- Protect log files from unauthorized modification.
- Restrict access to logs.
- Configure retention policies.
- Monitor log collection failures.
- Avoid storing unnecessary sensitive data.
- Keep backups of important security logs.

---

## 8. Alert Triage

Alert triage is the process of reviewing security alerts, determining their importance, and deciding what action should be taken.

Security monitoring systems can generate thousands of alerts. Analysts must identify which ones require immediate attention.

### Alert triage process

1. Receive an alert.
2. Understand what triggered it.
3. Identify the affected system.
4. Check the source and destination.
5. Review related logs.
6. Determine whether the activity is legitimate or suspicious.
7. Assess severity and impact.
8. Escalate or close the alert with documentation.

### Example

An IDS generates:

```text
Alert: Multiple failed SSH login attempts
Source IP: 192.168.1.50
Destination: 192.168.1.100
Severity: Medium
```

An analyst should investigate:

- Is the source IP known?
- Is the activity expected?
- Which account was targeted?
- Were any logins successful?
- Are there other suspicious events?
- Does the activity indicate brute force?

### Alert severity

| Severity | Meaning | Example |
|---|---|---|
| Critical | Immediate serious threat | Confirmed active ransomware |
| High | Significant security concern | Successful unauthorized access |
| Medium | Suspicious activity needing investigation | Repeated failed logins |
| Low | Minor or informational event | Unusual but explainable traffic |

Severity labels vary between security platforms. Always consider actual business impact and confidence.

### Important SOC skills

- Reading logs.
- Understanding network protocols.
- Identifying suspicious IP addresses.
- Correlating events.
- Understanding false positives.
- Writing investigation notes.
- Escalating incidents appropriately.

---

## 9. Network Flow Records

Network flow records summarize communication between network endpoints.

They generally describe who communicated with whom, when, and how much data was transferred.

Unlike a PCAP file, a flow record usually does not contain the complete packet contents.

### Typical flow information

- Source IP.
- Destination IP.
- Source port.
- Destination port.
- Protocol.
- Number of packets.
- Number of bytes.
- Start time.
- End time.

### Example

```text
Source IP:      192.168.1.10
Destination IP: 8.8.8.8
Source Port:    53000
Destination:    53
Protocol:       UDP
Packets:        12
Bytes:          850
```

This record indicates that the internal device communicated with an external DNS server over UDP port 53.

### Common flow technologies

- NetFlow.
- IPFIX.
- sFlow.

### NetFlow

NetFlow is a technology originally developed by Cisco for collecting IP traffic flow information.

### IPFIX

IPFIX is a standard for exporting IP flow information.

### sFlow

sFlow provides sampled network traffic and interface statistics for network monitoring.

### Why flow records matter

- Detect unusual communication.
- Identify high-volume transfers.
- Investigate suspicious connections.
- Understand network usage.
- Identify possible data exfiltration.
- Monitor lateral movement.

---

## 10. PCAP Files

PCAP stands for Packet Capture.

A PCAP file stores captured network packets so that they can be inspected later.

PCAP files are useful for troubleshooting, security investigations, protocol analysis, and digital forensics.

### What a PCAP can contain

Depending on the capture and encryption:

- Source and destination IP addresses.
- Source and destination ports.
- Protocol information.
- Packet timestamps.
- Packet headers.
- Packet payloads.

### PCAP vs network flow records

| Feature | PCAP | Flow Records |
|---|---|---|
| Data | Individual packets | Communication summaries |
| Detail | High | Usually lower |
| Payload | May contain payload | Normally no full payload |
| Storage | Can be large | Usually smaller |
| Use | Deep packet investigation | Traffic behavior analysis |

### Tools for PCAP analysis

- Wireshark.
- TShark.
- tcpdump.
- Zeek.
- Suricata.

### Capture packets

```bash
sudo tcpdump -i eth0 -w network.pcap
```

### Read packets

```bash
tcpdump -r network.pcap
```

### Display packet details

```bash
tcpdump -nn -r network.pcap
```

### Open in Wireshark

```bash
wireshark network.pcap
```

### Useful Wireshark display filters

Show DNS traffic:

```text
dns
```

Show HTTP traffic:

```text
http
```

Show TCP traffic:

```text
tcp
```

Show traffic involving a specific IP:

```text
ip.addr == 192.168.1.10
```

Show traffic to a specific port:

```text
tcp.port == 443
```

Show TCP SYN packets:

```text
tcp.flags.syn == 1
```

Show failed TCP connection attempts may require examining TCP resets, retransmissions, and handshake behavior rather than relying on a single filter.

### Important security consideration

PCAP files may contain sensitive information, including internal IP addresses, session metadata, and unencrypted application data.

Protect captured files and do not share them publicly without reviewing their contents.

---

## 11. Basic Detection Rules

A detection rule describes conditions under which a security system should generate an alert.

Rules can be based on:
- Known attack signatures.
- Network behavior.
- Protocol patterns.
- Connection frequency.
- Unusual destinations.
- Authentication events.

### Example 1: Repeated failed login attempts

Detection logic:

```text
IF failed_login_attempts > 10
WITHIN 5 minutes
FROM the same source
THEN generate an alert
```

### Example 2: Unusual outbound traffic

```text
IF outbound_data_volume > normal_baseline
AND destination is unusual
THEN generate an alert
```

### Example 3: Possible port scanning

```text
IF one source contacts many destination ports
ON one or more hosts
WITHIN a short time
THEN generate a possible port-scan alert
```

### Example 4: Suspicious DNS activity

```text
IF a host generates an unusually high number
of DNS queries
OR contacts suspicious domains
THEN investigate
```

### Example Suricata rule

The following is a simple illustrative rule that alerts on outbound DNS queries from a monitored network to external destinations. It is not, by itself, proof of malicious activity.

```text
alert dns $HOME_NET any -> !$HOME_NET any (
    msg:"DNS query from internal network to external destination";
    dns.query;
    sid:1000001;
    rev:1;
)
```

### Understanding the rule

- `alert`: Generate an alert.
- `dns`: Inspect DNS traffic.
- `$HOME_NET`: Configured internal network.
- `any`: Any source port.
- `!$HOME_NET`: Destination outside the configured internal network.
- `msg`: Alert message.
- `dns.query`: Match DNS query traffic.
- `sid`: Unique signature ID.
- `rev`: Rule revision.

### Good detection rule practices

- Keep rules specific enough to be useful.
- Avoid unnecessary alerts.
- Include meaningful alert messages.
- Test rules before production deployment.
- Document rule purpose.
- Review false positives.
- Update rules when threats change.

---

## 12. Zeek — Overview

Zeek is an open-source network security monitoring and network analysis platform.

It observes network traffic and generates detailed logs describing network activity.

Unlike a traditional packet-blocking firewall, Zeek is primarily used for monitoring, analysis, and investigation.

### What Zeek can monitor

- HTTP.
- DNS.
- SSL/TLS.
- SSH.
- SMTP.
- Connections.
- Files transferred over supported protocols.

### Important Zeek logs

| Log | Information |
|---|---|
| `conn.log` | Network connection summaries |
| `dns.log` | DNS queries and responses |
| `http.log` | HTTP activity |
| `ssl.log` | TLS-related information |
| `files.log` | Observed file information |
| `notice.log` | Important notices generated by Zeek |

Log availability depends on the traffic, enabled analyzers, and Zeek configuration.

### Example

A Zeek connection log can help answer:

- Which internal host connected to an external server?
- Which protocol was used?
- How long did the connection last?
- How much data was transferred?
- Was the connection successful?

### Basic Zeek commands

Check the version:

```bash
zeek --version
```

Analyze a PCAP:

```bash
zeek -r capture.pcap
```

Zeek generally creates log files in the current working directory.

List generated logs:

```bash
ls
```

Inspect connection logs:

```bash
cat conn.log
```

Inspect DNS logs:

```bash
cat dns.log
```

### Why Zeek is useful

- Network visibility.
- Security investigations.
- Protocol analysis.
- Threat hunting.
- Network behavior monitoring.
- Generating structured logs for SIEM platforms.

**Remember:** Zeek is especially useful for understanding what happened on a network, not simply blocking packets.

---

## 13. Suricata — Overview

Suricata is an open-source network threat detection engine.

It can perform:
- Intrusion Detection (IDS).
- Intrusion Prevention (IPS).
- Network Security Monitoring (NSM).

It analyzes network traffic using signatures and other detection capabilities.

### Important features

- Signature-based detection.
- Protocol identification.
- Network traffic inspection.
- File identification.
- Alert generation.
- JSON logging.
- IPS operation when properly configured.

### Important Suricata logs

| Log | Purpose |
|---|---|
| `eve.json` | Structured event and alert information |
| `fast.log` | Human-readable alert output |
| `stats.log` | Statistics |
| `http.log` | HTTP-related logging when configured |

### Check Suricata version

```bash
suricata --version
```

### Check configuration

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

### Run Suricata against a PCAP

```bash
sudo suricata -r capture.pcap -c /etc/suricata/suricata.yaml
```

### Inspect alerts

Depending on the configuration and output directory:

```bash
sudo tail -f /var/log/suricata/fast.log
```

Or inspect structured events:

```bash
sudo tail -f /var/log/suricata/eve.json
```

### Example rule

```text
alert icmp any any -> any any (
    msg:"ICMP packet detected";
    itype:8;
    sid:1000002;
    rev:1;
)
```

This illustrative rule alerts on ICMP echo requests.

### Why Suricata is useful

- Detects suspicious traffic.
- Generates security alerts.
- Supports custom detection rules.
- Can analyze PCAP files.
- Can integrate with SIEM platforms.
- Can operate in IDS or IPS deployments.

---

## 14. Snort — Overview

Snort is an open-source network intrusion detection and prevention system.

It analyzes network traffic and compares it against configured rules to identify suspicious activity.

### Main capabilities

- Network traffic inspection.
- Signature-based detection.
- Alert generation.
- Packet logging.
- Intrusion prevention when deployed appropriately.

### Snort rule structure

A simplified Snort rule follows this structure:

```text
action protocol source_ip source_port -> destination_ip destination_port (options)
```

### Example rule

```text
alert icmp any any -> any any (
    msg:"ICMP traffic detected";
    sid:1000003;
    rev:1;
)
```

### Rule components

| Component | Meaning |
|---|---|
| `alert` | Generate an alert |
| `icmp` | Protocol |
| `any` | Any source IP |
| `any` | Any source port |
| `->` | Traffic direction |
| `msg` | Alert message |
| `sid` | Signature ID |
| `rev` | Rule revision |

### Snort vs Suricata

| Feature | Snort | Suricata |
|---|---|---|
| Purpose | IDS/IPS | IDS/IPS/NSM |
| Rule system | Snort rules | Snort-compatible rule syntax with extensions |
| Protocol analysis | Yes | Yes |
| Multi-threading | Depends on version and architecture | Designed for multi-threaded operation |
| JSON logging | Supported in modern versions | Strong EVE JSON support |
| Common use | Network threat detection | Network threat detection and monitoring |

Both tools are useful for learning network intrusion detection.

---

## 15. SIEM Fundamentals

SIEM stands for Security Information and Event Management.

A SIEM platform collects, centralizes, analyzes, and correlates security events from multiple sources.

It helps security teams identify suspicious activities and investigate incidents.

### How SIEM works

```text
Firewall Logs --------+
Server Logs ----------+
Endpoint Alerts ------+
IDS/IPS Alerts -------+----> SIEM Platform
DNS Logs -------------+            |
Application Logs -----+            |
                                    |
                          Correlation and Analysis
                                    |
                              Security Alerts
                                    |
                              Security Analyst
```

### Main SIEM functions

**1. Log Collection**

Collects events from different systems.

**2. Log Normalization**

Converts different log formats into a more consistent structure.

**3. Event Correlation**

Connects related events to identify possible attacks.

**4. Alerting**

Generates alerts based on detection rules.

**5. Dashboards and Reporting**

Provides visibility into security activity.

**6. Investigation**

Helps analysts search and investigate historical events.

### Example

A SIEM receives these events:

```text
10:00 - Multiple failed SSH logins
10:02 - Successful SSH login
10:04 - New privileged account created
10:06 - Large outbound data transfer
```

Individually, these events may require investigation.

When correlated, they may indicate a compromised server.

### Popular SIEM platforms

- Splunk Enterprise Security.
- Microsoft Sentinel.
- IBM QRadar.
- Elastic Security.
- Wazuh.

### SIEM vs IDS

| Feature | IDS | SIEM |
|---|---|---|
| Main purpose | Detect suspicious network or system activity | Centralize and analyze security events |
| Data | Network traffic or host events | Logs and security events from many sources |
| Correlation | May have limited correlation | Strong event correlation capabilities |
| Output | Alerts | Alerts, dashboards, investigations, reports |

**Remember:** An IDS can send alerts to a SIEM. A SIEM can correlate those alerts with other events.

---

## 16. Network Incident Investigation

Network incident investigation is the process of examining network activity to understand whether a security incident occurred, what happened, which systems were affected, and how the incident should be handled.

### Common investigation questions

- Which device was involved?
- What was the source IP address?
- What was the destination IP address?
- Which ports and protocols were used?
- When did the activity begin?
- Was the activity successful?
- What data was transferred?
- Were other systems affected?
- Is the activity still occurring?

### Investigation workflow

**Step 1: Identify the alert**

Example:

```text
Alert: Suspicious outbound connection
Source: 192.168.1.25
Destination: 203.0.113.50
Protocol: TCP
Port: 443
```

**Step 2: Collect evidence**

Collect:
- Firewall logs.
- DNS logs.
- Authentication logs.
- Endpoint security alerts.
- Network flow records.
- PCAP files, where available.

**Step 3: Establish a timeline**

Create a timeline of relevant events.

| Time | Event |
|---|---|
| 10:00 | User logged in |
| 10:05 | Suspicious DNS query |
| 10:07 | External connection established |
| 10:12 | Unusual data transfer |
| 10:15 | Security alert generated |

**Step 4: Identify affected systems**

Determine whether the activity is limited to one computer or involves multiple systems.

**Step 5: Determine severity**

Evaluate:
- Business impact.
- Data sensitivity.
- Number of affected systems.
- Whether unauthorized access occurred.
- Whether the attack is ongoing.

**Step 6: Contain the incident**

Follow the organization's response plan to isolate affected systems or block malicious communication.

**Step 7: Eradicate and recover**

Remove the cause of the incident, restore systems, and verify that they are secure.

**Step 8: Document findings**

Record:
- Incident summary.
- Evidence.
- Timeline.
- Root cause.
- Actions taken.
- Recovery status.
- Recommendations.

### Useful investigation commands

Show active network connections:

```bash
ss -tunap
```

Show routing information:

```bash
ip route
```

Show IP configuration:

```bash
ip addr
```

Check DNS resolution:

```bash
dig example.com
```

Inspect a packet capture:

```bash
tcpdump -nn -r capture.pcap
```

Inspect system logs:

```bash
sudo journalctl -n 100
```

**Important:** Investigation must preserve evidence, maintain accurate timestamps, and follow the organization's legal and operational procedures.

---

# Practical Lab Exercises

Use your own Kali Linux virtual machine, local test services, and traffic captures. Do not scan or intercept networks that you do not own or have explicit permission to test.

## Lab 1: Discover Your Local Network

**Objective:** Understand your own network configuration.

Check your IP address:

```bash
ip addr
```

Check the default gateway:

```bash
ip route
```

View ARP/neighbor information:

```bash
ip neigh
```

Questions:
1. What is your local IP address?
2. What is your subnet?
3. What is your default gateway?
4. Which devices appear in your neighbor table?

## Lab 2: Scan Your Own Test Machine

**Objective:** Understand open ports and service enumeration.

First, identify your test machine's IP address.

Scan it:

```bash
nmap <YOUR_TEST_MACHINE_IP>
```

Detect service versions:

```bash
nmap -sV <YOUR_TEST_MACHINE_IP>
```

Questions:
1. Which ports are open?
2. Which services are running?
3. Are any unnecessary services exposed?
4. Which services should be restricted?

## Lab 3: Capture DNS Traffic

**Objective:** Understand packet capture and DNS.

Start a capture:

```bash
sudo tcpdump -i any -w dns-lab.pcap port 53
```

In another terminal, perform a DNS lookup:

```bash
dig example.com
```

Stop the capture using `Ctrl + C`.

Read the captured packets:

```bash
tcpdump -nn -r dns-lab.pcap
```

Open the file in Wireshark:

```bash
wireshark dns-lab.pcap
```

Questions:
1. What is the source IP?
2. What is the destination IP?
3. Which DNS query was made?
4. Was the query sent over UDP or TCP?

## Lab 4: Analyze a PCAP with Zeek

**Objective:** Understand network security monitoring.

Use a PCAP you generated yourself.

Run:

```bash
zeek -r dns-lab.pcap
```

Inspect:

```bash
cat dns.log
```

Also inspect:

```bash
cat conn.log
```

Questions:
1. What DNS requests were observed?
2. Which hosts communicated?
3. Which protocols were used?
4. What information does Zeek record?

## Lab 5: Analyze Traffic with Suricata

**Objective:** Understand IDS alert generation.

Check Suricata:

```bash
suricata --version
```

Test its configuration:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Analyze your own PCAP:

```bash
sudo suricata -r dns-lab.pcap -c /etc/suricata/suricata.yaml
```

Inspect the generated logs:

```bash
sudo tail -n 30 /var/log/suricata/fast.log
```

Questions:
1. Did Suricata generate any alerts?
2. Which rules were triggered?
3. What does the alert message mean?
4. How would you investigate an unexpected alert?

## Lab 6: Understand Linux Network Connections

**Objective:** Inspect active connections and listening services.

Show listening TCP and UDP sockets:

```bash
sudo ss -tulnp
```

Show established TCP connections:

```bash
ss -tn state established
```

Identify processes using network connections:

```bash
sudo ss -tunap
```

Questions:
1. Which services are listening?
2. Which ports are exposed?
3. Which processes own those ports?
4. Are any services unnecessary?

---

# Important Tools in This Phase

| Tool | Main purpose | Category |
|---|---|---|
| Nmap | Port scanning and service discovery | Reconnaissance |
| Wireshark | Packet inspection | Traffic analysis |
| tcpdump | Command-line packet capture | Traffic analysis |
| TShark | Command-line packet analysis | Traffic analysis |
| Zeek | Network security monitoring | Network monitoring |
| Suricata | IDS/IPS and network monitoring | Threat detection |
| Snort | IDS/IPS | Threat detection |
| Netcat | Network connection testing | Networking |
| dig | DNS investigation | DNS analysis |
| Wazuh | Security monitoring and SIEM-related capabilities | Security monitoring |
| Splunk | Log analysis and SIEM | SIEM |
| Elastic Security | Security analytics and SIEM capabilities | SIEM |

---

# Phase 12: Important Differences to Remember

| Concepts | Key difference |
|---|---|
| Threat vs Vulnerability | Potential danger vs system weakness |
| Vulnerability vs Exploit | Weakness vs method of abusing it |
| DoS vs DDoS | Limited attacking sources vs distributed sources |
| IDS vs IPS | Detection vs detection and prevention |
| Signature vs Anomaly Detection | Known patterns vs unusual behavior |
| False Positive vs False Negative | Normal activity incorrectly flagged vs malicious activity missed |
| PCAP vs Flow Records | Packet-level data vs communication summaries |
| Zeek vs Suricata | Network analysis and monitoring vs rule-based threat detection and prevention |
| Snort vs Wireshark | Intrusion detection/prevention vs packet analysis |
| IDS vs SIEM | Detects suspicious activity vs centralizes and correlates security events |
| Port Scanning vs Enumeration | Finds port states vs investigates services and their details |
| IP Spoofing vs Session Hijacking | Forging a network source address vs taking over an authenticated session |

---

# Quick Revision

1. A threat is a potential source of harm.
2. A vulnerability is a weakness in a system.
3. An exploit takes advantage of a vulnerability.
4. Risk describes the likelihood and impact of potential harm.
5. Attack surface means all possible points through which a system can be attacked.
6. Threat modeling identifies possible threats before they cause damage.
7. Spoofing means disguising an identity or source.
8. Sniffing means capturing and analyzing network traffic.
9. MITM attacks involve intercepting communication between parties.
10. Replay attacks reuse previously captured messages.
11. DNS spoofing manipulates DNS resolution.
12. ARP spoofing manipulates IP-to-MAC address mappings in IPv4 local networks.
13. DoS attempts to make a service unavailable.
14. DDoS uses distributed sources to overwhelm a target.
15. A SYN flood abuses the TCP handshake.
16. Amplification attacks use services to generate larger responses toward a victim.
17. Session hijacking involves taking over a valid session.
18. IP spoofing forges the source IP address.
19. Port scanning identifies open, closed, and filtered ports.
20. Service enumeration investigates services running on discovered ports.
21. Network segmentation separates systems into controlled network sections.
22. Rate limiting restricts excessive requests.
23. IDS detects suspicious activity.
24. IPS can block suspicious traffic.
25. NDR analyzes network behavior and supports threat investigation.
26. Secure configuration reduces unnecessary exposure.
27. Patching fixes known software vulnerabilities.
28. Incident response manages security incidents.
29. Signature-based detection searches for known patterns.
30. Anomaly-based detection identifies unusual behavior.
31. A false positive incorrectly flags legitimate activity.
32. A false negative fails to detect malicious activity.
33. A network baseline describes normal network behavior.
34. Centralized logging collects logs from multiple systems.
35. Alert triage prioritizes and investigates alerts.
36. Flow records summarize network communications.
37. PCAP files store captured packets.
38. Zeek generates detailed network activity logs.
39. Suricata performs IDS, IPS, and network monitoring.
40. Snort is a network intrusion detection and prevention system.
41. SIEM collects, correlates, and analyzes security events.

---

# Interview Questions

## Beginner Level

1. What is the difference between a threat, vulnerability, and exploit?
2. What is risk in cybersecurity?
3. What is an attack surface?
4. What is threat modeling?
5. What is spoofing?
6. What is network sniffing?
7. What is a Man-in-the-Middle attack?
8. What is a replay attack?
9. What is DNS spoofing?
10. What is ARP spoofing?
11. What is the difference between DoS and DDoS?
12. What is IP spoofing?
13. What is port scanning?
14. What is service enumeration?
15. What is network segmentation?

## Intermediate Level

16. Explain how a SYN flood attack works.
17. What are amplification attacks?
18. How can session hijacking happen?
19. What are the limitations of IP spoofing?
20. How does rate limiting protect an API?
21. What is the difference between IDS and IPS?
22. Explain signature-based detection.
23. Explain anomaly-based detection.
24. What are false positives and false negatives?
25. What is a network traffic baseline?
26. Why is centralized logging important?
27. What is alert triage?
28. What is the difference between PCAP and NetFlow?
29. What is the role of Zeek?
30. What is the role of Suricata?

## Advanced Level

31. Explain how a network security analyst investigates suspicious outbound traffic.
32. How can a company reduce its network attack surface?
33. Explain how network segmentation limits lateral movement.
34. How would you investigate a suspected SYN flood?
35. How can you identify possible DNS tunneling?
36. How would you investigate repeated failed SSH logins?
37. How can IDS alerts be integrated into a SIEM?
38. What are the limitations of signature-based detection?
39. How would you reduce false positives in a detection system?
40. Explain the incident response lifecycle.
41. How do network flow records help detect data exfiltration?
42. What is the difference between Zeek and Suricata?
43. How would you investigate a suspected compromised endpoint?
44. What evidence should be preserved during a network incident?
45. How do you determine whether unusual traffic is malicious or legitimate?

---

# How This Phase Connects to Your Cybersecurity Goal

This phase supports several areas of cybersecurity:

| Area | What this phase teaches you |
|---|---|
| Network Security | Attacks, defenses, segmentation, monitoring |
| SOC Analysis | IDS alerts, logs, SIEM, incident investigation |
| Threat Hunting | Baselines, suspicious traffic, network flows |
| Penetration Testing | Port scanning, enumeration, attack surfaces |
| Web Application Security | Session security, spoofing concepts, rate limiting, threat modeling |
| Bug Bounty | Understanding exposed services, attack paths, and application-level defenses |

## What should you prioritize?

Since your primary direction is web and application security, prioritize these topics:

1. Threat, vulnerability, exploit, and risk.
2. Attack surface and threat modeling.
3. MITM and session hijacking.
4. DNS spoofing and ARP spoofing concepts.
5. Port scanning and service enumeration.
6. Network segmentation.
7. Rate limiting.
8. IDS and IPS fundamentals.
9. PCAP analysis with Wireshark.
10. Incident investigation fundamentals.

Learn Zeek, Suricata, Snort, and SIEM concepts to understand network defense, but you do not need to become an expert in every monitoring platform before starting web application security.

**Important distinction:** Web application security and network security are related but separate specializations. You can start learning OWASP Top 10, HTTP security, authentication, authorization, API security, and Burp Suite without mastering SOC operations or wireless security first.

Your networking foundation should help you understand what happens underneath an application—not delay your practical web security journey.
