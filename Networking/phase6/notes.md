
# Phase 6: Network Devices and Routing

## 11. Networking Devices

### 11.1 What Are Networking Devices?

Networking devices are hardware or software components that connect computers and networks, forward traffic, control communication, or provide network services.

Different devices operate at different layers of the OSI model.

| Device | Primary OSI Layer | Main Function |
|---|---|---|
| NIC | Layer 1 and Layer 2 | Connects a host to a network |
| Repeater | Layer 1 | Regenerates a weakened signal |
| Hub | Layer 1 | Repeats incoming bits to all ports |
| Bridge | Layer 2 | Connects LAN segments and filters frames |
| Layer 2 switch | Layer 2 | Forwards Ethernet frames using MAC addresses |
| Layer 3 switch | Layers 2 and 3 | Switches frames and routes IP packets |
| Router | Layer 3 | Forwards packets between IP networks |
| Wireless access point | Layers 1 and 2 | Connects wireless clients to a LAN |
| Modem | Physical-layer signaling | Converts signals for a communication medium |
| Firewall | Layers 3–7, depending on type | Enforces traffic security policies |
| Proxy server | Usually Layer 7 | Makes requests on behalf of clients |
| Load balancer | Layers 4 or 7 | Distributes traffic across servers |
| Gateway | Depends on function | Connects networks or translates protocols |
| IDS | Depends on inspection | Detects suspicious activity |
| IPS | Depends on inspection | Detects and blocks suspicious activity |
| Network tap | Usually Layers 1–2 | Provides a copy of network traffic for monitoring |
| Reverse proxy | Usually Layer 7 | Receives requests for backend servers |
| CDN | Distributed infrastructure | Delivers content from nearby edge locations |

> OSI-layer classifications are useful learning models. Real devices may operate across multiple layers.

---

### 11.2 Network Interface Card (NIC)

A Network Interface Card (NIC) is a hardware or virtual interface that allows a device to communicate over a network.

Examples:
- Ethernet NIC
- Wi-Fi NIC
- Virtual network interface inside a virtual machine

#### Functions

- Provides a network interface to the operating system.
- Sends and receives network frames.
- Uses a MAC address for Layer 2 communication.
- Converts data between the host's networking stack and the network medium.
- May support hardware features such as checksum offloading and VLAN tagging.

A NIC may have a factory-assigned MAC address, but some systems allow the address to be changed or overridden.

#### Linux commands

```bash
ip link
ip addr
```

Example output:

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    link/ether 00:11:22:33:44:55
    inet 192.168.1.20/24
```

Here:
- `eth0` is the interface name.
- `00:11:22:33:44:55` is the MAC address.
- `192.168.1.20/24` is an IPv4 address with a `/24` prefix.

---

### 11.3 Repeater

A repeater is a Layer 1 device that regenerates or retransmits a signal to extend its reach.

#### Purpose

Signals may become weaker as they travel through a medium. A repeater receives a signal, regenerates it, and sends it onward.

#### Characteristics

- Operates at the Physical Layer.
- Does not understand MAC addresses or IP addresses.
- Does not filter traffic.
- Does not create a separate collision domain in the way a bridge or switch does.

A repeater extends the physical reach of a network, but it does not make the network more intelligent or secure.

---

### 11.4 Hub

A hub is a multiport repeater.

When a hub receives bits on one port, it repeats them to all other ports.

#### Characteristics

- Operates at Layer 1.
- Does not learn MAC addresses.
- Sends incoming signals to all other ports.
- All connected devices share the same collision domain.
- Typically operates in half-duplex mode.
- Is largely obsolete in modern Ethernet networks.

#### Example

If Computer A sends a frame to Computer B through a hub, the hub repeats the signal to every connected port. Each NIC checks the destination MAC address and decides whether to accept the frame.

A hub does not know which port belongs to Computer B.

---

### 11.5 Bridge

A bridge connects and filters traffic between LAN segments.

A traditional Ethernet bridge operates at Layer 2.

#### How a bridge works

1. Receives an Ethernet frame.
2. Reads the source MAC address.
3. Learns which segment contains that source MAC address.
4. Checks the destination MAC address.
5. Forwards or filters the frame based on its forwarding table.

#### Bridge behavior

| Destination | Bridge action |
|---|---|
| Known destination on the same segment | Filters the frame; does not forward it |
| Known destination on another segment | Forwards it to that segment |
| Unknown unicast destination | Floods it to other relevant segments |
| Broadcast destination | Floods it to other relevant segments |

A bridge reduces unnecessary traffic between LAN segments compared with a hub.

---

### 11.6 Layer 2 Switch

A Layer 2 switch is a multiport bridge that forwards Ethernet frames using MAC addresses.

#### MAC address table

A switch maintains a forwarding database, often called a MAC address table.

Example:

| MAC address | Switch port |
|---|---|
| AA:AA:AA:AA:AA:AA | Port 1 |
| BB:BB:BB:BB:BB:BB | Port 2 |
| CC:CC:CC:CC:CC:CC | Port 3 |

#### Learning and forwarding process

When a switch receives a frame:

1. It learns the source MAC address and associates it with the incoming port.
2. It looks up the destination MAC address.
3. If the destination is known, it forwards the frame to the associated port.
4. If the destination is unknown, it floods the frame within the VLAN, excluding the incoming port.
5. Broadcast frames are flooded within the VLAN, excluding the incoming port.

#### Collision domains and broadcast domains

- Each switch port is a separate collision domain.
- A VLAN is a separate Layer 2 broadcast domain.
- A switch without VLAN segmentation generally has one broadcast domain.

Modern switched Ethernet links commonly operate in full-duplex mode, so collisions are not expected on those links.

---

### 11.7 Layer 3 Switch

A Layer 3 switch combines Layer 2 switching with Layer 3 routing.

It can:
- Forward Ethernet frames using MAC addresses.
- Route IP packets between different IP networks or VLANs.
- Use hardware-based forwarding for high-speed inter-VLAN routing.

#### Example

Suppose a campus network has:

- VLAN 10: `192.168.10.0/24`
- VLAN 20: `192.168.20.0/24`

A Layer 3 switch can provide an interface for each VLAN:

```text
VLAN 10 gateway: 192.168.10.1
VLAN 20 gateway: 192.168.20.1
```

A host in VLAN 10 can send traffic to a host in VLAN 20 through the Layer 3 switch, provided routing and security policies allow it.

---

### 11.8 Router

A router connects different IP networks and forwards packets between them.

A router makes forwarding decisions primarily using:
- Destination IP address
- Routing table
- Longest-prefix match
- Route preference and metrics
- Next-hop information

#### Example

```text
Network A                         Network B
192.168.1.0/24                   192.168.2.0/24

PC-A ---- Router ---- PC-B
          .1   .1
```

Router interfaces might be:

```text
192.168.1.1/24
192.168.2.1/24
```

PC-A sends packets for `192.168.2.20` to its default gateway, `192.168.1.1`. The router forwards the packet toward Network B.

#### Important points

- Routers separate IP networks.
- Routers normally separate broadcast domains.
- Routers decrement the IPv4 TTL or IPv6 Hop Limit when forwarding packets.
- A router may also perform NAT, firewalling, VPN termination, or other functions, but these are separate functions from basic routing.

---

### 11.9 Wireless Access Point (AP)

A wireless access point allows Wi-Fi devices to connect to a wired LAN.

#### Functions

- Provides wireless connectivity.
- Advertises a wireless network name (SSID).
- Bridges wireless client traffic to the LAN.
- Supports wireless authentication and encryption, such as WPA2 or WPA3.

A typical access point is not necessarily a router. It may simply bridge Wi-Fi traffic to an existing Ethernet network.

A home Wi-Fi router commonly combines:
- Wireless access point
- Ethernet switch
- Router
- DHCP server
- Firewall
- NAT functionality

---

### 11.10 Modem

A modem is a device that modulates and demodulates signals, or more generally adapts data to the signaling method used by a communication link.

The exact technology depends on the access network.

Examples:
- DSL modem
- Cable modem
- Cellular modem
- Fiber ONT (Optical Network Terminal)

A fiber ONT is often casually called a modem, but it uses optical transmission technology rather than traditional electrical modulation.

#### Typical connection

```text
Home network
     |
Router
     |
Modem / ONT
     |
ISP access network
     |
Internet
```

A modem or ONT provides access to the ISP network. It does not necessarily perform IP routing.

---

### 11.11 Firewall

A firewall enforces security rules that allow, reject, or inspect network traffic.

#### Common firewall types

| Type | Description |
|---|---|
| Packet-filtering firewall | Filters traffic using fields such as IP addresses, ports, and protocol |
| Stateful firewall | Tracks connection state and evaluates traffic in relation to connections |
| Application firewall | Inspects application-layer traffic |
| Host-based firewall | Runs on an individual host |
| Network firewall | Protects or segments networks |

#### Example rule

A firewall policy might allow:

```text
Allow TCP traffic to destination port 443
Deny other unsolicited inbound traffic
```

A real policy must also specify details such as source, destination, interface, connection state, and rule order.

#### Firewall vs router

- A router decides where packets should be forwarded.
- A firewall decides whether traffic should be permitted according to security policy.
- One device can perform both functions.

---

### 11.12 Proxy Server

A proxy server acts as an intermediary between a client and another server.

A forward proxy commonly represents clients.

#### Forward proxy example

```text
Client ---> Forward Proxy ---> Internet Server
```

Possible purposes:
- Access control
- Content filtering
- Logging
- Caching
- Privacy or network policy enforcement

A proxy may terminate one connection and establish another. This differs from ordinary IP forwarding.

---

### 11.13 Load Balancer

A load balancer distributes traffic among multiple backend servers.

#### Example

```text
                 +--> Server 1
Client --> LB ---+--> Server 2
                 +--> Server 3
```

#### Benefits

- Distributes traffic.
- Improves availability.
- Can perform health checks.
- Can route requests based on configured policies.
- May support TLS termination.

#### Layer 4 vs Layer 7 load balancing

| Layer | Common decision inputs |
|---|---|
| Layer 4 | IP addresses, TCP/UDP ports, transport connections |
| Layer 7 | HTTP host, URL path, headers, cookies, application data |

A load balancer does not automatically make an application secure. Backend servers and the load-balancing configuration still require proper security.

---

### 11.14 Gateway

A gateway is a device or system that connects networks or provides a path to another network.

The term has several meanings.

#### Default gateway

A host's default gateway is the router or Layer 3 device used to reach destinations that do not match a more specific route.

#### Application gateway

An application gateway can translate, inspect, or mediate application protocols.

#### Protocol gateway

A protocol gateway may translate between different protocols or network technologies.

The meaning of "gateway" depends on the context. A default gateway is not necessarily a protocol translator.

---

### 11.15 IDS and IPS

IDS means Intrusion Detection System.

IPS means Intrusion Prevention System.

Both monitor traffic or system activity for suspicious patterns.

| Feature | IDS | IPS |
|---|---|---|
| Main purpose | Detect suspicious activity | Detect and prevent suspicious activity |
| Typical placement | Often out-of-band | Often inline |
| Response | Alert, log, report | Drop, block, reset, or alert |
| Risk | May miss activity | May block legitimate traffic if misconfigured |

#### Detection methods

- Signature-based detection
- Anomaly-based detection
- Behavior-based detection
- Protocol analysis

#### Example

An IDS might detect repeated suspicious connection attempts and create an alert.

An IPS placed inline might block matching traffic based on its configured policy.

Neither system guarantees detection of every attack.

---

### 11.16 Network Tap

A network tap provides a copy of traffic from a network link for monitoring.

It is commonly used with:
- Packet capture systems
- Network intrusion detection
- Traffic analysis
- Troubleshooting

#### Typical arrangement

```text
Device A ===== Network Tap ===== Device B
                    |
                    +------ Monitoring system
```

A passive tap can provide traffic to a monitoring device without requiring the monitoring device to sit directly in the forwarding path.

A tap is useful because monitoring systems can inspect copied traffic while normal communication continues.

---

### 11.17 Reverse Proxy

A reverse proxy receives requests on behalf of backend servers.

```text
Client ---> Reverse Proxy ---> Backend Server
```

Common functions:
- TLS termination
- Request routing
- Load balancing
- Caching
- Access control
- Hiding backend server details
- Web Application Firewall (WAF) integration

#### Forward proxy vs reverse proxy

| Forward proxy | Reverse proxy |
|---|---|
| Represents clients | Represents servers |
| Usually placed on the client side | Usually placed in front of backend servers |
| Controls or mediates client access outward | Controls or mediates incoming requests |

A reverse proxy is not the same as a router. A router forwards IP packets, while a reverse proxy commonly handles application-level requests.

---

### 11.18 Content Delivery Network (CDN)

A Content Delivery Network is a distributed collection of servers that delivers content from locations closer to users.

#### How a CDN works

1. A user requests content from a website.
2. DNS or another routing mechanism directs the user toward a suitable CDN edge.
3. The edge server checks whether the requested content is cached.
4. If cached, the CDN returns the content.
5. If not cached, the CDN may fetch it from the origin server and cache it according to policy.

#### Benefits

- Lower latency
- Reduced load on origin servers
- Improved content delivery performance
- Better ability to handle traffic spikes
- Potential protection against some forms of denial-of-service traffic

A CDN is not a complete security solution. Security depends on its configuration, origin protection, application controls, and other defenses.

---

## 12. Routing Fundamentals

### 12.1 What Is Routing?

Routing is the process of selecting a path for packets to travel from a source network toward a destination network.

A router uses its routing information to decide:
- Whether the destination is directly connected.
- Which route best matches the destination IP address.
- Which next hop should receive the packet.
- Which outgoing interface should be used.

Routing is a Layer 3 function.

#### Routing vs forwarding

- **Routing:** Determines or learns paths and builds routing information.
- **Forwarding:** Uses the forwarding table to send an individual packet to the appropriate next hop or interface.

Routing is the decision-making process; forwarding is the packet-moving process.

---

### 12.2 Routing Table

A routing table contains information used to determine where packets should be sent.

A route commonly includes:

| Field | Meaning |
|---|---|
| Destination prefix | The network or address range the route matches |
| Next hop | The next router to which the packet should be sent |
| Interface | The outgoing interface |
| Metric | A value used to compare routes within a routing protocol or route-selection process |
| Route source | How the route was learned, such as connected, static, or dynamic |

Example:

```text
Destination       Next Hop       Interface
192.168.1.0/24    directly connected eth0
10.10.0.0/16      192.168.1.254    eth0
0.0.0.0/0         192.168.1.1      eth0
```

Interpretation:
- `192.168.1.0/24` is directly connected.
- `10.10.0.0/16` is reached through `192.168.1.254`.
- The default route sends otherwise unmatched traffic to `192.168.1.1`.

---

### 12.3 Default Gateway

A default gateway is the next-hop router used when a destination does not match a more specific route in the host's routing table.

Example:

```text
Host IP:        192.168.1.20/24
Default gateway: 192.168.1.1
```

If the host sends a packet to `192.168.1.50`, the destination is in the same `/24` network, so the host can send directly to that destination on the LAN.

If the host sends a packet to `8.8.8.8`, the destination is outside the local `/24` network, so the host sends the packet to its default gateway.

The default gateway must be reachable through an appropriate local route.

---

### 12.4 Next-Hop Routing

The next hop is the router or Layer 3 device to which a packet is sent on its way to the destination.

Example:

```text
Host A ---> Router 1 ---> Router 2 ---> Network B
```

Router 1 may have a route like:

```text
Destination: 10.20.0.0/16
Next hop:    192.168.1.2
```

Router 1 forwards the packet to Router 2 at `192.168.1.2`.

The next hop is not necessarily the final destination. It is the next router along the selected path.

---

### 12.5 Directly Connected Routes

A directly connected route is created when an IP address and prefix are configured on an interface and the interface is active according to the operating system's routing rules.

Example:

```text
Interface: eth0
Address:   192.168.1.20/24
```

This creates a connected route for:

```text
192.168.1.0/24
```

The host can send packets to addresses in that subnet directly through `eth0`, typically resolving the destination's Layer 2 address using ARP for IPv4 or Neighbor Discovery for IPv6.

A connected route does not mean that every host in the subnet is reachable; the route only indicates that the network is considered directly reachable through that interface.

---

### 12.6 Static vs Dynamic Routing

#### Static routing

A static route is manually configured by an administrator.

Advantages:
- Simple for small networks.
- Predictable.
- No routing-protocol overhead.
- Useful for stub networks and specific paths.

Disadvantages:
- Requires manual maintenance.
- Does not automatically adapt to topology changes.
- Can become difficult to manage at scale.

#### Dynamic routing

Dynamic routing protocols exchange routing information and adapt to network changes.

Examples:
- OSPF
- BGP
- IS-IS
- RIP

Advantages:
- Can adapt to topology changes.
- Reduces manual route configuration in larger networks.
- Can select paths using protocol-specific algorithms.

Disadvantages:
- More complex.
- Requires careful configuration and security.
- Uses network and device resources.

| Static routing | Dynamic routing |
|---|---|
| Manually configured | Learned through a protocol |
| Simple and predictable | Adapts to changes |
| Limited scalability | Better suited to larger changing networks |
| No routing-protocol exchange | Exchanges routing information |

---

### 12.7 Longest-Prefix Match

Longest-prefix match is the main rule used by IP routers to select a route for a destination address.

The router selects the matching route with the most specific prefix, meaning the route with the greatest number of prefix bits.

Example routing table:

```text
10.0.0.0/8       via Router A
10.10.0.0/16     via Router B
10.10.20.0/24    via Router C
0.0.0.0/0        via Router D
```

Destination:

```text
10.10.20.50
```

The destination matches:
- `10.0.0.0/8`
- `10.10.0.0/16`
- `10.10.20.0/24`
- `0.0.0.0/0`

The selected route is:

```text
10.10.20.0/24 via Router C
```

because `/24` is the longest, most specific matching prefix.

> Longest-prefix match is different from route metric. Prefix specificity is evaluated first; metrics and route preferences help select among competing routes according to the routing system's rules.

---

### 12.8 Default Route

A default route is used when no more specific route matches the destination.

IPv4 default route:

```text
0.0.0.0/0
```

IPv6 default route:

```text
::/0
```

A `/0` prefix matches every IPv4 or IPv6 address, respectively.

Example:

```text
default via 192.168.1.1 dev eth0
```

This means unmatched IPv4 destinations are sent to `192.168.1.1` through `eth0`.

A default route does not guarantee Internet access. The next hop must be reachable and have a working path onward.

---

### 12.9 Route Metrics

A route metric is a value used to compare route choices.

In many systems, a lower metric is preferred among otherwise comparable routes. However, route selection also depends on factors such as:
- Prefix length
- Administrative distance or route preference
- Routing protocol rules
- Policy rules
- Platform-specific behavior

Metrics are not universally comparable between different routing protocols or operating systems.

Example:

```text
Route A: destination 10.0.0.0/8, metric 10
Route B: destination 10.0.0.0/8, metric 50
```

If the routes are otherwise comparable and the system prefers lower metrics, Route A is preferred.

---

### 12.10 ICMP and Routing Diagnostics

ICMP is used for network-layer control and diagnostic messages.

Common ICMP messages include:
- Echo Request
- Echo Reply
- Destination Unreachable
- Time Exceeded

#### Ping

`ping` commonly uses ICMP Echo Request and Echo Reply.

```bash
ping -c 4 192.168.1.1
```

This sends four echo requests to the target.

Ping can help test reachability, but a failed ping does not always mean the host is down. Firewalls may block ICMP.

#### Destination Unreachable

A router or host may send an ICMP Destination Unreachable message when it cannot deliver a packet or when a relevant policy prevents delivery.

The exact ICMP code helps identify the reason.

#### Time Exceeded

Routers decrement the IPv4 TTL or IPv6 Hop Limit when forwarding packets.

When the value reaches zero, a router discards the packet and may send an ICMP Time Exceeded message.

Traceroute uses this behavior to discover intermediate hops.

---

### 12.11 NAT vs Routing

NAT means Network Address Translation.

Routing forwards packets toward a destination network. NAT changes selected address or port information in packets.

#### Routing

A router uses the destination IP address and routing table to determine where to forward a packet.

#### NAT

NAT may change:
- Source IP address
- Destination IP address
- Source port
- Destination port

#### Example: source NAT

A private host:

```text
192.168.1.20
```

sends traffic toward the Internet. A NAT router may translate its source address to a public address:

```text
Before NAT:
Source:      192.168.1.20
Destination: 203.0.113.10

After NAT:
Source:      198.51.100.5
Destination: 203.0.113.10
```

The public addresses above are documentation examples, not real public endpoints.

NAT and routing often occur on the same device, but they are separate functions.

NAT is not, by itself, a complete firewall or security policy.

---

### 12.12 Policy-Based Routing (Overview)

Policy-Based Routing (PBR) allows packet forwarding decisions to be influenced by criteria other than, or in addition to, the ordinary destination-prefix route lookup.

Possible criteria include:
- Source IP address
- Incoming interface
- Traffic mark
- Protocol or port, depending on the platform

Example:

```text
Traffic from subnet A -> ISP 1
Traffic from subnet B -> ISP 2
```

PBR is useful for:
- Multi-WAN networks
- Traffic engineering
- Separating traffic by source
- Special routing requirements

PBR must be configured carefully because it can create unexpected paths or interfere with return traffic.

---

### 12.13 Asymmetric Routing (Overview)

Asymmetric routing occurs when traffic travels along different paths in each direction.

Example:

```text
Forward path:
Client ---> Router A ---> Server

Return path:
Server ---> Router B ---> Client
```

Asymmetric routing can occur in:
- Multi-homed networks
- Networks using multiple ISPs
- Large enterprise networks
- Load-balanced environments

#### Potential issues

- Stateful firewalls may not see both directions of a connection.
- Troubleshooting becomes more complex.
- Some security systems may reject traffic if they expect symmetric paths.

Asymmetric routing is not inherently wrong. Many networks operate with asymmetric paths successfully, provided routing and security systems support it.

---

### 12.14 BGP — Purpose and Basic Concepts

BGP stands for Border Gateway Protocol.

BGP is a path-vector routing protocol used to exchange routing information between Autonomous Systems (ASes). It is the primary routing protocol used to exchange reachability information across the public Internet.

#### Main purpose

BGP allows independently administered networks to announce which IP prefixes they can reach and to apply routing policies to those announcements.

#### Important concepts

- **Autonomous System (AS):** A network or group of networks under a common routing administration and policy.
- **ASN:** Autonomous System Number.
- **Prefix announcement:** A statement that a network is reachable through a particular AS.
- **AS_PATH:** The sequence of AS numbers through which a route has been advertised.
- **Policy:** Rules that influence which routes are accepted, preferred, or advertised.
- **eBGP:** BGP between different ASes.
- **iBGP:** BGP between routers within the same AS.

#### BGP is policy-driven

BGP does not simply choose the geographically shortest path. Its decisions depend on policy and attributes, including:
- Local preference
- AS_PATH
- MED
- Route origin
- Other implementation-specific and configured rules

BGP is designed to exchange routing information between networks with independent policies.

---

### 12.15 OSPF — Purpose and Basic Concepts

OSPF stands for Open Shortest Path First.

OSPF is a link-state interior gateway routing protocol used within an Autonomous System.

#### How OSPF works at a high level

1. Routers discover neighboring OSPF routers.
2. They exchange link-state information.
3. Routers build a link-state database for their area.
4. Each router runs the Shortest Path First (SPF) algorithm.
5. The resulting best paths are used to populate routing information.

#### Important concepts

- **Neighbor:** An OSPF router with which another router forms an adjacency or relationship.
- **Link-state advertisement (LSA):** Information describing network topology or reachability.
- **Link-state database (LSDB):** Collection of link-state information within an OSPF area.
- **Area:** A logical grouping of OSPF routers and links.
- **Cost:** The metric OSPF uses to represent path preference.
- **Area 0:** The OSPF backbone area.

OSPF is commonly used inside enterprise networks because it can adapt to topology changes and calculate paths based on configured costs.

---

### 12.16 Autonomous Systems (Overview)

An Autonomous System (AS) is a collection of IP networks and routers under a common administration that presents a consistent external routing policy.

Each public AS is identified by an Autonomous System Number (ASN).

ASNs are used by BGP.

#### Example

```text
AS 64500 ---- AS 64501 ---- AS 64502
```

These are example AS numbers. The diagram represents three independently identified routing domains exchanging reachability information.

#### Interior vs exterior routing

| Category | Purpose | Examples |
|---|---|---|
| Interior Gateway Protocol (IGP) | Routing within an AS | OSPF, IS-IS, RIP |
| Exterior Gateway Protocol (EGP) | Routing between ASes | BGP |

BGP is the modern protocol used for inter-AS routing on the Internet.

---

### 12.17 Traceroute and TTL / Hop-Limit Behavior

Traceroute discovers the path packets take through a network by sending probes with progressively increasing TTL or Hop Limit values.

#### IPv4 TTL

The IPv4 Time To Live (TTL) field is reduced by at least one at each router hop.

When the TTL reaches zero:
1. The router discards the packet.
2. The router may return an ICMP Time Exceeded message.
3. Traceroute records the router that responded.

#### IPv6 Hop Limit

IPv6 uses a Hop Limit field with similar behavior.

#### Example

```text
Probe 1: TTL = 1  -> Router 1 responds
Probe 2: TTL = 2  -> Router 2 responds
Probe 3: TTL = 3  -> Router 3 responds
```

This allows traceroute to reveal intermediate hops.

#### Linux commands

```bash
traceroute example.com
tracepath example.com
```

If `traceroute` is not installed, install it using your distribution's package manager or use `tracepath` if available.

Some networks filter or rate-limit traceroute probes. Therefore:
- A hop may show `* * *`.
- The path may appear incomplete.
- Different probe types may produce different results.
- The visible path may differ from the return path.

Traceroute shows the responses to its probes, not necessarily every forwarding detail of the network.

---

## Practical Tasks

> Perform these tasks on your own computer or an authorized lab network.

### Task 1: Inspect the Linux Routing Table

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.20
```

Interpretation:
- The default route uses `192.168.1.1`.
- The outgoing interface is `eth0`.
- The local network is `192.168.1.0/24`.
- The host's source address on that network is `192.168.1.20`.

To inspect IPv6 routes:

```bash
ip -6 route
```

### Task 2: Identify Your Default Gateway

Run:

```bash
ip route show default
```

Example:

```text
default via 192.168.1.1 dev eth0
```

The default gateway is `192.168.1.1`.

You can also inspect the route selected for a particular destination:

```bash
ip route get 8.8.8.8
```

This command shows the route and interface the Linux kernel would use for that destination.

### Task 3: Use Traceroute or Tracepath

Run:

```bash
traceroute 8.8.8.8
```

Or:

```bash
tracepath 8.8.8.8
```

Observe:
- The first hop, often your local router.
- The number of visible hops.
- Any timeouts.
- The approximate round-trip time to each responding hop.

A timeout does not automatically indicate a routing failure.

### Task 4: Diagnose a Missing Route in a Lab

Use an isolated lab or a network you are authorized to administer.

Example lab:

```text
Host A                 Router                 Host B
10.1.1.10/24      10.1.1.1 | 10.2.2.1      10.2.2.10/24
```

Assume Host A has no route to `10.2.2.0/24`.

Check the route:

```bash
ip route get 10.2.2.10
```

Inspect the table:

```bash
ip route
```

In a controlled lab, a temporary route can be added:

```bash
sudo ip route add 10.2.2.0/24 via 10.1.1.1
```

Then verify:

```bash
ip route get 10.2.2.10
```

Remove the temporary route when finished:

```bash
sudo ip route del 10.2.2.0/24
```

This example assumes `10.1.1.1` is a reachable router on Host A's local network and that the router has a working route to Host B's network.

### Task 5: Explain How a Router Forwards Packets

Suppose:

```text
Host A: 192.168.1.20/24
Gateway: 192.168.1.1
Host B: 192.168.2.30/24
```

Host A wants to send a packet to Host B.

1. Host A compares the destination IP address with its local subnet.
2. Host B is outside `192.168.1.0/24`.
3. Host A selects its default gateway, `192.168.1.1`.
4. Host A resolves the gateway's MAC address using ARP.
5. Host A sends an Ethernet frame to the gateway's MAC address. The IP packet's destination remains `192.168.2.30`.
6. The router receives the frame and removes the Layer 2 header.
7. The router examines the destination IP address.
8. The router performs a routing-table lookup using longest-prefix match.
9. The router selects an outgoing interface and next hop.
10. The router decrements the IPv4 TTL or IPv6 Hop Limit.
11. The router creates a new Layer 2 frame for the next link.
12. The packet continues toward Host B.

The Layer 2 frame changes at each routed hop, while the source and destination IP addresses normally remain the same unless a function such as NAT changes them.

---

## Quick Revision

| Concept | Key point |
|---|---|
| NIC | Connects a host to a network |
| Hub | Repeats signals to all ports |
| Switch | Forwards frames using MAC addresses |
| Router | Forwards packets between IP networks |
| Firewall | Enforces traffic security policy |
| Default gateway | Next hop for destinations without a more specific route |
| Routing table | Contains routes used for packet forwarding |
| Longest-prefix match | Selects the most specific matching route |
| Static route | Manually configured route |
| Dynamic route | Learned through a routing protocol |
| NAT | Translates address or port information |
| OSPF | Link-state routing protocol used within an AS |
| BGP | Path-vector protocol used to exchange routes between ASes |
| TTL / Hop Limit | Limits how many router hops a packet can traverse |
| Traceroute | Uses TTL/Hop Limit behavior to discover responding hops |

## Interview Questions

### 1. What is the difference between a switch and a router?

A switch primarily forwards Ethernet frames using MAC addresses within a Layer 2 network. A router forwards IP packets between different IP networks using a routing table.

### 2. What is a default gateway?

A default gateway is the router or Layer 3 device a host uses to reach destinations for which it has no more specific route.

### 3. What is longest-prefix match?

It is the process of selecting the matching route with the greatest prefix length, which represents the most specific matching destination network.

### 4. What is the difference between routing and NAT?

Routing selects where a packet should be forwarded. NAT modifies selected IP addresses or transport-layer ports as traffic passes through a device.

### 5. What is the difference between OSPF and BGP?

OSPF is an interior link-state routing protocol commonly used within one AS. BGP is a path-vector protocol used to exchange reachability information between ASes and apply routing policies.

### 6. Why does traceroute show asterisks?

Asterisks indicate that a probe did not receive a response within the expected time. The hop may filter, rate-limit, or fail to return the relevant response. It does not necessarily mean that the router is not forwarding traffic.

### 7. What happens when a router receives a packet?

The router processes the incoming Layer 2 frame, examines the destination IP address, selects a route, decrements TTL or Hop Limit, and forwards the packet in a new Layer 2 frame through the selected outgoing interface.

### 8. What is asymmetric routing?

Asymmetric routing occurs when traffic takes different paths in the forward and return directions. It can be valid, but may complicate stateful firewall inspection and troubleshooting.
