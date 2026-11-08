Complete Windows Roadmap for Cybersecurity

Target: Cybersecurity, Web Application Security, Application Security, and Penetration Testing
Level: Beginner → Intermediate → Advanced
Suggested duration: 6–8 weeks for core Windows skills
Study time: 30–45 minutes daily alongside Linux, Python, and Networking.

---

Part 1: Windows Fundamentals

Phase 1 — Introduction to Windows

- [ ] What is Windows?
- [ ] History and evolution of Microsoft Windows
- [ ] Windows architecture
- [ ] Windows kernel
- [ ] User mode vs kernel mode
- [ ] Windows operating system components
- [ ] Windows editions: Home, Pro, Enterprise, Education
- [ ] Windows 10 vs Windows 11
- [ ] Windows Server vs Windows Client
- [ ] 32-bit vs 64-bit architecture
- [ ] GUI vs CLI
- [ ] Desktop environment
- [ ] Windows boot process
- [ ] BIOS vs UEFI
- [ ] GPT vs MBR
- [ ] Windows Registry
- [ ] Windows services
- [ ] Windows processes
- [ ] Windows drivers
- [ ] Windows updates
- [ ] Windows recovery environment
- [ ] Windows installation and activation fundamentals

Phase 2 — Windows Installation and Environment

- [ ] Installing Windows in VMware or VirtualBox
- [ ] Creating a Windows virtual machine
- [ ] Windows installation requirements
- [ ] Partitioning and formatting
- [ ] Creating local user accounts
- [ ] Microsoft account vs local account
- [ ] Initial system configuration
- [ ] Windows Update configuration
- [ ] Device Manager
- [ ] Disk Management
- [ ] Task Manager
- [ ] Settings vs Control Panel
- [ ] System Information ("msinfo32")
- [ ] Environment variables
- [ ] System restore points
- [ ] Virtual machine snapshots
- [ ] Shared folders between host and VM

Practical tasks

- [ ] Install Windows 11 in a virtual machine.
- [ ] Create a local standard user.
- [ ] Explore Task Manager and Device Manager.
- [ ] Create a restore point.
- [ ] Take and restore a VM snapshot.

---

Part 2: Windows Filesystem and Command Line

Phase 3 — Windows Filesystem

- [ ] Windows drive structure
- [ ] "C:\" drive
- [ ] System directories
- [ ] User directories
- [ ] Program Files
- [ ] Program Files (x86)
- [ ] Windows directory
- [ ] System32
- [ ] SysWOW64
- [ ] AppData
- [ ] ProgramData
- [ ] Temp directories
- [ ] Hidden files and folders
- [ ] File extensions
- [ ] NTFS filesystem
- [ ] FAT32 and exFAT
- [ ] NTFS permissions
- [ ] File ownership
- [ ] Access Control Lists (ACLs)
- [ ] Alternate Data Streams (ADS)
- [ ] Symbolic links
- [ ] Hard links
- [ ] Junctions
- [ ] File compression
- [ ] EFS — Encrypting File System
- [ ] BitLocker fundamentals
- [ ] Disk quotas
- [ ] File recovery fundamentals

Phase 4 — Command Prompt (CMD)

CMD fundamentals

- [ ] What is Command Prompt?
- [ ] CMD vs PowerShell
- [ ] Running CMD as administrator
- [ ] CMD syntax
- [ ] Command arguments and options
- [ ] Environment variables
- [ ] Command history
- [ ] Help commands

Essential CMD commands

Navigation and file management

- [ ] "dir"
- [ ] "cd"
- [ ] "md" / "mkdir"
- [ ] "rd" / "rmdir"
- [ ] "copy"
- [ ] "xcopy"
- [ ] "robocopy"
- [ ] "move"
- [ ] "ren"
- [ ] "del"
- [ ] "type"
- [ ] "tree"
- [ ] "attrib"

System information

- [ ] "systeminfo"
- [ ] "hostname"
- [ ] "whoami"
- [ ] "ver"
- [ ] "set"
- [ ] "echo"
- [ ] "date"
- [ ] "time"
- [ ] "driverquery"
- [ ] "tasklist"

Process management

- [ ] "tasklist"
- [ ] "taskkill"
- [ ] "start"

Networking

- [ ] "ipconfig"
- [ ] "ping"
- [ ] "tracert"
- [ ] "pathping"
- [ ] "nslookup"
- [ ] "netstat"
- [ ] "arp"
- [ ] "route"
- [ ] "getmac"
- [ ] "hostname"

System administration

- [ ] "sfc"
- [ ] "DISM"
- [ ] "chkdsk"
- [ ] "shutdown"
- [ ] "shutdown /r"
- [ ] "shutdown /s"
- [ ] "sc"
- [ ] "net"
- [ ] "schtasks"
- [ ] "wevtutil"

Practical tasks

- [ ] Create and delete directories using CMD.
- [ ] Display IP configuration.
- [ ] Identify running processes.
- [ ] Check active network connections.
- [ ] Inspect system information.
- [ ] Copy files using "robocopy".

---

Part 3: Windows PowerShell

Phase 5 — PowerShell Fundamentals

- [ ] What is PowerShell?
- [ ] Why PowerShell is important for cybersecurity
- [ ] PowerShell vs CMD
- [ ] PowerShell vs Bash
- [ ] PowerShell architecture
- [ ] PowerShell console
- [ ] PowerShell ISE — legacy overview
- [ ] PowerShell 5.1 vs PowerShell 7+
- [ ] Cmdlets
- [ ] Verbs and nouns
- [ ] PowerShell pipeline
- [ ] Objects vs text
- [ ] PowerShell help system
- [ ] "Get-Help"
- [ ] "Get-Command"
- [ ] "Get-Member"
- [ ] Aliases
- [ ] PowerShell profiles
- [ ] Execution policies and their limitations
- [ ] Running scripts
- [ ] PowerShell modules
- [ ] PowerShell Gallery
- [ ] Administrative privileges

Phase 6 — PowerShell Commands

File and directory management

- [ ] "Get-ChildItem"
- [ ] "Set-Location"
- [ ] "Get-Location"
- [ ] "New-Item"
- [ ] "Remove-Item"
- [ ] "Copy-Item"
- [ ] "Move-Item"
- [ ] "Rename-Item"
- [ ] "Get-Content"
- [ ] "Set-Content"
- [ ] "Add-Content"
- [ ] "Clear-Content"
- [ ] "Test-Path"

System information

- [ ] "Get-ComputerInfo"
- [ ] "Get-CimInstance"
- [ ] "Get-Service"
- [ ] "Get-Process"
- [ ] "Get-EventLog" — legacy
- [ ] "Get-WinEvent"
- [ ] "Get-HotFix"
- [ ] "Get-LocalUser"
- [ ] "Get-LocalGroup"
- [ ] "Get-LocalGroupMember"

Process and service management

- [ ] "Start-Process"
- [ ] "Stop-Process"
- [ ] "Wait-Process"
- [ ] "Start-Service"
- [ ] "Stop-Service"
- [ ] "Restart-Service"
- [ ] "Set-Service"

Networking

- [ ] "Get-NetIPConfiguration"
- [ ] "Get-NetIPAddress"
- [ ] "Get-NetAdapter"
- [ ] "Get-NetRoute"
- [ ] "Get-NetTCPConnection"
- [ ] "Test-NetConnection"
- [ ] "Resolve-DnsName"
- [ ] "Get-NetFirewallProfile"
- [ ] "Get-NetFirewallRule"

Filtering and pipelines

- [ ] "Where-Object"
- [ ] "Select-Object"
- [ ] "Sort-Object"
- [ ] "Group-Object"
- [ ] "Measure-Object"
- [ ] "ForEach-Object"
- [ ] "Format-Table"
- [ ] "Format-List"
- [ ] "Export-Csv"
- [ ] "ConvertTo-Json"
- [ ] "ConvertFrom-Json"
- [ ] "Out-File"
- [ ] "Tee-Object"

Phase 7 — PowerShell Scripting

- [ ] Creating ".ps1" files
- [ ] Variables
- [ ] Data types
- [ ] Strings and numbers
- [ ] Arrays
- [ ] Hashtables
- [ ] Operators
- [ ] Conditional statements
- [ ] "if", "elseif", and "else"
- [ ] "switch"
- [ ] "for" loops
- [ ] "foreach" loops
- [ ] "while" loops
- [ ] Functions
- [ ] Parameters
- [ ] Return values
- [ ] Scope
- [ ] Error handling
- [ ] "try", "catch", and "finally"
- [ ] Exception handling
- [ ] Working with files
- [ ] Working with JSON and CSV
- [ ] Working with APIs
- [ ] Regular expressions
- [ ] Logging
- [ ] Script debugging
- [ ] Scheduled scripts
- [ ] Secure handling of credentials
- [ ] Code signing fundamentals

Practical projects

- [ ] Create a system-information collector.
- [ ] Build a running-process report.
- [ ] Create a Windows event-log analyzer.
- [ ] Write a script to check listening ports.
- [ ] Build a script that checks Windows security settings.
- [ ] Create a simple backup automation script.

---

Part 4: Windows Users, Groups, and Permissions

Phase 8 — Windows Account Management

- [ ] Local accounts
- [ ] Microsoft accounts
- [ ] Domain accounts
- [ ] Standard users
- [ ] Administrator accounts
- [ ] Built-in accounts
- [ ] Guest account
- [ ] Service accounts
- [ ] Local groups
- [ ] User profiles
- [ ] User Account Control (UAC)
- [ ] Windows logon process
- [ ] Authentication vs authorization
- [ ] Password policies
- [ ] Account lockout policies
- [ ] Windows Hello fundamentals
- [ ] Multi-factor authentication
- [ ] Windows Credential Manager

Phase 9 — NTFS Permissions and Access Control

- [ ] What are NTFS permissions?
- [ ] Read
- [ ] Write
- [ ] Modify
- [ ] Read & Execute
- [ ] Full Control
- [ ] Inheritance
- [ ] Explicit vs inherited permissions
- [ ] Permission precedence
- [ ] Access Control Lists
- [ ] Discretionary ACLs (DACLs)
- [ ] System ACLs (SACLs)
- [ ] Security identifiers (SIDs)
- [ ] Ownership
- [ ] Effective permissions
- [ ] Shared-folder permissions
- [ ] NTFS vs share permissions
- [ ] "icacls"
- [ ] "takeown"
- [ ] Least privilege
- [ ] Common permission misconfigurations

Practical tasks

- [ ] Create two local users.
- [ ] Create a shared directory.
- [ ] Configure different permissions.
- [ ] Inspect permissions using "icacls".
- [ ] Test access using each account.

---

Part 5: Windows Processes, Services, and Registry

Phase 10 — Windows Processes and Services

- [ ] What is a process?
- [ ] Process IDs (PID)
- [ ] Parent and child processes
- [ ] Threads
- [ ] Handles
- [ ] Windows process lifecycle
- [ ] Task Manager
- [ ] Resource Monitor
- [ ] Process Explorer — Sysinternals
- [ ] Process Monitor — Sysinternals
- [ ] "tasklist"
- [ ] "taskkill"
- [ ] "Get-Process"
- [ ] Windows services
- [ ] Service Control Manager
- [ ] Automatic, manual, and disabled startup types
- [ ] Service accounts
- [ ] Service dependencies
- [ ] "services.msc"
- [ ] "sc.exe"
- [ ] "Get-Service"
- [ ] Service security and permissions
- [ ] Service misconfiguration concepts

Phase 11 — Windows Registry

- [ ] What is the Windows Registry?
- [ ] Registry structure
- [ ] Registry hives
- [ ] "HKEY_LOCAL_MACHINE"
- [ ] "HKEY_CURRENT_USER"
- [ ] "HKEY_CLASSES_ROOT"
- [ ] "HKEY_USERS"
- [ ] "HKEY_CURRENT_CONFIG"
- [ ] Registry keys
- [ ] Registry values
- [ ] Registry data types
- [ ] "regedit"
- [ ] "reg.exe"
- [ ] Registry permissions
- [ ] Registry backups
- [ ] Registry recovery
- [ ] Startup-related registry locations
- [ ] Application configuration
- [ ] Registry auditing
- [ ] Common registry security risks
- [ ] Registry persistence concepts and detection

Important: Always back up registry settings before making changes. Incorrect edits can make Windows unstable.

---

Part 6: Windows Networking

Phase 12 — Windows Networking Fundamentals

- [ ] Windows network interfaces
- [ ] Ethernet and Wi-Fi configuration
- [ ] IPv4 and IPv6
- [ ] DHCP
- [ ] DNS
- [ ] Default gateway
- [ ] Subnet masks
- [ ] MAC addresses
- [ ] ARP
- [ ] Routing tables
- [ ] TCP and UDP
- [ ] Ports and sockets
- [ ] Loopback address
- [ ] Private and public IP addresses
- [ ] NAT
- [ ] Proxy configuration
- [ ] VPN configuration
- [ ] Network discovery
- [ ] Network profiles: Public, Private, Domain
- [ ] Network sharing
- [ ] Windows network troubleshooting

Phase 13 — Windows Networking Commands

- [ ] "ipconfig"
- [ ] "ipconfig /all"
- [ ] "ipconfig /release"
- [ ] "ipconfig /renew"
- [ ] "ipconfig /flushdns"
- [ ] "ping"
- [ ] "tracert"
- [ ] "pathping"
- [ ] "nslookup"
- [ ] "netstat"
- [ ] "arp"
- [ ] "route print"
- [ ] "getmac"
- [ ] "hostname"
- [ ] "netsh"
- [ ] "Test-NetConnection"
- [ ] "Resolve-DnsName"
- [ ] "Get-NetTCPConnection"

Phase 14 — Windows Firewall

- [ ] What is Windows Defender Firewall?
- [ ] Inbound rules
- [ ] Outbound rules
- [ ] Connection security rules
- [ ] Firewall profiles
- [ ] Domain profile
- [ ] Private profile
- [ ] Public profile
- [ ] Allowing and blocking applications
- [ ] Port-based rules
- [ ] Firewall logging
- [ ] Windows Defender Firewall with Advanced Security
- [ ] "wf.msc"
- [ ] PowerShell firewall management
- [ ] Common firewall misconfigurations
- [ ] Firewall troubleshooting

Practical tasks

- [ ] Inspect your IP configuration.
- [ ] Check listening ports.
- [ ] Investigate a DNS resolution problem.
- [ ] Create a firewall rule for a test application.
- [ ] Inspect firewall logs.

---

Part 7: Windows Security

Phase 15 — Windows Defender and Endpoint Security

- [ ] Microsoft Defender Antivirus
- [ ] Real-time protection
- [ ] Cloud-delivered protection
- [ ] Security intelligence updates
- [ ] Quick scans and full scans
- [ ] Custom scans
- [ ] Microsoft Defender Firewall
- [ ] Windows Security application
- [ ] SmartScreen
- [ ] Controlled folder access
- [ ] Tamper Protection
- [ ] Windows Security Center
- [ ] Potentially unwanted applications
- [ ] Endpoint Detection and Response (EDR) fundamentals
- [ ] Attack Surface Reduction (ASR) rules
- [ ] Exploit protection
- [ ] Application control fundamentals
- [ ] Device security
- [ ] Secure Boot
- [ ] TPM fundamentals
- [ ] Credential Guard overview
- [ ] Windows Sandbox
- [ ] Microsoft Defender for Endpoint — overview

Phase 16 — Windows Authentication and Security Architecture

- [ ] Windows authentication architecture
- [ ] Security Accounts Manager (SAM)
- [ ] Local Security Authority Subsystem Service (LSASS)
- [ ] Local Security Authority (LSA)
- [ ] Security Reference Monitor
- [ ] Access tokens
- [ ] Security identifiers (SIDs)
- [ ] Security principals
- [ ] Logon sessions
- [ ] NTLM authentication
- [ ] Kerberos authentication
- [ ] Windows Hello
- [ ] Credential storage concepts
- [ ] Windows Credential Manager
- [ ] Data Protection API (DPAPI) — overview
- [ ] Windows authentication protocols
- [ ] Authentication weaknesses and defenses
- [ ] Secure credential handling

Phase 17 — Windows Event Logs and Auditing

- [ ] What are Windows Event Logs?
- [ ] Event Viewer
- [ ] Application logs
- [ ] Security logs
- [ ] System logs
- [ ] Setup logs
- [ ] Forwarded Events
- [ ] Windows event channels
- [ ] Event IDs
- [ ] Audit policies
- [ ] Logon and logoff events
- [ ] Account management events
- [ ] Process creation auditing
- [ ] PowerShell logging
- [ ] Windows Defender logs
- [ ] Firewall logs
- [ ] Sysmon
- [ ] Sysmon configuration fundamentals
- [ ] "wevtutil"
- [ ] "Get-WinEvent"
- [ ] Event correlation
- [ ] Log retention
- [ ] Centralized event collection
- [ ] Security monitoring

Important Windows Event IDs to recognize

Event ID| Description
4624| Successful logon
4625| Failed logon
4634| Account logged off
4648| Logon using explicit credentials
4672| Special privileges assigned to a new logon
4688| Process creation
4697| Service installed
4720| User account created
4722| User account enabled
4725| User account disabled
4726| User account deleted
4732| Member added to a security-enabled local group
4740| User account locked out
1102| Security audit log cleared

Event availability depends on the audit policy and Windows configuration. Learn to investigate events in context rather than relying on a single event ID.

---

Part 8: Windows System Administration

Phase 18 — Windows Administration

- [ ] Local users and groups
- [ ] Computer Management
- [ ] Local Security Policy
- [ ] Group Policy fundamentals
- [ ] Local Group Policy Editor
- [ ] "gpedit.msc"
- [ ] "gpupdate"
- [ ] "gpresult"
- [ ] Windows Update
- [ ] Windows services
- [ ] Scheduled Tasks
- [ ] Task Scheduler
- [ ] Startup applications
- [ ] Windows backup and recovery
- [ ] System Restore
- [ ] Disk Management
- [ ] Storage Spaces — overview
- [ ] Remote Desktop
- [ ] Remote Assistance — overview
- [ ] Windows activation and licensing basics
- [ ] Troubleshooting startup problems
- [ ] Safe Mode
- [ ] Recovery Environment

Phase 19 — Windows Task Scheduler and Startup

- [ ] What is Task Scheduler?
- [ ] Scheduled tasks
- [ ] Task triggers
- [ ] Task actions
- [ ] Task conditions
- [ ] Startup tasks
- [ ] Logon tasks
- [ ] Scheduled task permissions
- [ ] "schtasks"
- [ ] PowerShell scheduled tasks
- [ ] Startup folder
- [ ] Startup registry locations
- [ ] Autoruns — Sysinternals
- [ ] Detecting suspicious startup entries
- [ ] Reviewing task execution history

---

Part 9: Windows Server and Active Directory

This section is particularly valuable if you later explore enterprise penetration testing or SOC work.

Phase 20 — Windows Server Fundamentals

- [ ] What is Windows Server?
- [ ] Windows Server editions
- [ ] Windows Server installation
- [ ] Server Manager
- [ ] Server roles and features
- [ ] Server Core vs Desktop Experience
- [ ] Remote Server Administration Tools (RSAT)
- [ ] Server services
- [ ] File and storage services
- [ ] DNS Server role
- [ ] DHCP Server role
- [ ] Web Server (IIS)
- [ ] Remote Desktop Services — overview
- [ ] Server hardening
- [ ] Server updates and patching

Phase 21 — Active Directory Fundamentals

- [ ] What is Active Directory?
- [ ] Why organizations use Active Directory
- [ ] Domain vs workgroup
- [ ] Active Directory Domain Services (AD DS)
- [ ] Domain controllers
- [ ] Domains
- [ ] Trees
- [ ] Forests
- [ ] Organizational Units (OUs)
- [ ] Users and groups
- [ ] Security groups vs distribution groups
- [ ] Group nesting
- [ ] Group Policy Objects (GPOs)
- [ ] Group Policy processing
- [ ] LDAP
- [ ] Kerberos
- [ ] NTLM
- [ ] DNS in Active Directory
- [ ] SYSVOL
- [ ] FSMO roles
- [ ] Replication
- [ ] Trust relationships
- [ ] Domain authentication
- [ ] Active Directory permissions
- [ ] Delegation of administration
- [ ] Service accounts
- [ ] Group Managed Service Accounts (gMSAs)
- [ ] Active Directory security best practices

Phase 22 — Active Directory Security

- [ ] Active Directory attack surface
- [ ] Kerberos security fundamentals
- [ ] NTLM security fundamentals
- [ ] Password policy weaknesses
- [ ] Excessive privileges
- [ ] Misconfigured group memberships
- [ ] Unsecured service accounts
- [ ] Delegation risks
- [ ] Group Policy security
- [ ] LDAP security
- [ ] Domain controller hardening
- [ ] Privileged account protection
- [ ] Lateral movement concepts
- [ ] Credential exposure risks
- [ ] BloodHound — understanding AD relationship graphs
- [ ] Purple-team and defensive validation
- [ ] Active Directory monitoring
- [ ] Security assessment reporting

Practice these topics only in an isolated Active Directory lab that you control or are authorized to assess.

---

Part 10: Windows Vulnerability and Attack Concepts

Phase 23 — Common Windows Security Weaknesses

- [ ] Weak passwords
- [ ] Excessive user privileges
- [ ] Misconfigured file permissions
- [ ] Misconfigured services
- [ ] Unpatched software
- [ ] Insecure registry permissions
- [ ] Unprotected credentials
- [ ] Insecure scheduled tasks
- [ ] Weak firewall configuration
- [ ] Exposed remote administration
- [ ] DLL search-order hijacking — concept
- [ ] Unquoted service paths — concept
- [ ] Insecure service permissions
- [ ] UAC misconfiguration
- [ ] Application allowlisting weaknesses
- [ ] Insecure PowerShell configuration
- [ ] Insecure remote access
- [ ] Windows privilege escalation concepts
- [ ] Common persistence mechanisms and their detection
- [ ] Vulnerability assessment fundamentals

Phase 24 — Windows Attack Techniques: Understand and Detect

- [ ] Phishing and malicious attachments
- [ ] Malware execution
- [ ] Credential theft concepts
- [ ] Password spraying concepts
- [ ] Pass-the-Hash — concept
- [ ] Pass-the-Ticket — concept
- [ ] Kerberoasting — concept
- [ ] AS-REP roasting — concept
- [ ] NTLM relay — concept
- [ ] Lateral movement
- [ ] Remote service abuse
- [ ] Scheduled-task persistence
- [ ] Registry persistence
- [ ] PowerShell abuse
- [ ] Living-off-the-land binaries (LOLBins)
- [ ] Defense evasion concepts
- [ ] Detection and prevention strategies
- [ ] Incident response

Focus on understanding the underlying weaknesses, their impact, and how defenders detect and prevent them.

---

Part 11: Windows Forensics and Malware Analysis

Phase 25 — Digital Forensics Fundamentals

- [ ] What is digital forensics?
- [ ] Evidence preservation
- [ ] Chain of custody
- [ ] Volatile vs non-volatile evidence
- [ ] File metadata
- [ ] File hashes
- [ ] Timeline analysis
- [ ] Windows event-log investigation
- [ ] Browser artifacts
- [ ] Prefetch files
- [ ] Windows Registry artifacts
- [ ] Scheduled-task artifacts
- [ ] Startup artifacts
- [ ] USB device history
- [ ] Recycle Bin artifacts
- [ ] NTFS metadata
- [ ] Memory forensics — introduction
- [ ] Disk imaging
- [ ] Forensic reporting

Phase 26 — Malware Analysis Fundamentals

- [ ] What is malware?
- [ ] Malware categories
- [ ] Static analysis
- [ ] Dynamic analysis
- [ ] Hash identification
- [ ] File signatures
- [ ] Strings analysis
- [ ] PE file format fundamentals
- [ ] Windows executable structure
- [ ] DLLs
- [ ] Imports and exports
- [ ] Process behavior
- [ ] Network behavior
- [ ] Sandbox fundamentals
- [ ] 
