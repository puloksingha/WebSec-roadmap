
# 5. Subnetting and CIDR

## 5.1 What Is a Subnet?

A **subnet** (subnetwork) is a logically divided portion of an IP network. Subnetting divides a larger network into smaller networks to improve address organization, routing, and network management.

For example, the network:

```text
192.168.1.0/24
```

can be divided into two smaller subnets:

```text
192.168.1.0/25
192.168.1.128/25
```

Each subnet has its own network address, host addresses, and broadcast address (for traditional IPv4 subnets).

### Why subnetting is used

- Organize devices into logical networks.
- Reduce broadcast domains.
- Improve network management.
- Allocate IP addresses efficiently.
- Separate departments, servers, and user devices.
- Support routing and security boundaries.

> A subnet is a logical network boundary. It does not automatically provide security; firewalls and access-control rules are still required.

---

## 5.2 Subnet Masks

An IPv4 address contains 32 bits.

A subnet mask identifies which bits belong to the network portion and which bits belong to the host portion.

- Network bits are represented by `1`.
- Host bits are represented by `0`.

Example:

```text
IP address:  192.168.1.10
Subnet mask: 255.255.255.0
CIDR:        /24
```

Binary representation:

```text
IP address:
11000000.10101000.00000001.00001010

Subnet mask:
11111111.11111111.11111111.00000000
```

The first 24 bits identify the network. The remaining 8 bits identify hosts within that network.

### Common subnet masks

| CIDR | Subnet mask | Network bits | Host bits |
|---|---|---:|---:|
| `/8` | `255.0.0.0` | 8 | 24 |
| `/16` | `255.255.0.0` | 16 | 16 |
| `/24` | `255.255.255.0` | 24 | 8 |
| `/25` | `255.255.255.128` | 25 | 7 |
| `/26` | `255.255.255.192` | 26 | 6 |
| `/27` | `255.255.255.224` | 27 | 5 |
| `/28` | `255.255.255.240` | 28 | 4 |
| `/29` | `255.255.255.248` | 29 | 3 |
| `/30` | `255.255.255.252` | 30 | 2 |

---

## 5.3 CIDR Notation

**CIDR** stands for Classless Inter-Domain Routing.

CIDR represents an IP address and its network prefix using slash notation.

Example:

```text
192.168.1.10/24
```

Here:

- `192.168.1.10` is the IP address.
- `/24` means the first 24 bits are network bits.
- The remaining 8 bits are host bits.

CIDR replaced the old class-based allocation approach with flexible network prefixes.

### CIDR formula

For IPv4:

```text
Host bits = 32 - Prefix length
```

The total number of addresses is:

```text
Total addresses = 2^(host bits)
```

For most traditional IPv4 subnets:

```text
Usable host addresses = 2^(host bits) - 2
```

The two reserved addresses are usually:

1. Network address
2. Broadcast address

The `-2` rule does not apply to `/31` point-to-point links or `/32` host routes.

---

## 5.4 Network Prefixes

A **network prefix** identifies the network portion of an IP address.

For example:

```text
192.168.10.25/24
```

The network prefix is:

```text
192.168.10.0/24
```

The host portion is:

```text
25
```

The network address is obtained by performing a bitwise AND operation between the IP address and subnet mask.

### Bitwise AND rules

| Input A | Input B | Result |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Example:

```text
IP:    192.168.1.10
Mask:  255.255.255.0
AND:   192.168.1.0
```

Therefore:

```text
Network address = 192.168.1.0
```

---

## 5.5 Common IPv4 Prefixes

| Prefix | Total addresses | Traditional usable hosts | Common use |
|---|---:|---:|---|
| `/8` | 16,777,216 | 16,777,214 | Very large network |
| `/16` | 65,536 | 65,534 | Large network |
| `/24` | 256 | 254 | Typical small LAN |
| `/25` | 128 | 126 | Half of a `/24` |
| `/26` | 64 | 62 | Smaller LAN |
| `/27` | 32 | 30 | Small network |
| `/28` | 16 | 14 | Small segment |
| `/29` | 8 | 6 | Small subnet |
| `/30` | 4 | 2 | Traditional point-to-point link |
| `/31` | 2 | 2 on a point-to-point link | Point-to-point connection |
| `/32` | 1 | 1 address represented | Single host route |

For traditional IPv4 subnets, the network and broadcast addresses are not assigned to ordinary hosts.

---

## 5.6 Calculating Network Addresses

### Method

1. Identify the CIDR prefix.
2. Convert the prefix into a subnet mask.
3. Apply the subnet mask to the IP address using bitwise AND.
4. The result is the network address.

### Example: Find the network address of `192.168.1.75/26`

A `/26` mask is:

```text
255.255.255.192
```

The final octet is divided into blocks of:

```text
256 - 192 = 64
```

The subnet ranges begin at:

```text
0
64
128
192
```

The IP address `192.168.1.75` falls in the block beginning at `64`.

Therefore:

```text
Network address = 192.168.1.64
```

---

## 5.7 Calculating Broadcast Addresses

The **broadcast address** is the final address in a traditional IPv4 subnet. It is used to send a packet to all hosts on that subnet.

For a traditional subnet, all host bits are set to `1`.

### Example: Find the broadcast address of `192.168.1.75/26`

The subnet block is:

```text
192.168.1.64 - 192.168.1.127
```

Therefore:

```text
Broadcast address = 192.168.1.127
```

### Full result

```text
IP address:       192.168.1.75/26
Subnet mask:      255.255.255.192
Network address:  192.168.1.64
First usable:     192.168.1.65
Last usable:      192.168.1.126
Broadcast:        192.168.1.127
```

---

## 5.8 Usable Host Ranges

For a traditional IPv4 subnet:

```text
First usable host = Network address + 1
Last usable host  = Broadcast address - 1
```

Example:

```text
Network:   10.0.0.0/24
Broadcast: 10.0.0.255
```

Usable host range:

```text
10.0.0.1 - 10.0.0.254
```

Total usable hosts:

```text
2^8 - 2 = 254
```

---

## 5.9 Number of Addresses per Subnet

### Formula

```text
Host bits = 32 - prefix
Total addresses = 2^(host bits)
```

For traditional IPv4 subnets:

```text
Usable hosts = Total addresses - 2
```

### Example: `/27`

```text
Host bits = 32 - 27
          = 5

Total addresses = 2^5
                = 32

Traditional usable hosts = 32 - 2
                         = 30
```

### Quick calculation table

| Prefix | Host bits | Total addresses | Traditional usable hosts |
|---|---:|---:|---:|
| `/24` | 8 | 256 | 254 |
| `/25` | 7 | 128 | 126 |
| `/26` | 6 | 64 | 62 |
| `/27` | 5 | 32 | 30 |
| `/28` | 4 | 16 | 14 |
| `/29` | 3 | 8 | 6 |
| `/30` | 2 | 4 | 2 |

---

## 5.10 Subnetting Practice

### Example 1: `192.168.10.0/24` divided into four equal subnets

A `/24` contains 256 addresses.

To create four equal subnets:

```text
2^2 = 4
```

Borrow 2 host bits:

```text
/24 + 2 = /26
```

Each `/26` contains 64 addresses.

| Subnet | Network address | Usable range | Broadcast |
|---|---|---|---|
| 1 | `192.168.10.0/26` | `.1 - .62` | `.63` |
| 2 | `192.168.10.64/26` | `.65 - .126` | `.127` |
| 3 | `192.168.10.128/26` | `.129 - .190` | `.191` |
| 4 | `192.168.10.192/26` | `.193 - .254` | `.255` |

### Example 2: Find the subnet for `172.16.5.130/25`

A `/25` has 128 addresses per block.

The last-octet blocks are:

```text
0 - 127
128 - 255
```

The address `172.16.5.130` belongs to the second block.

```text
Network:   172.16.5.128
Broadcast: 172.16.5.255
Usable:    172.16.5.129 - 172.16.5.254
```

### Practice questions

Try solving these without a calculator:

1. Find the network and broadcast addresses of `192.168.2.45/27`.
2. Find the usable host range of `10.10.10.100/26`.
3. How many total addresses exist in a `/28`?
4. How many traditional usable hosts exist in a `/29`?
5. Divide `192.168.20.0/24` into eight equal subnets.
6. Find the subnet of `172.16.8.200/28`.

---

## 5.11 VLSM — Variable Length Subnet Masking

**VLSM** allows different subnet sizes to be used within the same larger network.

Instead of dividing a network into equal-sized subnets, VLSM allocates subnet sizes according to actual host requirements.

### Why VLSM is useful

- Reduces wasted IP addresses.
- Supports networks with different host requirements.
- Allows flexible network design.
- Helps allocate address space efficiently.

### Example

Suppose the network `192.168.10.0/24` must support:

- Network A: 100 hosts
- Network B: 50 hosts
- Network C: 20 hosts
- Network D: 10 hosts

Allocate the largest subnet first.

| Network | Host requirement | Required prefix | Total addresses |
|---|---:|---|---:|
| A | 100 | `/25` | 128 |
| B | 50 | `/26` | 64 |
| C | 20 | `/27` | 32 |
| D | 10 | `/28` | 16 |

One valid allocation:

| Network | Network address | Usable range | Broadcast |
|---|---|---|---|
| A | `192.168.10.0/25` | `.1 - .126` | `.127` |
| B | `192.168.10.128/26` | `.129 - .190` | `.191` |
| C | `192.168.10.192/27` | `.193 - .222` | `.223` |
| D | `192.168.10.224/28` | `.225 - .238` | `.239` |

Addresses `192.168.10.240 - 192.168.10.255` remain unallocated.

### VLSM procedure

1. List all subnet host requirements.
2. Sort requirements from largest to smallest.
3. Find the smallest subnet that can support each requirement.
4. Allocate each subnet on a valid network boundary.
5. Ensure that allocated ranges do not overlap.
6. Record network, usable range, and broadcast addresses.

---

## 5.12 Route Aggregation and Summarization

**Route aggregation**, also called **route summarization**, combines multiple contiguous network routes into one larger route.

This reduces the number of entries in routing tables.

### Example

These four networks:

```text
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24
```

can be summarized as:

```text
192.168.0.0/22
```

A `/22` contains:

```text
2^(32 - 22) = 1024 addresses
```

### Requirements for valid summarization

- Networks must be contiguous.
- Networks must share a common prefix.
- The number of networks should align with a power-of-two block.
- The summary network must begin on the correct boundary.

Route summarization reduces routing-table size but must be configured carefully. An overly broad summary can direct traffic toward a network that does not actually contain the destination.

---

## 5.13 Supernetting Fundamentals

**Supernetting** combines multiple smaller networks into a larger network by using a shorter prefix.

For example:

```text
192.168.0.0/24
192.168.1.0/24
```

can be combined into:

```text
192.168.0.0/23
```

Supernetting is closely related to route aggregation.

```text
Smaller networks → One larger summarized network
```

A supernet uses fewer network bits and more host bits.

---

## 5.14 Special Cases: `/31` and `/32`

### `/31`

A `/31` contains two IPv4 addresses.

```text
Host bits = 32 - 31 = 1
Total addresses = 2^1 = 2
```

On point-to-point links, both addresses can be used as endpoint addresses under RFC 3021. There is no traditional network/broadcast address exclusion for this use.

Example:

```text
10.0.0.0/31
```

The two endpoint addresses are:

```text
10.0.0.0
10.0.0.1
```

A `/31` is not generally used for ordinary multi-access LANs.

### `/32`

A `/32` represents exactly one IPv4 address.

Example:

```text
192.168.1.10/32
```

It is commonly used for:

- Host routes
- Loopback interface addresses
- Routing entries for a single destination
- Firewall rules that match one IP address

A `/32` does not represent a normal multi-host subnet.

---

# 6. IPv6 Fundamentals

## 6.1 Why IPv6 Was Introduced

IPv6 was introduced primarily because the IPv4 address space was becoming insufficient for the growing number of internet-connected devices.

IPv4 uses 32-bit addresses:

```text
2^32 = 4,294,967,296 addresses
```

IPv6 uses 128-bit addresses:

```text
2^128 ≈ 3.4 × 10^38 addresses
```

IPv6 provides an enormously larger address space.

### Other reasons for IPv6

- Supports a much larger address space.
- Reduces the need for widespread address sharing through NAT.
- Supports hierarchical address allocation and routing.
- Simplifies certain aspects of the IP header.
- Supports automatic address configuration.
- Uses multicast instead of IPv4-style broadcast.
- Includes standardized support for IP-layer security mechanisms.

> IPv6 does not automatically make a network secure. Firewall configuration, patching, and secure network design are still essential.

---

## 6.2 IPv6 Address Structure

An IPv6 address is 128 bits long.

It is written as eight groups of four hexadecimal digits separated by colons.

Example:

```text
2001:0db8:0000:0000:0000:ff00:0042:8329
```

Each group contains 16 bits.

```text
8 groups × 16 bits = 128 bits
```

### Structure

```text
2001 : 0db8 : 0000 : 0000 : 0000 : ff00 : 0042 : 8329
 16     16      16     16      16     16      16      16 bits
```

An IPv6 address is divided into:

- Network prefix
- Interface identifier

The exact division depends on the prefix length. A common LAN allocation is `/64`, which leaves 64 bits for the interface identifier.

---

## 6.3 Hexadecimal Representation

IPv6 uses hexadecimal digits:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Each hexadecimal digit represents 4 bits.

Example:

```text
A = 1010
F = 1111
```

A group of four hexadecimal digits contains:

```text
4 × 4 = 16 bits
```

Hexadecimal makes 128-bit addresses more readable than binary.

---

## 6.4 IPv6 Shorthand and Address Compression

IPv6 allows two main shorthand rules.

### Rule 1: Remove leading zeros from a group

Full address:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

Remove leading zeros:

```text
2001:db8:0:0:0:0:0:1
```

Leading zeros can be removed from each group, but trailing zeros cannot be removed.

### Rule 2: Replace one consecutive sequence of zero groups with `::`

Compressed address:

```text
2001:db8::1
```

The `::` shorthand can be used only once in an address because multiple occurrences would make the number of omitted groups ambiguous.

### Example

Full:

```text
fe80:0000:0000:0000:0200:00ff:fe00:0001
```

Compressed:

```text
fe80::200:ff:fe00:1
```

---

## 6.5 Global Unicast Addresses

A **Global Unicast Address (GUA)** is an IPv6 address intended to be globally routable on the public internet.

The commonly used global unicast range is:

```text
2000::/3
```

Addresses in this range begin with binary bits `001`.

Example:

```text
2001:4860:4860::8888
```

Global unicast addresses are similar in purpose to public IPv4 addresses.

However, an address being globally routable does not mean that a device is reachable from the internet. Firewalls and routing policies determine actual reachability.

---

## 6.6 Link-Local Addresses

Link-local IPv6 addresses are used for communication on the local network link.

Range:

```text
fe80::/10
```

Example:

```text
fe80::1
```

Characteristics:

- Automatically assigned in many IPv6 configurations.
- Used for Neighbor Discovery.
- Used by many routing protocols.
- Not routed between different network links.
- Often required even when a device has no global IPv6 address.

A link-local address may require a **zone index** or interface identifier when used on a machine with multiple network interfaces.

Example on Linux:

```bash
ping -6 fe80::1%eth0
```

The `%eth0` identifies the interface used for the link-local destination.

---

## 6.7 Unique Local Addresses

**Unique Local Addresses (ULAs)** are intended for private internal IPv6 communication.

Range:

```text
fc00::/7
```

In common local use, ULAs are generated from the `fd00::/8` portion.

Example:

```text
fd12:3456:789a::1
```

ULAs are similar in purpose to private IPv4 ranges such as:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

ULAs are not intended to be globally routed on the public internet.

---

## 6.8 Multicast Addresses

IPv6 multicast addresses identify a group of interfaces.

Range:

```text
ff00::/8
```

A packet sent to a multicast address is delivered to members of the relevant multicast group.

IPv6 uses multicast for functions such as:

- Neighbor Discovery
- Router Discovery
- Service discovery
- Multicast applications

IPv6 does not use broadcast addresses. Multicast provides more targeted group communication.

---

## 6.9 Loopback Address: `::1`

The IPv6 loopback address is:

```text
::1
```

It is equivalent in purpose to IPv4 loopback:

```text
127.0.0.1
```

It refers to the local machine.

Example:

```bash
ping -6 ::1
```

This tests the local IPv6 stack and does not require a network connection to another machine.

---

## 6.10 Unspecified Address: `::`

The IPv6 unspecified address is:

```text
::
```

It represents the absence of an address.

It is similar in purpose to IPv4:

```text
0.0.0.0
```

Common uses include:

- A source address before a device has obtained a valid IPv6 address.
- Binding a service to all local IPv6 interfaces, depending on the application and operating system.

The unspecified address is not assigned to an ordinary interface as a normal usable address and is not used as a destination for normal communication.

---

## 6.11 IPv6 Prefix Notation

IPv6 uses CIDR-style prefix notation.

Example:

```text
2001:db8:abcd:0012::/64
```

The `/64` means the first 64 bits are the network prefix.

A `/64` is commonly used for an IPv6 LAN.

### Common IPv6 prefixes

| Prefix | Meaning |
|---|---|
| `/32` | Often used for a large provider allocation |
| `/48` | Common site-level allocation |
| `/56` | Common smaller-site allocation |
| `/64` | Typical IPv6 LAN subnet |
| `/128` | One specific IPv6 address |

These are common allocation patterns, not universal rules. Actual allocations depend on the network provider and design.

---

## 6.12 SLAAC — Stateless Address Autoconfiguration

**SLAAC** allows an IPv6 device to configure its own address without requiring a DHCPv6 server to assign the address.

### Basic process

1. The device creates a link-local address.
2. The device performs Duplicate Address Detection (DAD).
3. The device receives Router Advertisement (RA) messages from a router.
4. The RA provides network-prefix information and other configuration flags.
5. The device forms an IPv6 address using the advertised prefix and an interface identifier.
6. The device performs DAD for the resulting address.

### Router Advertisement information may include

- IPv6 prefix
- Prefix lifetime
- Whether the prefix can be used for SLAAC
- Whether a router is available as a default router
- Flags indicating whether DHCPv6 may provide additional configuration

SLAAC does not necessarily provide every configuration detail, such as DNS server information, in every environment. Other mechanisms may be used.

---

## 6.13 DHCPv6

**DHCPv6** is a protocol used to provide IPv6 configuration information to clients.

It can be used for:

- Address assignment
- DNS server information
- Other configuration parameters

### DHCPv6 modes

**Stateful DHCPv6**

The DHCPv6 server assigns and tracks IPv6 addresses for clients.

**Stateless DHCPv6**

Clients may use SLAAC to create their addresses while DHCPv6 provides additional configuration information.

DHCPv6 does not replace IPv6 Router Advertisements for default-router discovery. Clients typically learn the default router through Router Advertisement messages.

---

## 6.14 Neighbor Discovery Protocol (NDP)

IPv6 Neighbor Discovery Protocol operates using ICMPv6.

It performs functions that include:

- Discovering neighboring devices on the local link.
- Resolving IPv6 addresses to link-layer addresses.
- Discovering routers.
- Detecting whether an address is already in use.
- Maintaining neighbor reachability information.

NDP uses ICMPv6 messages such as:

| Message | Purpose |
|---|---|
| Router Solicitation (RS) | A host asks routers to send advertisements |
| Router Advertisement (RA) | A router advertises network information |
| Neighbor Solicitation (NS) | Used for address resolution and DAD |
| Neighbor Advertisement (NA) | Responds to neighbor solicitations or advertises neighbor information |
| Redirect | Informs a host of a better next hop in certain cases |

### Security relevance

NDP is important to IPv6 network security. Rogue Router Advertisements or malicious neighbor messages can affect local network traffic.

Network protections may include:

- Router Advertisement Guard (RA Guard)
- Switch-level IPv6 security controls
- Appropriate ICMPv6 filtering
- Monitoring for unexpected router advertisements

Do not block all ICMPv6 traffic indiscriminately. IPv6 relies on ICMPv6 for important network functions.

---

## 6.15 IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address length | 32 bits | 128 bits |
| Address format | Decimal | Hexadecimal |
| Example | `192.168.1.10` | `2001:db8::10` |
| Address space | About 4.3 billion | About 3.4 × 10^38 |
| Header | Variable length | Fixed base header |
| Broadcast | Supported | Not used |
| Multicast | Supported | Supported and widely used |
| Address configuration | Manual, DHCP | SLAAC, DHCPv6, manual |
| Address resolution | ARP | Neighbor Discovery |
| NAT | Commonly used | Not required for address conservation |
| IPsec | Supported | Standardized support |

IPv6 does not make NAT impossible, but NAT is generally not required to conserve IPv6 address space.

---

## 6.16 Dual-Stack Networks

A **dual-stack network** supports both IPv4 and IPv6.

A device may have:

```text
IPv4: 192.168.1.20
IPv6: 2001:db8:1234:1::20
```

The device can communicate using either protocol, depending on:

- Destination address availability
- DNS responses
- Routing
- Application behavior
- Network policy

### Benefits

- Supports gradual migration to IPv6.
- Maintains compatibility with IPv4 services.
- Allows IPv6 deployment without immediately removing IPv4.

### Security consideration

A network may have strong IPv4 firewall rules but weak or missing IPv6 firewall rules. This can create an unintended path into the network.

IPv6 must be included in firewall policy and security monitoring.

---

## 6.17 IPv6 Security Considerations

IPv6 introduces different network behaviors and attack surfaces.

### Common security concerns

- IPv6 may be enabled even when administrators believe the network is IPv4-only.
- Devices may automatically configure IPv6 addresses.
- Rogue Router Advertisements can affect host configuration.
- Neighbor Discovery can be abused on local networks.
- IPv6 firewall rules may be incomplete.
- Tunnels and transition mechanisms can create unexpected paths.
- Monitoring tools may not capture IPv6 traffic correctly if not configured.

### Defensive practices

1. Inventory IPv6 addresses and interfaces.
2. Review IPv6 routes and firewall rules.
3. Monitor IPv6 traffic as well as IPv4.
4. Use Router Advertisement Guard where appropriate.
5. Disable unused transition mechanisms according to organizational policy.
6. Avoid blindly disabling IPv6 if operating-system services depend on it.
7. Apply least-privilege firewall rules to IPv6.
8. Test exposure from an authorized external vantage point.

---

## 6.18 IPv6 Exposure and Firewall Configuration

A host with a global IPv6 address may be reachable over IPv6 if routing and firewall policy permit it.

This is important because IPv4 NAT may provide a false sense of protection. NAT is not itself a firewall, and IPv6 devices still need explicit firewall controls.

### Linux firewall inspection

Check firewall status and rules:

```bash
sudo ufw status verbose
sudo nft list ruleset
```

Depending on the distribution, the system may use UFW, nftables, firewalld, or another firewall manager.

### Check whether UFW handles IPv6

Inspect:

```bash
grep '^IPV6=' /etc/default/ufw
```

A typical UFW configuration that manages IPv6 has:

```text
IPV6=yes
```

Do not change firewall rules on a remote machine unless you have a safe recovery path. Incorrect rules can disconnect you.

---

# Practical Tasks

## Task 1: Inspect IPv4 and IPv6 Addresses on Linux

Run:

```bash
ip address
```

Short form:

```bash
ip a
```

Show IPv4 addresses:

```bash
ip -4 address
```

Show IPv6 addresses:

```bash
ip -6 address
```

Look for:

- Interface name, such as `eth0`, `ens33`, or `wlan0`
- IPv4 address
- IPv6 link-local address
- IPv6 global address, if present
- Prefix length, such as `/24` or `/64`

Example:

```text
inet 192.168.1.20/24
inet6 fe80::1234:5678:abcd:1/64
```

The `inet` line is IPv4. The `inet6` line is IPv6.

---

## Task 2: Calculate a `/24` Subnet and Host Range

Given:

```text
IP address: 192.168.1.50/24
```

Expected result:

```text
Subnet mask:      255.255.255.0
Network address:  192.168.1.0
First usable:     192.168.1.1
Last usable:      192.168.1.254
Broadcast:        192.168.1.255
Total addresses:  256
Usable hosts:     254
```

You can also use Python's standard library:

```python
import ipaddress

network = ipaddress.ip_interface("192.168.1.50/24").network

print("Network:", network.network_address)
print("Netmask:", network.netmask)
print("Broadcast:", network.broadcast_address)
print("Total addresses:", network.num_addresses)
print("Usable hosts:", network.num_addresses - 2)
```

For a traditional IPv4 subnet, the usable range can be inspected with:

```python
import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")

hosts = list(network.hosts())

print("First usable:", hosts[0])
print("Last usable:", hosts[-1])
```

For very large networks, avoid converting every host into a list. Use an iterator or calculate the boundaries directly.

---

## Task 3: Inspect Your Default Route

Run:

```bash
ip route
```

Look for a line similar to:

```text
default via 192.168.1.1 dev eth0
```

This means:

- `default`: route used when no more specific route matches.
- `via 192.168.1.1`: next-hop router.
- `dev eth0`: interface used to reach the router.

Inspect IPv6 routes:

```bash
ip -6 route
```

Look for:

```text
default via fe80::1 dev eth0
```

The default router may use a link-local IPv6 address.

---

## Task 4: Determine Whether Your Machine Has IPv6 Connectivity

### Step 1: Check local IPv6 addresses

```bash
ip -6 address
```

### Step 2: Check IPv6 routes

```bash
ip -6 route
```

A default route may look like:

```text
default via fe80::1 dev eth0
```

### Step 3: Test the local IPv6 stack

```bash
ping -6 ::1
```

This checks the local stack only. It does not prove internet connectivity.

### Step 4: Test an external IPv6 destination

```bash
ping -6 2606:4700:4700::1111
```

This is an IPv6 address associated with Cloudflare's public DNS service.

If the ping fails, it does not conclusively prove that IPv6 connectivity is unavailable. ICMP may be filtered.

### Step 5: Test DNS and HTTPS over IPv6

```bash
curl -6 https://example.com
```

If the command succeeds, your machine can reach the destination using IPv6 and resolve the domain in a way that supports the connection.

---

## Useful Linux Networking Commands

| Command | Purpose |
|---|---|
| `ip address` | Display interface addresses |
| `ip -4 address` | Display IPv4 addresses |
| `ip -6 address` | Display IPv6 addresses |
| `ip route` | Display IPv4 routes |
| `ip -6 route` | Display IPv6 routes |
| `ip neigh` | Display IPv4 neighbor table |
| `ip -6 neigh` | Display IPv6 neighbor table |
| `ping -4 example.com` | Test IPv4 reachability |
| `ping -6 example.com` | Test IPv6 reachability |
| `curl -4 https://example.com` | Test HTTPS using IPv4 |
| `curl -6 https://example.com` | Test HTTPS using IPv6 |
| `sudo nft list ruleset` | Inspect nftables firewall rules |

---

## Cybersecurity Connection

Subnetting and IPv6 knowledge are important for:

- Understanding network boundaries.
- Interpreting scan results.
- Identifying which addresses belong to a target network.
- Understanding routing and network segmentation.
- Recognizing IPv6 exposure that may be overlooked.
- Reviewing firewall policies.
- Understanding how local-network attacks can involve ARP, NDP, or Router Advertisements.

Only scan or test systems and networks you own or have explicit permission to assess.

---

## Interview Questions

1. What is subnetting, and why is it used?
2. What does `/24` mean in CIDR notation?
3. How many total addresses and traditional usable hosts exist in a `/26`?
4. What is the difference between a network address and a broadcast address?
5. How do you calculate a network address?
6. What is VLSM?
7. What is route summarization?
8. What is the purpose of a `/31` subnet?
9. What does a `/32` represent?
10. Why was IPv6 introduced?
11. What is the difference between global unicast and link-local IPv6 addresses?
12. What is the purpose of `::1`?
13. What is SLAAC?
14. What is the role of DHCPv6?
15. What does Neighbor Discovery do in IPv6?
16. Why is IPv6 firewall configuration important even on an IPv4-focused network?

---

## Summary

- A subnet divides an IP network into smaller logical networks.
- CIDR represents the network prefix using slash notation.
- IPv4 subnet size is calculated using `2^(32 - prefix)`.
- Traditional IPv4 usable host count is usually total addresses minus two.
- VLSM allocates different subnet sizes according to requirements.
- Route summarization combines contiguous networks into a shorter prefix.
- IPv6 uses 128-bit addresses and hexadecimal notation.
- IPv6 uses multicast rather than broadcast.
- SLAAC and DHCPv6 can provide IPv6 configuration.
- Neighbor Discovery performs important local-link functions.
- IPv6 must be included in firewall configuration and security monitoring.
