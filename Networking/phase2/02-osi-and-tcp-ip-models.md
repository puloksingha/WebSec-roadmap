
# Phase 2: OSI and TCP/IP Models

# 2. OSI Model

## Table of Contents

1. What is the OSI Model?
2. Why Networking Models Are Useful
3. Overview of the Seven OSI Layers
4. Layer 1 — Physical
5. Layer 2 — Data Link
6. Layer 3 — Network
7. Layer 4 — Transport
8. Layer 5 — Session
9. Layer 6 — Presentation
10. Layer 7 — Application
11. Responsibilities of Each Layer
12. Protocols and Devices Associated with Each Layer
13. Encapsulation and Decapsulation
14. How Data Travels Through the Layers
15. Troubleshooting Using the OSI Model
16. OSI Model and Cybersecurity

# 3. TCP/IP Model

17. What is the TCP/IP Model?
18. Network Access Layer
19. Internet Layer
20. Transport Layer
21. Application Layer
22. OSI vs TCP/IP Model
23. Mapping Protocols to Layers
24. Encapsulation in TCP/IP
25. How a Browser Request Travels Through the Stack
26. How a Server Response Returns to the Client
27. Practical Lab — HTTPS Request Journey
28. Practical Commands and Packet Analysis
29. Common Interview Questions
30. Key Takeaways

---

# Part 1: OSI Model

# 1. What is the OSI Model?

The **Open Systems Interconnection (OSI) model** is a conceptual framework that describes how data is communicated between devices over a network.

It divides the communication process into seven layers.

Each layer has a specific responsibility and interacts with the layers directly above and below it.

The OSI model was developed by the International Organization for Standardization (ISO) to provide a common framework for understanding and designing network communication.

The seven layers are:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

The OSI model is primarily a reference model. Real-world networking protocols do not always map perfectly to its layers.

## 1.1 Seven OSI Layers

```text
+--------------------------------+
| Layer 7: Application            |
+--------------------------------+
| Layer 6: Presentation           |
+--------------------------------+
| Layer 5: Session                |
+--------------------------------+
| Layer 4: Transport              |
+--------------------------------+
| Layer 3: Network                |
+--------------------------------+
| Layer 2: Data Link              |
+--------------------------------+
| Layer 1: Physical               |
+--------------------------------+
```

## 1.2 Mnemonic to Remember the Layers

From Layer 7 to Layer 1:

**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.

| Layer | Name |
|---|---|
| 7 | Application |
| 6 | Presentation |
| 5 | Session |
| 4 | Transport |
| 3 | Network |
| 2 | Data Link |
| 1 | Physical |

Another mnemonic from Layer 1 to Layer 7:

**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way.

---

# 2. Why Networking Models Are Useful

Networking models help us understand the complex process of network communication.

Without a layered model, it would be difficult to explain how an application communicates with another application across different networks.

## 2.1 Standardization

Networking models provide a common way to describe network communication.

Different manufacturers can develop devices and software that communicate using compatible protocols.

## 2.2 Modularity

Each layer performs a specific function.

A change in one layer does not necessarily require changes in every other layer.

For example, an application can use Wi-Fi or Ethernet without needing to change its HTTP implementation.

## 2.3 Troubleshooting

The OSI model helps identify where a network problem may occur.

For example:

- A damaged cable is a Physical Layer problem.
- A MAC address forwarding issue is a Data Link Layer problem.
- An incorrect IP address is a Network Layer problem.
- A TCP connection failure is a Transport Layer problem.
- An HTTP error is generally an Application Layer issue.

## 2.4 Interoperability

Layered models help different operating systems, hardware, and applications communicate.

## 2.5 Security Analysis

Cybersecurity professionals use the OSI model to understand where security controls and vulnerabilities exist.

Examples:

- Layer 2: ARP spoofing.
- Layer 3: IP filtering and routing security.
- Layer 4: TCP port filtering.
- Layer 7: HTTP request validation and web application security.

---

# 3. Overview of the Seven OSI Layers

| Layer | Name | Main Responsibility | Data Unit |
|---|---|---|---|
| 7 | Application | Provides network services to applications | Data |
| 6 | Presentation | Data representation, encoding, encryption, compression | Data |
| 5 | Session | Manages communication sessions | Data |
| 4 | Transport | End-to-end transport between processes | Segment / Datagram |
| 3 | Network | Logical addressing and routing | Packet |
| 2 | Data Link | Local delivery using frames and MAC addresses | Frame |
| 1 | Physical | Transmits bits or symbols over a medium | Bits / Symbols |

**Important:** The data unit names are common conventions. Exact terminology varies across protocols and implementations.

---

# 4. Layer 1 — Physical Layer

## 4.1 Definition

The Physical Layer is the lowest layer of the OSI model.

It is responsible for transmitting raw bits or symbols over a physical communication medium.

It defines the electrical, optical, radio, and mechanical characteristics of network communication.

## 4.2 Responsibilities

The Physical Layer handles:

- Transmission of bits.
- Electrical signaling.
- Optical signaling.
- Radio signaling.
- Cable specifications.
- Connector specifications.
- Data transmission rates.
- Signal timing.
- Physical transmission media.
- Physical network interfaces.

## 4.3 Examples of Physical Media

### Wired Media

- Twisted-pair Ethernet cables.
- Coaxial cables.
- Fiber-optic cables.

### Wireless Media

- Wi-Fi radio waves.
- Bluetooth radio waves.
- Cellular radio communication.

## 4.4 Devices Associated with Layer 1

| Device | Purpose |
|---|---|
| Repeater | Regenerates or retransmits signals. |
| Hub | Repeats signals to connected ports. |
| Media converter | Converts one physical medium to another. |
| Transceiver | Transmits and receives signals. |
| Cables | Carry physical signals. |

A NIC contains Physical Layer functions, but it also commonly performs Data Link Layer functions.

## 4.5 Common Technologies

Examples include:

- Ethernet physical-layer specifications.
- Fiber-optic transmission standards.
- Wi-Fi radio transmission.
- Bluetooth radio transmission.

IEEE 802.3 and IEEE 802.11 include specifications related to both Physical and Data Link Layer functions.

## 4.6 Example

Suppose you send a file through an Ethernet connection.

At the Physical Layer:

1. The data has already been prepared by higher layers.
2. The Ethernet interface converts the data into physical signals.
3. The signals travel through the cable.
4. The receiving interface detects and interprets the signals.

```text
Computer A                         Computer B
    |                                  |
 Ethernet NIC ===== Ethernet Cable ==== NIC
    |                                  |
  Signals --------------------------> Signals
```

## 4.7 Common Layer 1 Problems

- Damaged cable.
- Disconnected cable.
- Faulty network adapter.
- Incorrect transceiver.
- Poor wireless signal.
- Electrical interference.
- Hardware failure.

## 4.8 Practical Commands

### Windows

```powershell
Get-NetAdapter
```

### Linux

```bash
ip link
```

To inspect Ethernet link information:

```bash
sudo ethtool eth0
```

Replace `eth0` with your actual interface name.

---

# 5. Layer 2 — Data Link Layer

## 5.1 Definition

The Data Link Layer is responsible for communication between devices on the same local link.

It organizes data into frames and uses link-layer addressing to deliver frames across a local network.

For Ethernet, the most familiar link-layer address is the MAC address.

## 5.2 Responsibilities

- Framing.
- MAC addressing.
- Local frame delivery.
- Media access control.
- Error detection.
- Link-layer communication.
- VLAN tagging in supported technologies.

The Data Link Layer does not generally provide end-to-end delivery across the entire Internet.

## 5.3 MAC Address

A MAC address is a link-layer identifier commonly used by network interfaces.

Example:

```text
00:1A:2B:3C:4D:5E
```

A typical Ethernet MAC address is 48 bits long.

MAC addresses are used for communication within a local Layer 2 network.

## 5.4 Ethernet Frame

A simplified Ethernet frame:

```text
+---------------------+
| Destination MAC     |
+---------------------+
| Source MAC          |
+---------------------+
| Type / Length       |
+---------------------+
| Payload             |
+---------------------+
| Frame Check Sequence|
+---------------------+
```

The Frame Check Sequence (FCS) is used for error detection.

A standard Ethernet frame's FCS is 4 bytes long.

The frame format may contain additional fields, such as VLAN tags.

## 5.5 Devices Associated with Layer 2

| Device | Purpose |
|---|---|
| Ethernet switch | Forwards frames using MAC addresses. |
| Bridge | Connects Layer 2 network segments. |
| Network interface | Implements link-layer functions. |
| Wireless access point | Bridges wireless clients into a LAN. |

A Layer 2 switch uses a MAC address table to determine where frames should be forwarded.

## 5.6 Common Protocols and Technologies

- Ethernet.
- Wi-Fi MAC.
- ARP for IPv4 local address resolution.
- VLAN tagging using IEEE 802.1Q.
- Spanning Tree Protocol (STP).

ARP is commonly associated with the boundary between Layer 2 and Layer 3 because it resolves IPv4 addresses into link-layer addresses.

## 5.7 Example

Suppose Computer A wants to communicate with Computer B on the same LAN.

```text
Computer A ---- Switch ---- Computer B
```

The switch examines the destination MAC address and forwards the Ethernet frame to the appropriate port.

## 5.8 Common Layer 2 Problems

- Incorrect VLAN configuration.
- MAC address table issues.
- Switching loops.
- Incorrect access port configuration.
- ARP resolution problems.
- Faulty Ethernet link.

## 5.9 Practical Commands

### Windows

```powershell
ipconfig /all
```

### Linux

```bash
ip link
```

View the ARP or neighbor table:

```bash
ip neigh
```

---

# 6. Layer 3 — Network Layer

## 6.1 Definition

The Network Layer is responsible for logical addressing and forwarding packets between different networks.

The most important Layer 3 protocol is the Internet Protocol (IP).

## 6.2 Responsibilities

- Logical addressing.
- Packet forwarding.
- Routing.
- Inter-network communication.
- Path selection.
- Packet fragmentation in IPv4, where applicable.
- TTL or Hop Limit processing.

## 6.3 IP Address

An IP address is a logical address assigned to a network interface.

IPv4 addresses are 32 bits long.

Example:

```text
192.168.1.10
```

IPv6 addresses are 128 bits long.

Example:

```text
2001:db8::10
```

IP addresses are used to identify endpoints within IP networks and support packet forwarding.

## 6.4 Routing

Routing is the process of determining paths through a network.

Routers use routing tables to determine where packets should be forwarded.

Example:

```text
Computer A
192.168.1.10
     |
     v
  Router A
     |
     v
  Router B
     |
     v
Computer B
203.0.113.10
```

The packet may pass through several routers before reaching its destination.

## 6.5 Devices Associated with Layer 3

- Routers.
- Layer 3 switches.
- IP-enabled firewalls.
- Network interfaces implementing IP.

## 6.6 Common Protocols

| Protocol | Purpose |
|---|---|
| IPv4 | Logical addressing and packet forwarding. |
| IPv6 | Logical addressing and packet forwarding. |
| ICMP | Network control and diagnostic messages. |
| OSPF | Interior gateway routing protocol. |
| BGP | Routing between autonomous systems. |

## 6.7 TTL and Hop Limit

IPv4 uses Time to Live (TTL).

IPv6 uses Hop Limit.

These fields are reduced by routers as packets are forwarded.

If the value reaches zero, the packet is discarded.

This helps prevent packets from circulating indefinitely.

## 6.8 Common Layer 3 Problems

- Incorrect IP address.
- Incorrect subnet mask.
- Incorrect default gateway.
- Routing errors.
- IP address conflicts.
- Packet filtering.
- Incorrect network configuration.

## 6.9 Practical Commands

```bash
ip addr
```

```bash
ip route
```

```bash
ping 8.8.8.8
```

```bash
traceroute 8.8.8.8
```

On Windows:

```powershell
tracert 8.8.8.8
```

---

# 7. Layer 4 — Transport Layer

## 7.1 Definition

The Transport Layer provides communication between processes running on different hosts.

It uses port numbers to identify application processes or services.

The two most important transport protocols are:

- TCP.
- UDP.

## 7.2 Responsibilities

- Process-to-process communication.
- Port addressing.
- Segmentation.
- Reassembly.
- Multiplexing.
- Connection management.
- Reliability, when provided by the protocol.
- Flow control, when provided by the protocol.

## 7.3 Port Numbers

A port number identifies a transport-layer endpoint.

TCP and UDP use 16-bit port numbers.

The range is:

```text
0 - 65535
```

Common ports:

| Port | Protocol | Service |
|---|---|---|
| 20/21 | TCP | FTP data/control in traditional FTP |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS over TCP |
| 443 | UDP | Commonly used by QUIC/HTTP/3 |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |

Ports 0–1023 are commonly known as well-known ports.

## 7.4 TCP

TCP stands for Transmission Control Protocol.

TCP provides:

- Connection-oriented communication.
- Reliable delivery.
- Ordered byte-stream delivery.
- Retransmission of lost data.
- Flow control.
- Congestion control.

TCP establishes a connection using a three-way handshake.

```text
Client                         Server
  |                               |
  | -------- SYN ---------------> |
  |                               |
  | <------- SYN-ACK ------------ |
  |                               |
  | -------- ACK ---------------> |
  |                               |
  |        Connection            |
```

## 7.5 UDP

UDP stands for User Datagram Protocol.

UDP provides:

- Connectionless communication.
- Datagram delivery.
- Low protocol overhead.
- No built-in TCP-style retransmission.
- No built-in guarantee of ordered delivery.

UDP is commonly used by:

- DNS.
- Voice communication.
- Video communication.
- Online games.
- QUIC.

Applications may implement their own reliability or congestion control over UDP.

## 7.6 Common Layer 4 Problems

- Blocked ports.
- TCP handshake failure.
- Connection timeout.
- Connection reset.
- Application not listening on the expected port.
- Transport-layer filtering.

## 7.7 Practical Commands

### Linux

```bash
ss -tuln
```

This displays listening TCP and UDP sockets.

To inspect established TCP connections:

```bash
ss -tn
```

### Windows

```powershell
netstat -ano
```

---

# 8. Layer 5 — Session Layer

## 8.1 Definition

The Session Layer manages communication sessions between applications.

It provides conceptual mechanisms for establishing, maintaining, coordinating, and terminating sessions.

## 8.2 Responsibilities

- Session establishment.
- Session maintenance.
- Session termination.
- Dialog control.
- Synchronization.
- Checkpointing in some systems.

## 8.3 Example

Suppose two applications are communicating.

A session may involve:

1. Establishing communication.
2. Maintaining the communication state.
3. Synchronizing information.
4. Ending the session.

A long-running remote communication process may need to preserve session state.

## 8.4 Common Examples

Session-related functions can appear in:

- Remote procedure calls.
- Application session management.
- Some multimedia communication systems.
- Authentication and session management systems.

Many modern protocols implement session-related functionality at the application layer rather than as a separate OSI Layer 5 protocol.

## 8.5 Cybersecurity Relevance

Session management is especially important in web security.

Examples:

- Session cookies.
- Session identifiers.
- Session expiration.
- Session fixation.
- Session hijacking.
- Authentication state.

A web application may use an HTTP cookie to associate requests with a user's authenticated session.

However, HTTP itself is generally classified as an Application Layer protocol, not a dedicated Session Layer protocol.

---

# 9. Layer 6 — Presentation Layer

## 9.1 Definition

The Presentation Layer is responsible for the representation and interpretation of data exchanged between applications.

It helps ensure that the data produced by one system can be understood by another.

## 9.2 Responsibilities

- Data representation.
- Character encoding.
- Data format conversion.
- Data serialization.
- Data compression.
- Data encryption and decryption in the conceptual OSI model.

## 9.3 Examples

### Character Encoding

Text may be represented using:

- ASCII.
- UTF-8.
- UTF-16.

For example, a character must be represented consistently so that the receiving application can interpret it correctly.

### Serialization

Serialization converts structured data into a format suitable for transmission or storage.

Examples:

- JSON.
- XML.
- Protocol Buffers.

### Compression

Compression reduces the amount of data transmitted.

Examples:

- gzip.
- Brotli.

### Encryption

Encryption transforms readable data into ciphertext using cryptographic algorithms and keys.

Examples:

- TLS-protected communication.
- Encrypted application data.

In real-world TCP/IP networks, these functions are commonly implemented by application libraries and protocols rather than a separate Layer 6 protocol.

## 9.4 Cybersecurity Relevance

Presentation-related concepts are important for understanding:

- TLS encryption.
- Encoding issues.
- Serialization vulnerabilities.
- Compression-related risks.
- Data format validation.

Encoding is not encryption.

For example:

```text
Base64 is encoding, not encryption.
```

Base64 does not provide confidentiality.

---

# 10. Layer 7 — Application Layer

## 10.1 Definition

The Application Layer provides network services to user-facing applications and software processes.

It is the highest layer of the OSI model.

It defines how applications communicate over a network.

## 10.2 Responsibilities

- Application-level communication.
- Request and response formatting.
- Network service access.
- Application-specific commands.
- Resource identification.
- Application protocol behavior.

## 10.3 Common Protocols

| Protocol | Purpose |
|---|---|
| HTTP | Transfers web resources. |
| HTTPS | HTTP protected using TLS. |
| DNS | Resolves domain names. |
| SMTP | Transfers email. |
| IMAP | Retrieves and manages email. |
| POP3 | Retrieves email. |
| FTP | Transfers files. |
| SSH | Secure remote access. |
| DHCP | Provides network configuration. |

## 10.4 Example: HTTP Request

A browser sends a request:

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

The web server may return:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 125

<html>
<body>
<h1>Hello</h1>
</body>
</html>
```

HTTP defines the request and response structure.

## 10.5 Common Layer 7 Problems

- HTTP 404 errors.
- HTTP 500 errors.
- Incorrect request headers.
- Invalid application data.
- Authentication failures.
- Application configuration problems.
- DNS resolution issues.

DNS is an Application Layer protocol even though it is essential for establishing many network connections.

---

# 11. Responsibilities of Each Layer

| Layer | Main Responsibility | Addressing / Identifier |
|---|---|---|
| Application | Application services | URLs, domain names, application identifiers |
| Presentation | Data representation | Data formats and encodings |
| Session | Session management | Session identifiers |
| Transport | Process communication | TCP/UDP port numbers |
| Network | Inter-network delivery | IP addresses |
| Data Link | Local link delivery | MAC addresses |
| Physical | Signal transmission | Physical signals |

### Important Understanding

Each layer answers a different question.

| Layer | Question |
|---|---|
| Application | What service or resource does the application need? |
| Presentation | How should the data be represented? |
| Session | How is the communication session managed? |
| Transport | Which application process should receive the data? |
| Network | Which IP destination should receive the packet? |
| Data Link | Which local interface should receive the frame? |
| Physical | How are the bits or symbols transmitted? |

---

# 12. Protocols and Devices Associated with Each Layer

| OSI Layer | Protocols / Technologies | Devices / Components |
|---|---|---|
| 7 — Application | HTTP, DNS, SMTP, SSH | Application servers, proxies |
| 6 — Presentation | Encoding, serialization, TLS-related functions | Application libraries, cryptographic libraries |
| 5 — Session | Session management, RPC-related mechanisms | Application software |
| 4 — Transport | TCP, UDP | Host transport stack, stateful firewalls |
| 3 — Network | IPv4, IPv6, ICMP, OSPF, BGP | Routers, Layer 3 switches |
| 2 — Data Link | Ethernet, Wi-Fi MAC, VLAN, STP | Switches, bridges, NICs |
| 1 — Physical | Ethernet PHY, fiber, radio signaling | Cables, repeaters, transceivers |

### Important Note

Device-layer classifications are simplified.

Modern network devices often operate across multiple layers.

For example:

- A firewall may inspect Layer 3, Layer 4, and Layer 7 information.
- A router has both Physical and Data Link interfaces but performs routing at Layer 3.
- A NIC commonly implements both Physical and Data Link functions.

---

# 13. Encapsulation and Decapsulation

## 13.1 What is Encapsulation?

Encapsulation is the process of adding protocol information as data moves down the networking stack.

Each layer adds its own header, and some layers may add trailers.

The receiving device performs the reverse process.

## 13.2 Encapsulation Process

Suppose a browser sends an HTTP request.

```text
Application Layer
        |
        v
+----------------------+
| HTTP Request         |
+----------------------+
        |
        v
Transport Layer
+----------------------+
| TCP Header           |
| HTTP Request         |
+----------------------+
        |
        v
Network Layer
+----------------------+
| IP Header            |
| TCP Segment          |
+----------------------+
        |
        v
Data Link Layer
+----------------------+
| Ethernet Header      |
| IP Packet            |
| Ethernet Trailer     |
+----------------------+
        |
        v
Physical Layer
        |
        v
Bits / Physical Signals
```

Each layer adds information required for its function.

## 13.3 Decapsulation Process

At the receiving device:

1. Physical Layer receives signals.
2. Data Link Layer reconstructs and validates the frame.
3. Network Layer processes the IP packet.
4. Transport Layer processes the TCP segment or UDP datagram.
5. Application Layer receives the application data.

```text
Physical Signals
       |
       v
Ethernet Frame
       |
       v
IP Packet
       |
       v
TCP Segment
       |
       v
HTTP Data
       |
       v
Web Application
```

## 13.4 Why Encapsulation Is Important

Encapsulation allows:

- Different protocols to work together.
- Each layer to perform its own function.
- Data to be routed through different networks.
- Devices to process the information they need.
- Network troubleshooting to be organized by layer.

---

# 14. How Data Travels From One Layer to Another

Consider a user sending a message from a laptop to a web server.

## Sender

### Step 1: Application Layer

The browser generates an HTTP request.

### Step 2: Presentation and Session Concepts

Data may be encoded, compressed, or protected using TLS.

In the TCP/IP stack, these functions are generally implemented within application protocols and libraries.

### Step 3: Transport Layer

TCP adds:

- Source port.
- Destination port.
- Sequence information.
- Other TCP control information.

### Step 4: Network Layer

IP adds:

- Source IP address.
- Destination IP address.
- Other IP header information.

### Step 5: Data Link Layer

Ethernet or Wi-Fi adds local link-layer addressing and framing information.

### Step 6: Physical Layer

The interface transmits signals through the selected medium.

## Receiver

The receiving device processes the data in the reverse direction.

It removes or processes the relevant protocol headers and delivers the application data to the intended process.

---

# 15. Troubleshooting Using the OSI Model

The OSI model provides a systematic approach to network troubleshooting.

Instead of randomly changing configurations, investigate the layers in a structured way.

## 15.1 Layer 1 Troubleshooting — Physical

Questions:

- Is the cable connected?
- Is the Wi-Fi interface enabled?
- Is the network adapter functioning?
- Is the link light active?
- Is the signal strong enough?

Commands:

```powershell
Get-NetAdapter
```

```bash
ip link
```

## 15.2 Layer 2 Troubleshooting — Data Link

Questions:

- Is the device connected to the correct VLAN?
- Is the switch learning the correct MAC address?
- Is ARP resolution working?
- Is the link operating correctly?

Commands:

```bash
ip link
```

```bash
ip neigh
```

## 15.3 Layer 3 Troubleshooting — Network

Questions:

- Does the device have a valid IP address?
- Is the subnet mask correct?
- Is the default gateway correct?
- Is the destination reachable?
- Is routing configured correctly?

Commands:

```bash
ip addr
```

```bash
ip route
```

```bash
ping 8.8.8.8
```

## 15.4 Layer 4 Troubleshooting — Transport

Questions:

- Is the destination port open?
- Is a TCP connection being established?
- Is a firewall blocking the connection?
- Is the application listening?

Commands:

```bash
ss -tuln
```

```bash
nc -vz example.com 443
```

The `nc` command attempts a TCP connection to port 443.

## 15.5 Layer 7 Troubleshooting — Application

Questions:

- Is DNS resolving the correct hostname?
- Is the web server responding?
- Is the HTTP request correct?
- Is the application returning an error?
- Is authentication working?

Commands:

```bash
curl -I https://example.com
```

```bash
dig example.com
```

## 15.6 Troubleshooting Example

Problem:

A user cannot open a website.

A systematic approach:

1. Check the network adapter.
2. Check the IP address.
3. Check the default gateway.
4. Test IP connectivity.
5. Check DNS resolution.
6. Test the destination TCP port.
7. Inspect the HTTPS connection.
8. Examine the HTTP response.

### Troubleshooting Flow

```text
Website Not Loading
        |
        v
Check Network Interface
        |
        v
Check IP Configuration
        |
        v
Test Gateway Connectivity
        |
        v
Test DNS Resolution
        |
        v
Test TCP Connection
        |
        v
Inspect TLS / HTTPS
        |
        v
Inspect HTTP Response
```

This is a practical approach, not a strict rule that every issue must be investigated from Layer 1 upward.

---

# 16. OSI Model and Cybersecurity

Understanding the OSI model helps cybersecurity professionals identify where attacks occur and where defensive controls can be applied.

## 16.1 Layer 1 Security

Possible threats:

- Physical cable tampering.
- Unauthorized physical access.
- Hardware theft.
- Signal interference.

Security controls:

- Physical access restrictions.
- Equipment security.
- Cable protection.
- Secure equipment rooms.

## 16.2 Layer 2 Security

Possible threats:

- ARP spoofing.
- MAC address spoofing.
- VLAN misconfiguration.
- Switching loops.

Security controls:

- Port security.
- Dynamic ARP Inspection.
- DHCP snooping.
- VLAN segmentation.
- Spanning Tree protections.

## 16.3 Layer 3 Security

Possible threats:

- IP spoofing.
- Routing attacks.
- Network scanning.
- Unauthorized network access.

Security controls:

- Network firewalls.
- Routing authentication where supported.
- Network segmentation.
- Access Control Lists (ACLs).
- Anti-spoofing filters.

## 16.4 Layer 4 Security

Possible threats:

- SYN flooding.
- Port scanning.
- TCP connection abuse.
- Unauthorized exposed services.

Security controls:

- Stateful firewalls.
- Rate limiting.
- SYN flood protection.
- Restricting unnecessary ports.

## 16.5 Layer 7 Security

Possible threats:

- SQL injection.
- Cross-Site Scripting (XSS).
- Authentication flaws.
- Broken access control.
- Server-Side Request Forgery (SSRF).
- Insecure file uploads.

Security controls:

- Input validation.
- Output encoding.
- Secure authentication.
- Authorization checks.
- Secure application configuration.
- Web Application Firewalls (WAFs).

### Important Cybersecurity Concept

A vulnerability may involve several layers simultaneously.

For example, an attacker exploiting a web application may use:

- DNS to locate the service.
- IP to reach the server.
- TCP to establish a connection.
- TLS to protect communication.
- HTTP to send a malicious request.
- Application logic to trigger the vulnerability.

---

# Part 2: TCP/IP Model

# 17. What is the TCP/IP Model?

The TCP/IP model is a networking framework describing the protocols and communication processes used by the Internet.

TCP/IP stands for:

**Transmission Control Protocol / Internet Protocol**

The model is commonly represented using four layers:

1. Application.
2. Transport.
3. Internet.
4. Network Access.

Unlike the OSI model, TCP/IP is closely associated with the actual protocols used for Internet communication.

## 17.1 TCP/IP Model Diagram

```text
+--------------------------------+
| Application                    |
+--------------------------------+
| Transport                      |
+--------------------------------+
| Internet                       |
+--------------------------------+
| Network Access                 |
+--------------------------------+
```

Some textbooks use a five-layer model by separating the Physical Layer from the Data Link Layer.

The four-layer model is commonly used when describing the TCP/IP protocol suite.

---

# 18. Network Access Layer

## 18.1 Definition

The Network Access Layer handles communication over the local network link.

It combines the responsibilities commonly associated with the OSI Data Link and Physical Layers.

## 18.2 Responsibilities

- Local network delivery.
- Framing.
- MAC addressing.
- Media access.
- Physical transmission.
- Signal transmission.

## 18.3 Technologies

- Ethernet.
- Wi-Fi.
- Fiber-optic Ethernet.
- Other link-layer technologies.

## 18.4 Data Unit

Common data units:

- Frame.
- Bits or symbols.

## 18.5 Example

Suppose your laptop sends a packet to a server on the Internet.

The Network Access Layer prepares the packet for transmission over your local Wi-Fi or Ethernet connection.

---

# 19. Internet Layer

## 19.1 Definition

The Internet Layer is responsible for logical addressing and forwarding packets between networks.

It corresponds closely to the OSI Network Layer.

## 19.2 Responsibilities

- IP addressing.
- Packet forwarding.
- Routing.
- Inter-network communication.
- TTL or Hop Limit processing.

## 19.3 Protocols

- IPv4.
- IPv6.
- ICMP.

## 19.4 Data Unit

The common data unit is the IP packet.

## 19.5 Example

A packet may travel through several routers before reaching the destination server.

Each router uses the destination IP address and its routing table to determine the next hop.

---

# 20. Transport Layer

## 20.1 Definition

The TCP/IP Transport Layer provides communication between application processes.

It corresponds closely to the OSI Transport Layer.

## 20.2 Responsibilities

- Process-to-process communication.
- Port addressing.
- Segmentation.
- Reassembly.
- Connection management.
- Reliability, where supported.

## 20.3 Protocols

### TCP

Provides reliable, ordered byte-stream communication.

### UDP

Provides connectionless datagram communication.

### QUIC

QUIC operates over UDP and provides transport features including reliable streams and connection establishment.

QUIC is used by HTTP/3.

Although QUIC has transport-layer functionality, it is not simply another TCP-like protocol directly carried by IP; it is implemented over UDP.

## 20.4 Data Units

- TCP segment.
- UDP datagram.
- QUIC packet, in QUIC-specific terminology.

---

# 21. Application Layer

## 21.1 Definition

The TCP/IP Application Layer combines the functionality associated with the OSI Application, Presentation, and Session Layers.

It provides services used by network applications.

## 21.2 Responsibilities

- Application communication.
- Data formatting.
- Application-level protocols.
- Session-related functionality.
- Data representation.
- Application-level encryption through protocols and libraries.

## 21.3 Protocols

- HTTP.
- HTTPS.
- DNS.
- SSH.
- SMTP.
- IMAP.
- FTP.
- DHCP.

TLS is commonly used by application protocols to provide encryption and authentication.

## 21.4 Example

When you access a website:

- DNS resolves the hostname.
- HTTP defines the web request.
- TLS protects the connection when HTTPS is used.
- The browser processes the response.

---

# 22. OSI vs TCP/IP Model

## 22.1 Comparison

| Feature | OSI Model | TCP/IP Model |
|---|---|---|
| Number of layers | 7 | Commonly 4 |
| Purpose | Reference model | Internet protocol architecture |
| Origin | ISO | Internet research and protocol development |
| Application layers | Application, Presentation, Session | Application |
| Transport | Transport | Transport |
| Network | Network | Internet |
| Link layers | Data Link, Physical | Network Access |

## 22.2 Layer Mapping

```text
OSI Model                         TCP/IP Model

+------------------+             +------------------+
| 7 Application    |             |                  |
+------------------+             |                  |
| 6 Presentation   |------------>| Application      |
+------------------+             |                  |
| 5 Session        |             |                  |
+------------------+             +------------------+
| 4 Transport      |------------>| Transport        |
+------------------+             +------------------+
| 3 Network        |------------>| Internet         |
+------------------+             +------------------+
| 2 Data Link      |             |                  |
+------------------+------------>| Network Access   |
| 1 Physical       |             |                  |
+------------------+             +------------------+
```

## 22.3 Important Differences

### OSI Model

- Provides seven conceptual layers.
- Separates Session and Presentation functions.
- Useful for teaching and troubleshooting.
- Does not require a specific protocol suite.

### TCP/IP Model

- Represents the architecture of Internet communication.
- Uses four commonly described layers.
- Combines several OSI functions.
- Closely matches the protocols used in real networks.

### Which Model Should You Use?

Use the OSI model to understand and troubleshoot network communication systematically.

Use the TCP/IP model to understand how real Internet protocols interact.

Both models are useful and complementary.

---

# 23. Mapping Protocols to Layers

| Protocol / Technology | OSI Layer | TCP/IP Layer |
|---|---|---|
| HTTP | Application | Application |
| HTTPS | Application, using TLS security | Application |
| DNS | Application | Application |
| SSH | Application | Application |
| SMTP | Application | Application |
| TLS | Commonly between application protocols and transport | Application-layer protocol support |
| TCP | Transport | Transport |
| UDP | Transport | Transport |
| QUIC | Transport functionality over UDP | Transport/application boundary, depending on model |
| IPv4 | Network | Internet |
| IPv6 | Network | Internet |
| ICMP | Network | Internet |
| Ethernet | Data Link / Physical | Network Access |
| Wi-Fi | Data Link / Physical | Network Access |
| ARP | Link/network boundary | Network Access / boundary function |

### Important Note About TLS

TLS does not map neatly to one dedicated OSI layer.

It is commonly treated as a security protocol used by application protocols over a transport connection.

For HTTPS over TCP, TLS operates above TCP and below HTTP.

---

# 24. Encapsulation in TCP/IP

Encapsulation is the process of adding protocol headers as data moves down the TCP/IP stack.

## 24.1 TCP/IP Encapsulation

```text
Application Data
       |
       v
+-----------------------+
| TCP Header            |
| Application Data      |
+-----------------------+
       |
       v
+-----------------------+
| IP Header             |
| TCP Segment           |
+-----------------------+
       |
       v
+-----------------------+
| Ethernet Header       |
| IP Packet             |
| Ethernet Trailer      |
+-----------------------+
       |
       v
Physical Transmission
```

## 24.2 Encapsulation Example

Suppose a browser sends an HTTP request to a web server.

The request may be encapsulated as:

```text
HTTP Request
    |
    v
TCP Segment
    |
    v
IP Packet
    |
    v
Ethernet Frame
    |
    v
Physical Signals
```

The receiving device decapsulates the data and delivers it to the correct application.

## 24.3 Encapsulation Terminology

| TCP/IP Layer | Data Unit |
|---|---|
| Application | Data |
| Transport | Segment / Datagram |
| Internet | Packet |
| Network Access | Frame |
| Physical transmission | Bits / Symbols |

---

# 25. How a Browser Request Travels Through the Stack

Consider the following scenario:

You enter:

```text
https://example.com
```

into your browser.

The browser needs to resolve the domain, establish a connection, send an HTTPS request, and receive a response.

The process involves several protocols.

## 25.1 Step 1 — URL Processing

The browser parses the URL.

```text
https://example.com/
```

Components:

| Component | Value |
|---|---|
| Scheme | https |
| Hostname | example.com |
| Port | 443, by default for HTTPS over TCP |
| Path | / |

The browser determines which protocol and destination it should use.

## 25.2 Step 2 — DNS Resolution

The browser needs the IP address associated with the hostname.

It may check:

1. Browser DNS cache.
2. Operating system DNS cache.
3. Configured DNS resolver.
4. Other DNS resolution mechanisms.

If the answer is not cached, the system may query a DNS resolver.

Example:

```text
Browser
   |
   v
DNS Resolver
   |
   v
DNS Response
   |
   v
IP Address
```

A simplified DNS query might look like:

```text
Question:
example.com

Answer:
A record -> IPv4 address
AAAA record -> IPv6 address
```

An A record contains an IPv4 address.

An AAAA record contains an IPv6 address.

The actual DNS response may contain different records, and the address can vary.

## 25.3 Step 3 — Routing Decision

The operating system determines how to reach the destination IP address.

It consults its routing table.

If the destination is outside the local network, the packet is generally sent to the default gateway.

Example:

```text
Laptop
192.168.1.10
     |
     v
Default Gateway
192.168.1.1
     |
     v
Internet
```

The default gateway forwards the packet toward the destination.

## 25.4 Step 4 — TCP Connection Establishment

For HTTPS over TCP, the browser establishes a TCP connection to the server.

The default destination port is 443.

TCP performs a three-way handshake:

```text
Client                         Server
  |                               |
  | -------- SYN ---------------> |
  |                               |
  | <------- SYN-ACK ------------ |
  |                               |
  | -------- ACK ---------------> |
  |                               |
  |       TCP Established         |
```

The client and server establish TCP connection state.

The TCP connection provides a reliable, ordered byte stream.

### Important

This TCP handshake applies to HTTPS over TCP, including HTTP/1.1 and HTTP/2.

HTTP/3 uses QUIC over UDP instead of TCP.

## 25.5 Step 5 — TLS Handshake

HTTPS uses TLS to protect HTTP communication.

For HTTPS over TCP, TLS negotiation occurs after TCP connection establishment.

A simplified TLS 1.3 handshake:

```text
Client                         Server
  |                               |
  | ------ ClientHello ---------> |
  |                               |
  | <----- ServerHello ---------- |
  | <----- Certificate* --------- |
  | <----- Finished ------------- |
  |                               |
  | ------ Finished ------------> |
  |                               |
  |       Secure Connection       |
```

`*` The certificate is commonly included in the handshake, but TLS 1.3 permits different handshake configurations.

TLS provides:

- Confidentiality.
- Integrity.
- Server authentication.
- Optional client authentication.

The browser validates the server certificate according to its trust and hostname validation rules.

TLS 1.3 can use session resumption and other mechanisms that change the handshake flow.

## 25.6 Step 6 — HTTP Request

Once the secure connection is established, the browser sends an HTTP request.

Example:

```http
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

The request is protected by TLS.

The HTTP message is not normally visible as plaintext to a passive network observer when TLS is working correctly.

## 25.7 Step 7 — Server Processing

The server receives the encrypted TLS records.

It:

1. Processes the incoming network traffic.
2. Reassembles TCP data.
3. Processes TLS records.
4. Decrypts and validates the protected data.
5. Passes the HTTP request to the server application.
6. Processes the requested resource.

The server may interact with:

- Application logic.
- Databases.
- Caches.
- Authentication systems.
- Other internal services.

## 25.8 Step 8 — HTTP Response

The server generates an HTTP response.

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 125

<html>
<body>
<h1>Hello</h1>
</body>
</html>
```

The response is encrypted by TLS and transmitted through TCP.

## 25.9 Step 9 — Browser Receives the Response

The browser:

1. Receives the TCP data.
2. Processes TLS records.
3. Decrypts the HTTP response.
4. Interprets the HTTP headers.
5. Processes the HTML.
6. Requests additional resources, if required.
7. Renders the webpage.

Additional resources may include:

- CSS.
- JavaScript.
- Images.
- Fonts.
- API responses.

These may require additional requests and connections.

---

# 26. How a Server Response Returns to the Client

The server response travels through the networking stack in the reverse direction.

## 26.1 Server-Side Process

```text
Web Application
       |
       v
HTTP Response
       |
       v
TLS Encryption
       |
       v
TCP Segments
       |
       v
IP Packets
       |
       v
Link-Layer Frames
       |
       v
Physical Transmission
```

## 26.2 Client-Side Process

```text
Physical Signals
       |
       v
Link-Layer Frames
       |
       v
IP Packets
       |
       v
TCP Data Stream
       |
       v
TLS Decryption
       |
       v
HTTP Response
       |
       v
Browser Rendering
```

## 26.3 Important Concepts

### Source and Destination Addresses

The server's response uses the appropriate source and destination IP addresses for the connection.

### Port Numbers

The server sends data from its service port to the client's transport endpoint.

For a typical HTTPS-over-TCP connection:

```text
Client Port:  Random Ephemeral Port
Server Port:  443
```

Example:

```text
Client: 192.168.1.10:51524
Server: 93.184.216.34:443
```

The example addresses and client port are illustrative.

### TCP Reliability

TCP provides ordered delivery of the byte stream.

If TCP detects missing data, it can retransmit data as needed.

### TLS Security

TLS protects the application data against unauthorized reading and modification while it is transmitted.

### HTTP Response Codes

Common HTTP response codes include:

| Code | Meaning |
|---|---|
| 200 | OK |
| 301 | Moved Permanently |
| 302 | Found |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

---

# 27. Practical Lab — HTTPS Request Journey

## Objective

Understand the journey of an HTTPS request from your browser to a web server.

You will observe:

- DNS resolution.
- TCP connection establishment.
- TLS negotiation.
- HTTP request and response.
- IP routing.
- Network traffic.

Use a website you are authorized to access.

## Lab Environment

You can use:

- Windows.
- Kali Linux.
- Wireshark.
- curl.
- dig or nslookup.
- ping.
- traceroute or tracert.

## Step 1 — Resolve the Domain

### Kali Linux

```bash
dig example.com
```

To query IPv4:

```bash
dig A example.com
```

To query IPv6:

```bash
dig AAAA example.com
```

### Windows

```powershell
nslookup example.com
```

Record the returned IP address.

Remember that DNS responses may vary because of:

- CDN infrastructure.
- Load balancing.
- Geographic routing.
- DNS caching.
- IPv4 and IPv6 availability.

## Step 2 — Check the Route

### Kali Linux

```bash
ip route
```

### Windows

```powershell
route print
```

Identify the default gateway.

## Step 3 — Inspect the TCP Connection

Run:

```bash
curl -v https://example.com
```

The verbose output may show:

- DNS resolution.
- Destination IP.
- TCP connection.
- TLS handshake information.
- HTTP request details.
- HTTP response headers.

Note that exact output varies by curl version and TLS backend.

## Step 4 — Inspect the TLS Certificate

Run:

```bash
curl -Iv https://example.com
```

Look for information about:

- TLS version.
- Certificate.
- Certificate validation.
- Connection establishment.

Do not disable certificate verification when using HTTPS in normal practice.

## Step 5 — Capture Traffic Using Wireshark

Open Wireshark.

Select the network interface that carries your traffic.

Start a capture.

Then run:

```bash
curl https://example.com
```

Stop the capture after the request completes.

### Display Filters

DNS:

```text
dns
```

TCP:

```text
tcp
```

TLS:

```text
tls
```

HTTPS over TCP:

```text
tcp.port == 443
```

DNS and HTTPS:

```text
dns || tcp.port == 443
```

### What You May Observe

- DNS query and response.
- TCP SYN.
- TCP SYN-ACK.
- TCP ACK.
- TLS ClientHello.
- TLS ServerHello.
- Encrypted TLS application data.
- TCP acknowledgments.
- Connection termination.

The exact sequence varies depending on protocol version, connection reuse, session resumption, and other factors.

### Important

Modern HTTPS encrypts HTTP content.

A passive packet capture usually cannot reveal the full HTTP request or response body without suitable decryption keys or endpoint access.

You can still inspect useful metadata such as:

- IP addresses.
- TCP ports.
- Packet sizes.
- Timing.
- TCP flags.
- TLS handshake information.

## Step 6 — Inspect the HTTP Response

Run:

```bash
curl -I https://example.com
```

This requests response headers using the HTTP HEAD method.

Example:

```text
HTTP/2 200
content-type: text/html
```

The actual response may differ.

For a complete request and response:

```bash
curl -v https://example.com
```

## Step 7 — Record Your Observations

| Observation | Result |
|---|---|
| Domain | example.com |
| DNS IPv4 address | |
| DNS IPv6 address | |
| Default gateway | |
| Destination port | 443 |
| TCP connection established | |
| TLS version | |
| Certificate validation | |
| HTTP status code | |
| Response content type | |
| Approximate latency | |

---

# 28. Practical Commands and Packet Analysis

## 28.1 DNS

```bash
dig example.com
```

```bash
nslookup example.com
```

## 28.2 IP Configuration

```bash
ip addr
```

```bash
ip route
```

## 28.3 Connectivity

```bash
ping example.com
```

## 28.4 Route Inspection

```bash
traceroute example.com
```

Windows:

```powershell
tracert example.com
```

## 28.5 TCP Port Connectivity

```bash
nc -vz example.com 443
```

## 28.6 HTTPS Request

```bash
curl -v https://example.com
```

## 28.7 TLS Certificate Inspection

```bash
openssl s_client -connect example.com:443 -servername example.com
```

The `-servername` option sends the hostname using Server Name Indication (SNI), which helps the server select the appropriate TLS configuration.

## 28.8 Packet Capture Using tcpdump

On a Linux system, capture traffic to or from TCP port 443:

```bash
sudo tcpdump -i any 'tcp port 443'
```

To save the capture:

```bash
sudo tcpdump -i any 'tcp port 443' -w https-capture.pcap
```

Open the resulting file in Wireshark.

Use packet capture only on systems and networks where you have authorization.

---

# 29. Common Interview Questions

## Q1. What is the OSI model?

The OSI model is a seven-layer reference model that describes how data is communicated between networked devices.

## Q2. Name the seven OSI layers.

1. Physical.
2. Data Link.
3. Network.
4. Transport.
5. Session.
6. Presentation.
7. Application.

## Q3. Which OSI layer uses MAC addresses?

The Data Link Layer, Layer 2.

## Q4. Which OSI layer uses IP addresses?

The Network Layer, Layer 3.

## Q5. Which OSI layer uses port numbers?

The Transport Layer, Layer 4.

## Q6. What is the difference between TCP and UDP?

TCP provides reliable, ordered byte-stream communication.

UDP provides connectionless datagram communication without TCP-style delivery and ordering guarantees.

## Q7. What is encapsulation?

Encapsulation is the process of adding protocol headers and, where applicable, trailers as data moves down the networking stack.

## Q8. What is decapsulation?

Decapsulation is the process of processing and removing protocol headers and trailers as data moves up the receiving stack.

## Q9. What is the difference between a frame and a packet?

A frame is a Data Link Layer data unit.

A packet is a Network Layer data unit.

## Q10. What is the difference between OSI and TCP/IP?

OSI has seven conceptual layers.

TCP/IP is a four-layer model commonly used to describe Internet communication.

## Q11. Which layer is responsible for routing?

The Network Layer, Layer 3.

## Q12. Which layer is responsible for end-to-end transport?

The Transport Layer, Layer 4.

## Q13. At which layer does HTTP operate?

HTTP is an Application Layer protocol.

## Q14. At which layer does TLS operate?

TLS does not map perfectly to one OSI layer. It is commonly treated as a security protocol used by application protocols above the transport layer.

## Q15. What happens during a TCP three-way handshake?

The client sends SYN, the server replies with SYN-ACK, and the client sends ACK.

This establishes TCP connection state.

## Q16. What happens during an HTTPS request?

A typical HTTPS-over-TCP request involves:

1. DNS resolution.
2. TCP connection establishment.
3. TLS handshake.
4. HTTP request.
5. Server processing.
6. HTTP response.
7. TLS decryption and browser rendering.

## Q17. What is the role of a router?

A router forwards IP packets between networks using its routing table.

## Q18. What is the role of a switch?

A Layer 2 switch forwards Ethernet frames based on MAC addresses.

## Q19. What is the difference between encryption and encoding?

Encoding changes data representation.

Encryption protects confidentiality using cryptographic methods and keys.

Base64 is encoding, not encryption.

## Q20. Why is the OSI model useful in cybersecurity?

It helps security professionals understand network communication, locate vulnerabilities, analyze traffic, and identify appropriate security controls.

---

# 30. Key Takeaways

- The OSI model contains seven layers.
- The TCP/IP model commonly contains four layers.
- The OSI model is a reference framework, while TCP/IP closely describes Internet protocols.
- Physical Layer communication involves signals and transmission media.
- Data Link Layer communication uses frames and local link addressing.
- Network Layer communication uses IP addresses and routing.
- Transport Layer communication uses ports and protocols such as TCP and UDP.
- Session and Presentation functions are often implemented within application protocols and libraries.
- Application Layer protocols include HTTP, DNS, SSH, and SMTP.
- Encapsulation adds protocol information as data moves down the stack.
- Decapsulation processes that information as data moves up the stack.
- TCP provides reliable, ordered byte-stream communication.
- UDP provides connectionless datagram communication.
- HTTPS uses HTTP protected by TLS.
- HTTPS over TCP commonly uses TCP port 443.
- HTTP/3 uses QUIC over UDP.
- DNS resolution helps a browser determine the destination IP address.
- TLS protects the confidentiality and integrity of HTTPS communication.
- Wireshark and tcpdump are useful tools for understanding network traffic.
- The OSI model is valuable for troubleshooting and cybersecurity analysis.

---

# Further Reading

- [RFC Editor](https://www.rfc-editor.org/)
- [IETF](https://www.ietf.org/)
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000)
- [Wireshark Documentation](https://www.wireshark.org/docs/)
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/)

---

**End of Phase 2: OSI and TCP/IP Models**
