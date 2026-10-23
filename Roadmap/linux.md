# Linux & Kali Linux Complete Roadmap for Cybersecurity

**Target specialization:** Web Application Security, Application Security (AppSec), and Authorized Penetration Testing  
**Level:** Beginner refresh → Intermediate → Practical security skills  
**Suggested duration:** 6–8 weeks for the core Linux and Kali skills  
**Daily study time:** 45–60 minutes, alongside Python and web security

---

# Part 1: Linux Fundamentals

## Phase 1 — Linux Introduction and Environment

- [ ] What is Linux?
- [ ] Linux vs Windows vs macOS
- [ ] Linux kernel, shell, terminal, and distribution
- [ ] What is GNU/Linux?
- [ ] Linux distributions: Ubuntu, Debian, Fedora, Arch, Kali Linux
- [ ] What is a desktop environment?
- [ ] CLI vs GUI
- [ ] Open-source software and package repositories
- [ ] Linux filesystem hierarchy
- [ ] Linux boot process — basic understanding
- [ ] Kernel space vs user space — basic understanding
- [ ] Linux processes and services — introduction
- [ ] Installing Linux in a virtual machine
- [ ] VirtualBox or VMware fundamentals
- [ ] Snapshots, virtual disks, RAM, CPU, and network settings

**Practical tasks**
- [ ] Install Ubuntu in a virtual machine.
- [ ] Open the terminal and run your first commands.
- [ ] Create a VM snapshot and restore it.
- [ ] Navigate the filesystem using terminal commands.

## Phase 2 — Essential Linux Commands

### Navigation and file management

- [ ] `pwd` — show current directory
- [ ] `ls`, `ls -la` — list files
- [ ] `cd` — change directory
- [ ] `tree` — view directory structure
- [ ] `mkdir` — create directories
- [ ] `touch` — create files
- [ ] `cp` — copy files
- [ ] `mv` — move or rename files
- [ ] `rm`, `rmdir` — remove files and directories
- [ ] Absolute vs relative paths
- [ ] Hidden files and directories
- [ ] Wildcards: `*`, `?`, and character patterns

### Reading and editing files

- [ ] `cat`
- [ ] `less`
- [ ] `head`
- [ ] `tail`
- [ ] `tail -f` for live log monitoring
- [ ] `nano`
- [ ] `vim` basics
- [ ] `file`
- [ ] `stat`
- [ ] `wc`
- [ ] `sort`
- [ ] `uniq`
- [ ] `cut`
- [ ] `paste`
- [ ] `tr`
- [ ] `tee`

### Searching and finding information

- [ ] `find`
- [ ] `grep`
- [ ] `grep -i`, `grep -r`, and `grep -n`
- [ ] `locate`
- [ ] `which`
- [ ] `whereis`
- [ ] `command -v`
- [ ] Search logs and configuration files
- [ ] Combine commands to filter results

**Practical tasks**
- [ ] Create a directory structure for cybersecurity projects.
- [ ] Find all `.log` files in a directory.
- [ ] Search a log for failed-login messages.
- [ ] Extract selected columns from a text file.
- [ ] Save command output to a report file.

## Phase 3 — Linux Permissions and Users

- [ ] Linux users and groups
- [ ] Root user and regular users
- [ ] `whoami`
- [ ] `id`
- [ ] `who`
- [ ] `groups`
- [ ] `sudo`
- [ ] `su`
- [ ] `useradd` and `usermod`
- [ ] `passwd`
- [ ] `groupadd`
- [ ] `chmod`
- [ ] `chown`
- [ ] `chgrp`
- [ ] Read, write, and execute permissions
- [ ] Numeric permissions: `644`, `755`, `700`
- [ ] Symbolic permissions: `u`, `g`, `o`, `a`
- [ ] File permissions vs directory permissions
- [ ] `umask`
- [ ] SUID, SGID, and sticky bit
- [ ] Linux ACLs — introduction
- [ ] `/etc/passwd` and `/etc/group`
- [ ] `/etc/shadow` — purpose and access restrictions
- [ ] Least privilege
- [ ] Safe use of `sudo`

**Practical tasks**
- [ ] Create a separate user for lab work.
- [ ] Change file and directory permissions.
- [ ] Configure a shared directory for a group.
- [ ] Diagnose and fix a permission-denied error.
- [ ] Explain why running everything as root is dangerous.

## Phase 4 — Linux Filesystem, Processes, and Services

### Filesystem and storage

- [ ] `/`, `/home`, `/root`, `/tmp`, `/etc`
- [ ] `/var`, `/var/log`, `/usr`, `/opt`
- [ ] `/bin`, `/sbin`, `/dev`, `/proc`, `/sys`
- [ ] `/run`, `/mnt`, `/media`
- [ ] Symbolic links and hard links
- [ ] `ln`
- [ ] `df -h`
- [ ] `du -sh`
- [ ] `lsblk`
- [ ] `mount` and `umount`
- [ ] Disk partitions and filesystems — basics
- [ ] `free -h`

### Processes and system monitoring

- [ ] What is a process?
- [ ] Process IDs and parent process IDs
- [ ] `ps`
- [ ] `top`
- [ ] `htop`
- [ ] `pgrep`
- [ ] `pidof`
- [ ] `kill`
- [ ] `killall` — use carefully
- [ ] Foreground and background jobs
- [ ] `jobs`, `bg`, and `fg`
- [ ] `nohup`
- [ ] `nice` and `renice`
- [ ] CPU, memory, and disk usage

### Services and logs

- [ ] `systemctl`
- [ ] Start, stop, restart, and inspect services
- [ ] Enable and disable services
- [ ] `journalctl`
- [ ] System logs
- [ ] Authentication logs
- [ ] Web server logs
- [ ] `dmesg`
- [ ] `uptime`
- [ ] `uname -a`
- [ ] `hostnamectl`
- [ ] `date`
- [ ] `timedatectl`

**Practical tasks**
- [ ] Identify a running process and its PID.
- [ ] Inspect system logs for errors.
- [ ] Check which services start automatically.
- [ ] Monitor system resource usage.
- [ ] Investigate a service that fails to start.

## Phase 5 — Linux Package Management and Software

- [ ] What are packages and repositories?
- [ ] APT package management on Debian-based distributions
- [ ] `apt update`
- [ ] `apt upgrade`
- [ ] `apt install`
- [ ] `apt remove`
- [ ] `apt purge`
- [ ] `apt search`
- [ ] `apt show`
- [ ] `dpkg -l`
- [ ] `dpkg -L`
- [ ] Package dependencies
- [ ] Repository configuration
- [ ] Software updates and security patches
- [ ] Installing software from trusted sources
- [ ] Verifying downloads and checksums
- [ ] Understanding why random installation scripts can be dangerous
- [ ] Troubleshooting package installation failures
- [ ] Environment variables and `PATH`

**Practical tasks**
- [ ] Install and remove a harmless utility.
- [ ] Find which package provides a command.
- [ ] Update package metadata and inspect available updates.
- [ ] Diagnose a missing-command error.

## Phase 6 — Bash Shell and Scripting

Bash is especially useful for automating repetitive security tasks.

### Shell fundamentals

- [ ] What is a shell?
- [ ] Bash vs other shells
- [ ] Shell prompts and command history
- [ ] Command options and arguments
- [ ] Quoting: single quotes and double quotes
- [ ] Escaping special characters
- [ ] Environment variables
- [ ] `$PATH`, `$HOME`, `$USER`
- [ ] `export`
- [ ] `alias`
- [ ] Command substitution: `$(command)`
- [ ] Exit status: `$?`
- [ ] Standard input, output, and error
- [ ] Redirection: `>`, `>>`, `<`, `2>`, `2>&1`
- [ ] Pipes: `|`
- [ ] `&&`, `||`, and `;`
- [ ] `xargs`
- [ ] `tee`
- [ ] `history`

### Bash scripting

- [ ] Creating and running `.sh` files
- [ ] Shebang: `#!/usr/bin/env bash`
- [ ] Variables
- [ ] Positional parameters: `$1`, `$2`, `$@`, `$#`
- [ ] `read`
- [ ] `if`, `elif`, and `else`
- [ ] `case`
- [ ] `for` loops
- [ ] `while` loops
- [ ] Functions
- [ ] Exit codes and `exit`
- [ ] Tests using `[ ]` and `[[ ]]`
- [ ] File and directory checks
- [ ] String comparisons
- [ ] Arrays
- [ ] `getopts` for script arguments
- [ ] Error handling
- [ ] Logging and timestamps
- [ ] `trap` for cleanup
- [ ] Basic input validation
- [ ] Safe handling of filenames and untrusted input

### Scheduling and automation

- [ ] `cron`
- [ ] `crontab`
- [ ] `at` — where available
- [ ] Scheduled maintenance tasks
- [ ] Basic backup scripts

**Practical projects**
- [ ] Write a script that reports disk and memory usage.
- [ ] Write a script that summarizes selected log entries.
- [ ] Write a script that checks whether a local service is running.
- [ ] Create a backup script for a project directory.
- [ ] Build a command-line tool that accepts arguments and saves a report.

---

# Part 2: Linux Networking for Cybersecurity

## Phase 7 — Networking Fundamentals on Linux

- [ ] IP addresses: IPv4 and IPv6
- [ ] Public vs private IP addresses
- [ ] Loopback address
- [ ] MAC addresses
- [ ] Subnets and CIDR notation
- [ ] Default gateway
- [ ] Routing tables
- [ ] TCP vs UDP
- [ ] Ports and sockets
- [ ] DNS
- [ ] DHCP
- [ ] ARP
- [ ] ICMP
- [ ] HTTP and HTTPS
- [ ] TLS certificates — fundamentals
- [ ] NAT
- [ ] Firewalls
- [ ] Proxies
- [ ] VPNs — fundamentals
- [ ] Client-server architecture
- [ ] OSI and TCP/IP models

### Linux networking commands

- [ ] `ip addr`
- [ ] `ip link`
- [ ] `ip route`
- [ ] `ip neigh`
- [ ] `ping`
- [ ] `traceroute` or `tracepath`
- [ ] `ss`
- [ ] `curl`
- [ ] `wget`
- [ ] `dig`
- [ ] `host`
- [ ] `nslookup`
- [ ] `getent hosts`
- [ ] `resolvectl` — where available
- [ ] `nc` / Netcat
- [ ] `tcpdump`
- [ ] `nftables` — fundamentals
- [ ] `ufw` — on distributions where installed

### Network troubleshooting

- [ ] Diagnose a failed DNS lookup.
- [ ] Check whether a local port is listening.
- [ ] Inspect active network connections.
- [ ] Inspect routing and IP configuration.
- [ ] Use `curl` to inspect an HTTP response.
- [ ] Capture traffic from your own lab interface.
- [ ] Distinguish a DNS problem from a routing or application problem.

**Security connection:** These skills help you understand HTTP traffic, test web applications, investigate services, and interpret what tools such as Burp Suite and Nmap are reporting.

## Phase 8 — SSH, Remote Access, and File Transfer

- [ ] What is SSH?
- [ ] SSH client and server
- [ ] `ssh`
- [ ] `ssh-keygen`
- [ ] Public-key authentication
- [ ] SSH configuration file
- [ ] `scp`
- [ ] `sftp`
- [ ] `rsync` — fundamentals
- [ ] SSH host-key verification
- [ ] Secure permissions for private keys
- [ ] Basic SSH troubleshooting
- [ ] Secure remote administration
- [ ] Avoiding password and private-key exposure

**Practical tasks**
- [ ] Connect to a Linux VM you own.
- [ ] Generate an SSH key pair for lab use.
- [ ] Copy a file between your own VMs.
- [ ] Review SSH configuration and authentication logs.

---

# Part 3: Linux Security and Administration

## Phase 9 — Linux Security Essentials

- [ ] Principle of least privilege
- [ ] User and group security
- [ ] File permissions and sensitive files
- [ ] Secure `sudo` configuration
- [ ] Patch management
- [ ] Service hardening
- [ ] Disable unnecessary services
- [ ] Firewall basics
- [ ] SSH hardening fundamentals
- [ ] Password and authentication policies
- [ ] File integrity monitoring concepts
- [ ] Log collection and monitoring
- [ ] Audit logs
- [ ] Linux capabilities — introduction
- [ ] AppArmor and SELinux — concepts
- [ ] Secrets management
- [ ] Secure backups
- [ ] System recovery
- [ ] Basic incident-response workflow
- [ ] Indicators of compromise
- [ ] Persistence mechanisms — recognition and defensive analysis
- [ ] Privilege escalation concepts and common misconfigurations
- [ ] Security baselines and system hardening checklists

### Important configuration and log locations

- [ ] `/etc/ssh/`
- [ ] `/etc/sudoers` — inspect safely using `visudo` for changes
- [ ] `/etc/hosts`
- [ ] `/etc/resolv.conf` — understand how your system manages it
- [ ] `/etc/passwd`
- [ ] `/etc/shadow` — understand its purpose, not how to expose it
- [ ] `/var/log/`
- [ ] `/etc/systemd/`
- [ ] `/etc/cron.d/`
- [ ] `/etc/crontab`

**Practical tasks**
- [ ] Review the security of your own Linux VM.
- [ ] Identify unnecessary services.
- [ ] Check pending security updates.
- [ ] Review authentication logs.
- [ ] Write a short hardening report with findings and recommendations.

---

# Part 4: Kali Linux Fundamentals

## Phase 10 — Kali Linux Setup and Configuration

- [ ] What is Kali Linux?
- [ ] Kali vs Ubuntu vs Debian
- [ ] Why Kali is designed for penetration testing
- [ ] Kali Linux installation options
- [ ] Kali in VirtualBox or VMware
- [ ] Kali as a live system — overview
- [ ] Kali filesystem and terminal
- [ ] Root vs non-root usage
- [ ] Initial system updates
- [ ] APT repositories and package management
- [ ] Installing and removing tools
- [ ] Creating VM snapshots
- [ ] Shared folders
- [ ] Copy/paste and clipboard settings
- [ ] VM network modes: NAT, bridged, host-only, internal
- [ ] Network isolation for security labs
- [ ] Managing disk space
- [ ] Troubleshooting network connectivity
- [ ] Troubleshooting broken packages
- [ ] Updating Kali safely
- [ ] Saving notes, evidence, and lab reports

**Recommended setup:** Keep Kali in a virtual machine and use a separate vulnerable practice application or lab VM. Use snapshots so you can restore the environment after experiments.

## Phase 11 — Kali Linux Commands and Workflow

- [ ] Refresh all essential Linux terminal commands.
- [ ] Update packages with APT.
- [ ] Find installed tools using `command -v` and `which`.
- [ ] Read installed tool documentation and `--help` output.
- [ ] Use `man` pages.
- [ ] Check a tool's version.
- [ ] Save terminal output to files.
- [ ] Organize projects and evidence by lab.
- [ ] Use `tmux` for persistent terminal sessions.
- [ ] Understand tool dependencies.
- [ ] Verify download sources and checksums.
- [ ] Identify tools that require elevated privileges.
- [ ] Avoid running tools with unnecessary root permissions.
- [ ] Record exact commands, settings, and results in your notes.

Useful commands:

- [ ] `man`
- [ ] `apropos`
- [ ] `help`
- [ ] `type`
- [ ] `command -v`
- [ ] `apt`
- [ ] `dpkg`
- [ ] `tmux`
- [ ] `history`
- [ ] `tee`

---

# Part 5: Kali Tools for Web Application Security

Learn tools according to the work you want to do. You do not need to master every tool available in Kali.

## Phase 12 — Reconnaissance and Service Discovery

- [ ] Understand passive vs active reconnaissance.
- [ ] Define scope and authorization before testing.
- [ ] Understand domains, subdomains, DNS, IP addresses, and ports.
- [ ] `whois` — where available
- [ ] `dig`
- [ ] `host`
- [ ] `curl`
- [ ] `whatweb`
- [ ] `nmap`
- [ ] Nmap host discovery
- [ ] Nmap TCP port scanning
- [ ] Service and version detection
- [ ] Nmap output formats
- [ ] Understanding false positives and scan limitations
- [ ] Record discovered services and exposed attack surface
- [ ] Separate confirmed findings from hypotheses

**Practice:** Scan only your own lab VMs or targets that explicitly authorize scanning.

## Phase 13 — Web Traffic Analysis and Interception

- [ ] HTTP request and response structure
- [ ] HTTP methods and status codes
- [ ] Request headers and response headers
- [ ] Cookies and sessions
- [ ] Authentication and authorization
- [ ] URL encoding and decoding
- [ ] HTML forms and parameters
- [ ] JSON request bodies
- [ ] Redirects
- [ ] TLS and HTTPS fundamentals
- [ ] Browser developer tools
- [ ] Burp Suite Community Edition
- [ ] Burp Proxy
- [ ] Burp HTTP history
- [ ] Burp Repeater
- [ ] Burp Decoder
- [ ] Burp Comparer
- [ ] Burp Inspector
- [ ] Firefox proxy configuration
- [ ] Using a test-only certificate authority in your own lab
- [ ] Exporting evidence safely
- [ ] Reproducing a finding and documenting its impact

**Priority:** Burp Suite is one of the most important tools for your chosen specialization.

## Phase 14 — Web Vulnerability Testing Tools

- [ ] OWASP ZAP fundamentals
- [ ] Burp Suite testing workflow
- [ ] Browser developer tools for debugging
- [ ] `curl` for manual HTTP requests
- [ ] `ffuf` for authorized content discovery
- [ ] `dirsearch` — optional alternative
- [ ] `nikto` — basic web-server checks
- [ ] Nmap HTTP-related scripts — carefully and within scope
- [ ] Python `requests` for simple HTTP automation
- [ ] `jq` for JSON processing
- [ ] `whatweb` for basic technology fingerprinting
- [ ] Understand the limitations of automated scanners
- [ ] Verify scanner findings manually
- [ ] Avoid treating a tool's output as proof without validation

### Vulnerability categories to understand

- [ ] Broken access control
- [ ] IDOR / BOLA
- [ ] SQL injection
- [ ] Cross-site scripting (XSS)
- [ ] Cross-site request forgery (CSRF)
- [ ] Server-side request forgery (SSRF)
- [ ] Path traversal
- [ ] File-upload vulnerabilities
- [ ] Authentication weaknesses
- [ ] Session-management weaknesses
- [ ] Security misconfiguration
- [ ] Insecure deserialization — fundamentals
- [ ] Command injection — fundamentals
- [ ] Business-logic flaws
- [ ] Rate-limiting weaknesses
- [ ] CORS misconfiguration
- [ ] API security issues

Study the vulnerabilities through legal training labs, focusing on how to identify, validate, explain, and remediate them.

## Phase 15 — Network Analysis Tools

- [ ] Wireshark fundamentals
- [ ] `tcpdump`
- [ ] Packet capture filters
- [ ] Wireshark display filters
- [ ] TCP handshake
- [ ] DNS query analysis
- [ ] HTTP traffic analysis
- [ ] TLS handshake — basic interpretation
- [ ] TCP retransmissions and connection failures
- [ ] Identify suspicious or unexpected traffic
- [ ] Save and document packet captures
- [ ] Understand what encrypted traffic does and does not reveal

## Phase 16 — Password Auditing and Authentication Concepts

- [ ] Password storage and hashing concepts
- [ ] Salting and password-hashing algorithms
- [ ] Online vs offline password attacks — conceptual differences
- [ ] Multi-factor authentication
- [ ] Account lockout and rate limiting
- [ ] Password policy evaluation
- [ ] Recognize the purpose of John the Ripper
- [ ] Recognize the purpose of Hashcat
- [ ] Understand safe handling of password hashes
- [ ] Use only lab-provided hashes or explicitly authorized audit data
- [ ] Document defensive recommendations

Do not test passwords against real accounts or services without explicit authorization.

## Phase 17 — Other Kali Tool Categories

Know what these tools are for; prioritize only when they support your learning goals.

- [ ] Metasploit Framework — controlled lab fundamentals
- [ ] Searchsploit — finding public vulnerability references
- [ ] Gobuster — authorized content discovery
- [ ] `ffuf` — authorized web fuzzing
- [ ] SQLMap — understand automated SQL injection testing in labs
- [ ] Netcat — basic networking and troubleshooting
- [ ] Socat — advanced networking utility, optional
- [ ] GVM/OpenVAS — vulnerability assessment concepts
- [ ] Nikto — web-server checks
- [ ] Aircrack-ng — wireless security, optional
- [ ] Hydra — authentication-auditing concepts, optional
- [ ] Impacket — Windows network protocol tooling, optional
- [ ] Responder — network authentication concepts, optional

**Important:** These tools do not all belong to web application security. You can defer wireless, Windows-domain, and broader exploitation tools until your main specialization is established.

---

# Part 6: Python, Bash, and Linux Automation

## Phase 18 — Security Automation

- [ ] Automate repetitive file operations with Bash.
- [ ] Parse logs with `grep`, `awk`, and `sed`.
- [ ] Use Python to parse log files.
- [ ] Use Python `requests` for HTTP requests.
- [ ] Use Python `json` for API responses.
- [ ] Use Python `re` for pattern matching.
- [ ] Use Python `argparse` for command-line interfaces.
- [ ] Use Python `logging` for structured logs.
- [ ] Handle errors and timeouts.
- [ ] Use virtual environments for Python projects.
- [ ] Read environment variables safely.
- [ ] Avoid hardcoding passwords, API keys, or tokens.
- [ ] Save structured results as JSON or CSV.
- [ ] Write unit tests for scripts.
- [ ] Use Git to track changes.
- [ ] Document script limitations and safe usage.

### Suggested projects

- [ ] **Log Analyzer:** Detect repeated failed logins in sample logs.
- [ ] **HTTP Header Checker:** Inspect security headers on a lab application.
- [ ] **TLS Certificate Checker:** Report certificate expiry and basic details.
- [ ] **Service Inventory:** Summarize services on your own test VM.
- [ ] **File Integrity Monitor:** Detect changes in a selected directory.
- [ ] **API Test Client:** Send predefined requests to a local training API.
- [ ] **Lab Report Generator:** Turn validated test results into a Markdown report.

---

# Part 7: Practical Labs and Portfolio

## Phase 19 — Build a Safe Cybersecurity Lab

- [ ] Install Kali Linux in a VM.
- [ ] Install a separate Ubuntu VM.
- [ ] Configure an isolated or host-only lab network.
- [ ] Take snapshots before experiments.
- [ ] Install OWASP Juice Shop locally or use another authorized training environment.
- [ ] Configure Burp Suite or OWASP ZAP for the lab.
- [ ] Learn basic HTTP requests with `curl`.
- [ ] Capture and inspect lab traffic.
- [ ] Practice Linux permissions and service administration.
- [ ] Keep notes of each exercise.
- [ ] Reset the lab between exercises when needed.
- [ ] Ensure intentionally vulnerable services are not exposed to the public internet.

## Phase 20 — Portfolio Projects

Aim to complete at least four well-documented projects.

- [ ] **Project 1: Linux Security Audit**
  - Review users, permissions, services, updates, and logs.
  - Document findings and recommendations.

- [ ] **Project 2: Web Application Testing Report**
  - Test an authorized training application.
  - Document scope, reproduction steps, evidence, severity, and remediation.

- [ ] **Project 3: Python Security Automation**
  - Build a log analyzer or HTTP security-header checker.
  - Include input validation, error handling, tests, and documentation.

- [ ] **Project 4: Secure Web Application**
  - Build a small application using Flask, Django, or FastAPI.
  - Implement authentication, authorization, input validation, secure configuration, and tests.

- [ ] **Project 5: Security Regression Testing**
  - Add automated tests that verify security fixes remain effective.

- [ ] Publish sanitized documentation to GitHub.
- [ ] Never publish credentials, private keys, personal data, or unauthorized target information.

---

# Part 8: Recommended Learning Resources

1. **Linux command line:** [Linux Journey](https://linuxjourney.com/)
2. **Linux manual pages:** [man7.org](https://man7.org/linux/man-pages/)
3. **Bash reference:** [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
4. **Kali Linux documentation:** [Kali Documentation](https://www.kali.org/docs/)
5. **Kali tool documentation:** [Kali Tools](https://www.kali.org/tools/)
6. **Networking fundamentals:** [Cisco Skills for All](https://skillsforall.com/)
7. **Web security labs:** [PortSwigger Web Security Academy](https://portswigger.net/web-security)
8. **OWASP Juice Shop:** [Official Project](https://owasp.org/www-project-juice-shop/)
9. **OWASP testing guide:** [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
10. **Burp Suite documentation:** [PortSwigger Documentation](https://portswigger.net/burp/documentation)
11. **OWASP ZAP:** [Official Documentation](https://www.zaproxy.org/docs/)

---

# Part 9: Suggested 8-Week Study Schedule

| Week | Main focus | Practical outcome |
|---|---|---|
| 1 | Linux installation, terminal, files, and permissions | Navigate Linux comfortably |
| 2 | Users, processes, services, packages, and logs | Administer a Linux VM |
| 3 | Bash, pipes, redirection, and scripting | Build two simple scripts |
| 4 | Networking, DNS, HTTP, SSH, and troubleshooting | Diagnose common network problems |
| 5 | Kali installation, APT, lab networking, and tool workflow | Set up a safe security lab |
| 6 | Nmap basics, Burp Suite, `curl`, and HTTP analysis | Inspect a training application's traffic |
| 7 | OWASP ZAP, web testing tools, and vulnerability validation | Complete guided lab exercises |
| 8 | Python automation, Linux audit, and reporting | Finish a small portfolio project |

Treat these as flexible targets rather than deadlines. If a week feels difficult, repeat it instead of rushing forward.

---

# Part 10: What to Learn First

## Priority 1 — Must know

- [ ] Terminal navigation and file operations
- [ ] Permissions, users, and `sudo`
- [ ] Processes, services, and logs
- [ ] APT and package management
- [ ] Bash, pipes, redirection, and basic scripting
- [ ] IP addresses, DNS, TCP/UDP, and ports
- [ ] `curl`, `ss`, `ip`, `dig`, and `grep`
- [ ] Kali VM setup and safe lab networking
- [ ] Burp Suite Proxy and Repeater
- [ ] Basic Nmap usage within authorized scope

## Priority 2 — Learn alongside web security

- [ ] Python automation
- [ ] Wireshark and `tcpdump`
- [ ] `ffuf` and web content discovery
- [ ] OWASP ZAP
- [ ] Linux hardening and log analysis
- [ ] HTTP, cookies, sessions, and TLS
- [ ] Writing professional security reports

## Priority 3 — Learn later if your work requires it

- [ ] Advanced Bash
- [ ] SELinux and AppArmor administration
- [ ] Advanced routing and firewall rules
- [ ] Advanced packet analysis
- [ ] Wireless security
- [ ] Windows-domain security tools
- [ ] Advanced exploitation frameworks
- [ ] Container and cloud security
- [ ] Advanced Linux internals

---

# Final Goal: When Are You Ready to Move Forward?

You are ready to focus more heavily on web application security when you can:

- [ ] Work comfortably in the Linux terminal without following every command from a tutorial.
- [ ] Understand permissions, processes, services, and system logs.
- [ ] Write a basic Bash script and a useful Python automation script.
- [ ] Explain IP addresses, ports, DNS, TCP, and HTTP.
- [ ] Set up and troubleshoot Kali in a virtual machine.
- [ ] Use Burp Suite to intercept and replay requests to a training application.
- [ ] Use Nmap responsibly against your own lab.
- [ ] Complete guided web security labs and explain the underlying vulnerability.
- [ ] Write a clear report with evidence, impact, and remediation.

**My recommendation:** Spend approximately 2 weeks strengthening Linux fundamentals and Bash, then move into Kali and web security while continuing to practise Linux. You do not need to finish every item in this checklist before starting PortSwigger labs. The aim is to build the skills you will actually use, not to collect commands or tools.
