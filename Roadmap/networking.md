# Complete Networking Roadmap for Cybersecurity

**Target:** Web Application Security, Application Security, and Authorized Penetration Testing  
**Level:** Beginner → Intermediate → Practical Security  
**Suggested duration:** 6–8 weeks for the core topics  
**Study time:** 45–60 minutes daily alongside Linux and Python

---

# Phase 1: Networking Fundamentals

## 1. Introduction to Computer Networking

- [ ] What is a computer network?
- [ ] Why do we need computer networks?
- [ ] Advantages and disadvantages of networking
- [ ] Network devices and network interfaces
- [ ] Hosts, clients, servers, and peers
- [ ] Data communication fundamentals
- [ ] Network protocols and standards
- [ ] Network architecture
- [ ] Network topology
- [ ] Physical vs logical topology
- [ ] LAN — Local Area Network
- [ ] WAN — Wide Area Network
- [ ] MAN — Metropolitan Area Network
- [ ] PAN — Personal Area Network
- [ ] WLAN — Wireless LAN
- [ ] Internet vs intranet vs extranet
- [ ] Public networks vs private networks
- [ ] Wired vs wireless networks
- [ ] Peer-to-peer vs client-server networking
- [ ] Bandwidth, throughput, and latency
- [ ] Jitter and packet loss
- [ ] Full-duplex vs half-duplex communication
- [ ] Unicast, multicast, broadcast, and anycast
- [ ] Circuit switching vs packet switching
- [ ] What is a network packet?
- [ ] Frames, packets, segments, and datagrams

**Practical tasks**

- [ ] Identify your computer's network interface.
- [ ] Check your current IP address.
- [ ] Identify your default gateway.
- [ ] Compare Wi-Fi and Ethernet.
- [ ] Observe latency using `ping`.

# Phase 2: OSI and TCP/IP Models

## 2. OSI Model

- [ ] What is the OSI model?
- [ ] Why networking models are useful
- [ ] Layer 1 — Physical
- [ ] Layer 2 — Data Link
- [ ] Layer 3 — Network
- [ ] Layer 4 — Transport
- [ ] Layer 5 — Session
- [ ] Layer 6 — Presentation
- [ ] Layer 7 — Application
- [ ] Responsibilities of each layer
- [ ] Protocols and devices associated with each layer
- [ ] Encapsulation and decapsulation
- [ ] How data travels from one layer to another
- [ ] Troubleshooting using the OSI model

## 3. TCP/IP Model

- [ ] What is the TCP/IP model?
- [ ] Network access layer
- [ ] Internet layer
- [ ] Transport layer
- [ ] Application layer
- [ ] OSI vs TCP/IP model
- [ ] Mapping protocols to layers
- [ ] Encapsulation in TCP/IP
- [ ] How a browser request travels through the stack
- [ ] How a server response returns to the client

**Practical task:** Explain the journey of an HTTPS request from your browser to a web server, including DNS, TCP, TLS, HTTP, and the return response.

# Phase 3: IP Addressing

## 4. IPv4 Fundamentals

- [ ] What is an IP address?
- [ ] IPv4 address structure
- [ ] Binary and decimal representation
- [ ] Network portion vs host portion
- [ ] Public vs private IPv4 addresses
- [ ] Private ranges: `10.0.0.0/8`
- [ ] Private ranges: `172.16.0.0/12`
- [ ] Private ranges: `192.168.0.0/16`
- [ ] Loopback: `127.0.0.0/8`
- [ ] Link-local addresses: `169.254.0.0/16`
- [ ] Unspecified address: `0.0.0.0`
- [ ] Limited broadcast: `255.255.255.255`
- [ ] Static vs dynamic IP addressing
- [ ] IP conflicts
- [ ] Network address and broadcast address
- [ ] Reserved IP addresses
- [ ] NAT and private addressing
- [ ] Why internal IPs are not generally routable on the public Internet

## 5. Subnetting and CIDR

- [ ] What is a subnet?
- [ ] Subnet masks
- [ ] CIDR notation
- [ ] Network prefixes
- [ ] `/8`, `/16`, `/24`, `/25`, `/26`, `/27`, `/28`, `/30`
- [ ] Calculating network addresses
- [ ] Calculating broadcast addresses
- [ ] Usable host ranges in traditional IPv4 subnets
- [ ] Number of addresses per subnet
- [ ] Subnetting practice
- [ ] VLSM — Variable Length Subnet Masking
- [ ] Route aggregation and summarization
- [ ] Supernetting fundamentals
- [ ] Special cases such as `/31` and `/32`

## 6. IPv6 Fundamentals

- [ ] Why IPv6 was introduced
- [ ] IPv6 address structure
- [ ] Hexadecimal representation
- [ ] IPv6 shorthand and address compression
- [ ] Global unicast addresses
- [ ] Link-local addresses
- [ ] Unique local addresses
- [ ] Multicast addresses
- [ ] Loopback: `::1`
- [ ] Unspecified address: `::`
- [ ] IPv6 prefix notation
- [ ] SLAAC — Stateless Address Autoconfiguration
- [ ] DHCPv6
- [ ] Neighbor Discovery Protocol
- [ ] IPv4 vs IPv6
- [ ] Dual-stack networks
- [ ] IPv6 security considerations
- [ ] IPv6 exposure and firewall configuration

**Practical tasks**

- [ ] Inspect IPv4 and IPv6 addresses on Linux.
- [ ] Calculate a `/24` subnet and its host range.
- [ ] Inspect your default route.
- [ ] Determine whether a machine has IPv6 connectivity.

# Phase 4: MAC Addresses and Ethernet

## 7. Data Link Layer

- [ ] What is a MAC address?
- [ ] MAC address format
- [ ] Unicast, multicast, and broadcast MAC addresses
- [ ] MAC addresses vs IP addresses
- [ ] Ethernet fundamentals
- [ ] Ethernet frames
- [ ] Frame headers and trailers
- [ ] MTU — Maximum Transmission Unit
- [ ] Jumbo frames — overview
- [ ] ARP — Address Resolution Protocol
- [ ] ARP requests and replies
- [ ] ARP cache
- [ ] `ip neigh`
- [ ] MAC address learning in switches
- [ ] Switches vs hubs
- [ ] Collision domains and broadcast domains
- [ ] VLANs — Virtual LANs
- [ ] 802.1Q VLAN tagging
- [ ] Trunk vs access ports
- [ ] Spanning Tree Protocol — basic purpose
- [ ] Port mirroring — overview
- [ ] ARP spoofing/poisoning — concepts and defenses

**Practical tasks**

- [ ] Find your MAC address.
- [ ] Inspect the ARP/neighbor table.
- [ ] Observe an ARP exchange in Wireshark on your own network.
- [ ] Explain why a switch needs MAC addresses.

# Phase 5: Transport Layer — TCP and UDP

## 8. TCP

- [ ] What is TCP?
- [ ] Connection-oriented communication
- [ ] TCP segment structure
- [ ] Source and destination ports
- [ ] Sequence and acknowledgment numbers
- [ ] SYN, ACK, FIN, and RST flags
- [ ] Three-way handshake
- [ ] Connection termination
- [ ] Reliable delivery
- [ ] Retransmissions
- [ ] Flow control
- [ ] Congestion control — fundamentals
- [ ] TCP windows
- [ ] TCP states
- [ ] Half-open connections — concepts
- [ ] Connection timeouts
- [ ] TCP vs UDP
- [ ] How TCP carries HTTP and HTTPS traffic

## 9. UDP

- [ ] What is UDP?
- [ ] Connectionless communication
- [ ] UDP datagram structure
- [ ] UDP ports
- [ ] No built-in delivery guarantee
- [ ] UDP vs TCP performance trade-offs
- [ ] Common UDP applications
- [ ] DNS over UDP and TCP
- [ ] QUIC and its use of UDP
- [ ] How applications add reliability when needed

## 10. Ports and Sockets

- [ ] What is a port?
- [ ] Source port vs destination port
- [ ] Well-known, registered, and dynamic ports
- [ ] Listening vs established ports
- [ ] What is a socket?
- [ ] IP address + port + transport protocol
- [ ] Binding to an interface
- [ ] `localhost` vs `0.0.0.0`
- [ ] Port forwarding
- [ ] Port conflicts
- [ ] Firewall rules and ports
- [ ] Service discovery and port scanning concepts

### Important ports to memorize

| Port | Common service |
|---|---|
| 20/21 | FTP data/control, depending on mode |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCPv4 |
| 80 | HTTP |
| 110 | POP3 |
| 123 | NTP |
| 143 | IMAP |
| 161/162 | SNMP |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 465/587 | Common SMTP submission ports |
| 500 | IKE/IPsec |
| 514 | Syslog, commonly UDP |
| 636 | LDAPS |
| 993 | IMAPS |
| 995 | POP3S |
| 1433 | Microsoft SQL Server, default |
| 3306 | MySQL, default |
| 3389 | RDP |
| 5432 | PostgreSQL, default |
| 5900 | VNC, commonly |
| 6379 | Redis, default |
| 8080 | Common alternate HTTP port |
| 8443 | Common alternate HTTPS port |
| 27017 | MongoDB, default |

Ports are conventions, not guarantees: a service can run on a different port.

# Phase 6: Network Devices and Routing

## 11. Networking Devices

- [ ] Network interface card (NIC)
- [ ] Repeater
- [ ] Hub
- [ ] Bridge
- [ ] Layer 2 switch
- [ ] Layer 3 switch
- [ ] Router
- [ ] Wireless access point
- [ ] Modem
- [ ] Firewall
- [ ] Proxy server
- [ ] Load balancer
- [ ] Gateway
- [ ] IDS and IPS
- [ ] Network tap
- [ ] Reverse proxy
- [ ] Content Delivery Network (CDN)

## 12. Routing Fundamentals

- [ ] What is routing?
- [ ] Routing table
- [ ] Default gateway
- [ ] Next-hop routing
- [ ] Directly connected routes
- [ ] Static vs dynamic routing
- [ ] Longest-prefix match
- [ ] Default route
- [ ] Route metrics
- [ ] ICMP and routing diagnostics
- [ ] NAT vs routing
- [ ] Policy-based routing — overview
- [ ] Asymmetric routing — overview
- [ ] BGP — purpose and basic concepts
- [ ] OSPF — purpose and basic concepts
- [ ] Autonomous systems — overview
- [ ] Traceroute and TTL/hop-limit behavior

**Practical tasks**

- [ ] Inspect the Linux routing table with `ip route`.
- [ ] Identify your default gateway.
- [ ] Use `traceroute` or `tracepath`.
- [ ] Diagnose a missing route in a lab.
- [ ] Explain how a router forwards packets between networks.

# Phase 7: Core Network Protocols

## 13. DNS — Domain Name System

- [ ] What is DNS?
- [ ] Domain names and fully qualified domain names
- [ ] DNS hierarchy
- [ ] Root, TLD, and authoritative name servers
- [ ] Recursive vs authoritative DNS servers
- [ ] DNS resolver and cache
- [ ] DNS resolution process
- [ ] DNS A records
- [ ] AAAA records
- [ ] CNAME records
- [ ] MX records
- [ ] NS records
- [ ] TXT records
- [ ] PTR records
- [ ] SOA records
- [ ] SRV records
- [ ] TTL and caching
- [ ] Forward vs reverse lookup
- [ ] DNS over UDP and TCP
- [ ] DNSSEC fundamentals
- [ ] DoH and DoT
- [ ] DNS misconfiguration
- [ ] DNS cache poisoning — concept and defenses
- [ ] Subdomain discovery — authorized testing
- [ ] DNS tunneling — detection concepts

## 14. DHCP

- [ ] What is DHCP?
- [ ] DHCP server and client
- [ ] DHCP DORA process
- [ ] Discover, Offer, Request, Acknowledge
- [ ] IP leases
- [ ] DHCP scopes and reservations
- [ ] DHCP options
- [ ] DHCP relay
- [ ] DHCPv4 vs DHCPv6
- [ ] Rogue DHCP server risks
- [ ] DHCP starvation — concept and defense

## 15. ARP and ICMP

- [ ] ARP purpose and operation
- [ ] ARP cache and expiration
- [ ] ICMP purpose
- [ ] Echo request and echo reply
- [ ] Destination unreachable
- [ ] Time exceeded
- [ ] TTL exceeded in traceroute
- [ ] IPv6 Neighbor Discovery
- [ ] Ping limitations
- [ ] ICMP filtering and troubleshooting
- [ ] ARP spoofing defenses
- [ ] Network discovery limitations

## 16. Other Important Protocols

- [ ] NTP — Network Time Protocol
- [ ] SNMP — Simple Network Management Protocol
- [ ] LDAP — directory services
- [ ] SMB — file sharing
- [ ] FTP vs SFTP vs FTPS
- [ ] SMTP, IMAP, and POP3
- [ ] SSH vs Telnet
- [ ] RDP — remote desktop
- [ ] Syslog
- [ ] IPsec
- [ ] QUIC
- [ ] WebSocket
- [ ] MQTT — basic purpose
- [ ] RPC — basic purpose

# Phase 8: NAT, Firewalls, and Network Segmentation

## 17. NAT

- [ ] What is Network Address Translation?
- [ ] Static NAT
- [ ] Dynamic NAT
- [ ] PAT / NAT overload
- [ ] Source NAT vs destination NAT
- [ ] Port forwarding
- [ ] NAT traversal — overview
- [ ] NAT limitations
- [ ] NAT vs firewall
- [ ] NAT and private IP addresses
- [ ] Double NAT
- [ ] Hairpin NAT — overview

## 18. Firewalls

- [ ] What is a firewall?
- [ ] Packet-filtering firewalls
- [ ] Stateful firewalls
- [ ] Stateless filtering
- [ ] Application-layer firewalls
- [ ] Web Application Firewall (WAF)
- [ ] Inbound vs outbound rules
- [ ] Allowlist vs blocklist
- [ ] Default-deny policy
- [ ] Egress filtering
- [ ] Firewall logs
- [ ] Linux `nftables`
- [ ] `ufw` basics
- [ ] Network firewall vs host firewall
- [ ] Common firewall misconfigurations
- [ ] Testing firewall rules safely

## 19. VLANs, DMZ, and Network Segmentation

- [ ] What is network segmentation?
- [ ] VLANs
- [ ] Subnets vs VLANs
- [ ] Inter-VLAN routing
- [ ] DMZ — demilitarized zone
- [ ] Internal vs external network zones
- [ ] Guest networks
- [ ] Server isolation
- [ ] Management networks
- [ ] Microsegmentation — overview
- [ ] Zero Trust networking — fundamentals
- [ ] Lateral movement — concept
- [ ] Restricting access between application tiers

**Cybersecurity connection:** Understand why a web server, database, and management interface should not all be exposed to the same users or networks.

# Phase 9: HTTP, HTTPS, and Web Networking

## 20. HTTP Fundamentals

- [ ] What is HTTP?
- [ ] Client-server request-response model
- [ ] HTTP versions: 1.0, 1.1, 2, and 3
- [ ] HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- [ ] HTTP status codes: 1xx, 2xx, 3xx, 4xx, 5xx
- [ ] Request line and status line
- [ ] Request and response headers
- [ ] Request body and response body
- [ ] Content-Type and Content-Length
- [ ] Host header
- [ ] Authorization header
- [ ] Cookie and Set-Cookie headers
- [ ] Origin and Referer headers
- [ ] Accept and User-Agent headers
- [ ] Redirects
- [ ] Keep-alive and connection reuse
- [ ] Compression
- [ ] Chunked transfer encoding
- [ ] Caching headers
- [ ] ETags and conditional requests
- [ ] Content negotiation
- [ ] Idempotent vs safe HTTP methods
- [ ] HTTP proxies
- [ ] Reverse proxies
- [ ] Load balancing
- [ ] CDN behavior

## 21. HTTPS and TLS

- [ ] Why HTTPS is needed
- [ ] HTTP vs HTTPS
- [ ] Encryption, integrity, and authentication
- [ ] Symmetric vs asymmetric cryptography
- [ ] Public-key infrastructure (PKI)
- [ ] Digital certificates
- [ ] Certificate authorities
- [ ] Certificate chains
- [ ] Certificate expiration
- [ ] Hostname verification
- [ ] TLS handshake — overview
- [ ] TLS versions and secure configurations
- [ ] Cipher suites — basic concepts
- [ ] Key exchange and forward secrecy
- [ ] SNI — Server Name Indication
- [ ] ALPN — Application-Layer Protocol Negotiation
- [ ] HSTS
- [ ] Mixed content
- [ ] Certificate errors and troubleshooting
- [ ] TLS termination at reverse proxies
- [ ] Why HTTPS does not automatically make an application secure

## 22. Cookies, Sessions, and Browser Networking

- [ ] Cookies vs server-side sessions
- [ ] Session IDs
- [ ] `Secure` cookie attribute
- [ ] `HttpOnly` cookie attribute
- [ ] `SameSite` cookie attribute
- [ ] Cookie scope and domain
- [ ] Browser origin
- [ ] Same-origin policy
- [ ] CORS
- [ ] Preflight requests
- [ ] CSRF fundamentals
- [ ] Browser cache
- [ ] Local storage vs session storage
- [ ] WebSockets and the upgrade handshake
- [ ] WebSockets security basics
- [ ] Browser developer tools: Network tab
- [ ] Request timing and waterfall diagrams
- [ ] Redirect chains
- [ ] Third-party requests and external resources

## 23. Web Architecture and API Networking

- [ ] Frontend vs backend
- [ ] Web server vs application server
- [ ] Reverse proxy architecture
- [ ] Application-to-database communication
- [ ] REST APIs
- [ ] JSON and XML payloads
- [ ] API authentication
- [ ] API keys and bearer tokens
- [ ] OAuth 2.0 and OpenID Connect — fundamentals
- [ ] JWT structure and validation — fundamentals
- [ ] GraphQL — basic networking and request structure
- [ ] Rate limiting
- [ ] API gateways
- [ ] Webhooks
- [ ] Service-to-service communication
- [ ] API versioning
- [ ] Timeouts and retries
- [ ] Connection pooling
- [ ] Common API security misconfigurations

# Phase 10: Proxies, VPNs, and Privacy

## 24. Proxy Servers

- [ ] Forward proxy
- [ ] Reverse proxy
- [ ] Transparent proxy
- [ ] HTTP proxy
- [ ] SOCKS4 vs SOCKS5
- [ ] Proxy authentication
- [ ] Proxy headers
- [ ] Proxy chaining — concept
- [ ] TLS interception — authorized lab use
- [ ] Burp Suite proxy configuration
- [ ] Reverse-proxy trust boundaries
- [ ] Risks from incorrectly trusting forwarded headers

## 25. VPNs

- [ ] What is a VPN?
- [ ] Remote-access vs site-to-site VPN
- [ ] VPN tunneling
- [ ] IPsec VPN
- [ ] WireGuard
- [ ] OpenVPN
- [ ] Split tunneling
- [ ] VPN routes and DNS
- [ ] VPN vs proxy
- [ ] VPN limitations
- [ ] Common VPN configuration errors

# Phase 11: Wireless Networking

## 26. Wi-Fi Fundamentals

- [ ] Wireless networking basics
- [ ] IEEE 802.11 standards — overview
- [ ] 2.4 GHz, 5 GHz, and 6 GHz bands
- [ ] Channels and interference
- [ ] SSID and BSSID
- [ ] Access points and clients
- [ ] WPA2-Personal
- [ ] WPA3-Personal
- [ ] Enterprise Wi-Fi and 802.1X
- [ ] Authentication vs encryption
- [ ] Guest network isolation
- [ ] Rogue access points
- [ ] Evil twin attacks — concepts and defenses
- [ ] Wireless monitoring fundamentals
- [ ] Wireless network hardening
- [ ] Why Wi-Fi security is a separate specialization

Wireless security can be a later topic; it is not a prerequisite for web application security.

# Phase 12: Network Security Concepts

## 27. Threats and Defenses

- [ ] Threat, vulnerability, exploit, and risk
- [ ] Attack surface
- [ ] Threat modeling basics
- [ ] Spoofing
- [ ] Sniffing
- [ ] Man-in-the-middle attacks
- [ ] Replay attacks
- [ ] DNS spoofing — concept
- [ ] ARP spoofing — concept
- [ ] DoS vs DDoS
- [ ] SYN flood — concept and defenses
- [ ] Amplification attacks — concept and defenses
- [ ] Session hijacking — concept and defenses
- [ ] IP spoofing and its limitations
- [ ] Port scanning
- [ ] Service enumeration
- [ ] Network segmentation
- [ ] Rate limiting
- [ ] IDS vs IPS
- [ ] Network detection and response
- [ ] Secure configuration and patching
- [ ] Incident response fundamentals

## 28. IDS, IPS, and Network Monitoring

- [ ] Intrusion Detection System (IDS)
- [ ] Intrusion Prevention System (IPS)
- [ ] Signature-based detection
- [ ] Anomaly-based detection
- [ ] False positives and false negatives
- [ ] Network traffic baselines
- [ ] Centralized logging
- [ ] Alert triage
- [ ] Network flow records
- [ ] PCAP files
- [ ] Basic detection rules
- [ ] Zeek — overview
- [ ] Suricata — overview
- [ ] Snort — overview
- [ ] SIEM fundamentals
- [ ] Network incident investigation

# Phase 13: Network Tools on Linux and Kali

## 29. Essential Command-Line Tools

- [ ] `ip` — addresses, interfaces, and routes
- [ ] `ping` — connectivity tests
- [ ] `ss` — sockets and listening ports
- [ ] `curl` — HTTP and API requests
- [ ] `wget` — file retrieval
- [ ] `dig` — DNS queries
- [ ] `host` — DNS lookups
- [ ] `traceroute` or `tracepath` — route diagnostics
- [ ] `mtr` — combined route and loss diagnostics
- [ ] `nc` — basic socket testing
- [ ] `tcpdump` — packet capture
- [ ] `nmap` — authorized network discovery
- [ ] `whois` — domain/IP registration information, where available
- [ ] `openssl s_client` — TLS inspection
- [ ] `jq` — JSON processing
- [ ] `ethtool` — interface information, where available
- [ ] `nmcli` — NetworkManager management
- [ ] `resolvectl` — resolver diagnostics, where available

## 30. Wireshark

- [ ] What is packet analysis?
- [ ] Installing and opening Wireshark
- [ ] Selecting the correct capture interface
- [ ] Live captures vs saved PCAP files
- [ ] Packet list, details, and bytes panes
- [ ] Capture filters vs display filters
- [ ] Ethernet frame analysis
- [ ] ARP analysis
- [ ] DNS analysis
- [ ] TCP handshake analysis
- [ ] Retransmissions and resets
- [ ] HTTP request analysis
- [ ] TLS handshake analysis
- [ ] Follow TCP stream
- [ ] Exporting objects where appropriate
- [ ] Saving evidence and documenting findings
- [ ] Privacy considerations when capturing traffic

## 31. Nmap

- [ ] What Nmap does and does not do
- [ ] Host discovery
- [ ] TCP connect scans
- [ ] SYN scan concepts
- [ ] UDP scan concepts
- [ ] Port ranges
- [ ] Service/version detection
- [ ] OS detection limitations
- [ ] DNS resolution behavior
- [ ] Output formats
- [ ] Scan timing and network impact
- [ ] Understanding filtered, open, and closed ports
- [ ] Interpreting results
- [ ] Confirming findings manually
- [ ] Running scans only within authorized scope

# Phase 14: Cloud, Containers, and Modern Networking

## 32. Cloud Networking Fundamentals

- [ ] What is cloud networking?
- [ ] Virtual private cloud (VPC/VNet)
- [ ] Public and private subnets
- [ ] Internet gateways
- [ ] NAT gateways
- [ ] Route tables
- [ ] Security groups
- [ ] Network ACLs
- [ ] Cloud load balancers
- [ ] Private endpoints
- [ ] DNS in cloud environments
- [ ] Cloud network logging
- [ ] Cloud firewall concepts
- [ ] Publicly exposed services
- [ ] Least-privilege network access

## 33. Container Networking

- [ ] What are containers?
- [ ] Docker bridge networks
- [ ] Host networking
- [ ] Port publishing
- [ ] Container-to-container communication
- [ ] DNS within container networks
- [ ] Docker Compose networking
- [ ] Container isolation
- [ ] Network exposure and misconfiguration
- [ ] Kubernetes networking — introduction
- [ ] Services and ingress — overview
- [ ] Network policies — overview

These are useful later for AppSec, DevSecOps, and cloud security.

# Phase 15: Advanced Topics — Learn Later

- [ ] Advanced IPv4 subnetting and route aggregation
- [ ] Advanced IPv6 routing and security
- [ ] Dynamic routing protocols: BGP and OSPF
- [ ] MPLS — overview
- [ ] Software-defined networking (SDN)
- [ ] Network function virtualization
- [ ] Quality of Service (QoS)
- [ ] Multicast routing
- [ ] Advanced firewall design
- [ ] High availability and failover
- [ ] Load-balancing algorithms
- [ ] Anycast routing
- [ ] QUIC and HTTP/3 internals
- [ ] Advanced TLS troubleshooting
- [ ] Network forensics
- [ ] Cloud-native network security
- [ ] Zero Trust architecture
- [ ] Network automation with Python
- [ ] Infrastructure as Code — networking fundamentals

---

# Phase 16: Practical Projects

Complete these projects to connect theory with real skills.

## Project 1 — Network Inventory

- [ ] Record the interfaces and IP addresses of your lab VMs.
- [ ] Identify their gateways and DNS resolvers.
- [ ] Document the network topology.
- [ ] Create a simple network diagram.

## Project 2 — Network Troubleshooting

- [ ] Diagnose a failed DNS lookup in a lab.
- [ ] Identify a service that is not listening on its expected port.
- [ ] Trace a route to a permitted destination.
- [ ] Document the cause and resolution of each problem.

## Project 3 — Packet Analysis

- [ ] Capture traffic generated by your own browser.
- [ ] Identify DNS resolution.
- [ ] Identify a TCP handshake.
- [ ] Inspect an HTTP request to a local test service.
- [ ] Observe which details remain visible in encrypted HTTPS traffic.
- [ ] Write a short packet-analysis report.

## Project 4 — HTTP and TLS Inspector

- [ ] Use `curl` to inspect a lab website.
- [ ] Record its status code and selected response headers.
- [ ] Inspect its TLS certificate using appropriate tools.
- [ ] Identify certificate validity and hostname information.
- [ ] Write a Python script that produces a simple report.

## Project 5 — Authorized Lab Network Assessment

- [ ] Define the scope of your own lab.
- [ ] Discover lab hosts.
- [ ] Identify open ports.
- [ ] Determine the services running on those ports.
- [ ] Verify selected findings manually.
- [ ] Document risks and remediation recommendations.

## Project 6 — Secure Web Architecture

- [ ] Deploy a test frontend and backend.
- [ ] Keep the database inaccessible from the public network.
- [ ] Configure appropriate firewall rules.
- [ ] Use HTTPS in a suitable test environment.
- [ ] Document trusted boundaries and allowed traffic.
- [ ] Test that unnecessary ports are not exposed.

---

# Recommended 8-Week Schedule

| Week | Topics | Practical target |
|---|---|---|
| 1 | Fundamentals, OSI/TCP-IP, IPv4 | Explain basic network communication |
| 2 | Subnetting, IPv6, MAC, Ethernet, ARP | Inspect addresses and neighbor tables |
| 3 | TCP, UDP, ports, routing | Diagnose ports and routing problems |
| 4 | DNS, DHCP, ICMP, NAT, firewalls | Troubleshoot basic connectivity |
| 5 | HTTP, HTTPS, TLS, cookies, APIs | Understand browser-to-server traffic |
| 6 | Proxies, Wireshark, tcpdump | Capture and analyze lab traffic |
| 7 | Nmap, network security, IDS/IPS basics | Perform an authorized lab assessment |
| 8 | Python automation, projects, revision | Finish a network-analysis project |

You can extend this schedule if subnetting, TCP, or HTTP takes longer to understand. Practical understanding matters more than finishing on a fixed date.

---

# Priority Checklist for Your Cybersecurity Goal

## Must learn first

- [ ] OSI and TCP/IP models
- [ ] IPv4 and subnetting fundamentals
- [ ] MAC addresses, Ethernet, and ARP
- [ ] TCP vs UDP
- [ ] Ports and sockets
- [ ] DNS
- [ ] Routing and default gateways
- [ ] HTTP and HTTPS
- [ ] TLS and certificates
- [ ] NAT and firewall basics
- [ ] Linux networking commands
- [ ] Wireshark fundamentals
- [ ] Burp Suite's use of HTTP proxies
- [ ] Basic Nmap usage within authorized scope

## Learn alongside web application security

- [ ] Cookies and sessions
- [ ] Same-origin policy and CORS
- [ ] Reverse proxies and load balancers
- [ ] REST APIs and authentication
- [ ] DNS and TLS troubleshooting
- [ ] HTTP headers and caching
- [ ] Packet analysis
- [ ] Network segmentation
- [ ] Python HTTP automation

## Learn later

- [ ] Advanced routing protocols
- [ ] Wireless penetration testing
- [ ] Enterprise network architecture
- [ ] Advanced network forensics
- [ ] Cloud and Kubernetes networking
- [ ] Advanced IDS/IPS engineering

---

# Final Readiness Test

Before moving deeper into web application security, you should be able to:

- [ ] Explain how a browser resolves a domain and reaches a server.
- [ ] Explain what happens during a TCP three-way handshake.
- [ ] Calculate basic IPv4 subnets.
- [ ] Distinguish a DNS problem from a routing, firewall, or application problem.
- [ ] Identify listening ports on your own Linux machine.
- [ ] Use `curl` to inspect HTTP responses.
- [ ] Explain the purpose of TLS certificates and HTTPS.
- [ ] Use Wireshark to identify DNS, TCP, and HTTP traffic in a lab.
- [ ] Configure Burp Suite to inspect requests to a training application.
- [ ] Use Nmap responsibly on systems you own or are authorized to test.
- [ ] Write a short, evidence-based network assessment report.

**Recommended learning order:** Linux networking commands → IP addressing and TCP/IP → DNS and routing → HTTP/HTTPS and TLS → Wireshark → Burp Suite → authorized Nmap practice.

You do not need to master all advanced networking before studying web security. Once you understand IP addresses, ports, DNS, TCP, HTTP, HTTPS, and basic packet analysis, begin hands-on web security labs and deepen networking as needed.
