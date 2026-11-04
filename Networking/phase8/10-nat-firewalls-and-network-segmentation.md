
# Phase 8: NAT, Firewalls, and Network Segmentation

# 17. NAT — Network Address Translation

## 17.1 What Is Network Address Translation?

Network Address Translation (NAT) modifies IP address information in packets as they pass through a network device.

NAT is commonly used to allow devices with private IPv4 addresses to communicate with external networks using a public IPv4 address.

Example:

```text
Private network                  Internet
192.168.1.20 ---- Router/NAT ---- Public IP
```

Before NAT:

```text
Source IP:      192.168.1.20
Destination IP: 203.0.113.10
```

After source NAT:

```text
Source IP:      198.51.100.5
Destination IP: 203.0.113.10
```

The public addresses shown are documentation examples.

### Why NAT is used

- Conserves public IPv4 addresses.
- Allows multiple private hosts to share a public IPv4 address.
- Can hide internal address structure from external networks.
- Supports address translation between networks that use overlapping or different address spaces.

NAT is not a complete security mechanism. It does not replace a firewall or application security controls.

---

## 17.2 Private IPv4 Addresses

Private IPv4 addresses are reserved for use within private networks.

| Range | CIDR | Address count |
|---|---|---:|
| `10.0.0.0 – 10.255.255.255` | `10.0.0.0/8` | 16,777,216 |
| `172.16.0.0 – 172.31.255.255` | `172.16.0.0/12` | 1,048,576 |
| `192.168.0.0 – 192.168.255.255` | `192.168.0.0/16` | 65,536 |

Private addresses are not globally routable on the public Internet.

A typical home network may use:

```text
Router LAN IP: 192.168.1.1
Laptop:        192.168.1.20
Phone:         192.168.1.21
```

The router may translate these private source addresses to a public IPv4 address when devices access the Internet.

---

## 17.3 Static NAT

Static NAT maps one internal address to one external address using a fixed mapping.

Example:

```text
Internal host: 192.168.1.10
Public address: 198.51.100.10
```

Mapping:

```text
192.168.1.10 <----> 198.51.100.10
```

### Characteristics

- Usually a one-to-one address mapping.
- Mapping remains fixed.
- Can be useful when a system needs a consistent public address.
- Does not automatically imply that every inbound connection is permitted.

A firewall may still need a rule allowing inbound traffic.

---

## 17.4 Dynamic NAT

Dynamic NAT maps internal addresses to addresses selected from a configured public address pool.

Example:

```text
Private hosts                Public NAT pool
192.168.1.10  ------------> 198.51.100.10
192.168.1.11  ------------> 198.51.100.11
192.168.1.12  ------------> 198.51.100.12
```

The mapping is created dynamically and may change.

### Characteristics

- Uses a pool of public addresses.
- Often provides temporary one-to-one mappings.
- The pool may be exhausted if too many hosts need translation.
- Does not necessarily allow multiple hosts to share one public IP simultaneously.

---

## 17.5 PAT / NAT Overload

Port Address Translation (PAT), often called NAT overload, allows multiple private hosts to share one public IP address by translating transport-layer ports.

Example:

```text
Private host A: 192.168.1.20:51500
Private host B: 192.168.1.21:51500
                    |
                    v
                 NAT router
                    |
                    v
Public IP: 198.51.100.5
```

Possible translated mappings:

```text
192.168.1.20:51500 -> 198.51.100.5:40001
192.168.1.21:51500 -> 198.51.100.5:40002
```

The router tracks these mappings so return traffic can be directed to the correct internal host.

### Benefits

- Allows many private devices to share one public IPv4 address.
- Conserves public IPv4 addresses.
- Commonly used in home and small-business routers.

PAT is commonly used for outbound connections. It does not make internal services automatically reachable from outside.

---

## 17.6 Source NAT vs Destination NAT

### Source NAT (SNAT)

Source NAT modifies the source address of a packet.

Common use:
- Internal clients accessing external networks.

Example:

```text
Before:
192.168.1.20 -> 203.0.113.10

After:
198.51.100.5 -> 203.0.113.10
```

### Destination NAT (DNAT)

Destination NAT modifies the destination address of a packet.

Common use:
- Port forwarding
- Redirecting traffic to an internal server

Example:

```text
Before:
Client -> 198.51.100.5:443

After DNAT:
Client -> 192.168.1.50:443
```

### Comparison

| Source NAT | Destination NAT |
|---|---|
| Changes source address | Changes destination address |
| Often used for outbound traffic | Often used for inbound traffic |
| Can support private hosts accessing public networks | Can direct incoming traffic to internal services |

NAT implementations may also modify TCP or UDP ports and update checksums.

---

## 17.7 Port Forwarding

Port forwarding is a form of destination NAT that directs traffic arriving at a public IP address and port to an internal host and port.

Example:

```text
Public: 198.51.100.5:8443
             |
             v
Internal: 192.168.1.50:443
```

A forwarding rule might map:

```text
TCP 198.51.100.5:8443
        ->
TCP 192.168.1.50:443
```

### Common uses

- Hosting a service behind a home router.
- Accessing a lab service remotely.
- Publishing a specific internal application.

### Security risks

Port forwarding can expose an internal service to the Internet.

Before configuring it:
- Confirm the service needs external access.
- Patch the service.
- Require strong authentication.
- Restrict source addresses where possible.
- Use a VPN or secure access gateway when appropriate.
- Monitor logs.
- Avoid exposing management interfaces.

Port forwarding does not automatically secure the forwarded service.

---

## 17.8 NAT Traversal — Overview

NAT traversal refers to techniques that allow communication across NAT devices.

NAT can complicate peer-to-peer communication because internal hosts may not have globally reachable addresses.

Common technologies include:
- STUN
- TURN
- ICE

### STUN

STUN helps a client discover the public-facing address and port mapping observed by a server.

### TURN

TURN relays traffic when a direct peer-to-peer path cannot be established.

### ICE

ICE evaluates possible communication paths and selects a suitable connection method. It commonly uses STUN and TURN.

These technologies are used in applications such as real-time audio, video, and peer-to-peer communication.

---

## 17.9 NAT Limitations

NAT can create operational and security challenges.

### Limitations

- Breaks the simple end-to-end addressing model.
- Can complicate peer-to-peer applications.
- Makes inbound connections more difficult.
- Can complicate troubleshooting.
- May affect protocols that embed IP addresses in application data.
- Can create problems with IPsec or other protocols unless NAT traversal is supported.
- Does not provide application-level security.
- Can make attribution more difficult when many users share one public IP address.

NAT should not be treated as a substitute for access control.

---

## 17.10 NAT vs Firewall

NAT and firewalls are different functions.

| NAT | Firewall |
|---|---|
| Translates addresses or ports | Enforces traffic security policy |
| Maintains translation mappings | Evaluates traffic against rules |
| Can enable address sharing | Can allow, deny, or inspect traffic |
| Does not inherently provide full security policy | Designed to enforce security policy |

A home router often performs NAT and firewalling on the same device.

An outbound NAT mapping may allow related return traffic through a stateful firewall, but this behavior depends on the device's configuration.

---

## 17.11 Double NAT

Double NAT occurs when traffic passes through two devices that both perform NAT.

Example:

```text
Laptop
  |
Home Router
  | NAT #1
ISP Router
  | NAT #2
  |
Internet
```

### Potential problems

- Port forwarding may need configuration on both devices.
- Peer-to-peer applications may have difficulty establishing connections.
- Troubleshooting becomes more complex.
- VPNs or gaming applications may be affected.

Double NAT is common when a personal router is connected behind an ISP-provided router that also performs NAT.

Possible solutions include:
- Bridge mode on the upstream device, if supported.
- Configuring one device to route without NAT.
- Carefully configuring forwarding on both devices.
- Using a VPN or relay-based connection method when appropriate.

---

## 17.12 Hairpin NAT — Overview

Hairpin NAT, also called NAT loopback, allows an internal client to access an internal service using the network's public IP address or public DNS name.

Example:

```text
Internal client
     |
     v
Public address of router
     |
     v
NAT router
     |
     v
Internal web server
```

Without hairpin NAT, the internal client may not be able to use the public address to reach the internal server.

Hairpin NAT is useful when internal and external clients use the same public hostname.

---

# 18. Firewalls

## 18.1 What Is a Firewall?

A firewall is a security control that monitors and regulates network traffic according to a policy.

A firewall may:
- Allow traffic.
- Deny traffic.
- Track connection state.
- Inspect application data.
- Log events.
- Apply rate limits or other controls.

Firewalls can be implemented as:
- Network appliances
- Host software
- Cloud security controls
- Virtual network devices
- Application-layer services

---

## 18.2 Packet-Filtering Firewalls

A packet-filtering firewall evaluates packet fields such as:
- Source IP address
- Destination IP address
- Protocol
- Source port
- Destination port
- Incoming or outgoing interface

Example rule:

```text
Allow TCP traffic to destination port 443
```

A complete rule should specify relevant source and destination addresses, interfaces, direction, and policy context.

Packet filtering may be stateless or part of a stateful firewall.

---

## 18.3 Stateless Filtering

A stateless firewall evaluates packets independently.

It does not maintain a connection table to determine whether a packet belongs to an established connection.

### Advantages

- Simple.
- Can be efficient.
- Useful for basic filtering.

### Limitations

- Does not inherently track connection state.
- May require separate rules for return traffic.
- Has less context for evaluating packet sequences.

---

## 18.4 Stateful Firewalls

A stateful firewall tracks active connections or flows.

For TCP, it can use connection-state information to distinguish new traffic from traffic belonging to an established connection.

Common conceptual states include:
- NEW
- ESTABLISHED
- RELATED
- INVALID

Exact state names and behavior depend on the firewall implementation.

### Example policy

```text
Allow new outbound connections.
Allow related return traffic.
Deny unsolicited inbound connections.
```

Stateful filtering simplifies many policies, but it does not remove the need for careful rule configuration.

---

## 18.5 Application-Layer Firewalls

Application-layer firewalls inspect application-level information.

Depending on the firewall, this may include:
- HTTP methods
- Hostnames
- URLs
- Headers
- Protocol commands
- Application payloads

They can enforce rules that basic IP and port filtering cannot.

Application-layer inspection may require protocol decoding, TLS termination, or other capabilities.

---

## 18.6 Web Application Firewall (WAF)

A Web Application Firewall protects HTTP-based applications by inspecting web requests and responses.

A WAF may help detect or block:
- SQL injection patterns
- Cross-site scripting patterns
- Malicious request structures
- Known exploit signatures
- Abnormal request rates

### WAF placement

```text
Client
  |
  v
WAF / Reverse Proxy
  |
  v
Web Application
  |
  v
Database
```

### Important limitations

- A WAF does not fix vulnerable application code.
- Rules may produce false positives or false negatives.
- Encrypted traffic generally needs to be decrypted or terminated for inspection.
- Business-logic vulnerabilities may not be detected by generic rules.

A WAF is an additional defensive layer, not a replacement for secure development.

---

## 18.7 Inbound vs Outbound Rules

### Inbound rules

Control traffic entering a host or network.

Examples:
- Allow HTTPS to a public web server.
- Deny unsolicited connections to a workstation.
- Allow SSH only from a management subnet.

### Outbound rules

Control traffic leaving a host or network.

Examples:
- Allow DNS only to approved resolvers.
- Allow web access through an approved proxy.
- Restrict server connections to unnecessary destinations.

A secure policy considers both inbound and outbound traffic.

---

## 18.8 Allowlist vs Blocklist

### Allowlist

Only explicitly permitted traffic is allowed.

Advantages:
- Restrictive by default.
- Helps limit unexpected communication.
- Supports least privilege.

Challenges:
- Requires careful maintenance.
- May block legitimate traffic if incomplete.

### Blocklist

Traffic matching specified prohibited conditions is blocked, while other traffic may be allowed.

Advantages:
- Can be easier to deploy initially.
- Useful for known malicious sources or destinations.

Challenges:
- Unknown threats may not be listed.
- Rules can become outdated.

For sensitive systems, an allowlist-based policy is often preferred.

---

## 18.9 Default-Deny Policy

A default-deny firewall policy blocks traffic unless a rule explicitly allows it.

Example:

```text
1. Allow required inbound HTTPS.
2. Allow established and related traffic.
3. Allow required management traffic from a trusted subnet.
4. Deny all other inbound traffic.
```

The actual rule order and state handling depend on the firewall platform.

### Benefits

- Reduces exposed services.
- Makes allowed communication explicit.
- Supports least privilege.
- Limits accidental access.

A default-deny policy must be designed carefully to avoid disrupting required network functions.

---

## 18.10 Egress Filtering

Egress filtering controls outbound traffic leaving a host or network.

It can help:
- Limit unauthorized external connections.
- Reduce command-and-control communication.
- Restrict data exfiltration paths.
- Enforce approved DNS or proxy use.
- Reduce access to unnecessary services.

Example:

```text
Application server:
Allow outbound database traffic only to database subnet.
Allow DNS only to approved resolver.
Deny other unnecessary outbound connections.
```

Egress filtering is especially useful for servers that should communicate with only a limited set of destinations.

---

## 18.11 Firewall Logs

Firewall logs record events related to traffic policy.

Common log fields include:
- Timestamp
- Source IP
- Destination IP
- Source port
- Destination port
- Protocol
- Action: allow or deny
- Rule identifier
- Interface
- Connection state

### Why logs matter

- Troubleshooting blocked connections.
- Detecting unusual traffic.
- Investigating security incidents.
- Verifying policy behavior.
- Supporting audit requirements.

### Logging cautions

- Excessive logging can create noise.
- High-volume logging can consume storage or CPU.
- Sensitive information may appear in logs.
- Logs should be protected from unauthorized access or modification.

---

## 18.12 Linux nftables

`nftables` is the modern Linux packet-filtering framework.

It is used to configure:
- Packet filtering
- Stateful filtering
- NAT
- Traffic classification

The `nft` command manages rules.

### Inspect current rules

```bash
sudo nft list ruleset
```

### List tables

```bash
sudo nft list tables
```

### Important concepts

| Concept | Meaning |
|---|---|
| Table | Organizes rules for a family |
| Chain | Holds rules and may be attached to a packet-processing hook |
| Rule | Matches traffic and applies an action |
| Set | Stores reusable collections of values |
| Hook | Defines where a chain participates in packet processing |

Common address families include:
- `ip`
- `ip6`
- `inet`
- `arp`
- `bridge`
- `netdev`

The `inet` family can handle both IPv4 and IPv6 traffic.

### Example: inspect rules

```bash
sudo nft list ruleset
```

### Example: create an isolated test table

The following commands create a separate table and chain for a lab demonstration. They do not replace the system's existing firewall rules.

```bash
sudo nft add table inet labfilter
sudo nft add chain inet labfilter input \
  '{ type filter hook input priority 0; policy accept; }'
sudo nft list table inet labfilter
```

Remove the lab table when finished:

```bash
sudo nft delete table inet labfilter
```

> Be careful when modifying firewall rules on a remote system. An incorrect rule can disconnect you. Use a local console or a controlled lab, and keep a recovery path available.

---

## 18.13 UFW Basics

UFW stands for Uncomplicated Firewall.

It provides a simpler interface for configuring Linux firewall rules. On many Linux systems, UFW manages rules using the underlying firewall framework.

### Check status

```bash
sudo ufw status
sudo ufw status verbose
```

### Allow SSH

```bash
sudo ufw allow 22/tcp
```

### Allow HTTPS

```bash
sudo ufw allow 443/tcp
```

### Deny a port

```bash
sudo ufw deny 23/tcp
```

### Enable UFW

```bash
sudo ufw enable
```

### Disable UFW

```bash
sudo ufw disable
```

### Delete a rule

```bash
sudo ufw status numbered
sudo ufw delete <rule-number>
```

### Example: allow SSH only from a trusted subnet

```bash
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
```

Replace the example subnet with the actual trusted network.

### Important warning

Before enabling or changing UFW over SSH:
1. Confirm the required SSH rule exists.
2. Verify the source subnet is correct.
3. Keep access to a local console if possible.
4. Confirm the change does not interrupt your connection.

---

## 18.14 Network Firewall vs Host Firewall

| Network firewall | Host firewall |
|---|---|
| Protects a network boundary or segment | Protects an individual host |
| Controls traffic passing through it | Controls traffic entering or leaving the host |
| Often centrally managed | May be managed by the host or endpoint platform |
| Can protect multiple devices | Provides device-specific controls |

Both are useful.

A network firewall may not protect a device from traffic originating inside the same network segment. A host firewall can provide an additional layer of protection.

---

## 18.15 Common Firewall Misconfigurations

Common problems include:

- Allowing all inbound traffic.
- Exposing SSH, RDP, databases, or management interfaces publicly.
- Using overly broad source ranges.
- Creating duplicate or conflicting rules.
- Forgetting IPv6 rules.
- Allowing unnecessary outbound traffic.
- Logging too little or too much.
- Using incorrect rule order.
- Allowing a service without checking its authentication.
- Assuming NAT automatically blocks every inbound connection.
- Failing to review temporary rules.
- Leaving test services exposed.

### Review checklist

- Are only required ports open?
- Are source addresses restricted where possible?
- Are IPv4 and IPv6 both considered?
- Is the default policy appropriate?
- Are outbound connections restricted where necessary?
- Are logs enabled for meaningful events?
- Are rules documented and periodically reviewed?

---

## 18.16 Testing Firewall Rules Safely

Test firewall rules only on systems and networks you own or have explicit permission to assess.

### Local inspection

```bash
sudo nft list ruleset
sudo ufw status verbose
```

### Check listening services

```bash
ss -tuln
```

A listening service may still be blocked by a firewall.

### Test a specific service

From an authorized client:

```bash
nc -vz <target-ip> <port>
```

Example:

```bash
nc -vz 192.168.1.10 443
```

This tests TCP connection establishment. It does not prove that the application is secure or functioning correctly.

### Use a controlled test matrix

| Test | Expected result |
|---|---|
| Allowed source to allowed port | Connection permitted |
| Unapproved source to restricted port | Connection blocked |
| Unnecessary outbound connection | Blocked if egress policy denies it |
| Approved return traffic | Allowed according to stateful policy |

Record the expected and actual behavior. Do not run broad scans against networks without authorization.

---

# 19. VLANs, DMZ, and Network Segmentation

## 19.1 What Is Network Segmentation?

Network segmentation divides a network into smaller sections with controlled communication between them.

Segmentation can be based on:
- Department
- Device type
- Application role
- Security level
- Administrative ownership
- Business function

### Benefits

- Limits lateral movement.
- Reduces the impact of compromised devices.
- Restricts access to sensitive systems.
- Improves monitoring and policy enforcement.
- Separates guest, user, server, and management traffic.

Segmentation is effective only when communication between segments is controlled and reviewed.

---

## 19.2 VLANs

A VLAN is a Virtual Local Area Network.

A VLAN creates a logical Layer 2 broadcast domain within switching infrastructure.

Example:

```text
VLAN 10: Student devices
VLAN 20: Staff devices
VLAN 30: Servers
VLAN 40: Guest Wi-Fi
```

Devices in different VLANs are separated at Layer 2.

### VLAN tagging

IEEE 802.1Q defines VLAN tagging for Ethernet frames.

A VLAN tag identifies the VLAN associated with a frame on a tagged link.

### Access ports

An access port usually carries traffic for one VLAN and connects to an endpoint.

### Trunk ports

A trunk port carries traffic for multiple VLANs, commonly using 802.1Q tags.

Trunks are commonly used between:
- Switches
- Switches and routers
- Switches and Layer 3 switches
- Switches and virtualization hosts

Trunk configuration must be carefully restricted to the VLANs that are required.

---

## 19.3 Subnets vs VLANs

A subnet is a Layer 3 IP address range.

A VLAN is a Layer 2 logical network.

| VLAN | Subnet |
|---|---|
| Layer 2 concept | Layer 3 concept |
| Defines a broadcast domain | Defines an IP address range |
| Identified by a VLAN ID in 802.1Q environments | Identified by an IP prefix |
| Does not inherently provide an IP route | Used in IP routing decisions |

A common design uses one IP subnet per VLAN, but this is a network design convention rather than an absolute protocol requirement.

Example:

```text
VLAN 10 -> 192.168.10.0/24
VLAN 20 -> 192.168.20.0/24
```

---

## 19.4 Inter-VLAN Routing

Inter-VLAN routing allows devices in different VLANs to communicate at Layer 3.

It can be provided by:
- A router with VLAN interfaces
- A Layer 3 switch
- A firewall with VLAN interfaces

Example:

```text
VLAN 10 ---- Layer 3 Switch ---- VLAN 20
```

Each VLAN commonly has a gateway interface.

```text
VLAN 10 gateway: 192.168.10.1
VLAN 20 gateway: 192.168.20.1
```

### Security considerations

Inter-VLAN routing should not automatically allow all traffic.

Apply rules to control:
- Which source VLAN can reach which destination VLAN.
- Which services are permitted.
- Whether access is one-way or bidirectional.
- Which traffic should be logged.

---

## 19.5 DMZ — Demilitarized Zone

A DMZ is a network segment used to host systems that need to communicate with less-trusted networks, such as the Internet.

A DMZ helps separate public-facing services from internal systems.

Example:

```text
                 Internet
                    |
                 Firewall
                    |
             +------+------+
             |             |
            DMZ         Internal LAN
             |             |
          Web server     Database
```

A more controlled design may use separate firewall interfaces or policies for:
- Internet to DMZ
- DMZ to internal network
- Internal network to DMZ
- DMZ to Internet

### DMZ security principles

- Public services should not have unrestricted access to the internal network.
- Only required traffic should be allowed from DMZ systems.
- Administrative access should use a dedicated management path.
- DMZ hosts should be patched and monitored.
- Sensitive databases should generally remain in a more restricted zone.

A DMZ is a security boundary, not simply a subnet named "DMZ."

---

## 19.6 Internal vs External Network Zones

Networks can be divided into zones based on trust and function.

Example:

```text
External / Internet
        |
      Firewall
        |
      Public DMZ
        |
      Firewall
        |
    Internal LAN
        |
   Restricted Data Zone
```

Typical zones include:
- External network
- Public-facing DMZ
- User network
- Application server network
- Database network
- Management network
- Backup network

Each zone should have a defined purpose and allowed communication policy.

---

## 19.7 Guest Networks

A guest network provides connectivity for visitors or untrusted devices.

A guest network should generally:
- Be separated from internal business networks.
- Allow only necessary services.
- Restrict access to management interfaces.
- Use appropriate client isolation.
- Apply bandwidth or rate limits where needed.
- Provide controlled Internet access.

Guest Wi-Fi should not be treated as trusted merely because it uses the organization's wireless infrastructure.

---

## 19.8 Server Isolation

Server isolation separates servers based on their role and sensitivity.

Examples:
- Web servers
- Application servers
- Database servers
- Authentication servers
- Backup servers

A compromised web server should not automatically provide direct access to every database or management service.

### Example policy

```text
Internet -> Web server: HTTPS only
Web server -> App server: Required application port only
App server -> Database: Required database port only
User network -> Database: Deny by default
Management network -> Servers: Approved admin protocols only
```

This design limits unnecessary communication and helps reduce the impact of compromise.

---

## 19.9 Management Networks

A management network is a restricted network used to administer infrastructure.

Devices may include:
- Switch management interfaces
- Router management interfaces
- Firewall management interfaces
- Server administration interfaces
- Hypervisor management interfaces

### Security practices

- Restrict access to approved administrators.
- Avoid exposing management interfaces to the public Internet.
- Use secure protocols such as SSH and HTTPS.
- Require strong authentication and MFA where supported.
- Log administrative access.
- Separate management traffic from ordinary user traffic.

A management network should be treated as highly sensitive.

---

## 19.10 Microsegmentation — Overview

Microsegmentation applies fine-grained access controls between workloads, applications, or individual systems.

Instead of relying only on broad network zones, microsegmentation can define policies such as:

```text
Web tier -> App tier: Allow TCP 8443
App tier -> Database tier: Allow TCP 5432
Other traffic: Deny
```

Microsegmentation may be implemented through:
- Host firewalls
- Hypervisor or cloud network controls
- Distributed firewalls
- Identity-aware policy systems

### Benefits

- Limits lateral movement.
- Reduces unnecessary communication.
- Supports least privilege.
- Helps isolate compromised workloads.

Microsegmentation requires accurate application dependency mapping and ongoing policy maintenance.

---

## 19.11 Zero Trust Networking — Fundamentals

Zero Trust is a security approach based on the principle that access should not be granted solely because a user or device is inside a network perimeter.

A common principle is:

> Never trust automatically; verify explicitly.

Zero Trust commonly considers:
- User identity
- Device identity and health
- Resource sensitivity
- Context and risk
- Least-privilege access
- Continuous evaluation
- Strong authentication
- Segmentation

Zero Trust does not mean that every packet must be individually authenticated. It is an architecture and policy approach that combines identity, device, network, and resource controls.

---

## 19.12 Lateral Movement — Concept

Lateral movement occurs when an attacker who has compromised one system attempts to access other systems within the environment.

Example:

```text
Compromised workstation
        |
        v
Application server
        |
        v
Database server
```

Possible causes of successful lateral movement include:
- Excessive network access.
- Reused credentials.
- Weak internal authentication.
- Unpatched services.
- Poor segmentation.
- Unrestricted administrative protocols.

### Defensive measures

- Segment networks.
- Restrict access between application tiers.
- Use least privilege.
- Require strong authentication.
- Monitor east-west traffic.
- Patch systems.
- Limit administrative access.
- Detect unusual authentication and service activity.

---

## 19.13 Restricting Access Between Application Tiers

A common multi-tier application contains:

1. Web tier
2. Application tier
3. Database tier
4. Management tier

### Example architecture

```text
Internet
   |
   v
[Firewall / WAF]
   |
   v
[Web Tier]
   |
   v
[Application Tier]
   |
   v
[Database Tier]

[Management Network] ---> Approved admin access
```

### Recommended access policy

| Source | Destination | Example policy |
|---|---|---|
| Internet | Web tier | Allow required HTTPS |
| Internet | Application tier | Deny direct access |
| Internet | Database tier | Deny |
| Web tier | Application tier | Allow only required application port |
| Web tier | Database tier | Deny direct access unless specifically required |
| Application tier | Database tier | Allow only required database port |
| User network | Database tier | Deny by default |
| Management network | Server tiers | Allow approved administration only |

The specific ports depend on the application and database technology.

### Why this matters

If a public web server is compromised, segmentation can prevent the attacker from directly reaching the database or management interface.

Segmentation reduces risk, but it does not eliminate the need for:
- Secure application code
- Strong authentication
- Patch management
- Endpoint protection
- Monitoring
- Backups
- Incident response

---

# Practical Tasks

> Use a local lab, virtual machines, or networks you own or have explicit permission to administer.

## Task 1: Identify NAT in Your Network

Inspect your local interface and default route:

```bash
ip addr
ip route
```

Identify:
- Your private IPv4 address.
- Your default gateway.
- The interface used for Internet traffic.

A private address on your device may indicate that NAT is used upstream, but it does not prove exactly where or how NAT is configured.

## Task 2: Inspect Linux Firewall Rules

```bash
sudo nft list ruleset
sudo ufw status verbose
```

Record:
- Whether a firewall is active.
- Default input policy.
- Default output policy.
- Allowed services.
- Whether IPv6 rules are present.

Different Linux distributions may use different firewall management tools.

## Task 3: Inspect Listening Services

```bash
ss -tuln
```

For process details:

```bash
sudo ss -tulpn
```

Identify:
- Listening ports.
- Whether a service listens on `127.0.0.1`.
- Whether it listens on a specific interface.
- Whether it listens on all IPv4 or IPv6 interfaces.

A service listening on all interfaces may be reachable from more networks, depending on routing and firewall policy.

## Task 4: Build a Small Segmentation Lab

Use virtual machines or an isolated virtual network.

Example:

```text
Network A: 192.168.10.0/24
Network B: 192.168.20.0/24
```

Assign one VM to each network and use a router or Layer 3 device between them.

Test:
- Whether each VM can reach its own gateway.
- Whether inter-network routing works.
- Whether a firewall rule can permit one specific service.
- Whether other traffic is denied.

Do not change your primary network configuration unless you have a recovery path.

## Task 5: Design a Three-Tier Application Network

Create a diagram containing:
- Web server
- Application server
- Database server
- Firewall
- Management network

Write rules for:
- Internet to web server
- Web server to application server
- Application server to database
- Administrator to management interface
- All other traffic

Explain how the rules limit lateral movement.

---

# Quick Revision

| Concept | Key point |
|---|---|
| NAT | Modifies IP address or port information |
| Static NAT | Fixed one-to-one mapping |
| Dynamic NAT | Uses a pool of public addresses |
| PAT | Multiple private hosts share an address using ports |
| SNAT | Changes source address |
| DNAT | Changes destination address |
| Port forwarding | Directs incoming traffic to an internal service |
| Firewall | Enforces traffic security policy |
| Stateful firewall | Tracks connection state |
| Stateless firewall | Evaluates packets independently |
| WAF | Inspects and filters web application traffic |
| Default deny | Blocks traffic unless explicitly allowed |
| Egress filtering | Controls outbound traffic |
| VLAN | Logical Layer 2 broadcast domain |
| Subnet | Layer 3 IP address range |
| Inter-VLAN routing | Routes traffic between VLANs |
| DMZ | Separates public-facing systems from internal networks |
| Microsegmentation | Fine-grained access controls between workloads |
| Zero Trust | Access based on explicit verification and least privilege |
| Lateral movement | Attacker movement between systems after initial compromise |

---

# Interview Questions

## 1. What is NAT?

NAT modifies selected IP address or port information in packets. It is commonly used to allow private IPv4 hosts to communicate through a public IPv4 address.

## 2. What is the difference between static NAT and PAT?

Static NAT typically maps one internal IP address to one external IP address. PAT allows multiple internal hosts to share an external address by translating transport-layer ports.

## 3. Is NAT a firewall?

No. NAT translates addresses or ports. A firewall enforces security policy. A device can perform both functions, but they are distinct.

## 4. What is port forwarding?

Port forwarding directs traffic arriving at a public address and port to an internal address and port, commonly through destination NAT.

## 5. What is a stateful firewall?

A stateful firewall tracks active connections and uses connection state when deciding whether to permit traffic.

## 6. What is a WAF?

A Web Application Firewall inspects HTTP-based traffic and can help detect or block malicious web requests. It does not replace secure application development.

## 7. What is the difference between a VLAN and a subnet?

A VLAN is a Layer 2 logical network. A subnet is a Layer 3 IP address range. Networks commonly map one subnet to one VLAN.

## 8. What is a DMZ?

A DMZ is a network segment used to host systems that need to communicate with less-trusted networks while remaining separated from internal systems.

## 9. Why should a database not be directly exposed to the Internet?

A database contains sensitive information and generally does not need direct public access. Restricting it to approved application and management networks reduces exposure and limits lateral movement.

## 10. What is microsegmentation?

Microsegmentation applies fine-grained access controls between workloads or systems, allowing only the communication required for their roles.

## 11. What is lateral movement?

Lateral movement is an attacker's attempt to access additional systems after compromising an initial host.

## 12. How does network segmentation improve security?

Segmentation restricts communication between systems and zones. If one device is compromised, the attacker has fewer paths to other sensitive systems.
