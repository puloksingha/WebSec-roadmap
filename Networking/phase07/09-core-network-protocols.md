
# Phase 7: Core Network Protocols

# 13. DNS — Domain Name System

## 13.1 What Is DNS?

The Domain Name System (DNS) is a distributed, hierarchical naming system that translates domain names into information such as IP addresses.

Humans use names such as:

```text
example.com
```

Networks use IP addresses to route traffic, such as:

```text
93.184.216.34
```

DNS can provide many types of information, not just IP addresses.

### Why DNS is important

- Maps domain names to IP addresses.
- Supports email routing.
- Provides service discovery.
- Enables reverse IP-to-name lookups.
- Supports security and verification mechanisms.

DNS is often described as the Internet's phonebook, but technically it is a distributed database with a hierarchy and caching system.

---

## 13.2 Domain Names and Fully Qualified Domain Names

A domain name is a human-readable name in the DNS namespace.

Example:

```text
www.example.com
```

The name is composed of labels separated by dots:

```text
www . example . com .
 |       |       |   |
host   domain    TLD root
```

The final root dot is usually omitted in everyday use.

### Fully Qualified Domain Name (FQDN)

An FQDN identifies a complete name in the DNS hierarchy, ending at the root.

Example:

```text
www.example.com.
```

The trailing dot represents the DNS root.

A name without the final dot may be interpreted as a relative name in some DNS configuration contexts.

---

## 13.3 DNS Hierarchy

DNS is organized hierarchically.

```text
                    Root (.)
                       |
          +------------+------------+
          |            |            |
         .com         .org         .net
          |
       example
          |
         www
```

The hierarchy includes:

1. **Root:** The top of the DNS namespace.
2. **Top-Level Domain (TLD):** Examples include `.com`, `.org`, `.net`, and country-code TLDs such as `.in`.
3. **Second-level domain:** For example, `example` in `example.com`.
4. **Subdomain or host label:** For example, `www` in `www.example.com`.

The term "subdomain" describes a name below another domain in the hierarchy. A host label may be used for a server, but DNS names are not necessarily tied to physical hosts.

---

## 13.4 Root, TLD, and Authoritative Name Servers

### Root name servers

Root name servers provide referrals to the appropriate TLD name servers.

They do not normally contain the final IP address for every domain.

### TLD name servers

TLD name servers provide referrals to authoritative name servers for domains within that TLD.

For example, a `.com` name server can refer a resolver to the authoritative servers for `example.com`.

### Authoritative name servers

An authoritative name server stores or serves DNS records for a zone.

It provides authoritative answers for names within that zone.

### Example hierarchy

```text
Resolver
   |
   v
Root server
   |
   | referral to .com
   v
.com TLD server
   |
   | referral to example.com authoritative server
   v
Authoritative server
   |
   | answer for www.example.com
   v
IP address
```

---

## 13.5 Recursive vs Authoritative DNS Servers

### Recursive resolver

A recursive resolver performs the lookup process on behalf of a client.

It may:
- Check its cache.
- Query other DNS servers.
- Follow referrals.
- Return the final answer or an error.

### Authoritative server

An authoritative server provides DNS records for a zone it serves.

It does not need to recursively resolve names outside that zone.

| Recursive resolver | Authoritative server |
|---|---|
| Resolves on behalf of clients | Serves records for its zone |
| Commonly caches answers | Provides authoritative data |
| Queries other DNS servers | Usually responds from zone data |
| Often used by end-user devices | Used to publish DNS records |

A DNS server can be configured to provide both recursive and authoritative services, although separating these roles is often preferable for security and operational reasons.

---

## 13.6 DNS Resolver and Cache

A DNS resolver is the software component that performs DNS resolution.

A caching resolver stores DNS answers for a period determined by their TTL.

### Why caching matters

Caching:
- Reduces repeated DNS queries.
- Improves lookup speed.
- Reduces load on DNS infrastructure.

A cached answer may remain usable until its TTL expires.

A resolver may also cache negative answers, such as a response indicating that a name does not exist, according to DNS negative-caching rules.

---

## 13.7 DNS Resolution Process

Suppose a client needs the IP address for:

```text
www.example.com
```

A typical lookup proceeds as follows:

1. The client checks its local DNS cache.
2. If there is no usable cached answer, the client sends a query to its configured recursive resolver.
3. The resolver checks its cache.
4. If needed, the resolver queries a root server.
5. The root server refers the resolver to the relevant TLD servers.
6. The resolver queries a TLD server.
7. The TLD server refers the resolver to the domain's authoritative server.
8. The resolver queries the authoritative server.
9. The authoritative server returns the requested record.
10. The resolver caches the answer according to its TTL.
11. The resolver returns the answer to the client.

The client usually communicates with a recursive resolver, not directly with root or TLD servers.

---

## 13.8 DNS Record Types

DNS records store different types of information.

| Record | Purpose |
|---|---|
| A | Maps a name to an IPv4 address |
| AAAA | Maps a name to an IPv6 address |
| CNAME | Makes a name an alias of another DNS name |
| MX | Identifies mail servers for a domain |
| NS | Identifies authoritative name servers |
| TXT | Stores text data, often used for verification and email security |
| PTR | Maps an IP address to a name for reverse DNS |
| SOA | Contains administrative information about a DNS zone |
| SRV | Identifies a service endpoint, including port and target |

### A record

Maps a DNS name to an IPv4 address.

```dns
www.example.com.  300  IN  A  192.0.2.10
```

`192.0.2.10` is a documentation address.

### AAAA record

Maps a DNS name to an IPv6 address.

```dns
www.example.com.  300  IN  AAAA  2001:db8::10
```

`2001:db8::10` is an IPv6 documentation address.

### CNAME record

Creates an alias from one DNS name to another.

```dns
shop.example.com.  300  IN  CNAME  store.example.net.
```

The target name may then be resolved to other records.

A CNAME generally cannot coexist with other ordinary data at the same owner name. The DNS zone apex commonly has SOA and NS records, so a conventional CNAME is not normally used at the apex.

### MX record

Identifies mail servers for a domain.

```dns
example.com.  300  IN  MX  10 mail.example.com.
```

The number `10` is the preference value. Lower preference values are preferred over higher values.

### NS record

Identifies authoritative name servers for a DNS zone.

```dns
example.com.  300  IN  NS  ns1.example.net.
```

### TXT record

Stores text data.

Common uses:
- Domain ownership verification
- SPF email policy
- DKIM public-key information
- DMARC policy publication

Example:

```dns
example.com.  300  IN  TXT  "v=spf1 include:mail.example.net -all"
```

TXT records do not automatically enforce the text they contain. Other systems interpret them according to their own standards.

### PTR record

Used for reverse DNS lookups.

For IPv4, reverse DNS uses the `in-addr.arpa` namespace.

Example:

```text
192.0.2.10
```

Reverse lookup name:

```text
10.2.0.192.in-addr.arpa.
```

IPv6 reverse DNS uses the `ip6.arpa` namespace and represents the address using reversed hexadecimal nibbles.

### SOA record

The Start of Authority (SOA) record contains important information about a DNS zone, including:
- Primary name server field
- Responsible party field
- Serial number
- Refresh interval
- Retry interval
- Expire interval
- Negative caching parameter

The SOA serial number helps secondary servers determine whether zone data has changed.

### SRV record

An SRV record provides information about a service, including priority, weight, port, and target.

General format:

```dns
_service._proto.example.com. IN SRV priority weight port target
```

Example:

```dns
_sip._tcp.example.com. IN SRV 10 20 5060 sipserver.example.com.
```

---

## 13.9 TTL and Caching

TTL means Time To Live.

For DNS, TTL indicates how long a record may be cached before it must be refreshed.

Example:

```dns
www.example.com.  600  IN  A  192.0.2.10
```

A TTL of `600` means 600 seconds, or 10 minutes.

### Important points

- A longer TTL can reduce DNS query volume.
- A shorter TTL can allow changes to be reflected sooner.
- TTL does not guarantee that every cache updates at the same instant.
- Existing cached answers may remain available until their TTL expires.
- Lowering a TTL shortly before a change does not affect copies that were cached earlier with a higher TTL.

---

## 13.10 Forward vs Reverse Lookup

### Forward lookup

Maps a domain name to an IP address.

Example:

```text
www.example.com -> 192.0.2.10
```

Common record types:
- A
- AAAA

### Reverse lookup

Maps an IP address to a DNS name.

Example:

```text
192.0.2.10 -> server.example.com
```

Common record type:
- PTR

Reverse DNS is not guaranteed to return the original domain name. The IP address owner or administrator controls the reverse DNS records.

---

## 13.11 DNS over UDP and TCP

DNS commonly uses port 53.

### UDP port 53

UDP is commonly used for ordinary DNS queries because it has low overhead.

### TCP port 53

TCP is used in situations including:
- Zone transfers
- Responses that require TCP
- Some large or truncated DNS responses
- DNS implementations that choose TCP for reliability

DNS is not exclusively a UDP protocol.

### DNS zone transfer

A zone transfer copies DNS zone data between DNS servers.

Common transfer types:
- AXFR: Full zone transfer
- IXFR: Incremental zone transfer

Zone transfers should be restricted to authorized secondary servers. An improperly exposed zone transfer can disclose DNS records and internal naming information.

---

## 13.12 DNSSEC Fundamentals

DNSSEC stands for Domain Name System Security Extensions.

DNSSEC provides cryptographic authentication of DNS data.

It helps a resolver verify that DNS responses are authentic and have not been modified in transit.

### Important DNSSEC records

- **DNSKEY:** Publishes DNS public-key information.
- **RRSIG:** Contains a digital signature for a DNS record set.
- **DS:** Connects a child zone's key to its parent zone.
- **NSEC / NSEC3:** Supports authenticated denial of existence.

### What DNSSEC does not do

DNSSEC:
- Does not encrypt DNS queries.
- Does not hide the domain name being queried.
- Does not guarantee that a domain's content is safe.
- Does not replace TLS/HTTPS.

DNSSEC helps protect DNS data integrity and authenticity, not confidentiality.

---

## 13.13 DoH and DoT

DNS over HTTPS (DoH) and DNS over TLS (DoT) encrypt DNS queries between a client and a compatible resolver.

| Technology | Common transport |
|---|---|
| Traditional DNS | UDP/TCP port 53 |
| DoT | TLS, commonly TCP port 853 |
| DoH | HTTPS, commonly TCP port 443; HTTP/3 may use QUIC |

### Benefits

- Encrypts DNS queries between the client and resolver.
- Helps prevent local-network observers from reading the DNS query contents.
- Reduces some forms of DNS manipulation by on-path observers.

### Limitations

- The resolver can still see the queries.
- The destination IP address may still be visible to network observers.
- DoH/DoT do not prove that the resolved website is trustworthy.
- Centralized resolvers may create privacy and policy concerns.

---

## 13.14 DNS Misconfiguration

Common DNS configuration problems include:

- Incorrect A or AAAA records.
- Missing or incorrect MX records.
- Incorrect NS delegation.
- Expired or invalid DNSSEC configuration.
- Incorrect CNAME targets.
- Unexpected TTL values.
- Stale records.
- Exposed zone transfers.
- Incorrect reverse DNS.
- Split-horizon DNS configured incorrectly.

### Troubleshooting checklist

1. Confirm the domain name is spelled correctly.
2. Query the recursive resolver.
3. Query authoritative servers if needed.
4. Check record type and value.
5. Check TTL and caching.
6. Check delegation and NS records.
7. Check DNSSEC validation if the answer fails with a validation error.

---

## 13.15 DNS Cache Poisoning — Concept and Defenses

DNS cache poisoning is an attack in which false DNS information is inserted into a resolver's cache.

If a resolver accepts and caches a forged answer, clients may be directed to an incorrect IP address.

### Potential impact

- Redirection to fraudulent websites.
- Interception of application traffic.
- Phishing.
- Disruption of access to legitimate services.

### Defenses

- Use DNSSEC validation where supported.
- Keep resolver software updated.
- Use secure resolver configurations.
- Apply source-port and transaction-ID randomization.
- Restrict access to recursive resolvers.
- Monitor for suspicious DNS behavior.
- Avoid trusting unvalidated DNS data.

DNSSEC validation can help detect forged DNS data, but it does not protect against every DNS-related threat.

---

## 13.16 Subdomain Discovery — Authorized Testing

Subdomain discovery identifies names beneath a domain, such as:

```text
api.example.com
dev.example.com
mail.example.com
```

It is useful for:
- Asset inventory
- Security assessments
- Finding forgotten services
- Understanding an organization's public attack surface

### Common methods

- Search certificate transparency logs.
- Review public DNS records.
- Use passive DNS sources.
- Check authorized asset inventories.
- Perform controlled DNS enumeration within an approved scope.

### Example commands

```bash
dig example.com A
dig example.com MX
dig example.com NS
dig www.example.com CNAME
```

For an authorized assessment, document:
- Scope
- Discovered names
- Record types
- Resolved addresses
- Whether the asset is in scope
- Any unexpected exposure

Do not scan or test systems outside the authorized scope.

---

## 13.17 DNS Tunneling — Detection Concepts

DNS tunneling can encode data inside DNS queries or responses to communicate through DNS.

It may be used for legitimate purposes, but attackers can also use it for command-and-control or data exfiltration.

### Detection indicators

- Unusually long DNS labels.
- High volumes of DNS queries.
- Large numbers of unique subdomains.
- High-entropy or encoded-looking labels.
- Unusual query types or patterns.
- DNS traffic to unexpected resolvers.
- Abnormal query frequency for a host.

### Defensive measures

- Monitor DNS query logs.
- Use approved recursive resolvers.
- Apply DNS filtering.
- Alert on unusual query volume and label patterns.
- Investigate suspicious destinations and host behavior.

A single long DNS name is not proof of tunneling. Detection should consider context and normal application behavior.

---

# 14. DHCP

## 14.1 What Is DHCP?

DHCP stands for Dynamic Host Configuration Protocol.

DHCP automatically provides network configuration to devices.

DHCP can assign or communicate:
- IP address
- Subnet mask or prefix
- Default gateway
- DNS servers
- Lease duration
- Other configuration options

Without DHCP, an administrator may need to configure these values manually.

---

## 14.2 DHCP Server and Client

### DHCP client

A device requesting network configuration.

Examples:
- Laptop
- Phone
- Virtual machine

### DHCP server

A system that leases network configuration to clients.

It manages:
- Address pools
- Leases
- Reservations
- DHCP options

A DHCP server should be configured to serve the correct network and avoid handing out conflicting addresses.

---

## 14.3 DHCP DORA Process

DORA describes the common DHCPv4 address assignment process.

```text
Client                         DHCP Server
  |                                 |
  |-------- Discover -------------->|
  |<--------- Offer ----------------|
  |--------- Request -------------->|
  |<-------- Acknowledge -----------|
```

### 1. Discover

The client broadcasts a DHCP Discover message to find DHCP servers.

### 2. Offer

A server offers an available IP address and configuration.

### 3. Request

The client requests the offered address.

### 4. Acknowledge

The server confirms the lease and configuration.

DORA is the common initial DHCPv4 lease process. Renewal and rebinding use different message patterns.

---

## 14.4 IP Leases

A DHCP lease is a time-limited assignment of an IP address to a client.

The client may renew the lease before it expires.

### Common DHCPv4 renewal behavior

- At approximately 50% of the lease time, the client typically attempts renewal with the original server.
- At approximately 87.5% of the lease time, the client typically attempts rebinding with any available server.
- If the lease expires without successful renewal, the client must stop using the leased address.

These are standard timing defaults; actual behavior depends on protocol state and configuration.

---

## 14.5 DHCP Scopes and Reservations

### Scope

A DHCP scope is a pool of addresses and settings available to clients on a network.

Example:

```text
Network:       192.168.1.0/24
DHCP pool:     192.168.1.100–192.168.1.200
Default route: 192.168.1.1
DNS server:    192.168.1.10
```

### Reservation

A reservation associates a particular client identifier, commonly a MAC address in DHCPv4 environments, with a specific IP address.

Reservations are useful for devices that need predictable addresses while still using DHCP.

A reservation is not the same as manually configuring a static IP address on the client.

---

## 14.6 DHCP Options

DHCP options provide additional configuration.

Common options include:

| DHCPv4 Option | Meaning |
|---|---|
| 1 | Subnet mask |
| 3 | Router / default gateway |
| 6 | DNS servers |
| 15 | Domain name |
| 51 | IP address lease time |
| 54 | DHCP server identifier |
| 66 | TFTP server name |
| 67 | Boot file name |

Options should be configured according to the network's requirements.

Incorrect options can cause clients to receive an address but still fail to communicate properly.

---

## 14.7 DHCP Relay

A DHCP relay forwards DHCP messages between clients and a DHCP server on another subnet.

DHCPv4 clients commonly begin with a broadcast, and routers normally do not forward ordinary broadcasts across subnets.

A relay agent allows clients to use a centralized DHCP server.

```text
Client subnet
    |
Client -- Relay Router ------ DHCP Server
```

The relay adds information that helps the server identify the client network and select the correct address pool.

---

## 14.8 DHCPv4 vs DHCPv6

| Feature | DHCPv4 | DHCPv6 |
|---|---|---|
| Address family | IPv4 | IPv6 |
| Client discovery | Broadcast-based in common initial exchange | Uses IPv6 multicast |
| Common server port | UDP 67 | UDP 547 |
| Common client port | UDP 68 | UDP 546 |
| Address configuration | Can assign IPv4 addresses | Can assign IPv6 addresses |
| Router information | Commonly supplied through DHCP option 3 | Default router is normally learned through IPv6 Router Advertisements |
| DORA terminology | Commonly used | DHCPv6 uses Solicit, Advertise, Request, Reply in its common exchange |

IPv6 can use Stateless Address Autoconfiguration (SLAAC), DHCPv6, or a combination depending on the network configuration.

DHCPv6 does not normally provide the IPv6 default-router information; hosts learn default routers through Router Advertisements.

---

## 14.9 Rogue DHCP Server Risks

A rogue DHCP server is an unauthorized DHCP server that provides configuration to clients.

It may provide:
- Incorrect default gateway
- Malicious DNS server
- Incorrect network settings
- Conflicting IP addresses

### Potential impact

- Traffic interception
- DNS manipulation
- Network disruption
- Man-in-the-middle opportunities

### Defenses

- Use DHCP snooping on supported switches.
- Mark only legitimate server-facing ports as trusted.
- Restrict physical access to network ports.
- Monitor DHCP server activity.
- Use network access controls where appropriate.

DHCP snooping is a Layer 2 switch security feature that can help prevent unauthorized DHCP server responses.

---

## 14.10 DHCP Starvation — Concept and Defense

DHCP starvation is an attack that attempts to exhaust a DHCP address pool by requesting many leases.

If the pool is exhausted, legitimate clients may be unable to obtain addresses.

### Defenses

- DHCP snooping.
- Port security or device access controls.
- Rate limiting DHCP messages.
- Monitoring address-pool utilization.
- Appropriate lease duration and pool sizing.
- Network access control.

Perform DHCP security testing only in an isolated lab or an explicitly authorized environment.

---

# 15. ARP and ICMP

## 15.1 ARP Purpose and Operation

ARP stands for Address Resolution Protocol.

ARP resolves an IPv4 address to a Layer 2 MAC address on a local network.

Example:

```text
IPv4 address: 192.168.1.1
MAC address:  AA:BB:CC:DD:EE:FF
```

ARP is used on local IPv4 Ethernet networks. It is not used to discover the MAC address of a remote Internet host.

### ARP process

1. A host determines that the destination is on the local subnet, or that it needs to send to its gateway.
2. It checks its ARP cache.
3. If no usable mapping exists, it broadcasts an ARP Request.
4. The device using the requested IPv4 address responds with an ARP Reply.
5. The sender stores the mapping in its ARP cache for a limited period.

### Example

Host A wants to send a packet to `192.168.1.1`.

It asks:

```text
Who has 192.168.1.1?
Tell 192.168.1.20.
```

The device at `192.168.1.1` responds with its MAC address.

---

## 15.2 ARP Cache and Expiration

An ARP cache stores recently learned IPv4-to-MAC mappings.

Linux commands:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

Common neighbor states include:
- REACHABLE
- STALE
- DELAY
- PROBE
- FAILED

ARP cache entries are not permanent by default. Their state and lifetime depend on operating-system behavior and network activity.

---

## 15.3 ICMP Purpose

ICMP stands for Internet Control Message Protocol.

ICMP supports IP networking by carrying diagnostic and error messages.

It is used for:
- Reachability testing
- Reporting certain delivery failures
- Reporting TTL or Hop Limit expiration
- Network troubleshooting

ICMP is not a transport protocol like TCP or UDP. It is carried directly within IP.

---

## 15.4 Echo Request and Echo Reply

Ping commonly uses ICMP Echo Request and Echo Reply messages.

Example:

```bash
ping -c 4 192.168.1.1
```

This sends four echo requests on Linux.

The replies help estimate:
- Reachability
- Round-trip time
- Packet loss

A ping response does not prove that every service on the target is working.

---

## 15.5 Destination Unreachable

An ICMP Destination Unreachable message indicates that a packet could not be delivered or that a relevant condition prevented delivery.

Possible reasons include:
- Network unreachable
- Host unreachable
- Port unreachable
- Administratively prohibited

The exact message and code provide more detail.

ICMP errors may be filtered or rate-limited, so the absence of an error message does not necessarily mean the packet was delivered.

---

## 15.6 Time Exceeded

An ICMP Time Exceeded message may be generated when:
- An IPv4 packet's TTL reaches zero.
- An IPv6 packet's Hop Limit reaches zero.

This is important for traceroute.

Traceroute sends probes with increasing TTL or Hop Limit values and observes the routers that respond.

---

## 15.7 TTL Exceeded in Traceroute

Example:

```text
Probe with TTL 1 -> First router may respond
Probe with TTL 2 -> Second router may respond
Probe with TTL 3 -> Third router may respond
```

The response is commonly an ICMP Time Exceeded message.

Commands:

```bash
traceroute example.com
tracepath example.com
```

Some routers do not respond to these probes, so traceroute may display timeouts.

---

## 15.8 IPv6 Neighbor Discovery

IPv6 Neighbor Discovery (ND) is part of ICMPv6.

It performs functions including:
- Neighbor address resolution
- Router discovery
- Prefix discovery
- Neighbor reachability detection
- Duplicate Address Detection (DAD)

Neighbor Discovery replaces several functions associated with ARP in IPv4 networks.

### Important ICMPv6 messages

| Message | Purpose |
|---|---|
| Router Solicitation (RS) | Host asks routers to send Router Advertisements |
| Router Advertisement (RA) | Router advertises network information |
| Neighbor Solicitation (NS) | Resolves a neighbor's link-layer address or checks address use |
| Neighbor Advertisement (NA) | Responds to Neighbor Solicitation or advertises neighbor information |
| Redirect | Informs a host of a better first hop in applicable circumstances |

IPv6 Neighbor Discovery uses multicast rather than IPv4-style broadcast.

---

## 15.9 Ping Limitations

Ping is useful but has limitations.

- Firewalls may block ICMP Echo.
- A host may be reachable even if it does not respond to ping.
- A ping response does not prove that a TCP or UDP service is available.
- ICMP may be rate-limited.
- High latency may be caused by ICMP handling policy rather than application performance.
- A successful ping does not prove that DNS, HTTPS, or authentication works.

Use multiple diagnostic methods instead of relying on ping alone.

---

## 15.10 ICMP Filtering and Troubleshooting

ICMP filtering can improve some security controls, but blocking all ICMP indiscriminately may interfere with troubleshooting and network behavior.

For example:
- IPv4 Path MTU Discovery relies on ICMP messages.
- IPv6 depends heavily on ICMPv6 for core network functions.
- Traceroute may be affected by filtering.
- Error messages can help identify routing problems.

A good firewall policy allows necessary ICMP/ICMPv6 messages while limiting unwanted traffic according to the network's security requirements.

---

## 15.11 ARP Spoofing Defenses

ARP spoofing occurs when a device sends forged ARP messages to associate an IP address with an incorrect MAC address.

An attacker may attempt to impersonate a gateway or another local host.

### Potential impact

- Traffic interception
- Man-in-the-middle attacks
- Traffic disruption
- Session exposure if other protections are weak

### Defenses

- Dynamic ARP Inspection (DAI), where supported.
- DHCP snooping bindings.
- Static ARP entries for limited critical cases.
- Network segmentation.
- Monitoring unusual ARP changes.
- Encrypting application traffic with TLS.
- Restricting access to local network segments.

Static ARP entries are not a practical solution for every device in a large network.

---

## 15.12 Network Discovery Limitations

Network discovery tools cannot guarantee that every device will be identified.

Results may be affected by:
- Firewalls
- ICMP filtering
- Host-based security software
- VLAN boundaries
- Routing restrictions
- Rate limiting
- Offline devices
- Incorrect subnet assumptions

A host that does not respond to a discovery probe may still be active.

Use network discovery only on networks you own or are authorized to assess.

---

# 16. Other Important Protocols

## 16.1 NTP — Network Time Protocol

NTP synchronizes clocks across networked systems.

Accurate time is important for:
- Log correlation
- Authentication
- Incident investigation
- Certificate validation
- Distributed systems

NTP commonly uses UDP port 123.

### Security considerations

- Use trusted time sources.
- Restrict unnecessary NTP access.
- Monitor unexpected NTP traffic.
- Keep time services updated.
- Use secure time synchronization methods where supported.

Incorrect time can make security logs difficult to correlate.

---

## 16.2 SNMP — Simple Network Management Protocol

SNMP is used to monitor and manage network devices.

It can provide information such as:
- Interface status
- Traffic counters
- CPU and memory utilization
- Device uptime
- Network errors

SNMP commonly uses UDP port 161 for queries and UDP port 162 for traps or notifications.

### SNMP versions

| Version | Security |
|---|---|
| SNMPv1 | Basic community-string authentication; weak security |
| SNMPv2c | Improved protocol features but still uses community strings |
| SNMPv3 | Supports authentication and privacy features |

SNMPv3 is generally preferred for secure management.

Avoid exposing SNMP to untrusted networks and avoid default or easily guessed community strings.

---

## 16.3 LDAP — Directory Services

LDAP stands for Lightweight Directory Access Protocol.

LDAP is used to access and manage directory information.

A directory may store:
- User accounts
- Groups
- Organizational units
- Contact information
- Authentication-related information

LDAP commonly uses:
- TCP/UDP port 389 for LDAP
- TCP port 636 for LDAP over TLS (LDAPS)

StartTLS can also be used to upgrade an LDAP connection to TLS.

LDAP is a directory access protocol. It is not itself a complete authentication system, although it is often used as part of authentication and identity-management systems.

---

## 16.4 SMB — File Sharing

SMB stands for Server Message Block.

SMB is commonly used for:
- File sharing
- Printer sharing
- Accessing shared folders
- Some remote management operations

Modern SMB commonly uses TCP port 445.

Older NetBIOS-based SMB deployments may use additional NetBIOS-related ports.

### Security considerations

- Disable SMB versions that are no longer needed.
- Keep SMB implementations patched.
- Restrict access to trusted networks.
- Use strong authentication.
- Avoid exposing SMB directly to the public Internet.
- Apply least-privilege access to shares.

---

## 16.5 FTP vs SFTP vs FTPS

| Protocol | Meaning | Security |
|---|---|---|
| FTP | File Transfer Protocol | Traditional FTP does not encrypt credentials or data |
| SFTP | SSH File Transfer Protocol | Transfers files over SSH |
| FTPS | FTP over TLS | Adds TLS protection to FTP |

### FTP

FTP commonly uses:
- TCP port 21 for control
- A separate data connection, depending on active or passive mode

FTP can expose credentials and data when used without encryption.

### SFTP

SFTP is a file-transfer protocol carried over SSH.

It commonly uses TCP port 22.

SFTP is not simply "FTP with SSH"; it is a different protocol.

### FTPS

FTPS uses TLS to secure FTP connections.

Explicit FTPS commonly begins on TCP port 21 and upgrades to TLS. Implicit FTPS commonly uses TCP port 990.

The data-channel configuration may require additional ports depending on the server and passive-mode settings.

---

## 16.6 SMTP, IMAP, and POP3

These protocols support email delivery and access.

### SMTP — Simple Mail Transfer Protocol

SMTP is used to send email and relay messages between mail servers.

Common ports:
- TCP 25: Server-to-server mail transfer
- TCP 587: Message submission, commonly with STARTTLS
- TCP 465: Message submission over implicit TLS

### IMAP — Internet Message Access Protocol

IMAP allows clients to access and manage email stored on a mail server.

Common ports:
- TCP 143: IMAP, commonly upgraded using STARTTLS
- TCP 993: IMAP over implicit TLS

### POP3 — Post Office Protocol version 3

POP3 allows clients to retrieve email from a mail server.

Common ports:
- TCP 110: POP3, commonly upgraded using STARTTLS
- TCP 995: POP3 over implicit TLS

| Protocol | Main purpose |
|---|---|
| SMTP | Send or relay email |
| IMAP | Synchronize and manage server-side email |
| POP3 | Retrieve email, often with simpler mailbox behavior |

---

## 16.7 SSH vs Telnet

### SSH — Secure Shell

SSH provides encrypted remote access and supports:
- Remote command execution
- Secure terminal sessions
- File transfer through SCP or SFTP
- Port forwarding and tunneling

SSH commonly uses TCP port 22.

### Telnet

Telnet provides remote terminal access but does not encrypt its traffic.

It commonly uses TCP port 23.

### Comparison

| SSH | Telnet |
|---|---|
| Encrypted communication | Plaintext communication |
| Supports secure authentication methods | Credentials may be exposed |
| Commonly used for secure administration | Generally unsuitable for untrusted networks |

Use SSH rather than Telnet for remote administration.

---

## 16.8 RDP — Remote Desktop Protocol

RDP is a remote desktop protocol commonly associated with Microsoft Windows.

It allows users to interact with a remote graphical desktop.

RDP commonly uses TCP port 3389 and may also use UDP 3389.

### Security considerations

- Avoid exposing RDP directly to the public Internet.
- Use a VPN or secure access gateway.
- Enforce strong authentication.
- Use Network Level Authentication where appropriate.
- Apply security updates.
- Monitor login attempts.
- Restrict access to authorized users and systems.

---

## 16.9 Syslog

Syslog is a standard for transmitting and recording log messages.

It is commonly used by:
- Routers
- Firewalls
- Servers
- Network switches
- Security systems

Syslog messages may include:
- Timestamp
- Hostname
- Application or process
- Severity
- Message content

Common transport arrangements include:
- UDP port 514
- TCP port 514
- TLS-protected syslog, commonly TCP port 6514

UDP syslog does not guarantee delivery. Reliable or encrypted transport may be preferred for important security logs.

---

## 16.10 IPsec

IPsec is a suite of protocols used to protect IP communication.

It can provide:
- Confidentiality
- Integrity
- Authentication
- Anti-replay protection

IPsec is commonly used for VPNs.

### Main components

- **AH (Authentication Header):** Provides integrity and authentication but not encryption.
- **ESP (Encapsulating Security Payload):** Can provide encryption, integrity, and authentication.
- **IKE / IKEv2:** Negotiates security associations and keys.

IPsec can operate in:
- **Transport mode:** Protects the IP payload while retaining the original IP header.
- **Tunnel mode:** Encapsulates and protects an entire inner IP packet within a new outer IP packet.

IPsec commonly uses:
- UDP 500 for IKE
- UDP 4500 for NAT traversal
- IP protocol 50 for ESP
- IP protocol 51 for AH

ESP and AH are IP protocols, not TCP or UDP port numbers.

---

## 16.11 QUIC

QUIC is a transport protocol built over UDP.

It is designed to provide secure, reliable transport with features such as:
- Integrated TLS 1.3 security
- Stream multiplexing
- Reduced connection setup latency
- Improved handling of packet loss across independent streams

HTTP/3 uses QUIC.

QUIC commonly uses UDP port 443 for HTTP/3, although the port can vary by deployment.

### QUIC vs TCP

| QUIC | TCP |
|---|---|
| Runs over UDP | Runs directly over IP |
| Integrates TLS 1.3 | TLS is layered above TCP for HTTPS |
| Supports independent streams | TCP provides one ordered byte stream per connection |
| Can reduce some connection setup delays | Connection and TLS setup may require separate handshakes |

QUIC is not simply "TCP over UDP." It has its own transport behavior.

---

## 16.12 WebSocket

WebSocket provides persistent, bidirectional communication between a client and server.

It is commonly used for:
- Chat applications
- Live notifications
- Collaborative applications
- Real-time dashboards
- Interactive browser applications

WebSocket commonly begins with an HTTP-based handshake and then switches protocols.

Common URI schemes:
- `ws://` for unencrypted WebSocket
- `wss://` for WebSocket over TLS

Typical deployments use TCP port 80 for `ws://` and TCP port 443 for `wss://`, though ports can vary.

### Security considerations

- Validate the `Origin` header where appropriate.
- Authenticate connections.
- Authorize individual actions.
- Validate incoming messages.
- Apply rate limits.
- Use `wss://` on untrusted networks.
- Avoid assuming that an authenticated connection authorizes every message.

---

## 16.13 MQTT — Basic Purpose

MQTT stands for Message Queuing Telemetry Transport.

It is a lightweight publish/subscribe messaging protocol commonly used in:
- IoT devices
- Sensors
- Telemetry
- Industrial monitoring
- Messaging between constrained devices

### Basic model

```text
Publisher ---> MQTT Broker ---> Subscriber
```

A publisher sends a message to a topic. The broker distributes it to subscribers that are authorized and subscribed to that topic.

Example topic:

```text
building/floor1/temperature
```

### Common ports

- TCP 1883: MQTT without TLS
- TCP 8883: MQTT over TLS

Security considerations:
- Require authentication.
- Enforce topic-level authorization.
- Use TLS when appropriate.
- Avoid anonymous access unless explicitly required and safely isolated.
- Monitor unusual publish or subscribe behavior.

---

## 16.14 RPC — Basic Purpose

RPC stands for Remote Procedure Call.

RPC allows a program to invoke a procedure or function on another system as though it were a local call, while the underlying system handles network communication.

### Basic process

1. Client calls a local-looking function.
2. Client-side RPC software serializes the request.
3. The request is sent over the network.
4. The server receives and processes it.
5. The server serializes the result.
6. The client receives the response.

RPC can use different transports and protocols.

Examples include:
- XML-RPC
- JSON-RPC
- gRPC
- ONC RPC

### Security considerations

- Authenticate clients.
- Authorize operations.
- Validate input.
- Protect sensitive data in transit.
- Apply rate limits.
- Avoid exposing RPC endpoints unnecessarily.

---

# Practical Tasks

> Perform these tasks only on your own systems or authorized lab networks.

## Task 1: Query DNS Records

Use `dig` to inspect DNS records.

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
```

Query a specific resolver:

```bash
dig @1.1.1.1 example.com A
```

Query the authoritative name servers:

```bash
dig example.com NS
```

Then query one of the returned authoritative servers:

```bash
dig @<authoritative-server> example.com A
```

Replace `<authoritative-server>` with a real server name from your result.

## Task 2: Inspect DNS Resolution

Run:

```bash
dig example.com
```

Observe:
- `QUESTION SECTION`
- `ANSWER SECTION`
- `AUTHORITY SECTION`
- `ADDITIONAL SECTION`
- TTL values
- Query time
- Resolver address

Try:

```bash
dig +trace example.com
```

This requests an iterative trace through the DNS hierarchy. Some networks may restrict or interfere with direct DNS queries to authoritative servers.

## Task 3: Inspect Local DNS Configuration

On Linux:

```bash
cat /etc/resolv.conf
```

Also inspect:

```bash
resolvectl status
```

The second command is available on systems using `systemd-resolved`.

The resolver configuration may point to a local stub resolver, router, ISP resolver, or another DNS service.

## Task 4: Inspect ARP / Neighbor Cache

Run:

```bash
ip neigh
```

Ping your default gateway, then inspect the cache again:

```bash
ping -c 1 <gateway-ip>
ip neigh
```

Observe whether a neighbor entry was created or its state changed.

## Task 5: Inspect DHCP Configuration

Check your interface and IP configuration:

```bash
ip addr
ip route
```

Check the DHCP client or network manager used by your Linux distribution.

Do not release or renew an active network lease on a system where losing connectivity would interrupt important work.

## Task 6: Inspect Network Services

On your own Linux system, inspect listening sockets:

```bash
ss -tuln
```

To include process information where permissions allow:

```bash
sudo ss -tulpn
```

This shows local listening services. It does not prove that a service is reachable from another host, because firewall rules and routing may affect access.

## Task 7: Observe DNS and ARP Traffic in a Lab

Start a packet capture on your own interface:

```bash
sudo tcpdump -ni <interface> 'port 53 or arp or icmp'
```

In another terminal:
- Query a DNS name.
- Ping a local host.
- Ping your gateway.

Observe which packets appear.

Use a lab or network you are authorized to monitor. Avoid capturing other people's traffic.

---

# Quick Revision Table

| Protocol | Main purpose | Common port / protocol |
|---|---|---|
| DNS | Name resolution | UDP/TCP 53 |
| DoT | Encrypted DNS | TCP 853 |
| DoH | DNS over HTTPS | Commonly TCP 443; HTTP/3 may use QUIC |
| DHCPv4 | IPv4 configuration | UDP 67/68 |
| DHCPv6 | IPv6 configuration | UDP 547/546 |
| ARP | IPv4-to-MAC resolution on LAN | Layer 2 |
| ICMP | IP diagnostics and error messages | IP protocol 1 for IPv4 |
| ICMPv6 | IPv6 diagnostics and Neighbor Discovery | IP protocol 58 |
| NTP | Time synchronization | UDP 123 |
| SNMP | Network monitoring and management | UDP 161/162 |
| LDAP | Directory access | TCP/UDP 389 |
| LDAPS | LDAP over TLS | TCP 636 |
| SMB | File and printer sharing | TCP 445 |
| FTP | File transfer | TCP 21 plus data channel |
| SFTP | File transfer over SSH | TCP 22 |
| FTPS | FTP over TLS | Commonly TCP 21 or 990 |
| SMTP | Email sending and relay | TCP 25/465/587 |
| IMAP | Email access and synchronization | TCP 143/993 |
| POP3 | Email retrieval | TCP 110/995 |
| SSH | Secure remote administration | TCP 22 |
| Telnet | Unencrypted remote terminal | TCP 23 |
| RDP | Remote desktop | TCP/UDP 3389 |
| Syslog | Log transport | Commonly UDP/TCP 514; TLS 6514 |
| IPsec IKE | Key negotiation | UDP 500/4500 |
| ESP | IPsec protection | IP protocol 50 |
| QUIC | Secure transport over UDP | Commonly UDP 443 |
| WebSocket | Bidirectional application communication | Commonly TCP 80/443 |
| MQTT | Lightweight publish/subscribe | TCP 1883/8883 |
| RPC | Remote procedure invocation | Depends on implementation |

> Port numbers are common defaults, not guarantees. Services can be configured to use different ports.

---

# Interview Questions

## 1. What is DNS?

DNS is a distributed hierarchical naming system that maps domain names to information such as IP addresses, mail servers, and authoritative name servers.

## 2. What is the difference between a recursive resolver and an authoritative DNS server?

A recursive resolver resolves names on behalf of clients and may cache results. An authoritative server provides DNS records for the zone it serves.

## 3. What is the difference between A and AAAA records?

An A record maps a name to an IPv4 address. An AAAA record maps a name to an IPv6 address.

## 4. What is the purpose of DNS TTL?

TTL tells caching resolvers how long a DNS record may be cached before it should be refreshed.

## 5. Does DNSSEC encrypt DNS traffic?

No. DNSSEC authenticates DNS data and helps protect its integrity. It does not provide query confidentiality.

## 6. Explain DHCP DORA.

DORA stands for Discover, Offer, Request, and Acknowledge. It is the common initial DHCPv4 address assignment process.

## 7. What is a rogue DHCP server?

A rogue DHCP server is an unauthorized server that provides network configuration. It may give clients a malicious gateway or DNS server.

## 8. What is ARP used for?

ARP resolves an IPv4 address to a MAC address on a local network.

## 9. How does traceroute work?

Traceroute sends probes with increasing TTL or Hop Limit values. Intermediate routers may return ICMP Time Exceeded messages, revealing the responding hops.

## 10. What is the difference between SSH and Telnet?

SSH encrypts remote sessions and supports secure authentication. Telnet transmits data, including credentials, without encryption.

## 11. What is the difference between SFTP and FTPS?

SFTP is a file-transfer protocol carried over SSH. FTPS is FTP secured with TLS. They are different protocols.

## 12. What is MQTT used for?

MQTT is a lightweight publish/subscribe messaging protocol commonly used for IoT telemetry and communication between constrained devices.

## 13. What is QUIC?

QUIC is a secure transport protocol over UDP that supports multiplexed streams and is used by HTTP/3.

## 14. Why can ping fail even if a host is online?

The host or network may block or rate-limit ICMP Echo messages. Ping tests ICMP reachability, not every application service.

## 15. What is DNS tunneling?

DNS tunneling encodes data in DNS queries or responses. It can be used legitimately, but may also be abused for command-and-control or data exfiltration. Detection relies on traffic patterns and context.
