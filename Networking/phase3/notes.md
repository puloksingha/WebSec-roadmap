
# Phase 3: IP Addressing

# 4. IPv4 Fundamentals

## Table of Contents

1. What Is an IP Address?
2. IPv4 Address Structure
3. Binary and Decimal Representation
4. Network Portion vs Host Portion
5. Public vs Private IPv4 Addresses
6. Private IPv4 Address Ranges
7. Loopback Addresses
8. Link-Local Addresses
9. Unspecified Address — 0.0.0.0
10. Limited Broadcast Address
11. Static vs Dynamic IP Addressing
12. IP Address Conflicts
13. Network Address and Broadcast Address
14. Reserved IPv4 Addresses
15. NAT and Private Addressing
16. Why Internal IPs Are Not Generally Routable on the Public Internet
17. Practical IPv4 Exercises
18. Practical Commands
19. Cybersecurity Applications
20. Interview Questions
21. Key Takeaways

---

# 1. What Is an IP Address?

## 1.1 Definition

An **Internet Protocol (IP) address** is a logical numerical address assigned to a network interface to identify it within an IP network.

IP addresses help devices communicate with one another across local networks and interconnected networks such as the Internet.

An IP address is used by the Internet Protocol to determine where a packet should be delivered.

For example:

```text
192.168.1.10
```

This is an IPv4 address.

Another example:

```text
2001:db8::10
```

This is an IPv6 address.

There are two major versions of the Internet Protocol:

| Version | Address Size | Example |
|---|---|---|
| IPv4 | 32 bits | 192.168.1.10 |
| IPv6 | 128 bits | 2001:db8::10 |

IPv4 is still widely used, especially in local networks and Internet communication.

## 1.2 Why Do We Need IP Addresses?

IP addresses are necessary for logical network communication.

They help:

- Identify network interfaces.
- Locate devices within IP networks.
- Route packets between networks.
- Distinguish source and destination endpoints.
- Enable communication between different networks.

Example:

```text
Computer A                         Computer B

192.168.1.10                       192.168.1.20
     |                                  |
     +---------- Local Network ---------+
```

Computer A can send an IP packet to Computer B using its destination IP address.

## 1.3 IP Address vs MAC Address

| IP Address | MAC Address |
|---|---|
| Logical network address | Link-layer address |
| Used for IP communication and routing | Used for local link delivery |
| Can change when network configuration changes | Usually associated with a network interface |
| IPv4 uses 32 bits | Ethernet MAC commonly uses 48 bits |
| Operates at OSI Layer 3 | Operates at OSI Layer 2 |

Example:

```text
IP Address:
192.168.1.10

MAC Address:
00:1A:2B:3C:4D:5E
```

**Important:** An IP address identifies an IP endpoint or interface in a network context. It does not necessarily identify a physical device permanently.

---

# 2. IPv4 Address Structure

## 2.1 Definition

IPv4 stands for Internet Protocol version 4.

An IPv4 address is a 32-bit logical address.

It contains 32 binary digits, also called bits.

Example in binary:

```text
11000000 10101000 00000001 00001010
```

The same address in decimal notation is:

```text
192.168.1.10
```

## 2.2 IPv4 Address Format

IPv4 addresses are commonly written in dotted-decimal notation.

A 32-bit address is divided into four groups of 8 bits.

Each group is called an octet.

```text
192       . 168       . 1         . 10
|           |           |           |
Octet 1     Octet 2     Octet 3     Octet 4
```

Each octet contains 8 bits.

```text
8 + 8 + 8 + 8 = 32 bits
```

## 2.3 IPv4 Address Range

An IPv4 address contains 32 bits.

Therefore, the total number of possible IPv4 bit patterns is:

\[
2^{32}=4,294,967,296
\]

The theoretical address range is:

```text
0.0.0.0
```

to:

```text
255.255.255.255
```

Not all addresses are available for ordinary host assignment.

Some are reserved for:

- Private networks.
- Loopback.
- Multicast.
- Broadcast.
- Documentation.
- Special protocol purposes.

## 2.4 Important Octet Values

An octet contains 8 bits.

Its minimum value is:

\[
00000000_2=0
\]

Its maximum value is:

\[
11111111_2=255
\]

Therefore, each IPv4 octet ranges from 0 to 255.

An address such as:

```text
192.168.1.256
```

is invalid because the final octet exceeds 255.

---

# 3. Binary and Decimal Representation

## 3.1 What Is Binary?

Binary is a number system that uses only two digits:

```text
0 and 1
```

Computers use binary to represent information.

Each binary digit is called a bit.

The decimal number system uses base 10.

The binary number system uses base 2.

## 3.2 Binary Place Values

An 8-bit octet has the following place values:

| Bit Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Place Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Each position represents a power of 2.

\[
2^7,2^6,2^5,2^4,2^3,2^2,2^1,2^0
\]

## 3.3 Binary to Decimal Conversion

Consider:

```text
11000000
```

The bits represent:

| Bit | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Add the values where the bit is 1.

\[
128+64=192
\]

Therefore:

```text
11000000 = 192
```

## 3.4 Another Example

Convert:

```text
10101000
```

The active bit values are:

\[
128+32+8=168
\]

Therefore:

```text
10101000 = 168
```

## 3.5 Complete IPv4 Conversion Example

Convert the following IPv4 address into binary:

```text
192.168.1.10
```

### Octet 1

```text
192 = 128 + 64
```

Binary:

```text
11000000
```

### Octet 2

```text
168 = 128 + 32 + 8
```

Binary:

```text
10101000
```

### Octet 3

```text
1 = 1
```

Binary:

```text
00000001
```

### Octet 4

```text
10 = 8 + 2
```

Binary:

```text
00001010
```

### Final Answer

```text
Decimal:
192.168.1.10

Binary:
11000000.10101000.00000001.00001010
```

## 3.6 Binary to Decimal Shortcut

Remember these values:

```text
128 64 32 16 8 4 2 1
```

For example:

```text
11110000
```

\[
128+64+32+16=240
\]

Therefore:

```text
11110000 = 240
```

## 3.7 Decimal to Binary Shortcut

To convert decimal to binary:

1. Identify the largest power of 2 that does not exceed the number.
2. Subtract that value.
3. Repeat until the remainder becomes zero.
4. Place 1 in the positions used and 0 in the others.

Example: Convert 25 into binary.

```text
25 - 16 = 9
9 - 8 = 1
1 - 1 = 0
```

Active values:

```text
16, 8, 1
```

Therefore:

```text
25 = 00011001
```

---

# 4. Network Portion vs Host Portion

## 4.1 Definition

An IPv4 address is divided into two logical portions:

1. Network portion.
2. Host portion.

The network portion identifies the IP network.

The host portion identifies an interface within that network.

The division is determined by the subnet mask or prefix length.

Example:

```text
IP Address:
192.168.1.10

Subnet Mask:
255.255.255.0

Prefix:
 /24
```

The first 24 bits represent the network portion.

The remaining 8 bits represent the host portion.

## 4.2 Network and Host Bits

```text
192.168.1.10/24
```

Binary:

```text
11000000.10101000.00000001.00001010
```

A `/24` prefix means:

```text
Network Bits = 24
Host Bits    = 8
```

Conceptually:

```text
+---------------------------+----------+
| Network Portion           | Host     |
| 24 bits                   | 8 bits   |
+---------------------------+----------+
```

## 4.3 What Is a Subnet Mask?

A subnet mask identifies which bits belong to the network portion and which bits belong to the host portion.

Example:

```text
255.255.255.0
```

Binary:

```text
11111111.11111111.11111111.00000000
```

The 1 bits indicate the network portion.

The 0 bits indicate the host portion.

## 4.4 Common Subnet Masks

| CIDR Prefix | Subnet Mask | Network Bits | Host Bits |
|---|---|---|---|
| /8 | 255.0.0.0 | 8 | 24 |
| /16 | 255.255.0.0 | 16 | 16 |
| /24 | 255.255.255.0 | 24 | 8 |
| /25 | 255.255.255.128 | 25 | 7 |
| /26 | 255.255.255.192 | 26 | 6 |
| /27 | 255.255.255.224 | 27 | 5 |
| /28 | 255.255.255.240 | 28 | 4 |
| /29 | 255.255.255.248 | 29 | 3 |
| /30 | 255.255.255.252 | 30 | 2 |
| /32 | 255.255.255.255 | 32 | 0 |

## 4.5 What Is CIDR?

CIDR stands for Classless Inter-Domain Routing.

CIDR represents an IP network using a prefix length.

Example:

```text
192.168.1.0/24
```

The `/24` indicates that the first 24 bits are the network prefix.

CIDR allows networks to be divided into different sizes instead of relying on traditional fixed address classes.

## 4.6 Host Calculation

For an ordinary IPv4 subnet:

\[
\text{Host Bits}=32-\text{Prefix Length}
\]

The number of addresses is:

\[
2^{\text{Host Bits}}
\]

For a conventional subnet with a network address and broadcast address:

\[
\text{Usable Hosts}=2^{\text{Host Bits}}-2
\]

Example:

```text
192.168.1.0/24
```

Host bits:

\[
32-24=8
\]

Total addresses:

\[
2^8=256
\]

Usable host addresses:

\[
256-2=254
\]

The subtraction of 2 applies to conventional IPv4 subnets such as `/24`. Special cases include `/31` point-to-point links and `/32` host routes.

---

# 5. Public vs Private IPv4 Addresses

## 5.1 Public IPv4 Address

A public IPv4 address is an address that can be globally routed on the public Internet, subject to routing policy and special-purpose reservations.

Public IP addresses are commonly used by:

- Internet-facing web servers.
- Public DNS servers.
- Cloud infrastructure.
- Internet service providers.
- Public network services.

Example:

```text
8.8.8.8
```

This is a globally reachable public DNS resolver address.

Not every address outside the private ranges is necessarily globally usable.

Some public-looking addresses are reserved for special purposes.

## 5.2 Private IPv4 Address

Private IPv4 addresses are reserved for use within private networks.

They are commonly used in:

- Home networks.
- Office networks.
- College networks.
- Enterprise networks.
- Virtual machines.
- Internal cloud networks.

Private IPv4 addresses are not generally routed across the public Internet.

Example:

```text
192.168.1.10
```

A laptop may use this address within its home network.

## 5.3 Public vs Private Comparison

| Feature | Public IPv4 | Private IPv4 |
|---|---|---|
| Internet routing | Globally routable when properly assigned | Not generally routed on the public Internet |
| Assignment | Usually through an ISP or address allocation | Locally assigned or provided by DHCP |
| Common use | Public-facing services | Internal networks |
| NAT requirement | Not inherently required | Often uses NAT for Internet access |
| Example | 8.8.8.8 | 192.168.1.10 |

## 5.4 Important Concept

A device with a private IP address can access the Internet.

For example:

```text
Laptop
192.168.1.10
     |
     v
Router
192.168.1.1
     |
     v
Public Internet
```

The router may translate the laptop's private IP address into a public IP address using NAT.

The laptop does not need its own public IPv4 address to access the Internet.

---

# 6. Private IPv4 Address Ranges

RFC 1918 defines three private IPv4 address blocks.

These are reserved for private internets.

## 6.1 Private Range 1 — 10.0.0.0/8

Range:

```text
10.0.0.0 - 10.255.255.255
```

CIDR:

```text
10.0.0.0/8
```

Subnet mask:

```text
255.0.0.0
```

Total addresses:

\[
2^{24}=16,777,216
\]

This range is commonly used in:

- Large enterprise networks.
- Cloud networks.
- Corporate environments.
- Large internal address spaces.

Example:

```text
10.10.20.30
```

This is a private IPv4 address.

## 6.2 Private Range 2 — 172.16.0.0/12

Range:

```text
172.16.0.0 - 172.31.255.255
```

CIDR:

```text
172.16.0.0/12
```

Subnet mask:

```text
255.240.0.0
```

Total addresses:

\[
2^{20}=1,048,576
\]

This range is often used in:

- Corporate networks.
- Internal server networks.
- Cloud infrastructure.
- Segmented enterprise networks.

Example:

```text
172.20.10.5
```

This is a private IPv4 address.

### Important

Not every address beginning with `172` is private.

Only the range:

```text
172.16.0.0 - 172.31.255.255
```

is part of the RFC 1918 private address space.

For example:

```text
172.15.1.1
```

is not within the RFC 1918 private range.

Neither is:

```text
172.32.1.1
```

## 6.3 Private Range 3 — 192.168.0.0/16

Range:

```text
192.168.0.0 - 192.168.255.255
```

CIDR:

```text
192.168.0.0/16
```

Subnet mask:

```text
255.255.0.0
```

Total addresses:

\[
2^{16}=65,536
\]

This range is commonly used in:

- Home Wi-Fi networks.
- Small office networks.
- Local labs.
- Virtual machines.

Example:

```text
192.168.1.10
```

This is a private IPv4 address.

## 6.4 Private IPv4 Range Summary

| Private Block | Address Range | Prefix | Total Addresses |
|---|---|---|---:|
| 10/8 | 10.0.0.0 – 10.255.255.255 | /8 | 16,777,216 |
| 172.16/12 | 172.16.0.0 – 172.31.255.255 | /12 | 1,048,576 |
| 192.168/16 | 192.168.0.0 – 192.168.255.255 | /16 | 65,536 |

## 6.5 How to Identify a Private IPv4 Address

Check whether the address belongs to one of these ranges:

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

Example:

```text
10.5.6.7       -> Private
172.20.5.10    -> Private
192.168.1.100  -> Private
8.8.8.8        -> Public
```

---

# 7. Loopback Addresses — 127.0.0.0/8

## 7.1 Definition

The loopback address range is:

```text
127.0.0.0/8
```

Range:

```text
127.0.0.0 - 127.255.255.255
```

The most commonly used loopback address is:

```text
127.0.0.1
```

It is commonly called localhost.

## 7.2 Purpose

Loopback allows a computer to communicate with itself through its own IP networking stack.

Traffic sent to a loopback address does not travel over the physical network.

Example:

```bash
ping 127.0.0.1
```

This tests the local IP stack.

## 7.3 Localhost

The hostname:

```text
localhost
```

commonly resolves to:

```text
127.0.0.1
```

It may also resolve to the IPv6 loopback address:

```text
::1
```

## 7.4 Practical Example

Suppose you start a Python web server:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

You can access it using:

```text
http://127.0.0.1:8000
```

The service is bound to the loopback interface.

Other computers generally cannot reach it through the machine's ordinary network interface.

## 7.5 Cybersecurity Relevance

Loopback addresses are important when testing local services.

Examples:

- Local development servers.
- Local APIs.
- Internal application testing.
- Local proxy services.

A service listening only on `127.0.0.1` is generally not directly accessible from another machine.

However, local-only services may still be relevant to security issues such as Server-Side Request Forgery (SSRF).

---

# 8. Link-Local Addresses — 169.254.0.0/16

## 8.1 Definition

The IPv4 link-local address range is:

```text
169.254.0.0/16
```

Range:

```text
169.254.0.0 - 169.254.255.255
```

These addresses are used for communication on a local link when appropriate configuration is unavailable.

They are commonly associated with IPv4 Address Conflict Detection and Automatic Private IP Addressing (APIPA).

## 8.2 Why Does a Device Get a Link-Local Address?

Suppose a computer is configured to obtain an IP address using DHCP.

If it cannot obtain a suitable address, it may automatically assign itself a link-local address.

Example:

```text
169.254.25.10
```

This may indicate that DHCP configuration failed.

It is not always proof of a network failure, because link-local communication can be intentional.

## 8.3 Important Properties

Link-local IPv4 addresses:

- Are not intended for public Internet routing.
- Are limited to the local link.
- Can support communication between devices on the same link.
- May be automatically assigned when DHCP configuration fails.

## 8.4 Practical Troubleshooting

If your computer receives an address such as:

```text
169.254.10.20
```

Check:

1. Is the Wi-Fi connected?
2. Is the Ethernet cable connected?
3. Is the DHCP server available?
4. Is the network adapter functioning?
5. Is the device connected to the correct network?

---

# 9. Unspecified Address — 0.0.0.0

## 9.1 Definition

The address:

```text
0.0.0.0
```

is the IPv4 unspecified address.

It represents an unspecified or unknown IPv4 address in contexts where an ordinary assigned address is not yet available.

## 9.2 Common Uses

### Use 1: DHCP

A device without a configured IPv4 address may use:

```text
0.0.0.0
```

as its source address during DHCP initialization.

### Use 2: Binding a Server

A server application may bind to:

```text
0.0.0.0
```

This generally means it listens on all available local IPv4 interfaces.

Example:

```bash
python -m http.server 8000 --bind 0.0.0.0
```

This server may be accessible through:

- 127.0.0.1.
- The machine's LAN IPv4 address.
- Other configured IPv4 interfaces.

Accessibility still depends on firewall rules and network configuration.

### Use 3: Default Route

The destination prefix:

```text
0.0.0.0/0
```

represents the IPv4 default route.

It matches any IPv4 destination address.

A router uses the default route when no more specific matching route is available.

## 9.3 Important Difference

```text
0.0.0.0
```

and:

```text
0.0.0.0/0
```

are not interchangeable.

The first is an IPv4 address.

The second is a network prefix representing all IPv4 addresses.

---

# 10. Limited Broadcast Address — 255.255.255.255

## 10.1 Definition

The limited broadcast address is:

```text
255.255.255.255
```

It is used to send an IPv4 broadcast packet to the local network context.

## 10.2 Purpose

Broadcast communication allows a sender to transmit a packet intended for all applicable hosts on the local network.

Example:

```text
Computer A
     |
     v
Local Network
  /    |    \
 PC1   PC2   PC3
```

A broadcast packet can be delivered to all hosts on the relevant broadcast domain.

## 10.3 Limited Broadcast vs Directed Broadcast

### Limited Broadcast

```text
255.255.255.255
```

It is limited to the local network context and is not forwarded by routers.

### Directed Broadcast

A directed broadcast is the broadcast address of a particular IPv4 subnet.

Example:

```text
192.168.1.255
```

For the subnet:

```text
192.168.1.0/24
```

The directed broadcast address is:

```text
192.168.1.255
```

Routers generally do not forward directed broadcasts by default because of security concerns.

---

# 11. Static vs Dynamic IP Addressing

## 11.1 Static IP Addressing

A static IP address is configured manually or assigned through a persistent reservation.

Example:

```text
IP Address:      192.168.1.10
Subnet Mask:     255.255.255.0
Default Gateway: 192.168.1.1
DNS Server:      192.168.1.1
```

The address remains the same until the configuration is changed.

## 11.2 Advantages of Static IP Addressing

- Predictable address.
- Useful for servers.
- Useful for network infrastructure.
- Easier to configure certain firewall rules.
- Useful for services requiring stable addressing.

## 11.3 Disadvantages of Static IP Addressing

- Requires manual configuration or management.
- Incorrect settings can cause connectivity problems.
- Duplicate addresses can create conflicts.
- Can become difficult to manage in large networks.

## 11.4 Dynamic IP Addressing

Dynamic IP addressing is commonly performed using DHCP.

DHCP stands for:

**Dynamic Host Configuration Protocol**

A DHCP server can provide:

- IPv4 address.
- Subnet mask.
- Default gateway.
- DNS server addresses.
- Lease duration.
- Other network configuration options.

## 11.5 DHCP DORA Process

DHCP commonly uses a four-step process called DORA.

```text
D = Discover
O = Offer
R = Request
A = Acknowledge
```

### Step 1 — DHCP Discover

The client searches for a DHCP server.

### Step 2 — DHCP Offer

The server offers an IP address and configuration.

### Step 3 — DHCP Request

The client requests the offered configuration.

### Step 4 — DHCP Acknowledge

The server confirms the lease.

Diagram:

```text
Client                         DHCP Server
  |                                |
  | ------ Discover -------------> |
  |                                |
  | <------ Offer ---------------- |
  |                                |
  | ------ Request --------------> |
  |                                |
  | <------ Acknowledge ---------- |
  |                                |
  |       IP Configured            |
```

The exact packet flow can vary depending on the DHCP environment.

## 11.6 DHCP Lease

A DHCP lease is a temporary assignment of an IP address.

The client typically renews the lease before it expires.

Example:

```text
IP Address: 192.168.1.20
Lease Time: 24 Hours
```

The address may remain the same across renewals, but DHCP does not universally guarantee that it will.

## 11.7 Static vs Dynamic Comparison

| Feature | Static | Dynamic |
|---|---|---|
| Assignment | Manual or persistent reservation | DHCP or another automatic mechanism |
| Address stability | Usually fixed | May change |
| Management | More manual unless centrally managed | Easier for large client networks |
| Common use | Servers, infrastructure | Laptops, phones, client devices |
| Risk | Configuration mistakes and duplicates | DHCP failures or lease issues |

**Important:** A DHCP reservation is still DHCP-based addressing, but the server is configured to consistently provide a particular address to a client.

---

# 12. IP Address Conflicts

## 12.1 Definition

An IP address conflict occurs when two or more network interfaces use the same IPv4 address within the same relevant network.

This can cause communication problems.

## 12.2 Example

```text
Computer A:
192.168.1.10

Computer B:
192.168.1.10
```

Both computers use the same IP address.

Other devices may not know which computer should receive packets intended for that address.

## 12.3 Common Causes

- Two devices manually configured with the same address.
- A static address overlapping with the DHCP pool.
- DHCP server misconfiguration.
- Incorrect network cloning.
- Virtual machine network configuration errors.
- Duplicate IP assignments.

## 12.4 Symptoms

- Intermittent connectivity.
- Network warnings.
- Unexpected packet delivery.
- Connection failures.
- Devices losing access to network resources.

## 12.5 How to Prevent IP Conflicts

- Use DHCP for ordinary client devices.
- Maintain a documented IP address plan.
- Avoid overlapping static and dynamic address assignments.
- Use DHCP reservations where appropriate.
- Configure subnet masks correctly.
- Check for duplicate addresses before assigning static IPs.

## 12.6 Troubleshooting Commands

### Windows

```powershell
ipconfig /all
```

Renew DHCP configuration:

```powershell
ipconfig /release
ipconfig /renew
```

Clear the local DNS cache:

```powershell
ipconfig /flushdns
```

Note that flushing DNS does not resolve an IP address conflict.

### Linux

```bash
ip addr
```

Inspect neighbor information:

```bash
ip neigh
```

Check for address conflicts on a local Ethernet network using `arping` where available:

```bash
sudo arping -D -I eth0 192.168.1.10
```

Replace `eth0` and the IP address with the correct interface and address for your network.

---

# 13. Network Address and Broadcast Address

## 13.1 Network Address

The network address identifies an IPv4 subnet.

It is obtained by performing a bitwise AND operation between the IP address and subnet mask.

Example:

```text
IP Address:
192.168.1.10

Subnet Mask:
255.255.255.0
```

Network address:

```text
192.168.1.0
```

## 13.2 Broadcast Address

The broadcast address is the highest address in a conventional IPv4 subnet.

It is used to send broadcast traffic to the subnet.

For:

```text
192.168.1.0/24
```

The broadcast address is:

```text
192.168.1.255
```

## 13.3 Host Range

For the subnet:

```text
192.168.1.0/24
```

| Property | Address |
|---|---|
| Network address | 192.168.1.0 |
| First usable host | 192.168.1.1 |
| Last usable host | 192.168.1.254 |
| Broadcast address | 192.168.1.255 |
| Total addresses | 256 |
| Conventional usable hosts | 254 |

## 13.4 Binary Explanation

IP address:

```text
192.168.1.10
```

Binary:

```text
11000000.10101000.00000001.00001010
```

Subnet mask:

```text
255.255.255.0
```

Binary:

```text
11111111.11111111.11111111.00000000
```

Perform bitwise AND:

```text
IP:
11000000.10101000.00000001.00001010

Mask:
11111111.11111111.11111111.00000000

Result:
11000000.10101000.00000001.00000000
```

The result is:

```text
192.168.1.0
```

## 13.5 Finding the Broadcast Address

For a conventional subnet, set all host bits to 1.

For:

```text
192.168.1.0/24
```

Host bits:

```text
00000000
```

Set all host bits to 1:

```text
11111111
```

Decimal:

```text
255
```

Broadcast address:

```text
192.168.1.255
```

## 13.6 Example: /26 Subnet

Given:

```text
192.168.1.70/26
```

A `/26` subnet has:

```text
Network Bits = 26
Host Bits = 6
```

Total addresses:

\[
2^6=64
\]

Conventional usable hosts:

\[
64-2=62
\]

The subnet mask is:

```text
255.255.255.192
```

The block size is:

\[
256-192=64
\]

The subnet ranges in the final octet are:

```text
0 - 63
64 - 127
128 - 191
192 - 255
```

The address `192.168.1.70` falls within:

```text
64 - 127
```

Therefore:

| Property | Value |
|---|---|
| Network address | 192.168.1.64 |
| First usable host | 192.168.1.65 |
| Last usable host | 192.168.1.126 |
| Broadcast address | 192.168.1.127 |
| Total addresses | 64 |
| Conventional usable hosts | 62 |

---

# 14. Reserved IPv4 Addresses

Some IPv4 addresses and ranges are reserved for special purposes.

They are not all ordinary public or private host addresses.

## 14.1 Important Reserved Ranges

| Address / Range | Purpose |
|---|---|
| 0.0.0.0/8 | "This network" / special-purpose source contexts |
| 0.0.0.0 | Unspecified address |
| 10.0.0.0/8 | RFC 1918 private addressing |
| 127.0.0.0/8 | Loopback |
| 169.254.0.0/16 | Link-local |
| 172.16.0.0/12 | RFC 1918 private addressing |
| 192.168.0.0/16 | RFC 1918 private addressing |
| 192.0.2.0/24 | Documentation |
| 198.51.100.0/24 | Documentation |
| 203.0.113.0/24 | Documentation |
| 224.0.0.0/4 | IPv4 multicast |
| 240.0.0.0/4 | Reserved for future use / special-purpose status |
| 255.255.255.255 | Limited broadcast |

Special-purpose ranges may have specific routing rules and exceptions. Consult the IANA IPv4 Special-Purpose Address Registry when exact behavior matters.

## 14.2 Documentation Addresses

The following ranges are reserved for documentation and examples:

```text
192.0.2.0/24
198.51.100.0/24
203.0.113.0/24
```

These are often called TEST-NET ranges.

Example:

```text
203.0.113.10
```

This is useful in networking documentation.

It should not be treated as a normal public Internet destination.

## 14.3 Multicast Addresses

IPv4 multicast range:

```text
224.0.0.0/4
```

Range:

```text
224.0.0.0 - 239.255.255.255
```

Multicast allows one sender to transmit data to a group of interested receivers.

Examples of uses include:

- Streaming within networks.
- Routing protocols.
- Group communication.
- Network discovery mechanisms.

## 14.4 Reserved vs Private

Private addresses are reserved for internal use.

Reserved addresses have a broader meaning.

For example:

```text
127.0.0.1
```

is reserved for loopback.

```text
192.168.1.10
```

is a private address.

```text
203.0.113.10
```

is a documentation address.

All three are special-purpose addresses, but they serve different functions.

---

# 15. NAT and Private Addressing

## 15.1 What Is NAT?

NAT stands for Network Address Translation.

NAT modifies IP address information as packets pass through a network device.

NAT is commonly implemented on routers and firewalls.

It is frequently used to allow multiple devices with private IPv4 addresses to share one public IPv4 address.

## 15.2 Why Is NAT Needed?

IPv4 has a limited address space.

There are approximately 4.29 billion possible IPv4 bit patterns.

Many addresses are reserved for special purposes, and the globally usable address space is smaller.

Private addressing allows organizations and households to reuse the same private address ranges internally.

NAT helps connect those private networks to the public Internet.

## 15.3 Example Network

```text
Laptop A
192.168.1.10
       |
       |
Laptop B
192.168.1.20
       |
       |
Phone
192.168.1.30
       |
       v
+----------------------+
| Home Router          |
|                      |
| LAN: 192.168.1.1     |
| Public IP: 203.0.113.5|
+----------------------+
       |
       v
   Internet
```

The public address in this example is illustrative; `203.0.113.5` is a documentation address and is not a real public Internet address.

A real router would use an appropriately assigned public address.

## 15.4 NAT Translation Example

Suppose a laptop sends a request to a public web server.

Original packet:

```text
Source IP:
192.168.1.10

Destination IP:
93.184.216.34
```

The router translates the source address:

```text
Translated Source IP:
Public IPv4 Address
```

The destination remains the web server's address.

The response returns to the router's public address.

The router uses its translation state to forward the response to the correct internal device.

## 15.5 Port Address Translation (PAT)

PAT stands for Port Address Translation.

It is also commonly called NAT overload.

PAT allows multiple internal connections to share a public IP address by tracking transport-layer port information.

Example:

| Internal Connection | Translated Connection |
|---|---|
| 192.168.1.10:50001 | Public-IP:40001 |
| 192.168.1.20:50001 | Public-IP:40002 |
| 192.168.1.30:50001 | Public-IP:40003 |

The router tracks the mappings so that responses can be delivered to the correct internal connection.

The exact translated ports depend on the NAT implementation.

## 15.6 NAT vs PAT

| NAT | PAT |
|---|---|
| Translates IP addresses | Translates IP addresses and transport ports |
| May use one-to-one mappings | Commonly allows many internal connections to share one public IP |
| Can be static or dynamic | Commonly used for outbound Internet access |
| May not require port translation | Uses port information to distinguish connections |

In everyday networking, the term NAT is often used broadly to describe PAT as well.

## 15.7 Does NAT Provide Security?

NAT is not a complete security mechanism.

It can make unsolicited inbound connections more difficult because a translation entry may not exist.

However:

- NAT is not a replacement for a firewall.
- NAT does not automatically inspect application data.
- NAT does not protect against every attack.
- Applications may still be vulnerable.
- Incorrect port forwarding can expose internal services.

A firewall should be configured to enforce the intended network security policy.

---

# 16. Why Internal IPs Are Not Generally Routable on the Public Internet

## 16.1 Private Address Reuse

RFC 1918 private address ranges can be reused by different organizations.

For example:

```text
Home Network A:
192.168.1.10

Office Network B:
192.168.1.10
```

Both networks can use the same address internally.

This works because the addresses are not intended to be globally routed on the public Internet.

## 16.2 Routing Ambiguity

Suppose two organizations both use:

```text
10.0.0.0/8
```

If those private networks were advertised globally, Internet routers would not have a unique global destination for every reused private address.

The same address could refer to different devices in different organizations.

Therefore, RFC 1918 private address space is not generally routed across the public Internet.

## 16.3 NAT Provides a Boundary

A common network design is:

```text
Private Network
192.168.1.0/24
       |
       v
Router / NAT
       |
       v
Public Network
```

The router translates traffic between private and public addressing as configured.

The internal device uses a private IP address.

The public network sees the router's public address for translated traffic.

## 16.4 Can Private Networks Communicate With Each Other?

Yes.

Private networks can communicate through:

- VPNs.
- Private WAN links.
- Enterprise routing.
- Cloud private networking.
- Network tunnels.

However, overlapping private address ranges may require additional routing design or address translation.

---

# 17. Practical IPv4 Exercises

## Exercise 1 — Identify the Address Type

Determine whether each address is private, loopback, link-local, documentation, multicast, or ordinary public space.

| IP Address | Address Type |
|---|---|
| 192.168.1.10 | |
| 10.0.0.5 | |
| 172.20.10.5 | |
| 172.32.1.1 | |
| 127.0.0.1 | |
| 169.254.1.10 | |
| 8.8.8.8 | |
| 224.0.0.1 | |
| 203.0.113.10 | |

## Exercise 2 — Convert Binary to Decimal

Convert these octets:

```text
11000000
10101000
00000001
00001010
```

## Exercise 3 — Convert Decimal to Binary

Convert:

```text
192
168
10
25
```

## Exercise 4 — Find the Network Address

Given:

```text
IP Address: 192.168.1.100
Subnet Mask: 255.255.255.0
```

Find:

- Network address.
- Broadcast address.
- First usable host.
- Last usable host.
- Total addresses.
- Conventional usable hosts.

## Exercise 5 — Find the Subnet Details

Given:

```text
192.168.10.70/26
```

Find:

- Subnet mask.
- Network address.
- Broadcast address.
- First usable host.
- Last usable host.
- Total addresses.
- Conventional usable hosts.

## Exercise 6 — Calculate Host Capacity

Calculate the total and conventional usable host addresses for:

```text
/24
/25
/26
/27
/28
/29
/30
```

## Exercise 7 — Understand NAT

A laptop has:

```text
192.168.1.10
```

It accesses a public web server through a router.

Explain:

1. What source IP does the laptop use initially?
2. What may the router translate the source IP into?
3. How does the response return to the laptop?
4. What role does PAT play?

---

# 18. Practical Commands

## 18.1 Windows — Check IP Configuration

```powershell
ipconfig
```

Detailed information:

```powershell
ipconfig /all
```

Look for:

- IPv4 Address.
- Subnet Mask.
- Default Gateway.
- DHCP Enabled.
- DNS Servers.

## 18.2 Kali Linux — Check IP Address

```bash
ip addr
```

A shorter version:

```bash
ip -4 addr
```

## 18.3 Linux — Check Routing Table

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlan0
```

This indicates that the default route uses `192.168.1.1` through `wlan0`.

## 18.4 Linux — Check Neighbor Table

```bash
ip neigh
```

This displays neighbor information, including IP-to-link-layer address mappings.

## 18.5 Check Public IP Address

You can check the public IP address observed by an external service using:

```bash
curl https://api.ipify.org
```

This command sends a request to an external service.

Use it only when you are comfortable making that request.

The returned address may be:

- Your router's public IPv4 address.
- A carrier-grade NAT address visible to the external service.
- Another egress address used by your network.

## 18.6 Check Connectivity

```bash
ping 8.8.8.8
```

This tests whether ICMP echo traffic can reach the destination and receive a response.

A failed ping does not always mean the destination is unreachable because ICMP may be filtered.

## 18.7 Check Your Localhost

```bash
ping 127.0.0.1
```

This tests the local IPv4 loopback stack.

---

# 19. Cybersecurity Applications

IPv4 addressing is a fundamental skill for cybersecurity.

It is used in:

- Network reconnaissance.
- Asset discovery.
- Firewall analysis.
- Network segmentation.
- Packet capture.
- Incident response.
- Vulnerability assessment.
- Web application testing.

## 19.1 Identifying Internal Targets

In an authorized lab, you may encounter:

```text
192.168.1.10
192.168.1.20
192.168.1.30
```

These may represent internal systems.

Knowing the subnet helps determine which addresses belong to the same network.

## 19.2 Understanding Network Scope

Suppose you have:

```text
192.168.1.10/24
```

The local subnet is:

```text
192.168.1.0/24
```

This covers:

```text
192.168.1.0 - 192.168.1.255
```

In a conventional `/24` subnet, usable host addresses range from:

```text
192.168.1.1 - 192.168.1.254
```

## 19.3 Understanding Private Services

A web application may be accessible through:

```text
127.0.0.1:8000
```

or:

```text
192.168.1.10:8000
```

These addresses indicate different access contexts.

A service bound to `127.0.0.1` is generally accessible only from the local machine.

A service bound to `0.0.0.0` may listen on all local IPv4 interfaces.

This distinction is important when configuring development servers and testing network exposure.

## 19.4 NAT and Web Security

NAT does not eliminate application vulnerabilities.

A web server behind NAT may still be exposed through:

- Port forwarding.
- Reverse proxies.
- Load balancers.
- VPN access.
- Cloud network configuration.

A private IP address does not automatically mean that a service is secure.

## 19.5 SSRF and IP Addressing

Server-Side Request Forgery (SSRF) is a vulnerability where an application can be induced to make requests to unintended destinations.

Potentially sensitive destinations may include:

- Loopback addresses.
- Internal private networks.
- Internal services.
- Cloud metadata endpoints.

Security testing must be authorized and performed within the permitted scope.

Understanding private, loopback, and link-local addresses helps identify why destination validation is important.

---

# 20. Interview Questions

## Q1. What is an IPv4 address?

An IPv4 address is a 32-bit logical address used to identify an IP endpoint or interface within a network.

## Q2. How many bits are in IPv4?

IPv4 uses 32 bits.

## Q3. How many octets are in an IPv4 address?

Four octets.

Each octet contains 8 bits.

## Q4. What is a subnet mask?

A subnet mask identifies the network and host portions of an IPv4 address.

## Q5. What is CIDR?

CIDR is a method of representing IP networks using a prefix length.

Example:

```text
192.168.1.0/24
```

## Q6. What are the RFC 1918 private ranges?

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

## Q7. Is 172.32.1.1 a private address?

No.

It is outside the RFC 1918 private range `172.16.0.0/12`.

It is not automatically guaranteed to be globally routable, because other special-purpose rules may apply to particular addresses.

## Q8. What is a loopback address?

A loopback address allows a system to communicate with itself.

The commonly used IPv4 loopback address is:

```text
127.0.0.1
```

## Q9. What is APIPA?

APIPA is Automatic Private IP Addressing.

It commonly refers to automatic IPv4 link-local addressing in the range:

```text
169.254.0.0/16
```

## Q10. What is NAT?

NAT translates IP addresses as packets pass through a network device.

It is commonly used to allow private IPv4 networks to access the public Internet.

## Q11. What is PAT?

PAT translates transport-layer port information along with addresses to allow multiple internal connections to share a public IP address.

## Q12. What is the difference between a network address and a broadcast address?

The network address identifies the subnet.

The broadcast address is used to send traffic to all applicable hosts on that subnet.

## Q13. What is the difference between static and dynamic IP addressing?

Static addressing uses a fixed configuration or persistent assignment.

Dynamic addressing commonly uses DHCP to assign addresses automatically.

## Q14. What causes an IP address conflict?

An IP conflict occurs when multiple interfaces use the same IPv4 address within the same relevant network.

## Q15. What does 0.0.0.0 mean?

It is the IPv4 unspecified address.

It can be used in certain initialization contexts and as a wildcard bind address.

The prefix `0.0.0.0/0` represents the IPv4 default route.

## Q16. What is the limited broadcast address?

```text
255.255.255.255
```

It is used for local broadcast communication and is not forwarded by routers.

## Q17. Why are private IPv4 addresses not routed on the public Internet?

They are reusable internal addresses.

Global routing of these addresses would create ambiguity because many unrelated networks use the same private address ranges.

## Q18. Does NAT provide complete security?

No.

NAT is an address-translation mechanism, not a complete security solution.

Firewalls and other security controls are still required.

---

# 21. Key Takeaways

- IPv4 addresses are 32 bits long.
- IPv4 is written in four dotted-decimal octets.
- Each octet ranges from 0 to 255.
- An IPv4 address contains network and host portions.
- The subnet mask or CIDR prefix determines the network portion.
- RFC 1918 defines three private IPv4 ranges.
- `127.0.0.1` is the commonly used IPv4 loopback address.
- `169.254.0.0/16` is the IPv4 link-local range.
- `0.0.0.0` is the unspecified IPv4 address.
- `0.0.0.0/0` represents the IPv4 default route.
- `255.255.255.255` is the limited broadcast address.
- DHCP commonly provides dynamic IP configuration.
- Static addresses are useful for predictable network services.
- IP conflicts occur when interfaces use duplicate addresses.
- Network addresses identify subnets.
- Broadcast addresses are used for subnet broadcast communication.
- NAT translates IP address information.
- PAT allows multiple connections to share a public IPv4 address.
- Private IPv4 addresses are not generally routed across the public Internet.
- Private addressing does not automatically make a system secure.
- IP addressing is essential for network reconnaissance and cybersecurity analysis.

---

# Further Reading

- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131)
- [RFC 3022 — Traditional IP Network Address Translator](https://www.rfc-editor.org/rfc/rfc3022)
- [RFC 3927 — IPv4 Link-Local Addressing](https://www.rfc-editor.org/rfc/rfc3927)
- [IANA IPv4 Special-Purpose Address Registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)

---

**End of Phase 3: IPv4 Fundamentals**
