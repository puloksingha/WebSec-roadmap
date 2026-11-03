
# Phase 4: MAC Addresses and Ethernet

# 7. Data Link Layer

## 7.1 What Is the Data Link Layer?

The **Data Link Layer** is Layer 2 of the OSI model. It is responsible for transferring data between devices on the same local network link.

It takes packets from the Network Layer and encapsulates them into frames.

### Main responsibilities

- Framing: encapsulates network-layer packets into frames.
- Physical addressing: uses MAC addresses to identify network interfaces on a local link.
- Media access control: coordinates access to the shared or controlled transmission medium.
- Error detection: uses mechanisms such as the Ethernet Frame Check Sequence (FCS).
- Local delivery: forwards frames between devices on the same Layer 2 network.

### Data encapsulation

```text
Application data
       ↓
Transport segment/datagram
       ↓
Network packet (IP)
       ↓
Data Link frame (Ethernet)
       ↓
Physical bits/signals
```

The Data Link Layer receives an IP packet and places it inside an Ethernet frame.

### OSI Layer 2 protocols and technologies

- Ethernet — IEEE 802.3
- Wi-Fi — IEEE 802.11
- ARP — Address Resolution Protocol
- VLAN tagging — IEEE 802.1Q
- Spanning Tree Protocol — IEEE 802.1D, with later improvements and variants

> ARP is often described as a Layer 2 protocol because it operates directly over the local link, but it helps resolve Layer 3 IPv4 addresses to Layer 2 MAC addresses.

---

## 7.2 What Is a MAC Address?

A **MAC address** (Media Access Control address) is a link-layer address used to identify a network interface on a local network.

Ethernet frames use MAC addresses for local delivery.

Example:

```text
00:1A:2B:3C:4D:5E
```

A MAC address is usually 48 bits long for Ethernet.

```text
48 bits = 6 bytes = 12 hexadecimal digits
```

A MAC address is not necessarily a permanent hardware identity. Operating systems can use locally administered or randomized MAC addresses.

### Why MAC addresses are used

When a device sends an Ethernet frame on a local network, it needs to identify:

- The source network interface.
- The destination network interface.

For example:

```text
Laptop ───── Ethernet/Wi-Fi LAN ───── Router
```

The laptop uses the router's local MAC address when sending a frame to the router.

The IP packet inside that frame may be destined for a server on the internet. The Ethernet frame is still delivered locally to the router.

---

## 7.3 MAC Address Format

A standard 48-bit MAC address contains six octets.

Example:

```text
00:1A:2B:3C:4D:5E
```

Each pair of hexadecimal digits represents one byte.

```text
00  :  1A  :  2B  :  3C  :  4D  :  5E
 ↓      ↓      ↓      ↓      ↓      ↓
1st    2nd    3rd    4th    5th    6th
byte   byte   byte   byte   byte   byte
```

MAC addresses may be written in different formats:

```text
00:1A:2B:3C:4D:5E
00-1A-2B-3C-4D-5E
001A.2B3C.4D5E
001A2B3C4D5E
```

The notation varies, but the address value is the same.

### OUI — Organizationally Unique Identifier

The first 24 bits of a conventional globally administered MAC address are commonly associated with an organization through an IEEE-assigned identifier.

Example:

```text
00:1A:2B:3C:4D:5E
└───────┘
  24 bits
```

The remaining 24 bits are assigned by the organization.

This is a common structure, not a guarantee that every MAC address identifies a manufacturer. Locally administered and randomized addresses may not correspond to a vendor OUI.

---

## 7.4 Unicast, Multicast, and Broadcast MAC Addresses

Ethernet destination MAC addresses can represent unicast, multicast, or broadcast delivery.

### Unicast MAC address

A unicast MAC address identifies one network interface.

Example:

```text
00:1A:2B:3C:4D:5E
```

A frame sent to this destination is intended for one interface.

### Multicast MAC address

A multicast MAC address identifies a group of interfaces.

For Ethernet, the least significant bit of the first octet is set to `1` for multicast addresses.

Example:

```text
01:00:5E:00:00:01
```

This is an Ethernet multicast address in the IPv4 multicast mapping range.

### Broadcast MAC address

The Ethernet broadcast address is:

```text
FF:FF:FF:FF:FF:FF
```

It means:

```text
All devices on the local Layer 2 broadcast domain
```

A broadcast frame is normally flooded by a switch to all relevant ports in the same VLAN, except the port on which it arrived.

### Quick comparison

| Type | Destination | Purpose |
|---|---|---|
| Unicast | One interface | One-to-one local delivery |
| Multicast | Group of interfaces | One-to-many group delivery |
| Broadcast | All interfaces in the broadcast domain | One-to-all local delivery |

---

## 7.5 MAC Addresses vs IP Addresses

MAC addresses and IP addresses serve different purposes.

| Feature | MAC address | IP address |
|---|---|---|
| OSI layer | Layer 2 | Layer 3 |
| Purpose | Local link delivery | Logical addressing and routing |
| Typical IPv4/Ethernet size | 48 bits | 32 bits |
| IPv6 size | Ethernet MAC remains 48 bits | 128 bits |
| Example | `00:1A:2B:3C:4D:5E` | `192.168.1.10` |
| Used by | Ethernet switches | Routers |
| Scope | Local network link | Can be routed across networks |
| Changes when routing? | Usually replaced per link | Source/destination IPs generally remain end-to-end, except when NAT or other transformations occur |

### Example: Sending traffic to a remote server

Suppose:

```text
Laptop IP:       192.168.1.10
Laptop MAC:      AA:AA:AA:AA:AA:AA

Router IP:       192.168.1.1
Router MAC:      BB:BB:BB:BB:BB:BB

Remote server IP: 203.0.113.50
```

The laptop wants to communicate with `203.0.113.50`.

Because the server is outside the local subnet, the laptop sends the frame to its default gateway.

The Ethernet frame is:

```text
Ethernet:
  Source MAC:      AA:AA:AA:AA:AA:AA
  Destination MAC: BB:BB:BB:BB:BB:BB

IP packet:
  Source IP:       192.168.1.10
  Destination IP:  203.0.113.50
```

The destination MAC is the router's MAC address, while the destination IP is the remote server's IP address.

At each routed hop, the Layer 2 frame is replaced for the next link. The IP packet is forwarded according to routing and may be modified by mechanisms such as NAT.

---

## 7.6 Ethernet Fundamentals

**Ethernet** is a widely used wired LAN technology standardized mainly by IEEE 802.3.

Ethernet defines:

- Frame format
- MAC addressing
- Link operation
- Physical-layer variants
- Error detection through the Frame Check Sequence

Common Ethernet speeds include:

```text
10 Mbps
100 Mbps
1 Gbps
10 Gbps
25 Gbps
40 Gbps
100 Gbps
```

Actual speeds depend on the interface, cable, transceiver, switch, and negotiated link settings.

### Ethernet network example

```text
Laptop ───── Switch ───── Router ───── Internet
             │
             └────────── Desktop
```

A switch forwards Ethernet frames between devices based on destination MAC addresses.

---

## 7.7 Ethernet Frames

An Ethernet frame is the Layer 2 unit of transmission.

A standard Ethernet frame contains:

- Destination MAC address
- Source MAC address
- EtherType or Length field
- Payload
- Frame Check Sequence (FCS)

### Ethernet II frame format

```text
+-------------------+-------------------+
| Destination MAC   | 6 bytes           |
+-------------------+-------------------+
| Source MAC        | 6 bytes           |
+-------------------+-------------------+
| EtherType         | 2 bytes           |
+-------------------+-------------------+
| Payload           | 46-1500 bytes*    |
+-------------------+-------------------+
| FCS               | 4 bytes           |
+-------------------+-------------------+
```

`*` The common 1500-byte payload limit applies to standard Ethernet with a 1500-byte IP MTU. The minimum Ethernet payload is padded to 46 bytes when necessary.

### Common EtherType values

| EtherType | Protocol |
|---|---|
| `0x0800` | IPv4 |
| `0x0806` | ARP |
| `0x86DD` | IPv6 |
| `0x8100` | IEEE 802.1Q VLAN-tagged frame |

EtherType tells the receiver which protocol is carried in the Ethernet payload.

---

## 7.8 Frame Headers and Trailers

### Ethernet header

The Ethernet header contains:

- Destination MAC address
- Source MAC address
- EtherType/Length field

With Ethernet II, the header is 14 bytes long when there is no VLAN tag.

### Ethernet trailer

The Ethernet trailer contains the Frame Check Sequence (FCS).

The FCS is 4 bytes long and uses a CRC-based calculation to detect transmission errors.

A receiver can use the FCS to determine whether a frame was corrupted during transmission.

> Many packet captures taken on ordinary computers do not include the FCS because the network interface removes it before passing the frame to the operating system.

### Frame size

For standard Ethernet II:

```text
Header:       14 bytes
Payload:      46-1500 bytes
FCS:           4 bytes
```

The frame size from destination MAC through FCS is generally:

```text
64-1518 bytes
```

The preamble and Start Frame Delimiter are transmitted on the wire but are not normally included in the Ethernet frame size reported by packet captures.

---

## 7.9 MTU — Maximum Transmission Unit

**MTU** is the maximum size of the network-layer packet that can be carried in a link-layer payload without fragmentation at that layer.

For standard Ethernet:

```text
MTU = 1500 bytes
```

For IPv4 over Ethernet, the 1500-byte IP packet commonly includes:

```text
IPv4 header + IPv4 payload
```

The Ethernet header and FCS are not part of the IP MTU.

### Example

If an IPv4 packet has:

```text
IPv4 header: 20 bytes
IPv4 payload: 1480 bytes
```

Then:

```text
Total IPv4 packet = 20 + 1480
                  = 1500 bytes
```

This fits a standard Ethernet MTU of 1500 bytes.

### Why MTU matters

An MTU mismatch can cause:

- Fragmentation in IPv4, depending on flags and path behavior.
- Packet drops when packets exceed the path MTU and cannot be fragmented.
- Slow or failed connections.
- Problems with VPNs and tunnels due to added encapsulation overhead.

### Path MTU Discovery

Path MTU Discovery determines the largest packet size that can travel along a path without requiring fragmentation.

For IPv4, ICMP messages may indicate that fragmentation is needed.

For IPv6, routers do not fragment packets. The source uses Path MTU Discovery and may reduce packet size based on ICMPv6 Packet Too Big messages.

---

## 7.10 Jumbo Frames — Overview

**Jumbo frames** are Ethernet frames with payloads larger than the standard 1500-byte MTU.

A commonly used jumbo MTU is:

```text
9000 bytes
```

Jumbo frames may be useful in:

- Data centers
- Storage networks
- High-throughput server environments
- Some virtualization and backup networks

### Benefits

- Less per-packet overhead for large transfers.
- Potentially improved throughput in suitable environments.

### Limitations

- All relevant devices and links must support the configured MTU.
- Misconfiguration can cause packet loss or connectivity problems.
- Jumbo frames are not universally supported across the public internet.

---

## 7.11 ARP — Address Resolution Protocol

**ARP** stands for Address Resolution Protocol.

ARP resolves an IPv4 address to a MAC address on the local network.

For example, a computer knows:

```text
Destination IPv4 address: 192.168.1.1
```

But to send an Ethernet frame on the local network, it needs the destination MAC address.

ARP helps discover that address.

### Important distinction

ARP is used for IPv4 over a local link.

IPv6 does not use ARP. IPv6 uses Neighbor Discovery Protocol (NDP), which operates through ICMPv6.

---

## 7.12 ARP Requests and Replies

Suppose a laptop wants to send traffic to:

```text
192.168.1.1
```

but does not know its MAC address.

### ARP request

The laptop sends a broadcast Ethernet frame:

```text
Destination MAC: FF:FF:FF:FF:FF:FF
```

The ARP request asks:

```text
Who has 192.168.1.1?
Tell 192.168.1.10.
```

All devices in the local broadcast domain receive the request, but only the device configured with `192.168.1.1` should normally respond.

### ARP reply

The router replies, usually with a unicast frame:

```text
192.168.1.1 is at BB:BB:BB:BB:BB:BB
```

The laptop can now send Ethernet frames to the router's MAC address.

### ARP exchange

```text
Laptop
  |
  | ARP Request (broadcast)
  | "Who has 192.168.1.1?"
  |
  v
Local network
  |
  | ARP Reply (usually unicast)
  | "192.168.1.1 is BB:BB:BB:BB:BB:BB"
  |
  v
Laptop updates its ARP cache
```

---

## 7.13 ARP Cache

An **ARP cache** stores recently learned IPv4-to-MAC address mappings.

Example:

```text
192.168.1.1 → BB:BB:BB:BB:BB:BB
```

The cache reduces the need to send an ARP request for every packet.

Entries may be:

- Dynamic: learned through ARP.
- Static: manually configured and usually persistent until removed.

Dynamic entries expire or are refreshed according to the operating system's neighbor-cache behavior.

### Inspect ARP/neighbor information on Linux

```bash
ip neigh
```

Example output:

```text
192.168.1.1 dev eth0 lladdr bb:bb:bb:bb:bb:bb REACHABLE
```

Interpretation:

- `192.168.1.1`: IPv4 neighbor address.
- `dev eth0`: network interface.
- `lladdr`: link-layer address, commonly the MAC address.
- `REACHABLE`: neighbor is currently considered reachable.

Other possible states include:

```text
STALE
DELAY
PROBE
INCOMPLETE
FAILED
```

These states describe the neighbor-discovery process and reachability status.

---

## 7.14 `ip neigh`

The Linux `ip neigh` command displays and manages the neighbor table.

### Display neighbor table

```bash
ip neigh
```

### Display IPv4 neighbors

```bash
ip -4 neigh
```

### Display IPv6 neighbors

```bash
ip -6 neigh
```

### Display neighbors on a specific interface

```bash
ip neigh show dev eth0
```

Replace `eth0` with the actual interface name on your system.

### Delete a neighbor entry

```bash
sudo ip neigh del 192.168.1.1 dev eth0
```

This removes a local cache entry. The system may relearn it when communication resumes.

Use this only on your own machine or an authorized system. Avoid modifying neighbor entries on a production or remote system unless you understand the impact.

---

## 7.15 MAC Address Learning in Switches

A Layer 2 switch learns MAC addresses by examining the **source MAC address** of incoming Ethernet frames.

The switch records:

```text
Source MAC address → Incoming switch port
```

This information is stored in a MAC address table, also called a CAM table.

### Example

```text
PC-A ── Port 1
PC-B ── Port 2
PC-C ── Port 3
```

If PC-A sends a frame through Port 1, the switch learns:

```text
PC-A MAC → Port 1
```

When PC-A sends traffic to PC-B, the switch checks its MAC table.

If the destination MAC is known, the switch forwards the frame to the correct port.

If the destination MAC is unknown, the switch floods the frame to relevant ports in the same VLAN, except the incoming port.

### Learning and forwarding process

1. A frame arrives on a switch port.
2. The switch reads the source MAC address.
3. The switch records the source MAC and incoming port.
4. The switch checks the destination MAC.
5. If the destination is known, it forwards the frame to the mapped port.
6. If the destination is unknown, it floods the frame within the VLAN.
7. Broadcast frames are also flooded within the VLAN.

Switches age out dynamic MAC table entries when they have not been used for a configured period.

---

## 7.16 Switches vs Hubs

| Feature | Hub | Switch |
|---|---|---|
| OSI layer | Layer 1 | Mainly Layer 2 |
| Forwarding | Repeats signals to other ports | Forwards frames based on MAC table |
| MAC learning | No | Yes |
| Collision domains | One shared collision domain | Separate collision domain per port in full-duplex operation |
| Bandwidth | Shared | Typically dedicated per port |
| Traffic privacy | Traffic is repeated to all ports | Unicast is generally forwarded only to the destination port |
| Modern use | Obsolete in most LANs | Common |

A hub does not inspect MAC addresses. A switch learns and uses MAC addresses to make forwarding decisions.

---

## 7.17 Collision Domains and Broadcast Domains

### Collision domain

A collision domain is a network segment where Ethernet transmissions can collide when devices share a transmission medium.

With modern full-duplex switched Ethernet, collisions are generally not expected.

Each switch port is typically a separate collision domain.

### Broadcast domain

A broadcast domain is the set of devices that receive a Layer 2 broadcast.

A VLAN normally forms one broadcast domain.

Example:

```text
VLAN 10:
PC-A ── Switch ── PC-B

VLAN 20:
PC-C ── Switch ── PC-D
```

A broadcast from PC-A in VLAN 10 is not normally forwarded into VLAN 20.

### Key distinction

- Switches separate collision domains.
- VLANs separate broadcast domains.
- Routers or Layer 3 switches route traffic between IP subnets/VLANs.

---

## 7.18 VLANs — Virtual LANs

A **VLAN** is a logical Layer 2 network that separates devices into distinct broadcast domains.

VLANs allow one physical switching infrastructure to support multiple logical networks.

### Example

```text
                 Managed Switch
              /        |        \
           Port 1    Port 2    Port 3
            VLAN 10   VLAN 10   VLAN 20
             PC-A      PC-B      PC-C
```

PC-A and PC-B are in VLAN 10. PC-C is in VLAN 20.

Even if all devices connect to the same physical switch, VLAN separation keeps their Layer 2 broadcast traffic separate.

### Common VLAN uses

- Separating departments.
- Isolating guest networks.
- Separating servers from user devices.
- Organizing voice and data traffic.
- Reducing broadcast scope.
- Supporting network security policies.

VLANs provide segmentation, but they are not a complete security boundary by themselves. Inter-VLAN routing and firewall policy must also be configured appropriately.

---

## 7.19 IEEE 802.1Q VLAN Tagging

IEEE 802.1Q defines VLAN tagging for Ethernet frames.

A VLAN tag is inserted into the Ethernet frame between the source MAC address and the EtherType/Length field.

### Untagged Ethernet II frame

```text
+-------------------+
| Destination MAC   |
+-------------------+
| Source MAC        |
+-------------------+
| EtherType         |
+-------------------+
| Payload           |
+-------------------+
| FCS               |
+-------------------+
```

### 802.1Q tagged frame

```text
+-------------------+
| Destination MAC   |
+-------------------+
| Source MAC        |
+-------------------+
| 802.1Q VLAN Tag   | 4 bytes
+-------------------+
| EtherType         |
+-------------------+
| Payload           |
+-------------------+
| FCS               |
+-------------------+
```

The 802.1Q tag contains:

- Tag Protocol Identifier (TPID), commonly `0x8100`.
- Tag Control Information (TCI), including priority, drop eligibility, and VLAN ID.

The VLAN ID is 12 bits long.

```text
12 bits → 4096 possible values
```

VLAN IDs 0 and 4095 are reserved. Common usable VLAN IDs are 1 through 4094, subject to platform conventions and configuration.

---

## 7.20 Trunk vs Access Ports

### Access port

An access port normally carries traffic for one VLAN.

It is commonly used to connect:

- Desktop computers
- Printers
- Ordinary endpoints

Example:

```text
PC ─── Access Port ─── Switch
        VLAN 10
```

The connected endpoint typically sends and receives untagged Ethernet frames. The switch associates those frames with the configured access VLAN.

### Trunk port

A trunk port carries traffic for multiple VLANs.

It is commonly used between:

- Switches
- Switches and routers
- Switches and virtualization hosts

Example:

```text
Switch A ───── Trunk ───── Switch B
              VLAN 10
              VLAN 20
              VLAN 30
```

VLAN tags identify the VLAN associated with each tagged frame.

### Comparison

| Feature | Access port | Trunk port |
|---|---|---|
| Typical VLAN count | One data VLAN | Multiple VLANs |
| Typical connected device | End host | Switch/router/virtualization host |
| Frame handling | Usually untagged endpoint traffic | VLAN-tagged traffic |
| Purpose | Endpoint access | Carry VLANs between network devices |

Some trunk configurations also carry a native VLAN whose traffic is untagged. Native VLAN behavior must be configured consistently on both ends.

---

## 7.21 Spanning Tree Protocol — Basic Purpose

**Spanning Tree Protocol (STP)** prevents Layer 2 switching loops.

### Why switching loops are dangerous

Ethernet frames do not have a Layer 2 hop-count field like IP packets do.

If redundant switch links form a loop, broadcast and unknown-unicast frames may circulate repeatedly.

This can cause:

- Broadcast storms
- MAC address table instability
- Duplicate frame delivery
- Network congestion
- Network outages

### STP's purpose

STP identifies a loop-free logical topology by placing some redundant ports into a blocking or non-forwarding state.

If an active path fails, STP can allow a redundant path to become active.

### Conceptual example

```text
Switch A ───── Switch B
   |              |
   |              |
   └──── Switch C ┘
```

This triangle creates a physical loop.

STP selects a loop-free forwarding topology while retaining redundancy.

### Related versions

- STP — original spanning tree mechanism.
- RSTP — Rapid Spanning Tree Protocol, which provides faster convergence.
- MSTP — Multiple Spanning Tree Protocol, which supports multiple spanning-tree instances.

---

## 7.22 Port Mirroring — Overview

**Port mirroring**, also called SPAN on some switches, copies traffic from selected switch ports or VLANs to a monitoring port.

A security analyst can connect a monitoring device to the destination port and capture traffic using tools such as Wireshark.

### Example

```text
PC-A ── Port 1 ── Switch ── Router
                   |
                   | mirrored traffic
                   v
              Monitor Port
                   |
                   v
              Wireshark PC
```

### Uses

- Network troubleshooting
- Traffic analysis
- Security monitoring
- Intrusion detection
- Protocol investigation

### Limitations

- A mirror port may not capture every frame if traffic exceeds its capacity.
- The switch configuration determines which traffic is copied.
- Encryption can limit the contents visible in packet captures.
- Port mirroring should be configured only on networks you own or are authorized to monitor.

---

## 7.23 ARP Spoofing / Poisoning — Concepts and Defenses

**ARP spoofing** or **ARP poisoning** is a local-network attack in which an attacker sends forged ARP messages to associate an IP address with an incorrect MAC address.

Because ARP does not authenticate replies, a host may accept an incorrect mapping under some conditions.

### Conceptual example

Normal mapping:

```text
192.168.1.1 → Router MAC
```

A forged mapping may claim:

```text
192.168.1.1 → Attacker MAC
```

If a victim accepts the forged mapping, traffic intended for the router may be sent to the attacker's interface.

### Potential impact

- Traffic interception
- Man-in-the-middle positioning
- Traffic disruption
- Session or data exposure when other protections are weak

ARP spoofing does not automatically defeat HTTPS, TLS, or other end-to-end encryption. Encryption can still protect the contents of properly authenticated connections.

### Defenses

- Use Dynamic ARP Inspection (DAI) on supported managed switches.
- Use DHCP snooping as part of a DAI deployment where appropriate.
- Configure static neighbor entries only where operationally practical.
- Segment networks using VLANs and appropriate Layer 3 policies.
- Monitor for unexpected IP-to-MAC mapping changes.
- Use encrypted protocols such as HTTPS and SSH.
- Protect switch management interfaces.
- Avoid untrusted devices on sensitive LANs.

### Security monitoring

A possible warning sign is one IP address appearing to map to multiple MAC addresses unexpectedly.

This can have legitimate causes, such as failover or address changes, so investigate before treating it as an attack.

> Study ARP poisoning in an isolated lab or on systems you own and have permission to test. Do not poison a public, campus, workplace, or other shared network.

---

# Practical Tasks

## Task 1: Find Your MAC Address

Run:

```bash
ip link
```

Or:

```bash
ip address
```

Example output:

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    link/ether 00:11:22:33:44:55
```

The line:

```text
link/ether 00:11:22:33:44:55
```

shows the interface's Ethernet MAC address.

### Show a specific interface

```bash
ip link show eth0
```

Replace `eth0` with your actual interface name.

### Important note

A laptop may have multiple interfaces:

- Ethernet adapter
- Wi-Fi adapter
- VMware virtual adapter
- Loopback interface

Each Ethernet or Wi-Fi interface may have a different MAC address. Some operating systems also use MAC randomization for privacy.

---

## Task 2: Inspect the ARP / Neighbor Table

Run:

```bash
ip neigh
```

For IPv4:

```bash
ip -4 neigh
```

For IPv6:

```bash
ip -6 neigh
```

Example:

```text
192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

Identify:

- Neighbor IP address
- MAC address
- Interface
- Neighbor state

If the table is empty, generate traffic to a local device you are authorized to contact, then inspect the table again.

---

## Task 3: Observe an ARP Exchange in Wireshark

Use Wireshark on your own network or an authorized lab.

### Procedure

1. Open Wireshark.
2. Select the active Ethernet or Wi-Fi interface.
3. Start capturing packets.
4. Generate traffic to a local IPv4 device whose MAC address is not already cached.
5. Stop the capture.
6. Apply this display filter:

```text
arp
```

### What to look for

An ARP request may contain:

```text
Who has 192.168.1.1? Tell 192.168.1.10
```

An ARP reply may contain:

```text
192.168.1.1 is at aa:bb:cc:dd:ee:ff
```

Record:

- Sender IP address
- Sender MAC address
- Target IP address
- Target MAC address
- Whether the Ethernet destination is broadcast or unicast

### Note about Wi-Fi

Depending on the Wi-Fi adapter, driver, and capture mode, Wireshark may not show all link-layer details. Ethernet captures often make ARP and Ethernet header inspection more straightforward.

---

## Task 4: Explain Why a Switch Needs MAC Addresses

A switch uses MAC addresses to decide where to forward Ethernet frames.

Without MAC learning, a switch would not know which port leads to a particular destination interface.

A switch:

1. Learns source MAC addresses from incoming frames.
2. Associates each MAC address with a port and VLAN.
3. Looks up destination MAC addresses.
4. Forwards known unicast traffic to the correct port.
5. Floods unknown unicast and broadcast traffic within the relevant VLAN.

This is why switches can forward local traffic efficiently instead of repeating every frame to every port like a hub.

---

# Quick Revision

| Concept | Key point |
|---|---|
| MAC address | Layer 2 address used for local link delivery |
| IPv4 address | Layer 3 logical address used for routing |
| Ethernet frame | Layer 2 unit containing MAC addresses and payload |
| MTU | Maximum network-layer packet size supported by a link |
| ARP | Resolves IPv4 addresses to MAC addresses on a local link |
| ARP cache | Stores recently learned IPv4-to-MAC mappings |
| Switch | Learns MAC addresses and forwards frames by destination |
| Hub | Repeats signals to other ports |
| Collision domain | Segment where transmissions can collide |
| Broadcast domain | Set of devices receiving Layer 2 broadcasts |
| VLAN | Logical Layer 2 network and broadcast domain |
| 802.1Q | Ethernet VLAN tagging standard |
| Access port | Normally carries one VLAN for an endpoint |
| Trunk port | Carries multiple VLANs between network devices |
| STP | Prevents Layer 2 switching loops |
| Port mirroring | Copies selected traffic to a monitoring port |
| ARP poisoning | Forged ARP mapping used to redirect local traffic |

---

# Interview Questions

1. What is a MAC address?
2. How many bits are in a standard Ethernet MAC address?
3. What is the difference between a unicast and broadcast MAC address?
4. How are MAC addresses different from IP addresses?
5. What information is present in an Ethernet II frame?
6. What is the purpose of the Ethernet FCS?
7. What is MTU?
8. What are jumbo frames?
9. What problem does ARP solve?
10. What is the difference between an ARP request and an ARP reply?
11. What information is stored in the ARP cache?
12. How does a switch learn MAC addresses?
13. What happens when a switch receives a frame with an unknown destination MAC?
14. What is the difference between a hub and a switch?
15. What is the difference between a collision domain and a broadcast domain?
16. What is a VLAN?
17. What is the purpose of 802.1Q tagging?
18. What is the difference between an access port and a trunk port?
19. Why is Spanning Tree Protocol needed?
20. What is port mirroring?
21. What is ARP poisoning, and how can it be defended against?

---

# Summary

- The Data Link Layer provides local frame delivery.
- Ethernet frames use source and destination MAC addresses.
- A standard Ethernet MAC address is 48 bits long.
- MAC addresses and IP addresses operate at different layers and serve different purposes.
- ARP resolves IPv4 addresses to MAC addresses on a local network.
- Switches learn source MAC addresses and use their MAC tables to forward frames.
- VLANs separate Layer 2 broadcast domains.
- 802.1Q adds VLAN tags to Ethernet frames.
- STP prevents Layer 2 loops.
- Port mirroring helps analysts capture network traffic.
- ARP spoofing abuses the lack of ARP authentication and can be mitigated through switch protections, segmentation, monitoring, and encryption.
