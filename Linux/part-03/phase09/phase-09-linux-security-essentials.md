
# Phase 9: Linux Security Essentials

## Table of Contents

1. Introduction to Linux Security
2. Principle of Least Privilege
3. User and Group Security
4. File Permissions and Sensitive Files
5. Secure sudo Configuration
6. Patch Management
7. Service Hardening
8. Disabling Unnecessary Services
9. Firewall Basics
10. SSH Hardening Fundamentals
11. Password and Authentication Policies
12. File Integrity Monitoring
13. Log Collection and Monitoring
14. Audit Logs
15. Linux Capabilities
16. AppArmor and SELinux
17. Secrets Management
18. Secure Backups
19. System Recovery
20. Basic Incident-Response Workflow
21. Indicators of Compromise
22. Persistence Mechanisms
23. Privilege Escalation Concepts
24. Security Baselines and Hardening Checklists
25. Important Configuration and Log Locations
26. Practical Linux Security Assessment
27. Hands-on Lab Exercises
28. Interview Questions and Answers
29. Quick Revision

---

# 1. Introduction to Linux Security

## 1.1 What is Linux Security?

Linux security refers to the techniques, policies, configurations, and mechanisms used to protect Linux operating systems from unauthorized access, malicious activities, data theft, and system compromise.

Linux security aims to protect:

- Users and accounts.
- Files and directories.
- Running processes.
- Network connections.
- System services.
- Sensitive information.
- Application data.
- System configurations.

Linux provides several built-in security mechanisms, including:

1. User and group permissions.
2. Authentication and authorization.
3. sudo access control.
4. Firewall rules.
5. Security updates.
6. Linux capabilities.
7. AppArmor and SELinux.
8. System logging and auditing.

## 1.2 Three Main Goals of Linux Security

Linux security supports the CIA Triad.

### Confidentiality

Confidentiality ensures that information is accessible only to authorized users.

Example:
- Protecting `/etc/shadow`.
- Restricting access to private SSH keys.
- Preventing unauthorized users from reading sensitive files.

### Integrity

Integrity ensures that information and system configurations are not modified without authorization.

Example:
- Preventing unauthorized changes to system binaries.
- Monitoring sensitive configuration files.
- Detecting modifications to important files.

### Availability

Availability ensures that systems and services remain accessible when required.

Example:
- Maintaining backups.
- Applying security patches.
- Preventing resource exhaustion.
- Recovering systems after failures.

## 1.3 Linux Security Layers

A Linux system can be protected through multiple security layers.

```text
+--------------------------------+
|       Application Security     |
+--------------------------------+
|       Network Security         |
+--------------------------------+
|       Service Hardening        |
+--------------------------------+
|       File Permissions         |
+--------------------------------+
|       User Authentication     |
+--------------------------------+
|       Kernel Security          |
+--------------------------------+
|       Physical Security        |
+--------------------------------+
```

This is an example of defense-in-depth: multiple security controls work together rather than relying on a single protection mechanism.

---

# 2. Principle of Least Privilege

## 2.1 What is the Principle of Least Privilege?

The principle of least privilege states that every user, process, application, and service should receive only the minimum permissions required to perform its intended task.

In simple words:

**Give users and applications only the access they actually need.**

For example:

Suppose a normal user needs to read a report file.

That user should receive permission to read the file rather than unnecessary administrator privileges.

## 2.2 Why is Least Privilege Important?

It helps:

- Reduce unauthorized access.
- Limit the impact of compromised accounts.
- Prevent unnecessary administrative operations.
- Reduce privilege-escalation opportunities.
- Protect sensitive files.
- Limit damage caused by malware.

## 2.3 Example

Consider three Linux users:

| User | Required Access |
|---|---|
| Student | Read project files |
| Developer | Modify project files |
| Administrator | Manage system configuration |

Giving all three users root privileges would violate the principle of least privilege.

## 2.4 Identify users with administrative access

On many Debian-based systems:

```bash
getent group sudo
```

This displays the users belonging to the sudo group.

Check the current user:

```bash
whoami
```

Check the current user's groups:

```bash
groups
```

## 2.5 Identify processes running as root

```bash
ps -eo user,pid,comm
```

This displays process ownership, process IDs, and command names.

To identify processes owned by root:

```bash
ps -U root -u root -o pid,comm
```

### Security connection

If an application does not need administrative privileges, it should not run as root.

Running applications with unnecessary privileges increases the potential impact of a vulnerability.

---

# 3. User and Group Security

## 3.1 What are Linux users?

A Linux user is an account that represents an individual or a service within the operating system.

Each user has a unique User ID (UID).

Linux generally distinguishes between:

- Root user.
- Regular users.
- System or service users.

## 3.2 What are Linux groups?

A group is a collection of user accounts.

Groups simplify permission management because permissions can be assigned to a group instead of individual users.

Each group has a Group ID (GID).

Example:

A development team may belong to a group named `developers`.

Members of this group can receive access to shared development files.

## 3.3 Important user-management commands

Create a user:

```bash
sudo adduser student
```

Or:

```bash
sudo useradd student
```

Set a password:

```bash
sudo passwd student
```

Delete a user:

```bash
sudo userdel student
```

Delete a user and its home directory:

```bash
sudo userdel -r student
```

Modify a user:

```bash
sudo usermod -aG sudo student
```

The above command adds the user to the sudo group on Debian-based systems.

The `-aG` options mean:

- `-a`: Append to supplementary groups.
- `-G`: Specify supplementary groups.

Avoid using `-G` without `-a` when you intend to preserve existing supplementary group memberships.

## 3.4 Important group-management commands

Create a group:

```bash
sudo groupadd developers
```

Add a user to a group:

```bash
sudo usermod -aG developers student
```

Display a user's groups:

```bash
groups student
```

Display group information:

```bash
getent group developers
```

Remove a user from a group:

```bash
sudo gpasswd -d student developers
```

## 3.5 Important user configuration files

### /etc/passwd

Stores basic account information.

```bash
cat /etc/passwd
```

Example entry:

```text
student:x:1001:1001:Student:/home/student:/bin/bash
```

Fields:

| Field | Meaning |
|---|---|
| student | Username |
| x | Password information stored separately |
| 1001 | UID |
| 1001 | Primary GID |
| Student | User description |
| /home/student | Home directory |
| /bin/bash | Login shell |

### /etc/shadow

Stores password hashes and password-aging information.

```bash
sudo getent shadow student
```

This command requests the account's shadow entry. Access is normally restricted to privileged users.

Do not expose or share the output.

### /etc/group

Stores group information.

```bash
cat /etc/group
```

Example:

```text
developers:x:1002:student
```

### /etc/gshadow

Stores protected group authentication and membership information.

Its access is restricted because it contains sensitive information.

## 3.6 Security practices for users and groups

- Remove unused accounts.
- Disable accounts that are no longer required.
- Avoid sharing user accounts.
- Restrict sudo access.
- Review group memberships.
- Use dedicated service accounts.
- Avoid unnecessary root access.

---

# 4. File Permissions and Sensitive Files

## 4.1 Understanding Linux file permissions

Linux uses file permissions to control who can read, write, or execute files and directories.

There are three permission categories:

1. User (Owner)
2. Group
3. Others

There are three basic permission types:

| Permission | Symbol | Meaning |
|---|---|---|
| Read | r | Read file contents or list directory entries |
| Write | w | Modify file or directory entries |
| Execute | x | Execute a file or traverse a directory |

## 4.2 Understand permission output

Run:

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

Breakdown:

```text
-   rwx   r-x   r--
    User  Group Others
```

The first character identifies the file type.

For example:

- `-` = Regular file.
- `d` = Directory.
- `l` = Symbolic link.

## 4.3 Numeric permissions

Linux permissions can also be represented numerically.

| Permission | Numeric Value |
|---|---|
| Read | 4 |
| Write | 2 |
| Execute | 1 |

Examples:

| Permission | Calculation | Value |
|---|---|---|
| rwx | 4+2+1 | 7 |
| rw- | 4+2 | 6 |
| r-x | 4+1 | 5 |
| r-- | 4 | 4 |
| --- | 0 | 0 |

Example:

```bash
chmod 755 script.sh
```

This means:

- Owner: Read, write, execute.
- Group: Read, execute.
- Others: Read, execute.

Another example:

```bash
chmod 600 secret.txt
```

Only the owner receives read and write permission.

## 4.4 Change file ownership

Change file owner:

```bash
sudo chown student file.txt
```

Change owner and group:

```bash
sudo chown student:developers file.txt
```

Change ownership recursively:

```bash
sudo chown -R student:developers project/
```

Use recursive ownership changes carefully, especially on system directories.

## 4.5 Sensitive Linux files

Some Linux files contain important account, authentication, or configuration information.

| File | Purpose |
|---|---|
| `/etc/passwd` | User account information |
| `/etc/shadow` | Password hashes and aging information |
| `/etc/sudoers` | sudo policy configuration |
| `/etc/ssh/sshd_config` | SSH server configuration |
| `/etc/hosts` | Local hostname resolution |
| `/etc/resolv.conf` | Resolver configuration or managed resolver state |
| `/etc/crontab` | System-wide scheduled tasks |

Check permissions without exposing file contents:

```bash
ls -l /etc/shadow
ls -l /etc/sudoers
ls -ld /etc/ssh
```

## 4.6 Special permissions

Linux also supports special permission bits:

### SUID

Set User ID allows an executable to run with the effective UID of its owner.

Example:

```bash
ls -l /usr/bin/passwd
```

SUID is represented by `s` in the owner's execute position.

### SGID

Set Group ID can cause an executable to run with the effective group ID of its group owner.

On directories, it causes newly created entries to inherit the directory's group.

### Sticky Bit

The sticky bit on a directory restricts deletion or renaming of entries to the entry owner, directory owner, or a privileged user.

Example:

```bash
ls -ld /tmp
```

A sticky directory commonly displays `t` in its permission string.

### Security relevance

Incorrect permissions and unsafe special-permission configurations can create privilege-escalation risks.

---

# 5. Secure sudo Configuration

## 5.1 What is sudo?

`sudo` stands for "superuser do".

It allows authorized users to execute commands with elevated privileges.

Example:

```bash
sudo apt update
```

The command runs with elevated privileges according to the sudo policy.

## 5.2 Why is sudo important?

It helps administrators:

- Control administrative access.
- Grant specific privileges.
- Avoid sharing the root password.
- Record administrative command activity.
- Apply least privilege.

## 5.3 Check sudo permissions

```bash
sudo -l
```

This displays the commands the current user is permitted to execute through sudo.

## 5.4 Inspect sudo configuration

The main configuration file is:

```text
/etc/sudoers
```

Never edit it directly with an ordinary text editor.

Use:

```bash
sudo visudo
```

`visudo` validates the syntax before saving the configuration.

Additional policy files may exist in:

```text
/etc/sudoers.d/
```

## 5.5 Example sudo rule

A rule may look like:

```text
student ALL=(ALL:ALL) ALL
```

It means that the user `student` may run commands as any user or group on any host covered by that policy.

This is broad administrative access, not least privilege.

## 5.6 Secure sudo practices

- Give sudo access only to necessary users.
- Avoid unrestricted sudo permissions.
- Review sudoers rules regularly.
- Use `visudo` for modifications.
- Monitor sudo activity.
- Avoid giving users unrestricted access to programs that can launch arbitrary commands.

### Important security concept

A program that appears harmless may provide access to a shell or arbitrary command execution. Therefore, restricting sudo to a program name does not automatically make that permission safe.

---

# 6. Patch Management

## 6.1 What is patch management?

Patch management is the process of identifying, obtaining, testing, and installing software updates to fix security vulnerabilities, bugs, and other software problems.

Software vendors release updates to correct known vulnerabilities.

An unpatched system may remain exposed to security weaknesses.

## 6.2 Why are security updates important?

They help:

- Fix known vulnerabilities.
- Improve operating system stability.
- Correct software bugs.
- Reduce attack opportunities.
- Protect system services.

## 6.3 Check available updates

On Kali Linux and other Debian-based systems:

```bash
sudo apt update
```

This refreshes package repository information.

List upgradable packages:

```bash
apt list --upgradable
```

Upgrade installed packages:

```bash
sudo apt upgrade
```

For a broader dependency-aware upgrade:

```bash
sudo apt full-upgrade
```

Review the proposed changes before confirming.

## 6.4 Check package information

```bash
apt show openssh-server
```

Check installed package version:

```bash
dpkg -l openssh-server
```

## 6.5 Identify outdated packages

```bash
apt list --upgradable
```

This lists packages with available upgrades based on the configured repositories.

## 6.6 Patch management best practices

1. Maintain an inventory of installed software.
2. Monitor security advisories.
3. Prioritize critical vulnerabilities.
4. Test important updates where possible.
5. Apply security patches promptly.
6. Reboot when required by kernel or system updates.
7. Verify that services work after updates.
8. Maintain recovery options.

### Cybersecurity connection

An outdated application or operating system may contain publicly known vulnerabilities that attackers can exploit.

Patch management is an essential defensive security activity.

---

# 7. Service Hardening

## 7.1 What is a Linux service?

A service is a background program that performs a specific function on a Linux system.

Examples:

- SSH server.
- Web server.
- Database server.
- DNS service.
- Network management service.

Many Linux services are managed through systemd.

## 7.2 What is service hardening?

Service hardening means configuring services to reduce their attack surface and prevent unnecessary access or behavior.

It involves:

- Restricting service privileges.
- Limiting network exposure.
- Disabling unnecessary features.
- Applying security updates.
- Using secure configuration.
- Monitoring service activity.

## 7.3 List running services

```bash
systemctl list-units --type=service --state=running
```

List installed service unit files:

```bash
systemctl list-unit-files --type=service
```

## 7.4 Inspect a service

Example:

```bash
systemctl status ssh
```

View detailed service information:

```bash
systemctl cat ssh
```

Inspect recent service logs:

```bash
sudo journalctl -u ssh
```

## 7.5 Service hardening through systemd

Systemd supports security-related service settings.

Examples include:

- `NoNewPrivileges=`
- `PrivateTmp=`
- `ProtectSystem=`
- `ProtectHome=`
- `ReadOnlyPaths=`
- `CapabilityBoundingSet=`

These options can restrict a service's privileges and access to the system.

Example configuration fragment:

```ini
[Service]
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
```

These settings are illustrative. They may break a service if it legitimately needs the restricted resources.

Test service changes carefully before using them on important systems.

---

# 8. Disabling Unnecessary Services

## 8.1 Why disable unnecessary services?

Every running network service may introduce an additional attack surface.

If a service is not required, leaving it active may create unnecessary exposure.

For example, a machine that does not provide FTP services should not run an FTP server without a clear requirement.

## 8.2 Identify running services

```bash
systemctl --type=service --state=running
```

## 8.3 Identify listening network services

```bash
sudo ss -tulnp
```

This displays listening TCP and UDP sockets.

Identify the process associated with a listening port.

## 8.4 Stop a service

Example:

```bash
sudo systemctl stop apache2
```

This stops the Apache service immediately.

## 8.5 Disable automatic startup

```bash
sudo systemctl disable apache2
```

This prevents the service from starting automatically at boot.

## 8.6 Stop and disable a service

```bash
sudo systemctl disable --now apache2
```

Use this only when you have confirmed the service is unnecessary.

## 8.7 Important warning

Do not disable services simply because you do not recognize their names.

Some services are required for:

- Networking.
- Hardware management.
- Logging.
- System boot.
- Security monitoring.
- Virtual machine integration.

Investigate the purpose and dependencies of a service before changing it.

---

# 9. Firewall Basics

## 9.1 What is a firewall?

A firewall is a security mechanism that controls network traffic according to predefined rules.

It can allow or block incoming and outgoing network connections.

Firewalls help protect systems from unauthorized network access.

## 9.2 Types of firewall rules

### Inbound rules

Control traffic entering the system.

Example:

Allow SSH connections from an authorized network.

### Outbound rules

Control traffic leaving the system.

Example:

Allow required application traffic while restricting unnecessary connections.

## 9.3 UFW

UFW stands for Uncomplicated Firewall.

It provides a simpler interface for managing firewall rules on Linux.

Check its status:

```bash
sudo ufw status
```

Enable UFW:

```bash
sudo ufw enable
```

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTP:

```bash
sudo ufw allow 80/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

Deny a port:

```bash
sudo ufw deny 23/tcp
```

Delete a rule:

```bash
sudo ufw delete deny 23/tcp
```

View numbered rules:

```bash
sudo ufw status numbered
```

## 9.4 Default firewall policies

A common host firewall configuration is:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

This blocks unsolicited incoming connections while permitting outgoing traffic by default.

However, configure required access before enabling the firewall.

For example, if you are connected to a machine over SSH, allow the SSH port first:

```bash
sudo ufw allow 22/tcp
```

Otherwise, you may lock yourself out.

## 9.5 nftables

`nftables` is a Linux framework for packet filtering and network traffic control.

It is the modern replacement for older iptables-based packet filtering infrastructure.

Check rules:

```bash
sudo nft list ruleset
```

Check whether nftables is available:

```bash
nft --version
```

## 9.6 Firewall security considerations

- Allow only necessary ports.
- Restrict administrative access.
- Review firewall rules regularly.
- Remove obsolete rules.
- Understand inbound and outbound traffic.
- Avoid locking yourself out during configuration.
- Test the actual network behavior after changes.

---

# 10. SSH Hardening Fundamentals

## 10.1 What is SSH hardening?

SSH hardening means improving SSH server security by restricting unnecessary access and strengthening authentication.

The server configuration is commonly stored in:

```text
/etc/ssh/sshd_config
```

## 10.2 Important SSH security settings

### Disable direct root login

```text
PermitRootLogin no
```

### Restrict users

```text
AllowUsers student admin
```

### Enable public-key authentication

```text
PubkeyAuthentication yes
```

### Disable password authentication

```text
PasswordAuthentication no
```

Only do this after confirming that key-based authentication works and you have a recovery route.

### Limit authentication attempts

```text
MaxAuthTries 3
```

## 10.3 Validate SSH configuration

```bash
sudo sshd -t
```

## 10.4 Reload SSH

```bash
sudo systemctl reload ssh
```

Keep an existing session open until you verify that a fresh connection works.

## 10.5 SSH security checklist

- Disable unnecessary root login.
- Use strong key-based authentication.
- Protect private keys.
- Restrict access to authorized users.
- Monitor authentication logs.
- Keep OpenSSH updated.
- Verify host keys.
- Use firewall restrictions.

---

# 11. Password and Authentication Policies

## 11.1 What is an authentication policy?

An authentication policy defines how users prove their identity when accessing a system.

It may control:

- Password requirements.
- Password expiration.
- Account lockout.
- Authentication methods.
- Multi-factor authentication.
- Login restrictions.

## 11.2 Password quality

A strong password should:

- Be sufficiently long.
- Be difficult to guess.
- Avoid common words and predictable patterns.
- Not be reused across services.
- Be stored securely.

Passphrases are often easier to remember and can provide strong protection when sufficiently long and unique.

## 11.3 Check password aging

Linux provides the `chage` command for password-aging management.

View account aging information:

```bash
sudo chage -l student
```

Set a maximum password age:

```bash
sudo chage -M 90 student
```

Set a minimum password age:

```bash
sudo chage -m 1 student
```

Set account expiration:

```bash
sudo chage -E 2027-12-31 student
```

Use password expiration policies according to organizational requirements. Forced periodic password changes are not universally recommended for every environment.

## 11.4 PAM

PAM stands for Pluggable Authentication Modules.

PAM provides a flexible framework for authentication and related account-management operations on Linux.

PAM configuration is commonly found in:

```text
/etc/pam.d/
```

For example:

```bash
ls /etc/pam.d/
```

PAM can support:

- Password authentication.
- Account restrictions.
- Password quality checks.
- Authentication policies.
- Multi-factor authentication modules.

Do not modify PAM configuration without understanding the effects. An incorrect change can prevent users from logging in.

---

# 12. File Integrity Monitoring

## 12.1 What is file integrity monitoring?

File Integrity Monitoring (FIM) is the process of detecting unauthorized or unexpected changes to important files.

It helps identify modifications to:

- System binaries.
- Configuration files.
- Authentication files.
- Application files.
- Security policies.

## 12.2 Why is FIM important?

An attacker who gains access to a Linux machine may attempt to modify:

- System configuration.
- Executable files.
- SSH configuration.
- Scheduled tasks.
- Application code.

FIM can help identify suspicious changes.

## 12.3 Hashing for integrity checking

A cryptographic hash produces a fixed-length digest from input data.

Example:

```bash
sha256sum /etc/hosts
```

Example output:

```text
<sha256-hash>  /etc/hosts
```

Save a baseline:

```bash
sha256sum /etc/hosts > hosts.hash
```

Later, calculate the hash again:

```bash
sha256sum /etc/hosts
```

Compare the results.

If the hashes differ, the file contents have changed.

A different hash does not automatically mean malicious activity. Legitimate updates can also change files.

## 12.4 AIDE

AIDE stands for Advanced Intrusion Detection Environment.

It is a host-based file integrity monitoring tool.

On Debian-based systems:

```bash
sudo apt install aide
```

Initialize its database using the distribution's supported procedure:

```bash
sudo aideinit
```

Check the available commands and database locations for your installed version:

```bash
aide --help
```

AIDE compares current file states with a previously created baseline.

### Important limitation

If an attacker gains sufficient privileges, they may attempt to modify both monitored files and the integrity database.

Protect the baseline and its backups separately.

---

# 13. Log Collection and Monitoring

## 13.1 What are Linux logs?

Logs are records of events generated by the operating system, applications, and services.

They help administrators understand what happened on a system.

Logs can record:

- Login attempts.
- Authentication failures.
- Service activity.
- Application errors.
- System startup.
- Kernel events.
- Administrative actions.

## 13.2 Common log directory

The primary system log directory is:

```text
/var/log/
```

List its contents:

```bash
ls -lah /var/log/
```

## 13.3 Important log files

| File | Purpose |
|---|---|
| `/var/log/auth.log` | Authentication events on many Debian-based systems |
| `/var/log/syslog` | General system messages on many Debian-based systems |
| `/var/log/kern.log` | Kernel messages on systems that maintain this file |
| `/var/log/dpkg.log` | Package-management activity on Debian-based systems |
| `/var/log/boot.log` | Boot-related messages, where configured |

Not every distribution maintains all these files. Some use the systemd journal as the primary logging mechanism.

## 13.4 View logs

Display a log:

```bash
sudo cat /var/log/auth.log
```

Display the last 20 lines:

```bash
sudo tail -n 20 /var/log/auth.log
```

Monitor a log in real time:

```bash
sudo tail -f /var/log/auth.log
```

Search for a particular word:

```bash
sudo grep "Failed password" /var/log/auth.log
```

## 13.5 systemd journal

View system logs:

```bash
sudo journalctl
```

View logs from the current boot:

```bash
sudo journalctl -b
```

View SSH logs:

```bash
sudo journalctl -u ssh
```

Follow new log entries:

```bash
sudo journalctl -f
```

### Cybersecurity relevance

Log analysis helps identify suspicious behavior and reconstruct system activity during an investigation.

---

# 14. Audit Logs

## 14.1 What is system auditing?

System auditing is the process of recording and reviewing security-relevant events and system activities.

Auditing helps answer questions such as:

- Who accessed the system?
- When did an event occur?
- Which account performed an action?
- What files were modified?
- Which administrative operations were performed?

## 14.2 Linux audit framework

Linux commonly uses the audit subsystem through `auditd`.

Install it on Debian-based systems:

```bash
sudo apt install auditd audispd-plugins
```

Check service status:

```bash
sudo systemctl status auditd
```

Start the service:

```bash
sudo systemctl start auditd
```

Enable it at startup:

```bash
sudo systemctl enable auditd
```

## 14.3 View audit logs

The default audit log location is commonly:

```text
/var/log/audit/audit.log
```

View it:

```bash
sudo less /var/log/audit/audit.log
```

## 14.4 Audit rules

The `auditctl` command manages runtime audit rules.

View active rules:

```bash
sudo auditctl -l
```

Audit configuration files are commonly stored in:

```text
/etc/audit/
```

Persistent rules are often stored in:

```text
/etc/audit/rules.d/
```

### Important distinction

- System logs provide general information about system activity.
- Audit logs focus on configured security-relevant events and actions.

Audit coverage depends on the rules and system configuration.

---

# 15. Linux Capabilities

## 15.1 What are Linux capabilities?

Linux capabilities divide traditional root privileges into smaller, distinct permissions.

Instead of granting a process all root privileges, Linux can grant it only specific capabilities.

This supports the principle of least privilege.

## 15.2 Why are capabilities important?

Traditionally, the root user has extensive administrative privileges.

Linux capabilities allow more granular privilege control.

For example:

A network application may need permission to bind to a privileged network port without requiring unrestricted root privileges.

## 15.3 Common capabilities

| Capability | Purpose |
|---|---|
| CAP_NET_BIND_SERVICE | Bind to privileged network ports |
| CAP_NET_RAW | Use raw and packet sockets |
| CAP_NET_ADMIN | Perform network administration operations |
| CAP_SYS_ADMIN | Broad collection of administrative operations |
| CAP_CHOWN | Change file ownership |
| CAP_DAC_OVERRIDE | Bypass certain discretionary access checks |

## 15.4 View capabilities

Install libcap tools if needed:

```bash
sudo apt install libcap2-bin
```

Inspect capabilities of a file:

```bash
getcap /usr/bin/ping
```

Inspect process capabilities:

```bash
getpcaps PID
```

Replace `PID` with an actual process ID.

## 15.5 Set a capability

Example:

```bash
sudo setcap cap_net_bind_service=+ep ./server
```

This grants the specified capability to the executable.

Use this only in a controlled lab and understand the effect before applying it.

## 15.6 Security relevance

Incorrectly assigned capabilities may allow a process to perform operations beyond what its developers intended.

During security assessments, reviewing unusual file capabilities can reveal potential privilege-escalation risks.

---

# 16. AppArmor and SELinux

## 16.1 What is Mandatory Access Control?

Mandatory Access Control (MAC) is a security model in which access is restricted according to centrally enforced policies.

Traditional Linux file permissions use Discretionary Access Control (DAC).

MAC systems provide an additional layer of restrictions.

Two important Linux security systems are:

1. AppArmor.
2. SELinux.

## 16.2 AppArmor

AppArmor is a Linux security module that restricts what applications can access and do.

It uses application-specific security profiles.

Profiles can restrict:

- File access.
- Network operations.
- Capabilities.
- Application behavior.

Check AppArmor status:

```bash
sudo aa-status
```

List profile files:

```bash
ls /etc/apparmor.d/
```

AppArmor commonly supports these modes:

| Mode | Meaning |
|---|---|
| Enforce | Enforces the profile's restrictions |
| Complain | Records policy violations without enforcing them in the same way |

## 16.3 SELinux

SELinux stands for Security-Enhanced Linux.

It is a security architecture that provides Mandatory Access Control.

It uses security policies and labels to determine whether processes may access particular resources.

Check SELinux status:

```bash
getenforce
```

Possible results:

- Enforcing.
- Permissive.
- Disabled.

View detailed status:

```bash
sestatus
```

## 16.4 AppArmor vs SELinux

| Feature | AppArmor | SELinux |
|---|---|---|
| Security model | Mandatory Access Control | Mandatory Access Control |
| Policy approach | Path-based profiles | Label-based policies |
| Common use | Ubuntu and Debian-family environments | RHEL-family environments |
| Enforcement | Enforce and complain modes | Enforcing and permissive modes |

Both systems provide additional protection beyond ordinary file permissions.

Do not assume that both are active on every Linux distribution.

---

# 17. Secrets Management

## 17.1 What are secrets?

Secrets are sensitive pieces of information that provide access to systems, applications, or data.

Examples:

- Passwords.
- API keys.
- Database credentials.
- SSH private keys.
- Access tokens.
- Encryption keys.
- Cloud service credentials.

## 17.2 Why is secrets management important?

If secrets are exposed, attackers may gain unauthorized access to applications, databases, servers, or cloud infrastructure.

## 17.3 Common secrets-management mistakes

- Hardcoding passwords in source code.
- Uploading API keys to GitHub.
- Sharing private keys.
- Storing credentials in publicly accessible files.
- Logging sensitive tokens.
- Reusing credentials across applications.

## 17.4 Environment variables

Applications sometimes read credentials from environment variables.

Example:

```bash
export DATABASE_URL="example-connection-string"
```

Check a variable:

```bash
echo "$DATABASE_URL"
```

Environment variables can reduce hardcoding, but they are not automatically a secure secrets vault. They may be exposed through process inspection, logs, debugging, or misconfigured environments.

Avoid putting real secrets into shell history or shared terminals.

## 17.5 Secret-management best practices

- Use dedicated secrets-management systems when appropriate.
- Restrict access to credentials.
- Rotate compromised secrets.
- Avoid committing secrets to repositories.
- Keep private keys protected.
- Use separate credentials for development and production.
- Monitor access to important secrets.

---

# 18. Secure Backups

## 18.1 What is a backup?

A backup is a separate copy of data that can be used to restore information after deletion, corruption, system failure, or a security incident.

Backups protect against:

- Hardware failure.
- Accidental deletion.
- Ransomware.
- System compromise.
- Software failure.
- Configuration mistakes.

## 18.2 Types of backups

### Full backup

Copies all selected data.

### Incremental backup

Copies data changed since the previous backup.

### Differential backup

Copies data changed since the last full backup.

## 18.3 Important backup security practices

- Encrypt sensitive backups.
- Restrict backup access.
- Maintain multiple copies.
- Keep an offline or isolated copy.
- Test restoration regularly.
- Monitor backup failures.
- Protect backup credentials.
- Keep backup systems separate from ordinary user access.

## 18.4 The 3-2-1 backup rule

A common backup strategy recommends:

- 3 copies of important data.
- 2 different storage types.
- 1 copy stored off-site.

An additional offline or immutable copy provides stronger ransomware resilience.

## 18.5 Create a simple backup using tar

Create an archive:

```bash
tar -czvf backup.tar.gz ~/Documents/
```

Extract an archive:

```bash
tar -xzvf backup.tar.gz
```

List archive contents:

```bash
tar -tzvf backup.tar.gz
```

## 18.6 Backup with rsync

```bash
rsync -av ~/Documents/ /backup/Documents/
```

This copies and synchronizes the selected directory.

Remember that ordinary synchronization is not the same as a versioned backup. If files are deleted or corrupted at the source, those changes may propagate.

---

# 19. System Recovery

## 19.1 What is system recovery?

System recovery is the process of returning a Linux machine to a working and secure state after a failure or compromise.

Possible recovery situations include:

- Accidental file deletion.
- Failed system updates.
- Corrupted configuration.
- Boot failure.
- Malware infection.
- Unauthorized system modification.

## 19.2 Basic recovery process

1. Identify the problem.
2. Determine the affected systems and data.
3. Preserve relevant evidence if a security incident occurred.
4. Stop further damage.
5. Restore from a known-good backup or rebuild the system.
6. Apply required security updates.
7. Reset compromised credentials.
8. Validate system functionality.
9. Monitor the recovered system.

## 19.3 Recovery using backups

For example, extract a backup:

```bash
tar -xzvf backup.tar.gz
```

Before restoring files, confirm:

- The backup is trustworthy.
- It is not infected or compromised.
- The destination is correct.
- Existing files will not be overwritten unexpectedly.

## 19.4 Recovery after compromise

If a machine is suspected to be compromised:

- Isolate it where appropriate.
- Preserve forensic evidence.
- Investigate the cause.
- Rebuild from trusted installation media when necessary.
- Rotate exposed credentials and keys.
- Restore only verified data.
- Apply security updates.
- Review access and monitoring controls.

Simply deleting a suspicious file does not guarantee that a compromised system is clean.

---

# 20. Basic Incident-Response Workflow

## 20.1 What is incident response?

Incident response is a structured process used to identify, investigate, contain, and recover from cybersecurity incidents.

An incident may involve:

- Unauthorized access.
- Malware infection.
- Data theft.
- Privilege escalation.
- Suspicious network activity.
- System compromise.

## 20.2 Main stages of incident response

### 1. Preparation

Prepare the organization before an incident.

Examples:

- Maintain backups.
- Configure logging.
- Establish incident procedures.
- Prepare investigation tools.
- Define responsibilities.

### 2. Identification

Determine whether a security incident has occurred.

Examples:

- Unexpected login.
- Suspicious process.
- Unknown account.
- Unusual network connection.
- Unauthorized file modification.

### 3. Containment

Limit the incident's impact.

Examples:

- Isolate an affected machine.
- Restrict compromised accounts.
- Block malicious network connections.
- Preserve evidence.

### 4. Eradication

Remove the cause of the incident.

Examples:

- Remove malware.
- Close exploited vulnerabilities.
- Remove unauthorized persistence.
- Correct misconfigurations.

### 5. Recovery

Return systems to normal operation.

Examples:

- Restore clean backups.
- Rebuild systems.
- Reset credentials.
- Verify system integrity.

### 6. Lessons Learned

Review the incident.

Identify:

- What happened?
- How did it happen?
- What was affected?
- Which controls failed?
- What should be improved?

## 20.3 Incident-response diagram

```text
Preparation
    |
    v
Identification
    |
    v
Containment
    |
    v
Eradication
    |
    v
Recovery
    |
    v
Lessons Learned
```

Real incidents may require revisiting earlier stages as new evidence appears.

---

# 21. Indicators of Compromise

## 21.1 What is an Indicator of Compromise?

An Indicator of Compromise (IOC) is an observable sign that may indicate a system or network has been compromised.

An IOC does not automatically prove that an attack occurred. It provides evidence that should be investigated.

## 21.2 Common Linux IOCs

### Suspicious processes

Unknown or unexpected processes.

Check running processes:

```bash
ps aux
```

### Unusual network connections

Check active network connections:

```bash
sudo ss -tunap
```

### Unexpected listening ports

```bash
sudo ss -tulnp
```

### Suspicious login activity

```bash
sudo grep "Failed password" /var/log/auth.log
```

### Unknown users

```bash
cat /etc/passwd
```

### Unexpected scheduled tasks

```bash
sudo crontab -l
```

Also inspect:

```bash
ls -la /etc/cron.d/
```

### Unexpected SSH keys

Review:

```bash
cat ~/.ssh/authorized_keys
```

Only inspect accounts you are authorized to investigate.

### Unexpected file modifications

Compare important files against trusted integrity baselines.

## 21.3 Other indicators

- Unexpected administrative accounts.
- Modified system binaries.
- Unusual CPU or memory consumption.
- Unexpected outbound connections.
- Unknown services.
- Suspicious authentication activity.
- Unusual startup entries.

## 21.4 Investigating an IOC

When you identify a possible IOC:

1. Record the observation.
2. Note the time and affected system.
3. Collect supporting evidence.
4. Compare against expected system behavior.
5. Determine whether the activity is authorized.
6. Escalate or contain if necessary.

---

# 22. Persistence Mechanisms

## 22.1 What is persistence?

Persistence is the ability of a program, attacker, or unauthorized process to maintain access to a system across events such as logout or reboot.

Attackers may use persistence mechanisms to regain access after an initial compromise.

Understanding persistence is important for defensive security and incident response.

## 22.2 Common Linux persistence locations

### Cron jobs

Cron runs scheduled tasks.

Inspect the current user's scheduled jobs:

```bash
crontab -l
```

Inspect root's scheduled jobs:

```bash
sudo crontab -l
```

Inspect system-wide scheduled tasks:

```bash
ls -la /etc/cron.d/
```

Also review:

```bash
cat /etc/crontab
```

### systemd services

Services may be configured to start automatically.

List enabled services:

```bash
systemctl list-unit-files --type=service --state=enabled
```

Inspect a service:

```bash
systemctl cat SERVICE_NAME
```

### SSH authorized keys

Review authorized public keys:

```bash
cat ~/.ssh/authorized_keys
```

Unexpected keys may indicate unauthorized access.

### Shell startup files

Common user-level startup files include:

```text
~/.bashrc
~/.profile
~/.bash_profile
```

Review them for unexpected commands.

### System startup configuration

System-wide configuration may exist in:

```text
/etc/systemd/system/
/etc/rc.local
```

The exact startup mechanisms available vary by distribution.

## 22.3 Defensive persistence analysis

When investigating suspicious persistence:

- Record file paths and timestamps.
- Identify file ownership.
- Inspect the associated command.
- Identify the user or service account.
- Determine whether the configuration is legitimate.
- Compare against known-good baselines.
- Preserve evidence before modifying the system.

Do not delete unfamiliar entries without investigating their purpose.

---

# 23. Privilege Escalation Concepts and Common Misconfigurations

## 23.1 What is privilege escalation?

Privilege escalation occurs when a user or process gains permissions beyond those originally assigned.

There are two main types.

### Vertical privilege escalation

A user gains a higher privilege level.

Example:

A normal user gains root privileges.

### Horizontal privilege escalation

A user gains access to another account or resource at a similar privilege level.

Example:

One ordinary user gains unauthorized access to another ordinary user's files.

## 23.2 Common privilege-escalation weaknesses

### Excessive sudo permissions

A user may be permitted to execute powerful commands unnecessarily.

Inspect sudo permissions:

```bash
sudo -l
```

### Weak file permissions

Sensitive files may be readable or writable by unauthorized users.

Inspect permissions:

```bash
ls -l FILE_NAME
```

### Unsafe SUID executables

SUID programs may execute with the effective privileges of their owner.

List files with SUID permission:

```bash
find / -type f -perm -4000 2>/dev/null
```

Investigate unexpected entries carefully.

### Unsafe capabilities

Executables may have capabilities that grant unnecessary privileges.

List file capabilities:

```bash
getcap -r / 2>/dev/null
```

### Writable system configuration

Important system configuration or service files may be writable by unauthorized users.

Inspect their permissions and ownership.

### Vulnerable services

An outdated or misconfigured service may allow unauthorized users to gain higher privileges.

Review:

- Software versions.
- Service ownership.
- Service configuration.
- File permissions.
- Network exposure.

## 23.3 Why privilege escalation matters

Privilege escalation can allow an attacker to move from limited access to administrative control.

This may lead to:

- Sensitive data exposure.
- Unauthorized account creation.
- System modification.
- Security-control bypass.
- Long-term persistence.

## 23.4 Defensive assessment commands

```bash
# Current identity
id

# Current user
whoami

# Current sudo permissions
sudo -l

# SUID files
find / -type f -perm -4000 2>/dev/null

# File capabilities
getcap -r / 2>/dev/null

# Running services
systemctl list-units --type=service --state=running

# Listening ports
sudo ss -tulnp
```

These commands support authorized security assessment. Their results require interpretation; an unusual entry is not automatically exploitable.

---

# 24. Security Baselines and Hardening Checklists

## 24.1 What is a security baseline?

A security baseline is a documented set of minimum security configurations and practices that a system should follow.

It provides a standard against which system security can be assessed.

## 24.2 Why are baselines important?

They help:

- Maintain consistent security.
- Reduce configuration mistakes.
- Identify deviations.
- Improve auditing.
- Support compliance.
- Simplify system maintenance.

## 24.3 Linux security baseline

### User security

- Remove unnecessary accounts.
- Review group memberships.
- Restrict sudo privileges.
- Disable unused accounts.
- Use separate administrative accounts where appropriate.

### File security

- Protect sensitive files.
- Review file ownership.
- Remove unnecessary write permissions.
- Protect SSH private keys.
- Monitor important configuration files.

### Network security

- Enable an appropriate firewall.
- Restrict unnecessary listening ports.
- Disable unused network services.
- Restrict remote administration.

### Authentication security

- Use strong authentication.
- Protect SSH keys.
- Review authentication logs.
- Restrict direct root access.
- Apply suitable password policies.

### System security

- Apply security updates.
- Review running services.
- Use AppArmor or SELinux where supported.
- Monitor system logs.
- Maintain secure backups.

### Monitoring

- Review failed login attempts.
- Monitor administrative actions.
- Maintain integrity baselines.
- Investigate suspicious processes.
- Document security findings.

## 24.4 CIS Benchmarks

CIS Benchmarks are security configuration recommendations published by the Center for Internet Security.

They provide detailed guidance for hardening operating systems, applications, and infrastructure.

Reference:

https://www.cisecurity.org/cis-benchmarks

Another useful reference is the Linux security guidance from distribution vendors and the NIST security configuration resources.

---

# 25. Important Configuration and Log Locations

## 25.1 Configuration locations

| Path | Purpose |
|---|---|
| `/etc/ssh/` | SSH configuration and host keys |
| `/etc/sudoers` | sudo policy |
| `/etc/sudoers.d/` | Additional sudo policy files |
| `/etc/hosts` | Local hostname mappings |
| `/etc/resolv.conf` | DNS resolver configuration or managed resolver state |
| `/etc/passwd` | User account information |
| `/etc/shadow` | Password hashes and aging information |
| `/etc/group` | Group information |
| `/etc/systemd/` | systemd configuration |
| `/etc/cron.d/` | System-wide scheduled jobs |
| `/etc/crontab` | System-wide cron configuration |
| `/etc/pam.d/` | PAM authentication configuration |
| `/etc/audit/` | Audit configuration |
| `/etc/apparmor.d/` | AppArmor profiles |

## 25.2 Log locations

| Path | Purpose |
|---|---|
| `/var/log/` | Main system log directory |
| `/var/log/auth.log` | Authentication events on many Debian-based systems |
| `/var/log/syslog` | General system logs on many Debian-based systems |
| `/var/log/kern.log` | Kernel messages where configured |
| `/var/log/audit/audit.log` | Audit events |
| `/var/log/dpkg.log` | Package-management records |

## 25.3 Important system inspection commands

```bash
# User information
id
whoami
groups

# User database
getent passwd

# Group database
getent group

# sudo permissions
sudo -l

# Running services
systemctl list-units --type=service --state=running

# Listening network sockets
sudo ss -tulnp

# Current firewall rules
sudo ufw status verbose

# SSH configuration validation
sudo sshd -t

# Authentication logs
sudo journalctl -u ssh

# Current boot logs
sudo journalctl -b
```

### Important note about /etc/resolv.conf

On modern Linux systems, DNS configuration may be managed by NetworkManager, systemd-resolved, or another network-management service.

Therefore, `/etc/resolv.conf` may be a symbolic link or a generated file.

Inspect it with:

```bash
ls -l /etc/resolv.conf
```

For systemd-resolved:

```bash
resolvectl status
```

Do not blindly edit a generated resolver configuration file.

---

# 26. Practical Linux Security Assessment

## Objective

Perform a basic security review of your own Kali Linux or another Linux virtual machine.

You will inspect system configuration, accounts, permissions, services, firewall settings, updates, and logs.

## Step 1: Identify the system

```bash
hostnamectl
uname -a
whoami
id
```

Record:

- Hostname.
- Operating system.
- Kernel version.
- Current username.
- User and group IDs.

## Step 2: Review user security

```bash
getent passwd
getent group sudo
sudo -l
```

Identify:

- Unnecessary accounts.
- Users with administrative access.
- Unexpected group memberships.

Do not expose password hashes or sensitive account information in your report.

## Step 3: Review sensitive file permissions

```bash
ls -l /etc/passwd
ls -l /etc/shadow
ls -l /etc/sudoers
ls -ld /etc/ssh
```

Check whether permissions and ownership are appropriate.

## Step 4: Review sudo configuration

```bash
sudo visudo -c
```

Inspect sudo access:

```bash
sudo -l
```

Identify overly broad privileges.

## Step 5: Check security updates

```bash
sudo apt update
apt list --upgradable
```

Record the number and names of relevant pending updates.

Do not perform a full upgrade until you have reviewed the proposed changes and considered the VM's recovery options.

## Step 6: Review running services

```bash
systemctl list-units --type=service --state=running
```

Identify services that are unnecessary for the VM's intended purpose.

## Step 7: Review network exposure

```bash
sudo ss -tulnp
```

Record:

- Listening port.
- Protocol.
- Associated process.
- Whether the service is required.

## Step 8: Review firewall configuration

```bash
sudo ufw status verbose
```

If UFW is not installed or another firewall framework is in use, document that instead.

## Step 9: Review SSH security

```bash
sudo sshd -t
```

Inspect relevant directives in:

```bash
sudo grep -E '^(Port|PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|AllowUsers)' /etc/ssh/sshd_config
```

Note: Settings may also be supplied through included configuration files, so this command is not a complete representation of every effective SSH setting.

## Step 10: Review authentication logs

On Kali or other Debian-based systems:

```bash
sudo tail -n 50 /var/log/auth.log
```

Or:

```bash
sudo journalctl -u ssh --since today
```

Look for unexpected login activity and repeated failures.

## Step 11: Review scheduled tasks

```bash
crontab -l
sudo crontab -l
ls -la /etc/cron.d/
cat /etc/crontab
```

Investigate unfamiliar scheduled jobs.

## Step 12: Review file integrity

Create a baseline hash for a test file:

```bash
sha256sum /etc/hosts > hosts-baseline.txt
```

Recalculate it later:

```bash
sha256sum /etc/hosts
```

Compare the results.

## Step 13: Document findings

Create a report containing:

1. System information.
2. Users and groups reviewed.
3. Sensitive file permissions.
4. sudo configuration findings.
5. Pending updates.
6. Running services.
7. Listening ports.
8. Firewall configuration.
9. SSH security settings.
10. Authentication log observations.
11. Scheduled task observations.
12. Recommendations.

---

# 27. Hands-on Lab Exercises

Complete these exercises using your own Kali Linux VM.

## Lab 1: User and Group Security

**Objective:** Create a test user and a group.

```bash
sudo adduser labuser
sudo groupadd securitylab
sudo usermod -aG securitylab labuser
groups labuser
```

Verify that the group membership is correct.

## Lab 2: File Permissions

**Objective:** Understand Linux permissions.

```bash
touch secret.txt
chmod 600 secret.txt
ls -l secret.txt
```

Change permissions:

```bash
chmod 644 secret.txt
ls -l secret.txt
```

Explain the difference between these two permission settings.

## Lab 3: sudo Security

**Objective:** Inspect sudo permissions.

```bash
sudo -l
sudo visudo -c
```

Identify which commands the current user can run with elevated privileges.

## Lab 4: Patch Management

**Objective:** Identify available updates.

```bash
sudo apt update
apt list --upgradable
```

Record packages with pending updates.

## Lab 5: Service Hardening

**Objective:** Identify unnecessary services.

```bash
systemctl list-units --type=service --state=running
```

Choose one service you understand and confirm whether it is required.

Do not disable essential services.

## Lab 6: Firewall Configuration

**Objective:** Learn basic firewall management.

```bash
sudo ufw status
sudo ufw status verbose
```

In an isolated VM, configure a test firewall rule only after checking how you will retain access.

## Lab 7: SSH Hardening Review

**Objective:** Inspect SSH server security.

```bash
sudo sshd -t
sudo grep -E '^(Port|PermitRootLogin|PasswordAuthentication|PubkeyAuthentication)' /etc/ssh/sshd_config
```

Compare the settings with the hardening recommendations in Phase 9.

## Lab 8: Authentication Log Analysis

**Objective:** Identify SSH login activity.

```bash
sudo grep -E 'Accepted|Failed password|Invalid user' /var/log/auth.log
```

If the file is unavailable, use:

```bash
sudo journalctl -u ssh
```

Record successful and unsuccessful authentication events.

## Lab 9: File Integrity Monitoring

**Objective:** Detect changes to a test file.

```bash
echo "Original content" > integrity-test.txt
sha256sum integrity-test.txt > integrity-baseline.txt
```

Modify the file:

```bash
echo "Modified content" >> integrity-test.txt
```

Calculate its hash again:

```bash
sha256sum integrity-test.txt
```

Compare it with the original baseline.

## Lab 10: Persistence Mechanism Review

**Objective:** Review scheduled jobs and services.

```bash
crontab -l
sudo crontab -l
systemctl list-unit-files --type=service --state=enabled
```

Identify unfamiliar entries and investigate their purpose.

## Lab 11: Linux Capabilities Review

**Objective:** Identify file capabilities.

```bash
getcap -r /usr/bin /usr/sbin 2>/dev/null
```

Select a few results and explain what the assigned capabilities permit.

## Lab 12: Basic Security Assessment

**Objective:** Perform a complete security review of your VM.

Use the commands from Section 26.

Prepare a short report listing:

- At least five observations.
- At least three security recommendations.
- Any configuration requiring further investigation.

---

# 28. Interview Questions and Answers

## Q1. What is Linux security?

Linux security refers to mechanisms and practices that protect Linux systems, users, applications, and data against unauthorized access and malicious activity.

## Q2. What is the principle of least privilege?

It means giving each user, process, and application only the minimum permissions required to perform its intended task.

## Q3. What is the difference between a user and a group?

A user represents an account, while a group is a collection of users used to simplify permission management.

## Q4. What is the purpose of /etc/passwd?

It stores basic Linux user account information, such as usernames, UIDs, GIDs, home directories, and login shells.

## Q5. What is /etc/shadow?

It stores password hashes and password-aging information. Access is restricted because it contains sensitive authentication data.

## Q6. What is sudo?

sudo allows authorized users to execute commands with elevated privileges according to configured policies.

## Q7. Why should we use visudo?

`visudo` safely edits sudoers configuration and checks its syntax before saving changes.

## Q8. What is patch management?

Patch management is the process of identifying, testing, and installing updates to fix vulnerabilities, bugs, and software problems.

## Q9. What is service hardening?

Service hardening means configuring services to reduce unnecessary functionality, privileges, and exposure.

## Q10. Why should unnecessary services be disabled?

Unnecessary services can increase the attack surface and introduce avoidable security risks.

## Q11. What is a firewall?

A firewall controls network traffic according to predefined security rules.

## Q12. What is UFW?

UFW stands for Uncomplicated Firewall. It provides a simplified interface for managing Linux firewall rules.

## Q13. What is SSH hardening?

SSH hardening involves securing remote access by strengthening authentication, restricting users, protecting keys, and monitoring login activity.

## Q14. What is PAM?

PAM stands for Pluggable Authentication Modules. It provides a flexible framework for Linux authentication and account-management policies.

## Q15. What is File Integrity Monitoring?

FIM detects changes to important files and helps identify unauthorized modifications.

## Q16. What is AIDE?

AIDE is an open-source file integrity monitoring tool that compares system files against a stored baseline.

## Q17. What is the difference between system logs and audit logs?

System logs record general operating-system and application activity. Audit logs record security-relevant events according to configured audit rules.

## Q18. What are Linux capabilities?

Linux capabilities divide traditional root privileges into smaller permissions that can be assigned to processes.

## Q19. What is AppArmor?

AppArmor is a Linux security module that restricts application behavior using security profiles.

## Q20. What is SELinux?

SELinux is a security architecture that provides Mandatory Access Control through security policies and labels.

## Q21. What is secrets management?

Secrets management is the secure storage, distribution, access control, and rotation of sensitive credentials and keys.

## Q22. What is an IOC?

An Indicator of Compromise is an observable sign that may suggest a system or network has been compromised.

## Q23. What is persistence?

Persistence is a technique that allows a program or attacker to maintain access to a system across events such as logout or reboot.

## Q24. What is privilege escalation?

Privilege escalation occurs when a user or process obtains permissions beyond those originally assigned.

## Q25. What is vertical privilege escalation?

It occurs when a user gains a higher privilege level, such as moving from an ordinary account to root.

## Q26. What is horizontal privilege escalation?

It occurs when a user gains unauthorized access to another account or resource at a similar privilege level.

## Q27. What is a security baseline?

A security baseline is a documented set of minimum security configurations and practices used to assess and harden a system.

## Q28. What is the purpose of secure backups?

Secure backups allow organizations to restore data and systems after accidental deletion, hardware failure, ransomware, or other incidents.

## Q29. What is incident response?

Incident response is the structured process of preparing for, identifying, containing, eradicating, and recovering from cybersecurity incidents.

## Q30. How can you identify unnecessary listening services?

Use:

```bash
sudo ss -tulnp
```

Then investigate the associated processes and determine whether each service is required.

---

# 29. Quick Revision

## Important Concepts

| Concept | Meaning |
|---|---|
| Least Privilege | Minimum required permissions |
| User Security | Protecting individual accounts |
| Group Security | Managing shared access |
| File Permissions | Controlling read, write, and execute access |
| sudo | Controlled administrative access |
| Patch Management | Applying software and security updates |
| Service Hardening | Reducing service attack surface |
| Firewall | Controlling network traffic |
| SSH Hardening | Securing remote administration |
| PAM | Authentication framework |
| FIM | Monitoring file modifications |
| Audit Logs | Recording security-relevant events |
| Capabilities | Fine-grained Linux privileges |
| AppArmor | Profile-based mandatory access control |
| SELinux | Label-based mandatory access control |
| Secrets Management | Protecting sensitive credentials |
| Secure Backup | Protecting recoverable copies of data |
| Incident Response | Handling cybersecurity incidents |
| IOC | Indicator of Compromise |
| Persistence | Maintaining access across sessions or reboots |
| Privilege Escalation | Gaining additional permissions |
| Security Baseline | Minimum security configuration standard |

## Essential Commands

```bash
# User and group security
id
whoami
groups
getent passwd
getent group sudo
sudo -l

# File permissions
ls -l
chmod 600 secret.txt
chown user:group file.txt

# sudo configuration
sudo visudo
sudo visudo -c

# Patch management
sudo apt update
apt list --upgradable
sudo apt upgrade

# Service management
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service
sudo systemctl status ssh

# Network and firewall
sudo ss -tulnp
sudo ufw status verbose
sudo nft list ruleset

# SSH security
sudo sshd -t
sudo journalctl -u ssh

# Authentication logs
sudo tail -f /var/log/auth.log
sudo grep "Failed password" /var/log/auth.log

# File integrity
sha256sum /etc/hosts

# Audit
sudo auditctl -l

# AppArmor and SELinux
sudo aa-status
getenforce
sestatus

# Linux capabilities
getcap -r /usr/bin /usr/sbin 2>/dev/null

# Persistence review
crontab -l
sudo crontab -l
systemctl list-unit-files --type=service --state=enabled

# Privilege escalation assessment
find / -type f -perm -4000 2>/dev/null
getcap -r / 2>/dev/null
```

## Final Learning Checklist

- [ ] Understand the principle of least privilege.
- [ ] Manage Linux users and groups securely.
- [ ] Understand file permissions and ownership.
- [ ] Identify sensitive Linux configuration files.
- [ ] Inspect sudo permissions safely.
- [ ] Understand patch management.
- [ ] Identify and harden running services.
- [ ] Identify unnecessary services.
- [ ] Understand UFW and nftables.
- [ ] Apply basic SSH hardening.
- [ ] Understand password policies and PAM.
- [ ] Explain file integrity monitoring.
- [ ] Analyze system and authentication logs.
- [ ] Understand Linux audit logs.
- [ ] Explain Linux capabilities.
- [ ] Understand AppArmor and SELinux.
- [ ] Apply basic secrets-management practices.
- [ ] Create and verify backups.
- [ ] Understand system recovery.
- [ ] Explain the incident-response workflow.
- [ ] Recognize common indicators of compromise.
- [ ] Identify common Linux persistence locations.
- [ ] Understand privilege-escalation concepts.
- [ ] Apply a basic Linux security baseline.
- [ ] Complete and document a security assessment of your own VM.

---

# Further Reading

1. Linux Security Documentation: https://docs.kernel.org/admin-guide/
2. OpenSSH Manual: https://www.openssh.com/manual.html
3. AppArmor Documentation: https://documentation.ubuntu.com/server/how-to/security/apparmor/
4. SELinux Project: https://github.com/SELinuxProject
5. AIDE Documentation: https://aide.github.io/
6. Linux Audit Documentation: https://github.com/linux-audit/audit-userspace
7. CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks
8. NIST Cybersecurity Resources: https://www.nist.gov/cybersecurity

**End of Phase 9 — Linux Security Essentials**
