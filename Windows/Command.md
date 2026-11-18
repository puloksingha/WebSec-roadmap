Complete Windows Commands for Cybersecurity

1. Basic CMD Commands

Command| Purpose
"help"| Display available commands
"cls"| Clear terminal
"echo Hello"| Print text
"ver"| Display Windows version
"date"| Display or change date
"time"| Display or change time
"hostname"| Display computer name
"whoami"| Display current username
"whoami /all"| Show user privileges and groups
"whoami /priv"| Display user privileges
"systeminfo"| Display system information
"set"| Display environment variables
"path"| Display executable search path
"echo %USERNAME%"| Display username
"echo %USERPROFILE%"| Display user profile path
"echo %PATH%"| Display PATH variable
"exit"| Close terminal

2. Directory Management

Command| Purpose
"dir"| List files and folders
"dir /a"| Show hidden and system files
"dir /s"| List files recursively
"dir /b"| Display bare file listing
"cd"| Display current directory
"cd .."| Move one directory up
"cd \"| Go to drive root
"cd /d D:\Projects"| Change drive and directory
"mkdir test"| Create directory
"md test"| Create directory
"rmdir test"| Remove empty directory
"rmdir /s folder"| Remove directory recursively
"tree"| Display directory structure
"tree /f"| Display files and folders
"pushd C:\Temp"| Save location and change directory
"popd"| Return to previous location

3. File Management

Command| Purpose
"type file.txt"| Display file content
"copy a.txt b.txt"| Copy file
"xcopy folder backup /E"| Copy directory structure
"robocopy source destination /E"| Robust directory copying
"move a.txt D:\"| Move file
"ren old.txt new.txt"| Rename file
"del file.txt"| Delete file
"erase file.txt"| Delete file
"attrib file.txt"| Display file attributes
"attrib +h file.txt"| Set hidden attribute
"attrib -h file.txt"| Remove hidden attribute
"attrib +r file.txt"| Set read-only attribute
"fc file1.txt file2.txt"| Compare files
"find "error" file.txt"| Search for text
"findstr "error" file.txt"| Search text patterns
"more file.txt"| Display content page by page
"where python"| Find executable location

Be careful with "del", "rmdir /s", and "robocopy /MIR". They can permanently delete data.

4. Disk and Storage Management

Command| Purpose
"diskpart"| Open disk management utility
"list disk"| List disks inside DiskPart
"list volume"| List volumes inside DiskPart
"select disk 0"| Select a disk
"detail disk"| Show disk information
"exit"| Exit DiskPart
"chkdsk C:"| Check disk
"chkdsk C: /f"| Fix filesystem errors
"chkdsk C: /r"| Locate bad sectors and recover readable data
"format"| Format a volume
"vol C:"| Display volume label and serial number
"fsutil fsinfo drives"| List available drives
"mountvol"| Manage volume mount points
"manage-bde -status"| Check BitLocker status
"defrag C: /A"| Analyze a drive

Do not experiment with disk formatting or partition deletion on your primary Windows installation.

5. User and Account Management

Command| Purpose
"whoami"| Current user
"net user"| List local users
"net user username"| Display account information
"net user username *"| Change account password interactively
"net user username /add"| Create local account
"net user username /delete"| Delete account
"net localgroup"| List local groups
"net localgroup administrators"| List local administrators
"net localgroup administrators username /add"| Add user to administrators
"net localgroup administrators username /delete"| Remove user from administrators
"query user"| Show logged-in sessions
"quser"| Display user sessions
"logoff"| Sign out of current session

6. Process Management

Command| Purpose
"tasklist"| List running processes
"tasklist /v"| Detailed process information
"tasklist /svc"| Show services associated with processes
"tasklist /fi "STATUS eq RUNNING""| Filter running processes
"taskkill /PID 1234"| Terminate process
"taskkill /PID 1234 /F"| Force terminate process
"taskkill /IM notepad.exe"| Terminate process by name
"start notepad"| Start application
"start /B program.exe"| Start process without opening a new window
"wmic process list brief"| List processes (legacy; may be unavailable)

7. Networking Commands

Command| Purpose
"ipconfig"| Display IP configuration
"ipconfig /all"| Detailed network configuration
"ipconfig /release"| Release DHCP IPv4 address
"ipconfig /renew"| Request DHCP address
"ipconfig /flushdns"| Clear DNS cache
"ipconfig /displaydns"| Display DNS cache
"ping google.com"| Test connectivity
"ping -t google.com"| Continuous ping
"tracert google.com"| Trace network route
"pathping google.com"| Network route and packet-loss analysis
"nslookup example.com"| DNS lookup
"netstat -ano"| Show connections and process IDs
"netstat -abno"| Show connections and executable names (requires elevation)
"arp -a"| Display ARP cache
"route print"| Display routing table
"getmac /v"| Display MAC addresses
"hostname"| Display computer name
"netsh interface show interface"| List network interfaces
"netsh wlan show interfaces"| Display Wi-Fi interface information
"netsh wlan show profiles"| List saved Wi-Fi profiles
"netsh advfirewall show allprofiles"| Display firewall profile status
"curl -I https://example.com"| Inspect HTTP headers
"curl -v https://example.com"| Verbose HTTP request
"nslookup -type=MX example.com"| Query MX records

8. Windows Firewall

Command| Purpose
"netsh advfirewall show allprofiles"| Show firewall status
"netsh advfirewall set allprofiles state on"| Enable firewall
"netsh advfirewall set allprofiles state off"| Disable firewall
"netsh advfirewall firewall show rule name=all"| List firewall rules
"netsh advfirewall firewall add rule name="Test" dir=in action=allow protocol=TCP localport=8080"| Create inbound rule
"netsh advfirewall firewall delete rule name="Test""| Delete firewall rule

Avoid disabling the firewall on your everyday machine. Practice rule changes in a test VM.

9. Windows Services

Command| Purpose
"sc query"| List service information
"sc query state= all"| List all service states
"sc query wuauserv"| Check Windows Update service
"sc start servicename"| Start service
"sc stop servicename"| Stop service
"sc qc servicename"| Show service configuration
"net start"| List running services
"net start servicename"| Start service
"net stop servicename"| Stop service
"services.msc"| Open Services management console

10. System Administration

Command| Purpose
"sfc /scannow"| Scan and repair protected system files
"DISM /Online /Cleanup-Image /CheckHealth"| Check component store health
"DISM /Online /Cleanup-Image /ScanHealth"| Scan component store
"DISM /Online /Cleanup-Image /RestoreHealth"| Repair Windows image
"shutdown /s"| Shut down
"shutdown /r"| Restart
"shutdown /l"| Log off
"shutdown /a"| Abort pending shutdown
"shutdown /s /t 60"| Shut down after 60 seconds
"systeminfo"| System details
"driverquery"| List installed drivers
"driverquery /v"| Detailed driver information
"powercfg /batteryreport"| Generate battery report
"powercfg /energy"| Analyze energy efficiency
"msinfo32"| Open System Information
"dxdiag"| DirectX diagnostic information

11. Windows Event Logs

Command| Purpose
"eventvwr.msc"| Open Event Viewer
"wevtutil el"| List event logs
"wevtutil gli System"| Show System log information
"wevtutil qe System /c:10 /rd:true /f:text"| Display latest 10 System events
"wevtutil qe Security /c:10 /rd:true /f:text"| Display latest 10 Security events
"wevtutil epl System system.evtx"| Export System log
"wevtutil epl Security security.evtx"| Export Security log

Useful Windows Security Event IDs:

Event ID| Meaning
4624| Successful logon
4625| Failed logon
4634| Logoff
4648| Logon using explicit credentials
4672| Special privileges assigned
4688| Process creation (if auditing is enabled)
4720| User account created
4726| User account deleted
4732| Member added to security-enabled local group
1102| Security audit log cleared

12. Windows Registry

Command| Purpose
"reg query HKLM"| Query registry
"reg query HKCU"| Query current user registry
"reg query "HKLM\SOFTWARE""| Query software registry
"reg add"| Add registry key or value
"reg delete"| Delete registry key or value
"reg export HKCU backup.reg"| Export registry key
"reg import backup.reg"| Import registry file
"regedit"| Open Registry Editor

Be careful when modifying the registry. Back it up before making changes.

13. Windows Security and Defender

Command| Purpose
"sc query WinDefend"| Check Defender service
"Get-MpComputerStatus"| Check Defender status (PowerShell)
"Get-MpThreat"| List detected threats
"Get-MpThreatDetection"| View threat detections
"Start-MpScan -ScanType QuickScan"| Run quick scan
"Start-MpScan -ScanType FullScan"| Run full scan
"Get-MpPreference"| Display Defender preferences
"Get-NetFirewallProfile"| Display firewall profiles
"Get-LocalUser"| List local accounts (PowerShell)
"Get-LocalGroup"| List local groups (PowerShell)

Some Defender commands require administrator privileges and the Defender module.

14. PowerShell Fundamentals

Command| Purpose
"Get-Help"| Display help
"Get-Command"| List available commands
"Get-Command Get-Process"| Find a command
"Get-Location"| Current directory
"Set-Location C:\"| Change directory
"Get-ChildItem"| List files
"Get-ChildItem -Force"| Include hidden items
"New-Item file.txt -ItemType File"| Create file
"New-Item folder -ItemType Directory"| Create directory
"Get-Content file.txt"| Read file
"Set-Content file.txt "Hello""| Write or replace content
"Add-Content file.txt "Hello""| Append content
"Copy-Item a.txt b.txt"| Copy file
"Move-Item a.txt folder"| Move file
"Rename-Item old.txt new.txt"| Rename file
"Remove-Item file.txt"| Delete file
"Clear-Host"| Clear terminal
"Write-Output "Hello""| Print output
"Get-History"| Show command history
"Get-Alias"| List aliases

15. PowerShell Process Management

Command| Purpose
"Get-Process"| List processes
"Get-Process notepad"| Find a process
"Start-Process notepad"| Start application
"Stop-Process -Name notepad"| Stop process
"Stop-Process -Id 1234"| Stop by PID
"Wait-Process -Name notepad"| Wait for process
"Get-Service"| List services
"Get-Service -Name wuauserv"| Check service
"Start-Service wuauserv"| Start service
"Stop-Service wuauserv"| Stop service
"Restart-Service wuauserv"| Restart service

16. PowerShell Networking

Command| Purpose
"Get-NetIPConfiguration"| Show IP configuration
"Get-NetIPAddress"| Show IP addresses
"Get-NetAdapter"| List network adapters
"Get-NetRoute"| Display routes
"Get-NetTCPConnection"| Show TCP connections
"Get-DnsClientCache"| Display DNS cache
"Clear-DnsClientCache"| Clear DNS cache
"Resolve-DnsName example.com"| DNS lookup
"Test-Connection example.com"| Test connectivity
"Test-NetConnection example.com -Port 443"| Test TCP port
"Get-NetFirewallProfile"| Check firewall profiles
"Get-NetFirewallRule"| List firewall rules
"Get-NetNeighbor"| Display neighbor cache

17. PowerShell Security and System Inspection

Command| Purpose
"Get-ComputerInfo"| System information
"Get-CimInstance Win32_OperatingSystem"| OS details
"Get-CimInstance Win32_Process"| Process information
"Get-CimInstance Win32_Service"| Service information
"Get-LocalUser"| Local accounts
"Get-LocalGroup"| Local groups
"Get-LocalGroupMember Administrators"| Administrators group members
"Get-FileHash file.txt -Algorithm SHA256"| Calculate file hash
"Get-AuthenticodeSignature file.exe"| Inspect file signature
"Get-ExecutionPolicy -List"| Display execution policies
"Get-WinEvent -LogName System -MaxEvents 20"| Read recent System events
"Get-ScheduledTask"| List scheduled tasks
"Get-SmbShare"| List SMB shares
"Get-Volume"| Show storage volumes

18. PowerShell Text Processing

Command| Purpose
"Select-String "error" file.txt"| Search file content
"Where-Object"| Filter objects
"ForEach-Object"| Process objects
"Sort-Object"| Sort results
"Group-Object"| Group results
"Measure-Object"| Count or measure data
"Select-Object -First 10"| Select first 10 objects
"Format-Table"| Display table
"Format-List"| Display list
"Export-Csv output.csv"| Export CSV
"ConvertTo-Json"| Convert to JSON
"ConvertFrom-Json"| Parse JSON

19. Windows Troubleshooting Tools

Command| Purpose
"devmgmt.msc"| Device Manager
"diskmgmt.msc"| Disk Management
"taskmgr"| Task Manager
"resmon"| Resource Monitor
"perfmon"| Performance Monitor
"services.msc"| Services
"eventvwr.msc"| Event Viewer
"compmgmt.msc"| Computer Management
"gpedit.msc"| Local Group Policy Editor (edition dependent)
"secpol.msc"| Local Security Policy (edition dependent)
"wf.msc"| Windows Defender Firewall
"control"| Control Panel
"regedit"| Registry Editor
"msconfig"| System Configuration

20. Useful Windows Keyboard Shortcuts

Shortcut| Purpose
"Win + R"| Open Run
"Win + X"| Open Quick Link menu
"Win + E"| Open File Explorer
"Win + I"| Open Settings
"Win + L"| Lock computer
"Ctrl + Shift + Esc"| Open Task Manager
"Win + R", then "cmd"| Open CMD
"Win + R", then "powershell"| Open PowerShell
"Win + R", then "msinfo32"| Open System Information
"Win + R", then "eventvwr.msc"| Open Event Viewer

21. Cybersecurity Practical Exercises

- [ ] Find your Windows username using "whoami".
- [ ] Inspect your Windows version using "systeminfo".
- [ ] Find your IP address using "ipconfig /all".
- [ ] Inspect DNS cache using "ipconfig /displaydns".
- [ ] Inspect active network connections using "netstat -ano".
- [ ] Identify the process using a particular PID.
- [ ] List local users using "net user".
- [ ] Inspect administrator group members.
- [ ] Inspect Windows firewall status.
- [ ] Read failed login events (4625).
- [ ] Generate a SHA-256 hash using PowerShell.
- [ ] Inspect a file's digital signature.
- [ ] List running services.
- [ ] Inspect scheduled tasks.
- [ ] Run a Windows Defender quick scan.
- [ ] Create a PowerShell script that collects system information.

22. Suggested Learning Order

1. CMD fundamentals
2. File and directory management
3. User and group management
4. Process management
5. Networking commands
6. Windows services
7. PowerShell fundamentals
8. PowerShell automation
9. Windows Firewall and Defender
10. Event logs and monitoring
11. Windows internals and authentication
12. Practical security investigations

Goal: Become comfortable administering Windows through CMD and PowerShell, investigating system activity, and understanding how Windows security works.
