
# PHASE 4 — LINUX FILESYSTEM, PROCESSES, AND SERVICES

# PART 1: LINUX FILESYSTEM AND STORAGE

## 1. Understanding the Linux Filesystem

Linux organizes files and directories using a hierarchical structure called the filesystem.

Unlike Windows, which commonly uses drive letters such as C: and D:, Linux starts its filesystem from a single root directory represented by `/`.

### 1.1 Root Directory (/)

The root directory is the starting point of the entire Linux filesystem.

- Represented by `/`.
- Every file and directory exists somewhere under `/`.
- It contains important system directories such as `/home`, `/etc`, `/var`, and `/usr`.

Example:

```bash
cd /
ls
```

This displays the directories located directly inside the root directory.

### 1.2 Important Linux Directories

#### /home

- Stores personal directories of regular users.
- Each user generally has their own directory.
- Users store documents, downloads, scripts, and personal files here.

Example:

```bash
cd /home
ls
```

A user named `student` might have:

```text
/home/student
```

#### /root

- Home directory of the root administrator.
- Used by the root account.
- Different from `/`, which is the filesystem's root directory.

Example:

```bash
sudo ls /root
```

#### /tmp

- Stores temporary files created by applications and users.
- Temporary files may be deleted automatically during reboot or by system cleanup processes.
- Usually writable by multiple users, subject to its permissions.

Example:

```bash
cd /tmp
touch temporary.txt
ls
```

#### /etc

- Contains system-wide configuration files.
- Used to configure services, networking, users, and other system components.

Important examples:

```text
/etc/passwd
/etc/shadow
/etc/group
/etc/hostname
/etc/hosts
/etc/fstab
```

#### /var

- Stores variable data that changes during system operation.
- Commonly contains logs, caches, databases, and application data.

Important subdirectories:

```text
/var/log
/var/cache
/var/tmp
/var/lib
```

#### /var/log

- Stores system and application log files.
- Useful for troubleshooting and security investigations.

Examples:

```bash
ls /var/log
sudo less /var/log/syslog
```

Note: Some Linux distributions, including Kali, use different logging arrangements. For example, authentication logs may be stored in `/var/log/auth.log` when traditional file logging is enabled.

#### /usr

- Contains many user-space programs, libraries, documentation, and shared resources.
- Most installed applications place their executable files or supporting files under this directory.

Important subdirectories:

```text
/usr/bin
/usr/sbin
/usr/lib
/usr/share
```

#### /opt

- Commonly stores optional or third-party software.
- Applications that do not follow the distribution's usual package layout may be installed here.

Example:

```bash
ls /opt
```

#### /bin

- Traditionally contains essential user commands.
- Examples include `ls`, `cp`, `mv`, and `cat`.
- On modern distributions, `/bin` is often a symbolic link to `/usr/bin`.

#### /sbin

- Traditionally contains system administration commands.
- Examples include commands for managing filesystems and system configuration.
- On modern distributions, `/sbin` may be a symbolic link to `/usr/sbin`.

#### /dev

- Contains device files representing hardware and virtual devices.
- Linux exposes many devices through files.

Examples:

```text
/dev/sda
/dev/null
/dev/zero
/dev/tty
```

#### /proc

- A virtual filesystem containing information about running processes and the kernel.
- Most entries are generated dynamically rather than stored as ordinary files on disk.

Examples:

```bash
ls /proc
cat /proc/cpuinfo
cat /proc/meminfo
```

A process with PID 1234 may have information available under:

```text
/proc/1234
```

#### /sys

- Provides an interface to kernel devices, drivers, and hardware information.
- Used to inspect and manage certain kernel-exposed device settings.

Example:

```bash
ls /sys
```

#### /run

- Stores runtime information about the system since the current boot.
- Often contains PID files, sockets, and service runtime information.

Example:

```bash
ls /run
```

#### /mnt

- Commonly used as a temporary mount point for filesystems and storage devices.
- Administrators can manually mount disks here.

Example:

```bash
sudo mount /dev/sdb1 /mnt
```

#### /media

- Commonly used for automatically mounted removable storage devices.
- Examples include USB drives and external disks.

Example:

```bash
ls /media
```

### 1.3 Quick Directory Reference

| Directory | Purpose |
|---|---|
| `/` | Root of the filesystem |
| `/home` | Regular users' home directories |
| `/root` | Root user's home directory |
| `/tmp` | Temporary files |
| `/etc` | Configuration files |
| `/var` | Variable system data |
| `/var/log` | Log files |
| `/usr` | Programs and shared resources |
| `/opt` | Optional third-party software |
| `/bin` | Essential user commands |
| `/sbin` | System administration commands |
| `/dev` | Device files |
| `/proc` | Process and kernel information |
| `/sys` | Device and kernel interfaces |
| `/run` | Runtime system information |
| `/mnt` | Temporary mount point |
| `/media` | Removable storage mount points |

---

## 2. Symbolic Links and Hard Links

Linux supports links that allow files or directories to be accessed through different paths.

There are two major types:

1. Symbolic links (soft links).
2. Hard links.

### 2.1 Symbolic Links (Soft Links)

A symbolic link is a special file that points to another file or directory through its path.

Think of it as a shortcut.

Characteristics:

- Stores the path to the target.
- Can point to files and directories.
- Can point to targets on different filesystems.
- Can become broken if the target is deleted or moved.

Create a symbolic link:

```bash
ln -s original.txt shortcut.txt
```

Inspect it:

```bash
ls -l
```

Example:

```text
original.txt
shortcut.txt -> original.txt
```

Access the original content through the link:

```bash
cat shortcut.txt
```

### 2.2 Hard Links

A hard link is another directory entry referring to the same underlying file data (inode).

Characteristics:

- Refers to the same inode as the original file.
- Both names access the same file contents.
- Removing one filename does not remove the data while another hard link remains.
- Normally cannot be created for directories by ordinary users.
- Cannot cross filesystem boundaries.

Create a hard link:

```bash
ln original.txt hardlink.txt
```

Inspect inode numbers:

```bash
ls -li
```

The original file and hard link should have the same inode number.

### 2.3 Difference Between Symbolic and Hard Links

| Feature | Symbolic Link | Hard Link |
|---|---|---|
| Points to | A pathname | Same inode |
| Cross-filesystem | Yes | No |
| Directory links | Yes | Normally restricted |
| Target deleted | Link becomes broken | Other hard links still work |
| Inode | Different inode | Same inode |
| Command | `ln -s` | `ln` |

---

## 3. The ln Command

The `ln` command creates links between files.

Syntax:

```bash
ln [options] source destination
```

Create a hard link:

```bash
ln file.txt file-link.txt
```

Create a symbolic link:

```bash
ln -s file.txt file-shortcut.txt
```

Display links:

```bash
ls -l
```

Check inode numbers:

```bash
ls -li
```

---

## 4. Checking Disk Usage and Storage

Linux provides several commands to inspect disk space, directory sizes, storage devices, and memory.

### 4.1 df -h

The `df` command displays filesystem disk-space usage.

Syntax:

```bash
df [options]
```

Example:

```bash
df -h
```

The `-h` option displays sizes in human-readable units such as KB, MB, and GB.

Important columns:

- Filesystem: Storage device or filesystem.
- Size: Total filesystem capacity.
- Used: Space already occupied.
- Avail: Available space.
- Use%: Percentage of used storage.
- Mounted on: Filesystem mount location.

Check a specific path:

```bash
df -h /
```

### 4.2 du -sh

The `du` command estimates disk space used by files and directories.

Syntax:

```bash
du [options] directory
```

Example:

```bash
du -sh /home
```

Options:

- `-s`: Display only the total.
- `-h`: Human-readable output.

Check the size of the current directory:

```bash
du -sh .
```

Check individual directory sizes:

```bash
du -h --max-depth=1 /home
```

### 4.3 Difference Between df and du

| Command | Purpose |
|---|---|
| `df -h` | Shows available and used filesystem space |
| `du -sh` | Shows space used by a file or directory |

Example:

If your disk has 100 GB capacity and 70 GB is occupied, `df -h` reports filesystem usage.

If your Downloads directory occupies 5 GB, `du -sh ~/Downloads` reports that directory's size.

### 4.4 lsblk

The `lsblk` command displays block devices such as hard disks, SSDs, and partitions.

Example:

```bash
lsblk
```

Useful options:

```bash
lsblk -f
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

Important terms:

- NAME: Device or partition name.
- SIZE: Device size.
- TYPE: Disk, partition, or another block-device type.
- FSTYPE: Filesystem type.
- MOUNTPOINTS: Where the device is mounted.

Example output:

```text
NAME   SIZE TYPE FSTYPE MOUNTPOINTS
sda    100G disk
├─sda1  50G part ext4   /
└─sda2  50G part ext4   /home
```

This is an illustrative example, not a required partition layout.

### 4.5 Mount and Umount

Mounting means making a filesystem accessible at a directory called a mount point.

The `mount` command attaches a filesystem to the directory tree.

Syntax:

```bash
mount [options] device mount_point
```

Example:

```bash
sudo mount /dev/sdb1 /mnt
```

Check mounted filesystems:

```bash
mount
```

Or:

```bash
findmnt
```

Unmount a filesystem:

```bash
sudo umount /mnt
```

Important:

- Close files and applications using the mounted device before unmounting.
- Never disconnect an external storage device before it is safely unmounted.
- Use `lsblk -f` and `findmnt` to inspect devices before making changes.

### 4.6 Disk Partitions and Filesystems — Basics

A disk partition is a logical division of a physical storage device.

For example, a 500 GB SSD may contain:

- One partition for the operating system.
- One partition for personal data.
- One EFI System Partition for booting.

Common partitioning schemes:

**MBR (Master Boot Record)**

- Older partitioning scheme.
- Has limitations, including a typical maximum disk size of approximately 2 TiB with 512-byte logical sectors.
- Supports up to four primary partition entries.

**GPT (GUID Partition Table)**

- Modern partitioning scheme.
- Supports large disks.
- Supports many partitions.
- Commonly used with UEFI systems.

Common Linux filesystems:

| Filesystem | Description |
|---|---|
| ext4 | Widely used Linux filesystem |
| XFS | High-performance journaling filesystem |
| Btrfs | Supports features such as snapshots |
| FAT32 | Commonly used for removable storage |
| exFAT | Common for external drives |
| NTFS | Common Windows filesystem |

Inspect filesystem information:

```bash
lsblk -f
```

### 4.7 free -h

The `free` command displays RAM and swap memory usage.

Example:

```bash
free -h
```

Important columns:

- Total: Total memory.
- Used: Memory currently used.
- Free: Completely unused memory.
- Shared: Memory shared by processes.
- Buff/cache: Memory used for buffers and cache.
- Available: Estimated memory available for new applications without swapping.

Important:

Linux uses otherwise-unused RAM for caching. Therefore, low `free` memory does not automatically mean the system is running out of RAM. Pay attention to the `available` column.

---

# PART 2: PROCESSES AND SYSTEM MONITORING

## 5. What Is a Process?

A process is an instance of a running program.

When you execute a program, the operating system creates a process to manage its execution.

Examples:

- Running Firefox creates browser processes.
- Running a Python script creates a Python process.
- Starting an SSH server creates a service process.

A process uses system resources such as:

- CPU.
- RAM.
- Disk I/O.
- Network resources.

### 5.1 Process ID (PID)

Every process receives a unique Process ID, commonly called PID.

Example:

```bash
ps
```

The output includes the PID of running processes.

### 5.2 Parent Process ID (PPID)

A process may be created by another process.

The process that creates another process is its parent process.

Its identifier is called the Parent Process ID (PPID).

Example:

```bash
ps -ef
```

Important columns:

- UID: User who owns the process.
- PID: Process ID.
- PPID: Parent Process ID.
- CMD: Command used to start the process.

Inspect your current shell:

```bash
echo $$
```

This displays the PID of the current shell.

### 5.3 Process States

Linux processes can have different states.

| State | Meaning |
|---|---|
| R | Running or runnable |
| S | Interruptible sleep |
| D | Uninterruptible sleep |
| T | Stopped or traced |
| Z | Zombie process |

A zombie process has finished execution, but its parent has not yet collected its exit status.

---

## 6. ps Command

The `ps` command displays information about processes.

Basic example:

```bash
ps
```

Display all processes:

```bash
ps aux
```

Another common format:

```bash
ps -ef
```

Find a specific process:

```bash
ps aux | grep firefox
```

Display PID, PPID, user, and command:

```bash
ps -eo pid,ppid,user,comm
```

Important options:

- `a`: Show processes associated with terminals.
- `u`: User-oriented format.
- `x`: Include processes without controlling terminals.
- `-e`: Select all processes.
- `-f`: Full-format listing.

Note: `grep` may also appear in the output because it is itself a running process.

---

## 7. top Command

The `top` command displays real-time information about running processes and system resources.

Run:

```bash
top
```

It displays:

- CPU usage.
- Memory usage.
- Running processes.
- Process IDs.
- Load averages.
- Process states.

Useful keyboard shortcuts:

| Key | Function |
|---|---|
| `q` | Quit |
| `k` | Send a signal to a process |
| `P` | Sort by CPU usage |
| `M` | Sort by memory usage |
| `1` | Show individual CPU cores |

Use `top` to identify processes consuming excessive CPU or memory.

---

## 8. htop Command

`htop` is an interactive process-monitoring tool with a more user-friendly interface.

Install it if necessary:

```bash
sudo apt update
sudo apt install htop
```

Run:

```bash
htop
```

Features:

- Interactive process management.
- CPU and memory visualization.
- Process searching.
- Sorting processes.
- Sending signals to processes.

Quit:

```text
F10 or q
```

---

## 9. pgrep Command

The `pgrep` command searches for processes by name or other matching criteria and displays their PIDs.

Example:

```bash
pgrep firefox
```

Display process names along with PIDs:

```bash
pgrep -a firefox
```

Search for a process owned by a specific user:

```bash
pgrep -u username
```

---

## 10. pidof Command

The `pidof` command displays the PIDs of running programs.

Example:

```bash
pidof sshd
```

If the program is running, its PID or PIDs will be displayed.

Difference:

- `pgrep` provides flexible process searching.
- `pidof` searches for process IDs associated with a program name.

---

## 11. kill Command

The `kill` command sends a signal to a process.

It is commonly used to request a process to terminate.

Syntax:

```bash
kill [signal] PID
```

Example:

```bash
kill 1234
```

By default, `kill` sends SIGTERM (signal 15).

### Important Signals

| Signal | Number | Meaning |
|---|---:|---|
| SIGTERM | 15 | Requests process termination |
| SIGKILL | 9 | Forces process termination |
| SIGINT | 2 | Interrupt signal |
| SIGHUP | 1 | Hangup signal |

Request termination:

```bash
kill -15 1234
```

Force termination:

```bash
kill -9 1234
```

Important:

Use SIGTERM first whenever possible. SIGKILL should be a last resort because the process cannot handle or clean up after that signal.

---

## 12. killall Command

The `killall` command sends a signal to processes matching a given name.

Example:

```bash
killall firefox
```

This may terminate multiple Firefox processes.

Send SIGTERM explicitly:

```bash
killall -15 firefox
```

Use carefully because it can affect every matching process, including processes belonging to other users if you have sufficient privileges.

---

## 13. Foreground and Background Processes

Linux allows commands to run in the foreground or background.

### 13.1 Foreground Process

A foreground process runs in the terminal and normally occupies the shell until it finishes.

Example:

```bash
ping google.com
```

Stop it using:

```text
Ctrl + C
```

### 13.2 Background Process

A background process runs without keeping the terminal occupied.

Add `&` at the end of a command:

```bash
ping google.com &
```

The shell displays job information and returns the prompt.

### 13.3 jobs Command

The `jobs` command displays background and suspended jobs associated with the current shell.

Example:

```bash
jobs
```

### 13.4 bg Command

The `bg` command resumes a suspended job in the background.

Example:

```bash
ping google.com
```

Press:

```text
Ctrl + Z
```

Then:

```bash
bg
```

### 13.5 fg Command

The `fg` command brings a background or suspended job into the foreground.

Example:

```bash
fg
```

For a particular job:

```bash
fg %1
```

### 13.6 nohup Command

`nohup` runs a command so that it ignores the hangup signal, helping it continue after the terminal session closes.

Example:

```bash
nohup python3 script.py &
```

By default, output is commonly written to `nohup.out` if it is not redirected.

Redirect output manually:

```bash
nohup python3 script.py > output.log 2>&1 &
```

---

## 14. nice and renice Commands

Linux uses process priority values to influence CPU scheduling.

The nice value generally ranges from:

```text
-20 to +19
```

- `-20`: Highest scheduling priority in the nice-value range.
- `0`: Default nice value.
- `+19`: Lowest scheduling priority in the nice-value range.

### 14.1 nice

The `nice` command starts a process with a specified nice value.

Example:

```bash
nice -n 10 python3 script.py
```

This starts the script with a nice value of 10.

### 14.2 renice

The `renice` command changes the nice value of an existing process.

Example:

```bash
renice 10 -p 1234
```

Check process information:

```bash
ps -o pid,ni,comm -p 1234
```

Note: Lower nice values generally require elevated privileges to assign.

---

## 15. CPU, Memory, and Disk Usage

System monitoring helps identify performance problems and unusual activity.

### CPU Usage

CPU usage indicates how much processor capacity processes are consuming.

Commands:

```bash
top
htop
lscpu
```

### Memory Usage

Memory usage shows how much RAM is being used.

Commands:

```bash
free -h
top
```

### Disk Usage

Disk usage indicates how much storage is occupied.

Commands:

```bash
df -h
du -sh /home
lsblk
```

### Disk I/O Monitoring

Disk I/O measures data being read from and written to storage devices.

Useful command:

```bash
iostat
```

Install the required package if needed:

```bash
sudo apt install sysstat
```

Then run:

```bash
iostat -xz 1
```

---

# PART 3: SERVICES AND LOGS

## 16. What Is a Service?

A service is a program that performs a particular function, often in the background.

Services are commonly used to provide system functionality or network services.

Examples:

- SSH service.
- Web server.
- Database server.
- Cron scheduler.
- Network management service.

A service may start automatically during system boot or be started manually.

Many modern Linux distributions use `systemd` to manage services.

---

## 17. systemctl Command

`systemctl` is used to manage and inspect systemd services and other systemd units.

### 17.1 Check Service Status

Syntax:

```bash
systemctl status service_name
```

Example:

```bash
systemctl status ssh
```

This displays:

- Whether the service is loaded.
- Whether it is enabled.
- Whether it is active.
- Main process PID.
- Recent log messages.

### 17.2 Start a Service

Starts a service immediately.

```bash
sudo systemctl start ssh
```

### 17.3 Stop a Service

Stops a running service.

```bash
sudo systemctl stop ssh
```

### 17.4 Restart a Service

Stops and starts a service again.

```bash
sudo systemctl restart ssh
```

### 17.5 Reload a Service

Asks a service to reload its configuration without a full restart, if that service supports reloading.

```bash
sudo systemctl reload apache2
```

### 17.6 Enable a Service

Configures a service to start automatically during boot.

```bash
sudo systemctl enable ssh
```

### 17.7 Disable a Service

Removes the automatic-start configuration.

```bash
sudo systemctl disable ssh
```

Disabling a service does not necessarily stop it immediately.

### 17.8 Enable and Start Together

```bash
sudo systemctl enable --now ssh
```

### 17.9 Disable and Stop Together

```bash
sudo systemctl disable --now ssh
```

### 17.10 List Running Services

```bash
systemctl list-units --type=service
```

List all loaded service units, including inactive ones:

```bash
systemctl list-units --type=service --all
```

List services configured to start at boot:

```bash
systemctl list-unit-files --type=service
```

To filter for enabled services:

```bash
systemctl list-unit-files --type=service --state=enabled
```

---

## 18. journalctl Command

`journalctl` is used to view logs collected by the systemd journal.

Logs help administrators investigate errors, service failures, and system activity.

### 18.1 Display All Available Journal Entries

```bash
journalctl
```

### 18.2 Display Recent Logs

```bash
journalctl -n 50
```

Displays the latest 50 entries.

### 18.3 Follow Logs in Real Time

```bash
journalctl -f
```

Useful for monitoring new log entries as they arrive.

Exit using:

```text
Ctrl + C
```

### 18.4 View Logs of a Particular Service

Example:

```bash
journalctl -u ssh
```

### 18.5 View Recent Service Logs

```bash
journalctl -u ssh -n 50
```

### 18.6 View Logs Since Boot

```bash
journalctl -b
```

### 18.7 View Logs From the Previous Boot

```bash
journalctl -b -1
```

This requires the previous boot's journal to be available.

### 18.8 Display Logs With Priority

Example:

```bash
journalctl -p err
```

This filters for error-priority messages and more severe priorities.

---

## 19. System Logs

System logs record events and activities occurring within the operating system.

They help administrators:

- Troubleshoot system errors.
- Investigate service failures.
- Monitor system activity.
- Identify suspicious events.
- Understand unexpected behavior.

Common log locations:

```text
/var/log/
```

Important examples:

| Log | Purpose |
|---|---|
| `/var/log/syslog` | General system messages on systems using traditional syslog |
| `/var/log/auth.log` | Authentication and authorization events on systems using this log |
| `/var/log/kern.log` | Kernel messages on systems using this log |
| `/var/log/dpkg.log` | Package installation and removal activity on Debian-based systems |
| `/var/log/apache2/` | Apache web server logs, when configured there |
| `/var/log/nginx/` | Nginx web server logs, when configured there |

Note: Log locations depend on the distribution and logging configuration. Some systems primarily use the systemd journal.

---

## 20. Authentication Logs

Authentication logs record events related to user authentication and certain authorization activities.

They may contain:

- Successful login attempts.
- Failed login attempts.
- SSH authentication events.
- Sudo activity.
- User session information.

On many Debian-based systems, including some Kali installations:

```bash
sudo less /var/log/auth.log
```

Search for failed authentication attempts:

```bash
sudo grep -i "failed" /var/log/auth.log
```

Search for SSH-related events:

```bash
sudo grep -i "ssh" /var/log/auth.log
```

Using systemd journal:

```bash
sudo journalctl -u ssh
```

Security importance:

Repeated failed login attempts may indicate password guessing or brute-force activity. However, they can also result from normal user mistakes or misconfigured applications. Investigate the surrounding context before drawing conclusions.

---

## 21. Web Server Logs

Web servers record requests and events related to web applications.

Two important log categories:

### Access Logs

Record incoming HTTP requests.

They may include:

- Client IP address.
- Request method.
- Requested URL.
- HTTP status code.
- User agent.
- Timestamp.

Example:

```bash
sudo tail -f /var/log/apache2/access.log
```

### Error Logs

Record errors and problems involving the web server.

Example:

```bash
sudo tail -f /var/log/apache2/error.log
```

For Nginx:

```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

Note: Actual log paths can vary according to the server configuration.

---

## 22. dmesg Command

The `dmesg` command displays messages from the kernel's ring buffer.

These messages can provide information about:

- Hardware detection.
- Device drivers.
- USB devices.
- Storage devices.
- Kernel warnings.
- Hardware-related errors.

Example:

```bash
dmesg
```

Display recent messages:

```bash
dmesg | tail
```

Display human-readable timestamps:

```bash
dmesg -T
```

Search for errors:

```bash
sudo dmesg -T | grep -i error
```

---

## 23. uptime Command

The `uptime` command displays how long the system has been running.

Example:

```bash
uptime
```

It commonly displays:

- Current time.
- System uptime.
- Number of logged-in users.
- Load averages.

Example:

```text
16:30:00 up 2 days, 3:20, 2 users, load average: 0.20, 0.35, 0.40
```

Load averages represent the average number of tasks that are running or waiting for CPU and certain other resources over different time periods.

---

## 24. uname -a Command

The `uname` command displays system and kernel information.

Example:

```bash
uname -a
```

It displays information such as:

- Kernel name.
- Hostname.
- Kernel release.
- Kernel version.
- Hardware architecture.

Other useful commands:

```bash
uname -r
uname -m
uname -s
```

---

## 25. hostnamectl Command

The `hostnamectl` command displays or manages the system hostname and related system information.

Display information:

```bash
hostnamectl
```

Set a new hostname:

```bash
sudo hostnamectl set-hostname kali-lab
```

Check the hostname:

```bash
hostname
```

---

## 26. date Command

The `date` command displays or formats the system date and time.

Example:

```bash
date
```

Display date in a custom format:

```bash
date +"%Y-%m-%d"
```

Display time:

```bash
date +"%H:%M:%S"
```

---

## 27. timedatectl Command

The `timedatectl` command displays and manages system time settings.

Example:

```bash
timedatectl
```

It can display:

- Local time.
- Universal time (UTC).
- RTC time.
- Time zone.
- System clock synchronization status.

List available time zones:

```bash
timedatectl list-timezones
```

Set a time zone:

```bash
sudo timedatectl set-timezone Asia/Kolkata
```

Check the configuration again:

```bash
timedatectl
```

---

# PART 4: PRACTICAL LABS

Perform these exercises in your Kali Linux virtual machine.

## LAB 1 — Explore the Linux Filesystem

### Objective
Understand the Linux directory hierarchy.

Commands:

```bash
cd /
ls -la
```

Explore important directories:

```bash
ls /home
ls /etc
ls /var
ls /var/log
ls /usr
ls /dev
ls /proc
```

Tasks:

1. Identify the root directory.
2. Locate your home directory.
3. Find the system configuration directory.
4. Explore the log directory.
5. Identify some device files under `/dev`.

## LAB 2 — Create and Inspect Links

### Objective
Understand symbolic links and hard links.

Create a working directory:

```bash
mkdir ~/phase4-lab
cd ~/phase4-lab
```

Create a file:

```bash
echo "Linux filesystem practice" > original.txt
```

Create both link types:

```bash
ln original.txt hardlink.txt
ln -s original.txt symlink.txt
```

Inspect:

```bash
ls -li
```

Read through the links:

```bash
cat hardlink.txt
cat symlink.txt
```

Tasks:

1. Compare the inode numbers.
2. Identify which link has a different inode.
3. Remove the original filename and test the two links.
4. Explain why their behavior is different.

Cleanup:

```bash
cd ~
rm -r ~/phase4-lab
```

## LAB 3 — Investigate Disk and Memory Usage

### Objective
Understand storage and memory information.

Run:

```bash
df -h
du -sh ~
lsblk -f
free -h
```

Tasks:

1. Identify the filesystem mounted at `/`.
2. Find the total disk capacity.
3. Identify the largest mounted partition.
4. Check the size of your home directory.
5. Find total and available RAM.
6. Identify your storage device and filesystem type.

## LAB 4 — Identify Running Processes

### Objective
Find processes and understand their PIDs.

Run:

```bash
ps aux
```

Find a process:

```bash
pgrep -a firefox
```

If Firefox is not running, try:

```bash
pgrep -a systemd
```

Display process information:

```bash
ps -ef
```

Monitor processes:

```bash
top
```

Or:

```bash
htop
```

Tasks:

1. Find the PID of a running process.
2. Identify its PPID.
3. Find which user owns the process.
4. Identify its CPU and memory usage.
5. Explain what happens when a process terminates.

## LAB 5 — Practice Foreground and Background Jobs

### Objective
Learn how Linux manages terminal jobs.

Run:

```bash
sleep 300
```

Press `Ctrl + Z` to suspend it.

Check jobs:

```bash
jobs
```

Resume in the background:

```bash
bg
```

Bring it back to the foreground:

```bash
fg
```

Terminate it using:

```text
Ctrl + C
```

Try starting another background process:

```bash
sleep 300 &
```

Check:

```bash
jobs
```

Terminate the background job using its job ID:

```bash
kill %1
```

## LAB 6 — Practice Process Signals

### Objective
Understand how processes receive termination signals.

Start a process:

```bash
sleep 300 &
```

Find its PID:

```bash
pgrep -a sleep
```

Send SIGTERM:

```bash
kill -15 PID
```

Replace `PID` with the actual process ID.

Check whether it is still running:

```bash
pgrep -a sleep
```

Do not practice SIGKILL on important system processes.

## LAB 7 — Monitor System Resources

### Objective
Observe CPU and memory usage.

Run:

```bash
top
```

Observe:

- CPU usage.
- Memory usage.
- Load averages.
- Running processes.

In another terminal, run:

```bash
free -h
```

Then:

```bash
df -h
```

Tasks:

1. Identify the process using the most CPU.
2. Identify the process using the most memory.
3. Record available RAM.
4. Record available disk space.
5. Explain the difference between CPU usage and memory usage.

## LAB 8 — Manage Linux Services

### Objective
Learn how to inspect and manage system services.

Check SSH service status:

```bash
systemctl status ssh
```

Start SSH:

```bash
sudo systemctl start ssh
```

Check status again:

```bash
systemctl status ssh
```

Stop SSH:

```bash
sudo systemctl stop ssh
```

Check whether SSH is enabled:

```bash
systemctl is-enabled ssh
```

List enabled services:

```bash
systemctl list-unit-files --type=service --state=enabled
```

Important:

Do not enable SSH automatically unless you actually need remote access. Keep services disabled when they are unnecessary.

## LAB 9 — Investigate System Logs

### Objective
Learn to inspect system and service logs.

Display recent journal entries:

```bash
sudo journalctl -n 50
```

Display current boot logs:

```bash
sudo journalctl -b
```

Check SSH logs:

```bash
sudo journalctl -u ssh
```

Check errors:

```bash
sudo journalctl -p err
```

If traditional authentication logging is configured:

```bash
sudo tail -n 50 /var/log/auth.log
```

Tasks:

1. Find a recent system error or warning.
2. Identify its timestamp.
3. Find which service or component generated it.
4. Inspect SSH authentication events.
5. Explain why logs are important in security investigations.

## LAB 10 — Investigate a Failed Service

### Objective
Understand how to troubleshoot a service that fails to start.

Use a practice service in your Kali VM.

First, inspect its status:

```bash
systemctl status apache2
```

If Apache is installed, inspect its configuration:

```bash
sudo apache2ctl configtest
```

Inspect recent service logs:

```bash
sudo journalctl -u apache2 -n 50
```

Check whether its port is already occupied:

```bash
sudo ss -lntp
```

If the configuration is valid and the issue is resolved, start the service:

```bash
sudo systemctl start apache2
```

Verify:

```bash
systemctl status apache2
```

Important:

Do not deliberately break important system services. Practice with a disposable lab service or a test configuration.

---

# PART 5: IMPORTANT COMMAND REVISION

## Filesystem and Storage

| Command | Purpose |
|---|---|
| `pwd` | Display current directory |
| `ls` | List files |
| `cd` | Change directory |
| `ln` | Create hard links |
| `ln -s` | Create symbolic links |
| `df -h` | Display filesystem space |
| `du -sh` | Display directory size |
| `lsblk` | Display block devices |
| `mount` | Mount a filesystem |
| `umount` | Unmount a filesystem |
| `free -h` | Display memory usage |
| `findmnt` | Display mounted filesystems |

## Processes and Monitoring

| Command | Purpose |
|---|---|
| `ps` | Display processes |
| `top` | Monitor processes |
| `htop` | Interactive process monitoring |
| `pgrep` | Search for process IDs |
| `pidof` | Find program PIDs |
| `kill` | Send a signal to a process |
| `killall` | Send signals to matching processes |
| `jobs` | List shell jobs |
| `bg` | Resume a job in the background |
| `fg` | Bring a job to the foreground |
| `nohup` | Ignore hangup signals |
| `nice` | Start a process with a nice value |
| `renice` | Change a process's nice value |
| `iostat` | Display CPU and disk I/O statistics |

## Services and Logs

| Command | Purpose |
|---|---|
| `systemctl` | Manage systemd units |
| `journalctl` | Read systemd journal logs |
| `dmesg` | Display kernel messages |
| `uptime` | Display system uptime |
| `uname -a` | Display kernel and system information |
| `hostnamectl` | Display or change hostname |
| `date` | Display date and time |
| `timedatectl` | Manage system time settings |
| `tail` | Display the end of a file |
| `grep` | Search text patterns |
| `ss -lntp` | Inspect listening TCP sockets and processes |

---

# PART 6: KNOWLEDGE CHECK

Before moving to Phase 5, make sure you can answer these questions:

1. What is the Linux root directory?
2. What is the difference between `/` and `/root`?
3. What is the purpose of `/etc`?
4. What information is stored in `/var/log`?
5. What is the difference between a symbolic link and a hard link?
6. What is an inode?
7. What is the difference between `df -h` and `du -sh`?
8. What is the purpose of `lsblk`?
9. What does mounting mean in Linux?
10. What is a process?
11. What is the difference between PID and PPID?
12. What is the purpose of `ps aux`?
13. What is the difference between `top` and `htop`?
14. What is the difference between SIGTERM and SIGKILL?
15. What is the difference between foreground and background processes?
16. What is the purpose of `nohup`?
17. What is a Linux service?
18. What is the difference between `start` and `enable` in systemctl?
19. What is the purpose of `journalctl`?
20. Why are authentication logs important in cybersecurity?
21. What is the purpose of `dmesg`?
22. How would you investigate a service that fails to start?

# PHASE 4 COMPLETION CHECKLIST

- [ ] Understand the Linux filesystem hierarchy.
- [ ] Understand symbolic and hard links.
- [ ] Use `ln` to create links.
- [ ] Check storage using `df`, `du`, and `lsblk`.
- [ ] Understand mounting and unmounting.
- [ ] Understand basic disk partitions and filesystems.
- [ ] Check RAM using `free`.
- [ ] Understand processes, PIDs, and PPIDs.
- [ ] Use `ps`, `top`, and `htop`.
- [ ] Find processes using `pgrep` and `pidof`.
- [ ] Manage processes using `kill`.
- [ ] Understand foreground and background jobs.
- [ ] Use `nohup`, `nice`, and `renice`.
- [ ] Monitor CPU, memory, and disk usage.
- [ ] Manage services using `systemctl`.
- [ ] Inspect logs using `journalctl`.
- [ ] Understand authentication and web server logs.
- [ ] Inspect kernel messages using `dmesg`.
- [ ] Investigate a failed service.

# WHY THIS PHASE MATTERS IN CYBERSECURITY

These Linux skills are useful in several cybersecurity activities:

1. **System Enumeration:** Identifying running processes, services, users, and system configurations.
2. **Incident Investigation:** Inspecting logs to understand suspicious activities.
3. **Privilege and Process Analysis:** Understanding which users own processes and how they operate.
4. **Web Application Security:** Inspecting web server processes, services, and logs.
5. **System Administration:** Managing storage, services, and system resources.
6. **Security Monitoring:** Identifying unusual resource consumption and unexpected processes.

**Your goal:** Do not just memorize commands. Understand what information each command provides, when to use it, and how to interpret its output.
