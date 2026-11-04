
# Phase 5: Transport Layer — TCP and UDP

# 8. TCP

## 8.1 What Is TCP?

**TCP (Transmission Control Protocol)** is a transport-layer protocol that provides reliable, ordered, and error-checked delivery of data between applications.

TCP operates over IP and is commonly used by applications that need reliable communication.

Examples include:

- HTTP and HTTPS
- SSH
- FTP
- SMTP
- IMAP
- Database connections

TCP provides a byte stream rather than preserving the boundaries of individual application messages.

### Main characteristics

- Connection-oriented
- Reliable delivery
- Ordered data delivery
- Error detection using checksums
- Retransmission of lost data
- Flow control
- Congestion control
- Full-duplex communication

> TCP reliability means that TCP attempts to deliver data correctly and in order. It does not guarantee that the application itself will successfully process the data.

---

## 8.2 Connection-Oriented Communication

TCP is called **connection-oriented** because communicating applications establish a logical connection before exchanging application data.

A TCP connection is identified by a combination of:

```text
Source IP address
Source port
Destination IP address
Destination port
Transport protocol
```

The combination of source and destination IP addresses and ports is often called the **four-tuple**. The transport protocol distinguishes TCP from UDP.

### General TCP communication

```text
Client                         Server
  |                               |
  |------ Establish connection -->|
  |                               |
  |<------ Data exchange -------->|
  |                               |
  |------ Close connection ------>|
```

TCP connection establishment and termination use control flags in TCP segments.

---

## 8.3 TCP Segment Structure

TCP transfers data in units called **segments**.

A TCP segment contains a TCP header and application data.

```text
+-------------------------+
| Source Port      16 bits|
+-------------------------+
| Destination Port 16 bits|
+-------------------------+
| Sequence Number  32 bits|
+-------------------------+
| Acknowledgment   32 bits|
+-------------------------+
| Header Length + Flags   |
+-------------------------+
| Window Size      16 bits|
+-------------------------+
| Checksum          16 bits|
+-------------------------+
| Urgent Pointer    16 bits|
+-------------------------+
| Options (optional)      |
+-------------------------+
| Application Data        |
+-------------------------+
```

### Important TCP header fields

| Field | Purpose |
|---|---|
| Source port | Identifies the sending application endpoint |
| Destination port | Identifies the receiving application endpoint |
| Sequence number | Identifies the position of data in the byte stream |
| Acknowledgment number | Indicates the next byte expected from the other side |
| Data offset | Specifies the TCP header length |
| Flags | Control connection establishment, termination, and other behavior |
| Window size | Advertises the receiver's available capacity |
| Checksum | Detects corruption in the TCP segment and pseudo-header |
| Urgent pointer | Used with the URG flag for urgent-data signaling |
| Options | Supports features such as MSS, window scaling, and timestamps |

### TCP header size

- Minimum TCP header: 20 bytes
- Maximum TCP header: 60 bytes

The header length varies because TCP options may be included.

---

## 8.4 Source and Destination Ports

TCP uses port numbers to identify application endpoints.

Example:

```text
Client: 192.168.1.10:51500
Server: 203.0.113.20:443
```

The client uses an ephemeral source port, while the server commonly listens on port 443 for HTTPS.

```text
Source port:      51500
Destination port: 443
```

Port numbers are 16 bits long:

```text
2^16 = 65,536 possible values
```

The range is:

```text
0 - 65535
```

Ports identify application endpoints; they do not identify the physical computer by themselves.

---

## 8.5 Sequence and Acknowledgment Numbers

TCP uses sequence and acknowledgment numbers to provide reliable, ordered delivery.

### Sequence number

The sequence number identifies the position of a byte in the TCP stream.

TCP sequence numbers count bytes, not individual packets.

### Acknowledgment number

The acknowledgment number indicates the next byte the receiver expects.

Example:

```text
Client sends 100 bytes:
Sequence number = 1000
Data length = 100

Server acknowledges:
Acknowledgment number = 1100
```

The acknowledgment means:

```text
"I have received bytes through 1099.
I expect byte 1100 next."
```

### Cumulative acknowledgments

TCP commonly uses cumulative acknowledgments.

An acknowledgment for byte 1100 confirms receipt of all preceding bytes in the stream up to byte 1099.

If a segment is lost, the receiver may continue acknowledging the last contiguous byte received.

---

## 8.6 SYN, ACK, FIN, and RST Flags

TCP uses flags to control connection behavior.

| Flag | Meaning | Purpose |
|---|---|---|
| SYN | Synchronize | Establishes a connection and synchronizes sequence numbers |
| ACK | Acknowledgment | Acknowledges received data or control information |
| FIN | Finish | Indicates that the sender has finished sending data |
| RST | Reset | Abruptly resets or rejects a connection |
| PSH | Push | Requests prompt delivery of data to the receiving application |
| URG | Urgent | Indicates urgent data handling |
| ECE | ECN Echo | Used in Explicit Congestion Notification |
| CWR | Congestion Window Reduced | Indicates response to congestion notification |

### Common flag combinations

```text
SYN       Connection initiation
SYN, ACK  Connection acknowledgment
ACK       Acknowledgment
FIN, ACK  Orderly connection termination
RST       Connection reset
```

---

## 8.7 TCP Three-Way Handshake

TCP uses a three-way handshake to establish a connection.

### Steps

1. Client sends SYN.
2. Server responds with SYN-ACK.
3. Client sends ACK.

```text
Client                              Server
  |                                   |
  |------------ SYN ---------------->|
  |                                   |
  |<--------- SYN + ACK ---------------|
  |                                   |
  |------------ ACK ---------------->|
  |                                   |
  |         Connection established    |
```

### Example with sequence numbers

Suppose the client chooses an initial sequence number of 1000 and the server chooses 5000.

```text
Client → Server:
SYN, Seq = 1000

Server → Client:
SYN + ACK, Seq = 5000, Ack = 1001

Client → Server:
ACK, Seq = 1001, Ack = 5001
```

SYN consumes one sequence number, even though it does not carry application data.

### Why the handshake is needed

- Synchronizes sequence numbers.
- Confirms that both endpoints can communicate.
- Negotiates TCP options.
- Establishes connection state at both endpoints.

---

## 8.8 TCP Connection Termination

TCP connections are commonly closed using a four-step exchange because each direction of a TCP connection can be closed independently.

```text
Client                              Server
  |                                   |
  |------------ FIN ---------------->|
  |                                   |
  |<----------- ACK -----------------|
  |                                   |
  |<----------- FIN -----------------|
  |                                   |
  |------------ ACK ---------------->|
  |                                   |
  |          Connection closed        |
```

### Why four messages?

TCP is full-duplex. Each endpoint can independently indicate that it has no more data to send.

The first FIN closes one direction. The other endpoint may still send data before sending its own FIN.

### FIN vs RST

| FIN | RST |
|---|---|
| Orderly shutdown | Abrupt reset |
| Allows remaining data to be handled normally | Discards or interrupts connection state |
| Common in normal connection closure | Common when a connection is rejected or invalid |

A RST can occur for several reasons, including connecting to a closed port or an application aborting a connection.

---

## 8.9 Reliable Delivery

TCP provides reliability through mechanisms such as:

- Sequence numbers
- Acknowledgments
- Checksums
- Retransmissions
- Reordering received data
- Duplicate-data detection

### Example

Suppose a sender transmits:

```text
Segment 1
Segment 2
Segment 3
```

If Segment 2 is lost, the receiver may receive Segment 1 and Segment 3 but cannot deliver the stream to the application as though the missing bytes were present.

TCP uses acknowledgments and retransmission mechanisms to recover the missing data.

This ensures the receiving application gets an ordered byte stream.

---

## 8.10 Retransmissions

A TCP sender retransmits data when it determines that data has likely been lost.

Retransmission may be triggered by:

- A retransmission timeout (RTO)
- Duplicate acknowledgments and fast retransmission
- Other loss-detection mechanisms

### Retransmission timeout

If the sender does not receive an expected acknowledgment before the retransmission timer expires, it may retransmit the segment.

The timeout is calculated using estimates of the round-trip time (RTT) and its variation.

### Fast retransmission

In classic TCP behavior, receiving multiple duplicate acknowledgments can indicate that a segment was lost while later data arrived.

The sender may retransmit the missing segment without waiting for the timeout.

Modern TCP implementations may use additional loss-detection mechanisms.

---

## 8.11 Flow Control

**Flow control** prevents a sender from overwhelming the receiving application or its TCP receive buffer.

TCP uses a receiver-advertised window.

The receiver tells the sender how much additional data it can accept.

Example:

```text
Receiver advertises:
Window = 8000 bytes
```

The sender should keep the amount of unacknowledged data within the allowed receive window, subject to other TCP constraints.

### Purpose

Flow control protects the receiver.

It is different from congestion control, which protects the network.

---

## 8.12 Congestion Control — Fundamentals

**Congestion control** helps prevent too much traffic from overwhelming the network.

TCP uses a congestion window (`cwnd`) to control how much data may be outstanding in the network.

The sender's usable sending window is constrained by both:

```text
Receiver window (rwnd)
Congestion window (cwnd)
```

Conceptually:

```text
Allowed outstanding data
    ≤ min(rwnd, cwnd)
```

### Common congestion-control concepts

- Slow start
- Congestion avoidance
- Loss detection
- Congestion response
- Congestion window reduction

### Slow start

TCP begins with a relatively small congestion window and increases it as acknowledgments arrive.

The growth is approximately exponential per round-trip time during the slow-start phase, subject to implementation details and limits.

### Congestion avoidance

After reaching a threshold, TCP generally increases its congestion window more cautiously.

### Important distinction

- Flow control protects the receiver.
- Congestion control protects the network.

---

## 8.13 TCP Windows

TCP uses windows to allow multiple bytes to be in transit before acknowledgment.

Without a window, the sender might need to wait for an acknowledgment after every small piece of data, reducing throughput.

### Sliding window concept

```text
Sequence space:

[ Acknowledged ][ Data in flight ][ Allowed to send ][ Not yet allowed ]
```

As acknowledgments arrive, the window slides forward.

### Window scaling

The TCP window field is 16 bits and has a maximum unscaled value of 65,535 bytes.

The TCP Window Scale option allows larger effective windows to support high-bandwidth, high-latency networks.

### Example

A connection with a high bandwidth-delay product may need a receive window larger than 65,535 bytes to achieve full throughput.

Window scaling allows the advertised window to represent a much larger value.

---

## 8.14 TCP States

TCP endpoints move through states during connection establishment, data transfer, and termination.

Common TCP states include:

| State | Meaning |
|---|---|
| LISTEN | Waiting for an incoming connection |
| SYN-SENT | SYN sent; waiting for a response |
| SYN-RECEIVED | SYN received and SYN-ACK sent |
| ESTABLISHED | Connection is open for data transfer |
| FIN-WAIT-1 | FIN sent; waiting for acknowledgment or peer FIN |
| FIN-WAIT-2 | FIN acknowledged; waiting for peer FIN |
| CLOSE-WAIT | Peer sent FIN; local application has not fully closed |
| LAST-ACK | Local FIN sent while waiting for final acknowledgment |
| CLOSING | Both endpoints sent FIN before receiving acknowledgment |
| TIME-WAIT | Waiting to ensure delayed segments expire and final ACK can be retransmitted if needed |
| CLOSED | No connection state remains |

### Important states for troubleshooting

- `LISTEN`: a service is waiting for connections.
- `ESTABLISHED`: an active connection exists.
- `TIME-WAIT`: often normal after connections close.
- `CLOSE-WAIT`: may indicate an application has not closed its side of a connection.

A large number of `CLOSE-WAIT` sockets can sometimes point to an application resource-management problem.

---

## 8.15 Half-Open Connections — Concepts

A half-open TCP connection refers to a situation where one endpoint believes a connection exists while the other endpoint does not, or where connection setup is incomplete.

The term is used in different contexts.

### Incomplete handshake

A client sends SYN, but the handshake does not complete.

The server may maintain state while waiting for the final ACK.

### One-sided failure

A host may lose connection state because of a reboot, network failure, or application problem, while the other endpoint still believes the connection is active.

### Security relevance

Large numbers of incomplete connection attempts can consume server resources.

Defenses include:

- SYN cookies where supported
- Connection-rate limiting
- Appropriate firewall policies
- Monitoring connection states
- Keeping network services updated

---

## 8.16 Connection Timeouts

TCP connections use timers for several purposes:

- Retransmission timeout
- Connection establishment timeout
- Keepalive probes
- Persist timer for zero-window conditions
- TIME-WAIT duration

A timeout is not always a fixed universal value. Operating systems and applications may configure different limits.

### Common causes of timeout

- Remote host is unavailable.
- Packets are dropped by a firewall.
- Network route is broken.
- Server is overloaded.
- Application is not responding.
- The connection is silently filtered.

### Timeout vs refusal

A connection refusal often means a TCP RST was received, commonly because no service is listening on the destination port.

A timeout often means no response arrived before the client gave up.

---

## 8.17 TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection model | Connection-oriented | Connectionless |
| Reliability | Built-in retransmission and acknowledgment | No built-in delivery guarantee |
| Ordering | Ordered byte stream | Datagrams may arrive out of order |
| Data boundaries | Byte stream | Preserves datagram boundaries |
| Flow control | Yes | No built-in transport flow control |
| Congestion control | Built-in TCP mechanisms | Application or protocol must handle it if needed |
| Header size | At least 20 bytes | 8 bytes |
| Common uses | HTTPS, SSH, email, databases | DNS, VoIP, streaming, QUIC |

TCP is not always slower than UDP in every situation. Performance depends on application requirements, network conditions, protocol design, and implementation.

---

## 8.18 How TCP Carries HTTP and HTTPS Traffic

HTTP can operate over TCP.

For HTTP/1.1 and HTTP/2, a common transport is TCP.

### HTTP example

```text
Client
  |
  | TCP connection to port 80
  |
  | HTTP request
  v
Web server
```

For HTTPS over TCP, TLS is used to encrypt and authenticate the application communication.

```text
Client
  |
  | TCP connection to port 443
  |
  | TLS handshake
  |
  | Encrypted HTTP data
  v
Web server
```

### Typical HTTPS connection

1. Client resolves the server name through DNS.
2. Client establishes a TCP connection to the server.
3. Client and server perform a TLS handshake.
4. HTTP data is exchanged inside TLS.
5. TCP provides ordered and reliable delivery.

HTTP/3 is different: it uses QUIC over UDP rather than TCP.

---

# 9. UDP

## 9.1 What Is UDP?

**UDP (User Datagram Protocol)** is a transport-layer protocol that sends datagrams without establishing a connection.

UDP provides a lightweight way to send data between applications.

UDP does not provide built-in:

- Connection establishment
- Delivery acknowledgments
- Retransmissions
- Ordered delivery
- Flow control
- Congestion control

Applications may implement some of these features themselves.

### Common UDP applications

- DNS
- DHCP
- NTP
- VoIP
- Real-time video and audio
- Online games
- QUIC

---

## 9.2 Connectionless Communication

UDP is called connectionless because it does not perform a transport-layer handshake before sending datagrams.

```text
Client                         Server
  |                               |
  |--------- UDP datagram ------->|
  |                               |
  |--------- UDP datagram ------->|
  |                               |
```

A UDP application can send a datagram without first establishing a TCP-style connection.

However, applications may still maintain their own session or connection-like state.

---

## 9.3 UDP Datagram Structure

UDP has a simple 8-byte header.

```text
+-------------------------+
| Source Port      16 bits|
+-------------------------+
| Destination Port 16 bits|
+-------------------------+
| Length           16 bits|
+-------------------------+
| Checksum         16 bits|
+-------------------------+
| Application Data        |
+-------------------------+
```

### UDP header fields

| Field | Purpose |
|---|---|
| Source port | Identifies the sending application endpoint |
| Destination port | Identifies the receiving application endpoint |
| Length | Total UDP header and data length |
| Checksum | Detects corruption in the UDP datagram and pseudo-header |

The UDP header is 8 bytes long.

The UDP checksum is mandatory in IPv6, with a narrow exception for certain tunnel cases. In IPv4, a UDP checksum of zero can indicate that no checksum was provided.

---

## 9.4 UDP Ports

UDP uses 16-bit port numbers, just like TCP.

```text
Port range: 0 - 65535
```

UDP and TCP port spaces are separate.

For example, a service may use:

```text
TCP port 53
UDP port 53
```

These are distinct transport endpoints.

DNS commonly uses UDP port 53 for ordinary queries, but it can also use TCP port 53.

---

## 9.5 No Built-In Delivery Guarantee

UDP does not guarantee that a datagram will:

- Reach the destination.
- Arrive only once.
- Arrive in order.
- Be acknowledged by the receiver.

Example:

```text
Sender sends: A → B → C

Receiver gets: A → C
```

Datagram B may have been lost.

UDP itself does not retransmit B.

If the application requires reliability, it must implement it or use a protocol that provides it.

---

## 9.6 UDP vs TCP Performance Trade-Offs

UDP has a smaller header and does not require a TCP handshake.

This can reduce overhead for applications that need quick, independent datagrams.

However, UDP is not automatically faster or better.

### UDP may be useful when

- Low latency is important.
- Some packet loss is acceptable.
- Data is sent in independent messages.
- The application implements its own recovery or congestion control.
- The application uses a protocol such as QUIC.

### TCP may be useful when

- Reliable delivery is required.
- Data must arrive in order.
- The application benefits from built-in flow and congestion control.
- The application needs a simple reliable byte stream.

---

## 9.7 Common UDP Applications

| Application | Common UDP port | Purpose |
|---|---:|---|
| DNS | 53 | Name resolution |
| DHCPv4 server | 67 | Address configuration |
| DHCPv4 client | 68 | Address configuration |
| TFTP | 69 | Simple file transfer |
| NTP | 123 | Time synchronization |
| SNMP | 161 | Network management |
| SNMP traps | 162 | Notifications |
| Syslog | 514 | Logging, commonly UDP |
| RADIUS authentication | 1812 | Authentication |
| RADIUS accounting | 1813 | Accounting |
| QUIC | Often 443 | Modern transport used by HTTP/3 |

Port numbers are conventions, not guarantees. A service can use a different port.

---

## 9.8 DNS over UDP and TCP

DNS commonly uses UDP port 53 for ordinary queries.

Example:

```text
Client → UDP port 53 → DNS server
```

DNS can also use TCP port 53.

TCP is used in cases such as:

- Zone transfers
- Responses that require TCP
- Situations where DNS message size or protocol behavior calls for TCP

Modern DNS implementations must support both UDP and TCP.

### DNS query flow

```text
Application
    |
    | DNS query
    v
Local resolver
    |
    | UDP or TCP port 53
    v
DNS server
    |
    | DNS response
    v
Application
```

DNS may also be carried over encrypted transports such as DNS over TLS or DNS over HTTPS.

---

## 9.9 QUIC and Its Use of UDP

**QUIC** is a modern transport protocol that runs over UDP.

It provides features including:

- Reliable delivery for streams
- Congestion control
- Encryption integrated into connection establishment
- Stream multiplexing
- Connection migration support

HTTP/3 uses QUIC.

### Why QUIC uses UDP

UDP provides a simple datagram transport. QUIC implements its own transport features above UDP.

This allows QUIC to evolve transport behavior without requiring changes to the operating system's TCP implementation.

### Conceptual stack

```text
HTTP/3
   ↓
QUIC
   ↓
UDP
   ↓
IP
```

QUIC is not simply "unreliable UDP." It implements reliability and other transport functions at a higher layer.

---

## 9.10 How Applications Add Reliability When Needed

An application using UDP can implement reliability mechanisms such as:

- Sequence numbers
- Acknowledgments
- Retransmissions
- Duplicate detection
- Reordering buffers
- Congestion control
- Flow control

### Simple conceptual example

The sender transmits:

```text
Message 1, sequence 100
Message 2, sequence 101
Message 3, sequence 102
```

The receiver acknowledges received messages.

If message 101 is missing, the sender may retransmit it.

This resembles some TCP features, but the application is responsible for implementing and maintaining the behavior.

QUIC is a well-known example of a protocol that provides reliable streams over UDP.

---

# 10. Ports and Sockets

## 10.1 What Is a Port?

A **port** is a 16-bit number used by transport protocols to identify an application endpoint on a host.

An IP address identifies a host or network interface at the network layer. A port helps identify the application endpoint.

Example:

```text
192.168.1.10:443
```

Here:

- `192.168.1.10` is the IP address.
- `443` is the port number.

TCP and UDP maintain separate port spaces.

---

## 10.2 Source Port vs Destination Port

A transport segment or datagram contains a source port and destination port.

Example:

```text
Client: 192.168.1.10:51500
Server: 203.0.113.20:443
```

The client sends:

```text
Source port:      51500
Destination port: 443
```

The server response commonly reverses the endpoints:

```text
Source port:      443
Destination port: 51500
```

The client source port is often dynamically assigned from the ephemeral range.

---

## 10.3 Well-Known, Registered, and Dynamic Ports

IANA divides port numbers into three broad ranges.

| Range | Name | Typical purpose |
|---|---|---|
| 0–1023 | System / well-known ports | Common standard services |
| 1024–49151 | User / registered ports | Registered application services |
| 49152–65535 | Dynamic / private ports | Common ephemeral client ports |

Operating systems may use different ephemeral-port ranges. The ranges above are the IANA categories.

### Examples

```text
22    SSH
80    HTTP
443   HTTPS
3306  MySQL
```

A client may use a temporary source port such as:

```text
51500
```

The temporary port allows the operating system to distinguish multiple simultaneous connections.

---

## 10.4 Listening vs Established Ports

### Listening

A service is waiting for incoming connections or datagrams.

Example:

```text
TCP 0.0.0.0:22 LISTEN
```

This indicates a TCP service listening on port 22 across IPv4 interfaces.

### Established

A TCP connection has been established between two endpoints.

Example:

```text
192.168.1.10:51500 → 203.0.113.20:443
```

A listening socket and an established connection are different states.

A server can have one listening socket and many established connections associated with that service.

---

## 10.5 What Is a Socket?

A **socket** is a software endpoint used by an application to send or receive data over a network.

A socket is associated with:

- A transport protocol
- A local IP address
- A local port
- For connected sockets, a remote IP address and port

A TCP connection is commonly distinguished by the four-tuple:

```text
Source IP
Source port
Destination IP
Destination port
```

The protocol is TCP.

### Example

```text
TCP
192.168.1.10:51500
203.0.113.20:443
```

This identifies one TCP connection.

Multiple TCP connections can use the same server IP and port, as long as their endpoint combinations differ.

---

## 10.6 IP Address + Port + Transport Protocol

A transport endpoint is commonly represented as:

```text
IP address + port + transport protocol
```

Examples:

```text
192.168.1.10:53/UDP
192.168.1.10:53/TCP
```

These are different endpoints because TCP and UDP are distinct protocols.

### Socket examples

A DNS server may listen on:

```text
UDP 0.0.0.0:53
TCP 0.0.0.0:53
```

It can receive DNS requests over both protocols.

---

## 10.7 Binding to an Interface

When an application starts a network service, it can bind its socket to a specific IP address or interface.

### Bind to loopback

```text
127.0.0.1:8000
```

The service is reachable only through the IPv4 loopback interface on that host.

### Bind to a specific LAN address

```text
192.168.1.10:8000
```

The service listens on that specific address.

### Bind to all IPv4 interfaces

```text
0.0.0.0:8000
```

The service listens on all local IPv4 interfaces, subject to the operating system and firewall.

### Security relevance

Binding to all interfaces can expose a development service to other devices on the network.

Before starting a service, check which address it binds to and whether a firewall permits incoming connections.

---

## 10.8 `localhost` vs `0.0.0.0`

### `localhost`

`localhost` is a hostname that normally resolves to loopback addresses.

Common loopback addresses:

```text
IPv4: 127.0.0.1
IPv6: ::1
```

A service bound to loopback is generally accessible only from the local machine.

### `0.0.0.0`

For IPv4, `0.0.0.0` is commonly used as a wildcard bind address.

It means:

```text
Listen on all local IPv4 interfaces
```

It is not a normal destination address for remote clients to connect to.

### Comparison

| Address | Common meaning |
|---|---|
| `127.0.0.1` | IPv4 loopback |
| `::1` | IPv6 loopback |
| `localhost` | Hostname commonly resolving to loopback |
| `0.0.0.0` | Wildcard IPv4 bind address |
| `::` | Wildcard IPv6 bind address, depending on socket configuration |

A wildcard IPv6 socket may or may not also accept IPv4 connections, depending on the operating system and socket settings.

---

## 10.9 Port Forwarding

**Port forwarding** directs incoming traffic received at one network endpoint to another endpoint.

It can be configured in:

- Routers
- Firewalls
- Virtual machines
- Containers
- Cloud networking systems

### Example: Router port forwarding

```text
Internet client
      |
      | Public IP:443
      v
Home router
      |
      | Forward to 192.168.1.20:443
      v
Internal web server
```

Port forwarding can make an internal service reachable from outside the local network.

### Security considerations

- Expose only necessary services.
- Use strong authentication.
- Keep exposed services patched.
- Restrict source addresses where possible.
- Monitor access logs.
- Avoid exposing administrative interfaces unnecessarily.

---

## 10.10 Port Conflicts

A port conflict occurs when two applications attempt to bind to the same local address and port in a way that the operating system does not permit.

Example:

```text
Application A → 127.0.0.1:8000
Application B → 127.0.0.1:8000
```

The second application may fail with an error such as:

```text
Address already in use
```

Whether multiple sockets can share a port depends on the protocol, address, socket options, and operating-system rules.

### Troubleshooting

Find the process listening on a port:

```bash
sudo ss -lntup
```

Check a specific port:

```bash
sudo ss -lntup | grep ':8000'
```

Use another port or stop the conflicting service if appropriate.

---

## 10.11 Firewall Rules and Ports

Firewalls control network traffic based on rules.

Rules may consider:

- Source IP address
- Destination IP address
- Transport protocol
- Source port
- Destination port
- Connection state
- Network interface

### Example policy

```text
Allow TCP destination port 443
Deny unsolicited inbound TCP destination port 22
```

This is only a conceptual example. Actual firewall rules depend on the firewall system and network design.

### Important points

- TCP port 443 and UDP port 443 are different.
- A service listening on a port does not guarantee that it is reachable.
- A firewall may block traffic before it reaches the service.
- A service may be listening only on loopback.
- NAT or routing may prevent external reachability.

---

## 10.12 Service Discovery and Port Scanning Concepts

**Service discovery** identifies which network services are available on a host.

A port scan checks whether selected ports appear open, closed, or filtered.

### Common scan interpretations

| Result | General meaning |
|---|---|
| Open | A service is accepting connections or responding on the port |
| Closed | The host is reachable, but no service is listening on the port |
| Filtered | A firewall or network behavior prevents a clear determination |

The exact interpretation depends on the scan type and response.

### TCP connection scan concept

A scanner attempts to establish a TCP connection to a destination port.

If the handshake completes, the port is generally considered open.

If a TCP RST is received, the port is commonly considered closed.

If no response arrives, the port may be filtered or the host may be unreachable.

### Authorized use

Only scan systems you own or have explicit permission to test.

For learning, use your own local machine or an isolated lab environment.

---

# Important Ports to Memorize

Ports are conventions, not guarantees. A service can run on a different port, and a port can be used by a different application.

| Port | Common service |
|---|---|
| 20/21 | FTP data/control, depending on mode |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCPv4 |
| 69 | TFTP |
| 80 | HTTP |
| 110 | POP3 |
| 123 | NTP |
| 143 | IMAP |
| 161/162 | SNMP |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 465 | Common SMTP submission over implicit TLS |
| 500 | IKE/IPsec |
| 514 | Syslog, commonly UDP |
| 587 | SMTP submission, commonly with STARTTLS |
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

### Port memory groups

```text
Web:
80  HTTP
443 HTTPS

Remote access:
22   SSH
23   Telnet
3389 RDP

Email:
25   SMTP
110  POP3
143  IMAP
465  SMTP over implicit TLS
587  SMTP submission
993  IMAPS
995  POP3S

Databases:
1433  Microsoft SQL Server
3306  MySQL
5432  PostgreSQL
6379  Redis
27017 MongoDB

Network services:
53    DNS
67/68 DHCPv4
123   NTP
161/162 SNMP
389   LDAP
445   SMB
500   IKE/IPsec
514   Syslog
```

---

# Practical Tasks

## Task 1: Inspect Listening and Established Sockets

Run:

```bash
ss -tuln
```

Options:

- `-t`: TCP
- `-u`: UDP
- `-l`: listening sockets
- `-n`: numeric addresses and ports

Show TCP sockets:

```bash
ss -tn
```

Show UDP sockets:

```bash
ss -un
```

Show listening TCP sockets:

```bash
ss -ltn
```

Show listening UDP sockets:

```bash
ss -lun
```

Show processes associated with sockets:

```bash
sudo ss -tulnp
```

Look for:

- Local address
- Local port
- TCP state
- Process name, if available

---

## Task 2: Check Whether a Port Is Open Locally

Start a simple local HTTP server using Python:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

In another terminal, inspect the listener:

```bash
ss -ltn
```

You should see a listener on:

```text
127.0.0.1:8000
```

Test it:

```bash
curl http://127.0.0.1:8000
```

Because it is bound to loopback, another device on the LAN should not be able to access it through the machine's LAN address.

Stop the server with:

```text
Ctrl + C
```

---

## Task 3: Compare `localhost` and `0.0.0.0`

Start a server bound to loopback:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Inspect:

```bash
ss -ltn
```

Then stop it and start a server bound to all IPv4 interfaces:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

Inspect again:

```bash
ss -ltn
```

Notice the difference in the local address.

A service bound to `0.0.0.0` may be reachable through the machine's LAN IP, subject to firewall rules and network configuration.

Use this only on your own machine and network.

---

## Task 4: Observe a TCP Three-Way Handshake in Wireshark

1. Open Wireshark.
2. Capture traffic on the interface you are using.
3. Visit a website or connect to a local test service.
4. Apply a display filter:

```text
tcp
```

To narrow the capture to a specific port:

```text
tcp.port == 443
```

Look for:

```text
SYN
SYN, ACK
ACK
```

Record:

- Source IP
- Destination IP
- Source port
- Destination port
- Initial sequence number
- Acknowledgment number

A packet capture may not show every handshake packet if capture begins after the connection is already established.

---

## Task 5: Inspect TCP Connection States

Run:

```bash
ss -tan
```

Look for states such as:

```text
LISTEN
ESTABLISHED
TIME-WAIT
CLOSE-WAIT
```

To show listening TCP sockets:

```bash
ss -ltn
```

To show established TCP connections:

```bash
ss -tn state established
```

---

## Task 6: Test TCP and UDP with Netcat

Netcat implementations differ, so command options may vary.

### TCP listener

On one terminal:

```bash
nc -l 9000
```

On another terminal:

```bash
nc 127.0.0.1 9000
```

Type text into either terminal and observe how it is transferred.

### UDP listener

On one terminal:

```bash
nc -u -l 9001
```

On another terminal:

```bash
nc -u 127.0.0.1 9001
```

UDP does not establish a TCP-style connection. The application may still wait for datagrams.

Use only local or authorized systems for these exercises.

---

# Cybersecurity Connection

Understanding TCP, UDP, and ports is essential for:

- Network service discovery.
- Interpreting port scan results.
- Understanding firewall rules.
- Troubleshooting connectivity.
- Analyzing packet captures.
- Identifying exposed services.
- Understanding web application traffic.
- Reviewing database and remote-access exposure.

For web and application security, pay particular attention to:

- TCP connections to HTTP and HTTPS services.
- TLS and HTTP request flows.
- Listening ports on development servers.
- Services accidentally bound to `0.0.0.0`.
- Databases exposed beyond their intended network.
- Differences between a closed port and a filtered port.

Only scan or test systems you own or have explicit permission to assess.

---

# Interview Questions

## TCP

1. What is TCP?
2. Why is TCP called connection-oriented?
3. What is a TCP segment?
4. What is the purpose of sequence numbers?
5. What is an acknowledgment number?
6. Explain the TCP three-way handshake.
7. What is the purpose of SYN, ACK, FIN, and RST?
8. How does TCP provide reliable delivery?
9. What is the difference between flow control and congestion control?
10. What is a TCP sliding window?
11. What is the purpose of the TIME-WAIT state?
12. What is the difference between FIN and RST?
13. What does a TCP retransmission timeout indicate?
14. How does TCP carry HTTPS traffic?

## UDP

15. What is UDP?
16. Why is UDP called connectionless?
17. What fields exist in a UDP header?
18. Why is UDP often used for real-time communication?
19. Does UDP guarantee delivery?
20. How can an application implement reliability over UDP?
21. Why can DNS use both UDP and TCP?
22. What is QUIC, and why does it use UDP?

## Ports and Sockets

23. What is a port number?
24. What is the difference between a source port and destination port?
25. What is an ephemeral port?
26. What is a socket?
27. What is the difference between a listening socket and an established connection?
28. What is the difference between `localhost` and `0.0.0.0`?
29. What is port forwarding?
30. What does it mean when a port is open, closed, or filtered?
31. Why might a service be listening but still unreachable?
32. Why should databases not be exposed unnecessarily to public networks?

---

# Summary

- TCP provides reliable, ordered, connection-oriented communication.
- TCP uses sequence numbers, acknowledgments, retransmissions, and windows.
- The three-way handshake establishes a TCP connection.
- FIN is used for orderly shutdown; RST resets a connection.
- Flow control protects the receiver, while congestion control protects the network.
- UDP sends datagrams without a TCP-style handshake or built-in reliability.
- Applications can add reliability over UDP; QUIC is an important example.
- Ports identify application endpoints.
- A socket is a software endpoint for network communication.
- `localhost` normally refers to loopback; `0.0.0.0` is commonly used as an IPv4 wildcard bind address.
- Listening services can be inspected with `ss`.
- Port numbers are conventions, not guarantees.
- Always check service binding and firewall configuration to understand real network exposure.
