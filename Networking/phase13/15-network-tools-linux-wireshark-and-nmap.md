
# Phase 13: Network Tools on Linux and Kali

# 29. Essential Command-Line Tools

Linux provides many command-line tools for network configuration, troubleshooting, traffic analysis, DNS investigation, and security testing.

As a cybersecurity learner, you should become comfortable using these tools directly from the terminal.

---

## 1. `ip` — Addresses, Interfaces, and Routes

The `ip` command is used to manage and inspect network interfaces, IP addresses, routes, and neighboring devices.

It is part of the `iproute2` package.

### View network interfaces

```bash
ip link
```

Displays available network interfaces and their states.

Example:

```text
1: lo: <LOOPBACK,UP>
2: eth0: <BROADCAST,MULTICAST,UP>
3: wlan0: <BROADCAST,MULTICAST,UP>
```

Common interface names:

| Interface | Meaning |
|---|---|
| `lo` | Loopback interface |
| `eth0` | Ethernet interface |
| `wlan0` | Wireless interface |
| `ens33` | Common virtual machine Ethernet interface |

### View IP addresses

```bash
ip addr
```

Or:

```bash
ip -br addr
```

The second command displays a shorter summary.

### View routing table

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel
```

Meaning:

- `default`: Default route.
- `via 192.168.1.1`: Default gateway.
- `dev eth0`: Interface used for communication.
- `192.168.1.0/24`: Local network route.

### View neighboring devices

```bash
ip neigh
```

Displays neighboring devices and their IP-to-link-layer address mappings.

### Bring an interface up or down

```bash
sudo ip link set eth0 up
```

```bash
sudo ip link set eth0 down
```

**Remember:** The `ip` command is the modern replacement for many older commands such as `ifconfig` and `route`.

---

## 2. `ping` — Connectivity Tests

`ping` checks whether a destination can be reached using ICMP Echo Request and Echo Reply messages.

It is commonly used for basic network troubleshooting.

### Basic usage

```bash
ping example.com
```

Send a limited number of packets:

```bash
ping -c 4 example.com
```

Ping a local gateway:

```bash
ping -c 4 192.168.1.1
```

### Important output fields

Example:

```text
64 bytes from 93.184.216.34:
icmp_seq=1 ttl=56 time=25.4 ms
```

| Field | Meaning |
|---|---|
| `64 bytes` | Response size |
| `icmp_seq` | ICMP sequence number |
| `ttl` | Time To Live |
| `time` | Round-trip time |

### Packet loss

At the end of a ping session, you may see:

```text
4 packets transmitted, 4 received, 0% packet loss
```

This means all four probes received replies.

### Important limitations

A failed ping does not always mean that a server is unavailable.

Possible reasons:
- ICMP is blocked by a firewall.
- The destination does not respond to ping.
- Network routing is unavailable.
- The host is offline.

**Cybersecurity relevance:** Ping is useful for initial connectivity checks, but it should not be treated as proof that a service or host is secure or insecure.

---

## 3. `ss` — Sockets and Listening Ports

`ss` stands for Socket Statistics.

It displays information about network sockets, listening services, and active connections.

It is commonly used instead of the older `netstat` command.

### Show all TCP and UDP sockets

```bash
ss -tuna
```

### Show listening TCP sockets

```bash
ss -tln
```

### Show listening UDP sockets

```bash
ss -uln
```

### Show listening sockets with process information

```bash
sudo ss -tulnp
```

### Show established TCP connections

```bash
ss -tn state established
```

### Important options

| Option | Meaning |
|---|---|
| `-t` | TCP |
| `-u` | UDP |
| `-l` | Listening sockets |
| `-n` | Numeric addresses and ports |
| `-a` | All sockets |
| `-p` | Process information |

### Example output

```text
Netid  State   Local Address:Port
tcp    LISTEN  0.0.0.0:22
tcp    LISTEN  0.0.0.0:80
tcp    LISTEN  127.0.0.1:3306
```

Interpretation:

- Port 22: SSH service.
- Port 80: HTTP service.
- Port 3306: MySQL service listening on localhost.

**Cybersecurity relevance:** Use `ss` to identify unexpected listening services and investigate which processes are accepting network connections.

---

## 4. `curl` — HTTP and API Requests

`curl` is a command-line tool used to transfer data to and from servers using different protocols.

It is particularly important for web development and web application security.

### Make a basic HTTP request

```bash
curl https://example.com
```

### Display only response headers

```bash
curl -I https://example.com
```

### Display detailed connection information

```bash
curl -v https://example.com
```

### Make a GET request

```bash
curl -X GET https://api.example.com/users
```

### Make a POST request with JSON

```bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex","email":"alex@example.com"}'
```

This is an illustrative API request. The endpoint must support the operation.

### Send an authorization header

```bash
curl https://api.example.com/profile \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Never share real API tokens or passwords in public logs or screenshots.

### Save a response to a file

```bash
curl -o response.html https://example.com
```

### Follow redirects

```bash
curl -L https://example.com
```

### Useful options

| Option | Purpose |
|---|---|
| `-I` | Fetch headers |
| `-v` | Verbose output |
| `-X` | Specify HTTP method |
| `-H` | Add request header |
| `-d` | Send request data |
| `-o` | Save output to a file |
| `-L` | Follow redirects |
| `-s` | Silent mode |

**Cybersecurity relevance:** `curl` helps you inspect HTTP headers, test API behavior, examine authentication responses, and understand how web servers respond to requests.

---

## 5. `wget` — File Retrieval

`wget` is a command-line utility used to download files from web servers.

### Download a file

```bash
wget https://example.com/file.zip
```

### Save with a custom filename

```bash
wget -O downloaded.zip https://example.com/file.zip
```

### Continue an interrupted download

```bash
wget -c https://example.com/large-file.zip
```

### Download in the background

```bash
wget -b https://example.com/file.zip
```

### Download with a specific output directory

```bash
wget -P ~/Downloads https://example.com/file.zip
```

### Difference between curl and wget

| Feature | curl | wget |
|---|---|---|
| Main purpose | Data transfer and API interaction | File downloading |
| HTTP methods | Supports many | Primarily retrieval |
| API testing | Very useful | Less convenient |
| Recursive downloading | Not its primary use | Supported |
| Saving output | Supported | Natural default behavior |

**Remember:** `curl` is especially useful for API and HTTP testing, while `wget` is especially convenient for downloading files.

---

## 6. `dig` — DNS Queries

`dig` stands for Domain Information Groper.

It is used to query DNS servers and inspect DNS records.

### Basic DNS lookup

```bash
dig example.com
```

### Query A record

```bash
dig example.com A
```

An A record maps a domain name to an IPv4 address.

### Query AAAA record

```bash
dig example.com AAAA
```

An AAAA record maps a domain name to an IPv6 address.

### Query MX record

```bash
dig example.com MX
```

MX records identify mail servers.

### Query NS record

```bash
dig example.com NS
```

NS records identify authoritative name servers.

### Query TXT record

```bash
dig example.com TXT
```

TXT records store text information, often used for SPF, DKIM, domain verification, and other purposes.

### Query a specific DNS server

```bash
dig @8.8.8.8 example.com
```

### Short output

```bash
dig +short example.com
```

### Trace DNS delegation

```bash
dig +trace example.com
```

**Cybersecurity relevance:** DNS investigation is useful during domain reconnaissance, troubleshooting, and detection of suspicious DNS behavior.

---

## 7. `host` — DNS Lookups

`host` is a simple command-line DNS lookup utility.

It provides an alternative to `dig` for common DNS queries.

### Basic lookup

```bash
host example.com
```

### Find mail servers

```bash
host -t MX example.com
```

### Find name servers

```bash
host -t NS example.com
```

### Find IPv4 addresses

```bash
host -t A example.com
```

### Find IPv6 addresses

```bash
host -t AAAA example.com
```

### Difference between dig and host

| Feature | dig | host |
|---|---|---|
| Detailed DNS output | Yes | Simpler |
| DNS troubleshooting | Excellent | Useful |
| Record queries | Yes | Yes |
| Trace functionality | Supported | Limited compared with dig |

**Remember:** Use `dig` when you need detailed DNS information and `host` when you need a quick lookup.

---

## 8. `traceroute` or `tracepath` — Route Diagnostics

These tools help identify the network path packets take toward a destination.

They show intermediate routers, commonly called hops.

### Using traceroute

```bash
traceroute example.com
```

### Using tracepath

```bash
tracepath example.com
```

### Example output

```text
1  192.168.1.1
2  10.10.0.1
3  172.16.0.1
4  93.184.216.34
```

Each numbered entry represents a hop along the observed route.

### How it works

Traceroute commonly uses packets with increasing TTL values.

1. First probe has TTL 1.
2. The first router decreases TTL to zero.
3. It may return an ICMP Time Exceeded message.
4. The next probe uses TTL 2.
5. The process continues toward the destination.

### Important limitations

- Some routers do not respond to traceroute probes.
- Firewalls may block the probes.
- Different probes may follow different paths.
- A timeout does not necessarily mean that the network is broken.

**Cybersecurity relevance:** Route diagnostics help investigate routing problems and understand network paths.

---

## 9. `mtr` — Combined Route and Loss Diagnostics

`mtr` combines features of traceroute and ping.

It continuously measures network performance across the route to a destination.

### Basic usage

```bash
mtr example.com
```

### Report mode

```bash
mtr -r -c 10 example.com
```

This performs a report with ten cycles.

### Important output fields

| Field | Meaning |
|---|---|
| Loss% | Percentage of probes without responses |
| Snt | Number of probes sent |
| Last | Last recorded latency |
| Avg | Average latency |
| Best | Lowest latency |
| Wrst | Highest latency |
| StDev | Latency variation |

### Important interpretation

A router showing packet loss does not necessarily mean that it is dropping forwarded traffic.

Some routers deprioritize or limit responses to diagnostic probes.

Look for consistent loss that continues through later hops and affects the destination before concluding there is a forwarding problem.

---

## 10. `nc` — Basic Socket Testing

`nc` stands for Netcat.

It is a command-line networking utility used to read and write data across network connections.

It can help test TCP and UDP connectivity.

### Test a TCP port

```bash
nc -vz 192.168.1.10 80
```

### Test SSH connectivity

```bash
nc -vz 192.168.1.10 22
```

### Listen on a local TCP port

```bash
nc -l -p 9000
```

Exact listening syntax can vary between Netcat implementations.

### Connect to a listening service

```bash
nc 127.0.0.1 9000
```

### Send a simple message

Type text into one terminal after establishing a connection. It should appear in the other terminal.

### Common options

| Option | Meaning |
|---|---|
| `-v` | Verbose output |
| `-z` | Scan mode without sending application data |
| `-l` | Listen |
| `-n` | Do not resolve hostnames |
| `-u` | UDP mode |

**Cybersecurity relevance:** Netcat helps test connectivity and understand how TCP and UDP sockets work. Use listening and connection tests only on systems you control or are authorized to test.

---

## 11. `tcpdump` — Packet Capture

`tcpdump` is a command-line packet analyzer used to capture and inspect network packets.

### Capture traffic on an interface

```bash
sudo tcpdump -i eth0
```

### Capture traffic on all interfaces

```bash
sudo tcpdump -i any
```

### Capture only DNS traffic

```bash
sudo tcpdump -i eth0 port 53
```

### Capture traffic from a specific host

```bash
sudo tcpdump -i eth0 host 192.168.1.10
```

### Capture only TCP traffic

```bash
sudo tcpdump -i eth0 tcp
```

### Save packets to a PCAP file

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

### Read a PCAP file

```bash
tcpdump -r capture.pcap
```

### Display numeric addresses

```bash
tcpdump -nn -r capture.pcap
```

### Limit the number of packets

```bash
sudo tcpdump -i eth0 -c 50
```

**Cybersecurity relevance:** Packet capture is useful for network troubleshooting, security monitoring, and incident investigation.

---

## 12. `nmap` — Authorized Network Discovery

Nmap is a network discovery and security auditing tool.

It helps identify:
- Live hosts.
- Open ports.
- Running services.
- Software versions.
- Some operating system characteristics.

### Basic scan

```bash
nmap 192.168.1.10
```

### Scan a local subnet

```bash
nmap 192.168.1.0/24
```

### Scan selected ports

```bash
nmap -p 22,80,443 192.168.1.10
```

### Detect service versions

```bash
nmap -sV 192.168.1.10
```

### Scan all TCP ports

```bash
nmap -p- 192.168.1.10
```

### Save output

```bash
nmap -oN scan.txt 192.168.1.10
```

**Important:** Only scan systems and networks that you own or have explicit authorization to test. A public IP address being reachable does not grant permission to scan it.

---

## 13. `whois` — Domain/IP Registration Information

`whois` queries registration databases to obtain information about domain names and IP address allocations.

### Query a domain

```bash
whois example.com
```

### Query an IP address

```bash
whois 8.8.8.8
```

### Information that may be available

- Registrar.
- Registration dates.
- Expiration dates.
- Name servers.
- Domain status.
- Organization or network allocation.
- Abuse contact information.

### Important limitations

- Privacy protection may hide registrant information.
- Some registries provide incomplete records.
- WHOIS access may be rate-limited.
- Modern registration data may also be available through RDAP.

**Cybersecurity relevance:** WHOIS and RDAP are useful for domain and IP ownership research during authorized reconnaissance.

---

## 14. `openssl s_client` — TLS Inspection

OpenSSL is a cryptographic toolkit.

The `s_client` command can establish and inspect TLS connections.

### Connect to an HTTPS server

```bash
openssl s_client -connect example.com:443
```

### Include the hostname for SNI

```bash
openssl s_client -connect example.com:443 -servername example.com
```

SNI stands for Server Name Indication. It allows a client to indicate which hostname it wants during the TLS handshake.

### Display certificates

```bash
openssl s_client -connect example.com:443 \
  -servername example.com -showcerts
```

### Verify certificate validation

```bash
openssl s_client -connect example.com:443 \
  -servername example.com -verify_return_error
```

### Inspect a certificate file

```bash
openssl x509 -in certificate.pem -text -noout
```

### Information you can investigate

- TLS protocol version.
- Cipher suite.
- Certificate chain.
- Certificate subject.
- Certificate issuer.
- Certificate validity.
- Handshake behavior.

**Cybersecurity relevance:** TLS inspection is important when investigating HTTPS configurations, certificate errors, and encrypted network communication.

---

## 15. `jq` — JSON Processing

`jq` is a command-line utility for parsing, filtering, and transforming JSON data.

It is especially useful when working with APIs and security logs.

### Example JSON

```json
{
  "name": "Alex",
  "role": "admin",
  "active": true
}
```

### Extract a field

```bash
echo '{"name":"Alex","role":"admin"}' | jq '.name'
```

Output:

```text
"Alex"
```

### Extract multiple fields

```bash
echo '{"name":"Alex","role":"admin"}' | jq '.name, .role'
```

### Pretty-print JSON

```bash
cat data.json | jq .
```

### Extract data from an API response

```bash
curl -s https://api.example.com/users | jq .
```

### Filter an array

```bash
jq '.[] | select(.active == true)' users.json
```

### Cybersecurity relevance

- Analyze JSON security alerts.
- Filter SIEM events.
- Process API responses.
- Extract IP addresses and timestamps.
- Investigate structured application logs.

---

## 16. `ethtool` — Interface Information

`ethtool` is used to inspect and configure Ethernet network interfaces.

Availability depends on the installed package and supported hardware.

### Display interface information

```bash
sudo ethtool eth0
```

### Display driver information

```bash
sudo ethtool -i eth0
```

### Display link status

```bash
sudo ethtool eth0 | grep "Link detected"
```

### Information available

- Link status.
- Supported speeds.
- Duplex mode.
- Driver information.
- Auto-negotiation.
- Interface capabilities.

**Remember:** Some virtual interfaces and wireless interfaces do not support all `ethtool` features.

---

## 17. `nmcli` — NetworkManager Management

`nmcli` is the command-line interface for NetworkManager.

It helps manage network connections on Linux systems using NetworkManager.

### Show network devices

```bash
nmcli device status
```

### Show connection profiles

```bash
nmcli connection show
```

### Show active connections

```bash
nmcli connection show --active
```

### Show Wi-Fi networks

```bash
nmcli device wifi list
```

### Display detailed device information

```bash
nmcli device show
```

### Disconnect an interface

```bash
sudo nmcli device disconnect eth0
```

### Connect an interface

```bash
sudo nmcli device connect eth0
```

### Important note

Kali Linux installations may use NetworkManager, but the exact networking setup depends on the installation and whether Kali is running in a virtual machine.

**Cybersecurity relevance:** `nmcli` helps troubleshoot network connectivity and manage interfaces without a graphical desktop.

---

## 18. `resolvectl` — Resolver Diagnostics

`resolvectl` is a command-line tool for inspecting and managing the systemd-resolved DNS resolver, where available.

### View DNS configuration

```bash
resolvectl status
```

### Query a hostname

```bash
resolvectl query example.com
```

### Display DNS statistics

```bash
resolvectl statistics
```

### Flush DNS cache

```bash
sudo resolvectl flush-caches
```

### Important note

Not every Linux installation uses systemd-resolved.

If the command is unavailable, inspect the system's DNS configuration through other tools, such as:

```bash
cat /etc/resolv.conf
```

**Cybersecurity relevance:** DNS resolver diagnostics help investigate resolution failures, unexpected DNS servers, and DNS configuration issues.

---

# 30. Wireshark

## 1. What Is Packet Analysis?

Packet analysis is the process of capturing, examining, and interpreting network packets to understand communication between devices.

Network communication is divided into packets or frames that carry information from one system to another.

Packet analysis helps you understand:
- Which devices are communicating.
- Which protocols are being used.
- Which ports are involved.
- Whether communication is successful.
- Whether packets are retransmitted.
- Whether suspicious activity is present.

### Why packet analysis matters

**Network troubleshooting**
- Identify connectivity issues.
- Investigate packet loss.
- Diagnose DNS problems.
- Understand TCP connection failures.

**Cybersecurity**
- Investigate suspicious traffic.
- Identify unusual communication.
- Examine protocol behavior.
- Analyze potential attacks.
- Preserve network evidence.

### Example

A browser tries to access a website.

Packet analysis can help you observe:

```text
DNS Query
   ↓
DNS Response
   ↓
TCP Three-Way Handshake
   ↓
TLS Handshake
   ↓
Encrypted HTTPS Communication
```

Wireshark is one of the most widely used tools for this purpose.

---

## 2. Installing and Opening Wireshark

Wireshark is a graphical network protocol analyzer.

### Install on Kali Linux

Update package information:

```bash
sudo apt update
```

Install Wireshark:

```bash
sudo apt install wireshark
```

### Verify installation

```bash
wireshark --version
```

### Open Wireshark

```bash
wireshark
```

Depending on the installation, you may need appropriate permissions or capture capabilities.

### Capture permissions

On Linux, packet capture often uses `dumpcap` and capture permissions.

Follow the installation's permission prompts and security guidance. Avoid running the entire graphical Wireshark application as root just to obtain capture access.

### Verify capture interfaces

Open Wireshark and examine the available interfaces.

You may see:
- `eth0`
- `ens33`
- `wlan0`
- `lo`
- `any`

---

## 3. Selecting the Correct Capture Interface

A capture interface is the network interface from which Wireshark collects packets.

Choosing the wrong interface may result in capturing no relevant traffic.

### Common interfaces

| Interface | Meaning |
|---|---|
| `eth0` | Ethernet |
| `ens33` | Common VMware virtual Ethernet interface |
| `wlan0` | Wireless interface |
| `lo` | Loopback |
| `any` | Multiple Linux interfaces, where supported |

### How to select an interface

1. Open Wireshark.
2. Review the available interfaces.
3. Observe the traffic activity graph.
4. Select the interface carrying the communication you want to inspect.
5. Start the capture.

### Example

If Kali is running in VMware using a NAT network adapter, its traffic may appear on `eth0` or `ens33`.

The exact interface depends on the virtual machine configuration.

### Useful command

```bash
ip -br addr
```

This helps identify available interfaces and their IP addresses.

**Important:** Capturing on your Kali VM's virtual interface generally shows traffic visible to that VM. It does not automatically reveal every device's traffic on your physical Wi-Fi network.

---

## 4. Live Captures vs Saved PCAP Files

Wireshark can capture packets in real time or open previously saved packet captures.

### Live capture

A live capture records traffic as it happens.

Example:

```text
Browser request
      ↓
Wireshark captures packets
      ↓
Packets appear in real time
```

Useful for:
- Troubleshooting current connections.
- Observing DNS lookups.
- Understanding TCP handshakes.
- Investigating current network behavior.

### Saved PCAP files

A PCAP file stores captured packets for later analysis.

Example:

```bash
sudo tcpdump -i any -w capture.pcap
```

Open it in Wireshark:

```bash
wireshark capture.pcap
```

### Comparison

| Feature | Live Capture | Saved PCAP |
|---|---|---|
| Data source | Live network traffic | Previously captured traffic |
| Real-time view | Yes | No |
| Repeat analysis | Requires a new capture unless saved | Yes |
| Evidence preservation | Must save the capture | Already stored |
| Investigation | Current activity | Historical activity |

### PCAP and PCAPNG

- PCAP is a common packet capture format.
- PCAPNG is a newer, extensible format that can store additional capture metadata.

---

## 5. Packet List, Details, and Bytes Panes

Wireshark's main interface has three important analysis panes.

### 1. Packet List Pane

Displays a summary of captured packets.

Common columns:

| Column | Meaning |
|---|---|
| No. | Packet number |
| Time | Capture timestamp |
| Source | Source address |
| Destination | Destination address |
| Protocol | Protocol name |
| Length | Packet length |
| Info | Short packet description |

### 2. Packet Details Pane

Displays the protocol fields of the selected packet.

For example, expanding an Ethernet and IPv4 packet may show:

```text
Frame
Ethernet II
Internet Protocol Version 4
Transmission Control Protocol
```

You can expand individual sections to inspect their fields.

### 3. Packet Bytes Pane

Displays the selected packet's raw bytes in hexadecimal and ASCII representations.

This helps analysts inspect the actual packet data.

### Example

When selecting an HTTP request, you may see readable HTTP headers and data in the packet bytes pane.

For HTTPS, application data is generally encrypted, so you cannot simply read the HTTP contents from an ordinary capture.

---

## 6. Capture Filters vs Display Filters

This is one of the most important Wireshark concepts.

### Capture Filters

Capture filters decide which packets Wireshark records.

They are applied before packets are stored.

They use the libpcap filter syntax.

Examples:

Capture only DNS:

```text
port 53
```

Capture only TCP:

```text
tcp
```

Capture traffic involving a host:

```text
host 192.168.1.10
```

Capture traffic on a specific port:

```text
port 443
```

Capture traffic from a specific network:

```text
net 192.168.1.0/24
```

### Display Filters

Display filters decide which packets are shown from the captured data.

They do not remove other packets from the capture file.

Examples:

Show DNS:

```text
dns
```

Show TCP:

```text
tcp
```

Show HTTP:

```text
http
```

Show traffic involving an IP:

```text
ip.addr == 192.168.1.10
```

Show traffic to or from port 443:

```text
tcp.port == 443
```

### Comparison

| Feature | Capture Filter | Display Filter |
|---|---|---|
| Applied | Before packets are captured | After packets are captured |
| Purpose | Controls what gets recorded | Controls what is displayed |
| Syntax | BPF/libpcap syntax | Wireshark display-filter syntax |
| Can hide captured packets? | Excluded packets are not recorded | Yes, temporarily hidden |
| Example | `port 53` | `dns` |

**Remember:** Capture filters control collection; display filters control viewing.

---

## 7. Ethernet Frame Analysis

Ethernet is commonly used for communication within wired local area networks.

An Ethernet frame contains:
- Destination MAC address.
- Source MAC address.
- EtherType or length field.
- Payload.
- Frame Check Sequence (FCS), where present in the capture.

### Simplified Ethernet frame

```text
+-----------------------+
| Destination MAC       |
+-----------------------+
| Source MAC            |
+-----------------------+
| EtherType             |
+-----------------------+
| Payload               |
+-----------------------+
| FCS (if present)      |
+-----------------------+
```

### Important fields

**Destination MAC**

Identifies the intended destination on the local Layer 2 network.

**Source MAC**

Identifies the sending interface's MAC address.

**EtherType**

Identifies the payload protocol.

Common examples:

| EtherType | Protocol |
|---|---|
| `0x0800` | IPv4 |
| `0x0806` | ARP |
| `0x86DD` | IPv6 |

### Analyze in Wireshark

1. Capture traffic.
2. Select an Ethernet packet.
3. Expand `Ethernet II`.
4. Inspect source and destination MAC addresses.
5. Inspect the EtherType field.

**Important:** The Ethernet frame's FCS may not be visible because network interfaces commonly remove it before delivering captured packets to the operating system.

---

## 8. ARP Analysis

ARP resolves IPv4 addresses into MAC addresses on a local network.

Wireshark can display ARP requests and replies.

### Example ARP request

```text
Who has 192.168.1.1?
Tell 192.168.1.20
```

The device at `192.168.1.20` is asking for the MAC address associated with `192.168.1.1`.

### Example ARP reply

```text
192.168.1.1 is at AA:BB:CC:DD:EE:FF
```

The device replies with its MAC address.

### Wireshark filter

```text
arp
```

Show ARP requests:

```text
arp.opcode == 1
```

Show ARP replies:

```text
arp.opcode == 2
```

### What to investigate

- Which device sent the ARP request?
- Which IP address was requested?
- Which MAC address replied?
- Are there unexpected or conflicting IP-to-MAC mappings?

### Security relevance

Repeated unexpected ARP changes may indicate misconfiguration or possible ARP spoofing.

However, an ARP change alone is not sufficient proof of an attack.

---

## 9. DNS Analysis

DNS translates domain names into IP addresses.

Wireshark can help investigate DNS queries and responses.

### Example

A user visits:

```text
example.com
```

The computer sends a DNS query asking for its IP address.

A DNS server returns an answer.

### Wireshark display filter

```text
dns
```

Show DNS queries:

```text
dns.flags.response == 0
```

Show DNS responses:

```text
dns.flags.response == 1
```

Show queries for a particular name:

```text
dns.qry.name == "example.com"
```

Show DNS response errors:

```text
dns.flags.rcode != 0
```

### What to investigate

- Query name.
- Query type.
- DNS server.
- Response address.
- Response code.
- Query frequency.
- Unusual domains.

### Example DNS record types

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| MX | Mail server |
| NS | Name server |
| TXT | Text information |
| CNAME | Canonical name alias |
| PTR | Reverse DNS lookup |

### Security relevance

DNS analysis can help detect:
- Unexpected DNS servers.
- Suspicious domain lookups.
- Unusual query volume.
- Possible DNS tunneling.
- DNS resolution failures.

---

## 10. TCP Handshake Analysis

TCP uses a three-way handshake to establish a connection.

### Three-way handshake

```text
Client                         Server
  |                               |
  |---------- SYN --------------->|
  |                               |
  |<--------- SYN-ACK ------------|
  |                               |
  |---------- ACK --------------->|
  |                               |
  |       Connection established
```

### Step 1: SYN

The client requests a TCP connection.

### Step 2: SYN-ACK

The server acknowledges the request and sends its own synchronization message.

### Step 3: ACK

The client acknowledges the server's response.

The connection is established.

### Wireshark filter for SYN packets

```text
tcp.flags.syn == 1
```

Show SYN packets without ACK:

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

Show SYN-ACK packets:

```text
tcp.flags.syn == 1 && tcp.flags.ack == 1
```

Show ACK packets:

```text
tcp.flags.ack == 1
```

### What to investigate

- Did the server respond?
- Was the handshake completed?
- Were packets retransmitted?
- Was a TCP reset sent?
- Was the connection closed normally?

**Cybersecurity relevance:** Understanding the handshake helps investigate connection failures, SYN floods, and suspicious TCP activity.

---

## 11. Retransmissions and Resets

### TCP Retransmission

A TCP retransmission occurs when TCP resends data because the expected acknowledgment was not received within the relevant time.

Possible causes:
- Packet loss.
- Network congestion.
- Unstable wireless communication.
- Firewall interference.
- Delayed acknowledgments.

Wireshark may label packets as:

```text
[TCP Retransmission]
```

Display filter:

```text
tcp.analysis.retransmission
```

### TCP Reset (RST)

A TCP reset is used to abruptly terminate or reject a connection.

For example, a server may send a reset when a connection targets a port where no service is listening.

Display filter:

```text
tcp.flags.reset == 1
```

### Difference

| Feature | Retransmission | Reset |
|---|---|---|
| Meaning | Resending unacknowledged data | Abruptly rejecting or terminating a connection |
| Common reason | Packet loss or missing acknowledgment | No suitable connection or forced termination |
| Security relevance | May indicate network problems | May indicate scanning, rejected connections, or policy enforcement |

**Important:** Retransmissions and resets are not automatically signs of an attack. Always investigate surrounding traffic.

---

## 12. HTTP Request Analysis

HTTP is an application-layer protocol used for communication between web clients and servers.

Wireshark can inspect unencrypted HTTP requests and responses.

### Example HTTP request

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### Example HTTP response

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1200
```

### Wireshark filters

Show HTTP traffic:

```text
http
```

Show GET requests:

```text
http.request.method == "GET"
```

Show POST requests:

```text
http.request.method == "POST"
```

Show HTTP responses with status 404:

```text
http.response.code == 404
```

Show HTTP requests to a particular host:

```text
http.host == "example.com"
```

### What to inspect

- HTTP method.
- Request URI.
- Host header.
- User-Agent.
- Status code.
- Response headers.
- Cookies.
- Request body, where visible.

### Security relevance

HTTP analysis can help identify:
- Exposed credentials.
- Insecure cookies.
- Unexpected redirects.
- Unusual request patterns.
- Application errors.
- Suspicious web communication.

**Important:** HTTP is unencrypted. Sensitive information sent over HTTP may be readable to parties able to capture the traffic.

---

## 13. TLS Handshake Analysis

TLS stands for Transport Layer Security.

It protects communication by providing encryption, authentication, and integrity.

HTTPS is HTTP communication protected by TLS.

### Simplified TLS handshake

```text
Client                         Server
  |                               |
  |-------- ClientHello --------->|
  |                               |
  |<------- ServerHello ----------|
  |<------- Certificate ----------|
  |                               |
  |   Key establishment           |
  |                               |
  |-------- Finished ------------>|
  |<------- Finished -------------|
  |                               |
  |     Encrypted communication
```

This is a simplified conceptual sequence. The exact handshake messages differ between TLS versions and configurations.

### What to inspect in Wireshark

- ClientHello.
- ServerHello.
- Server certificate information, when visible.
- TLS version.
- Cipher suite.
- Server Name Indication (SNI), when visible.
- Handshake alerts.
- Connection failures.

### Wireshark filters

Show TLS traffic:

```text
tls
```

Show ClientHello:

```text
tls.handshake.type == 1
```

Show ServerHello:

```text
tls.handshake.type == 2
```

Show TLS handshake messages:

```text
tls.handshake
```

### Important limitation

Modern TLS encrypts application data.

A normal packet capture generally cannot reveal the contents of HTTPS requests and responses.

TLS 1.3 also encrypts more handshake information than earlier versions after the ServerHello.

**Cybersecurity relevance:** TLS analysis helps investigate certificate problems, protocol versions, cipher suites, and encrypted connection failures.

---

## 14. Follow TCP Stream

Wireshark's Follow TCP Stream feature reconstructs the application data exchanged within a TCP conversation.

Instead of examining packets individually, you can view the communication as a stream.

### How to use it

1. Capture or open a PCAP file.
2. Select a TCP packet.
3. Right-click the packet.
4. Select `Follow`.
5. Select `TCP Stream`.

Wireshark displays the reconstructed conversation.

### What it helps with

- Understanding client-server communication.
- Reading unencrypted HTTP requests.
- Investigating application protocols.
- Reviewing the sequence of messages.

### Example

You may see:

```text
Client:
GET /login HTTP/1.1

Server:
HTTP/1.1 200 OK
```

### Important limitation

Following a TCP stream does not decrypt HTTPS automatically.

For encrypted TLS traffic, application content remains protected unless you have a legitimate decryption method and the necessary session secrets.

---

## 15. Exporting Objects Where Appropriate

Wireshark can extract certain objects transferred through supported protocols.

For example, an HTTP capture may contain downloadable files.

### How to export HTTP objects

1. Open a suitable PCAP file.
2. Select `File`.
3. Select `Export Objects`.
4. Select `HTTP`.
5. Review the available objects.
6. Save the required object if authorized.

### Why this is useful

- Malware investigations.
- File transfer analysis.
- Evidence collection.
- Understanding web communication.

### Security considerations

Extracted files may contain malware.

Do not execute unknown files on your normal system.

Use an isolated analysis environment and appropriate safety controls.

**Important:** Object export depends on the protocol and the available captured data. Encrypted HTTPS application content generally cannot be exported as ordinary readable HTTP objects from a normal capture.

---

## 16. Saving Evidence and Documenting Findings

Packet captures can serve as evidence during network investigations.

A good investigation should preserve the original capture and document the analysis.

### Evidence handling

- Save the original PCAP or PCAPNG file.
- Record the capture date and time.
- Record the capture interface.
- Document the capture filter, if used.
- Record the tool and version.
- Avoid modifying the original evidence.
- Restrict access to captured files.
- Calculate a file hash to help verify integrity.

### Calculate SHA-256 hash

```bash
sha256sum capture.pcap
```

Example:

```text
a1b2c3... capture.pcap
```

Save the hash alongside the evidence.

### Example investigation record

```text
Investigation ID: NET-001
Capture file: capture.pcap
Capture interface: eth0
Capture date: 2026-11-07
Tool: Wireshark
Observation: Repeated DNS queries
Source IP: 192.168.1.20
Destination IP: 192.168.1.1
Finding: Requires further investigation
```

### Why documentation matters

- Supports incident investigation.
- Makes findings reproducible.
- Helps other analysts review evidence.
- Maintains a clear investigation timeline.
- Supports audit and reporting requirements.

---

## 17. Privacy Considerations When Capturing Traffic

Network captures may contain sensitive information.

Depending on the protocols and encryption, captures may expose:
- IP addresses.
- MAC addresses.
- DNS queries.
- Website destinations.
- Session metadata.
- Cookies.
- Credentials transmitted over unencrypted protocols.
- Personal or business information.

### Best practices

- Capture only what is necessary.
- Obtain permission before monitoring a network.
- Avoid capturing other people's private communications.
- Store captures securely.
- Restrict access to evidence.
- Delete captures according to retention policies.
- Redact sensitive data before sharing screenshots or reports.
- Avoid publishing raw PCAP files without reviewing them.

**Remember:** Having the technical ability to capture traffic does not mean you have permission to inspect it.

---

# 31. Nmap

## 1. What Nmap Does and Does Not Do

Nmap stands for Network Mapper.

It is an open-source network discovery and security auditing tool.

It is widely used by network administrators, penetration testers, and security researchers.

### What Nmap does

- Discovers live hosts.
- Identifies open ports.
- Detects available network services.
- Performs service/version detection.
- Attempts operating system detection.
- Identifies certain network characteristics.
- Saves scan results for later analysis.

### What Nmap does not automatically do

- Prove that a system is vulnerable.
- Guarantee detection of every open port.
- Guarantee accurate operating system identification.
- Automatically exploit discovered vulnerabilities.
- Bypass every firewall.
- Identify every application security issue.

### Example

A scan may report:

```text
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https
```

This tells you that these ports appear open and have services commonly associated with SSH, HTTP, and HTTPS.

It does not prove that those services are vulnerable.

---

## 2. Host Discovery

Host discovery is the process of identifying which systems are reachable on a network.

Nmap uses different probes depending on the scan type and privileges.

### Basic host discovery

```bash
nmap -sn 192.168.1.0/24
```

The `-sn` option performs host discovery without a port scan.

### Scan one host for availability

```bash
nmap -sn 192.168.1.10
```

### Disable DNS resolution

```bash
nmap -n -sn 192.168.1.0/24
```

### Why host discovery matters

- Identifies active devices.
- Helps build an asset inventory.
- Locates test systems.
- Supports network administration.

### Important limitation

A host may be online but fail to respond to the discovery probes.

For example:
- ICMP may be blocked.
- A firewall may filter probes.
- The host may only respond to certain traffic.

Therefore, an Nmap host discovery result should not always be treated as definitive proof that a device is offline.

---

## 3. TCP Connect Scans

A TCP connect scan attempts to establish a complete TCP connection to a target port.

It uses the operating system's normal connection mechanism.

### Command

```bash
nmap -sT 192.168.1.10
```

### How it works

For an open TCP port:

```text
Scanner                  Target
   |                        |
   |-------- SYN ---------->|
   |<------- SYN-ACK -------|
   |-------- ACK ---------->|
   |                        |
   |   Connection established
```

The scanner completes the TCP handshake.

### Advantages

- Works without raw-packet privileges on many systems.
- Straightforward and reliable for many environments.
- Useful when SYN scanning is unavailable.

### Limitations

- Completes connections.
- Can be more visible in service logs.
- May be slower than some alternative scan types.

---

## 4. SYN Scan Concepts

A SYN scan is commonly called a half-open scan because it does not normally complete the full TCP handshake.

### Command

```bash
sudo nmap -sS 192.168.1.10
```

### How it works

For an open port:

```text
Scanner                  Target
   |                        |
   |-------- SYN ---------->|
   |<------- SYN-ACK -------|
   |                        |
   |-------- RST ---------->|
   |                        |
```

The scanner receives SYN-ACK and sends a reset instead of completing a normal connection.

### Common interpretations

| Response | Likely port state |
|---|---|
| SYN-ACK | Open |
| RST | Closed |
| No response or certain ICMP errors | Filtered or otherwise uncertain |

### Advantages

- Often efficient.
- Does not normally complete the TCP connection.
- Useful for authorized security assessments.

### Limitations

- Usually requires raw-packet privileges.
- Firewalls may filter probes.
- Network devices may alter responses.
- It is not invisible or guaranteed to avoid detection.

**Remember:** A SYN scan is not an undetectable scan.

---

## 5. UDP Scan Concepts

UDP is a connectionless transport protocol.

Unlike TCP, UDP does not use a three-way handshake.

Nmap UDP scans attempt to determine whether UDP ports are open, closed, or filtered.

### Command

```bash
sudo nmap -sU 192.168.1.10
```

### How it works

Nmap sends UDP probes to target ports and examines responses.

Possible results:

| Response | Likely state |
|---|---|
| UDP response | Open |
| ICMP Port Unreachable | Closed |
| No response | Open or filtered |
| Other relevant ICMP errors | Often filtered |

### Why UDP scans can be difficult

- UDP services may not respond to arbitrary probes.
- Firewalls may silently drop packets.
- ICMP responses may be rate-limited.
- Scans can take longer.

### Common UDP services

| Port | Service |
|---|---|
| 53 | DNS |
| 67/68 | DHCP |
| 123 | NTP |
| 161 | SNMP |
| 500 | IKE |

**Important:** A UDP port with no response is not automatically open. Nmap may report it as `open|filtered`.

---

## 6. Port Ranges

Nmap supports scanning individual ports, selected ports, ranges, and all TCP ports.

### Scan one port

```bash
nmap -p 80 192.168.1.10
```

### Scan multiple ports

```bash
nmap -p 22,80,443 192.168.1.10
```

### Scan a range

```bash
nmap -p 1-1000 192.168.1.10
```

### Scan all TCP ports

```bash
nmap -p- 192.168.1.10
```

### Scan the most common 100 ports

```bash
nmap --top-ports 100 192.168.1.10
```

### Scan all ports for a selected protocol

TCP and UDP are scanned separately:

```bash
nmap -sS -p- 192.168.1.10
```

```bash
sudo nmap -sU -p- 192.168.1.10
```

**Important:** A full UDP scan can take a long time. Use a clearly defined authorized scope and an appropriate scan plan.

---

## 7. Service/Version Detection

Nmap can attempt to identify the service and software version running on an open port.

### Command

```bash
nmap -sV 192.168.1.10
```

### Example output

```text
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH
80/tcp  open  http    Apache
443/tcp open  ssl/http
```

### Why service detection matters

Suppose a port scan identifies:

```text
80/tcp open http
```

Service detection may provide additional information about the web server.

This helps administrators:
- Identify outdated software.
- Review exposed services.
- Check patch status.
- Investigate unexpected service configurations.

### Important limitation

Version detection is based on service responses and probes.

The reported version may be:
- Incomplete.
- Incorrect.
- Hidden by a proxy.
- Modified by a custom server configuration.

Always verify important findings manually.

---

## 8. OS Detection Limitations

Nmap can attempt to estimate the target operating system using network behavior and TCP/IP characteristics.

### Command

```bash
sudo nmap -O 192.168.1.10
```

### How it works

Nmap examines characteristics such as:
- TCP response behavior.
- IP packet behavior.
- TCP window sizes.
- Network stack implementation details.

### Limitations

OS detection may be inaccurate because:
- Firewalls alter responses.
- Routers and proxies modify traffic.
- Virtual machines resemble other systems.
- Different operating systems may share similar network behavior.
- Too few ports are available for reliable fingerprinting.

### Remember

An OS detection result is an estimate, not guaranteed identification.

Confirm it using authorized administrative information or additional evidence where possible.

---

## 9. DNS Resolution Behavior

By default, Nmap may attempt reverse DNS lookups for discovered addresses.

This can make scans slower and add DNS-related traffic.

### Disable DNS resolution

```bash
nmap -n 192.168.1.10
```

### Enable DNS resolution explicitly

```bash
nmap -R 192.168.1.10
```

### Use a specific DNS server

```bash
nmap --dns-servers 8.8.8.8 192.168.1.10
```

### Why DNS behavior matters

- DNS resolution can affect scan speed.
- Reverse DNS may provide useful hostnames.
- Incorrect DNS information can complicate interpretation.
- Some networks restrict DNS queries.

**Remember:** Nmap's DNS resolution is separate from the actual port state determination.

---

## 10. Output Formats

Nmap supports several output formats.

Saving scan results is important for documentation and comparison.

### Normal output

```bash
nmap -oN scan.txt 192.168.1.10
```

### XML output

```bash
nmap -oX scan.xml 192.168.1.10
```

### Grepable output

```bash
nmap -oG scan.gnmap 192.168.1.10
```

### All major formats

```bash
nmap -oA scan-results 192.168.1.10
```

This creates multiple output files with a common base name.

### Output format comparison

| Format | Purpose |
|---|---|
| Normal | Human-readable results |
| XML | Structured output for tools and automation |
| Grepable | Easier text-based processing |
| All (`-oA`) | Saves multiple formats |

### Why save results?

- Compare scans over time.
- Document findings.
- Build asset inventories.
- Share results with authorized teams.
- Automate analysis.

---

## 11. Scan Timing and Network Impact

Nmap provides timing options that influence how quickly it sends probes.

Faster scans are not always better.

Aggressive scanning can:
- Increase network traffic.
- Trigger intrusion detection alerts.
- Affect fragile services.
- Produce incomplete results on congested networks.

### Timing templates

Nmap provides timing templates from T0 to T5.

| Template | Description |
|---|---|
| T0 | Paranoid; extremely slow |
| T1 | Sneaky; very slow |
| T2 | Polite; slower |
| T3 | Normal default |
| T4 | Aggressive; faster |
| T5 | Insane; very fast |

### Example

Use a normal scan:

```bash
nmap -T3 192.168.1.10
```

Use a faster timing template in an authorized lab:

```bash
nmap -T4 192.168.1.10
```

### Important considerations

- Faster timing can reduce accuracy on unreliable networks.
- Firewalls may react to scan traffic.
- Rate limits may affect results.
- Network owners may have operational restrictions.

Choose scan timing based on the authorized testing scope and the target environment.

---

## 12. Understanding Filtered, Open, and Closed Ports

Nmap classifies port states based on the responses it receives.

### Open

A service is accepting connections on the port.

Example:

```text
80/tcp open http
```

### Closed

The host is reachable, but no application is listening on that port.

Example:

```text
8080/tcp closed http-proxy
```

### Filtered

Nmap cannot determine whether the port is open because a firewall or other network filter prevents a clear response.

Example:

```text
443/tcp filtered https
```

### Open|Filtered

Nmap cannot distinguish between an open port that does not respond and a filtered port.

This commonly appears in UDP scans.

### Closed|Filtered

Nmap cannot distinguish between a closed port and a filtered port under the scan conditions.

### Comparison

| State | Meaning |
|---|---|
| Open | Service accepts connections |
| Closed | Host responds, but no service listens |
| Filtered | Filtering prevents a clear determination |
| Open\|Filtered | Open or filtered cannot be distinguished |
| Closed\|Filtered | Closed or filtered cannot be distinguished |

---

## 13. Interpreting Results

Nmap results should be interpreted carefully.

### Example scan

```text
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
443/tcp  open     https
3306/tcp filtered mysql
```

### Interpretation

**Port 22 — SSH**

An SSH service appears to be accepting connections.

Investigate:
- Is SSH required?
- Is password authentication enabled?
- Is access restricted?
- Is the software patched?

**Port 80 — HTTP**

An HTTP service appears to be available.

Investigate:
- Does it redirect to HTTPS?
- Are sensitive pages exposed?
- Are security headers configured appropriately?

**Port 443 — HTTPS**

An HTTPS service appears to be available.

Investigate:
- TLS configuration.
- Certificate validity.
- Supported protocols.
- Application security.

**Port 3306 — MySQL**

The port is filtered.

This does not establish whether MySQL is running. A firewall or network filter may be preventing a reliable result.

### Important principle

An open port is an observation, not a vulnerability.

A security finding requires additional evidence about the service, configuration, exposure, and impact.

---

## 14. Confirming Findings Manually

Automated scan results should be validated before reporting them.

### Example: Confirm an HTTP service

```bash
curl -I http://192.168.1.10
```

### Example: Confirm an HTTPS service

```bash
curl -I https://192.168.1.10
```

Certificate verification may fail when testing an IP address instead of the certificate's hostname.

### Example: Test TCP connectivity

```bash
nc -vz 192.168.1.10 22
```

### Example: Inspect service version

```bash
nmap -sV -p 22 192.168.1.10
```

### Example: Inspect TLS

```bash
openssl s_client -connect 192.168.1.10:443
```

### Why manual verification matters

- Scan results may be inaccurate.
- Services may use non-standard ports.
- Proxies can hide backend services.
- Firewalls can affect responses.
- Version information may be incomplete.

**Remember:** Confirm important findings using more than one source of evidence.

---

## 15. Running Scans Only Within Authorized Scope

Authorization is essential when using Nmap.

Before scanning, confirm:
- Which IP addresses are included?
- Which domains are included?
- Which ports may be tested?
- Are UDP scans permitted?
- Are aggressive scans permitted?
- Are there restrictions on scan timing?
- Are production systems involved?
- Who should be contacted if a service becomes unstable?

### Safe practice

Use:
- Your Kali Linux VM.
- Your own laptop.
- Your own virtual machines.
- A deliberately vulnerable lab.
- A training environment that explicitly permits scanning.

### Example: Scan a local lab machine

```bash
nmap -sV 192.168.56.101
```

Only use the example address if it belongs to your authorized lab.

### Bug bounty scope

For bug bounty programs:
- Read the program policy.
- Check the in-scope domains and IPs.
- Follow rate limits.
- Avoid prohibited testing methods.
- Do not scan unrelated infrastructure.
- Do not access, modify, or download other people's data.

**Important:** Public accessibility does not mean unrestricted authorization.

---

# Practical Lab Exercises

These exercises use your Kali Linux environment and systems you own or have permission to test.

## Lab 1: Inspect Your Network Configuration

Objective: Understand your Linux network interfaces and routes.

Run:

```bash
ip -br addr
```

```bash
ip route
```

```bash
ip neigh
```

```bash
nmcli device status
```

Questions:

1. Which network interfaces are available?
2. Which interface has an IP address?
3. What is your default gateway?
4. Is NetworkManager managing your interface?
5. Which neighboring devices are listed?

## Lab 2: Test Connectivity

Objective: Understand connectivity testing.

Run:

```bash
ping -c 4 127.0.0.1
```

Then:

```bash
ping -c 4 <YOUR_GATEWAY_IP>
```

Finally:

```bash
ping -c 4 example.com
```

Questions:

1. Does loopback respond?
2. Does your gateway respond?
3. Does the domain resolve?
4. Is there packet loss?
5. What could cause ping to fail?

## Lab 3: DNS Investigation

Objective: Learn DNS record queries.

Run:

```bash
dig example.com
```

```bash
dig example.com A
```

```bash
dig example.com MX
```

```bash
dig example.com NS
```

```bash
host example.com
```

Questions:

1. What is the A record?
2. Does the domain have an AAAA record?
3. Which name servers are authoritative?
4. What is the difference between `dig` and `host`?

## Lab 4: Inspect Listening Ports

Objective: Identify services running on Kali.

Run:

```bash
sudo ss -tulnp
```

Identify:
- Listening TCP ports.
- Listening UDP ports.
- Process names.
- Local addresses.

Questions:

1. Which services are listening?
2. Are they bound to `127.0.0.1` or `0.0.0.0`?
3. Which services need network access?
4. Are any unnecessary services running?

## Lab 5: Capture Your Own Traffic

Objective: Understand tcpdump and PCAP files.

Start a capture:

```bash
sudo tcpdump -i any -w phase13-lab.pcap
```

In another terminal, run:

```bash
dig example.com
```

```bash
curl -I https://example.com
```

Stop the capture using `Ctrl + C`.

Read the capture:

```bash
tcpdump -nn -r phase13-lab.pcap
```

Open it in Wireshark:

```bash
wireshark phase13-lab.pcap
```

Questions:

1. Can you identify DNS queries?
2. Can you identify TCP connections?
3. Can you identify TLS handshakes?
4. Which application data is encrypted?

## Lab 6: Wireshark Filter Practice

Objective: Learn display filters.

Open your saved capture and try:

```text
dns
```

```text
tcp
```

```text
tls
```

```text
tcp.flags.syn == 1
```

```text
tcp.flags.reset == 1
```

```text
ip.addr == YOUR_KALI_IP
```

Questions:

1. How many DNS packets are visible?
2. Can you identify a TCP handshake?
3. Can you identify a TLS handshake?
4. What changes when you apply a display filter?

## Lab 7: Nmap Against Your Own Lab Machine

Objective: Understand host discovery and port scanning.

Find your test machine's IP address.

Run:

```bash
nmap -sn <YOUR_LAB_IP>
```

Then:

```bash
nmap -sT <YOUR_LAB_IP>
```

If authorized, compare with:

```bash
sudo nmap -sS <YOUR_LAB_IP>
```

Detect service versions:

```bash
nmap -sV <YOUR_LAB_IP>
```

Save results:

```bash
nmap -oA phase13-results <YOUR_LAB_IP>
```

Questions:

1. Is the host reachable?
2. Which ports are open?
3. Which services are detected?
4. What is the difference between TCP connect and SYN scans?
5. Why might results differ between scans?

---

# Important Command Comparison

| Task | Tool |
|---|---|
| Inspect IP addresses | `ip` |
| Test connectivity | `ping` |
| Inspect listening ports | `ss` |
| Send HTTP requests | `curl` |
| Download files | `wget` |
| Query DNS records | `dig` |
| Quick DNS lookup | `host` |
| Trace network route | `traceroute` / `tracepath` |
| Analyze route and loss | `mtr` |
| Test TCP/UDP sockets | `nc` |
| Capture packets | `tcpdump` |
| Discover hosts and ports | `nmap` |
| Inspect registration data | `whois` |
| Inspect TLS | `openssl s_client` |
| Process JSON | `jq` |
| Inspect Ethernet interface | `ethtool` |
| Manage network connections | `nmcli` |
| Diagnose DNS resolver | `resolvectl` |
| Analyze packets graphically | Wireshark |

---

# Important Differences to Remember

| Concepts | Difference |
|---|---|
| `ip` vs `ifconfig` | Modern network configuration tool vs older tool |
| `ping` vs `traceroute` | Tests reachability vs examines the route |
| `ss` vs `nmap` | Inspects local sockets vs scans remote network ports |
| `curl` vs `wget` | General data transfer/API testing vs convenient file retrieval |
| `dig` vs `host` | Detailed DNS investigation vs simple DNS lookup |
| `tcpdump` vs Wireshark | Command-line capture and analysis vs graphical packet analysis |
| Capture filter vs display filter | Controls what is recorded vs what is displayed |
| PCAP vs PCAPNG | Packet capture formats with different capabilities |
| TCP connect vs SYN scan | Completes handshake vs normally does not complete it |
| TCP scan vs UDP scan | TCP connection-oriented probing vs connectionless UDP probing |
| Open vs Closed | Service accepting connections vs no service listening |
| Closed vs Filtered | Explicit indication of no listener vs filtering prevents a clear result |
| Port scanning vs Service detection | Identifies port states vs investigates services and versions |
| `whois` vs `dig` | Registration information vs DNS information |

---

# Quick Revision

1. `ip` displays and manages network interfaces, addresses, and routes.
2. `ping` checks connectivity using ICMP.
3. `ss` displays sockets and listening ports.
4. `curl` sends HTTP requests and transfers data.
5. `wget` downloads files.
6. `dig` performs detailed DNS queries.
7. `host` performs simple DNS lookups.
8. `traceroute` and `tracepath` help investigate network paths.
9. `mtr` combines route diagnostics and repeated connectivity measurements.
10. `nc` tests network sockets.
11. `tcpdump` captures and analyzes packets from the terminal.
12. `nmap` performs authorized network discovery and security auditing.
13. `whois` queries domain and IP registration databases.
14. `openssl s_client` inspects TLS connections.
15. `jq` processes JSON data.
16. `ethtool` provides Ethernet interface information.
17. `nmcli` manages NetworkManager connections.
18. `resolvectl` diagnoses systemd-resolved DNS configuration.
19. Wireshark is a graphical packet analyzer.
20. Packet analysis helps investigate network communication.
21. A capture interface determines where packets are collected.
22. PCAP files store packet captures.
23. Capture filters control which packets are recorded.
24. Display filters control which captured packets are shown.
25. Ethernet frames contain source and destination MAC addresses.
26. ARP resolves IPv4 addresses to MAC addresses.
27. DNS resolves domain names.
28. TCP uses a three-way handshake.
29. Retransmissions may indicate packet loss or delayed acknowledgments.
30. TCP RST packets abruptly reject or terminate connections.
31. HTTP traffic is generally readable without encryption.
32. HTTPS protects HTTP communication using TLS.
33. Follow TCP Stream reconstructs a TCP conversation.
34. Nmap identifies hosts, ports, and services.
35. TCP connect scans complete the TCP handshake.
36. SYN scans normally do not complete the handshake.
37. UDP scans can be difficult to interpret because UDP services may not respond.
38. Service detection attempts to identify software and versions.
39. OS detection provides an estimate, not guaranteed identification.
40. Nmap can save results in normal, XML, and grepable formats.
41. Open ports are not automatically vulnerabilities.
42. Scan results should be manually verified.
43. Only scan systems within your authorized scope.

---

# Interview Questions

## Beginner Level

1. What is the purpose of the `ip` command?
2. What is the difference between `ping` and `traceroute`?
3. What is the purpose of the `ss` command?
4. What is the difference between `curl` and `wget`?
5. What is DNS?
6. What is the difference between `dig` and `host`?
7. What is Netcat?
8. What is tcpdump?
9. What is Nmap?
10. What is packet analysis?
11. What is a PCAP file?
12. What is Wireshark?
13. What is the difference between HTTP and HTTPS?
14. What is TLS?
15. What is a TCP three-way handshake?

## Intermediate Level

16. Explain how `ip route` works.
17. How can you identify listening ports in Linux?
18. How do you capture DNS traffic using tcpdump?
19. What is the difference between capture filters and display filters?
20. How do you identify ARP requests in Wireshark?
21. How do you identify TCP SYN packets?
22. What are TCP retransmissions?
23. What is the purpose of Follow TCP Stream?
24. How can you inspect a TLS handshake?
25. What is the difference between PCAP and PCAPNG?
26. What is Nmap host discovery?
27. What is a TCP connect scan?
28. What is a SYN scan?
29. How does UDP scanning work?
30. What is service/version detection?

## Advanced Level

31. How would you troubleshoot a server that does not respond to ping?
32. How would you investigate DNS resolution failure?
33. How would you identify an unexpected listening service?
34. How would you investigate suspicious traffic using Wireshark?
35. How can you identify a TCP handshake failure?
36. How would you investigate repeated TCP retransmissions?
37. Why might a Wireshark capture not show HTTP request contents?
38. What is the difference between an open and filtered port?
39. Why can Nmap OS detection be inaccurate?
40. How would you validate an Nmap service detection result?
41. How can you reduce the network impact of an Nmap scan?
42. How would you document a packet capture investigation?
43. How can you identify suspicious DNS queries in a PCAP?
44. What information can `openssl s_client` provide?
45. Why is authorization important before network scanning?

---

# How This Phase Connects to Your Web Application Security Goal

These tools are not just networking utilities. They will become part of your everyday security workflow.

| Tool | How it helps in web security |
|---|---|
| `curl` | Test HTTP requests, APIs, headers, cookies, and authentication |
| `dig` | Investigate DNS records and subdomains |
| `whois` | Research domain registration information |
| `nmap` | Discover authorized exposed services |
| `nc` | Test connectivity to services |
| `ss` | Understand local listening services |
| `tcpdump` | Capture network communication |
| Wireshark | Understand HTTP, TCP, DNS, and TLS behavior |
| `openssl s_client` | Inspect HTTPS and TLS configurations |
| `jq` | Analyze JSON API responses and security data |
| `mtr` | Investigate connectivity and routing issues |

## Recommended learning priority

For your web and application security direction, become especially comfortable with:

**Priority 1 — Learn thoroughly**
1. `ip`
2. `ping`
3. `ss`
4. `curl`
5. `dig`
6. `nc`
7. `tcpdump`
8. Wireshark
9. Nmap
10. `openssl s_client`

**Priority 2 — Learn as needed**
1. `wget`
2. `host`
3. `traceroute`
4. `mtr`
5. `whois`
6. `jq`
7. `nmcli`
8. `resolvectl`
9. `ethtool`

You do not need to memorize every command or option. Learn what each tool does, understand its output, and practice using it in your Kali environment.

**Your next logical step:** After this phase, start connecting these networking concepts to web application security: HTTP request manipulation, authentication, session management, access control, API testing, and Burp Suite.
