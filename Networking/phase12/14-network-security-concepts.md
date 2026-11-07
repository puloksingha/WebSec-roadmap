
# Phase 12: Network Security Concepts

## 1. What Is Network Security?

Network Security refers to the policies, technologies, tools, and practices used to protect computer networks from unauthorized access, attacks, misuse, modification, and data theft.

Its primary goals are:

- **Confidentiality:** Only authorized users should access information.
- **Integrity:** Data should not be modified without authorization.
- **Availability:** Network services should remain accessible when needed.

These three principles are known as the **CIA Triad**.

### Example

Suppose you use an online banking application:

- Confidentiality: Attackers should not be able to read your banking information.
- Integrity: Attackers should not be able to modify your account balance.
- Availability: You should be able to access banking services when required.

## 2. CIA Triad

| Principle | Meaning | Example |
|---|---|---|
| Confidentiality | Protect information from unauthorized access | Encryption |
| Integrity | Protect information from unauthorized modification | Hashing and digital signatures |
| Availability | Keep systems and services operational | Backups and DDoS protection |

### A. Confidentiality

Confidentiality ensures that sensitive information is accessible only to authorized individuals and systems.

Common techniques:

- Encryption
- Authentication
- Access control
- Network segmentation
- Secure communication protocols

Example:

HTTPS encrypts communication between a browser and a web server using TLS.

### B. Integrity

Integrity ensures that information remains accurate and has not been altered unexpectedly.

Common techniques:

- Cryptographic hashing
- Digital signatures
- Message Authentication Codes (MACs)
- File integrity monitoring

Example:

A website can use a cryptographic hash to detect whether a downloaded file has been modified.

### C. Availability

Availability ensures that systems, applications, and network resources remain accessible to legitimate users.

Common techniques:

- Redundant servers
- Load balancing
- Backups
- Disaster recovery
- DDoS protection
- Network monitoring

Example:

If one web server fails, a load balancer can direct requests to another healthy server.

## 3. Common Network Attacks

Network attacks attempt to compromise confidentiality, integrity, or availability.

### A. Man-in-the-Middle (MITM) Attack

A Man-in-the-Middle attack occurs when an attacker secretly intercepts or potentially modifies communication between two parties.

Example:

A user connects to an insecure public Wi-Fi network. An attacker on the same network attempts to intercept the user's communication.

Possible consequences:

- Credential theft
- Session hijacking
- Data interception
- Communication manipulation

Protection:

- Use HTTPS.
- Validate TLS certificates.
- Avoid sending sensitive information over untrusted connections.
- Use properly configured VPNs when appropriate.
- Avoid ignoring browser certificate warnings.

### B. Denial-of-Service (DoS)

A Denial-of-Service attack attempts to make a service unavailable by exhausting its resources or exploiting a weakness.

Example:

An attacker sends excessive requests to a web server, preventing legitimate users from accessing it.

Possible targets:

- Web servers
- DNS servers
- Network infrastructure
- APIs

### C. Distributed Denial-of-Service (DDoS)

A Distributed Denial-of-Service attack uses multiple systems to overwhelm a target.

Difference:

| DoS | DDoS |
|---|---|
| Usually originates from one source | Uses multiple sources |
| Easier to identify the source in some cases | More difficult to distinguish malicious traffic |
| Limited attack infrastructure | Often uses botnets or distributed systems |

Protection:

- Rate limiting
- Traffic filtering
- CDN-based protection
- DDoS mitigation services
- Network monitoring
- Traffic scrubbing

### D. IP Spoofing

IP spoofing occurs when an attacker forges the source IP address in an IP packet.

Purpose:

- Hide the actual source of traffic.
- Bypass weak IP-based filtering.
- Support certain network attacks.

Important:

IP spoofing changes the source address in a packet. It does not automatically allow an attacker to receive responses sent to the forged address.

Protection:

- Ingress and egress filtering
- Anti-spoofing rules
- Proper firewall configuration
- Network monitoring

### E. ARP Spoofing / ARP Poisoning

ARP spoofing occurs when an attacker sends forged ARP messages to associate their MAC address with another device's IP address.

It can allow traffic interception within a local network.

Example:

A victim believes that the attacker's MAC address belongs to the network gateway.

Possible consequences:

- Traffic interception
- MITM attacks
- Network disruption

Protection:

- Dynamic ARP Inspection (DAI)
- DHCP snooping
- Static ARP entries in limited environments
- Network segmentation
- Secure switch configuration

### F. DNS Spoofing

DNS spoofing occurs when false DNS information causes a user or system to connect to an unintended IP address.

Example:

A user tries to visit `example.com`, but manipulated DNS information directs them to a malicious server.

Possible consequences:

- Phishing
- Credential theft
- Malware distribution

Protection:

- DNSSEC where supported
- Trusted DNS resolvers
- Secure DNS configuration
- HTTPS certificate validation
- Monitoring DNS responses

Important distinction:

DNSSEC helps authenticate DNS data. It does not encrypt DNS queries.

### G. Packet Sniffing

Packet sniffing means capturing and inspecting network packets traveling across a network.

It can be used for legitimate troubleshooting and security monitoring, or maliciously to collect sensitive information.

Common tools:

- Wireshark
- tcpdump
- TShark

Protection:

- Use HTTPS and TLS.
- Avoid transmitting credentials in plaintext.
- Secure wireless networks.
- Apply proper network segmentation.

### H. Session Hijacking

Session hijacking occurs when an attacker obtains or takes control of a valid user's session.

Example:

An attacker steals a session cookie and attempts to use it to access a victim's account.

Protection:

- HTTPS everywhere
- Secure and HttpOnly cookie attributes
- SameSite cookie configuration
- Session expiration
- Session rotation after authentication
- Multi-factor authentication

**Web security connection:** Session hijacking is particularly important in web application security because web applications commonly use cookies or tokens to maintain authenticated sessions.

## 4. Authentication and Authorization

These two concepts are fundamental to network and application security.

### Authentication

Authentication verifies the identity of a user or system.

It answers:

**Who are you?**

Examples:

- Username and password
- OTP
- Biometrics
- Security keys
- Digital certificates

### Authorization

Authorization determines what an authenticated user is allowed to access or perform.

It answers:

**What are you allowed to do?**

Example:

A student can view their marks, but only an authorized administrator can modify them.

### Difference

| Authentication | Authorization |
|---|---|
| Verifies identity | Checks permissions |
| Happens before access is granted | Determines allowed actions |
| Example: Login | Example: Admin-only access |

## 5. Access Control Models

Access control determines who can access a resource and what actions they can perform.

### A. DAC — Discretionary Access Control

The resource owner decides who can access the resource.

Example:

A file owner grants another user permission to read a file.

### B. MAC — Mandatory Access Control

Access is controlled by a central security policy, often using security classifications and clearance levels.

Example:

Military information classified as confidential, secret, or top secret.

### C. RBAC — Role-Based Access Control

Permissions are assigned according to user roles.

Example:

| Role | Permissions |
|---|---|
| Admin | Manage users and settings |
| Teacher | Manage student records |
| Student | View personal records |

### D. ABAC — Attribute-Based Access Control

Access decisions are made using attributes such as:

- User department
- Device security status
- Location
- Time
- Resource sensitivity

Example:

An employee can access a company resource only from an approved device during permitted working hours.

## 6. Encryption Basics

Encryption converts readable information (plaintext) into unreadable information (ciphertext) using a cryptographic algorithm and key.

Decryption converts ciphertext back into readable information.

### A. Symmetric Encryption

The same secret key is used for encryption and decryption.

Examples:

- AES
- ChaCha20

Advantages:

- Fast
- Efficient for large amounts of data

Disadvantage:

The secret key must be securely shared between communicating parties.

### B. Asymmetric Encryption

Uses a public key and a private key.

- Public key: Can be shared with others.
- Private key: Must be kept secret.

Examples:

- RSA
- Elliptic Curve Cryptography (ECC)

Uses include:

- Key exchange
- Digital signatures
- Authentication

### Symmetric vs Asymmetric Encryption

| Symmetric | Asymmetric |
|---|---|
| One shared secret key | Public and private key pair |
| Generally faster | Generally slower |
| Used for bulk encryption | Used for key establishment and signatures |
| Example: AES | Example: RSA |

### C. Hashing

Hashing converts input data into a fixed-length digest.

Examples:

- SHA-256
- SHA-3

Properties:

- Deterministic: The same input produces the same hash.
- One-way: Designed to be computationally infeasible to reverse.
- Small changes in input produce significantly different digests.

Important:

Hashing is not encryption. A hash is not decrypted to recover the original input.

Password storage:

Use dedicated password-hashing algorithms such as:

- Argon2id
- bcrypt
- scrypt

Do not store passwords as plaintext or as simple unsalted SHA-256 hashes.

## 7. TLS and Secure Communication

TLS (Transport Layer Security) is a cryptographic protocol that protects communication between systems.

It provides:

- Confidentiality
- Integrity
- Server authentication
- Optional client authentication

HTTPS means HTTP communication protected by TLS.

### Simplified TLS Handshake

1. Client sends a ClientHello message.
2. Server responds with ServerHello and its selected parameters.
3. Server provides its certificate when required.
4. Client validates the certificate.
5. Both parties establish shared session keys.
6. Encrypted application communication begins.

Modern TLS commonly uses ephemeral key exchange to establish shared session keys and symmetric encryption to protect application data.

### Why TLS Matters

Without secure transport, sensitive information may be exposed or modified in transit.

TLS helps protect:

- Login credentials
- Session cookies
- Personal information
- Payment information
- API requests and responses

## 8. Network Security Devices and Technologies

### A. Firewall

A firewall monitors and controls network traffic according to defined security rules.

Common types:

- Packet-filtering firewall
- Stateful firewall
- Proxy firewall
- Next-Generation Firewall (NGFW)

Example:

A firewall blocks unsolicited inbound connections to a server.

### B. IDS — Intrusion Detection System

An IDS monitors network or system activity and identifies suspicious behavior.

Its primary role is detection and alerting.

Types:

- NIDS: Network-based Intrusion Detection System
- HIDS: Host-based Intrusion Detection System

### C. IPS — Intrusion Prevention System

An IPS detects malicious activity and can automatically block or prevent it.

### IDS vs IPS

| IDS | IPS |
|---|---|
| Detects suspicious activity | Detects and can block suspicious activity |
| Commonly alerts administrators | Can take preventive action |
| Often deployed out-of-band | Often deployed inline |

### D. WAF — Web Application Firewall

A WAF protects web applications by inspecting HTTP/HTTPS requests and responses.

It can help detect or block:

- SQL injection attempts
- Cross-Site Scripting (XSS) attempts
- Malicious HTTP requests
- Some automated attacks

Important:

A WAF is not a replacement for secure application code. It is one layer of defense.

### E. VPN — Virtual Private Network

A VPN creates an encrypted tunnel between a device and a VPN endpoint or between networks.

Common uses:

- Secure remote access
- Connecting office networks
- Protecting traffic over untrusted networks

A VPN does not automatically make a device anonymous or protect it from every attack.

## 9. Network Segmentation

Network segmentation divides a network into smaller, isolated sections.

Purpose:

- Limit unauthorized access.
- Reduce lateral movement.
- Separate sensitive systems.
- Contain security incidents.

Example:

A company may separate:

- Employee network
- Guest Wi-Fi
- Server network
- Database network
- Management network

### VLAN

A Virtual Local Area Network (VLAN) logically separates devices into different Layer 2 broadcast domains.

Example:

- VLAN 10: Employees
- VLAN 20: Guests
- VLAN 30: Servers

Communication between VLANs requires routing and can be controlled with firewall or access-control rules.

### DMZ — Demilitarized Zone

A DMZ is a network segment used to host systems that need to be accessible from less-trusted networks, such as the internet.

Example:

A public-facing web server may be placed in a DMZ while the internal database remains on a restricted network.

## 10. Zero Trust Security

Zero Trust is a security approach based on the principle:

**Never trust automatically; always verify.**

It assumes that no user, device, or network location should receive implicit trust.

Important principles:

- Verify every access request.
- Apply least-privilege access.
- Continuously evaluate security context.
- Monitor activity.
- Limit access to necessary resources.

Example:

An employee accessing a company application must authenticate and satisfy device-security requirements, even when connected to the company network.

## 11. Least Privilege Principle

The Principle of Least Privilege means giving users and systems only the permissions they need to perform their tasks.

Example:

A normal application user should not have administrator permissions.

Benefits:

- Reduces attack surface.
- Limits damage from compromised accounts.
- Reduces accidental changes.
- Helps prevent privilege escalation.

## 12. Security Monitoring and Logging

Security monitoring involves continuously observing systems and network traffic to identify suspicious activity.

Important log sources:

- Firewall logs
- DNS logs
- Authentication logs
- Web server logs
- IDS/IPS alerts
- Endpoint security logs
- VPN logs

### SIEM — Security Information and Event Management

A SIEM collects and analyzes security logs from multiple sources.

It helps security teams:

- Detect suspicious activity.
- Correlate events.
- Investigate incidents.
- Generate alerts.
- Support incident response.

Examples:

- Splunk
- Microsoft Sentinel
- Elastic Security

## 13. Network Hardening

Network hardening means reducing vulnerabilities and improving the security of network devices and services.

Common practices:

1. Change default passwords.
2. Disable unnecessary services.
3. Close unused ports.
4. Apply security updates.
5. Use strong authentication.
6. Configure firewalls correctly.
7. Enable logging and monitoring.
8. Use secure protocols.
9. Segment sensitive networks.
10. Restrict administrative access.
11. Back up configurations.
12. Review permissions regularly.

### Example

If a server does not need Telnet, disable it and use SSH for secure remote administration.

## 14. Common Network Security Protocols

| Protocol / Technology | Purpose |
|---|---|
| TLS | Secure communication |
| HTTPS | HTTP over TLS |
| SSH | Secure remote access |
| IPsec | Security at the IP layer |
| DNSSEC | DNS data authentication |
| 802.1X | Network access control |
| RADIUS | Centralized authentication, authorization, and accounting |
| SNMPv3 | Secure network device monitoring |
| WPA2/WPA3 | Wireless network security |

Important distinctions:

- SSH is preferred over Telnet for secure remote administration.
- SFTP operates over SSH; it is not the same as ordinary FTP.
- DNSSEC provides authenticity and integrity for DNS data, not encryption.
- IPsec can protect IP traffic at the network layer.

## 15. Network Security and Web Application Security

Network security and web application security are related, but they are not identical.

### Network Security Focus

- Firewalls
- Network protocols
- Routing and segmentation
- VPNs
- IDS/IPS
- Traffic monitoring
- Infrastructure protection

### Web Application Security Focus

- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Broken Access Control
- Authentication weaknesses
- Session management flaws
- Server-Side Request Forgery (SSRF)
- API security
- Business logic vulnerabilities

### How They Connect

Consider a web application:

1. DNS resolves its domain name.
2. TCP establishes a connection.
3. TLS protects communication.
4. HTTP carries application requests.
5. The application authenticates the user.
6. Authorization controls access to resources.
7. The database processes application queries.

A weakness at any layer can affect the overall security of the application.

**For your web security and bug bounty path:** Understand network security fundamentals, but prioritize HTTP, HTTPS, DNS, TLS, browser behavior, authentication, authorization, APIs, and application vulnerabilities. You do not need to become a network security specialist before learning web application security.

## 16. Practical Labs

Perform these exercises only on your own systems, local virtual machines, or environments where you have explicit permission.

### Lab 1: Inspect Network Connections

Command:

```bash
ss -tuln
```

Purpose:

- Display listening TCP and UDP sockets.
- Identify services listening on your machine.
- Understand which ports are exposed locally.

### Lab 2: Inspect Network Traffic Using Wireshark

Steps:

1. Open Wireshark.
2. Select your active network interface.
3. Start capturing packets.
4. Visit a website you control or a public website.
5. Observe DNS, TCP, TLS, and HTTP traffic where available.
6. Stop the capture and inspect packet details.

Useful display filters:

```text
dns
tcp
tls
http
icmp
```

Note: HTTPS application data is encrypted. You can usually inspect connection metadata and TLS handshake information, but not read protected application content without authorized decryption.

### Lab 3: Inspect DNS Resolution

Command:

```bash
nslookup example.com
```

Alternative:

```bash
dig example.com
```

Observe:

- DNS server used
- Resolved IP address
- DNS response information

### Lab 4: Inspect TLS Certificates

Command:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Observe:

- Certificate details
- TLS version
- Cipher suite
- Certificate chain

Press `Ctrl + C` to exit.

### Lab 5: Inspect Firewall Rules in Linux

For systems using UFW:

```bash
sudo ufw status verbose
```

For systems using nftables:

```bash
sudo nft list ruleset
```

Purpose:

Understand how firewall rules control network access.

Do not change firewall rules on a remote system unless you understand the impact and have recovery access.

### Lab 6: Check Network Routes

Command:

```bash
ip route
```

Purpose:

- Identify the default gateway.
- Understand routing decisions.
- Inspect network interfaces and routes.

## 17. Important Commands for Revision

| Command | Purpose |
|---|---|
| `ip addr` | View IP addresses |
| `ip route` | View routing table |
| `ss -tuln` | View listening sockets |
| `ping example.com` | Test basic reachability |
| `traceroute example.com` | Inspect network path |
| `dig example.com` | Query DNS |
| `nslookup example.com` | Resolve domain names |
| `tcpdump -i eth0` | Capture packets on an interface |
| `sudo ufw status` | Check UFW firewall status |
| `openssl s_client -connect example.com:443 -servername example.com` | Inspect TLS connection |

## 18. Quick Revision

- Network security protects network infrastructure, communication, and data.
- CIA stands for Confidentiality, Integrity, and Availability.
- MITM attacks involve intercepting communication.
- DoS attempts to make a service unavailable.
- DDoS uses multiple sources to overwhelm a target.
- IP spoofing forges the source IP address.
- ARP spoofing manipulates IP-to-MAC address mappings.
- DNS spoofing manipulates DNS resolution.
- Packet sniffing captures network traffic.
- Authentication verifies identity.
- Authorization determines permissions.
- Symmetric encryption uses a shared secret key.
- Asymmetric cryptography uses public and private keys.
- Hashing produces a digest and is not encryption.
- TLS protects communication.
- IDS detects suspicious activity.
- IPS can detect and block suspicious activity.
- WAF helps protect web applications.
- VPN creates an encrypted tunnel.
- Network segmentation limits access and lateral movement.
- Zero Trust requires verification rather than implicit trust.
- Least privilege limits unnecessary permissions.
- SIEM collects and analyzes security events.

## 19. Interview Questions

1. What is network security?
2. Explain the CIA Triad with examples.
3. What is the difference between confidentiality and integrity?
4. What is a Man-in-the-Middle attack?
5. Explain DoS and DDoS attacks.
6. What is IP spoofing?
7. What is ARP poisoning?
8. What is DNS spoofing?
9. What is packet sniffing?
10. What is session hijacking?
11. What is the difference between authentication and authorization?
12. Explain DAC, MAC, RBAC, and ABAC.
13. What is symmetric encryption?
14. What is asymmetric encryption?
15. What is hashing, and how is it different from encryption?
16. What is TLS?
17. What is the difference between IDS and IPS?
18. What is a WAF?
19. What is network segmentation?
20. What is a VLAN?
21. What is a DMZ?
22. Explain Zero Trust Security.
23. What is the Principle of Least Privilege?
24. What is SIEM?
25. How does network security support web application security?

## 20. Phase 12 Completion Checklist

- [ ] Understand the CIA Triad.
- [ ] Understand common network attacks.
- [ ] Differentiate authentication and authorization.
- [ ] Understand access control models.
- [ ] Understand encryption and hashing.
- [ ] Understand TLS and secure communication.
- [ ] Differentiate firewall, IDS, IPS, and WAF.
- [ ] Understand network segmentation, VLANs, and DMZ.
- [ ] Understand Zero Trust and least privilege.
- [ ] Understand security monitoring and SIEM.
- [ ] Practice basic network inspection commands.
- [ ] Inspect DNS, TCP, and TLS traffic using Wireshark.

**Phase 12 completed: Network Security Concepts.**
