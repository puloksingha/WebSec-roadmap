
# Phase 7: Linux Networking Fundamentals for Cybersecurity

## Learning Objectives

By the end of this phase, you should be able to:

- Understand how computer networks communicate.
- Understand IPv4, IPv6, MAC addresses, ports, and protocols.
- Understand how DNS, DHCP, ARP, ICMP, and NAT work.
- Understand routing, subnets, gateways, and CIDR notation.
- Understand TCP, UDP, HTTP, HTTPS, and TLS.
- Understand firewalls, proxies, and VPNs.
- Inspect and troubleshoot network configurations using Linux.
- Monitor network connections and capture network packets.
- Understand the network-related information displayed by tools such as Nmap and Burp Suite.

---

# 1. Introduction to Computer Networking

## 1.1 What Is Computer Networking?

Computer networking is the process of connecting two or more computing devices so that they can communicate and exchange information.

A network allows computers, servers, smartphones, routers, and other devices to share resources and communicate with one another.

For example:

- Your laptop connects to your Wi-Fi router.
- Your router connects to your Internet Service Provider (ISP).
- Your ISP provides access to the internet.
- Your browser communicates with a web server.
- The web server sends the requested webpage back to your browser.

### Simple Network Communication

```text
Your Laptop
     |
     | Wi-Fi
     |
Wi-Fi Router
     |
     | Internet Connection
     |
Internet Service Provider
     |
     |
Internet
     |
     |
Web Server
```

## 1.2 Why Is Networking Important in Cybersecurity?

Networking is one of the most important foundations of cybersecurity.

Security professionals need to understand how devices communicate before they can understand how network-based attacks and defenses work.

Networking knowledge is useful for:

- Understanding how web applications communicate.
- Identifying open ports and running services.
- Understanding HTTP requests and responses.
- Analyzing network traffic.
- Identifying suspicious connections.
- Understanding firewalls and network restrictions.
- Performing authorized network enumeration.
- Troubleshooting connectivity problems.
- Understanding how Burp Suite intercepts web traffic.
- Understanding how Nmap discovers network services.

## 1.3 Important Networking Terminology

| Term | Meaning |
|---|---|
| Network | A collection of connected devices |
| Host | A device connected to a network |
| Server | A system that provides services |
| Client | A system that requests services |
| Packet | A unit of data transmitted over a network layer |
| Protocol | A set of communication rules |
| IP address | A logical network address |
| MAC address | A link-layer hardware address |
| Port | A logical communication endpoint identifier |
| Router | A device that forwards packets between networks |
| Switch | A device that forwards Ethernet frames within a network |
| Gateway | A device or system providing access to another network |
| Bandwidth | The maximum data-transfer capacity of a connection |
| Latency | The time required for data to travel between endpoints |

---

# 2. IP Addresses: IPv4 and IPv6

## 2.1 What Is an IP Address?

An IP address (Internet Protocol address) is a logical address assigned to a network interface.

It helps identify the source and destination of IP packets so that devices can communicate across networks.

For example:

```text
192.168.1.10
```

This is an example of an IPv4 address.

An IP address is associated with a network interface, not necessarily permanently with an entire physical computer.

A computer may have multiple IP addresses because it has multiple network interfaces.

For example:

- Ethernet interface.
- Wi-Fi interface.
- Virtual machine interface.
- Loopback interface.

## 2.2 IPv4

IPv4 stands for Internet Protocol version 4.

It uses a 32-bit address.

An IPv4 address consists of four octets separated by dots.

Example:

```text
192.168.1.10
```

Each octet contains 8 bits.

Therefore:

```text
8 + 8 + 8 + 8 = 32 bits
```

Each octet can represent a decimal value from 0 to 255.

Example:

```text
192 . 168 . 1 . 10
 |     |    |   |
Octet Octet Octet Octet
```

### IPv4 Address Structure

An IPv4 address contains two logical parts:

1. Network portion.
2. Host portion.

The subnet mask or prefix length determines which bits identify the network and which bits identify the host.

For example:

```text
IP Address:  192.168.1.10
Prefix:      /24
Subnet Mask: 255.255.255.0
```

Here:

- Network address: `192.168.1.0`
- Host address: `192.168.1.10`
- Broadcast address: `192.168.1.255`

### Advantages of IPv4

- Widely supported.
- Easy to understand and configure.
- Supported by most networking equipment.
- Commonly used in local networks and internet communication.

### Limitations of IPv4

IPv4 has approximately 4.3 billion possible addresses.

The number of available public IPv4 addresses is limited, which is one reason IPv6 was developed.

## 2.3 IPv6

IPv6 stands for Internet Protocol version 6.

It uses a 128-bit address.

Example:

```text
2001:db8:abcd:0012:0000:0000:0000:0001
```

IPv6 addresses are written using hexadecimal values separated by colons.

### IPv6 Address Compression

IPv6 allows leading zeros in a group to be removed.

Example:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

Can be shortened to:

```text
2001:db8::1
```

The double colon represents one or more consecutive groups of zeros.

It can only be used once in an IPv6 address.

### Advantages of IPv6

- Very large address space.
- Supports stateless address autoconfiguration.
- Simplifies some aspects of network addressing.
- Supports multicast communication.
- Removes the IPv4 header checksum.
- Provides standardized IPsec support, although actual IPsec deployment is not automatically guaranteed.

### IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address size | 32 bits | 128 bits |
| Format | Decimal | Hexadecimal |
| Separator | Dot | Colon |
| Example | 192.168.1.10 | 2001:db8::1 |
| Address space | Approximately 4.3 billion | Extremely large |
| Broadcast | Supported | Not supported |
| Multicast | Supported | Supported |
| NAT | Commonly used | Generally not required for address conservation |
| Configuration | Manual or DHCP | Manual, SLAAC, or DHCPv6 |

## 2.4 How to Check IPv4 and IPv6 Addresses in Linux

Use:

```bash
ip addr
```

Or:

```bash
ip -4 addr
```

For IPv6:

```bash
ip -6 addr
```

Example output:

```text
2: eth0:
    inet 192.168.1.10/24
    inet6 fe80::1234:abcd:5678:1234/64
```

Explanation:

- `eth0`: Network interface name.
- `inet`: IPv4 address.
- `inet6`: IPv6 address.
- `/24`: IPv4 prefix length.
- `/64`: IPv6 prefix length.

## 2.5 Practical Exercise

**Objective:** Identify your Linux machine's IPv4 and IPv6 addresses.

Commands:

```bash
ip -4 addr
ip -6 addr
```

Observe:

- Which interfaces are available?
- Does your interface have an IPv4 address?
- Does it have an IPv6 address?
- Is the IPv6 address link-local or globally scoped?

Verification:

```bash
ip addr show
```

---

# 3. Public vs Private IP Addresses

## 3.1 What Is a Public IP Address?

A public IP address is an address that is globally routable across the public internet.

It is generally assigned by an ISP or an upstream network provider.

Example:

```text
8.8.8.8
1.1.1.1
```

Public IP addresses allow internet-facing systems to communicate across the internet.

### Characteristics

- Globally routable.
- Must be appropriately allocated.
- Used by internet-facing servers and network connections.
- Can be reachable from the internet when routing and firewall rules permit it.

A public IP address does not automatically mean that a device is accessible from the internet. Firewalls, NAT, and service configuration can prevent access.

## 3.2 What Is a Private IP Address?

Private IP addresses are reserved for internal networks.

They are not directly routed across the public internet.

For IPv4, the private ranges are defined by RFC 1918.

### Private IPv4 Address Ranges

| Range | CIDR | Address range |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Private |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Private |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | Private |

Examples:

```text
192.168.1.10
10.0.0.5
172.16.1.20
```

These addresses are commonly used in home networks, organizations, and virtual machine environments.

### Important Note

Not every address beginning with `172` is private.

Only the range `172.16.0.0` through `172.31.255.255` is private.

Similarly, not every `192.168`-looking address should be assumed to be globally routable.

## 3.3 How to Check Your Private IP Address

```bash
ip addr
```

Look for the `inet` field on your network interface.

## 3.4 How to Check Your Public IP Address

If your machine has internet access, you can use an external IP-checking service.

For example:

```bash
curl https://api.ipify.org
```

This sends an HTTP request to an external service and displays the public source IP address it observes.

Alternative:

```bash
curl https://ifconfig.me
```

These commands require internet connectivity and access to the relevant external services.

### Private IP vs Public IP

| Feature | Private IP | Public IP |
|---|---|---|
| Usage | Internal networks | Internet communication |
| Global routing | Not globally routed | Globally routable |
| Allocation | Locally configured or assigned | Public address allocation |
| Example | 192.168.1.10 | 8.8.8.8 |
| NAT | Commonly used for internet access | Not inherently required |

## 3.5 Cybersecurity Relevance

Understanding public and private IP addresses helps security professionals:

- Identify internal and external network boundaries.
- Understand network exposure.
- Analyze server configurations.
- Understand NAT behavior.
- Identify accidentally exposed services.
- Interpret network scan results.

**Important:** An IP address being public does not mean the host or service is vulnerable.

---

# 4. Loopback Address

## 4.1 What Is a Loopback Address?

A loopback address is a special IP address used by a computer to communicate with itself.

It does not require communication with another physical computer.

The most commonly used IPv4 loopback address is:

```text
127.0.0.1
```

For IPv6:

```text
::1
```

The complete IPv4 loopback range is:

```text
127.0.0.0/8
```

### What Is localhost?

`localhost` is a hostname that normally resolves to loopback addresses.

For example:

```text
localhost
127.0.0.1
::1
```

### How It Works

```text
Application
     |
     |
127.0.0.1
     |
     |
Local Network Stack
     |
     |
Same Computer
```

The traffic remains within the local machine.

## 4.2 Why Is Loopback Important?

Loopback addresses are used for:

- Testing applications locally.
- Running development servers.
- Testing local web applications.
- Communicating between local processes.
- Troubleshooting network applications.

### Example

Start a local Python HTTP server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open another terminal:

```bash
curl http://127.0.0.1:8000
```

You should receive an HTTP response containing a directory listing.

Stop the server using:

```text
Ctrl + C
```

### Important Security Difference

Compare:

```text
127.0.0.1
0.0.0.0
```

`127.0.0.1` means the application listens only on the IPv4 loopback interface.

`0.0.0.0` means the application listens on all applicable IPv4 interfaces.

For example:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

This can make the server accessible through other network interfaces, subject to firewall and network restrictions.

> Never expose a development server unnecessarily. Bind services to localhost when external access is not required.

---

# 5. MAC Addresses

## 5.1 What Is a MAC Address?

MAC stands for Media Access Control.

A MAC address is a link-layer address used to identify a network interface within a local network technology such as Ethernet or Wi-Fi.

A traditional Ethernet MAC address is 48 bits long.

Example:

```text
00:1A:2B:3C:4D:5E
```

It is generally represented using hexadecimal numbers.

### MAC Address Structure

A conventional 48-bit MAC address contains:

- First 24 bits: Organizationally Unique Identifier (OUI).
- Remaining 24 bits: Interface-specific identifier.

The OUI identifies an allocation associated with an organization.

However, MAC addresses can be locally administered or randomized, so the address does not always reveal the actual hardware manufacturer.

## 5.2 MAC Address vs IP Address

| Feature | MAC Address | IP Address |
|---|---|---|
| Purpose | Link-layer identification | Network-layer addressing |
| OSI layer | Layer 2 | Layer 3 |
| Format | Hexadecimal | IPv4 decimal or IPv6 hexadecimal |
| Example | 00:1A:2B:3C:4D:5E | 192.168.1.10 |
| Scope | Local network link | Network communication |
| Changes | Can be changed or randomized | Can change with network configuration |

## 5.3 How to Find a MAC Address in Linux

Command:

```bash
ip link
```

Example output:

```text
2: eth0:
    link/ether 00:1a:2b:3c:4d:5e
```

Here:

```text
link/ether
```

Indicates an Ethernet-style link-layer address.

Another command:

```bash
ip addr
```

Look for:

```text
link/ether
```

## 5.4 Change a MAC Address

Changing a MAC address is commonly called MAC spoofing.

For a lab interface, you can use:

```bash
sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 02:11:22:33:44:55
sudo ip link set dev eth0 up
```

Replace `eth0` with your actual interface name.

The address beginning with `02` is an example of a locally administered unicast MAC address.

Verify:

```bash
ip link show eth0
```

Restore the original hardware or virtual interface address by reconnecting the interface or using its previously recorded address.

> Changing a MAC address can disrupt network connectivity. Do not perform this on an interface you depend on without understanding the consequences.

## 5.5 Cybersecurity Relevance

MAC addresses are relevant to:

- Local network investigations.
- ARP analysis.
- Network device identification.
- MAC spoofing concepts.
- Wireless security.
- Network access controls.

MAC filtering should not be treated as strong authentication because MAC addresses can be changed or impersonated.

---

# 6. Subnets and CIDR Notation

## 6.1 What Is a Subnet?

A subnet is a logically divided portion of an IP network.

Subnetting divides a larger network into smaller networks.

It helps organizations:

- Organize network devices.
- Separate departments.
- Reduce broadcast domains.
- Manage IP addresses efficiently.
- Apply network access restrictions.

## 6.2 What Is a Subnet Mask?

A subnet mask identifies which bits of an IPv4 address represent the network and which represent the host.

Example:

```text
IP Address:  192.168.1.10
Subnet Mask: 255.255.255.0
```

The subnet mask contains 24 network bits and 8 host bits.

Binary representation:

```text
11111111.11111111.11111111.00000000
```

Therefore, the prefix length is `/24`.

## 6.3 What Is CIDR?

CIDR stands for Classless Inter-Domain Routing.

CIDR notation represents a network using an IP address followed by a slash and a prefix length.

Example:

```text
192.168.1.0/24
```

Here:

- `192.168.1.0` is the network address.
- `/24` means the first 24 bits are network bits.

### Common IPv4 Prefixes

| CIDR | Subnet Mask | Total IPv4 Addresses |
|---|---|---:|
| /8 | 255.0.0.0 | 16,777,216 |
| /16 | 255.255.0.0 | 65,536 |
| /24 | 255.255.255.0 | 256 |
| /25 | 255.255.255.128 | 128 |
| /26 | 255.255.255.192 | 64 |
| /27 | 255.255.255.224 | 32 |
| /28 | 255.255.255.240 | 16 |
| /30 | 255.255.255.252 | 4 |

For conventional IPv4 subnets, two addresses are reserved for the network and broadcast addresses.

Therefore, a `/24` normally provides 254 usable host addresses.

Special-purpose and point-to-point subnets have different considerations. IPv4 `/31` and `/32` have specific uses.

## 6.4 Understanding a /24 Network

Consider:

```text
192.168.1.0/24
```

Its details are:

```text
Network Address:   192.168.1.0
First Host:        192.168.1.1
Last Host:         192.168.1.254
Broadcast Address: 192.168.1.255
```

The total number of addresses is 256.

## 6.5 How to Identify Your Subnet in Linux

```bash
ip addr
```

Example:

```text
inet 192.168.1.10/24
```

This indicates that the interface has:

- IP address: `192.168.1.10`
- Prefix length: `/24`

## 6.6 Cybersecurity Relevance

Subnetting is important for:

- Understanding internal network ranges.
- Planning authorized network scans.
- Identifying network boundaries.
- Understanding firewall rules.
- Network segmentation.
- Interpreting Nmap scan targets.

Example of an authorized local subnet scan:

```bash
nmap -sn 192.168.1.0/24
```

This performs host discovery across the specified subnet.

Only scan networks for which you have authorization.

---

# 7. Default Gateway

## 7.1 What Is a Default Gateway?

A default gateway is the next-hop router used when a system needs to send packets to destinations for which it has no more specific routing entry.

For example, your laptop may have this configuration:

```text
IP Address:      192.168.1.10
Subnet Mask:     255.255.255.0
Default Gateway: 192.168.1.1
```

Your router is the default gateway.

### How It Works

Suppose your laptop wants to communicate with:

```text
8.8.8.8
```

Your laptop checks its routing table.

If the destination is outside its local network, it sends the packet to the default gateway.

```text
Laptop
192.168.1.10
      |
      |
      v
Router
192.168.1.1
      |
      |
      v
Internet
      |
      |
      v
8.8.8.8
```

## 7.2 How to Check the Default Gateway

Command:

```bash
ip route
```

Example output:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

Explanation:

- `default`: Default route.
- `via 192.168.1.1`: Gateway address.
- `dev eth0`: Interface used.
- `192.168.1.0/24`: Connected network.
- `src 192.168.1.10`: Preferred source address.

## 7.3 Practical Exercise

Run:

```bash
ip route
```

Identify:

1. Your default gateway.
2. Your network interface.
3. Your local subnet.
4. Your preferred source IP address.

---

# 8. Routing Tables

## 8.1 What Is Routing?

Routing is the process of selecting a path through which IP packets should travel to reach their destination.

Routers and computers use routing tables to determine where packets should be forwarded.

## 8.2 What Is a Routing Table?

A routing table is a collection of routes that tells the operating system how to forward packets.

It contains information such as:

- Destination network.
- Gateway or next hop.
- Network interface.
- Route metric.
- Preferred source address.

## 8.3 Linux Routing Command

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

### Important Routing Commands

Display IPv4 routes:

```bash
ip -4 route
```

Display IPv6 routes:

```bash
ip -6 route
```

Display all routing information:

```bash
ip route show table all
```

Check how a destination will be routed:

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.10
```

This indicates that the packet will use:

- Destination: `8.8.8.8`
- Gateway: `192.168.1.1`
- Interface: `eth0`
- Source address: `192.168.1.10`

## 8.4 Add and Remove a Route

Example of adding a route:

```bash
sudo ip route add 10.10.10.0/24 via 192.168.1.1
```

This adds a route for the `10.10.10.0/24` network through the specified gateway.

Remove it:

```bash
sudo ip route del 10.10.10.0/24 via 192.168.1.1
```

These are runtime configuration changes and may disappear after a reboot or network reconfiguration.

Do not add arbitrary routes to your working network.

## 8.5 Routing Process

```text
Application creates data
          |
          v
IP packet is created
          |
          v
Routing table is checked
          |
          v
Destination network identified
          |
          v
Next-hop selected
          |
          v
Packet forwarded through interface
```

## 8.6 Cybersecurity Relevance

Routing knowledge helps with:

- Understanding network paths.
- Investigating unreachable systems.
- Understanding network segmentation.
- Diagnosing routing problems.
- Identifying incorrect routes.
- Understanding VPN routing behavior.

---

# 9. TCP vs UDP

## 9.1 What Is TCP?

TCP stands for Transmission Control Protocol.

It is a connection-oriented transport-layer protocol.

TCP establishes a connection before normal data transfer and provides reliable, ordered delivery of a byte stream.

Its important characteristics include:

- Connection establishment.
- Reliable delivery.
- Sequence numbers.
- Acknowledgments.
- Retransmission.
- Flow control.
- Congestion control.
- Ordered data delivery.

TCP is commonly used by:

- HTTP/1.1.
- HTTP/2.
- SSH.
- SMTP.
- FTP control connections.

HTTP/3 is an important exception because it uses QUIC over UDP.

## 9.2 TCP Three-Way Handshake

Before normal TCP data transmission, a connection is established using a three-way handshake.

The three steps are:

1. SYN
2. SYN-ACK
3. ACK

### Diagram

```text
Client                         Server
  |                               |
  | -------- SYN ---------------->|
  |                               |
  |<------- SYN-ACK --------------|
  |                               |
  | -------- ACK ---------------->|
  |                               |
  |        Connection Established |
```

### Explanation

**Step 1: SYN**

The client sends a SYN packet to request a TCP connection.

**Step 2: SYN-ACK**

The server responds with SYN-ACK to acknowledge the request and synchronize sequence numbers.

**Step 3: ACK**

The client sends an ACK.

The TCP connection is now established.

## 9.3 What Is UDP?

UDP stands for User Datagram Protocol.

It is a connectionless transport-layer protocol.

UDP does not establish a TCP-style connection before sending datagrams.

Its characteristics include:

- No built-in delivery guarantee.
- No built-in retransmission.
- No built-in ordering guarantee.
- Lower protocol overhead.
- Supports broadcast and multicast in appropriate environments.

UDP is commonly used by:

- DNS queries.
- DHCP.
- VoIP.
- Online gaming.
- Streaming applications.
- QUIC.

Applications may implement their own reliability mechanisms over UDP.

## 9.4 TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Delivery | Reliable transport | No built-in guarantee |
| Ordering | Preserves byte-stream order | No built-in ordering |
| Acknowledgment | Yes | No |
| Retransmission | Yes | No built-in retransmission |
| Header size | Minimum 20 bytes | 8 bytes |
| Speed/overhead | More protocol overhead | Less protocol overhead |
| Common use | SSH, HTTP/1.1, HTTP/2 | DNS, DHCP, QUIC |

## 9.5 TCP and UDP Ports

Both TCP and UDP use 16-bit port numbers.

Port range:

```text
0 - 65535
```

Common examples:

| Port | Protocol | Common Service |
|---|---|---|
| 20/21 | TCP | FTP data/control |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 67/68 | UDP | DHCP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 443 | UDP | QUIC/HTTP/3 |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 8080 | TCP | Common alternative HTTP port |

These are common defaults, not proof that a particular service is running on a port.

## 9.6 Cybersecurity Relevance

Understanding TCP and UDP helps with:

- Port scanning.
- Service identification.
- Packet analysis.
- Understanding Nmap output.
- Understanding firewall behavior.
- Troubleshooting application communication.
- Understanding TCP handshakes in Wireshark and tcpdump.

---

# 10. Ports and Sockets

## 10.1 What Is a Port?

A port is a logical number used by transport-layer protocols to identify an application endpoint.

An IP address identifies a network interface at the network layer.

A port identifies a communication endpoint within the transport protocol.

Example:

```text
192.168.1.10:443
```

Here:

- `192.168.1.10` is the IP address.
- `443` is the port number.

TCP and UDP have separate port spaces.

Therefore, TCP port 53 and UDP port 53 are different transport endpoints.

## 10.2 Port Number Categories

| Range | Category |
|---|---|
| 0–1023 | Well-known ports |
| 1024–49151 | Registered ports |
| 49152–65535 | Dynamic/private ports |

These categories are defined by IANA.

Operating systems commonly use dynamic ports for outgoing client connections.

## 10.3 What Is a Socket?

A socket is a software communication endpoint used by applications.

A network socket is commonly identified by:

- Transport protocol.
- Local IP address.
- Local port.
- Remote IP address.
- Remote port.

For an established TCP connection, the combination of these values helps distinguish individual connections.

Example:

```text
TCP
Local:  192.168.1.10:51520
Remote: 93.184.216.34:443
```

This represents a connection from a local client port to a remote HTTPS service.

## 10.4 Listening Ports vs Established Connections

**Listening socket:**

An application is waiting for incoming connections.

Example:

```text
0.0.0.0:8000
```

**Established connection:**

A connection has already been established between endpoints.

Example:

```text
192.168.1.10:51520 -> 93.184.216.34:443
```

## 10.5 How to Check Listening Ports

Use:

```bash
ss -lnt
```

Options:

- `-l`: Listening sockets.
- `-n`: Numeric addresses and ports.
- `-t`: TCP sockets.

For UDP:

```bash
ss -lnu
```

For TCP and UDP:

```bash
ss -lntu
```

Show process information:

```bash
sudo ss -lntup
```

The `-p` option attempts to show process information. `sudo` may be needed for complete process visibility.

Show established TCP connections:

```bash
ss -tn state established
```

Show all TCP connections:

```bash
ss -ant
```

## 10.6 Cybersecurity Relevance

Listening-port inspection helps identify:

- Unexpected services.
- Development servers.
- Exposed administration interfaces.
- Unnecessary network services.
- Suspicious processes listening on network interfaces.

A listening port does not automatically indicate a vulnerability.

---

# 11. DNS (Domain Name System)

## 11.1 What Is DNS?

DNS stands for Domain Name System.

It translates human-readable domain names into IP addresses and provides other types of naming information.

For example:

```text
google.com
```

May resolve to one or more IP addresses.

Without DNS, users would need to remember IP addresses instead of domain names.

## 11.2 Why Is DNS Important?

DNS is essential because users generally access websites using domain names.

It is used by:

- Web browsers.
- Email systems.
- Applications.
- Network services.
- Security monitoring systems.

## 11.3 How DNS Works

Suppose you visit:

```text
example.com
```

The simplified process is:

```text
User enters example.com
          |
          v
Browser checks available cache
          |
          v
Operating system checks local
name-resolution information
          |
          v
DNS resolver receives query
          |
          v
Resolver performs necessary lookup
          |
          v
DNS response returns IP address
          |
          v
Browser connects to the server
```

A recursive resolver may consult:

1. Root DNS servers.
2. Top-level domain (TLD) servers.
3. Authoritative DNS servers.

It may also already have a cached answer.

## 11.4 Important DNS Record Types

| Record | Purpose | Example |
|---|---|---|
| A | Maps hostname to IPv4 address | example.com → IPv4 |
| AAAA | Maps hostname to IPv6 address | example.com → IPv6 |
| CNAME | Alias to another hostname | www → example.com |
| MX | Specifies mail servers | Mail routing |
| NS | Identifies authoritative name servers | DNS delegation |
| TXT | Stores text information | SPF and verification |
| PTR | Reverse DNS lookup | IP → hostname |
| SOA | Start of Authority information | Zone administration |
| SRV | Specifies service location | Service discovery |

## 11.5 DNS Commands in Linux

### dig

`dig` is a DNS query utility.

Install if required:

```bash
sudo apt update
sudo apt install dnsutils
```

On Debian-based systems, `dnsutils` provides `dig`.

Basic lookup:

```bash
dig example.com
```

Look only for the answer:

```bash
dig example.com +short
```

Query IPv4:

```bash
dig A example.com
```

Query IPv6:

```bash
dig AAAA example.com
```

Query MX records:

```bash
dig MX example.com
```

Query NS records:

```bash
dig NS example.com
```

Query a particular DNS server:

```bash
dig @1.1.1.1 example.com
```

Explanation:

- `@1.1.1.1`: Sends the query to the specified DNS server.
- `example.com`: Domain being queried.

### host

`host` is a simple DNS lookup utility.

```bash
host example.com
```

Query a particular record:

```bash
host -t MX example.com
```

### nslookup

`nslookup` is another DNS troubleshooting tool.

```bash
nslookup example.com
```

Specify a DNS server:

```bash
nslookup example.com 1.1.1.1
```

### getent hosts

`getent` queries the operating system's configured name-service databases.

```bash
getent hosts example.com
```

It can use sources configured in `/etc/nsswitch.conf`, including local host entries and DNS.

This is useful because application name resolution may involve more than direct DNS queries.

### resolvectl

`resolvectl` is a command-line interface for systemd-resolved where that service is available.

Check DNS status:

```bash
resolvectl status
```

Query a hostname:

```bash
resolvectl query example.com
```

Not every Linux distribution or installation uses systemd-resolved.

## 11.6 Important DNS Configuration Files

### /etc/resolv.conf

This file traditionally contains DNS resolver configuration.

Inspect it:

```bash
cat /etc/resolv.conf
```

Example:

```text
nameserver 192.168.1.1
```

The listed nameserver is an address used for DNS resolution.

On some distributions, this file is automatically generated or managed by NetworkManager or systemd-resolved.

Do not overwrite it blindly.

### /etc/hosts

This file contains static hostname mappings.

Inspect it:

```bash
cat /etc/hosts
```

Example:

```text
127.0.0.1 localhost
192.168.1.20 testserver.local
```

A local hosts entry can influence name resolution without querying DNS.

## 11.7 DNS Security Relevance

DNS knowledge is important for:

- Subdomain enumeration.
- Understanding DNS misconfigurations.
- Investigating suspicious domains.
- Understanding domain takeover risks.
- Analyzing DNS traffic.
- Understanding DNS tunneling.
- Troubleshooting web application connectivity.

A DNS record alone does not prove that a web application is vulnerable.

---

# 12. DHCP (Dynamic Host Configuration Protocol)

## 12.1 What Is DHCP?

DHCP stands for Dynamic Host Configuration Protocol.

It automatically provides network configuration information to devices.

Instead of manually configuring an IP address on every device, a DHCP server can assign configuration information.

Common DHCP information includes:

- IP address.
- Subnet mask or prefix.
- Default gateway.
- DNS servers.
- Lease duration.

## 12.2 Why Is DHCP Important?

DHCP simplifies network management.

It is commonly used in:

- Home routers.
- Office networks.
- University networks.
- Enterprise networks.
- Virtual machine networks.

## 12.3 DHCP DORA Process

DHCP commonly uses a four-step process called DORA.

DORA stands for:

1. Discover
2. Offer
3. Request
4. Acknowledge

### Diagram

```text
Client                         DHCP Server
  |                                 |
  | -------- Discover ------------>|
  |                                 |
  |<--------- Offer ----------------|
  |                                 |
  | -------- Request ------------->|
  |                                 |
  |<--------- Acknowledge ----------|
  |                                 |
  |       Configuration received    |
```

### Step 1: Discover

The client broadcasts a DHCP discovery message to locate DHCP servers.

### Step 2: Offer

The DHCP server offers an IP address and configuration details.

### Step 3: Request

The client requests the offered configuration.

### Step 4: Acknowledge

The DHCP server confirms the assignment.

## 12.4 DHCP Ports

DHCP for IPv4 commonly uses UDP:

| Device | Port |
|---|---:|
| DHCP Server | 67 |
| DHCP Client | 68 |

## 12.5 DHCP Lease

A DHCP lease is the period for which a client can use an assigned IP configuration.

The client may renew its lease before it expires.

## 12.6 How to Inspect DHCP Information

Check interface information:

```bash
ip addr
```

Inspect NetworkManager connections where available:

```bash
nmcli connection show
```

Show active devices:

```bash
nmcli device status
```

Show connection details:

```bash
nmcli connection show "Wired connection 1"
```

The actual connection name depends on your system.

DHCP client commands differ between network managers and Linux distributions.

For example, `dhclient` may be available on some systems but is not guaranteed to be installed or used.

## 12.7 Cybersecurity Relevance

DHCP knowledge helps understand:

- Rogue DHCP server risks.
- DHCP spoofing concepts.
- IP address assignment.
- Network configuration attacks.
- Internal network investigations.
- DHCP-related packet analysis.

---

# 13. ARP (Address Resolution Protocol)

## 13.1 What Is ARP?

ARP stands for Address Resolution Protocol.

It is used in IPv4 local networks to discover the link-layer address associated with an IPv4 address.

For example, a computer may know:

```text
IP Address: 192.168.1.1
```

But it needs the corresponding MAC address to construct an Ethernet frame for local delivery.

ARP helps resolve this information.

## 13.2 How ARP Works

Suppose your computer wants to communicate with:

```text
192.168.1.1
```

But it does not know the MAC address.

The following process occurs:

1. The computer checks its neighbor cache.
2. If no valid entry exists, it broadcasts an ARP request.
3. The device with the matching IP responds.
4. The sender learns the corresponding MAC address.
5. The mapping is stored temporarily in the neighbor cache.

### ARP Communication

```text
Computer A                         Router
192.168.1.10                       192.168.1.1
     |                                  |
     | -------- ARP Request ---------->|
     |                                  |
     |<--------- ARP Reply -------------|
     |                                  |
     |       MAC Address Learned        |
```

ARP is used for IPv4. IPv6 uses Neighbor Discovery Protocol (NDP) instead.

## 13.3 Linux Commands for ARP Information

Modern Linux systems use the `ip neigh` command.

Show the neighbor table:

```bash
ip neigh
```

Example output:

```text
192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

Explanation:

- `192.168.1.1`: Neighbor IP address.
- `dev eth0`: Interface.
- `lladdr`: Link-layer address.
- `REACHABLE`: Neighbor entry is currently considered reachable.

Common neighbor states include:

| State | Meaning |
|---|---|
| REACHABLE | Recently confirmed reachable |
| STALE | Entry exists but has not been recently confirmed |
| DELAY | Reachability confirmation is delayed |
| PROBE | Reachability is being checked |
| INCOMPLETE | Address resolution is in progress |
| FAILED | Resolution or reachability failed |

The older `arp` utility may also be available through the `net-tools` package.

## 13.4 ARP Spoofing / ARP Poisoning

ARP has no built-in authentication mechanism.

An attacker on a local network may attempt to send forged ARP messages so that another device associates an incorrect MAC address with an IP address.

This is called ARP spoofing or ARP poisoning.

Possible consequences include:

- Man-in-the-middle attacks.
- Traffic interception.
- Traffic redirection.
- Network disruption.

### Defensive Measures

- Use network segmentation.
- Use Dynamic ARP Inspection where supported.
- Monitor unusual ARP changes.
- Use appropriate switch security controls.
- Use encrypted application protocols such as HTTPS and SSH.

## 13.5 Cybersecurity Relevance

ARP is important when:

- Investigating local network communication.
- Understanding local network attacks.
- Analyzing packet captures.
- Identifying unexpected IP-to-MAC mappings.
- Troubleshooting local network problems.

---

# 14. ICMP (Internet Control Message Protocol)

## 14.1 What Is ICMP?

ICMP stands for Internet Control Message Protocol.

It is used by network devices and operating systems to communicate error conditions and diagnostic information related to IP communication.

ICMP is not a transport protocol like TCP or UDP.

It is associated with the IP layer.

## 14.2 Common Uses of ICMP

- Network diagnostics.
- Error reporting.
- Destination unreachable messages.
- Time exceeded messages.
- Echo requests and replies.

## 14.3 Ping

`ping` is a utility that commonly uses ICMP Echo Request and Echo Reply messages to test reachability.

Command:

```bash
ping 127.0.0.1
```

Test a hostname:

```bash
ping example.com
```

Limit the number of packets:

```bash
ping -c 4 127.0.0.1
```

Important options:

| Option | Meaning |
|---|---|
| `-c` | Number of packets |
| `-i` | Interval between packets |
| `-W` | Timeout for an individual response |
| `-4` | Use IPv4 |
| `-6` | Use IPv6 |

Example:

```bash
ping -c 4 -4 1.1.1.1
```

Example output:

```text
64 bytes from 1.1.1.1: icmp_seq=1 ttl=58 time=20 ms
```

Explanation:

- `64 bytes`: Response size.
- `icmp_seq=1`: Sequence number.
- `ttl=58`: Remaining IPv4 Time To Live.
- `time=20 ms`: Round-trip time.

## 14.4 Does Ping Always Prove a Server Is Available?

No.

A server may block ICMP while allowing HTTPS traffic.

Similarly, a successful ping does not guarantee that a particular application or TCP port is working.

Therefore, ping should be combined with other diagnostic tools.

## 14.5 Cybersecurity Relevance

ICMP is relevant for:

- Host discovery.
- Network troubleshooting.
- Packet analysis.
- Understanding firewall rules.
- Investigating network errors.
- Understanding Nmap host discovery.

---

# 15. HTTP and HTTPS

## 15.1 What Is HTTP?

HTTP stands for Hypertext Transfer Protocol.

It is an application-layer protocol used for communication between clients and servers.

It is commonly used by web browsers and web applications.

Example:

```text
https://example.com
```

A browser sends an HTTP request and receives an HTTP response.

## 15.2 Client-Server Communication

```text
Browser (Client)
       |
       | HTTP Request
       v
Web Server
       |
       | HTTP Response
       v
Browser (Client)
```

### Example HTTP Request

```http
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

Explanation:

- `GET`: HTTP method.
- `/`: Requested resource path.
- `HTTP/1.1`: Protocol version.
- `Host`: Requested hostname.
- `User-Agent`: Client information.
- `Accept`: Content types the client can accept.

### Example HTTP Response

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 125

<html>
<body>
<h1>Hello World</h1>
</body>
</html>
```

Explanation:

- `HTTP/1.1`: Protocol version.
- `200`: Status code.
- `OK`: Status description.
- `Content-Type`: Response content type.
- `Content-Length`: Response body length.

## 15.3 HTTP Methods

HTTP methods describe the intended operation.

| Method | Purpose |
|---|---|
| GET | Retrieve a resource |
| POST | Submit data or request processing |
| PUT | Create or replace a resource |
| PATCH | Partially modify a resource |
| DELETE | Delete a resource |
| HEAD | Retrieve response headers without the response body |
| OPTIONS | Discover communication options |

### Example

```http
GET /users HTTP/1.1
Host: example.com
```

Requests the `/users` resource.

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{"username":"test","password":"example"}
```

Submits login data.

Never send real passwords in demonstration commands or public logs.

## 15.4 HTTP Status Codes

HTTP response status codes are divided into five categories.

| Range | Category |
|---|---|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client error |
| 5xx | Server error |

### Common Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 302 | Found |
| 304 | Not Modified |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

## 15.5 What Is HTTPS?

HTTPS stands for Hypertext Transfer Protocol Secure.

It is HTTP communication protected by TLS.

HTTPS provides:

- Encryption.
- Integrity protection.
- Server authentication through certificate validation.

Depending on the configuration, client certificates can also be used for mutual authentication.

HTTPS normally uses TCP port 443 for HTTP/1.1 and HTTP/2.

HTTP/3 uses QUIC over UDP port 443.

## 15.6 HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|---|---|---|
| Security | No TLS protection | TLS protection |
| Encryption | No built-in encryption | Encrypts application traffic |
| Integrity | No TLS integrity protection | TLS integrity protection |
| Server authentication | Not provided by HTTP | Supported through certificate validation |
| Common port | 80 | 443 |
| Security use | Unsuitable for sensitive internet traffic | Recommended for web applications |

## 15.7 Linux Commands for HTTP Testing

Use curl:

```bash
curl https://example.com
```

Display response headers:

```bash
curl -I https://example.com
```

Display verbose connection details:

```bash
curl -v https://example.com
```

Display only the HTTP status code:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

Follow redirects:

```bash
curl -L https://example.com
```

Send a GET request explicitly:

```bash
curl -X GET https://example.com
```

Send a POST request with JSON:

```bash
curl -X POST https://example.com/api \
  -H "Content-Type: application/json" \
  -d '{"name":"test"}'
```

The example endpoint is illustrative. Use an application or API you own or are authorized to test.

## 15.8 Cybersecurity Relevance

HTTP and HTTPS are fundamental to web application security.

They help you understand:

- Request and response structures.
- Authentication and authorization.
- HTTP headers.
- Cookies and sessions.
- Security headers.
- Status codes.
- API communication.
- Burp Suite interception.
- Web application vulnerabilities.

You will study these concepts in much greater detail during web application security.

---

# 16. TLS Certificates — Fundamentals

## 16.1 What Is TLS?

TLS stands for Transport Layer Security.

It is a cryptographic protocol designed to secure communication between systems.

TLS provides:

1. Confidentiality.
2. Integrity.
3. Authentication.

HTTPS uses TLS to protect HTTP communication.

## 16.2 What Is a Digital Certificate?

A digital certificate is an electronic document that binds an identity, such as a domain name, to a public key.

It is commonly issued by a Certificate Authority (CA).

A certificate contains information such as:

- Subject identity.
- Public key.
- Issuer.
- Validity period.
- Signature.
- Subject Alternative Names (SANs).
- Key usage information.

## 16.3 What Is a Certificate Authority?

A Certificate Authority is an entity trusted to issue and sign digital certificates.

Operating systems and browsers maintain trust stores containing trusted root certificates.

The certificate chain may look like this:

```text
Trusted Root CA
       |
       v
Intermediate CA
       |
       v
Website Certificate
       |
       v
example.com
```

The client validates the certificate chain according to its trust configuration.

## 16.4 How TLS Works

A simplified TLS 1.3 handshake:

```text
Client                         Server
  |                                |
  | -------- ClientHello --------> |
  |                                |
  | <------- ServerHello --------- |
  |                                |
  | <------- Certificate ----------|
  |                                |
  | <------- Finished -------------|
  |                                |
  | -------- Finished -----------> |
  |                                |
  |      Secure Communication      |
```

The actual TLS 1.3 handshake has additional cryptographic details.

Important concepts include:

- Cipher suites.
- Key exchange.
- Certificates.
- Certificate validation.
- Session keys.
- Authenticated encryption.

TLS 1.3 commonly uses ephemeral key exchange to establish shared secrets.

Application data is then protected using symmetric encryption.

## 16.5 How to Inspect a TLS Certificate

Use OpenSSL:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Explanation:

- `s_client`: OpenSSL TLS client utility.
- `-connect`: Specifies the server and port.
- `-servername`: Sends the hostname using Server Name Indication (SNI).

The output includes certificate and TLS connection details.

To inspect certificate dates and subject information:

```bash
echo | openssl s_client \
  -connect example.com:443 \
  -servername example.com 2>/dev/null |
  openssl x509 -noout -subject -issuer -dates
```

This command connects to the remote server and displays certificate information.

## 16.6 Certificate Validation

A certificate should be checked for:

- Trusted certificate chain.
- Correct hostname.
- Validity period.
- Appropriate usage.
- Acceptable cryptographic algorithms.

A certificate being present does not automatically mean the connection is secure.

## 16.7 Cybersecurity Relevance

TLS knowledge is essential for:

- HTTPS inspection.
- Certificate misconfiguration analysis.
- Understanding Burp Suite's proxy certificate.
- Identifying expired certificates.
- Understanding man-in-the-middle risks.
- Investigating TLS errors.

> Never disable certificate verification as a permanent solution to TLS problems. Identify and correct the underlying certificate or trust issue.

---

# 17. NAT (Network Address Translation)

## 17.1 What Is NAT?

NAT stands for Network Address Translation.

NAT modifies IP address information in packet headers as packets pass through a network device.

It is commonly used by routers to allow multiple private IPv4 devices to access the internet through one or more public IPv4 addresses.

## 17.2 Why Is NAT Used?

Private IPv4 addresses are not globally routed.

NAT allows internal devices to communicate with external networks using public addressing.

Example:

```text
Laptop 1: 192.168.1.10
Laptop 2: 192.168.1.11
Laptop 3: 192.168.1.12
       |
       v
     Router
       |
       | Public IP: 203.0.113.10
       |
       v
    Internet
```

The router translates the internal source addresses when forwarding traffic.

## 17.3 Types of NAT

### 1. Static NAT

A fixed one-to-one mapping between an internal address and an external address.

### 2. Dynamic NAT

Uses a pool of public addresses for translation.

### 3. PAT (Port Address Translation)

Allows multiple internal devices to share a public IP address by tracking transport-layer ports.

PAT is commonly called NAT overload or many-to-one NAT.

## 17.4 NAT Example

Suppose:

```text
Private IP: 192.168.1.10
Private Port: 51520
Public IP: 203.0.113.10
Public Port: 40001
```

A router may translate the outgoing connection as follows:

```text
192.168.1.10:51520
          |
          v
203.0.113.10:40001
          |
          v
Internet Server
```

The router maintains translation state so responses can be sent back to the correct internal device.

## 17.5 NAT vs Firewall

| NAT | Firewall |
|---|---|
| Translates network addresses | Controls network traffic |
| Modifies packet addressing | Applies traffic filtering rules |
| Commonly used for IPv4 address sharing | Used to enforce security policy |
| Does not automatically provide strong security | Can restrict unauthorized connections |

NAT may reduce direct inbound reachability, but NAT itself is not a complete security solution.

## 17.6 Cybersecurity Relevance

NAT is important for understanding:

- Internal and external IP addresses.
- Port forwarding.
- Network boundaries.
- Virtual machine networking.
- Firewall interactions.
- Remote access to internal services.

---

# 18. Firewalls

## 18.1 What Is a Firewall?

A firewall is a security mechanism that monitors and controls network traffic according to defined rules.

It can allow or block traffic based on:

- Source IP address.
- Destination IP address.
- Protocol.
- Source port.
- Destination port.
- Connection state.
- Interface.

Firewalls can be implemented in hardware, software, cloud infrastructure, or network appliances.

## 18.2 Types of Firewalls

### 1. Packet-Filtering Firewall

Examines packet information and applies filtering rules.

### 2. Stateful Firewall

Tracks connection state and uses it when deciding whether traffic should be allowed.

### 3. Application-Layer Firewall

Inspects application-layer traffic and can enforce application-specific rules.

### 4. Next-Generation Firewall

May combine traditional firewall functions with features such as intrusion prevention and application awareness.

## 18.3 Linux Firewall Technologies

Linux networking includes several firewall-related technologies.

Important components:

- Netfilter: Linux kernel networking framework.
- nftables: Modern packet filtering and rule-management interface.
- iptables: Older, widely encountered firewall interface.
- UFW: Simplified firewall management tool.
- firewalld: Firewall management service used by some distributions.

## 18.4 What Is nftables?

`nftables` is the modern Linux packet-filtering framework and userspace administration interface.

It supports:

- Packet filtering.
- Network address translation.
- Connection tracking integration.
- Stateful firewall rules.
- IPv4 and IPv6 filtering.

Check whether it is installed:

```bash
nft --version
```

Display rules:

```bash
sudo nft list ruleset
```

## 18.5 Basic nftables Concepts

The main concepts include:

### Table

A table is a container for chains.

### Chain

A chain contains rules that process packets at particular hooks.

### Rule

A rule specifies conditions and an action.

### Hook

A hook determines where a chain processes packets in the network stack.

Common hooks include:

- input
- output
- forward
- prerouting
- postrouting

## 18.6 Create a Basic nftables Firewall in a Lab

> WARNING: Firewall configuration can interrupt your network connection. Use a local VM console, take a VM snapshot, and understand the existing firewall rules before modifying them.

First inspect the current ruleset:

```bash
sudo nft list ruleset
```

Create a new example table:

```bash
sudo nft add table inet labfilter
```

Create an input chain:

```bash
sudo nft 'add chain inet labfilter input { type filter hook input priority 0; policy accept; }'
```

Add a rule allowing loopback traffic:

```bash
sudo nft add rule inet labfilter input iifname "lo" accept
```

Add a rule allowing established and related traffic:

```bash
sudo nft add rule inet labfilter input ct state established,related accept
```

This is an illustrative lab ruleset, not a complete production firewall.

It still has an ACCEPT default policy and therefore does not provide restrictive inbound filtering.

Remove the lab table:

```bash
sudo nft delete table inet labfilter
```

Verify:

```bash
sudo nft list ruleset
```

## 18.7 What Is UFW?

UFW stands for Uncomplicated Firewall.

It provides a simpler command-line interface for managing firewall rules.

It is commonly available on Ubuntu and can be installed on Debian-based distributions, including Kali.

Install if required:

```bash
sudo apt update
sudo apt install ufw
```

Check status:

```bash
sudo ufw status
```

Enable UFW:

```bash
sudo ufw enable
```

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTP:

```bash
sudo ufw allow 80/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

Block a port:

```bash
sudo ufw deny 23/tcp
```

Delete a rule:

```bash
sudo ufw delete deny 23/tcp
```

Disable UFW:

```bash
sudo ufw disable
```

> Before enabling a firewall on a remote system, make sure the required management port is allowed. Otherwise, you may lose remote access.

## 18.8 Cybersecurity Relevance

Firewalls are important for:

- Restricting exposed services.
- Reducing attack surface.
- Blocking unauthorized access.
- Enforcing network segmentation.
- Protecting servers.
- Understanding why network scans report filtered ports.

---

# 19. Proxies

## 19.1 What Is a Proxy Server?

A proxy server acts as an intermediary between a client and another server.

Instead of communicating directly with the destination, the client sends its request through the proxy.

### Basic Architecture

```text
Client
  |
  v
Proxy Server
  |
  v
Destination Server
```

## 19.2 Types of Proxies

### 1. Forward Proxy

A forward proxy acts on behalf of clients.

Example:

```text
Client -> Forward Proxy -> Website
```

It is commonly used for:

- Web access control.
- Traffic filtering.
- Privacy.
- Network monitoring.
- Caching.

### 2. Reverse Proxy

A reverse proxy acts on behalf of backend servers.

Example:

```text
Internet Client
       |
       v
Reverse Proxy
       |
       v
Backend Server
```

Common reverse proxy software includes:

- Nginx.
- HAProxy.
- Apache HTTP Server.

Reverse proxies can provide:

- Load balancing.
- TLS termination.
- Caching.
- Request routing.
- Access control.

### 3. Transparent Proxy

A transparent proxy intercepts or processes traffic without requiring the client to explicitly configure a conventional proxy setting.

The exact behavior depends on the network architecture.

### 4. Intercepting Proxy

An intercepting proxy captures application traffic for inspection or modification.

## 19.3 What Is Burp Suite?

Burp Suite is a web application security testing platform.

Its proxy component allows security testers to intercept HTTP and HTTPS traffic between a browser and a web application.

### Burp Proxy Architecture

```text
Browser
   |
   | HTTP/HTTPS Request
   v
Burp Suite Proxy
   |
   | Forwarded Request
   v
Web Application
   |
   | Response
   v
Burp Suite Proxy
   |
   v
Browser
```

It allows testers to inspect and modify requests and responses in authorized testing environments.

## 19.4 Proxy vs VPN

| Proxy | VPN |
|---|---|
| Acts as an intermediary | Creates a protected network tunnel |
| Often works at application level | Usually operates at network layer or below |
| May handle only selected application traffic | Can route broader device traffic |
| Encryption depends on protocol and configuration | Tunnel traffic is encrypted according to VPN configuration |
| Does not necessarily protect all device traffic | Can protect configured routed traffic |

A proxy is not automatically encrypted, anonymous, or secure.

## 19.5 Cybersecurity Relevance

Proxy knowledge is essential for:

- Understanding Burp Suite.
- Intercepting HTTP requests.
- Testing authentication flows.
- Inspecting API communication.
- Understanding reverse proxy configurations.
- Identifying proxy-related security issues.

---

# 20. VPNs — Fundamentals

## 20.1 What Is a VPN?

VPN stands for Virtual Private Network.

A VPN creates a logical private communication path over an existing network.

It commonly uses encryption and authentication to protect traffic between endpoints.

### Basic VPN Architecture

```text
Your Computer
      |
      | Encrypted VPN Tunnel
      |
      v
VPN Server
      |
      v
Destination Network
```

## 20.2 Why Are VPNs Used?

VPNs are used for:

- Secure remote access.
- Connecting office networks.
- Protecting traffic over untrusted networks.
- Accessing private network resources.
- Connecting geographically separated networks.

## 20.3 Types of VPNs

### 1. Remote-Access VPN

Connects an individual device to a private network.

### 2. Site-to-Site VPN

Connects two or more networks through a VPN tunnel.

### 3. Client-to-Site VPN

A client connects to an organization's network through a VPN gateway.

## 20.4 Common VPN Technologies

| Technology | Description |
|---|---|
| WireGuard | Modern VPN protocol |
| OpenVPN | VPN solution using TLS-based security |
| IPsec | Suite of protocols for IP-layer security |
| IKEv2 | Key exchange protocol commonly used with IPsec |

## 20.5 VPN and Routing

When a VPN is connected, the system may install additional network interfaces and routes.

Inspect interfaces:

```bash
ip addr
```

Inspect routes:

```bash
ip route
```

You may see an interface such as:

```text
tun0
```

or:

```text
wg0
```

These are common interface names for tunnel-based VPN configurations.

The exact interface depends on the VPN implementation.

## 20.6 VPN Security Limitations

A VPN does not automatically make a user anonymous.

A VPN provider may still be able to observe some metadata or traffic information, depending on the configuration and encryption.

A VPN also does not protect an application from vulnerabilities.

## 20.7 Cybersecurity Relevance

VPN knowledge helps understand:

- Remote lab access.
- Private testing environments.
- Network tunneling.
- Routing behavior.
- Encrypted network communication.
- VPN-related DNS leaks and routing issues.

---

# 21. Client-Server Architecture

## 21.1 What Is Client-Server Architecture?

Client-server architecture is a communication model in which one system requests services and another system provides them.

The client initiates a request.

The server processes the request and returns a response.

## 21.2 Example

When you open a website:

1. Your browser acts as the client.
2. The browser resolves the website's domain name.
3. It establishes a network connection.
4. It sends an HTTP request.
5. The web server processes the request.
6. The server sends an HTTP response.
7. The browser renders the webpage.

### Diagram

```text
+------------------+
|      Client      |
|                  |
|  Web Browser     |
+------------------+
         |
         | HTTP Request
         v
+------------------+
|      Server      |
|                  |
|  Web Application |
+------------------+
         |
         | Database Query
         v
+------------------+
|     Database     |
+------------------+
```

## 21.3 Types of Servers

| Server | Purpose |
|---|---|
| Web Server | Serves web content |
| DNS Server | Resolves domain names |
| DHCP Server | Assigns network configuration |
| Mail Server | Handles email communication |
| Database Server | Stores and retrieves data |
| File Server | Provides file storage and access |
| Proxy Server | Forwards client requests |

## 21.4 Important Concepts

### Client

Requests a service.

### Server

Provides a service.

### Request

A message sent by the client.

### Response

A message returned by the server.

### Service

A function or resource made available by a server.

### API

An Application Programming Interface allows software components to communicate using defined interfaces.

## 21.5 Cybersecurity Relevance

Client-server architecture is essential to understanding:

- Web application architecture.
- Authentication.
- Authorization.
- API security.
- Database communication.
- Session management.
- Request manipulation.
- Server-side vulnerabilities.

---

# 22. OSI and TCP/IP Models

## 22.1 What Is the OSI Model?

OSI stands for Open Systems Interconnection.

It is a conceptual reference model used to understand network communication.

It divides network communication into seven layers.

The model helps engineers understand where different protocols and networking functions operate.

## 22.2 Seven Layers of the OSI Model

| Layer | Name | Main Responsibility | Examples |
|---|---|---|---|
| 7 | Application | Network services for applications | HTTP, DNS, SMTP |
| 6 | Presentation | Data representation, encoding, encryption concepts | TLS concepts, encoding |
| 5 | Session | Session establishment and management concepts | Session control |
| 4 | Transport | End-to-end transport | TCP, UDP |
| 3 | Network | Logical addressing and routing | IPv4, IPv6, ICMP |
| 2 | Data Link | Local frame delivery | Ethernet, MAC, ARP-related operations |
| 1 | Physical | Transmission of raw bits | Cables, radio signals |

The OSI model is conceptual. Real-world protocols do not always map perfectly to one layer.

## 22.3 Explanation of Each Layer

### Layer 7: Application Layer

Provides network services to applications.

Examples:

- HTTP.
- HTTPS.
- DNS.
- SMTP.
- FTP.

Cybersecurity relevance:

- Web application testing.
- HTTP request analysis.
- DNS security.
- API security.

### Layer 6: Presentation Layer

Deals with data representation and transformation concepts.

Examples:

- Data encoding.
- Character encoding.
- Serialization.
- Encryption-related representation.

### Layer 5: Session Layer

Deals with managing communication sessions between applications.

Examples of session-related functions include:

- Session establishment.
- Session management.
- Session termination.

### Layer 4: Transport Layer

Provides communication between application endpoints.

Protocols:

- TCP.
- UDP.

Important concepts:

- Ports.
- Segmentation.
- Reliability.
- Flow control.

### Layer 3: Network Layer

Handles logical addressing and routing.

Protocols:

- IPv4.
- IPv6.
- ICMP.

Important concepts:

- IP addressing.
- Routing.
- Subnetting.
- Packet forwarding.

### Layer 2: Data Link Layer

Handles communication over a local network link.

Important concepts:

- MAC addresses.
- Ethernet frames.
- Switching.
- Link-layer addressing.

### Layer 1: Physical Layer

Handles the physical transmission of bits.

Examples:

- Ethernet cables.
- Fiber optics.
- Radio signals.
- Wireless transmission.

## 22.4 What Is the TCP/IP Model?

The TCP/IP model is a practical networking model based on the protocols used in internet communication.

It is commonly represented using four layers.

| TCP/IP Layer | Responsibility | Examples |
|---|---|---|
| Application | Application communication | HTTP, DNS, SMTP |
| Transport | Process-to-process communication | TCP, UDP |
| Internet | Logical addressing and routing | IPv4, IPv6, ICMP |
| Network Access | Local network transmission | Ethernet, Wi-Fi |

Some textbooks use a five-layer model by separating the physical layer from the network access layer.

## 22.5 OSI vs TCP/IP Model

| OSI Model | TCP/IP Model |
|---|---|
| 7 layers | Commonly 4 layers |
| Conceptual reference model | Practical protocol architecture |
| Developed by ISO | Developed around DARPA/Internet protocol work |
| Separates session and presentation | Includes them in application |
| Separates physical and data link | Combines them in network access in the four-layer model |

## 22.6 Data Encapsulation

When an application sends data, information is encapsulated as it moves through the networking stack.

Example:

```text
Application Data
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
Physical Transmission
```

At the receiving system, the process is reversed. This is called decapsulation.

### Important Data Units

| Layer | Data Unit |
|---|---|
| Application | Data / Message |
| Transport | TCP Segment / UDP Datagram |
| Network | IP Packet |
| Data Link | Frame |
| Physical | Bits |

## 22.7 Cybersecurity Relevance

The OSI and TCP/IP models help you:

- Understand where protocols operate.
- Troubleshoot network communication.
- Interpret packet captures.
- Understand network attacks.
- Identify the layer where a problem occurs.
- Understand Nmap and Wireshark output.

---

# PART 2: LINUX NETWORKING COMMANDS

# 23. The `ip addr` Command

## 23.1 What Is `ip addr`?

The `ip addr` command displays and manages IP addresses assigned to network interfaces.

It is part of the modern Linux `iproute2` utility suite.

Syntax:

```bash
ip addr [COMMAND] [OPTIONS]
```

## 23.2 Display All IP Addresses

```bash
ip addr
```

Short form:

```bash
ip a
```

Displays:

- Interface names.
- Interface state.
- IPv4 addresses.
- IPv6 addresses.
- Prefix lengths.
- Interface properties.

## 23.3 Display IPv4 Addresses Only

```bash
ip -4 addr
```

## 23.4 Display IPv6 Addresses Only

```bash
ip -6 addr
```

## 23.5 Display a Specific Interface

```bash
ip addr show eth0
```

Replace `eth0` with your interface name.

## 23.6 Add an IP Address

Example:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

This adds an IPv4 address to the specified interface.

This is a temporary runtime change.

## 23.7 Remove an IP Address

```bash
sudo ip addr del 192.168.1.100/24 dev eth0
```

Only remove an address that you intentionally added.

## 23.8 Practical Exercise

```bash
ip addr
ip -4 addr
ip -6 addr
```

Record:

- Interface name.
- IPv4 address.
- IPv6 address.
- Prefix length.
- Interface state.

---

# 24. The `ip link` Command

## 24.1 What Is `ip link`?

The `ip link` command displays and manages network interfaces at the link layer.

It is used to inspect interface status and configure certain link properties.

## 24.2 Show Interfaces

```bash
ip link
```

Example:

```text
1: lo: <LOOPBACK,UP,LOWER_UP>
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

Explanation:

- `lo`: Loopback interface.
- `eth0`: Example Ethernet interface.
- `UP`: Administratively enabled.
- `LOWER_UP`: Lower-layer connectivity is available.

## 24.3 Enable an Interface

```bash
sudo ip link set eth0 up
```

## 24.4 Disable an Interface

```bash
sudo ip link set eth0 down
```

Disabling an interface will interrupt its network connectivity.

## 24.5 Display Interface Details

```bash
ip -details link show eth0
```

## 24.6 Practical Exercise

```bash
ip link
```

Identify:

- Your loopback interface.
- Your primary network interface.
- Your interface MAC address.
- Whether each interface is UP or DOWN.

---

# 25. The `ip route` Command

## 25.1 What Is `ip route`?

It displays and manages the IP routing table.

## 25.2 Show Routes

```bash
ip route
```

## 25.3 Show IPv4 Routes

```bash
ip -4 route
```

## 25.4 Show IPv6 Routes

```bash
ip -6 route
```

## 25.5 Check the Route to a Destination

```bash
ip route get 8.8.8.8
```

## 25.6 Show All Routing Tables

```bash
ip route show table all
```

## 25.7 Practical Exercise

Run:

```bash
ip route
```

Identify:

- Default route.
- Gateway.
- Network interface.
- Local subnet.

---

# 26. The `ip neigh` Command

## 26.1 What Is `ip neigh`?

The `ip neigh` command displays and manages the Linux neighbor table.

For IPv4, this includes ARP-related mappings.

For IPv6, it includes Neighbor Discovery information.

## 26.2 Display Neighbor Table

```bash
ip neigh
```

## 26.3 Show Neighbors on a Specific Interface

```bash
ip neigh show dev eth0
```

## 26.4 Display IPv4 Neighbors

```bash
ip -4 neigh
```

## 26.5 Display IPv6 Neighbors

```bash
ip -6 neigh
```

## 26.6 Practical Exercise

```bash
ping -c 1 192.168.1.1
ip neigh
```

Replace the address with your actual gateway.

Observe whether a neighbor entry appears.

---

# 27. The `ping` Command

## 27.1 What Is Ping?

`ping` is a network diagnostic utility that commonly uses ICMP Echo Request and Echo Reply messages.

It helps test basic reachability and measure round-trip time.

## 27.2 Basic Syntax

```bash
ping [OPTIONS] destination
```

## 27.3 Test Loopback

```bash
ping 127.0.0.1
```

## 27.4 Limit Packet Count

```bash
ping -c 4 127.0.0.1
```

## 27.5 Test a Public IP

```bash
ping -c 4 1.1.1.1
```

## 27.6 Test DNS and Connectivity Together

```bash
ping -c 4 example.com
```

This requires successful name resolution unless the address is already available through a relevant cache or local configuration.

## 27.7 Important Options

| Option | Purpose |
|---|---|
| `-c` | Set packet count |
| `-i` | Set packet interval |
| `-W` | Set response timeout |
| `-4` | Use IPv4 |
| `-6` | Use IPv6 |

## 27.8 Understanding Packet Loss

Example:

```text
4 packets transmitted, 4 received, 0% packet loss
```

This indicates that all four packets received replies.

If packets are lost, possible causes include:

- Network congestion.
- Packet filtering.
- Routing problems.
- Destination unavailability.
- Wireless interference.

---

# 28. `traceroute` and `tracepath`

## 28.1 What Is Traceroute?

Traceroute is a network diagnostic tool used to identify intermediate network hops between a source and destination.

It works by manipulating the TTL field in IPv4 packets or Hop Limit in IPv6 packets.

Intermediate routers may return ICMP Time Exceeded messages when the value expires.

## 28.2 Install Traceroute

```bash
sudo apt update
sudo apt install traceroute
```

## 28.3 Basic Command

```bash
traceroute example.com
```

Use IPv4:

```bash
traceroute -4 example.com
```

Use IPv6:

```bash
traceroute -6 example.com
```

## 28.4 What Is tracepath?

`tracepath` is another Linux utility for discovering network paths.

Example:

```bash
tracepath example.com
```

It is available through the `iputils-tracepath` package on many Debian-based systems.

## 28.5 Understanding Output

Example:

```text
1  192.168.1.1
2  10.10.0.1
3  203.0.113.1
```

Each numbered line represents a hop.

A `* * *` result means that no response was received for the corresponding probe within the timeout.

It does not necessarily mean the router is down.

## 28.6 Cybersecurity Relevance

Traceroute helps:

- Understand network paths.
- Diagnose routing issues.
- Identify where communication stops.
- Investigate latency.
- Understand network topology at a basic level.

---

# 29. The `ss` Command

## 29.1 What Is ss?

`ss` stands for socket statistics.

It is a Linux utility used to display socket information.

It is commonly used instead of the older `netstat` command.

## 29.2 Display All TCP Connections

```bash
ss -at
```

## 29.3 Display Listening TCP Sockets

```bash
ss -lt
```

## 29.4 Display Listening UDP Sockets

```bash
ss -lu
```

## 29.5 Display Listening TCP and UDP Sockets

```bash
ss -lntu
```

## 29.6 Show Process Information

```bash
sudo ss -lntup
```

## 29.7 Show Established TCP Connections

```bash
ss -tn state established
```

## 29.8 Important Options

| Option | Meaning |
|---|---|
| `-a` | All sockets |
| `-l` | Listening sockets |
| `-t` | TCP |
| `-u` | UDP |
| `-n` | Numeric addresses and ports |
| `-p` | Process information |
| `-e` | Extended information |
| `-r` | Resolve names where applicable |

## 29.9 Practical Exercise: Check a Local Listening Port

Start a test server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open another terminal:

```bash
ss -lnt
```

Look for port `8000`.

Stop the server:

```text
Ctrl + C
```

Run the command again.

Observe that the listening socket is no longer present.

---

# 30. The `curl` Command

## 30.1 What Is curl?

`curl` is a command-line tool for transferring data using URLs.

It supports multiple protocols, including:

- HTTP.
- HTTPS.
- FTP.
- SFTP.
- SMTP.
- Other supported protocols.

It is especially useful for testing web servers and APIs.

## 30.2 Basic Syntax

```bash
curl [OPTIONS] URL
```

## 30.3 Request a Webpage

```bash
curl https://example.com
```

## 30.4 Display Only Headers

```bash
curl -I https://example.com
```

## 30.5 Display Verbose Information

```bash
curl -v https://example.com
```

This displays connection and protocol details, including TLS information when applicable.

## 30.6 Follow Redirects

```bash
curl -L https://example.com
```

## 30.7 Display HTTP Status Code

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

## 30.8 Send a POST Request

```bash
curl -X POST https://example.com/api \
  -H "Content-Type: application/json" \
  -d '{"username":"test"}'
```

Use an authorized test API.

## 30.9 Important Options

| Option | Meaning |
|---|---|
| `-I` | Fetch headers only using HEAD |
| `-v` | Verbose output |
| `-L` | Follow redirects |
| `-X` | Specify request method |
| `-H` | Add a request header |
| `-d` | Send request data |
| `-o` | Save output to a file |
| `-O` | Save using remote filename |
| `-s` | Silent mode |
| `-k` | Disable TLS certificate verification |

**Security warning:** Avoid `-k` unless you are deliberately testing a certificate problem in a controlled environment. It disables certificate verification.

---

# 31. The `wget` Command

## 31.1 What Is wget?

`wget` is a command-line utility used to download files from network locations.

It supports HTTP, HTTPS, and FTP.

## 31.2 Download a File

```bash
wget https://example.com/file.txt
```

## 31.3 Save Using a Different Filename

```bash
wget -O downloaded.txt https://example.com/file.txt
```

## 31.4 Continue an Interrupted Download

```bash
wget -c https://example.com/file.zip
```

## 31.5 Download in the Background

```bash
wget -b https://example.com/file.zip
```

## 31.6 Important Options

| Option | Purpose |
|---|---|
| `-O` | Specify output filename |
| `-c` | Continue a partial download |
| `-b` | Background download |
| `-q` | Quiet mode |
| `-P` | Specify download directory |
| `--limit-rate` | Limit download speed |

## 31.7 curl vs wget

| Feature | curl | wget |
|---|---|---|
| Main purpose | Data transfer | File downloading |
| HTTP requests | Excellent support | Supported |
| API testing | Commonly used | Possible |
| File downloads | Supported | Main use |
| Recursive website download | Not its main purpose | Supported |
| Request customization | Extensive | Available |

---

# 32. The `dig` Command

## 32.1 Purpose

`dig` is used to query DNS servers and inspect DNS records.

## 32.2 Basic Commands

```bash
dig example.com
```

Short output:

```bash
dig +short example.com
```

Query A record:

```bash
dig A example.com
```

Query AAAA record:

```bash
dig AAAA example.com
```

Query MX record:

```bash
dig MX example.com
```

Query TXT record:

```bash
dig TXT example.com
```

Query a specific DNS server:

```bash
dig @1.1.1.1 example.com
```

## 32.3 Understanding DNS Output

Important sections:

- HEADER: Query information and response status.
- QUESTION SECTION: The question asked.
- ANSWER SECTION: Returned DNS records.
- AUTHORITY SECTION: Authority information.
- ADDITIONAL SECTION: Additional records.

A response status of `NOERROR` means the DNS query completed without a DNS-level error. It does not necessarily mean an answer record exists.

---

# 33. The `host` Command

## 33.1 Purpose

`host` is a simple DNS lookup utility.

## 33.2 Basic Lookup

```bash
host example.com
```

## 33.3 Query MX Records

```bash
host -t MX example.com
```

## 33.4 Query NS Records

```bash
host -t NS example.com
```

## 33.5 Reverse Lookup

```bash
host 8.8.8.8
```

Reverse DNS results are not guaranteed to exist.

---

# 34. The `nslookup` Command

## 34.1 Purpose

`nslookup` is used to query DNS servers.

## 34.2 Basic Lookup

```bash
nslookup example.com
```

## 34.3 Specify DNS Server

```bash
nslookup example.com 1.1.1.1
```

## 34.4 Query a Record Type

```bash
nslookup -type=MX example.com
```

## 34.5 Practical Exercise

Run:

```bash
dig example.com
host example.com
nslookup example.com
getent hosts example.com
```

Compare their outputs.

Remember that these tools may use different resolution paths and configuration sources.

---

# 35. The `getent hosts` Command

## 35.1 What Is getent?

`getent` retrieves entries from system-configured databases.

The `hosts` database contains hostname and address information.

## 35.2 Basic Syntax

```bash
getent hosts hostname
```

Example:

```bash
getent hosts example.com
```

## 35.3 Inspect Name Service Configuration

```bash
cat /etc/nsswitch.conf
```

Look for:

```text
hosts:
```

This entry determines the configured lookup sources and their order.

Common sources include:

- `files`
- `dns`
- `myhostname`

The exact configuration varies.

## 35.4 Why Is getent Useful?

Applications often use the system's name-resolution interfaces rather than making direct DNS queries.

Therefore, `getent hosts` helps test the name-resolution path that many applications use.

---

# 36. The `resolvectl` Command

## 36.1 Purpose

`resolvectl` communicates with systemd-resolved.

It is available on systems using systemd-resolved.

## 36.2 Display DNS Status

```bash
resolvectl status
```

## 36.3 Query a Domain

```bash
resolvectl query example.com
```

## 36.4 Flush DNS Cache

```bash
sudo resolvectl flush-caches
```

This command only applies when systemd-resolved is available and managing the relevant DNS cache.

## 36.5 Important Note

Not all Linux distributions use systemd-resolved.

If the command is unavailable, inspect:

```bash
cat /etc/resolv.conf
```

Also check the active network manager.

---

# 37. Netcat (`nc`)

## 37.1 What Is Netcat?

Netcat, commonly called `nc`, is a command-line networking utility used to establish TCP or UDP connections and transfer data.

It is sometimes called the networking Swiss Army knife.

It is useful for:

- Testing connectivity.
- Testing ports.
- Creating temporary listeners.
- Sending and receiving data.
- Basic network troubleshooting.

## 37.2 Check Whether a Port Is Open

```bash
nc -vz example.com 443
```

Explanation:

- `-v`: Verbose.
- `-z`: Scan mode without sending application data.
- `443`: Destination port.

A successful connection indicates that the TCP connection could be established at that time.

It does not prove the application is functioning correctly.

## 37.3 Create a Local TCP Listener

Terminal 1:

```bash
nc -l 127.0.0.1 9000
```

Terminal 2:

```bash
nc 127.0.0.1 9000
```

Type a message in either terminal.

You should see the message on the other terminal.

Exact options may differ between OpenBSD netcat and traditional netcat implementations.

Check:

```bash
nc -h
```

## 37.4 Test a Local HTTP Server

Start a Python server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Then:

```bash
nc -vz 127.0.0.1 8000
```

## 37.5 Security Relevance

Netcat helps understand:

- TCP connections.
- Listening services.
- Client-server communication.
- Port reachability.
- Basic socket communication.

Use listeners only in your own machine or authorized lab.

---

# 38. tcpdump

## 38.1 What Is tcpdump?

`tcpdump` is a command-line packet analyzer.

It captures and displays network packets observed on a selected interface.

It is widely used for network troubleshooting and security investigation.

## 38.2 Install tcpdump

```bash
sudo apt update
sudo apt install tcpdump
```

## 38.3 Identify Network Interfaces

```bash
ip link
```

## 38.4 Capture Packets on an Interface

```bash
sudo tcpdump -i eth0
```

Replace `eth0` with your actual interface.

## 38.5 Capture a Limited Number of Packets

```bash
sudo tcpdump -i eth0 -c 10
```

## 38.6 Capture ICMP Traffic

```bash
sudo tcpdump -i eth0 icmp
```

## 38.7 Capture DNS Traffic

```bash
sudo tcpdump -i eth0 port 53
```

## 38.8 Capture HTTP Traffic

```bash
sudo tcpdump -i eth0 tcp port 80
```

## 38.9 Capture HTTPS Traffic

```bash
sudo tcpdump -i eth0 tcp port 443
```

For HTTP/3 or QUIC traffic, UDP port 443 may also be relevant:

```bash
sudo tcpdump -i eth0 udp port 443
```

## 38.10 Save Captured Packets

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Stop the capture with:

```text
Ctrl + C
```

Read a saved capture:

```bash
tcpdump -r capture.pcap
```

## 38.11 Display Numeric Addresses

```bash
sudo tcpdump -nn -i eth0
```

The `-nn` option disables address and port name resolution.

This is useful for clearer troubleshooting.

## 38.12 Important Options

| Option | Purpose |
|---|---|
| `-i` | Select interface |
| `-c` | Limit packet count |
| `-w` | Write capture to file |
| `-r` | Read capture file |
| `-n` | Disable address resolution |
| `-nn` | Disable address and port resolution |
| `-v` | Verbose output |
| `-A` | Display packet contents as ASCII |
| `-X` | Display packet contents in hexadecimal and ASCII |
| `-s` | Set snapshot length |

## 38.13 Practical Exercise: Capture Localhost Traffic

Open terminal 1:

```bash
sudo tcpdump -i lo -nn tcp port 8000
```

Open terminal 2:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open terminal 3:

```bash
curl http://127.0.0.1:8000
```

Observe the packets in terminal 1.

Stop the capture using `Ctrl + C`.

Stop the Python server too.

### Security Relevance

tcpdump is useful for:

- Network traffic analysis.
- DNS troubleshooting.
- HTTP troubleshooting.
- Investigating unexpected connections.
- Understanding TCP handshakes.
- Capturing traffic for Wireshark analysis.

> Capture only traffic you are authorized to inspect. Packet captures may contain sensitive information.

---

# 39. nftables Fundamentals

## 39.1 Basic Concepts

nftables is the modern Linux packet-filtering system.

Its important concepts are:

- Tables.
- Chains.
- Rules.
- Sets.
- Maps.
- Hooks.
- Verdicts.

## 39.2 Check Version

```bash
nft --version
```

## 39.3 Display Existing Rules

```bash
sudo nft list ruleset
```

## 39.4 List Tables

```bash
sudo nft list tables
```

## 39.5 Display a Specific Table

```bash
sudo nft list table inet labfilter
```

## 39.6 Common Verdicts

| Verdict | Meaning |
|---|---|
| accept | Accept the packet |
| drop | Silently discard the packet |
| reject | Discard and send a rejection response where appropriate |
| jump | Continue processing in another chain |
| return | Return from a chain |

## 39.7 Example Rule

```bash
sudo nft add rule inet labfilter input ip protocol icmp accept
```

This adds a rule accepting IPv4 ICMP packets in the specified input chain.

The table and chain must already exist.

## 39.8 Cybersecurity Relevance

Understanding nftables helps you:

- Inspect Linux firewall rules.
- Understand packet filtering.
- Secure Linux servers.
- Investigate blocked traffic.
- Understand network access controls.

---

# 40. UFW Fundamentals

## 40.1 Basic Commands

Check status:

```bash
sudo ufw status
```

Detailed status:

```bash
sudo ufw status verbose
```

Enable:

```bash
sudo ufw enable
```

Disable:

```bash
sudo ufw disable
```

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTP:

```bash
sudo ufw allow 80/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

Deny a port:

```bash
sudo ufw deny 23/tcp
```

Show numbered rules:

```bash
sudo ufw status numbered
```

Delete a rule by number:

```bash
sudo ufw delete 1
```

Check UFW documentation and current rules before deleting anything.

## 40.2 Important Security Principle

Only expose the services that are necessary.

For example:

A web server may require:

- TCP 80.
- TCP 443.

An SSH management service may require:

- TCP 22.

Other ports should not be opened without a legitimate requirement.

The actual requirements depend on the server architecture.

---

# PART 3: LINUX NETWORK TROUBLESHOOTING

# 41. Understanding Network Troubleshooting

## 41.1 What Is Network Troubleshooting?

Network troubleshooting is the process of identifying and resolving problems that prevent network communication.

Common problems include:

- Incorrect IP configuration.
- Missing default gateway.
- DNS resolution failure.
- Firewall restrictions.
- Application errors.
- Routing problems.
- Unavailable services.
- Physical or wireless connectivity problems.

## 41.2 A Systematic Troubleshooting Approach

Use the following general sequence:

```text
1. Check Network Interface
          |
          v
2. Check IP Configuration
          |
          v
3. Check Routing Table
          |
          v
4. Check Gateway Reachability
          |
          v
5. Check External IP Connectivity
          |
          v
6. Check DNS Resolution
          |
          v
7. Check Destination Port
          |
          v
8. Check Application Response
```

Do not assume every network problem is a DNS problem.

---

# 42. Diagnose a Failed DNS Lookup

## 42.1 What Is a DNS Failure?

A DNS failure occurs when a hostname cannot be successfully resolved through the configured name-resolution process.

Example:

```bash
curl https://example.com
```

Possible error:

```text
Could not resolve host: example.com
```

This indicates a name-resolution problem.

## 42.2 Step-by-Step Diagnosis

### Step 1: Check Local Host Resolution

```bash
getent hosts example.com
```

If no result appears, investigate name resolution.

### Step 2: Query DNS Directly

```bash
dig example.com
```

### Step 3: Test an Alternative Resolver

```bash
dig @1.1.1.1 example.com
```

If the alternative resolver works but the configured resolver does not, the problem may be associated with your configured DNS resolver or its path.

### Step 4: Inspect Resolver Configuration

```bash
cat /etc/resolv.conf
```

### Step 5: Check systemd-resolved

```bash
resolvectl status
```

Use only when available.

### Step 6: Test IP Connectivity

```bash
ping -c 4 1.1.1.1
```

If IP connectivity works but DNS resolution fails, DNS becomes a stronger suspect.

However, ICMP filtering and DNS-specific routing policies must also be considered.

## 42.3 Common DNS Problems

| Problem | Possible Cause |
|---|---|
| Domain does not resolve | DNS server unavailable |
| NXDOMAIN | Domain name does not exist in DNS |
| Timeout | DNS server unreachable or not responding |
| SERVFAIL | DNS server failed to process query |
| Wrong IP address | Incorrect DNS data or cache |
| Local applications fail | NSS or local resolver configuration problem |

---

# 43. Check Whether a Local Port Is Listening

## 43.1 What Is a Listening Port?

A listening port is a transport endpoint waiting for incoming connections.

For example, a local web server may listen on TCP port 8000.

## 43.2 Start a Test Server

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

## 43.3 Inspect the Listening Port

```bash
ss -lnt
```

Expected output will include something similar to:

```text
LISTEN 0 5 127.0.0.1:8000
```

The exact output varies.

## 43.4 Test the Port

```bash
nc -vz 127.0.0.1 8000
```

## 43.5 Test the Application

```bash
curl http://127.0.0.1:8000
```

## 43.6 Stop the Server

```text
Ctrl + C
```

Repeat:

```bash
ss -lnt
```

The port should no longer appear as a listening socket.

---

# 44. Inspect Active Network Connections

## 44.1 Why Inspect Network Connections?

Inspecting connections helps you understand which processes are communicating with other systems.

It is useful for:

- System monitoring.
- Security investigation.
- Troubleshooting.
- Identifying unexpected network activity.

## 44.2 Display All TCP Connections

```bash
ss -ant
```

## 44.3 Display Established Connections

```bash
ss -tn state established
```

## 44.4 Display UDP Sockets

```bash
ss -anu
```

## 44.5 Show Process Information

```bash
sudo ss -tupn
```

## 44.6 Inspect Processes

```bash
ps aux
```

Search for a particular process:

```bash
ps aux | grep python
```

Be aware that `grep` may also match its own search command.

For more reliable process identification, use:

```bash
pgrep -a python
```

---

# 45. Inspect Routing and IP Configuration

Use the following commands together:

```bash
ip addr
ip link
ip route
ip neigh
```

### What Each Command Shows

| Command | Information |
|---|---|
| `ip addr` | IP addresses |
| `ip link` | Interface and link information |
| `ip route` | Routing table |
| `ip neigh` | Neighbor table |

### Practical Exercise

Create a small network configuration report.

Record:

1. Primary interface.
2. Interface state.
3. IPv4 address.
4. IPv6 address.
5. MAC address.
6. Default gateway.
7. DNS configuration.
8. Neighbor entries.

---

# 46. Use curl to Inspect an HTTP Response

## 46.1 Basic Request

```bash
curl -i https://example.com
```

The `-i` option includes response headers in the output.

## 46.2 Headers Only

```bash
curl -I https://example.com
```

## 46.3 Verbose Mode

```bash
curl -v https://example.com
```

## 46.4 Inspect Response Status

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

## 46.5 What Should You Observe?

- HTTP status code.
- Response headers.
- Content type.
- Server response behavior.
- Redirects.
- TLS connection information when using verbose output.

---

# 47. Capture Traffic from Your Own Lab Interface

## 47.1 Objective

Capture network traffic generated by a local test web server.

## 47.2 Start a Local Web Server

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

## 47.3 Start Packet Capture

In another terminal:

```bash
sudo tcpdump -i lo -nn tcp port 8000
```

## 47.4 Generate Traffic

```bash
curl http://127.0.0.1:8000
```

## 47.5 Observe Packets

You should observe TCP communication involving port 8000.

Depending on the output, you may see:

- TCP connection establishment.
- HTTP request traffic.
- HTTP response traffic.
- Connection termination.

## 47.6 Save the Capture

```bash
sudo tcpdump -i lo -w local-web.pcap tcp port 8000
```

Stop the capture and inspect it:

```bash
tcpdump -r local-web.pcap
```

The capture can also be opened in Wireshark.

---

# 48. Distinguish DNS Problems from Routing or Application Problems

This is one of the most important troubleshooting skills.

Consider the following situations.

## Situation 1: DNS Is Failing

Command:

```bash
curl https://example.com
```

Output:

```text
Could not resolve host
```

Possible issue:

- DNS resolution failure.

Investigate:

```bash
getent hosts example.com
dig example.com
cat /etc/resolv.conf
```

## Situation 2: Routing or Connectivity Is Failing

Test:

```bash
ping -c 4 1.1.1.1
```

If the destination is unreachable or no replies are received, investigate:

```bash
ip addr
ip route
ip neigh
```

Remember that ICMP filtering can also cause ping failure.

## Situation 3: The TCP Port Is Unreachable

Test:

```bash
nc -vz example.com 443
```

Possible problems:

- Firewall filtering.
- No service listening.
- Routing issue.
- Remote service unavailable.

## Situation 4: The Web Application Is Failing

Test:

```bash
curl -v https://example.com
```

If the TCP and TLS connections work but the server returns:

```text
HTTP/1.1 500 Internal Server Error
```

The issue may be in the server-side application.

## Troubleshooting Comparison

| Observation | Likely Area to Investigate |
|---|---|
| Hostname cannot resolve | DNS |
| IP destination unreachable | Routing or network connectivity |
| TCP connection refused | Destination port or service |
| Connection times out | Filtering, routing, or unresponsive endpoint |
| TLS certificate error | TLS configuration or trust |
| HTTP 404 | Resource or application routing |
| HTTP 500 | Server-side application |
| HTTP 403 | Access-control decision |
| HTTP 502 | Gateway or upstream service |

These are diagnostic clues, not absolute conclusions.

---

# PART 4: CYBERSECURITY CONNECTIONS

# 49. How Linux Networking Helps in Web Application Security

Networking knowledge is essential for web application security because web applications communicate over networks.

Understanding networking allows you to interpret what is happening between a browser, proxy, server, and backend services.

## 49.1 Understanding HTTP Traffic

You should understand:

- HTTP methods.
- Request headers.
- Response headers.
- Cookies.
- Status codes.
- HTTP versions.
- TLS.
- Ports.

These concepts are required for effective Burp Suite usage.

## 49.2 Understanding Open Ports

An open port may indicate a service listening on a network interface.

For example:

```text
22/tcp   SSH
80/tcp   HTTP
443/tcp  HTTPS
3306/tcp MySQL
```

The actual service must be identified rather than assumed from its port number.

## 49.3 Understanding Network Enumeration

Network enumeration involves gathering information about systems and services within an authorized scope.

Tools such as Nmap can help identify:

- Live hosts.
- Open ports.
- Service versions.
- Network exposure.

Example:

```bash
nmap -sV 127.0.0.1
```

This performs service-version detection against localhost.

## 49.4 Understanding Packet Captures

tcpdump and Wireshark allow you to inspect network packets.

You can learn:

- TCP handshakes.
- DNS queries.
- HTTP requests.
- Connection failures.
- Network retransmissions.
- Packet loss.

## 49.5 Understanding Network Security Boundaries

You should understand:

- Public vs private networks.
- NAT.
- Firewalls.
- Proxies.
- VPNs.
- Routing.
- Network segmentation.

These concepts help explain how an application is exposed and how traffic reaches it.

---

# PART 5: PRACTICAL LABS

# 50. Lab 1 — Explore Your Linux Network Configuration

### Objective

Understand your Kali Linux network configuration.

### Commands

```bash
ip addr
ip link
ip route
ip neigh
```

### What to Observe

- Network interface names.
- IPv4 and IPv6 addresses.
- MAC address.
- Interface state.
- Default gateway.
- Neighbor table.

### Verification

```bash
ip -br addr
ip route
```

### What You Learned

You learned how to inspect your Linux network interfaces, addresses, and routes.

---

# 51. Lab 2 — Test Localhost Communication

### Objective

Understand loopback communication and local TCP ports.

### Step 1: Start a Server

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

### Step 2: Check the Listening Port

```bash
ss -lnt
```

### Step 3: Connect Using curl

```bash
curl http://127.0.0.1:8000
```

### Step 4: Connect Using Netcat

```bash
nc -vz 127.0.0.1 8000
```

### Step 5: Stop the Server

```text
Ctrl + C
```

### Step 6: Verify

```bash
ss -lnt
```

### What You Learned

- How a local server listens.
- How ports work.
- How clients connect to servers.
- How to inspect local network services.

---

# 52. Lab 3 — DNS Investigation

### Objective

Understand DNS queries and resolution.

### Commands

```bash
dig example.com
dig A example.com
dig AAAA example.com
dig MX example.com
host example.com
nslookup example.com
getent hosts example.com
```

### What to Observe

- IP addresses.
- DNS response status.
- Record types.
- DNS server information.
- Differences between lookup tools.

### Verification

```bash
curl -I https://example.com
```

### What You Learned

You learned how Linux resolves hostnames and how to inspect DNS records.

---

# 53. Lab 4 — TCP Connection Testing

### Objective

Understand TCP listening sockets and connections.

### Step 1: Start a Local Listener

```bash
nc -l 127.0.0.1 9000
```

### Step 2: Connect From Another Terminal

```bash
nc 127.0.0.1 9000
```

### Step 3: Exchange Messages

Type a message in one terminal and observe the other terminal.

### Step 4: Inspect Connections

```bash
ss -ant
```

### Step 5: Stop Both Processes

Use:

```text
Ctrl + C
```

### What You Learned

You learned how TCP connections work and how to inspect them.

---

# 54. Lab 5 — HTTP Request Analysis

### Objective

Understand HTTP requests and responses.

### Commands

```bash
curl -I https://example.com
curl -v https://example.com
curl -L https://example.com
```

### What to Observe

- HTTP status code.
- Response headers.
- Redirect behavior.
- TLS connection details.
- Server response.

### What You Learned

You learned how to inspect web server communication from the Linux terminal.

---

# 55. Lab 6 — Packet Capture

### Objective

Capture and inspect local network traffic.

### Step 1: Identify the Loopback Interface

```bash
ip link
```

### Step 2: Start tcpdump

```bash
sudo tcpdump -i lo -nn tcp port 8000
```

### Step 3: Start a Local Web Server

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

### Step 4: Generate Traffic

```bash
curl http://127.0.0.1:8000
```

### Step 5: Observe the Capture

Look for:

- TCP packets.
- Source and destination ports.
- Sequence information.
- HTTP traffic.

### Step 6: Stop Capture

```text
Ctrl + C
```

### What You Learned

You learned how packet capture works and how to observe communication between local applications.

---

# 56. Lab 7 — Network Troubleshooting Challenge

### Objective

Practice diagnosing connectivity problems systematically.

Answer these questions using your Kali VM.

1. What is your current IPv4 address?
2. What is your default gateway?
3. Which interface connects your VM to the network?
4. Can you resolve `example.com`?
5. Can you reach `1.1.1.1`?
6. What DNS server is configured?
7. Is TCP port 443 reachable on an external test website?
8. Can you start a local web server?
9. Can you identify its listening port?
10. Can you capture its traffic with tcpdump?

### Suggested Commands

```bash
ip addr
ip route
ip neigh
ping -c 4 1.1.1.1
dig example.com
getent hosts example.com
nc -vz example.com 443
ss -lnt
curl -I https://example.com
sudo tcpdump -i lo -nn
```

Use only authorized destinations and keep packet captures limited to your lab.

---

# PART 6: QUICK REVISION

# 57. Important Networking Concepts

| Concept | Remember |
|---|---|
| IPv4 | 32-bit IP addressing |
| IPv6 | 128-bit IP addressing |
| Public IP | Globally routable address |
| Private IP | Internal network addressing |
| Loopback | Communication with the same machine |
| MAC | Link-layer address |
| Subnet | Logical division of a network |
| CIDR | Prefix-based network notation |
| Gateway | Next-hop router for other networks |
| Routing | Selecting a packet's forwarding path |
| TCP | Reliable, ordered byte-stream transport |
| UDP | Connectionless datagram transport |
| Port | Transport endpoint identifier |
| Socket | Software communication endpoint |
| DNS | Domain name resolution |
| DHCP | Automatic network configuration |
| ARP | IPv4-to-link-layer address resolution |
| ICMP | Network diagnostics and error reporting |
| HTTP | Web application protocol |
| HTTPS | HTTP protected by TLS |
| TLS | Secure communication protocol |
| NAT | Network address translation |
| Firewall | Network traffic filtering |
| Proxy | Intermediary communication server |
| VPN | Virtual private network |
| OSI | Seven-layer reference model |
| TCP/IP | Practical internet protocol architecture |

# 58. Important Linux Networking Commands

| Command | Purpose |
|---|---|
| `ip addr` | Display IP addresses |
| `ip link` | Display network interfaces |
| `ip route` | Display routing table |
| `ip neigh` | Display neighbor table |
| `ping` | Test ICMP reachability |
| `traceroute` | Trace network path |
| `tracepath` | Discover network path |
| `ss` | Inspect sockets and connections |
| `curl` | Transfer data and test HTTP |
| `wget` | Download files |
| `dig` | Query DNS records |
| `host` | Perform DNS lookups |
| `nslookup` | Query DNS |
| `getent hosts` | Resolve hostnames using system databases |
| `resolvectl` | Inspect systemd-resolved |
| `nc` | Test TCP/UDP communication |
| `tcpdump` | Capture network packets |
| `nft` | Manage nftables rules |
| `ufw` | Manage firewall rules |

# 59. Important Networking Ports

| Port | Protocol | Service |
|---|---|---|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 67 | UDP | DHCP Server |
| 68 | UDP | DHCP Client |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 443 | UDP | QUIC / HTTP/3 |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 8080 | TCP | Alternative HTTP |

# 60. Important Configuration Files

| File | Purpose |
|---|---|
| `/etc/hosts` | Local hostname mappings |
| `/etc/resolv.conf` | DNS resolver configuration |
| `/etc/nsswitch.conf` | Name-service lookup configuration |
| `/etc/hostname` | System hostname |
| `/etc/NetworkManager/` | NetworkManager configuration |
| `/etc/ssh/sshd_config` | SSH server configuration |

The exact configuration and management method depends on the Linux distribution and installed network services.

---

# PART 7: INTERVIEW AND SELF-ASSESSMENT

# 61. Beginner-Level Questions

### Q1. What is an IP address?

An IP address is a logical network address used to identify a network interface and enable IP communication.

### Q2. What is the difference between IPv4 and IPv6?

IPv4 uses 32-bit addresses, whereas IPv6 uses 128-bit addresses.

### Q3. What is a private IP address?

A private IP address is an address reserved for internal networks and is not globally routed across the public internet.

### Q4. What is localhost?

Localhost is a hostname that normally resolves to loopback addresses, allowing a machine to communicate with itself.

### Q5. What is a MAC address?

A MAC address is a link-layer address used for communication over local network technologies.

### Q6. What is a default gateway?

A default gateway is the next-hop router used when a destination does not match a more specific route.

### Q7. What is DNS?

DNS translates domain names into IP addresses and provides other naming information.

### Q8. What is DHCP?

DHCP automatically assigns IP configuration information to network clients.

### Q9. What is ARP?

ARP resolves an IPv4 address to a link-layer address on a local network.

### Q10. What is ICMP?

ICMP is a protocol used for IP-related error reporting and diagnostics.

# 62. Intermediate-Level Questions

### Q1. What is the difference between TCP and UDP?

TCP provides reliable, ordered byte-stream delivery. UDP provides connectionless datagram delivery without built-in reliability or ordering guarantees.

### Q2. Explain the TCP three-way handshake.

The client sends SYN, the server responds with SYN-ACK, and the client sends ACK.

### Q3. What is CIDR notation?

CIDR represents an IP network using an address and prefix length, such as `192.168.1.0/24`.

### Q4. What is NAT?

NAT modifies IP addressing information as packets pass through a network device. It commonly allows multiple private IPv4 devices to share public IPv4 connectivity.

### Q5. What is the difference between a port and a socket?

A port is a transport-layer endpoint identifier. A socket is a software communication endpoint that uses addressing and transport information.

### Q6. What is the difference between a firewall and a proxy?

A firewall filters network traffic according to security rules. A proxy acts as an intermediary between clients and servers.

### Q7. What is HTTPS?

HTTPS is HTTP protected by TLS, providing encryption, integrity protection, and certificate-based server authentication.

### Q8. What is the purpose of tcpdump?

tcpdump captures and displays network packets for troubleshooting and traffic analysis.

### Q9. What is the difference between `ip addr` and `ip route`?

`ip addr` displays IP address configuration, whereas `ip route` displays routing information.

### Q10. Why might ping fail while a website still works?

The destination or an intermediate firewall may block ICMP while allowing TCP or UDP application traffic.

# 63. Practical Interview Questions

1. How would you identify your default gateway in Linux?
2. How would you identify your network interface?
3. How would you find the MAC address of your interface?
4. How would you inspect listening TCP ports?
5. How would you identify established TCP connections?
6. How would you troubleshoot a DNS resolution failure?
7. How would you check whether a web server is reachable?
8. How would you inspect HTTP response headers?
9. How would you capture DNS traffic?
10. How would you identify the network route to a destination?
11. How would you identify a local server listening on port 8000?
12. What is the difference between an open, closed, and filtered port?
13. How does the TCP three-way handshake work?
14. What is the difference between a forward proxy and reverse proxy?
15. What happens when a client connects to an HTTPS website?

---

# PART 8: LEARNING CHECKLIST

# 64. Networking Fundamentals Checklist

## IP Addressing

- [ ] Understand IPv4.
- [ ] Understand IPv6.
- [ ] Understand public IP addresses.
- [ ] Understand private IP addresses.
- [ ] Understand loopback addresses.
- [ ] Understand MAC addresses.
- [ ] Understand subnet masks.
- [ ] Understand CIDR notation.
- [ ] Understand default gateways.
- [ ] Understand routing tables.

## Network Protocols

- [ ] Understand TCP.
- [ ] Understand UDP.
- [ ] Understand ports.
- [ ] Understand sockets.
- [ ] Understand DNS.
- [ ] Understand DHCP.
- [ ] Understand ARP.
- [ ] Understand ICMP.
- [ ] Understand HTTP.
- [ ] Understand HTTPS.
- [ ] Understand TLS certificates.

## Network Architecture

- [ ] Understand NAT.
- [ ] Understand firewalls.
- [ ] Understand proxies.
- [ ] Understand VPNs.
- [ ] Understand client-server architecture.
- [ ] Understand the OSI model.
- [ ] Understand the TCP/IP model.
- [ ] Understand encapsulation and decapsulation.

## Linux Networking Commands

- [ ] Practise `ip addr`.
- [ ] Practise `ip link`.
- [ ] Practise `ip route`.
- [ ] Practise `ip neigh`.
- [ ] Practise `ping`.
- [ ] Practise `traceroute`.
- [ ] Practise `tracepath`.
- [ ] Practise `ss`.
- [ ] Practise `curl`.
- [ ] Practise `wget`.
- [ ] Practise `dig`.
- [ ] Practise `host`.
- [ ] Practise `nslookup`.
- [ ] Practise `getent hosts`.
- [ ] Practise `resolvectl` where available.
- [ ] Practise `nc`.
- [ ] Practise `tcpdump`.
- [ ] Understand `nftables`.
- [ ] Understand `ufw`.

## Troubleshooting

- [ ] Diagnose a DNS lookup failure.
- [ ] Check whether a local port is listening.
- [ ] Inspect active network connections.
- [ ] Inspect IP configuration.
- [ ] Inspect routing information.
- [ ] Inspect HTTP response headers.
- [ ] Capture traffic from a lab interface.
- [ ] Distinguish DNS problems from routing problems.
- [ ] Distinguish connectivity problems from application problems.

## Cybersecurity Preparation

- [ ] Understand how web traffic travels.
- [ ] Understand HTTP requests and responses.
- [ ] Understand TCP connections.
- [ ] Understand DNS resolution.
- [ ] Understand network ports.
- [ ] Understand firewalls and network filtering.
- [ ] Understand proxies and VPNs.
- [ ] Understand basic packet analysis.
- [ ] Understand network enumeration fundamentals.
- [ ] Understand how networking supports Burp Suite and Nmap.

---

# 65. Final Phase 7 Completion Goals

Before moving to the next phase, you should be able to perform the following tasks without relying heavily on notes:

1. Identify your Kali Linux IP address.
2. Identify your MAC address.
3. Find your default gateway.
4. Inspect your routing table.
5. Explain TCP and UDP differences.
6. Explain how DNS resolves a hostname.
7. Explain the DHCP DORA process.
8. Explain how ARP resolves a local IPv4 address.
9. Explain how HTTPS uses TLS.
10. Identify listening ports using `ss`.
11. Test a TCP connection using `nc`.
12. Inspect a website using `curl`.
13. Query DNS using `dig`.
14. Capture packets using `tcpdump`.
15. Troubleshoot a basic DNS failure.
16. Explain the seven OSI layers.
17. Explain how a browser communicates with a web server.

## Final Understanding

Linux networking is not simply about memorizing commands.

You should understand what happens when a device communicates with another device:

- How it obtains an IP address.
- How it identifies the destination.
- How it determines whether the destination is local or remote.
- How it finds the next hop.
- How it establishes transport communication.
- How applications exchange data.
- How the operating system monitors and filters traffic.

These fundamentals will help you understand web application communication, network enumeration, packet analysis, and application security testing.

**Phase 7 is complete when you can explain the concepts and demonstrate the practical exercises in your own Kali Linux environment.**
