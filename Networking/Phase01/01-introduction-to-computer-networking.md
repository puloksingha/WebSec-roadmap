
# Phase 1: Networking Fundamentals

## 1. Introduction to Computer Networking

## Table of Contents

1. What is a Computer Network?
2. Why Do We Need Computer Networks?
3. Advantages and Disadvantages of Networking
4. Network Devices and Network Interfaces
5. Hosts, Clients, Servers, and Peers
6. Data Communication Fundamentals
7. Network Protocols and Standards
8. Network Architecture
9. Network Topology
10. Physical vs Logical Topology
11. LAN — Local Area Network
12. WAN — Wide Area Network
13. MAN — Metropolitan Area Network
14. PAN — Personal Area Network
15. WLAN — Wireless LAN
16. Internet vs Intranet vs Extranet
17. Public Networks vs Private Networks
18. Wired vs Wireless Networks
19. Peer-to-Peer vs Client-Server Networking
20. Bandwidth, Throughput, and Latency
21. Jitter and Packet Loss
22. Full-Duplex vs Half-Duplex Communication
23. Unicast, Multicast, Broadcast, and Anycast
24. Circuit Switching vs Packet Switching
25. What is a Network Packet?
26. Frames, Packets, Segments, and Datagrams
27. Practical Networking Tasks
28. Key Takeaways

---

# 1. What is a Computer Network?

A **computer network** is a collection of two or more computing devices connected together through communication links to exchange data, share resources, and communicate with one another.

These devices may include:

- Computers
- Laptops
- Smartphones
- Servers
- Printers
- Routers
- Switches
- IoT devices

A network allows devices to communicate using a set of rules called **network protocols**.

### Example

Suppose you have:

- A laptop
- A smartphone
- A Wi-Fi router
- An internet connection

Your laptop and smartphone connect to the router through Wi-Fi.

The router allows these devices to communicate with one another and access the internet.

```text
             Internet
                |
             [Router]
             /      \
          Wi-Fi    Wi-Fi
           /          \
       [Laptop]    [Phone]
```

This is a simple computer network.

### Definition for Exams

A computer network is an interconnected collection of computers and other devices that communicate with one another to exchange information and share resources through communication links using standard protocols.

---

# 2. Why Do We Need Computer Networks?

Computer networks are essential because they allow devices and users to communicate efficiently.

## 2.1 Resource Sharing

Networks allow multiple devices to share resources.

Examples:

- Sharing a printer among multiple computers.
- Sharing files between computers.
- Sharing an internet connection.
- Accessing a centralized storage system.

## 2.2 Communication

Networks enable communication between people and systems.

Examples:

- Email
- Video conferencing
- Messaging applications
- Voice calls
- Social media

## 2.3 Data Sharing

Users can exchange data between devices without physically transferring storage devices.

For example, a file can be transferred from one computer to another over a local network.

## 2.4 Centralized Management

Organizations can manage users, systems, and data from centralized servers.

For example, an organization may use a central server to manage employee accounts.

## 2.5 Remote Access

Users can access systems and resources from remote locations.

Examples:

- SSH access to a Linux server.
- Remote desktop connections.
- Accessing cloud-based applications.

## 2.6 Scalability

A network can be expanded by adding more devices, servers, or communication links.

## 2.7 Cloud Computing

Networks enable access to cloud services.

Examples:

- Google Drive
- Microsoft Azure
- Amazon Web Services
- Cloud-hosted websites

### Cybersecurity Relevance

Networking is the foundation of cybersecurity.

To understand how an attacker or defender interacts with a system, you must understand:

- How devices communicate.
- How IP addresses identify devices.
- How ports identify services.
- How packets travel across networks.
- How network protocols operate.

For example, a penetration tester may investigate an authorized target to identify exposed network services.

---

# 3. Advantages and Disadvantages of Networking

## Advantages

| Advantage | Explanation |
|---|---|
| Resource sharing | Multiple devices can share printers, storage, and other resources. |
| Communication | Enables email, messaging, and video calls. |
| Data sharing | Allows quick exchange of information. |
| Cost reduction | Shared resources reduce infrastructure costs. |
| Centralized management | Users and systems can be managed centrally. |
| Remote access | Resources can be accessed from different locations. |
| Scalability | New devices can be added to the network. |
| Collaboration | Multiple users can work on shared resources. |

## Disadvantages

| Disadvantage | Explanation |
|---|---|
| Security risks | Networks can be targeted by attackers. |
| Malware propagation | Malware may spread between connected systems. |
| Infrastructure cost | Networking equipment and maintenance can be expensive. |
| Dependency | Network failures may interrupt services. |
| Privacy concerns | Network traffic may expose sensitive information if not protected. |
| Complexity | Large networks require careful configuration and management. |
| Performance issues | Congestion can reduce network performance. |

### Important Point

A network improves communication and resource sharing, but it also increases the number of systems that may need protection.

This is why network security is an important part of cybersecurity.

---

# 4. Network Devices and Network Interfaces

Network devices are hardware components that enable communication between computers and other devices.

## 4.1 Network Interface Card (NIC)

A **Network Interface Card (NIC)** is a hardware component that allows a device to connect to a network.

A NIC may support:

- Ethernet
- Wi-Fi
- Other networking technologies

A network interface may be integrated into the motherboard or installed separately.

### Types of NIC

**Wired NIC**

Uses an Ethernet cable to connect to a network.

**Wireless NIC**

Uses radio signals to connect to a wireless network.

### MAC Address

A NIC commonly has a Media Access Control (MAC) address.

A MAC address is a link-layer identifier used for communication within a local network.

Example:

```text
00:1A:2B:3C:4D:5E
```

A MAC address is usually represented as six hexadecimal bytes.

Important: MAC addresses can be changed or spoofed in software, so they should not be treated as permanent proof of a device's identity.

## 4.2 Repeater

A repeater regenerates or retransmits a signal to extend its transmission distance.

It operates primarily at the Physical Layer (Layer 1) of the OSI model.

## 4.3 Hub

A hub connects multiple devices in a network.

When a hub receives a signal, it repeats that signal to its other ports.

Characteristics:

- Operates at Layer 1.
- Does not learn MAC addresses.
- Sends incoming signals to all other ports.
- Creates a shared collision domain.

Hubs are largely obsolete in modern Ethernet networks.

## 4.4 Bridge

A bridge connects network segments and forwards frames based on MAC addresses.

It operates at Layer 2.

A bridge can reduce unnecessary traffic between network segments.

## 4.5 Switch

A network switch connects devices within a local area network.

A typical Ethernet switch operates at Layer 2 and forwards frames based on MAC addresses.

### How a switch works

1. A frame arrives at a switch port.
2. The switch learns the source MAC address.
3. It associates that address with the incoming port.
4. It checks the destination MAC address.
5. It forwards the frame to the appropriate port.

If the destination MAC address is unknown, a switch generally floods the frame within the VLAN, excluding the incoming port.

### Example

```text
              [Switch]
             /    |    \
            /     |     \
         PC1     PC2    PC3
```

Switches are important because they allow devices within a LAN to communicate efficiently.

## 4.6 Router

A router connects different IP networks and forwards packets between them.

It primarily operates at Layer 3.

A router uses a routing table to determine where packets should be forwarded.

Example:

```text
      [LAN 1]
          |
       [Router]
          |
      [LAN 2]
```

A home router often performs several functions:

- Routing
- NAT (Network Address Translation)
- DHCP
- Firewall filtering
- Wireless access point functionality

These are separate networking functions that may be combined into one device.

## 4.7 Modem

A modem converts signals or adapts data transmission to the technology used by an internet access connection.

The term modem comes from:

- Modulator
- Demodulator

Modern broadband equipment may combine modem and router functions.

## 4.8 Wireless Access Point (AP)

A wireless access point allows wireless devices to connect to a network.

It commonly bridges Wi-Fi devices to an Ethernet-based LAN.

Example:

```text
        [Ethernet Switch]
               |
        [Wireless AP]
          /        \
       Laptop     Phone
```

A wireless access point is not necessarily a router.

## 4.9 Firewall

A firewall monitors and controls network traffic according to security rules.

Firewalls may filter traffic based on:

- Source IP address
- Destination IP address
- Protocol
- Source or destination port
- Connection state
- Application information

Firewalls can be implemented as hardware appliances, software, or cloud services.

---

# 5. Hosts, Clients, Servers, and Peers

## 5.1 Host

A host is a device connected to a network that can send or receive data.

Examples:

- Laptop
- Smartphone
- Web server
- Virtual machine

A host may have one or more network interfaces and IP addresses.

## 5.2 Client

A client is a device or software application that requests a service or resource.

Examples:

- A browser requesting a webpage.
- An email application retrieving messages.
- An SSH client connecting to a remote server.

## 5.3 Server

A server is a device or software application that provides a service to clients.

Examples:

| Server Type | Purpose |
|---|---|
| Web server | Delivers websites and web applications. |
| DNS server | Resolves domain names into IP addresses. |
| DHCP server | Assigns network configuration to clients. |
| File server | Provides shared file storage. |
| Mail server | Sends, receives, or stores email. |
| Database server | Provides database services. |

A server does not always need to be a separate physical computer. It can run as software on a virtual machine or container.

## 5.4 Peer

A peer is a device that can communicate directly with another device without relying exclusively on a centralized server.

In a peer-to-peer network, devices may act as both clients and servers.

Example:

```text
       [Peer A] <----> [Peer B]
           ^               |
           |               |
           +----> [Peer C]
```

### Important Difference

A host is a network-connected device.

A client requests services.

A server provides services.

A peer participates in a peer-to-peer relationship.

---

# 6. Data Communication Fundamentals

Data communication is the exchange of information between two or more devices through a transmission medium.

## 6.1 Basic Components of Data Communication

A data communication system has five main components.

| Component | Description |
|---|---|
| Sender | Device that sends the data. |
| Receiver | Device that receives the data. |
| Message | Information being transmitted. |
| Transmission medium | Path through which the data travels. |
| Protocol | Rules governing communication. |

### Example

When you send a message through a messaging application:

- Sender: Your smartphone.
- Receiver: The recipient's smartphone.
- Message: Text or media.
- Medium: Wi-Fi, cellular, and internet links.
- Protocol: The protocols used by the application and network.

## 6.2 Transmission Media

Transmission media are the paths through which data travels.

### Guided Media

Data travels through a physical medium.

Examples:

- Twisted-pair Ethernet cable.
- Coaxial cable.
- Optical fiber.

### Unguided Media

Data travels through electromagnetic waves without a physical cable.

Examples:

- Wi-Fi
- Bluetooth
- Cellular networks
- Satellite communication

## 6.3 Characteristics of Data Communication

Effective data communication should provide:

**Delivery:** Data reaches the intended destination.

**Accuracy:** Data is received without unacceptable errors.

**Timeliness:** Data arrives when needed.

**Jitter:** Variation in packet arrival time should be sufficiently low for applications that require consistent timing.

For example, video conferencing requires timely delivery and low jitter.

---

# 7. Network Protocols and Standards

## 7.1 What is a Network Protocol?

A network protocol is a set of rules that defines how devices communicate and exchange data.

Protocols define:

- Data format
- Addressing
- Transmission procedures
- Error handling
- Connection management
- Communication behavior

Without shared protocols, devices from different manufacturers would have difficulty communicating.

## 7.2 Common Network Protocols

| Protocol | Purpose |
|---|---|
| IP | Provides logical addressing and packet forwarding. |
| TCP | Provides reliable, ordered byte-stream communication. |
| UDP | Provides connectionless datagram communication. |
| HTTP | Transfers web resources. |
| HTTPS | HTTP protected using TLS. |
| DNS | Resolves domain names and provides other DNS information. |
| DHCP | Automatically provides network configuration. |
| ARP | Resolves IPv4 addresses to link-layer addresses on a local network. |
| ICMP | Supports network control and diagnostic messages. |
| SSH | Provides secure remote access and other secure communication features. |
| SMTP | Transfers email between mail systems. |
| FTP | Transfers files using a traditional client-server protocol. |

## 7.3 Network Standards

Network standards define common specifications that allow devices and systems to interoperate.

Examples:

- IEEE 802.3 — Ethernet.
- IEEE 802.11 — Wi-Fi.
- IETF RFCs — Internet protocol specifications.
- ISO standards — International standards for various technologies.

### Important Organizations

| Organization | Role |
|---|---|
| IEEE | Develops standards such as Ethernet and Wi-Fi. |
| IETF | Develops Internet standards and RFCs. |
| ISO | Develops international standards. |
| ITU-T | Develops telecommunications standards. |
| ICANN | Coordinates key Internet naming and numbering functions. |

### What is an RFC?

RFC stands for **Request for Comments**.

RFC documents describe technical specifications, standards, best practices, and other Internet-related information.

For example, TCP is specified in RFC 9293.

---

# 8. Network Architecture

Network architecture describes the overall structure and organization of a network, including how devices, services, protocols, and communication layers interact.

## 8.1 Client-Server Architecture

In client-server architecture, clients request services from servers.

Example:

```text
[Browser] ---- Request ----> [Web Server]
[Browser] <--- Response ---- [Web Server]
```

Advantages:

- Centralized management.
- Easier access control.
- Centralized data storage.
- Easier service monitoring.

Disadvantages:

- Server failure may affect many clients.
- Infrastructure may be expensive.
- Servers can become performance bottlenecks.

## 8.2 Peer-to-Peer Architecture

In peer-to-peer architecture, devices communicate and share resources directly.

Advantages:

- No mandatory central server.
- Can distribute workload.
- May reduce centralized infrastructure costs.

Disadvantages:

- More difficult centralized management.
- Security and trust can be challenging.
- Availability depends on participating peers.

## 8.3 Layered Architecture

Networking is organized into layers.

Each layer performs a specific function and communicates with adjacent layers through defined interfaces.

Benefits:

- Simplifies network design.
- Supports interoperability.
- Makes troubleshooting easier.
- Allows protocols to evolve independently.

Two important networking models are:

1. OSI model.
2. TCP/IP model.

These models are covered in detail in later networking topics.

---

# 9. Network Topology

Network topology describes how devices and communication links are arranged in a network.

There are two major forms:

- Physical topology.
- Logical topology.

## 9.1 Bus Topology

All devices share a common communication backbone.

```text
[PC1] ---- [PC2] ---- [PC3] ---- [PC4]
```

Advantages:

- Simple design.
- Requires less cable in some implementations.

Disadvantages:

- Backbone failure can affect the network.
- Troubleshooting can be difficult.
- Shared-medium collisions may occur.

Bus topology was common in older Ethernet networks.

## 9.2 Star Topology

All devices connect to a central device, such as a switch.

```text
             [PC1]
               |
[PC2] ---- [Switch] ---- [PC3]
               |
             [PC4]
```

Advantages:

- Easy to manage.
- Easy to add devices.
- Failure of one endpoint cable usually affects only that endpoint.

Disadvantages:

- Central switch failure can affect all connected devices.
- Requires more cabling than some bus designs.

Modern Ethernet LANs commonly use a physical star topology.

## 9.3 Ring Topology

Devices are connected in a circular arrangement.

```text
[PC1] ---- [PC2]
  |          |
[PC4] ---- [PC3]
```

Advantages:

- Can provide orderly access in some ring technologies.
- Predictable communication behavior.

Disadvantages:

- Some ring designs are vulnerable to a link failure.
- Reconfiguration may be complex.

Some technologies use dual rings or protection mechanisms to improve resilience.

## 9.4 Mesh Topology

Devices connect to multiple other devices.

### Full Mesh

Every device has a direct connection to every other device.

For `n` devices, the number of links in a full mesh is:

\[
L = \frac{n(n-1)}{2}
\]

Example:

For 5 devices:

\[
L = \frac{5(5-1)}{2} = 10
\]

Advantages:

- Multiple communication paths.
- High redundancy.
- Improved resilience.

Disadvantages:

- Expensive.
- Requires many connections.
- Complex to maintain.

### Partial Mesh

Only selected devices have multiple direct connections.

Partial mesh networks are common in real-world infrastructure.

## 9.5 Tree Topology

A tree topology organizes devices hierarchically.

```text
             [Core Switch]
              /         \
       [Switch A]      [Switch B]
         /    \          /    \
       PC1    PC2      PC3    PC4
```

Advantages:

- Scalable.
- Supports hierarchical management.
- Suitable for large networks.

Disadvantages:

- Failure of an upper-level device may affect multiple branches.
- Configuration can become complex.

## 9.6 Hybrid Topology

A hybrid topology combines multiple topology types.

For example, a network may use star topology within buildings and partial mesh connections between buildings.

---

# 10. Physical vs Logical Topology

## Physical Topology

Physical topology describes the actual physical arrangement of:

- Devices
- Cables
- Ports
- Network equipment

Example:

A set of computers connected to a central switch forms a physical star topology.

## Logical Topology

Logical topology describes how data flows through a network, regardless of its physical arrangement.

For example, a switched Ethernet network may physically use a star topology while allowing devices to communicate through logical paths determined by switching.

### Comparison

| Physical Topology | Logical Topology |
|---|---|
| Describes physical connections. | Describes data flow. |
| Focuses on cables and devices. | Focuses on communication behavior. |
| Helps with physical installation. | Helps with understanding communication. |

### Important Example

A Wi-Fi network may have a physical arrangement involving an access point and several wireless devices.

Its logical communication behavior depends on the wireless protocol and network configuration.

---

# 11. LAN — Local Area Network

A **Local Area Network (LAN)** connects devices within a relatively limited area.

Examples:

- Home network.
- Computer laboratory.
- Office network.
- School network.

A LAN commonly uses Ethernet or Wi-Fi.

### Characteristics

- Usually covers a limited geographical area.
- Often privately managed.
- Typically offers high-speed communication.
- Usually has relatively low latency.
- Can support resource sharing.

### Example

```text
           [Router]
              |
           [Switch]
          /   |    \
        PC1  PC2  Printer
```

### Cybersecurity Relevance

LAN security includes:

- Network segmentation.
- Access control.
- Switch security.
- Monitoring network traffic.
- Protecting internal services.

A compromised device on a LAN may attempt to communicate with other devices, which makes internal network security important.

---

# 12. WAN — Wide Area Network

A **Wide Area Network (WAN)** connects networks over large geographical areas.

Examples:

- Networks connecting offices in different cities.
- Corporate networks connecting multiple countries.
- Internet service provider infrastructure.

The Internet is the largest example of an interconnected global network.

### Characteristics

- Covers large geographical areas.
- Often uses infrastructure provided by telecommunications companies.
- May have higher latency than a local network.
- Can use fiber, leased lines, cellular networks, and satellite links.

### Example

```text
[Office LAN A] ---- WAN ---- [Office LAN B]
       |                         |
     Router                    Router
```

### LAN vs WAN

| Feature | LAN | WAN |
|---|---|---|
| Coverage | Limited area | Large geographical area |
| Ownership | Often privately managed | May involve multiple providers |
| Latency | Usually lower | Often higher |
| Example | Home network | Interconnected branch offices |

---

# 13. MAN — Metropolitan Area Network

A **Metropolitan Area Network (MAN)** connects networks across a city or metropolitan region.

It is generally larger than a LAN but smaller than a WAN.

Examples:

- City-wide university networks.
- Metropolitan fiber networks.
- Networks connecting government offices across a city.

### Characteristics

- Covers a metropolitan region.
- Can connect multiple LANs.
- May use high-speed fiber infrastructure.
- May be operated by a service provider or organization.

### Example

```text
[Campus A] ----\
                \
[Campus B] ------ [Metropolitan Network]
                /
[Campus C] ----/
```

---

# 14. PAN — Personal Area Network

A **Personal Area Network (PAN)** connects devices around an individual.

Examples:

- Smartphone connected to wireless earbuds.
- Laptop connected to a Bluetooth mouse.
- Smartphone sharing internet through a hotspot.

### Characteristics

- Covers a short distance.
- Usually connects personal devices.
- Commonly uses Bluetooth or USB.
- May use Wi-Fi for personal hotspot communication.

### Example

```text
       [Smartphone]
        /        \
   Bluetooth   Bluetooth
      /            \
 [Earbuds]       [Watch]
```

---

# 15. WLAN — Wireless LAN

A **Wireless Local Area Network (WLAN)** is a LAN that uses wireless communication.

WLANs commonly use IEEE 802.11, also known as Wi-Fi.

### Components

- Wireless access point.
- Wireless network interface.
- Wireless clients.
- Authentication and encryption mechanisms.

### Example

```text
           [Wireless Router]
             /          \
          Wi-Fi        Wi-Fi
           /              \
       [Laptop]         [Phone]
```

### Wi-Fi Security

Modern Wi-Fi networks commonly use WPA2 or WPA3 security.

Security recommendations:

- Use a strong Wi-Fi password.
- Prefer WPA3 or WPA2-AES.
- Disable obsolete security modes.
- Update router firmware.
- Avoid exposing router administration to untrusted networks.
- Use a guest network for untrusted devices when appropriate.

### Important Difference

WLAN is a type of LAN.

Wi-Fi is a wireless networking technology commonly used to implement WLANs.

---

# 16. Internet vs Intranet vs Extranet

## Internet

The Internet is a global system of interconnected networks that communicate using the Internet Protocol Suite.

It enables access to services such as:

- Websites.
- Email.
- Cloud applications.
- Online communication.

## Intranet

An intranet is a private network or collection of services used within an organization.

Examples:

- Internal employee portal.
- Internal document management system.
- Company-only applications.

An intranet may use the same technologies as the Internet but restrict access to authorized users.

## Extranet

An extranet allows selected external users or organizations to access specific resources of a private organization.

Examples:

- Supplier portal.
- Business partner dashboard.
- Customer support portal.

### Comparison

| Feature | Internet | Intranet | Extranet |
|---|---|---|---|
| Access | Publicly accessible services | Restricted internal access | Restricted external and internal access |
| Users | General public | Organization members | Authorized partners or customers |
| Purpose | Global communication | Internal communication | Controlled external collaboration |

### Example

A company may use:

- Internet: Public company website.
- Intranet: Internal employee portal.
- Extranet: Supplier login portal.

---

# 17. Public Networks vs Private Networks

## Public Network

A public network is a network that provides connectivity to a broad set of users or is accessible through public infrastructure.

Examples:

- Public Wi-Fi in a café.
- Airport Wi-Fi.
- Public Internet services.

A public network may still have authentication or usage restrictions.

## Private Network

A private network is a network restricted to an organization or defined group of users.

Examples:

- Home LAN.
- Office LAN.
- Internal corporate network.

Private networks commonly use private IPv4 address ranges.

### Private IPv4 Address Ranges

RFC 1918 defines the following private IPv4 ranges:

| Range | CIDR |
|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

Example:

```text
192.168.1.10
```

This is a private IPv4 address.

### Important

Private IP addresses are not directly globally routable on the public Internet.

However, private networks can access Internet services through mechanisms such as NAT.

### Public IP Address

A public IP address is globally routable, subject to routing policies and other restrictions.

Public IP addresses are commonly assigned by Internet service providers.

---

# 18. Wired vs Wireless Networks

## Wired Networks

Wired networks use physical cables to transmit data.

Examples:

- Ethernet.
- Fiber-optic communication.
- Coaxial cable networks.

### Advantages

- Often more stable.
- Generally less affected by radio interference.
- Can provide high throughput.
- Often suitable for servers and fixed workstations.

### Disadvantages

- Requires physical cabling.
- Limits mobility.
- Installation may be expensive.
- Cable damage can interrupt connectivity.

## Wireless Networks

Wireless networks use electromagnetic waves to communicate.

Examples:

- Wi-Fi.
- Bluetooth.
- Cellular communication.

### Advantages

- Mobility.
- Flexible installation.
- Convenient connectivity.
- Reduced need for physical cables.

### Disadvantages

- Radio interference.
- Signal attenuation.
- Shared wireless medium.
- Security depends on proper configuration.
- Performance may vary with distance and congestion.

### Comparison

| Feature | Wired | Wireless |
|---|---|---|
| Medium | Physical cable | Radio waves or other wireless signals |
| Mobility | Limited | High |
| Interference | Usually lower | Can be affected by radio interference |
| Installation | Requires cabling | Often easier to deploy |
| Security | Physical access and network controls matter | Physical access and wireless security both matter |

---

# 19. Peer-to-Peer vs Client-Server Networking

## Peer-to-Peer Networking

In peer-to-peer networking, devices communicate directly and may share resources with one another.

Each device can act as both a client and a server.

Example:

```text
[Peer A] <------> [Peer B]
    ^                 ^
    |                 |
    +----> [Peer C] <-+
```

Advantages:

- Distributed resource sharing.
- No mandatory centralized server.
- Can scale by adding peers.

Disadvantages:

- More difficult centralized administration.
- Security management can be challenging.
- Peers may become unavailable.

## Client-Server Networking

In client-server networking, clients request services from a central or dedicated server.

Example:

```text
             [Server]
             /  |   \
            /   |    \
         [C1]  [C2]  [C3]
```

Advantages:

- Centralized administration.
- Easier data management.
- Centralized authentication.
- Easier monitoring.

Disadvantages:

- Server failure may disrupt service.
- Server infrastructure may be costly.
- High demand can create bottlenecks.

### Comparison

| Feature | Peer-to-Peer | Client-Server |
|---|---|---|
| Architecture | Distributed | Service-oriented, often centralized |
| Dedicated server | Not required | Commonly used |
| Management | Often decentralized | Usually centralized |
| Scalability | Depends on design | Depends on server architecture |
| Example | Some file-sharing systems | Web applications |

---

# 20. Bandwidth, Throughput, and Latency

These three concepts are important for understanding network performance.

## 20.1 Bandwidth

Bandwidth refers to the maximum data-carrying capacity of a communication link.

It is commonly measured in bits per second.

Units:

- bps — bits per second.
- Kbps — kilobits per second.
- Mbps — megabits per second.
- Gbps — gigabits per second.

Example:

A network connection may have a bandwidth of 100 Mbps.

This does not guarantee that every application will receive 100 Mbps.

## 20.2 Throughput

Throughput is the actual rate at which data is successfully transferred over a network.

Throughput may be lower than bandwidth because of:

- Network congestion.
- Protocol overhead.
- Packet loss.
- Device limitations.
- Server limitations.
- Wireless interference.

Example:

A 100 Mbps connection may deliver an actual throughput of 75 Mbps.

## 20.3 Latency

Latency is the time required for data to travel from one point to another.

It is commonly measured in milliseconds (ms).

A common practical measurement is Round-Trip Time (RTT), which measures the time for a packet to reach a destination and for a response to return.

Example:

```text
Laptop ----> Server ----> Laptop
       20 ms RTT
```

Lower latency is generally better for interactive applications.

Examples:

- Online gaming.
- Video conferencing.
- Remote desktop.
- SSH sessions.

### Bandwidth vs Throughput vs Latency

| Term | Meaning | Example |
|---|---|---|
| Bandwidth | Maximum capacity | 100 Mbps |
| Throughput | Actual transfer rate | 75 Mbps |
| Latency | Time delay | 20 ms RTT |

### Important Analogy

Imagine a road:

- Bandwidth = Maximum number of vehicles the road can carry.
- Throughput = Number of vehicles actually passing per second.
- Latency = Time taken by a vehicle to reach its destination.

A high-bandwidth network does not necessarily have low latency.

---

# 21. Jitter and Packet Loss

## 21.1 Jitter

Jitter is the variation in packet delay.

For example, suppose packets arrive after these delays:

```text
Packet 1: 20 ms
Packet 2: 25 ms
Packet 3: 60 ms
Packet 4: 22 ms
```

The delay is not consistent.

This variation can cause problems in real-time applications.

Examples:

- Voice calls.
- Video conferencing.
- Online gaming.
- Live streaming.

### Reducing Jitter

Possible methods:

- Reduce network congestion.
- Use traffic prioritization.
- Improve network capacity.
- Use suitable buffering for real-time applications.

## 21.2 Packet Loss

Packet loss occurs when transmitted packets fail to reach their destination.

Possible causes:

- Network congestion.
- Faulty cables.
- Wireless interference.
- Hardware problems.
- Routing issues.
- Firewall filtering.

### Effects of Packet Loss

- Slower file transfers.
- Retransmissions in TCP.
- Audio or video glitches.
- Poor gaming performance.
- Interrupted communication.

### Packet Loss Example

Suppose 100 packets are sent, and 5 are lost.

\[
\text{Packet Loss Percentage}
=
\frac{5}{100}\times100
\]

\[
=5\%
\]

A 5% packet loss rate can be significant for many real-time applications.

---

# 22. Full-Duplex vs Half-Duplex Communication

Duplex communication describes whether devices can transmit and receive data simultaneously.

## 22.1 Simplex

Simplex communication allows data to travel in only one direction.

Example:

```text
Sender --------> Receiver
```

Traditional broadcast television is a common example of one-way communication.

## 22.2 Half-Duplex

Half-duplex communication allows both devices to transmit and receive, but not simultaneously.

Example:

```text
Device A <------> Device B

Only one side transmits at a time.
```

A walkie-talkie is a familiar example.

## 22.3 Full-Duplex

Full-duplex communication allows both devices to transmit and receive simultaneously.

Example:

```text
Device A <======> Device B

Both sides can transmit simultaneously.
```

Modern switched Ethernet links commonly operate in full-duplex mode.

### Comparison

| Mode | Communication Direction |
|---|---|
| Simplex | One direction only |
| Half-duplex | Both directions, one at a time |
| Full-duplex | Both directions simultaneously |

---

# 23. Unicast, Multicast, Broadcast, and Anycast

These terms describe how data is delivered to destinations.

## 23.1 Unicast

Unicast is one-to-one communication.

One sender transmits data to one destination.

```text
Sender --------> Receiver
```

Examples:

- A browser connecting to a web server.
- An SSH client connecting to a Linux server.

## 23.2 Broadcast

Broadcast is one-to-all communication within a broadcast domain.

```text
             [Sender]
             /  |  \
            /   |   \
          PC1  PC2  PC3
```

An IPv4 broadcast packet is intended for all hosts within the relevant broadcast domain.

Example:

```text
255.255.255.255
```

This is the IPv4 limited broadcast address.

Routers generally do not forward ordinary IPv4 broadcasts between networks.

IPv6 does not use broadcast; it uses multicast for similar group communication functions.

## 23.3 Multicast

Multicast is one-to-many communication to a specific group of interested receivers.

```text
             [Sender]
             /     \
           PC1     PC3

       PC2 is not in the group.
```

Examples:

- IPTV.
- Some streaming systems.
- Routing protocol communication.

Multicast is more selective than broadcast.

## 23.4 Anycast

Anycast is a communication method in which the same destination address is advertised from multiple locations, and routing delivers traffic to one of the available destinations, often the one considered nearest by routing policy.

```text
                [Client]
                   |
              [Anycast IP]
               /        \
          [Server A]  [Server B]
```

Anycast is commonly used in:

- DNS services.
- Content delivery networks.
- Distributed network services.

### Comparison

| Type | Communication Pattern |
|---|---|
| Unicast | One-to-one |
| Broadcast | One-to-all within a broadcast domain |
| Multicast | One-to-selected-group |
| Anycast | One-to-one of several possible destinations |

---

# 24. Circuit Switching vs Packet Switching

## 24.1 Circuit Switching

Circuit switching establishes a dedicated communication path between two endpoints for the duration of a communication session.

Example:

Traditional telephone networks commonly used circuit switching.

### Characteristics

- Dedicated path.
- Resources may be reserved.
- Predictable performance after setup.
- Connection setup may be required.
- Inefficient when the reserved path is idle.

### Example

```text
A ===== Dedicated Circuit ===== B
```

## 24.2 Packet Switching

Packet switching divides data into packets.

Each packet is forwarded through a network using routing and forwarding mechanisms.

Packets may share network links with traffic from other users.

The Internet primarily uses packet switching.

### Characteristics

- Data is divided into packets.
- Network resources are shared.
- Packets may follow different paths.
- Efficient use of network capacity.
- Congestion and variable delay may occur.

### Example

```text
             +---- Router B ----+
             |                  |
Sender ---- Router A          Router D ---- Receiver
             |                  |
             +---- Router C ----+
```

Packets may take different paths through the network.

### Comparison

| Feature | Circuit Switching | Packet Switching |
|---|---|---|
| Path | Dedicated communication path | Packets are forwarded through shared infrastructure |
| Resource use | May reserve resources | Resources are shared |
| Delay | Often predictable after setup | May vary |
| Efficiency | Can waste reserved capacity | Efficient for bursty traffic |
| Example | Traditional telephone circuit | Internet |

### Important Point

Packet switching is a fundamental concept behind the Internet.

---

# 25. What is a Network Packet?

A network packet is a formatted unit of data carried by a network-layer protocol.

For example, an IPv4 or IPv6 packet contains:

- A header.
- Payload data.
- Additional fields depending on the protocol.

The header contains information needed for delivery and processing.

An IPv4 header may include:

- Source IP address.
- Destination IP address.
- TTL (Time to Live).
- Protocol identifier.
- Header length.
- Total length.

### Example

Suppose a computer sends data to a web server.

The IP packet may contain:

```text
Source IP:      192.168.1.10
Destination IP: 93.184.216.34
Protocol:       TCP
Payload:        TCP segment
```

The actual addresses and values depend on the connection.

### Why Packets Matter

Packets allow network communication to be:

- Divided into manageable units.
- Forwarded across routers.
- Shared across communication links.
- Monitored and analyzed.
- Processed by network devices.

### Cybersecurity Relevance

Packet analysis is a fundamental cybersecurity skill.

Tools such as Wireshark and tcpdump allow security professionals to inspect network traffic.

Packet analysis can help identify:

- Suspicious communication.
- Unexpected DNS queries.
- Unencrypted credentials.
- Unusual connection attempts.
- Malware communication patterns.

Only inspect networks and traffic that you are authorized to monitor.

---

# 26. Frames, Packets, Segments, and Datagrams

Networking uses different names for data units at different layers.

## 26.1 Application Data

Application protocols generate the data that needs to be transmitted.

Examples:

- HTTP request.
- DNS query.
- SSH data.

## 26.2 TCP Segment

TCP divides application data into units commonly called segments.

A TCP segment contains:

- TCP header.
- TCP payload.

The TCP header includes information such as:

- Source port.
- Destination port.
- Sequence number.
- Acknowledgment number.
- Flags.
- Window size.

TCP provides reliable, ordered byte-stream communication.

## 26.3 UDP Datagram

UDP carries data in units called datagrams.

A UDP datagram contains:

- UDP header.
- UDP payload.

The UDP header includes:

- Source port.
- Destination port.
- Length.
- Checksum.

UDP does not provide TCP-style reliable delivery, retransmission, or ordering guarantees.

## 26.4 IP Packet

An IP packet contains:

- IP header.
- Payload.

The payload may contain a TCP segment, UDP datagram, or another IP-supported protocol.

## 26.5 Ethernet Frame

An Ethernet frame contains:

- Ethernet header.
- Payload.
- Frame Check Sequence (FCS), where applicable.

The Ethernet header commonly includes:

- Destination MAC address.
- Source MAC address.
- EtherType or length information.

### Encapsulation

As data moves down the network stack, each layer adds its own header.

```text
Application Data
       |
       v
+----------------------+
| TCP Header           |
| Application Data     |
+----------------------+
       |
       v
+----------------------+
| IP Header            |
| TCP Segment          |
+----------------------+
       |
       v
+----------------------+
| Ethernet Header      |
| IP Packet            |
| Ethernet Trailer     |
+----------------------+
```

This process is called **encapsulation**.

At the receiving device, headers are processed and removed as the data moves upward through the network stack. This is called **decapsulation**.

### Important Terminology

| Layer | Data Unit |
|---|---|
| Application | Data or message |
| Transport — TCP | Segment |
| Transport — UDP | Datagram |
| Network — IP | Packet |
| Data Link — Ethernet | Frame |
| Physical | Bits or symbols |

### Important Note

The terms "packet" and "datagram" are sometimes used more broadly in networking literature. The table shows the common terminology used when learning TCP/IP encapsulation.

---

# 27. Practical Networking Tasks

These exercises help you understand the network configuration of your own computer.

You can perform them on Windows or Kali Linux.

## Practical 1: Identify Your Network Interface

A network interface is the component through which your device connects to a network.

Examples:

- Ethernet adapter.
- Wi-Fi adapter.
- Virtual network adapter.

### Windows

Open PowerShell or Command Prompt.

Run:

```powershell
ipconfig /all
```

Look for entries such as:

```text
Wireless LAN adapter Wi-Fi
Ethernet adapter Ethernet
```

### Kali Linux

Run:

```bash
ip link
```

Or:

```bash
ip -br link
```

Example output:

```text
lo        UNKNOWN
eth0      UP
wlan0     UP
```

Common interface names:

| Interface | Meaning |
|---|---|
| lo | Loopback interface |
| eth0 | Ethernet interface, common in some systems |
| wlan0 | Wireless interface, common in some systems |
| enp0s3 | Ethernet interface using predictable naming |
| wlp2s0 | Wireless interface using predictable naming |

Interface names vary by operating system and hardware.

---

## Practical 2: Check Your Current IP Address

An IP address is a logical address used to identify an interface within an IP network.

### Windows

Run:

```powershell
ipconfig
```

Look for:

```text
IPv4 Address
```

Example:

```text
IPv4 Address: 192.168.1.10
```

### Kali Linux

Run:

```bash
ip addr
```

Or:

```bash
ip -br addr
```

Example:

```text
eth0    UP    192.168.1.10/24
```

Here:

- `192.168.1.10` is the IPv4 address.
- `/24` indicates the network prefix length.

The `/24` prefix corresponds to the subnet mask:

```text
255.255.255.0
```

### Check Your Public IP Address

Your private IP address is not necessarily the same as your public IP address.

You can check the public IP address shown by an external service using:

```bash
curl https://api.ipify.org
```

This sends a request to an external service.

Note that the public address observed by an external service may belong to a NAT gateway, VPN, proxy, or other upstream device rather than your individual computer.

---

## Practical 3: Identify Your Default Gateway

A default gateway is the router or next-hop device used to forward traffic when no more specific route matches the destination.

### Windows

Run:

```powershell
ipconfig
```

Look for:

```text
Default Gateway
```

Example:

```text
Default Gateway: 192.168.1.1
```

You can also run:

```powershell
route print
```

Look for the IPv4 default route:

```text
0.0.0.0
```

### Kali Linux

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev eth0
```

This means:

- `default` = Default route.
- `via 192.168.1.1` = Next-hop gateway.
- `dev eth0` = Interface used for the route.

### Verify Gateway Connectivity

Run:

```bash
ping 192.168.1.1
```

Replace the address with your actual gateway.

---

## Practical 4: Compare Wi-Fi and Ethernet

You can compare the network interfaces available on your computer.

### Windows

Run:

```powershell
Get-NetAdapter
```

Example:

```text
Name       InterfaceDescription       Status
----       --------------------       ------
Wi-Fi      Wireless Network Adapter   Up
Ethernet   Ethernet Adapter            Up
```

Check the interface speeds:

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed
```

### Kali Linux

Run:

```bash
ip -br link
```

To check Wi-Fi information:

```bash
iw dev
```

To inspect an Ethernet interface's link speed, use:

```bash
sudo ethtool eth0
```

Replace `eth0` with the correct interface name.

Look for:

```text
Speed: 1000Mb/s
Duplex: Full
```

The reported speed depends on the adapter and connection.

### What to Observe

Compare:

- Connection status.
- Interface type.
- Link speed.
- Signal strength, for Wi-Fi.
- Stability.
- Latency.
- Packet loss.

A wired Ethernet connection is often more stable, while Wi-Fi provides mobility.

---

## Practical 5: Observe Latency Using Ping

The `ping` command is used to test IP connectivity and measure round-trip time.

It commonly uses ICMP Echo Request and Echo Reply messages.

### Windows

Run:

```powershell
ping 8.8.8.8
```

Example output:

```text
Reply from 8.8.8.8:
time=20ms
```

To send a specific number of requests:

```powershell
ping -n 10 8.8.8.8
```

### Kali Linux

Run:

```bash
ping 8.8.8.8
```

Stop the command using:

```text
Ctrl + C
```

To send 10 packets:

```bash
ping -c 10 8.8.8.8
```

### Observe the Results

Look for:

- Minimum latency.
- Average latency.
- Maximum latency.
- Packet loss.

Example:

```text
10 packets transmitted
10 packets received
0% packet loss
```

### Test Your Default Gateway

```bash
ping 192.168.1.1
```

### Test an Internet Destination

```bash
ping 8.8.8.8
```

### Test DNS Resolution

```bash
ping google.com
```

If pinging an IP address works but pinging a domain name fails, DNS resolution may be a problem.

However, ICMP traffic may be blocked or deprioritized, so ping failure does not automatically mean the destination is unavailable.

---

# 28. Practical Lab Worksheet

Use this worksheet to record your observations.

| Task | Your Observation |
|---|---|
| Operating system | |
| Active network interface | |
| Interface type | |
| Private IPv4 address | |
| Subnet prefix | |
| Default gateway | |
| DNS server | |
| Wi-Fi or Ethernet | |
| Link speed | |
| Average ping latency | |
| Packet loss percentage | |

### Questions to Answer

1. What is the difference between an IP address and a MAC address?
2. What is the purpose of a default gateway?
3. Why does a switch use MAC addresses?
4. Why does a router use IP addresses?
5. What is the difference between a LAN and a WAN?
6. What is the difference between bandwidth and throughput?
7. Why is low latency important for online gaming?
8. What is the difference between a TCP segment and an IP packet?
9. What is the purpose of encapsulation?
10. Why is networking knowledge important for cybersecurity?

---

# 29. Key Takeaways

- A computer network connects devices to exchange information and share resources.
- Network devices include NICs, switches, routers, access points, and firewalls.
- Hosts are network-connected devices; clients request services, and servers provide them.
- Network protocols define how devices communicate.
- LANs cover limited areas, while WANs connect networks over larger geographical areas.
- WLANs use wireless communication, commonly Wi-Fi.
- Network topology describes the physical or logical arrangement of a network.
- Bandwidth is capacity, throughput is actual transfer rate, and latency is delay.
- Jitter is variation in packet delay.
- Packet loss occurs when packets fail to reach their destination.
- Unicast, broadcast, multicast, and anycast describe different delivery patterns.
- The Internet primarily uses packet switching.
- Encapsulation adds headers as data moves down the network stack.
- Frames, packets, TCP segments, and UDP datagrams are data units associated with different layers.
- Understanding networking is essential for web security, penetration testing, and defensive security.

---

# 30. Further Reading

- [Computer Networking — RFC Editor](https://www.rfc-editor.org/)
- [IETF — Internet Engineering Task Force](https://www.ietf.org/)
- [IEEE — Ethernet and Wi-Fi Standards](https://standards.ieee.org/)
- [Cloudflare Learning Center — What is a Network?](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-network/)
- [Wireshark — Official Documentation](https://www.wireshark.org/docs/)
- [Linux `ip` Command Manual](https://man7.org/linux/man-pages/man8/ip.8.html)
- [Linux `ping` Command Manual](https://man7.org/linux/man-pages/man8/ping.8.html)

---

**End of Topic 1: Introduction to Computer Networking**
