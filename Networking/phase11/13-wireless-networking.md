
# Phase 11: Wireless Networking

## 26. Wi-Fi Fundamentals

### 26.1 Wireless Networking Basics

Wireless networking allows devices to communicate without physical network cables, using radio waves to transmit data.

Wi-Fi is based on the IEEE 802.11 family of wireless networking standards.

Examples of wireless devices:
- Laptops.
- Smartphones.
- Tablets.
- Wireless printers.
- Smart TVs.
- IoT devices.
- Wireless access points.

Basic architecture:

```text
Laptop ─────┐
            |
Phone ──────┼── Wi-Fi Access Point ─── Router ─── Internet
            |
Tablet ─────┘
```

A wireless device communicates with an access point (AP), which provides connectivity to a wired or wireless network.

Important concepts:
- Radio frequency (RF).
- Frequency bands.
- Channels.
- Signal strength.
- Interference.
- Authentication.
- Encryption.
- Wireless access control.

### 26.2 IEEE 802.11 Standards — Overview

IEEE 802.11 is a family of standards defining wireless LAN communication.

Common generations:

| Standard | Wi-Fi generation | Frequency bands |
|---|---|---|
| 802.11b | Legacy | 2.4 GHz |
| 802.11a | Legacy | 5 GHz |
| 802.11g | Legacy | 2.4 GHz |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz |
| 802.11ac | Wi-Fi 5 | 5 GHz |
| 802.11ax | Wi-Fi 6 / 6E | 2.4, 5, and 6 GHz depending on device and region |
| 802.11be | Wi-Fi 7 | 2.4, 5, and 6 GHz |

Important technologies:

- **MIMO:** Uses multiple antennas to improve wireless communication.
- **MU-MIMO:** Allows an access point to communicate with multiple clients using multiple spatial streams.
- **OFDMA:** Divides a channel into smaller resource units to serve multiple devices efficiently.
- **Beamforming:** Focuses radio energy toward a client to improve signal quality.
- **Channel bonding:** Combines adjacent channels to increase bandwidth.

Wi-Fi 6E extends Wi-Fi 6 operation into the 6 GHz band. Wi-Fi 7 introduces improvements such as Multi-Link Operation (MLO).

Actual capabilities depend on the router, client device, channel configuration, and local regulations.

### 26.3 2.4 GHz, 5 GHz, and 6 GHz Bands

Wi-Fi operates across different radio frequency bands.

| Feature | 2.4 GHz | 5 GHz | 6 GHz |
|---|---|---|---|
| Range | Generally longer | Generally shorter | Generally shorter |
| Wall penetration | Usually better | Usually weaker | Usually weaker |
| Interference | Often higher | Often lower | Often lower in suitable environments |
| Available channels | Fewer | More | More |
| Typical speed potential | Lower | Higher | Higher |
| Device compatibility | Very widespread | Widespread | Requires compatible devices |

**2.4 GHz:**
- Offers good coverage.
- Can penetrate walls relatively well.
- Often experiences interference from Bluetooth devices and other equipment.
- Commonly used by older and IoT devices.

**5 GHz:**
- Supports wider channels and higher potential throughput.
- Usually has less interference than crowded 2.4 GHz environments.
- Has shorter effective range through obstacles.

**6 GHz:**
- Provides additional spectrum for compatible Wi-Fi 6E and Wi-Fi 7 devices.
- Can support wider channels.
- Requires compatible access points and clients.
- Availability and permitted channels depend on national regulations.

No frequency band is automatically secure. Security depends on authentication, encryption, and configuration.

### 26.4 Channels and Interference

A Wi-Fi channel is a portion of the frequency spectrum used for wireless communication.

Different access points can use different channels to reduce interference.

Example:

```text
2.4 GHz band:

Channel 1
Channel 6
Channel 11
```

These are commonly used non-overlapping 20 MHz channel choices in many 2.4 GHz deployments, subject to local regulations.

Common sources of interference:
- Nearby Wi-Fi networks.
- Bluetooth devices.
- Microwave ovens.
- Wireless cameras.
- Other radio-frequency equipment.
- Physical obstacles.

**Co-channel interference:** Multiple access points share the same channel and compete for airtime.

**Adjacent-channel interference:** Overlapping channels interfere with each other.

Ways to reduce interference:
- Select suitable channels.
- Avoid unnecessary channel width.
- Position access points properly.
- Use 5 GHz or 6 GHz where appropriate.
- Perform a wireless site survey in larger environments.

### 26.5 SSID and BSSID

**SSID (Service Set Identifier)** is the network name displayed when scanning for Wi-Fi networks.

Example:

```text
SSID: Home_WiFi
```

**BSSID (Basic Service Set Identifier)** identifies a particular wireless access point radio interface, commonly represented by a MAC address.

Example:

```text
BSSID: AA:BB:CC:11:22:33
```

Difference:

| SSID | BSSID |
|---|---|
| Network name | Access point radio identifier |
| Can be shared by multiple APs | Identifies a particular BSS |
| Displayed as Wi-Fi name | Commonly represented as a MAC address |

Multiple access points can advertise the same SSID to provide roaming across a larger area.

Hiding an SSID does not provide meaningful security. Attackers may still discover the network through wireless traffic and client behavior.

### 26.6 Access Points and Clients

An **Access Point (AP)** provides wireless connectivity to client devices.

A **wireless client** is a device that connects to the AP.

Example:

```text
          Access Point
          /    |    \
         /     |     \
      Laptop  Phone  Tablet
```

Common access point functions:
- Advertise wireless networks.
- Handle client associations.
- Enforce wireless security.
- Forward traffic to the network.
- Manage wireless channels.
- Support client roaming.

The access point may be built into a home router or deployed as a separate enterprise device.

### 26.7 WPA2-Personal

**WPA2-Personal** is a Wi-Fi security mode commonly used in home networks.

It uses a pre-shared key (PSK), generally derived from the Wi-Fi password, to authenticate devices and establish encryption keys.

Common encryption:

- AES-CCMP.

Basic connection process:

```text
Client
  |
  | Connects using Wi-Fi password
  v
Access Point
  |
  | Authentication and key establishment
  v
Encrypted Wireless Communication
```

Important concepts:
- PSK: Pre-shared key.
- Four-way handshake: Establishes and confirms session keys.
- CCMP: Provides encryption and integrity protection using AES.

Security recommendations:
- Use a long, unique Wi-Fi password.
- Avoid dictionary words and predictable passwords.
- Disable WEP and WPA/TKIP.
- Update router firmware.
- Avoid sharing the main network password unnecessarily.

WPA2-Personal is still widely deployed, but WPA3-Personal is preferred when supported by all required devices.

### 26.8 WPA3-Personal

**WPA3-Personal** is a newer Wi-Fi security standard designed to improve security over WPA2-Personal.

It uses **SAE (Simultaneous Authentication of Equals)** instead of the traditional PSK authentication approach.

Benefits:
- Better protection against offline password-guessing attacks.
- Stronger authentication design.
- Improved protection against certain password-related attacks.
- Supports forward secrecy properties in its key establishment design.

WPA3-Personal commonly uses AES-CCMP, with stronger cryptographic options available in applicable configurations.

WPA3 transition mode may allow WPA2 and WPA3 devices to connect to the same network.

For better security:
- Prefer WPA3-only mode when device compatibility permits.
- Use a strong, unique password.
- Keep firmware updated.
- Disable insecure legacy security modes where possible.

WPA3 does not eliminate all wireless risks. Weak passwords, compromised routers, and insecure client devices remain potential problems.

### 26.9 Enterprise Wi-Fi and 802.1X

Enterprise Wi-Fi is commonly used by organizations that need individual user or device authentication.

Unlike Personal mode, it does not rely on one shared password for every user.

It commonly uses:
- IEEE 802.1X.
- EAP (Extensible Authentication Protocol).
- A RADIUS authentication server.

Architecture:

```text
Wireless Client
      |
      v
Access Point
      |
      v
RADIUS Server
      |
      v
Authentication Decision
```

Main components:

**Supplicant:**
- The client requesting network access.

**Authenticator:**
- The access point or network device controlling access.

**Authentication server:**
- Commonly a RADIUS server that verifies credentials.

Common EAP methods:
- EAP-TLS.
- PEAP.
- EAP-TTLS.

EAP-TLS uses certificates for mutual authentication and is a strong option when properly managed.

Security recommendations:
- Validate server certificates.
- Avoid accepting unexpected authentication servers.
- Use strong EAP configurations.
- Manage certificates and credentials carefully.
- Disable unused authentication methods.

### 26.10 Authentication vs Encryption

Authentication and encryption solve different problems.

**Authentication:** Verifies the identity of a user or device.

**Encryption:** Protects information from being read by unauthorized parties.

Example:

```text
Wi-Fi Authentication
        |
        v
Verify Client Identity
        |
        v
Establish Cryptographic Keys
        |
        v
Encrypted Wireless Traffic
```

Comparison:

| Authentication | Encryption |
|---|---|
| Answers "Who are you?" | Answers "Can others read the data?" |
| Verifies identity | Protects confidentiality |
| Uses credentials, certificates, or keys | Uses cryptographic algorithms and keys |

A wireless network may authenticate users but still be configured with inadequate encryption. Likewise, encryption does not automatically mean that the correct user is authorized to access a resource.

### 26.11 Guest Network Isolation

A guest network provides internet access to visitors without giving them unrestricted access to the main private network.

Example:

```text
                 Router
                   |
          ┌────────┴────────┐
          |                 |
       Main Wi-Fi        Guest Wi-Fi
          |                 |
      Private LAN        Internet Only
          |
    Computers / NAS
```

Benefits:
- Separates visitors from private devices.
- Limits access to internal resources.
- Reduces exposure from untrusted devices.
- Simplifies temporary access management.

Recommended configuration:
- Enable guest network isolation.
- Block access to the private LAN.
- Use a separate password.
- Enable client isolation where appropriate.
- Disable unnecessary management access.
- Set bandwidth or time limits if needed.

A guest SSID alone does not guarantee isolation. Verify the actual network segmentation and firewall rules.

### 26.12 Rogue Access Points

A **rogue access point** is an unauthorized wireless access point connected to or operating within an organization's network environment.

Example:

```text
Company Network
      |
      |
Unauthorized Wi-Fi AP
      |
      |
Attacker-Controlled Wireless Access
```

Potential risks:
- Unauthorized network access.
- Bypassing network security controls.
- Exposure of internal resources.
- Traffic interception.
- Creation of an uncontrolled entry point.

Detection and prevention:
- Monitor wireless infrastructure.
- Maintain an inventory of authorized APs.
- Use wireless intrusion detection systems.
- Restrict physical access to network ports.
- Monitor unusual network devices.
- Apply network access control.

A rogue AP is different from an unauthorized but externally operated nearby network. Context matters when classifying it.

### 26.13 Evil Twin Attacks — Concepts and Defenses

An **Evil Twin** is a fake wireless access point designed to imitate a legitimate Wi-Fi network.

Example:

```text
Legitimate Network:
Campus_WiFi

Fake Network:
Campus_WiFi
```

An attacker creates a network with a similar or identical SSID to trick users into connecting.

Potential risks:
- Credential theft through fake login portals.
- Traffic interception.
- Phishing.
- Collection of browsing metadata.
- Attempts to downgrade or bypass security protections.

Conceptual attack flow:

```text
Victim Device
      |
      v
Connects to Fake Access Point
      |
      v
Attacker-Controlled Network
      |
      v
Internet or Captive Portal
```

Defenses:
- Verify network identity with the organization.
- Prefer WPA2-Enterprise or WPA3-Enterprise with proper certificate validation.
- Avoid entering sensitive credentials into unexpected captive portals.
- Disable automatic connection to unknown networks.
- Use HTTPS and verify certificate warnings.
- Use a trusted VPN where appropriate.
- Monitor wireless networks in enterprise environments.

Important: HTTPS protects application traffic even when connected through an untrusted Wi-Fi network, provided certificate validation is correct. A VPN can add another layer of network protection, but neither makes a fake network harmless.

### 26.14 Wireless Monitoring Fundamentals

Wireless monitoring involves observing wireless network activity to understand performance, availability, and security.

Common monitoring information:
- SSIDs.
- BSSIDs.
- Signal strength.
- Channels.
- Frequency bands.
- Client associations.
- Authentication failures.
- Retransmissions.
- Interference.
- Rogue access points.

Common tools:

| Tool | Purpose |
|---|---|
| Wireshark | Analyze captured wireless or network packets |
| Kismet | Wireless network discovery and monitoring |
| Linux `iw` | Display and manage wireless device information |
| `nmcli` | Manage and inspect NetworkManager connections |
| Aircrack-ng suite | Wireless security auditing in authorized environments |

Monitoring concepts:

**RSSI (Received Signal Strength Indicator):**
- An indication of received signal power.
- Often expressed in dBm.

Example:

```text
-35 dBm = Strong signal
-60 dBm = Moderate signal
-80 dBm = Weak signal
```

These are approximate interpretations; actual quality depends on noise, interference, and hardware.

**SNR (Signal-to-Noise Ratio):**
- Difference between signal strength and noise level.
- Higher SNR generally means better signal quality.

**Packet loss and retransmissions:**
- Can indicate interference, congestion, or poor signal conditions.

### 26.15 Wireless Network Hardening

Wireless hardening means reducing security weaknesses through proper configuration and maintenance.

Recommended practices:

1. Use WPA3-Personal or WPA3-Enterprise where supported.
2. Use WPA2-AES when WPA3 is unavailable.
3. Disable WEP and WPA/TKIP.
4. Use a long, unique Wi-Fi password.
5. Change default router administrator credentials.
6. Update router firmware regularly.
7. Disable WPS if it is not required.
8. Create a separate guest network.
9. Enable client isolation where appropriate.
10. Restrict administrative access to trusted networks.
11. Disable remote administration unless necessary.
12. Monitor connected devices.
13. Remove unused wireless networks and credentials.
14. Use strong certificate validation for enterprise Wi-Fi.
15. Review DNS, DHCP, and firewall configuration.
16. Physically secure access points and network equipment.

**WPS (Wi-Fi Protected Setup):**

WPS is a feature designed to simplify connecting devices to a wireless network.

Some older WPS implementations have security weaknesses. Disable WPS PIN functionality when it is not required, and preferably disable WPS entirely if your environment does not need it.

### 26.16 Why Wi-Fi Security Is a Separate Specialization

Wireless security focuses on radio-frequency communication and the security of wireless infrastructure.

It involves knowledge of:
- IEEE 802.11 frame types.
- Radio-frequency behavior.
- Wireless authentication.
- WPA2 and WPA3.
- Enterprise Wi-Fi.
- Wireless monitoring.
- Wireless intrusion detection.
- Rogue access points.
- Wireless client behavior.

Web application security focuses more on:
- HTTP and HTTPS.
- Authentication and authorization.
- APIs.
- Sessions and cookies.
- SQL injection.
- Cross-site scripting.
- Access control.
- Business logic vulnerabilities.

There is some overlap, but the technical areas are different.

For a web application security and bug bounty path, wireless security is useful additional knowledge, not a prerequisite.

---

## Practical Labs

Perform these exercises only on your own wireless equipment or in an explicitly authorized wireless lab.

### Lab 1: Inspect Wireless Interfaces on Linux

List wireless interfaces:

```bash
iw dev
```

Display wireless device information:

```bash
iw list
```

Show network interfaces:

```bash
ip link
```

### Lab 2: Scan Nearby Wi-Fi Networks

Using NetworkManager:

```bash
nmcli device wifi list
```

Observe:
- SSID.
- BSSID.
- Signal strength.
- Channel.
- Security mode.

Scanning for publicly visible networks is different from attempting to access or disrupt them.

### Lab 3: Inspect Your Connected Wi-Fi Network

```bash
nmcli connection show --active
```

Display device status:

```bash
nmcli device status
```

Check your IP configuration:

```bash
ip addr
```

Check your default route:

```bash
ip route
```

### Lab 4: Understand Wi-Fi Security Settings

Log in to your own router's administration interface.

Inspect:
- Security mode.
- Encryption method.
- Frequency band.
- Channel.
- WPS status.
- Guest network configuration.
- Connected devices.

Do not change settings on a network you do not own or administer.

### Lab 5: Observe Wireless Signal Strength

```bash
nmcli -f IN-USE,SSID,BSSID,CHAN,SIGNAL,SECURITY device wifi list
```

Move your device closer to and farther from your access point.

Observe:
- Signal changes.
- Channel information.
- Network availability.
- Possible interference.

### Lab 6: Review Wireless Packets

If you have compatible hardware and an authorized capture environment, Wireshark can help you study wireless packet structures.

Learn to recognize:
- Beacon frames.
- Probe requests.
- Probe responses.
- Authentication frames.
- Association requests.
- Association responses.
- Data frames.

A normal Wi-Fi adapter may not support monitor mode. Hardware and driver support are required for certain wireless captures.

---

## Quick Revision

- Wi-Fi is based on the IEEE 802.11 family of standards.
- SSID is the wireless network name.
- BSSID identifies a particular basic service set, commonly through an AP radio's MAC address.
- Access points provide wireless connectivity to clients.
- 2.4 GHz generally offers longer range; 5 GHz and 6 GHz offer additional capacity and higher speed potential.
- Channels help organize wireless communication and reduce interference.
- WPA2-Personal uses a pre-shared key approach.
- WPA3-Personal uses SAE for improved password-based authentication.
- Enterprise Wi-Fi commonly uses 802.1X, EAP, and RADIUS.
- Authentication verifies identity; encryption protects data.
- Guest isolation separates visitors from private network resources.
- A rogue AP is an unauthorized access point.
- An Evil Twin imitates a legitimate Wi-Fi network.
- Wireless monitoring observes network activity, signal quality, and security events.
- Wireless hardening includes strong authentication, firmware updates, disabling unnecessary features, and network segmentation.
- Wireless security is a separate specialization from web application security.

## Interview Questions

1. What is wireless networking?
2. What is IEEE 802.11?
3. Explain Wi-Fi 4, Wi-Fi 5, Wi-Fi 6, Wi-Fi 6E, and Wi-Fi 7.
4. Compare 2.4 GHz, 5 GHz, and 6 GHz.
5. What is a Wi-Fi channel?
6. What is the difference between co-channel and adjacent-channel interference?
7. Explain SSID vs BSSID.
8. What is an access point?
9. What is WPA2-Personal?
10. What is WPA3-Personal, and how does SAE work at a high level?
11. Explain WPA2-Personal vs WPA2-Enterprise.
12. What is IEEE 802.1X?
13. What are supplicant, authenticator, and authentication server?
14. What is RADIUS?
15. Explain authentication vs encryption.
16. What is guest network isolation?
17. What is a rogue access point?
18. Explain an Evil Twin attack.
19. How can an Evil Twin attack be prevented?
20. What is wireless monitoring?
21. What are RSSI and SNR?
22. What is monitor mode?
23. What is WPS, and why can it be risky?
24. List important wireless network hardening practices.
25. Why is hiding an SSID not a reliable security measure?
26. Why should enterprise Wi-Fi clients validate authentication-server certificates?
27. What is the difference between Wi-Fi security and web application security?

---

## Learning Priority for Your Cybersecurity Roadmap

For a web and application security / bug bounty learning path:

**Learn now:**
- Wi-Fi fundamentals.
- WPA2 and WPA3 differences.
- SSID and BSSID.
- Access points and wireless clients.
- Basic wireless network hardening.
- Rogue AP and Evil Twin concepts.

**Learn later if you choose wireless security:**
- 802.11 frame analysis.
- Monitor mode.
- Wireless penetration-testing tools.
- Enterprise Wi-Fi security testing.
- Wireless intrusion detection.
- Advanced RF analysis.

Do not delay your web security progress to master wireless penetration testing. Your HTTP, HTTPS, DNS, TCP/IP, proxies, sessions, and API knowledge are much more directly relevant to your immediate bug bounty goals.
