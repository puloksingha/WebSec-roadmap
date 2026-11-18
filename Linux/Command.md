# Complete Linux & Kali Linux Command Reference

## 1. Basic Linux Commands

| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls` | List files and directories |
| `ls -l` | Detailed listing |
| `ls -a` | Show hidden files |
| `ls -lah` | Human-readable detailed listing |
| `clear` | Clear terminal |
| `whoami` | Show current username |
| `id` | Show user and group IDs |
| `hostname` | Show computer hostname |
| `uname -a` | Show kernel/system information |
| `date` | Display date and time |
| `cal` | Display calendar |
| `history` | Show command history |
| `man ls` | Open command manual |
| `command --help` | Show command help |
| `whatis ls` | Brief command description |
| `which python3` | Find executable path |
| `whereis python3` | Find binary and manual locations |
| `type cd` | Identify command type |
| `echo "Hello"` | Print text |
| `printf "Hello\n"` | Formatted output |

## 2. Directory Management

| Command | Purpose |
|---|---|
| `mkdir test` | Create directory |
| `mkdir -p a/b/c` | Create nested directories |
| `rmdir test` | Remove empty directory |
| `cd /home` | Change directory |
| `cd ..` | Move one directory up |
| `cd ~` | Go to home directory |
| `cd -` | Return to previous directory |
| `tree` | Display directory tree |
| `tree -L 2` | Limit tree depth |
| `pushd /tmp` | Save directory and change |
| `popd` | Return to saved directory |

## 3. File Management

| Command | Purpose |
|---|---|
| `touch file.txt` | Create empty file |
| `cat file.txt` | Display file content |
| `less file.txt` | Read file page by page |
| `more file.txt` | Read file page by page |
| `head file.txt` | Show first 10 lines |
| `head -n 20 file.txt` | Show first 20 lines |
| `tail file.txt` | Show last 10 lines |
| `tail -f log.txt` | Follow live log updates |
| `cp a.txt b.txt` | Copy file |
| `cp -r folder1 folder2` | Copy directory |
| `mv old.txt new.txt` | Move or rename file |
| `rm file.txt` | Delete file |
| `rm -r folder` | Delete directory recursively |
| `file sample.bin` | Identify file type |
| `stat file.txt` | Show file metadata |
| `du -sh folder/` | Show directory size |
| `df -h` | Show disk space |
| `ln -s target link` | Create symbolic link |
| `shred -u file.txt` | Attempt secure file overwrite and removal |

Be careful with `rm -r`, especially when using `sudo`. Check the path before deleting anything.

## 4. Search Commands

| Command | Purpose |
|---|---|
| `find /home -name file.txt` | Find file by name |
| `find . -type f` | Find files |
| `find . -type d` | Find directories |
| `find . -name "*.py"` | Find Python files |
| `find . -size +100M` | Find files larger than 100 MB |
| `locate file.txt` | Search indexed file database |
| `updatedb` | Update locate database |
| `grep "error" file.txt` | Search text |
| `grep -i "error" file.txt` | Case-insensitive search |
| `grep -r "password" .` | Search recursively |
| `grep -n "error" file.txt` | Show matching line numbers |
| `grep -v "success" file.txt` | Exclude matching lines |
| `grep -E "error|warning" log.txt` | Extended regular expressions |
| `rg "pattern"` | Fast recursive text search (ripgrep) |

## 5. File Permissions and Ownership

| Command | Purpose |
|---|---|
| `ls -l` | View permissions |
| `chmod 755 file.sh` | Set permissions |
| `chmod 644 file.txt` | Set file permissions |
| `chmod +x script.sh` | Make executable |
| `chmod -R 755 folder` | Change permissions recursively |
| `chown user file.txt` | Change owner |
| `chown user:group file.txt` | Change owner and group |
| `chgrp group file.txt` | Change group |
| `umask` | Display default permission mask |
| `sudo command` | Run command with elevated privileges |
| `su - username` | Switch user |
| `sudo -l` | List permitted sudo commands |
| `getfacl file.txt` | View ACL permissions |
| `setfacl -m u:user:r file.txt` | Add an ACL permission |

Understand the permission values:

- `r` = Read (4)
- `w` = Write (2)
- `x` = Execute (1)

Examples:
- `755` = Owner: rwx, Group: r-x, Others: r-x
- `644` = Owner: rw-, Group: r--, Others: r--

## 6. Users and Groups

| Command | Purpose |
|---|---|
| `who` | Show logged-in users |
| `w` | Show logged-in users and activity |
| `users` | Display logged-in usernames |
| `id username` | Show user identity |
| `groups username` | Show user's groups |
| `getent passwd` | List account records |
| `getent group` | List groups |
| `sudo adduser username` | Create user interactively |
| `sudo useradd username` | Create user |
| `sudo passwd username` | Set password |
| `sudo userdel username` | Delete user |
| `sudo usermod -aG group username` | Add user to group |
| `sudo groupadd groupname` | Create group |
| `sudo groupdel groupname` | Delete group |
| `sudo usermod -s /bin/bash username` | Change login shell |

## 7. Process Management

| Command | Purpose |
|---|---|
| `ps` | Show processes |
| `ps aux` | Show all processes |
| `ps -ef` | Full process listing |
| `top` | Live process monitoring |
| `htop` | Interactive process monitor |
| `pgrep firefox` | Find process ID |
| `pidof firefox` | Find process ID by program |
| `kill PID` | Send termination signal |
| `kill -9 PID` | Forcefully terminate process |
| `pkill firefox` | Terminate matching processes |
| `jobs` | List shell background jobs |
| `bg` | Resume job in background |
| `fg` | Bring job to foreground |
| `nohup command &` | Run command immune to hangup |
| `nice -n 10 command` | Start with adjusted priority |
| `renice 5 -p PID` | Change process priority |
| `free -h` | Show memory usage |
| `uptime` | Show system uptime and load |

## 8. Package Management (APT)

| Command | Purpose |
|---|---|
| `sudo apt update` | Update package lists |
| `sudo apt upgrade` | Upgrade installed packages |
| `sudo apt full-upgrade` | Perform full distribution upgrade |
| `sudo apt install nmap` | Install package |
| `sudo apt remove nmap` | Remove package |
| `sudo apt purge nmap` | Remove package and configuration |
| `sudo apt autoremove` | Remove unused dependencies |
| `sudo apt clean` | Clear package cache |
| `sudo apt search wireshark` | Search packages |
| `apt show nmap` | Show package information |
| `dpkg -l` | List installed packages |
| `dpkg -i package.deb` | Install local Debian package |
| `dpkg -r package-name` | Remove installed package |
| `sudo apt install kali-linux-default` | Install Kali default tool collection |

## 9. Networking Commands

| Command | Purpose |
|---|---|
| `ip a` | Show network interfaces and IPs |
| `ip addr` | Show IP addresses |
| `ip link` | Show network interfaces |
| `ip route` | Show routing table |
| `ip neigh` | Show neighbor/ARP table |
| `ip route get 8.8.8.8` | Show route to destination |
| `ping google.com` | Test connectivity |
| `traceroute google.com` | Trace network route |
| `tracepath google.com` | Trace path |
| `mtr google.com` | Continuous route diagnostics |
| `ss -tuln` | Show listening TCP/UDP ports |
| `ss -tulpn` | Show listening ports and processes |
| `netstat -tuln` | Show listening ports (legacy) |
| `hostname -I` | Show assigned IP addresses |
| `nmcli device status` | Show network device status |
| `nmcli connection show` | Show network connections |
| `curl https://example.com` | Make HTTP request |
| `wget https://example.com/file` | Download file |
| `dig example.com` | DNS lookup |
| `nslookup example.com` | DNS lookup |
| `host example.com` | DNS lookup |
| `whois example.com` | Domain registration lookup |
| `resolvectl status` | Show DNS resolver status, if available |

## 10. Network Interface Management

| Command | Purpose |
|---|---|
| `ip link show` | Display interfaces |
| `ip link set eth0 up` | Enable interface |
| `ip link set eth0 down` | Disable interface |
| `ip addr show eth0` | Show interface IP |
| `ip addr add 192.168.1.10/24 dev eth0` | Add IP address |
| `ip addr del 192.168.1.10/24 dev eth0` | Remove IP address |
| `sudo dhclient eth0` | Request DHCP address, if installed |
| `nmcli radio wifi` | Check Wi-Fi radio |
| `nmcli device wifi list` | List available Wi-Fi networks |

Interface names vary. Check `ip link` before using an interface-specific command.

## 11. Network Security and Analysis Tools

| Command | Purpose |
|---|---|
| `nmap 192.168.1.1` | Scan a host |
| `nmap -sV 192.168.1.1` | Detect service versions |
| `nmap -sC 192.168.1.1` | Run default scripts |
| `nmap -p 80,443 example.com` | Scan selected ports |
| `nmap -O 192.168.1.1` | Attempt OS detection |
| `nmap -A 192.168.1.1` | Enable aggressive detection |
| `tcpdump -i eth0` | Capture network packets |
| `tcpdump -i eth0 -nn` | Capture without name resolution |
| `wireshark` | Open graphical packet analyzer |
| `tshark -i eth0` | Capture packets from terminal |
| `nc -lvnp 4444` | Listen on TCP port |
| `nc -vz example.com 443` | Test TCP connectivity |
| `socat -h` | Show socat help |
| `arp-scan --localnet` | Discover local network devices |
| `ethtool eth0` | Inspect interface settings |

Only scan systems and networks you own or have explicit permission to test.

## 12. Bash Commands and Shell Scripting

| Command | Purpose |
|---|---|
| `bash` | Start Bash shell |
| `echo $HOME` | Display environment variable |
| `echo $PATH` | Display executable search path |
| `export NAME=value` | Set environment variable |
| `env` | Display environment |
| `printenv` | Display environment variables |
| `read name` | Read user input |
| `sleep 5` | Pause for five seconds |
| `date` | Display date and time |
| `seq 1 10` | Generate sequence |
| `for i in {1..5}; do echo $i; done` | Loop |
| `if [ -f file.txt ]; then echo "Exists"; fi` | Conditional |
| `chmod +x script.sh` | Make script executable |
| `./script.sh` | Execute script |
| `bash script.sh` | Run script through Bash |
| `source ~/.bashrc` | Reload Bash configuration |
| `alias ll='ls -lah'` | Create alias |
| `unalias ll` | Remove alias |
| `set -x` | Enable command tracing |
| `set -e` | Exit script when a command fails |

## 13. Pipes and Redirection

| Command | Purpose |
|---|---|
| `command > output.txt` | Redirect output |
| `command >> output.txt` | Append output |
| `command < input.txt` | Read input from file |
| `command 2> error.txt` | Redirect errors |
| `command > output.txt 2>&1` | Redirect output and errors |
| `command1 \| command2` | Pipe output |
| `cat file.txt \| grep error` | Search through output |
| `sort file.txt` | Sort lines |
| `uniq file.txt` | Remove adjacent duplicate lines |
| `sort file.txt \| uniq` | Sort and remove duplicates |
| `wc -l file.txt` | Count lines |
| `wc -w file.txt` | Count words |
| `cut -d: -f1 /etc/passwd` | Extract fields |
| `awk '{print $1}' file.txt` | Extract first column |
| `sed 's/old/new/g' file.txt` | Replace text |
| `tee output.txt` | Display and save output |
| `xargs` | Build command arguments from input |

## 14. Disk and Storage Management

| Command | Purpose |
|---|---|
| `lsblk` | List block devices |
| `blkid` | Show filesystem identifiers |
| `df -h` | Show filesystem space |
| `du -sh *` | Show sizes of current directory entries |
| `mount` | Show mounted filesystems |
| `findmnt` | Show mount information |
| `sudo mount /dev/sdb1 /mnt` | Mount filesystem |
| `sudo umount /mnt` | Unmount filesystem |
| `fdisk -l` | List disk partitions |
| `parted -l` | List partition information |
| `mkfs.ext4 /dev/sdb1` | Create ext4 filesystem (destructive) |
| `fsck` | Check filesystem |
| `sync` | Flush filesystem buffers |

Be extremely careful with partitioning, formatting, and filesystem repair commands. They can destroy data.

## 15. System Information and Monitoring

| Command | Purpose |
|---|---|
| `uname -r` | Kernel version |
| `uname -m` | Machine architecture |
| `cat /etc/os-release` | Distribution information |
| `lscpu` | CPU information |
| `lsmem` | Memory information |
| `free -h` | Memory usage |
| `lspci` | PCI devices |
| `lsusb` | USB devices |
| `dmidecode` | Hardware information |
| `dmesg` | Kernel messages |
| `journalctl` | System journal |
| `journalctl -xe` | Recent journal errors |
| `uptime` | System uptime |
| `watch -n 2 free -h` | Monitor memory every two seconds |

## 16. Services and System Administration

| Command | Purpose |
|---|---|
| `systemctl status ssh` | Check service status |
| `sudo systemctl start ssh` | Start service |
| `sudo systemctl stop ssh` | Stop service |
| `sudo systemctl restart ssh` | Restart service |
| `sudo systemctl enable ssh` | Enable at startup |
| `sudo systemctl disable ssh` | Disable startup |
| `systemctl list-units --type=service` | List active services |
| `systemctl --failed` | Show failed units |
| `journalctl -u ssh` | View service logs |
| `service ssh status` | Check service status |
| `sudo reboot` | Restart computer |
| `sudo poweroff` | Shut down computer |
| `sudo shutdown -h now` | Shut down now |

## 17. SSH and Remote Access

| Command | Purpose |
|---|---|
| `ssh user@192.168.1.10` | Connect remotely |
| `ssh -p 2222 user@host` | Connect using custom port |
| `ssh-keygen` | Generate SSH key pair |
| `ssh-copy-id user@host` | Copy public key to server |
| `scp file.txt user@host:/tmp/` | Copy file remotely |
| `scp user@host:/tmp/file.txt .` | Download remote file |
| `sftp user@host` | Start secure file transfer |
| `ssh -v user@host` | Verbose connection troubleshooting |

## 18. Archive and Compression

| Command | Purpose |
|---|---|
| `tar -cvf archive.tar folder/` | Create TAR archive |
| `tar -xvf archive.tar` | Extract TAR archive |
| `tar -czvf archive.tar.gz folder/` | Create compressed TAR |
| `tar -xzvf archive.tar.gz` | Extract compressed TAR |
| `zip -r archive.zip folder/` | Create ZIP archive |
| `unzip archive.zip` | Extract ZIP archive |
| `gzip file.txt` | Compress file |
| `gunzip file.txt.gz` | Decompress file |
| `xz file.txt` | Compress using xz |
| `7z a archive.7z folder/` | Create 7z archive |

## 19. Text Editors

| Command | Purpose |
|---|---|
| `nano file.txt` | Open Nano |
| `vim file.txt` | Open Vim |
| `vi file.txt` | Open Vi |
| `code .` | Open current directory in VS Code, if installed |
| `gedit file.txt` | Open Gedit, if installed |

## 20. Python and Development Commands

| Command | Purpose |
|---|---|
| `python3 --version` | Check Python version |
| `python3` | Open Python interpreter |
| `python3 script.py` | Run Python script |
| `python3 -m venv venv` | Create virtual environment |
| `source venv/bin/activate` | Activate virtual environment |
| `deactivate` | Deactivate environment |
| `pip install requests` | Install Python package |
| `pip list` | List installed packages |
| `pip freeze` | List package versions |
| `python3 -m http.server 8000` | Start local HTTP server |
| `git --version` | Check Git version |
| `git clone URL` | Clone repository |
| `git status` | Check repository status |
| `git add .` | Stage changes |
| `git commit -m "message"` | Commit changes |
| `git pull` | Pull changes |
| `git push` | Push changes |

## 21. Kali Linux-Specific Commands

| Command | Purpose |
|---|---|
| `kali-tweaks` | Configure Kali environment |
| `sudo apt update` | Update package information |
| `sudo apt install kali-linux-default` | Install default tool collection |
| `sudo apt install kali-linux-large` | Install larger tool collection |
| `apt search kali-tools` | Search Kali tool packages |
| `dpkg -l` | List installed packages |
| `nmap --version` | Check Nmap |
| `burpsuite` | Launch Burp Suite, if installed |
| `wireshark` | Launch Wireshark, if installed |
| `msfconsole` | Launch Metasploit, if installed |
| `sqlmap --version` | Check SQLmap |
| `gobuster version` | Check Gobuster |
| `ffuf -V` | Check ffuf |
| `nikto -Version` | Check Nikto |
| `wpscan --version` | Check WPScan |
| `whatweb --version` | Check WhatWeb |

Kali tools are installed separately or through Kali metapackages. Not every tool is present in every installation.

## 22. Web Application Security Commands

| Command | Purpose |
|---|---|
| `curl -I https://example.com` | Inspect HTTP response headers |
| `curl -v https://example.com` | Verbose HTTP request |
| `curl -X GET https://example.com` | Send GET request |
| `curl -X POST -d 'a=1' URL` | Send POST data |
| `curl -H 'Content-Type: application/json' URL` | Set request header |
| `wget -S https://example.com` | Show response headers |
| `whatweb https://example.com` | Identify web technologies |
| `nikto -h https://example.com` | Check web server configuration |
| `gobuster dir -u https://example.com -w wordlist.txt` | Discover directories |
| `ffuf -u https://example.com/FUZZ -w wordlist.txt` | Discover paths |
| `sqlmap -u 'https://example.com/item?id=1' --batch` | Test a parameter for SQL injection |
| `wpscan --url https://example.com` | Assess WordPress installation |
| `openssl s_client -connect example.com:443` | Inspect TLS connection |
| `openssl x509 -in cert.pem -text -noout` | Inspect certificate |
| `jq '.' response.json` | Format JSON |
| `http https://example.com` | Make HTTP request using HTTPie |

Use these tools only against your own applications, intentionally vulnerable labs, or systems where you have explicit authorization. Do not run automated tests against random public websites.

## 23. Cryptography and Hashing

| Command | Purpose |
|---|---|
| `sha256sum file.txt` | Calculate SHA-256 |
| `sha1sum file.txt` | Calculate SHA-1 |
| `md5sum file.txt` | Calculate MD5 |
| `sha512sum file.txt` | Calculate SHA-512 |
| `openssl rand -hex 16` | Generate random bytes as hex |
| `openssl dgst -sha256 file.txt` | Calculate SHA-256 |
| `openssl enc -aes-256-cbc -salt -in file.txt -out file.enc` | Encrypt file |
| `openssl enc -d -aes-256-cbc -in file.enc -out file.txt` | Decrypt file |
| `gpg --gen-key` | Generate GPG key |
| `gpg --list-keys` | List public keys |
| `gpg --encrypt file.txt` | Encrypt file |
| `gpg --decrypt file.txt.gpg` | Decrypt file |

## 24. Useful Keyboard Shortcuts

| Shortcut | Purpose |
|---|---|
| `Ctrl + C` | Interrupt current command |
| `Ctrl + Z` | Suspend current process |
| `Ctrl + D` | End input or exit shell |
| `Ctrl + L` | Clear terminal |
| `Ctrl + A` | Move to beginning of line |
| `Ctrl + E` | Move to end of line |
| `Ctrl + U` | Delete before cursor |
| `Ctrl + K` | Delete after cursor |
| `Ctrl + R` | Search command history |
| `Tab` | Autocomplete |
| `↑ / ↓` | Navigate command history |
| `!!` | Repeat previous command |
| `!$` | Use last argument of previous command |

## 25. Essential Configuration Files

| File | Purpose |
|---|---|
| `/etc/passwd` | User account information |
| `/etc/shadow` | Password hash records (restricted) |
| `/etc/group` | Group information |
| `/etc/hosts` | Local hostname mapping |
| `/etc/hostname` | System hostname |
| `/etc/hosts.allow` | TCP Wrappers access rules, if used |
| `/etc/hosts.deny` | TCP Wrappers access rules, if used |
| `/etc/resolv.conf` | DNS resolver configuration |
| `/etc/fstab` | Filesystem mount configuration |
| `/etc/sudoers` | Sudo permissions |
| `/etc/ssh/sshd_config` | SSH server configuration |
| `/etc/apt/sources.list` | APT repository configuration |
| `~/.bashrc` | Bash user configuration |
| `~/.profile` | Login environment configuration |
| `~/.ssh/` | SSH user configuration and keys |

Never share private SSH keys or password hashes. Be careful when editing system configuration files.

## 26. Practical Linux Exercises

- [ ] Navigate between directories using `cd`, `pwd`, and `ls`.
- [ ] Create a directory structure using `mkdir -p`.
- [ ] Create, edit, copy, move, and delete files.
- [ ] Search for files using `find`.
- [ ] Search file contents using `grep`.
- [ ] Change file permissions using `chmod`.
- [ ] Create a user and group in a disposable VM.
- [ ] Monitor processes using `ps` and `htop`.
- [ ] Install and remove a package using APT.
- [ ] Inspect network interfaces using `ip a`.
- [ ] Inspect listening ports using `ss`.
- [ ] Capture traffic using Wireshark.
- [ ] Write a Bash script that collects system information.
- [ ] Write a Python script that checks HTTP response headers.
- [ ] Connect to a test machine using SSH.
- [ ] Analyze system logs using `journalctl`.

## 27. Suggested Learning Order

1. Basic commands and navigation
2. File and directory management
3. Permissions and ownership
4. Users and groups
5. Processes and services
6. Package management
7. Networking commands
8. Bash scripting
9. Pipes, redirection, and text processing
10. SSH and remote administration
11. System monitoring and logs
12. Kali Linux security tools
13. Web application security tools
14. Automation with Python and Bash

**Important:** This is a reference library, not a requirement to memorize every command. Learn the frequently used commands first, then practice the security tools in authorized labs.
