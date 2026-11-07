
# Part 1: Linux Fundamentals
# Phase 1 — Linux Introduction and Environment

---

## Table of Contents

1. Introduction to Linux
2. Linux vs Windows vs macOS
3. Linux Kernel, Shell, Terminal, and Distribution
4. What Is GNU/Linux?
5. Linux Distributions
6. Desktop Environment
7. CLI vs GUI
8. Open-Source Software and Package Repositories
9. Linux Filesystem Hierarchy
10. Linux Boot Process
11. Kernel Space vs User Space
12. Linux Processes and Services
13. Installing Linux in a Virtual Machine
14. VirtualBox and VMware Fundamentals
15. Snapshots, Virtual Disks, RAM, CPU, and Network Settings
16. Practical Exercises
17. Quick Revision
18. Interview and Self-Assessment Questions
19. Learning Checklist

---

# 1. Introduction to Linux

## 1.1 What Is Linux?

Linux is an open-source, Unix-like operating system kernel that manages the hardware and software resources of a computer.

It acts as an intermediary between computer hardware and applications.

Linux allows users and applications to interact with hardware components such as:

- CPU
- RAM
- Hard disks and SSDs
- Network adapters
- USB devices
- Graphics cards
- Keyboards and mice

Linux is widely used in:

- Personal computers
- Servers
- Cloud computing
- Supercomputers
- Embedded systems
- Networking devices
- Android-based devices
- Cybersecurity environments

### Simple Definition

Linux is an open-source, Unix-like operating system kernel that manages hardware resources and provides essential services for running applications.

**Important:** Technically, Linux is the kernel, not the entire operating system. A complete Linux-based operating system generally combines the Linux kernel with system utilities, libraries, applications, and other components.

## 1.2 History of Linux

Linux was created by Linus Torvalds in 1991.

Some important historical milestones:

| Year | Event |
|---|---|
| 1969 | UNIX development began at Bell Labs. |
| 1983 | Richard Stallman started the GNU Project. |
| 1985 | Free Software Foundation was established. |
| 1991 | Linus Torvalds announced the Linux kernel. |
| 1992 | Linux adopted the GPL license. |
| 1993 | Debian and Slackware distributions appeared. |
| 2004 | Ubuntu was first released. |

### Important People

**Linus Torvalds**

- Created the Linux kernel.
- Started Linux development in 1991.
- Continues to lead Linux kernel development.

**Richard Stallman**

- Started the GNU Project.
- Promoted free software.
- Founded the Free Software Foundation.

## 1.3 Important Characteristics of Linux

### 1. Open Source

Linux source code is publicly available under its applicable open-source licensing terms.

Developers can study, modify, and redistribute it according to the license.

### 2. Multiuser

Multiple users can access a Linux system with separate accounts and permissions.

For example:

- User A can access personal files.
- User B can access their own files.
- The administrator can manage system resources.

### 3. Multitasking

Linux can run multiple processes simultaneously.

For example, you can:

- Browse the internet.
- Download files.
- Run a Python program.
- Execute terminal commands.

### 4. Security

Linux provides security mechanisms such as:

- User authentication.
- File permissions.
- Ownership.
- Access control.
- Process isolation.
- Firewall functionality.
- Security modules.

### 5. Portability

Linux supports multiple hardware architectures, including:

- x86
- x86-64
- ARM
- RISC-V

### 6. Stability

Linux is widely used in environments that require reliable long-running services.

### 7. Customization

Users can customize:

- Desktop environments.
- Shells.
- Window managers.
- Kernel configurations.
- System services.
- Software packages.

## 1.4 Where Is Linux Used?

| Area | Example |
|---|---|
| Web servers | Apache, Nginx |
| Cloud computing | AWS, Azure, Google Cloud |
| Cybersecurity | Kali Linux |
| Programming | Python, C, Java development |
| Networking | Routers and network appliances |
| Containers | Docker |
| Supercomputers | Scientific computing |
| Embedded systems | IoT devices |
| Mobile devices | Android uses the Linux kernel |

### Cybersecurity Relevance

Linux is important in cybersecurity because:

- Many web servers run Linux.
- Security tools commonly support Linux.
- Security researchers use Linux command-line utilities.
- Linux permissions are important when investigating privilege escalation.
- Linux logs help identify suspicious activity.
- Kali Linux provides tools for authorized security testing.

---

# 2. Linux vs Windows vs macOS

Linux, Windows, and macOS are operating system environments with different architectures, licensing models, and approaches to system management.

## 2.1 Comparison

| Feature | Linux | Windows | macOS |
|---|---|---|---|
| Developer | Open-source community and organizations | Microsoft | Apple |
| Kernel | Linux kernel | Windows NT kernel | XNU kernel |
| Source code | Generally open source | Mostly proprietary | Mostly proprietary |
| Cost | Many distributions are free | Usually licensed | Included with Apple hardware |
| Customization | Very high | Moderate | More restricted |
| CLI | Bash, Zsh, etc. | PowerShell, CMD | Zsh, Bash |
| Software installation | Package managers and repositories | Installers, Store, package managers | App Store, installers, Homebrew |
| Security | Permissions and security frameworks | Security frameworks and permissions | Security frameworks and permissions |
| Hardware support | Broad, varies by distribution | Broad | Primarily Apple hardware |
| Server usage | Very common | Common | Less common |

## 2.2 Kernel Differences

Each operating system uses a kernel to manage system resources.

### Linux

Uses the Linux kernel.

Examples:

- Ubuntu
- Debian
- Fedora
- Kali Linux

### Windows

Uses the Windows NT kernel architecture.

### macOS

Uses the XNU kernel, which combines Mach and BSD-derived components.

## 2.3 Why Do Cybersecurity Professionals Use Linux?

Linux provides:

1. Powerful command-line utilities.
2. Flexible networking tools.
3. Access to system configuration.
4. Extensive scripting capabilities.
5. A large collection of security tools.
6. Easy access to logs and system processes.
7. Support for isolated testing environments.

For example, a security researcher might use:

```bash
ip addr
```

To inspect network interfaces.

```bash
ps aux
```

To inspect running processes.

```bash
ss -tulnp
```

To inspect listening network sockets.

These commands will become important as you progress toward web application security.

---

# 3. Linux Kernel, Shell, Terminal, and Distribution

These four terms are fundamental to understanding Linux.

They are related, but they are not the same thing.

## 3.1 Linux Kernel

The kernel is the core component of an operating system.

It manages communication between hardware and software.

### Main Responsibilities

1. Process management.
2. Memory management.
3. Device management.
4. Filesystem management.
5. Network management.
6. System call handling.
7. Hardware resource allocation.

### How Does the Kernel Work?

Consider what happens when you execute a program.

1. You enter a command in the terminal.
2. The shell interprets the command.
3. The operating system requests services from the kernel when needed.
4. The kernel manages the required resources.
5. The program executes.
6. Results are returned to the user.

The shell and kernel communicate through operating system interfaces, especially system calls.

### Check Your Kernel Version

```bash
uname -r
```

Example output:

```text
6.12.0-kali-amd64
```

Your actual output will depend on your distribution and installed kernel.

To display complete system information:

```bash
uname -a
```

Important options:

| Option | Purpose |
|---|---|
| `-r` | Kernel release |
| `-s` | Kernel name |
| `-m` | Machine architecture |
| `-a` | All available system information |

No `sudo` is required.

## 3.2 Shell

A shell is a command interpreter that accepts commands from users and executes programs.

It provides an interface between the user and the operating system.

Popular Linux shells include:

- Bash
- Zsh
- Fish
- Dash
- Ksh

### Bash

Bash stands for Bourne Again Shell.

It is one of the most commonly used shells in Linux.

Example:

```bash
echo "Hello Linux"
```

Output:

```text
Hello Linux
```

### Check Your Current Shell

```bash
echo "$SHELL"
```

Example output:

```text
/bin/bash
```

This variable usually identifies your configured login shell.

To inspect the shell process currently running:

```bash
ps -p "$$" -o comm=
```

## 3.3 Terminal

A terminal is an application or interface through which you interact with a shell.

Examples:

- GNOME Terminal
- Konsole
- Xfce Terminal
- Windows Terminal

When you open a Linux terminal, it usually starts a shell session.

### Example

You open the terminal and enter:

```bash
pwd
```

The shell interprets the command and displays the current working directory.

**Remember:**

- Terminal = Interface.
- Shell = Command interpreter.
- Kernel = Core system component.

## 3.4 Linux Distribution

A Linux distribution is a complete operating system built around the Linux kernel.

It generally includes:

- Linux kernel.
- System utilities.
- Libraries.
- Package manager.
- Software repositories.
- Installer.
- Applications.
- Sometimes a desktop environment.

Examples:

- Ubuntu
- Debian
- Fedora
- Arch Linux
- Kali Linux

### Check Your Linux Distribution

```bash
cat /etc/os-release
```

Example output:

```text
PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
ID=kali
```

The actual output depends on the distribution.

### Important Difference

| Component | Responsibility |
|---|---|
| Kernel | Manages hardware and system resources |
| Shell | Interprets commands |
| Terminal | Provides the command-line interface |
| Distribution | Combines the kernel and software into a usable operating system |

---

# 4. What Is GNU/Linux?

## 4.1 Introduction

GNU/Linux refers to an operating system environment that combines the Linux kernel with GNU software and other components.

The GNU Project was started by Richard Stallman in 1983.

Its goal was to create a complete Unix-like operating system consisting of free software.

GNU developed important system components, including:

- GNU Compiler Collection (GCC).
- GNU Bash.
- GNU Core Utilities.
- GNU Debugger (GDB).
- GNU Make.

However, the GNU Project still needed a working kernel for its complete operating system.

In 1991, Linus Torvalds released the Linux kernel.

The Linux kernel and GNU software were subsequently combined to provide a complete operating environment.

## 4.2 Relationship Between GNU and Linux

```text
             GNU/Linux System
                    |
          +---------+---------+
          |                   |
      Linux Kernel        GNU Software
          |                   |
    Hardware Management   System Utilities
                              |
                         Shell and Tools
                              |
                       User Applications
```

This is a simplified conceptual diagram.

A complete Linux distribution may also contain many non-GNU components.

## 4.3 GNU vs Linux

| GNU | Linux |
|---|---|
| Started by Richard Stallman | Created by Linus Torvalds |
| Started in 1983 | Released in 1991 |
| Developed system utilities and software | Developed the kernel |
| Provides tools such as Bash and GCC | Manages hardware and system resources |

### Important Point

Linux is technically the kernel.

GNU/Linux is a name commonly used for systems that combine GNU software with the Linux kernel.

Not every Linux distribution uses the same GNU components.

For example, Android uses the Linux kernel but does not use the traditional GNU userland as its standard environment.

---

# 5. Linux Distributions

## 5.1 What Is a Linux Distribution?

A Linux distribution is a packaged operating system that combines the Linux kernel with software, utilities, package management, and configuration tools.

Different distributions are designed for different purposes.

Some focus on beginners, while others focus on servers, development, security testing, or advanced customization.

## 5.2 Ubuntu

Ubuntu is a popular Linux distribution based on Debian.

It is developed by Canonical and the Ubuntu community.

### Features

- Beginner-friendly.
- Large software ecosystem.
- Good hardware support.
- Desktop and server editions.
- APT package management.
- Regular release schedule.

### Package Management

Ubuntu uses APT and the DPKG package system.

Install a package:

```bash
sudo apt install curl
```

Update package information:

```bash
sudo apt update
```

Upgrade installed packages:

```bash
sudo apt upgrade
```

### Common Uses

- Desktop computing.
- Programming.
- Web development.
- Cloud servers.
- Learning Linux.

## 5.3 Debian

Debian is a community-developed Linux distribution.

It is known for stability and its large software repository.

### Features

- Community-driven.
- Stable releases.
- Large package repository.
- APT package management.
- Supports multiple hardware architectures.

### Common Uses

- Servers.
- Development.
- General-purpose computing.
- Building other Linux distributions.

Ubuntu and Kali Linux are both based on Debian.

## 5.4 Fedora

Fedora is a Linux distribution sponsored by Red Hat.

It is known for adopting relatively recent technologies.

### Features

- Modern software packages.
- Strong developer ecosystem.
- SELinux integration.
- RPM package format.
- DNF package manager.

Install software:

```bash
sudo dnf install curl
```

Update the system:

```bash
sudo dnf upgrade
```

## 5.5 Arch Linux

Arch Linux is a lightweight, flexible Linux distribution designed for users who want greater control over their system.

### Features

- Rolling release model.
- Minimal base installation.
- Extensive customization.
- Pacman package manager.
- Arch User Repository (AUR).

Install a package:

```bash
sudo pacman -S curl
```

Synchronize package databases and upgrade:

```bash
sudo pacman -Syu
```

Arch Linux generally requires more manual configuration than beginner-oriented distributions.

## 5.6 Kali Linux

Kali Linux is a Debian-based Linux distribution designed for penetration testing, security research, digital forensics, and security auditing.

It is maintained by OffSec.

### Features

- Security testing tools.
- Network analysis utilities.
- Web application testing tools.
- Digital forensics utilities.
- Security research environment.
- APT package management.

Examples of tools available in Kali:

| Tool | Purpose |
|---|---|
| Nmap | Network discovery and service enumeration |
| Burp Suite | Web application security testing |
| Wireshark | Network packet analysis |
| Metasploit Framework | Security testing framework |
| SQLmap | SQL injection testing |
| Gobuster | Directory and DNS enumeration |

Use these tools only against systems you own or have explicit authorization to test.

### Is Kali Linux Suitable for Beginners?

Kali can be useful for learning cybersecurity, but it is not necessarily the best first distribution for understanding everyday Linux fundamentals.

Ubuntu is a good starting point because it provides a familiar general-purpose environment.

You can continue using Kali in your VMware environment for security-related practice.

## 5.7 Distribution Comparison

| Distribution | Main Focus | Package Manager |
|---|---|---|
| Ubuntu | General-purpose and beginner-friendly | APT |
| Debian | Stability and general-purpose use | APT |
| Fedora | Modern technologies and development | DNF |
| Arch Linux | Customization and control | Pacman |
| Kali Linux | Penetration testing and forensics | APT |

## 5.8 Check Distribution Information

```bash
cat /etc/os-release
```

Check kernel information:

```bash
uname -r
```

Check architecture:

```bash
uname -m
```

Check package manager availability:

```bash
apt --version
```

On Debian-based systems.

```bash
dnf --version
```

On Fedora-based systems.

---

# 6. What Is a Desktop Environment?

## 6.1 Introduction

A desktop environment (DE) is a collection of graphical components that provides users with a graphical interface for interacting with a Linux system.

It makes Linux easier to use without requiring every task to be performed through commands.

A desktop environment usually includes:

- Desktop background.
- Application launcher.
- Taskbar or panel.
- File manager.
- Window manager.
- System settings.
- Notification system.
- Graphical applications.

## 6.2 Popular Linux Desktop Environments

### GNOME

<insert conceptual description: modern desktop with Activities overview, application launcher and system settings>

Features:

- Modern interface.
- Clean design.
- Keyboard shortcuts.
- GNOME Shell.
- Nautilus file manager.

Commonly used in Ubuntu.

### KDE Plasma

Features:

- Highly customizable.
- Advanced desktop settings.
- Widgets.
- Flexible panels.
- Dolphin file manager.

### Xfce

Features:

- Lightweight.
- Low resource usage.
- Simple interface.
- Suitable for older hardware and lightweight virtual machines.

### LXQt

Features:

- Lightweight desktop environment.
- Low memory requirements.
- Simple interface.

## 6.3 Desktop Environment Comparison

| Desktop | Main Characteristic |
|---|---|
| GNOME | Modern and simple |
| KDE Plasma | Highly customizable |
| Xfce | Lightweight |
| LXQt | Very lightweight |

## 6.4 Desktop Environment vs Window Manager

These concepts are related but different.

**Desktop Environment:**

Provides a complete graphical experience, including panels, settings, applications, and window management.

**Window Manager:**

Controls how application windows are displayed and arranged.

A window manager can operate independently or as part of a desktop environment.

---

# 7. CLI vs GUI

## 7.1 What Is CLI?

CLI stands for Command-Line Interface.

It allows users to interact with a computer by entering text commands.

Example:

```bash
mkdir linux-practice
```

This creates a directory named `linux-practice`.

### Advantages of CLI

- Fast for repetitive operations.
- Suitable for automation.
- Powerful system administration.
- Remote server management.
- Efficient resource usage.
- Useful for cybersecurity work.

### Disadvantages of CLI

- Requires command knowledge.
- Incorrect commands can cause damage.
- Some operations are difficult to visualize.
- Beginners may find it challenging.

## 7.2 What Is GUI?

GUI stands for Graphical User Interface.

It allows users to interact with a computer through visual elements.

Examples:

- Windows.
- Buttons.
- Icons.
- Menus.
- Dialog boxes.
- File manager windows.

### Advantages of GUI

- Easy for beginners.
- Visual feedback.
- Convenient file management.
- Easier configuration for many desktop tasks.

### Disadvantages of GUI

- Some tasks require more clicks.
- Automation can be more difficult.
- Some advanced administrative tasks are unavailable or less convenient.

## 7.3 CLI vs GUI Comparison

| Feature | CLI | GUI |
|---|---|---|
| Interaction | Text commands | Visual elements |
| Learning | Requires command knowledge | Usually easier |
| Automation | Excellent | More limited |
| Resource usage | Often lower | Often higher |
| Remote administration | Very useful | Depends on remote desktop tools |
| Speed | Fast for repeated tasks | Convenient for visual tasks |

## 7.4 Why Should Cybersecurity Learners Understand CLI?

Many cybersecurity activities involve terminal commands.

Examples:

```bash
ip addr
```

Displays network interface information.

```bash
ss -tuln
```

Displays listening TCP and UDP sockets.

```bash
find /var/log -type f
```

Finds files inside the log directory.

```bash
grep -i "error" /var/log/syslog
```

Searches for lines containing the word `error` in the specified log file.

The exact log files available depend on the distribution.

**Learning recommendation:** Become comfortable with both CLI and GUI, but give consistent attention to CLI practice.

---

# 8. Open-Source Software and Package Repositories

## 8.1 What Is Open-Source Software?

Open-source software is software whose source code is made available under a license that allows specified rights such as inspection, modification, and redistribution.

The exact rights depend on the software license.

### Examples

- Linux kernel.
- Python.
- Mozilla Firefox.
- LibreOffice.
- Git.
- Apache HTTP Server.

## 8.2 Open Source vs Proprietary Software

| Feature | Open Source | Proprietary |
|---|---|---|
| Source code | Available under its license | Usually not publicly available |
| Modification | Permitted according to license | Usually restricted |
| Redistribution | Permitted according to license | Usually restricted |
| Development | Community or organization | Vendor-controlled |
| Cost | Can be free or paid | Can be free or paid |

**Important:** Open source does not automatically mean free of cost, and free of cost does not automatically mean open source.

## 8.3 What Is a Package?

A package is a collection of files containing software and information needed to install or manage it.

For example, installing `curl` installs the program and its associated package files.

## 8.4 What Is a Package Manager?

A package manager is software that helps users install, update, remove, and manage packages.

Popular Linux package managers:

| Distribution | Package Manager | Package Format |
|---|---|---|
| Ubuntu | APT / DPKG | DEB |
| Debian | APT / DPKG | DEB |
| Fedora | DNF / RPM | RPM |
| Arch Linux | Pacman | PKG.TAR.ZST |
| Kali Linux | APT / DPKG | DEB |

## 8.5 What Is a Package Repository?

A package repository is a software storage location containing packages and related metadata.

Your package manager communicates with configured repositories to obtain software.

Repositories can be maintained by:

- Distribution developers.
- Software vendors.
- Community projects.
- Organizations.

### How Package Installation Works

```text
User enters installation command
             |
             v
        Package Manager
             |
             v
       Configured Repository
             |
             v
       Package Information
             |
             v
     Download Required Packages
             |
             v
     Resolve Dependencies
             |
             v
       Install the Software
```

## 8.6 APT Package Management

APT is commonly used on Ubuntu, Debian, and Kali Linux.

### Update Package Information

```bash
sudo apt update
```

Purpose:

Downloads updated package metadata from configured repositories.

Important distinction:

`apt update` does not itself upgrade all installed software.

### Upgrade Installed Packages

```bash
sudo apt upgrade
```

Purpose:

Installs available upgrades for installed packages.

### Install Software

```bash
sudo apt install curl
```

Purpose:

Installs the curl package and required dependencies.

### Remove Software

```bash
sudo apt remove curl
```

Removes the package but may leave some configuration files.

### Remove Package and Configuration

```bash
sudo apt purge curl
```

Removes the package and its system configuration files managed by the package.

### Search for a Package

```bash
apt search nmap
```

### Display Package Information

```bash
apt show curl
```

### List Installed Packages

```bash
apt list --installed
```

### Clean Downloaded Package Archives

```bash
sudo apt clean
```

Removes downloaded package archives from APT's local cache.

> Warning: Do not randomly remove repository configuration files or run unfamiliar package-management commands. Incorrect repository configurations can cause installation and upgrade problems.

## 8.7 Why Are Repositories Important?

Repositories provide:

- Centralized software distribution.
- Package metadata.
- Dependency information.
- Software updates.
- Security fixes.
- Package verification mechanisms.

### Cybersecurity Relevance

Using trusted repositories is important because malicious or compromised packages can introduce:

- Malware.
- Backdoors.
- Unauthorized scripts.
- Vulnerable dependencies.
- Supply-chain risks.

Install software from trusted sources and verify third-party repositories before adding them.

---

# 9. Linux Filesystem Hierarchy

## 9.1 What Is a Filesystem?

A filesystem is a method used by an operating system to organize, store, retrieve, and manage data on storage devices.

Linux uses a hierarchical filesystem structure.

Unlike Windows, which commonly uses drive letters such as `C:` and `D:`, Linux presents files and directories under a single root directory.

## 9.2 Root Directory (/)

The root directory is the top-level directory in the Linux filesystem.

It is represented by:

```text
/
```

All ordinary directories and files are organized beneath it.

Example:

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

This is a simplified view. Some directories may be symbolic links to other directories on modern distributions.

## 9.3 Important Linux Directories

### 1. /bin

Contains essential user commands.

Examples may include:

- `ls`
- `cp`
- `mv`
- `cat`

On modern distributions, `/bin` is often a symbolic link to `/usr/bin`.

### 2. /boot

Contains files needed for the boot process.

Examples:

- Linux kernel images.
- Initial RAM filesystem images.
- Bootloader-related files.

### 3. /dev

Contains device files representing hardware and virtual devices.

Examples:

- `/dev/sda`
- `/dev/null`
- `/dev/zero`
- `/dev/tty`

Linux exposes many devices through this directory.

### 4. /etc

Contains system-wide configuration files.

Examples:

- `/etc/passwd`
- `/etc/group`
- `/etc/hosts`
- `/etc/hostname`
- `/etc/fstab`
- `/etc/os-release`

### 5. /home

Contains ordinary users' personal directories.

Example:

```text
/home/pulok
```

A user's documents, downloads, and personal configuration files are commonly stored here.

### 6. /lib

Contains essential shared libraries and kernel modules.

On modern distributions, `/lib` may be a symbolic link into `/usr/lib`.

### 7. /media

Commonly used as a mount location for removable devices.

Example:

```text
/media/pulok/USB
```

### 8. /mnt

Commonly used for temporary or manually mounted filesystems.

Example:

```text
/mnt/backup
```

### 9. /opt

Used for optional or additional software packages.

Some third-party applications install their files here.

### 10. /proc

A virtual filesystem providing information about processes and kernel-related information.

Examples:

```text
/proc/cpuinfo
/proc/meminfo
/proc/version
```

These are not ordinary files stored on disk.

### 11. /root

The home directory of the root administrator account.

It is different from `/`.

| Path | Meaning |
|---|---|
| `/` | Root of the entire filesystem |
| `/root` | Root user's personal directory |

### 12. /run

Contains runtime system information, often created during boot.

Examples include PID files and runtime socket information.

### 13. /sbin

Contains system administration utilities.

On modern systems, it is often a symbolic link to `/usr/sbin`.

### 14. /srv

Contains data served by system services.

For example, files associated with a web or file server may be stored here.

### 15. /sys

A virtual filesystem exposing information about devices, drivers, and kernel subsystems.

### 16. /tmp

Used for temporary files.

Temporary files may be removed automatically during reboot or by cleanup policies.

Do not assume every file in `/tmp` is deleted immediately.

### 17. /usr

Contains many user-space applications, libraries, documentation, and shared resources.

Important subdirectories:

| Directory | Purpose |
|---|---|
| `/usr/bin` | User commands and applications |
| `/usr/sbin` | System administration programs |
| `/usr/lib` | Libraries |
| `/usr/share` | Architecture-independent shared data |
| `/usr/local` | Locally installed software |

### 18. /var

Contains variable data that changes during system operation.

Examples:

- Logs.
- Caches.
- Application data.
- Mail queues.
- Spool files.

Important directory:

```text
/var/log
```

It stores many system and application logs.

## 9.4 Linux Filesystem Hierarchy Table

| Directory | Main Purpose |
|---|---|
| `/` | Root filesystem |
| `/bin` | Essential commands |
| `/boot` | Boot-related files |
| `/dev` | Device files |
| `/etc` | Configuration files |
| `/home` | User directories |
| `/lib` | Essential libraries |
| `/media` | Removable media mount points |
| `/mnt` | Temporary mount points |
| `/opt` | Optional software |
| `/proc` | Process and kernel information |
| `/root` | Root user's home |
| `/run` | Runtime data |
| `/sbin` | System administration utilities |
| `/srv` | Service data |
| `/sys` | Device and kernel information |
| `/tmp` | Temporary files |
| `/usr` | Applications and shared resources |
| `/var` | Variable data and logs |

## 9.5 Absolute Path vs Relative Path

### Absolute Path

An absolute path starts from the root directory `/`.

Example:

```bash
/home/pulok/Documents
```

It identifies the location independently of your current working directory.

### Relative Path

A relative path is interpreted from your current working directory.

Example:

```bash
Documents/file.txt
```

It refers to a location relative to the directory in which you are currently working.

### Special Path Symbols

| Symbol | Meaning |
|---|---|
| `/` | Root directory |
| `.` | Current directory |
| `..` | Parent directory |
| `~` | Current user's home directory |
| `-` | Previous working directory when used with `cd -` |

### Example

```bash
cd ~
```

Moves to your home directory.

```bash
cd ..
```

Moves one directory level upward.

```bash
cd /
```

Moves to the root directory.

---

# 10. Linux Boot Process — Basic Understanding

## 10.1 What Is the Boot Process?

The boot process is the sequence of operations performed when a computer starts and loads its operating system.

When you power on your Linux computer, several components work together to initialize the hardware and start Linux.

## 10.2 Main Stages of Linux Booting

### Stage 1: Power On

When you press the power button:

- The CPU starts executing firmware instructions.
- Hardware initialization begins.
- The motherboard firmware takes control.

### Stage 2: BIOS or UEFI

BIOS and UEFI are firmware interfaces that initialize the computer and locate a bootable device.

**BIOS:**

- Older firmware interface.
- Commonly works with MBR partitioning.
- Uses legacy boot mechanisms.

**UEFI:**

- Modern firmware interface.
- Supports GPT partitioning.
- Can load EFI applications from an EFI System Partition.

### Stage 3: Bootloader

The bootloader loads the Linux kernel.

A common Linux bootloader is GRUB.

GRUB stands for GRand Unified Bootloader.

It can provide a menu for selecting:

- Linux kernel versions.
- Different operating systems.
- Recovery options.

### Stage 4: Kernel Initialization

The Linux kernel:

- Initializes memory management.
- Detects and initializes hardware.
- Loads required drivers and modules.
- Initializes kernel subsystems.
- Prepares the system for user space.

### Stage 5: Initramfs

Initramfs is a temporary initial root filesystem loaded into memory.

It provides tools and drivers needed to prepare the real root filesystem.

For example, it can help locate and mount the actual root filesystem.

### Stage 6: Init System

After preparing the real root filesystem, the kernel starts the first user-space process.

On most modern Linux distributions, this is:

```text
systemd
```

It normally runs as PID 1.

### Stage 7: Services and Login

The init system starts configured system services and prepares the system for user login.

Depending on the system configuration, you may see:

- A graphical login screen.
- A command-line login prompt.
- An automatically started desktop session.

## 10.3 Linux Boot Process Diagram

```text
       Power On
           |
           v
       BIOS / UEFI
           |
           v
        Bootloader
          (GRUB)
           |
           v
      Linux Kernel
           |
           v
        Initramfs
           |
           v
   Mount Real Root Filesystem
           |
           v
    Init System (systemd)
           |
           v
      Start Services
           |
           v
     Login / Desktop
```

This is a simplified boot sequence; actual details depend on firmware, distribution, boot configuration, and init system.

## 10.4 Useful Boot-Related Commands

Check kernel information:

```bash
uname -a
```

Check system uptime:

```bash
uptime
```

Display system boot time:

```bash
uptime -s
```

Display boot messages:

```bash
sudo dmesg
```

Display logs from the current boot:

```bash
journalctl -b
```

Display boot duration information:

```bash
systemd-analyze
```

Display service startup timing:

```bash
systemd-analyze blame
```

These systemd commands require systemd to be installed and running.

### Cybersecurity Relevance

Understanding the boot process helps when:

- Investigating startup problems.
- Examining unexpected services.
- Reviewing boot logs.
- Understanding kernel initialization.
- Investigating persistence mechanisms.
- Hardening boot configurations.

---

# 11. Kernel Space vs User Space — Basic Understanding

## 11.1 What Is Kernel Space?

Kernel space is the protected memory and execution environment in which the operating system kernel operates.

The kernel performs privileged operations in this environment.

Examples:

- Managing hardware.
- Scheduling processes.
- Managing memory.
- Handling system calls.
- Managing device drivers.

## 11.2 What Is User Space?

User space is the environment in which ordinary applications and user-level programs execute.

Examples:

- Web browsers.
- Text editors.
- Python programs.
- Terminal applications.
- File managers.
- Web servers.

Applications generally cannot directly perform privileged hardware operations.

They request kernel services through controlled interfaces.

## 11.3 Difference Between Kernel Space and User Space

| Feature | Kernel Space | User Space |
|---|---|---|
| Purpose | Core operating system operations | Application execution |
| Privilege | High privilege | Restricted privilege |
| Memory access | Kernel-managed memory | Restricted process memory |
| Examples | Kernel, kernel drivers | Browser, Python, text editor |
| Failure impact | Can affect the entire system | Usually limited to the application |

## 11.4 What Is a System Call?

A system call is a controlled interface through which a user-space program requests a service from the kernel.

Examples include:

- `open()`
- `read()`
- `write()`
- `close()`
- `fork()`
- `execve()`

### Example: Reading a File

Suppose a Python program wants to read a file.

1. Python requests that the file be opened.
2. The relevant library functionality eventually invokes an operating system interface.
3. The kernel checks access permissions and handles the file operation.
4. The requested data is made available to the program.
5. The program processes the data.

## 11.5 Simple Architecture

```text
           USER SPACE
    +----------------------+
    | Browser              |
    | Python Program       |
    | Text Editor          |
    | Web Server           |
    +----------------------+
               |
               | System Calls
               v
    +----------------------+
    |      KERNEL SPACE    |
    |                      |
    | Process Management   |
    | Memory Management    |
    | Device Management    |
    | Filesystem           |
    | Networking           |
    +----------------------+
               |
               v
            HARDWARE
```

### Cybersecurity Relevance

The distinction is important when studying:

- Privilege escalation.
- Kernel vulnerabilities.
- System call interfaces.
- Process isolation.
- Kernel modules.
- Application sandboxing.

---

# 12. Linux Processes and Services — Introduction

## 12.1 What Is a Process?

A process is an instance of a running program.

Whenever you execute a program, the operating system creates a process to manage its execution.

Examples:

- Running a Python script.
- Opening Firefox.
- Executing a Bash command.
- Running an Nginx web server.

Each process has a process identifier called a PID.

## 12.2 Important Process Terms

| Term | Meaning |
|---|---|
| PID | Process Identifier |
| PPID | Parent Process Identifier |
| UID | User Identifier |
| GID | Group Identifier |
| CPU usage | Processor resources consumed |
| Memory usage | RAM used by a process |
| Foreground process | Process associated with the current terminal |
| Background process | Process running without occupying the terminal foreground |

## 12.3 What Is a Parent Process?

A parent process is a process that creates another process.

The newly created process is called a child process.

Example:

```text
Parent Process
      |
      +------ Child Process 1
      |
      +------ Child Process 2
```

Linux maintains relationships between processes.

## 12.4 Process States

Some common Linux process states:

| State | Meaning |
|---|---|
| R | Running or runnable |
| S | Interruptible sleep |
| D | Uninterruptible sleep |
| T | Stopped |
| Z | Zombie |

A zombie process has finished execution but still has an entry in the process table because its parent has not yet collected its exit status.

## 12.5 What Is a Service?

A service is a background system function that provides functionality to the operating system or other applications.

Examples:

- SSH service.
- Web server.
- Database server.
- Network management service.
- Logging service.

Many Linux services run as background processes.

Services are often managed through systemd on modern Linux distributions.

## 12.6 Process vs Service

| Process | Service |
|---|---|
| An instance of a running program | A system function or managed background workload |
| Can be temporary | Often intended to run continuously or on demand |
| Can be started by a user | Often managed by an init system |
| Has a PID | Usually backed by one or more processes |

A service is not necessarily a single process. Some services use multiple processes or are activated only when needed.

## 12.7 Useful Process Commands

### Display Current Processes

```bash
ps
```

Displays processes associated with the current terminal.

### Display All Processes

```bash
ps aux
```

Displays a detailed snapshot of processes across the system.

Important options:

- `a`: Show processes associated with terminals.
- `u`: Use a user-oriented display.
- `x`: Include processes without a controlling terminal.

### Display Processes in Real Time

```bash
top
```

Shows changing information about processes and resource usage.

### Display Process Tree

```bash
pstree
```

Shows parent-child process relationships.

The command may require installation on some minimal distributions.

### Find a Process

```bash
pgrep firefox
```

Displays PIDs matching the process name.

### Terminate a Process

```bash
kill PID
```

Sends the default SIGTERM signal to the specified process.

Example:

```bash
kill 1234
```

Replace `1234` with the actual PID.

> Warning: Never terminate an unknown system process simply because its name looks unfamiliar.

### Forcefully Terminate a Process

```bash
kill -9 PID
```

Sends SIGKILL.

This does not allow the process to perform normal cleanup. Use it only when necessary.

## 12.8 Managing Services with systemctl

`systemctl` is a command-line utility used to manage systemd units.

Check the status of SSH:

```bash
systemctl status ssh
```

Start SSH:

```bash
sudo systemctl start ssh
```

Stop SSH:

```bash
sudo systemctl stop ssh
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

Enable SSH at boot:

```bash
sudo systemctl enable ssh
```

Disable automatic startup:

```bash
sudo systemctl disable ssh
```

Check whether SSH is enabled:

```bash
systemctl is-enabled ssh
```

Check whether SSH is currently active:

```bash
systemctl is-active ssh
```

**Important:** A service can be running without being enabled at boot. Likewise, it can be enabled but currently stopped.

### Cybersecurity Relevance

Process and service knowledge is essential for:

- Identifying suspicious processes.
- Investigating unauthorized services.
- Checking exposed network services.
- Reviewing system resource consumption.
- Understanding persistence.
- Managing SSH and web server services.

---

# 13. Installing Linux in a Virtual Machine

## 13.1 What Is a Virtual Machine?

A virtual machine (VM) is a software-based computer that runs inside a physical computer.

It behaves like an independent computer with virtualized hardware resources.

A VM can have:

- Virtual CPU.
- Virtual RAM.
- Virtual hard disk.
- Virtual network adapter.
- Virtual graphics adapter.
- Virtual USB devices.

### Example

Your physical computer runs Windows.

You install VMware or VirtualBox.

Inside that software, you create a virtual machine and install Ubuntu.

```text
       Physical Computer
          (Windows)
               |
               v
      VMware / VirtualBox
               |
               v
        Ubuntu Virtual Machine
               |
        +------+------+
        |             |
      Linux         Apps
      Kernel       Terminal
```

This is a simplified virtualization diagram.

## 13.2 Why Use a Virtual Machine?

Virtual machines are useful for:

1. Learning Linux safely.
2. Testing different distributions.
3. Practising system administration.
4. Building cybersecurity labs.
5. Experimenting with software.
6. Testing network configurations.
7. Creating isolated environments.

You can experiment inside a VM without modifying your primary operating system in many situations.

However, a VM is not a perfect security boundary. Vulnerabilities in virtualization software and unsafe shared-resource configurations can create risks.

## 13.3 Requirements Before Installing Ubuntu

Check the following:

- VirtualBox or VMware installed.
- Ubuntu ISO downloaded from the official Ubuntu website.
- Sufficient free disk space.
- Hardware virtualization enabled.
- Sufficient RAM.
- Compatible CPU architecture.

### Recommended Starting VM Configuration

For a basic Ubuntu desktop learning VM:

| Resource | Suggested Starting Configuration |
|---|---|
| RAM | 4 GB |
| CPU | 2 virtual processors |
| Disk | 30–40 GB |
| Network | NAT |
| Firmware | UEFI or default supported setting |
| Display | Default virtual graphics configuration |

These are starting recommendations, not universal minimum requirements. Adjust them according to your physical computer's available resources and the Ubuntu version.

## 13.4 Step-by-Step Ubuntu Installation

### Step 1: Download Ubuntu

Visit:

https://ubuntu.com/download/desktop

Download the desktop ISO image.

An ISO image is a file containing the installation media for an operating system.

### Step 2: Open VMware or VirtualBox

Start your virtualization software.

Choose the option to create a new virtual machine.

### Step 3: Select the Installation ISO

Choose the Ubuntu ISO file you downloaded.

### Step 4: Configure the VM

Set:

- VM name: Ubuntu-Linux-Lab
- RAM: 4 GB if available.
- CPU: 2 virtual processors.
- Disk: 30–40 GB.
- Network: NAT.

### Step 5: Start the VM

Power on the virtual machine.

The Ubuntu installer should start.

### Step 6: Follow the Installer

Select:

- Language.
- Keyboard layout.
- Installation type.
- Software selection.
- Time zone.
- Username.
- Password.

Choose installation options carefully.

For a dedicated new virtual disk, you can normally use the guided disk installation option.

> Important: Verify that you are installing Ubuntu inside the virtual machine's virtual disk, not modifying your physical computer's disk.

### Step 7: Complete Installation

Wait for the installation to finish.

Restart the VM when prompted.

If necessary, disconnect the ISO from the virtual optical drive after installation so the VM boots from its virtual disk.

### Step 8: Log In

Enter your Ubuntu username and password.

You should now reach the Ubuntu desktop.

## 13.5 Verify Ubuntu Installation

Open the terminal and execute:

```bash
cat /etc/os-release
```

Check the kernel:

```bash
uname -r
```

Check the architecture:

```bash
uname -m
```

Check available memory:

```bash
free -h
```

Check disk space:

```bash
df -h
```

If the outputs show your Ubuntu environment and expected resources, the installation is working.

---

# 14. VirtualBox or VMware Fundamentals

## 14.1 What Is Virtualization?

Virtualization is a technology that allows physical computing resources to be divided into virtual computing environments.

Instead of requiring separate physical computers, multiple virtual machines can run on one physical machine.

## 14.2 Hypervisor

A hypervisor is software or firmware that creates and manages virtual machines.

There are two major types.

### Type 1: Bare-Metal Hypervisor

Runs directly on physical hardware.

Examples:

- VMware ESXi.
- Microsoft Hyper-V in its hypervisor architecture.
- Xen.

### Type 2: Hosted Hypervisor

Runs as an application on a host operating system.

Examples:

- Oracle VirtualBox.
- VMware Workstation.

## 14.3 Host vs Guest Operating System

**Host OS:**

The operating system running on your physical computer.

Example:

```text
Windows 11
```

**Guest OS:**

The operating system installed inside a virtual machine.

Example:

```text
Ubuntu Linux
```

## 14.4 VMware

VMware Workstation is desktop virtualization software that allows you to create and operate virtual machines.

Common features:

- VM creation.
- Virtual disk management.
- Snapshot management.
- Network configuration.
- Shared folders.
- USB device support.

## 14.5 VirtualBox

VirtualBox is a desktop virtualization platform developed by Oracle.

It supports creating and managing virtual machines.

Common features:

- VM creation.
- Virtual disk management.
- Snapshots.
- Virtual networking.
- Shared folders.
- Guest additions.

## 14.6 VMware vs VirtualBox

| Feature | VMware Workstation | VirtualBox |
|---|---|---|
| Type | Hosted virtualization | Hosted virtualization |
| VM support | Yes | Yes |
| Snapshots | Yes, product-dependent features | Yes |
| Virtual networking | Yes | Yes |
| Shared folders | Yes | Yes |
| Guest integration | VMware Tools | Guest Additions |
| Cost | Depends on product and licensing | Base product is free and open source |

Feature availability and licensing can vary by version and edition.

## 14.7 What Are VMware Tools?

VMware Tools is a set of utilities and drivers that improves communication between the guest operating system and VMware.

It can improve:

- Display resolution.
- Mouse integration.
- Clipboard sharing.
- Time synchronization.
- Shared folders.
- Guest performance and integration.

## 14.8 What Are VirtualBox Guest Additions?

Guest Additions are utilities installed inside the guest operating system to improve integration with VirtualBox.

They support features such as:

- Better display integration.
- Mouse pointer integration.
- Shared folders.
- Clipboard integration.
- Drag and drop, depending on configuration.

---

# 15. Snapshots, Virtual Disks, RAM, CPU, and Network Settings

These are essential VM concepts.

## 15.1 What Is a VM Snapshot?

A snapshot captures the state of a virtual machine at a particular point in time.

Depending on the virtualization software and snapshot configuration, it can preserve:

- Virtual disk state.
- VM configuration.
- Memory state, if included.

### Why Are Snapshots Useful?

Suppose you are experimenting with Linux configuration.

Before changing anything, create a snapshot.

If the experiment breaks the system, you can restore the previous state.

### Example Workflow

```text
Ubuntu VM Working Normally
           |
           v
     Create Snapshot
           |
           v
   Experiment with System
           |
           v
     System Has Problems
           |
           v
     Restore Snapshot
           |
           v
    Previous VM State
```

### Important Snapshot Considerations

- Snapshots are not complete independent backups.
- Snapshot chains can consume considerable disk space.
- Deleting snapshots may merge or consolidate disk changes.
- Restoring a snapshot discards changes made after that snapshot.
- Memory-state snapshots can capture running processes and open sessions.

For important files, maintain a separate backup.

## 15.2 Creating a Snapshot in VMware

1. Open VMware Workstation.
2. Select your Ubuntu virtual machine.
3. Open the Snapshot menu.
4. Select Take Snapshot.
5. Enter a descriptive name.
6. Add a description.
7. Confirm the operation.

Example snapshot name:

```text
Ubuntu-Clean-Installation
```

## 15.3 Restoring a Snapshot

1. Select your virtual machine.
2. Open the Snapshot Manager.
3. Select the snapshot you want.
4. Choose the restore or go-to option.
5. Confirm the operation.

The exact interface depends on the VMware version.

## 15.4 What Is a Virtual Disk?

A virtual disk is a file or set of files that represents a virtual machine's storage device.

The guest operating system sees it as a disk.

Examples:

| Software | Common Virtual Disk Format |
|---|---|
| VMware | VMDK |
| VirtualBox | VDI |
| Hyper-V | VHD / VHDX |

A virtual disk can store:

- Operating system files.
- Applications.
- User documents.
- Configuration files.
- Logs.

### Virtual Disk Allocation

Two common approaches:

**Dynamically Allocated Disk**

The virtual disk file grows as data is stored, up to its configured maximum size.

**Fixed-Size Disk**

The configured storage space is generally allocated in advance.

Example:

You create a 40 GB dynamically allocated virtual disk.

The guest sees a disk with a capacity of up to 40 GB, but the host storage usage grows as data is written.

## 15.5 What Is RAM?

RAM stands for Random Access Memory.

It is temporary working memory used by running programs and the operating system.

When you assign RAM to a virtual machine, you reserve or allocate part of your computer's memory for the guest.

Example:

```text
Physical Computer RAM: 16 GB
Ubuntu VM Allocation:   4 GB
```

The remaining memory must support the host operating system and other workloads.

Do not allocate all physical RAM to your virtual machine.

## 15.6 What Is a Virtual CPU?

A virtual CPU (vCPU) is a processor resource presented to a virtual machine.

For example:

```text
Physical Computer: 8 CPU cores
Ubuntu VM:         2 vCPUs
```

The hypervisor schedules virtual CPU execution on the available physical processor resources.

A vCPU is not necessarily a dedicated physical CPU core.

## 15.7 Virtual Machine Network Settings

Networking allows a virtual machine to communicate with other systems.

Common networking modes include:

### 1. NAT (Network Address Translation)

NAT allows the guest VM to access external networks through the host's network connection.

The guest typically uses a private virtual network address.

Example:

```text
              Internet
                 |
                 v
          Host Computer
                 |
                 v
             NAT Layer
                 |
                 v
            Ubuntu VM
```

Advantages:

- Convenient internet access.
- Guest is generally not directly reachable from the external network by default.
- Useful for ordinary Linux learning.

### 2. Bridged Networking

Bridged networking connects the VM to the same physical network as the host.

The VM usually receives its own IP address from the network's DHCP server.

Example:

```text
           Wi-Fi Router
                 |
        +--------+--------+
        |                 |
    Host PC           Ubuntu VM
    IP Address        IP Address
```

Advantages:

- VM can behave like another machine on the local network.
- Useful for certain networking exercises.

Security consideration:

The VM may be accessible to other devices on the same network, depending on firewall and network configuration.

### 3. Host-Only Networking

Host-only networking creates a private network between the host and the virtual machines connected to it.

It generally does not provide direct external internet connectivity.

Example:

```text
          Host Computer
                 |
           Host-Only Network
                 |
          +------+------+
          |             |
        Ubuntu        Kali
          VM            VM
```

Useful for:

- Isolated cybersecurity labs.
- Testing communication between VMs.
- Practising networking.
- Reducing exposure to external networks.

### 4. Internal Networking

Some virtualization platforms support internal networking.

It allows connected VMs to communicate with each other without providing ordinary host connectivity through that virtual network.

Useful for isolated multi-machine labs.

## 15.8 Network Mode Comparison

| Mode | Internet Access | Host Communication | VM-to-VM Communication |
|---|---|---|---|
| NAT | Usually yes | Usually through host mechanisms | Depends on network configuration |
| Bridged | Usually yes | Yes | Yes, on the same reachable network |
| Host-only | Usually no | Yes | Yes, when connected to the same network |
| Internal | Usually no | No, through that internal network | Yes |

Actual behavior depends on the virtualization platform and network configuration.

### Recommended Setup for Your Linux Learning Lab

| Purpose | Recommended Mode |
|---|---|
| Normal Ubuntu learning | NAT |
| Internet access | NAT |
| Isolated security practice | Host-only |
| Multiple isolated VMs | Host-only or Internal |
| Local network testing | Bridged, when authorized |

---

# 16. Practical Exercises

The following exercises are designed to be performed inside your Ubuntu virtual machine.

Do not execute destructive experiments on your primary operating system.

## Practical 1: Install Ubuntu in a Virtual Machine

### Objective

Install Ubuntu inside VMware or VirtualBox.

### Requirements

- VMware Workstation or VirtualBox.
- Ubuntu Desktop ISO.
- Sufficient free disk space.
- At least 4 GB RAM available for the VM, if your host supports it comfortably.

### Procedure

1. Open your virtualization software.
2. Create a new virtual machine.
3. Select the Ubuntu ISO.
4. Allocate RAM and CPU.
5. Create a virtual disk.
6. Configure NAT networking.
7. Start the VM.
8. Complete Ubuntu installation.
9. Log in to the desktop.

### Expected Result

You should be able to access the Ubuntu desktop.

### Verification

Open a terminal and run:

```bash
cat /etc/os-release
```

Then:

```bash
uname -r
```

### What You Learned

- How to create a virtual machine.
- How to install a Linux distribution.
- How a guest operating system works.
- How to verify Linux installation.

---

## Practical 2: Open the Terminal and Run Your First Commands

### Objective

Become comfortable with the Linux terminal.

### Command 1: Display Current Directory

```bash
pwd
```

Purpose:

Displays the current working directory.

### Command 2: Display Files and Directories

```bash
ls
```

Purpose:

Lists the contents of the current directory.

### Command 3: Display Detailed Information

```bash
ls -l
```

Purpose:

Displays file permissions, ownership, size, modification time, and names.

### Command 4: Display Hidden Files

```bash
ls -a
```

Purpose:

Displays hidden files as well.

In Linux, filenames beginning with a dot are normally treated as hidden.

### Command 5: Display Username

```bash
whoami
```

Purpose:

Displays the current effective username.

### Command 6: Display Current Date

```bash
date
```

Purpose:

Displays the current system date and time.

### Command 7: Display Hostname

```bash
hostname
```

Purpose:

Displays the system's hostname.

### Command 8: Display System Information

```bash
uname -a
```

Purpose:

Displays kernel and machine information.

### Command 9: Display Memory Usage

```bash
free -h
```

Purpose:

Displays RAM and swap information in a human-readable format.

### Command 10: Display Disk Usage

```bash
df -h
```

Purpose:

Displays filesystem disk usage.

### What You Learned

- Running terminal commands.
- Understanding command output.
- Inspecting the system.
- Identifying basic Linux resources.

---

## Practical 3: Create a VM Snapshot and Restore It

### Objective

Learn how snapshots protect your virtual machine's working state.

### Procedure

1. Shut down or prepare your Ubuntu VM according to your virtualization software's snapshot requirements.
2. Open VMware or VirtualBox.
3. Select your Ubuntu VM.
4. Open the snapshot management interface.
5. Create a snapshot.

Use this name:

```text
Ubuntu-Phase-1-Clean-State
```

6. Start the Ubuntu VM.
7. Create a test directory:

```bash
mkdir snapshot-test
```

8. Verify that it exists:

```bash
ls
```

9. Shut down the VM if required by your chosen snapshot workflow.
10. Restore the earlier snapshot.
11. Start Ubuntu again.
12. Check whether the directory exists:

```bash
ls
```

### Expected Result

The `snapshot-test` directory should be absent after restoring the earlier snapshot.

### What You Learned

- How snapshots work.
- How to preserve a VM state.
- How to restore a previous configuration.
- Why snapshots are useful before experiments.

---

## Practical 4: Navigate the Filesystem Using Terminal Commands

### Objective

Understand Linux directory navigation and basic file operations.

### Step 1: Move to Home Directory

```bash
cd ~
```

### Step 2: Check Your Location

```bash
pwd
```

Expected example:

```text
/home/pulok
```

Your username and path may differ.

### Step 3: Create a Practice Directory

```bash
mkdir linux-practice
```

### Step 4: Enter the Directory

```bash
cd linux-practice
```

### Step 5: Create a File

```bash
touch notes.txt
```

### Step 6: List Files

```bash
ls -l
```

You should see:

```text
notes.txt
```

### Step 7: Add Text to the File

```bash
echo "My first Linux practice file" > notes.txt
```

The `>` operator redirects output into a file and replaces its previous contents.

### Step 8: Read the File

```bash
cat notes.txt
```

Expected output:

```text
My first Linux practice file
```

### Step 9: Create Another Directory

```bash
mkdir commands
```

### Step 10: Copy the File

```bash
cp notes.txt commands/
```

### Step 11: Verify the Copy

```bash
ls commands/
```

Expected output:

```text
notes.txt
```

### Step 12: Rename a File

```bash
mv notes.txt linux-notes.txt
```

### Step 13: Verify

```bash
ls
```

You should see:

```text
commands
linux-notes.txt
```

### Step 14: Navigate to the Parent Directory

```bash
cd ..
```

### Step 15: Verify Your Location

```bash
pwd
```

### What You Learned

- Navigating directories.
- Creating directories.
- Creating files.
- Writing text to files.
- Reading files.
- Copying and renaming files.
- Understanding relative paths.

---

## Practical 5: Explore the Linux Filesystem

### Objective

Become familiar with the Linux filesystem hierarchy.

### Commands

Move to the root directory:

```bash
cd /
```

List its contents:

```bash
ls
```

Inspect configuration files:

```bash
ls /etc
```

Inspect user directories:

```bash
ls /home
```

Inspect system logs:

```bash
ls /var/log
```

Inspect virtual process information:

```bash
ls /proc
```

Check CPU information:

```bash
cat /proc/cpuinfo
```

Check memory information:

```bash
cat /proc/meminfo
```

Check mounted filesystems:

```bash
findmnt
```

### Expected Result

You should recognize the purpose of common directories and understand that some Linux filesystems, such as `/proc`, provide virtual system information.

---

## Practical 6: Inspect Running Processes

### Objective

Learn how Linux manages running programs.

### Step 1: Display Processes

```bash
ps aux
```

### Step 2: Display Process Tree

```bash
pstree
```

Install it if necessary:

```bash
sudo apt install psmisc
```

### Step 3: Display System Resource Usage

```bash
top
```

Press `q` to exit.

### Step 4: Find a Process

```bash
pgrep bash
```

### Step 5: Display System Uptime

```bash
uptime
```

### What You Learned

- What processes are.
- How to inspect processes.
- How to identify process IDs.
- How to inspect system resource usage.

---

## Practical 7: Inspect System Information

### Objective

Understand your virtual machine's basic configuration.

Run:

```bash
hostnamectl
```

Displays hostname and operating system information.

```bash
lscpu
```

Displays CPU information.

```bash
free -h
```

Displays memory usage.

```bash
df -h
```

Displays filesystem capacity.

```bash
ip addr
```

Displays network interfaces and IP addresses.

```bash
uptime
```

Displays system uptime and load averages.

### What You Learned

You can now inspect basic hardware, memory, storage, networking, and operating system information.

---

# 17. Quick Revision

## 17.1 Important Concepts

| Concept | Meaning |
|---|---|
| Linux | Open-source Unix-like kernel |
| Kernel | Core component managing system resources |
| Shell | Command interpreter |
| Terminal | Interface for interacting with a shell |
| Distribution | Complete Linux-based operating system |
| GNU/Linux | GNU software combined with Linux kernel |
| Desktop Environment | Graphical desktop components |
| CLI | Command-Line Interface |
| GUI | Graphical User Interface |
| Package Manager | Installs and manages software |
| Repository | Location containing software packages |
| Filesystem | Method of organizing and storing data |
| Root Directory | Top-level directory `/` |
| Process | Instance of a running program |
| Service | Background system function |
| PID | Process Identifier |
| Bootloader | Loads the operating system kernel |
| GRUB | Common Linux bootloader |
| systemd | Common Linux init and service manager |
| VM | Virtual Machine |
| Hypervisor | Software that creates and manages VMs |
| Snapshot | Captured VM state |
| NAT | Network Address Translation |
| vCPU | Virtual CPU |
| RAM | Random Access Memory |

## 17.2 Important Commands

| Command | Purpose |
|---|---|
| `uname -a` | Display kernel and system information |
| `uname -r` | Display kernel release |
| `cat /etc/os-release` | Identify Linux distribution |
| `echo "$SHELL"` | Display configured shell |
| `pwd` | Display current directory |
| `ls` | List directory contents |
| `ls -la` | List detailed contents, including hidden files |
| `cd` | Change directory |
| `whoami` | Display current effective username |
| `hostname` | Display hostname |
| `date` | Display date and time |
| `free -h` | Display memory usage |
| `df -h` | Display filesystem usage |
| `ip addr` | Display network interfaces |
| `ps aux` | Display running processes |
| `top` | Monitor processes |
| `pstree` | Display process hierarchy |
| `pgrep` | Find processes by name |
| `kill` | Send a signal to a process |
| `systemctl status` | Check service status |
| `journalctl -b` | Display current boot logs |
| `dmesg` | Display kernel messages |
| `uptime` | Display system uptime |
| `findmnt` | Display mounted filesystems |
| `apt update` | Refresh package metadata |
| `apt upgrade` | Upgrade installed packages |
| `apt install` | Install software |
| `mkdir` | Create a directory |
| `touch` | Create an empty file or update timestamps |
| `cp` | Copy files |
| `mv` | Move or rename files |
| `cat` | Display file contents |
| `find` | Search for files and directories |

---

# 18. Interview and Self-Assessment Questions

## Beginner-Level Questions

### Q1. What is Linux?

Linux is an open-source, Unix-like operating system kernel that manages hardware and system resources.

### Q2. Who created Linux?

Linus Torvalds created the Linux kernel in 1991.

### Q3. What is a kernel?

The kernel is the core component of an operating system that manages CPU, memory, processes, devices, and other system resources.

### Q4. What is a shell?

A shell is a command interpreter that accepts user commands and executes programs.

### Q5. What is a terminal?

A terminal provides an interface through which users interact with a shell.

### Q6. What is a Linux distribution?

A Linux distribution is a complete operating system built using the Linux kernel and other software components.

### Q7. Name five Linux distributions.

Ubuntu, Debian, Fedora, Arch Linux, and Kali Linux.

### Q8. What is GNU/Linux?

GNU/Linux commonly refers to an operating system environment combining GNU software and the Linux kernel.

### Q9. What is the difference between CLI and GUI?

CLI uses text commands, whereas GUI uses graphical elements such as windows, buttons, and menus.

### Q10. What is a desktop environment?

A desktop environment provides graphical components that allow users to interact with Linux visually.

## Intermediate-Level Questions

### Q11. What is the difference between Linux and a Linux distribution?

Linux is the kernel, while a distribution combines the kernel with system utilities, libraries, package management, and other software.

### Q12. What is a package manager?

A package manager is a software tool used to install, update, remove, and manage software packages.

### Q13. What is a package repository?

A package repository is a storage location containing software packages and metadata that package managers can access.

### Q14. What is the purpose of the `/etc` directory?

It contains system-wide configuration files.

### Q15. What is the purpose of `/var/log`?

It stores system and application log files.

### Q16. What is the difference between `/` and `/root`?

`/` is the root of the entire filesystem, while `/root` is the home directory of the root administrator.

### Q17. What is the Linux bootloader?

A bootloader loads the Linux kernel and initiates the operating system boot process. GRUB is a commonly used example.

### Q18. What is systemd?

systemd is an init system and service manager used by many modern Linux distributions.

### Q19. What is the difference between a process and a service?

A process is an instance of a running program. A service is a background system function, often managed by an init system and implemented using one or more processes.

### Q20. What is a PID?

PID stands for Process Identifier. It is a numeric identifier assigned to a process.

### Q21. What is a virtual machine?

A virtual machine is a software-based computer that uses virtualized hardware resources to run an operating system.

### Q22. What is a hypervisor?

A hypervisor creates and manages virtual machines.

### Q23. What is the difference between a host OS and a guest OS?

The host OS runs on the physical computer, while the guest OS runs inside a virtual machine.

### Q24. What is a VM snapshot?

A snapshot captures a virtual machine's state at a particular point so it can be restored later.

### Q25. What is the difference between NAT and bridged networking?

NAT allows the VM to access external networks through a translated connection. Bridged networking connects the VM to the physical network as a separate device.

## Technical Understanding Questions

### Q26. Why does Linux use a kernel?

The kernel manages system resources and provides controlled interfaces between applications and hardware.

### Q27. What happens when you execute a Linux command?

The shell interprets the command, locates and executes the relevant program, and the program requests operating system services as necessary.

### Q28. What is the difference between kernel space and user space?

Kernel space is the privileged execution environment of the kernel. User space is the restricted execution environment of ordinary applications.

### Q29. What is a system call?

A system call is an interface through which a user-space program requests services from the kernel.

### Q30. Why is Kali Linux not necessarily the best first Linux distribution?

Kali is designed primarily for security testing and forensics. Ubuntu provides a more general-purpose starting environment for learning everyday Linux fundamentals.

---

# 19. Learning Checklist

Use this checklist to track your progress.

## Linux Introduction

- [ ] I understand what Linux is.
- [ ] I understand the history of Linux.
- [ ] I know the major characteristics of Linux.
- [ ] I understand where Linux is used.
- [ ] I can explain Linux vs Windows vs macOS.

## Linux Architecture

- [ ] I understand the Linux kernel.
- [ ] I understand what a shell does.
- [ ] I understand what a terminal does.
- [ ] I understand what a Linux distribution is.
- [ ] I can explain GNU/Linux.
- [ ] I understand kernel space and user space.
- [ ] I understand system calls.

## Distributions and Interfaces

- [ ] I understand Ubuntu.
- [ ] I understand Debian.
- [ ] I understand Fedora.
- [ ] I understand Arch Linux.
- [ ] I understand Kali Linux.
- [ ] I understand desktop environments.
- [ ] I understand CLI and GUI.

## Software Management

- [ ] I understand open-source software.
- [ ] I understand software packages.
- [ ] I understand package repositories.
- [ ] I can explain package managers.
- [ ] I can use basic APT commands.

## Filesystem

- [ ] I understand the Linux root directory.
- [ ] I know the purpose of `/etc`.
- [ ] I know the purpose of `/home`.
- [ ] I know the purpose of `/var`.
- [ ] I know the purpose of `/proc`.
- [ ] I understand absolute and relative paths.
- [ ] I can navigate directories through the terminal.

## System Operations

- [ ] I understand the Linux boot process.
- [ ] I understand BIOS and UEFI at a basic level.
- [ ] I understand the bootloader.
- [ ] I understand initramfs.
- [ ] I understand systemd.
- [ ] I understand processes and services.
- [ ] I can inspect running processes.

## Virtualization

- [ ] I understand virtualization.
- [ ] I understand virtual machines.
- [ ] I understand hypervisors.
- [ ] I understand VMware.
- [ ] I understand VirtualBox.
- [ ] I can install Ubuntu inside a VM.
- [ ] I understand virtual disks.
- [ ] I understand virtual RAM and CPUs.
- [ ] I can create a snapshot.
- [ ] I can restore a snapshot.
- [ ] I understand NAT networking.
- [ ] I understand bridged networking.
- [ ] I understand host-only networking.

## Practical Skills

- [ ] I installed Ubuntu in a virtual machine.
- [ ] I opened the Linux terminal.
- [ ] I executed my first Linux commands.
- [ ] I created directories and files.
- [ ] I copied and renamed files.
- [ ] I explored the Linux filesystem.
- [ ] I inspected system information.
- [ ] I inspected running processes.
- [ ] I created a VM snapshot.
- [ ] I restored a VM snapshot.

---

# Final Learning Advice

Do not try to memorize every Linux command immediately.

Your goal in this phase is to understand the Linux environment and become comfortable interacting with it.

Focus on these five things:

1. Understand the relationship between the kernel, shell, terminal, and distribution.
2. Learn the purpose of important Linux directories.
3. Understand how Linux starts and manages processes.
4. Become comfortable using a virtual machine.
5. Practise basic terminal commands every day.

Since your long-term direction is Web Application Security and Bug Bounty Hunting, these fundamentals will prepare you for more advanced topics such as:

- Linux command-line administration.
- File permissions and ownership.
- User and group management.
- Process and service management.
- Networking.
- Bash scripting.
- Linux security and hardening.
- Security testing environments.

**Phase 1 Completion Goal:** You should be able to install Ubuntu in a virtual machine, navigate its filesystem, understand its basic architecture, inspect system resources, and explain how Linux operates at a fundamental level.

**End of Phase 1 — Linux Introduction and Environment**
