
# Phase 3 — Linux Permissions and Users

## Table of Contents

1. Introduction to Linux Users and Permissions
2. Linux Users and Groups
3. Root User and Regular Users
4. Identifying Users — `whoami`, `id`, `who`, `groups`
5. Administrative Privileges — `sudo`
6. Switching Users — `su`
7. User Management — `useradd` and `usermod`
8. Password Management — `passwd`
9. Group Management — `groupadd`
10. Read, Write, and Execute Permissions
11. Linux Permission Representation
12. Numeric Permissions — `644`, `755`, `700`
13. Symbolic Permissions — `u`, `g`, `o`, `a`
14. File Permissions vs Directory Permissions
15. Changing Permissions — `chmod`
16. Changing Ownership — `chown`
17. Changing Group Ownership — `chgrp`
18. Default Permissions — `umask`
19. Special Permissions — SUID, SGID, Sticky Bit
20. Linux Access Control Lists (ACLs)
21. Linux Account Files
22. Principle of Least Privilege
23. Safe Use of sudo
24. Practical Linux Labs
25. Cybersecurity Relevance
26. Common Mistakes
27. Quick Revision
28. Interview and Self-Assessment Questions
29. Learning Checklist

---

# 1. Introduction to Linux Users and Permissions

Linux is a multi-user operating system. It allows multiple users to access and use the same computer system while maintaining separate accounts, files, and permissions.

However, every user should not have unrestricted access to the entire system.

Linux uses a permission and ownership mechanism to control access to files, directories, and system resources.

For example:

Suppose a Linux system has three users:

- Alice
- Bob
- Charlie

Alice creates a private file named `secret.txt`.

Linux should be able to prevent Bob and Charlie from reading or modifying that file if Alice does not want them to access it.

This is achieved through Linux users, groups, ownership, and permissions.

## 1.1 Why Are Linux Permissions Important?

Linux permissions are important for:

1. Protecting sensitive information.
2. Preventing unauthorized access.
3. Managing multiple users.
4. Controlling access to files and directories.
5. Securing applications and services.
6. Preventing unauthorized modifications.
7. Managing administrative privileges.
8. Maintaining system security.

## 1.2 Basic Linux Permission Model

Linux associates three important properties with files and directories:

| Property | Description |
|---|---|
| Owner | User who owns the file or directory. |
| Group | Group associated with the file or directory. |
| Others | Everyone else who is neither the owner nor a member of the associated group. |

Each category can receive different permissions.

Example:

```bash
ls -l
```

Possible output:

```text
-rwxr-xr-- 1 alice developers 1200 Nov 11 10:00 script.sh
```

This means:

- Owner (`alice`): Read, write, execute.
- Group (`developers`): Read and execute.
- Others: Read only.

---

# 2. Linux Users and Groups

## 2.1 What Are Linux Users?

A Linux user is an account that allows an individual, application, or service to interact with the operating system.

Every Linux user has a unique numerical identifier called a UID (User ID).

Linux internally uses this numerical ID to identify users and determine ownership and access permissions.

For example:

```bash
whoami
```

Output:

```text
pulok
```

The current effective username is `pulok`.

## 2.2 Types of Linux Users

Linux accounts can generally be classified into three categories.

### 1. Root User

The root user is the superuser of Linux.

- UID is always `0`.
- Has extensive administrative privileges.
- Can manage other users.
- Can modify protected system files.
- Can install and remove system packages.
- Can manage system services.

### 2. Regular Users

Regular users are normal accounts used by people to interact with Linux.

- Usually have UIDs starting at 1000 on modern Debian-based systems.
- Have restricted administrative privileges.
- Can manage their own files.
- Can execute permitted programs.
- Can access shared resources according to permissions.

### 3. System Users

System users are accounts generally created for running system services and applications.

Examples:

| System User | Common Purpose |
|---|---|
| `www-data` | Web server processes |
| `mysql` | MySQL database service |
| `postgres` | PostgreSQL database service |
| `sshd` | SSH-related service operations, depending on configuration |

System users help isolate applications and services from ordinary human accounts.

## 2.3 What Are Linux Groups?

A group is a collection of users.

Groups simplify permission management because administrators can assign permissions to a group rather than configuring access separately for every user.

Example:

Suppose a company has three developers:

- Alice
- Bob
- Charlie

The administrator creates a group named `developers`.

All three users are added to the group.

The administrator can then give the group access to a shared project directory.

## 2.4 Types of Group Membership

### Primary Group

Every user has a primary group.

It is the default group associated with the user's processes and normally determines the group ownership of newly created files, subject to directory settings and other mechanisms.

### Supplementary Groups

A user can belong to additional groups.

These provide additional access to system resources.

Example:

```bash
groups alice
```

Possible output:

```text
alice : alice sudo developers
```

Alice belongs to:

- `alice` — Primary group.
- `sudo` — Supplementary group.
- `developers` — Supplementary group.

## 2.5 UID and GID

| Term | Full Form | Purpose |
|---|---|---|
| UID | User ID | Identifies a user. |
| GID | Group ID | Identifies a group. |
| EUID | Effective User ID | Identity used for many permission checks. |
| EGID | Effective Group ID | Effective group identity used for many permission checks. |

Linux uses numerical IDs internally rather than relying exclusively on usernames and group names.

---

# 3. Root User and Regular Users

## 3.1 What Is the Root User?

The root user is the most privileged account in Linux.

Its UID is `0`.

Root can perform administrative operations that ordinary users cannot normally perform.

Examples:

```bash
# Install software
apt install nginx

# Modify system configuration
nano /etc/hosts

# Create a user
useradd testuser

# Restart a system service
systemctl restart ssh
```

These operations normally require administrative privileges.

## 3.2 What Is a Regular User?

A regular user operates with restricted privileges.

A regular user can generally:

- Create files in permitted directories.
- Modify their own files.
- Execute permitted programs.
- Access authorized shared resources.
- Run administrative commands through sudo if authorized.

A regular user cannot automatically:

- Modify `/etc/passwd`.
- Modify `/etc/shadow`.
- Install system-wide packages.
- Change another user's password.
- Modify protected system services.

## 3.3 Root vs Regular User

| Feature | Root | Regular User |
|---|---|---|
| UID | 0 | Usually 1000 or above |
| Administrative access | Extensive | Restricted |
| Modify protected system files | Generally yes | Requires authorization |
| Create users | Yes | Requires authorization |
| Install packages | Yes | Usually requires sudo |
| Access protected files | Generally yes | Depends on permissions |
| Security impact if compromised | Very high | Usually more limited |

## 3.4 Why Is Running Everything as Root Dangerous?

Running all commands as root increases the impact of mistakes and malicious programs.

Consider:

```bash
rm -rf /some/directory
```

A regular user might not have permission to delete protected files.

Root can generally bypass ordinary discretionary permission checks.

Risks include:

1. Accidental deletion of important files.
2. Modification of critical configurations.
3. Execution of malicious programs with elevated privileges.
4. Increased damage from software vulnerabilities.
5. Easier access to sensitive system resources.

**Best practice:** Use a regular account for daily activities and obtain administrative privileges only when necessary.

---

# 4. Identifying the Current User

Linux provides several commands to identify users and groups.

## 4.1 whoami

### What Is whoami?

The `whoami` command displays the effective username associated with the current process.

Syntax:

```bash
whoami
```

Example:

```bash
whoami
```

Output:

```text
pulok
```

This means the effective user is `pulok`.

### Practical Uses

- Checking which user is running a command.
- Verifying a user switch.
- Checking whether you are root.
- Troubleshooting permission problems.

Example:

```bash
sudo whoami
```

Output:

```text
root
```

This demonstrates that sudo executed the command with root privileges.

## 4.2 id

### What Is id?

The `id` command displays UID, GID, and group membership information.

Syntax:

```bash
id
```

Example:

```bash
id
```

Possible output:

```text
uid=1000(pulok) gid=1000(pulok) groups=1000(pulok),27(sudo)
```

Explanation:

| Output | Meaning |
|---|---|
| `uid=1000` | User ID is 1000. |
| `pulok` | Username. |
| `gid=1000` | Primary group ID. |
| `groups=` | Group membership information. |
| `27(sudo)` | Membership in the sudo group. |

### Important Options

Display another user's identity:

```bash
id alice
```

Display only the UID:

```bash
id -u
```

Display only the primary GID:

```bash
id -g
```

Display supplementary group IDs:

```bash
id -G
```

Display group names:

```bash
id -Gn
```

## 4.3 who

### What Is who?

The `who` command displays information about users currently logged into the system.

Syntax:

```bash
who
```

Possible output:

```text
pulok    tty2    2026-11-11 09:30
```

Explanation:

| Field | Meaning |
|---|---|
| pulok | Logged-in username |
| tty2 | Terminal session |
| Date | Login date |
| Time | Login time |

### Important Options

```bash
who -a
```

Displays additional login-related information.

```bash
who -b
```

Displays the last system boot time.

```bash
who -q
```

Displays logged-in usernames and a count.

## 4.4 groups

### What Is groups?

The `groups` command displays the groups to which a user belongs.

Syntax:

```bash
groups
```

Example:

```bash
groups
```

Output:

```text
pulok sudo developers
```

Check another user:

```bash
groups alice
```

Possible output:

```text
alice : alice developers
```

## 4.5 Difference Between These Commands

| Command | Purpose |
|---|---|
| `whoami` | Displays effective username. |
| `id` | Displays UID, GID, and group information. |
| `who` | Displays logged-in users. |
| `groups` | Displays group memberships. |

---

# 5. sudo — Administrative Privileges

## 5.1 What Is sudo?

`sudo` stands for **Superuser Do**.

It allows an authorized user to execute a command with elevated privileges or as another specified user.

Instead of continuously logging in as root, a regular user can execute individual administrative commands.

Example:

```bash
sudo apt update
```

This executes the package-list update with administrative privileges.

## 5.2 How Does sudo Work?

The general process is:

1. A user requests administrative execution.
2. sudo identifies the requesting user.
3. sudo checks the configured authorization policy.
4. Authentication may be required.
5. The requested command executes using the permitted target identity.
6. The action may be recorded in system logs.

The default target user is normally root.

## 5.3 Basic Syntax

```bash
sudo command
```

Examples:

```bash
sudo apt update
sudo apt install nginx
sudo systemctl restart ssh
sudo nano /etc/hosts
```

## 5.4 Important sudo Options

| Option | Purpose |
|---|---|
| `-u` | Execute as another user. |
| `-i` | Start a login shell as the target user. |
| `-s` | Start a shell using the target user identity. |
| `-l` | List permitted commands. |
| `-k` | Invalidate cached authentication credentials. |
| `-v` | Refresh authentication credentials. |

### Execute a command as another user

```bash
sudo -u alice whoami
```

Output:

```text
alice
```

### Start a root login shell

```bash
sudo -i
```

Verify:

```bash
whoami
```

Output:

```text
root
```

Exit:

```bash
exit
```

### Check sudo permissions

```bash
sudo -l
```

This displays the commands the current user is permitted to execute through sudo.

## 5.5 sudo Group

On Debian-based distributions such as Kali and Ubuntu, users belonging to the `sudo` group are commonly authorized to use sudo.

Check membership:

```bash
groups
```

Add a user to the sudo group:

```bash
sudo usermod -aG sudo alice
```

Verify:

```bash
id alice
```

The user generally needs to start a new login session before the new supplementary group membership becomes active.

## 5.6 sudoers Configuration

The sudoers file defines sudo permissions and policies.

Main configuration file:

```text
/etc/sudoers
```

Additional configuration directory:

```text
/etc/sudoers.d/
```

Use `visudo` to edit the configuration:

```bash
sudo visudo
```

`visudo` checks the syntax before installing the modified configuration.

Example rule:

```text
alice ALL=(ALL:ALL) ALL
```

Explanation:

| Part | Meaning |
|---|---|
| `alice` | User |
| First `ALL` | All hosts |
| `(ALL:ALL)` | Any permitted user and group identity |
| Last `ALL` | Any command |

The complete sudoers policy determines the actual authorization.

### Security Best Practices

- Give sudo access only to trusted users.
- Avoid unnecessary unrestricted privileges.
- Never execute unknown scripts with sudo.
- Inspect commands before running them.
- Use `visudo` for configuration changes.
- Prefer individual administrative commands instead of permanent root sessions.

---

# 6. su — Switching Users

## 6.1 What Is su?

`su` stands for **Substitute User**.

It allows a user to switch to another account.

If no username is supplied, it normally attempts to switch to root.

Syntax:

```bash
su [options] [username]
```

Example:

```bash
su alice
```

This switches to the Alice account after successful authentication.

## 6.2 Switch to Root

```bash
su
```

On many distributions, this asks for the root account password.

## 6.3 Switch to Root With a Login Environment

```bash
su -
```

The `-` option requests a login shell.

It loads the target user's login environment and normally changes to the target user's home directory.

## 6.4 Switch to Another User With a Login Environment

```bash
su - alice
```

## 6.5 Exit the Switched Account

```bash
exit
```

## 6.6 Difference Between sudo and su

| Feature | sudo | su |
|---|---|---|
| Full form | Superuser Do | Substitute User |
| Main purpose | Execute authorized commands as another user | Switch to another user |
| Authentication | Usually requesting user's password | Usually target user's password |
| Default target | root | root |
| Single command | Yes | Possible using `-c` |
| Administrative policy | sudoers | Account authentication and system policies |

Examples:

```bash
sudo apt update
```

Executes one administrative command.

```bash
su -
```

Starts a root login shell.

**Kali Linux note:** Kali commonly provides sudo access to its regular installation user. Root account availability and configuration can differ between installations.

---

# 7. User Management — useradd and usermod

Linux provides commands to create, modify, and delete user accounts.

## 7.1 useradd

### What Is useradd?

`useradd` creates a new Linux user account.

Syntax:

```bash
sudo useradd [options] username
```

Example:

```bash
sudo useradd alice
```

This creates an account named `alice`.

Depending on distribution defaults, it may not create a home directory.

### Important Options

| Option | Purpose |
|---|---|
| `-m` | Create the home directory. |
| `-d` | Specify the home directory. |
| `-s` | Specify the login shell. |
| `-g` | Set the primary group. |
| `-G` | Set supplementary groups. |
| `-u` | Specify a UID. |
| `-c` | Add a descriptive comment. |

Create a user with a home directory:

```bash
sudo useradd -m alice
```

Create a user with Bash:

```bash
sudo useradd -m -s /bin/bash alice
```

Create a user with a description:

```bash
sudo useradd -m -c "Lab User" alice
```

Verify:

```bash
id alice
```

Check the home directory:

```bash
ls -ld /home/alice
```

## 7.2 usermod

### What Is usermod?

`usermod` modifies an existing user account.

Syntax:

```bash
sudo usermod [options] username
```

### Important Options

| Option | Purpose |
|---|---|
| `-a` | Append supplementary groups. |
| `-G` | Set supplementary groups. |
| `-g` | Change primary group. |
| `-d` | Change home directory path. |
| `-m` | Move home directory contents when used with `-d`. |
| `-s` | Change login shell. |
| `-l` | Change login name. |
| `-L` | Lock password authentication. |
| `-U` | Unlock password authentication. |

### Add a User to a Group

```bash
sudo usermod -aG developers alice
```

Explanation:

- `usermod` modifies the user.
- `-a` appends supplementary groups.
- `-G` specifies the supplementary group.
- `developers` is the group.
- `alice` is the username.

**Important:** Avoid using `-G` without `-a` when you intend to add a supplementary group.

For example:

```bash
sudo usermod -G developers alice
```

This replaces the user's supplementary group list and may remove existing memberships.

### Change Login Shell

```bash
sudo usermod -s /bin/bash alice
```

### Change Username

```bash
sudo usermod -l alice2 alice
```

This changes the login name but does not automatically rename the home directory.

### Change Home Directory

```bash
sudo usermod -d /home/alice2 -m alice2
```

This updates the home directory path and moves its contents.

Verify:

```bash
id alice2
```

## 7.3 userdel

`userdel` deletes a user account.

```bash
sudo userdel alice
```

To remove the home directory and mail spool as well:

```bash
sudo userdel -r alice
```

> Warning: The `-r` option can permanently remove user data. Back up important files first.

---

# 8. Password Management — passwd

## 8.1 What Is passwd?

The `passwd` command manages Linux user passwords.

Syntax:

```bash
passwd [username]
```

Change your own password:

```bash
passwd
```

Change another user's password:

```bash
sudo passwd alice
```

The administrator can set another user's password without knowing their previous password.

## 8.2 Important Options

| Option | Purpose |
|---|---|
| `-l` | Lock password authentication. |
| `-u` | Unlock password authentication. |
| `-d` | Delete the password hash. |
| `-e` | Expire the password immediately. |
| `-S` | Display password status. |

Examples:

Check password status:

```bash
sudo passwd -S alice
```

Lock password authentication:

```bash
sudo passwd -l alice
```

Unlock password authentication:

```bash
sudo passwd -u alice
```

Expire the password:

```bash
sudo passwd -e alice
```

> Locking a password does not necessarily disable all authentication methods. SSH keys, existing sessions, and other authentication mechanisms may still permit access. Account deactivation requires reviewing the complete authentication configuration.

---

# 9. Group Management — groupadd

## 9.1 What Is groupadd?

`groupadd` creates a new Linux group.

Syntax:

```bash
sudo groupadd groupname
```

Example:

```bash
sudo groupadd developers
```

This creates a group named `developers`.

## 9.2 Verify the Group

```bash
getent group developers
```

Possible output:

```text
developers:x:1002:
```

Explanation:

| Field | Meaning |
|---|---|
| developers | Group name |
| x | Password field placeholder |
| 1002 | GID |
| Empty field | No supplementary members listed |

## 9.3 Add Users to the Group

```bash
sudo usermod -aG developers alice
```

Add another user:

```bash
sudo usermod -aG developers bob
```

Verify:

```bash
groups alice
groups bob
```

## 9.4 groupmod

`groupmod` modifies an existing group.

Change the group name:

```bash
sudo groupmod -n programmers developers
```

Change its GID:

```bash
sudo groupmod -g 1500 programmers
```

Changing a GID requires care because existing files may still be associated with the old numerical GID.

## 9.5 groupdel

`groupdel` deletes a group.

```bash
sudo groupdel developers
```

A group cannot normally be deleted if it is the primary group of an existing user.

---

# 10. Read, Write, and Execute Permissions

Linux has three basic permission types:

1. Read (`r`)
2. Write (`w`)
3. Execute (`x`)

These permissions are assigned to:

1. Owner (`u`)
2. Group (`g`)
3. Others (`o`)

## 10.1 Read Permission (r)

For files:

Read permission allows users to view file contents.

Example:

```bash
cat notes.txt
```

For directories:

Read permission allows users to list directory entries.

Example:

```bash
ls directory/
```

## 10.2 Write Permission (w)

For files:

Write permission allows users to modify file contents.

Example:

```bash
echo "Hello Linux" >> notes.txt
```

For directories:

Write permission allows users to create, delete, and rename entries, subject to directory traversal permissions and additional restrictions.

## 10.3 Execute Permission (x)

For files:

Execute permission allows a user to execute a program, subject to other system restrictions.

Example:

```bash
./script.sh
```

For directories:

Execute permission means search or traversal permission.

It allows users to access entries inside the directory when they know the names and have the necessary permissions.

## 10.4 Permission Summary

| Permission | File | Directory |
|---|---|---|
| Read | Read contents | List entries |
| Write | Modify contents | Create, delete, rename entries when traversal is allowed |
| Execute | Execute program | Traverse/search directory |

Important:

Having write permission on a file does not automatically allow deleting it.

Deleting or renaming an entry is primarily controlled by permissions on its parent directory.

The sticky bit and ACLs may impose additional restrictions.

---

# 11. Linux Permission Representation

Use:

```bash
ls -l
```

Example output:

```text
-rwxr-xr-- 1 alice developers 1200 Nov 11 10:00 script.sh
```

The permission string is:

```text
-rwxr-xr--
```

Breakdown:

```text
- | rwx | r-x | r--
    Owner Group Others
```

| Position | Meaning |
|---|---|
| 1 | File type |
| 2–4 | Owner permissions |
| 5–7 | Group permissions |
| 8–10 | Others permissions |

## 11.1 Common File Type Indicators

| Symbol | Meaning |
|---|---|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe |
| `s` | Socket |

---

# 12. Numeric Permissions — 644, 755, 700

Linux uses numerical values to represent permissions.

| Permission | Numeric Value |
|---|---:|
| Read (`r`) | 4 |
| Write (`w`) | 2 |
| Execute (`x`) | 1 |
| No permission | 0 |

These values are added together for each permission category.

## 12.1 Permission Calculations

| Combination | Calculation | Value |
|---|---|---:|
| Read | 4 | 4 |
| Write | 2 | 2 |
| Execute | 1 | 1 |
| Read + Write | 4 + 2 | 6 |
| Read + Execute | 4 + 1 | 5 |
| Write + Execute | 2 + 1 | 3 |
| Read + Write + Execute | 4 + 2 + 1 | 7 |
| No permission | 0 | 0 |

## 12.2 Understanding 644

```bash
chmod 644 notes.txt
```

Breakdown:

```text
Owner:  6 = rw-
Group:  4 = r--
Others: 4 = r--
```

Calculation:

```text
Owner:  4 + 2 = 6
Group:  4     = 4
Others: 4     = 4
```

Final representation:

```text
-rw-r--r--
```

Meaning:

- Owner can read and modify.
- Group can read.
- Others can read.

Commonly used for ordinary files.

## 12.3 Understanding 755

```bash
chmod 755 script.sh
```

Breakdown:

```text
Owner:  7 = rwx
Group:  5 = r-x
Others: 5 = r-x
```

Final representation:

```text
-rwxr-xr-x
```

Meaning:

- Owner can read, modify, and execute.
- Group can read and execute.
- Others can read and execute.

Commonly used for executable files and directories intended to be accessible to everyone.

## 12.4 Understanding 700

```bash
chmod 700 private.sh
```

Breakdown:

```text
Owner:  7 = rwx
Group:  0 = ---
Others: 0 = ---
```

Final representation:

```text
-rwx------
```

Meaning:

- Owner has full access.
- Group has no access.
- Others have no access.

Useful for private directories and scripts.

## 12.5 Common Numeric Permissions

| Numeric | Symbolic | Typical Purpose |
|---|---|---|
| 644 | `rw-r--r--` | Ordinary files |
| 755 | `rwxr-xr-x` | Executable files and accessible directories |
| 700 | `rwx------` | Private directories and scripts |
| 600 | `rw-------` | Private files |
| 750 | `rwxr-x---` | Owner and group access |
| 640 | `rw-r-----` | Owner write, group read |
| 444 | `r--r--r--` | Read-only file |
| 000 | `----------` | No basic permissions |

These are common examples, not universal security recommendations.

---

# 13. Symbolic Permissions — u, g, o, a

Symbolic permissions use letters instead of numbers.

## 13.1 Permission Categories

| Symbol | Meaning |
|---|---|
| `u` | User/Owner |
| `g` | Group |
| `o` | Others |
| `a` | All |

## 13.2 Permission Operators

| Operator | Meaning |
|---|---|
| `+` | Add permission |
| `-` | Remove permission |
| `=` | Set exact permission |

## 13.3 Practical Examples

Add execute permission to the owner:

```bash
chmod u+x script.sh
```

Remove write permission from the group:

```bash
chmod g-w notes.txt
```

Add read permission to everyone:

```bash
chmod a+r notes.txt
```

Remove all permissions from others:

```bash
chmod o-rwx private.txt
```

Set exact permissions:

```bash
chmod u=rwx,g=rx,o= script.sh
```

Equivalent numeric permission:

```bash
chmod 750 script.sh
```

---

# 14. File Permissions vs Directory Permissions

Understanding this distinction is essential for Linux administration and troubleshooting.

## 14.1 File Permissions

Example:

```text
-rw-r--r--
```

The owner can:

- Read the file.
- Modify the file.

Group members and others can read the file.

## 14.2 Directory Permissions

Example:

```text
drwxr-xr-x
```

The owner can:

- List directory entries.
- Create and remove entries, subject to the required parent-directory permissions.
- Traverse the directory.

Group members and others can list and traverse the directory.

## 14.3 Directory Permission Combinations

| Permission | General Result |
|---|---|
| `r--` | Can list names but cannot normally access entries without execute permission |
| `--x` | Can traverse/search known names but cannot list entries |
| `r-x` | Can list and traverse entries |
| `rwx` | Can list, traverse, create, and remove entries, subject to other restrictions |
| `---` | No normal access |

Remember:

- Directory read = List names.
- Directory write = Modify directory entries.
- Directory execute = Traverse/search.

## 14.4 Practical Example

Create a directory:

```bash
mkdir permission_lab
```

Create a file:

```bash
touch permission_lab/test.txt
```

Set directory permissions:

```bash
chmod 700 permission_lab
```

Check:

```bash
ls -ld permission_lab
```

Only the owner has normal access to this directory.

---

# 15. chmod — Changing Permissions

## 15.1 What Is chmod?

`chmod` stands for Change Mode.

It changes file and directory permissions.

Syntax:

```bash
chmod [options] permissions filename
```

Examples:

```bash
chmod 644 notes.txt
chmod 755 script.sh
chmod 700 private/
```

## 15.2 Important Options

| Option | Purpose |
|---|---|
| `-R` | Apply changes recursively |
| `-v` | Display processed files |
| `-c` | Report only when changes are made |
| `--reference` | Copy permissions from another file |

Examples:

```bash
chmod -v 644 notes.txt
```

Apply permissions recursively:

```bash
chmod -R 755 directory/
```

> Warning: Recursive permission changes can affect many files. Applying 755 to an entire project is usually inappropriate because ordinary files become executable. Set file and directory permissions separately when necessary.

## 15.3 Verify Permissions

For a file:

```bash
ls -l notes.txt
```

For a directory:

```bash
ls -ld directory/
```

---

# 16. chown — Changing Ownership

## 16.1 What Is chown?

`chown` stands for Change Owner.

It changes the owner of a file or directory.

Syntax:

```bash
sudo chown owner filename
```

Example:

```bash
sudo chown alice notes.txt
```

This changes the owner to Alice.

## 16.2 Change Owner and Group

```bash
sudo chown alice:developers notes.txt
```

This changes:

- Owner: Alice.
- Group: Developers.

Change only the group using chown:

```bash
sudo chown :developers notes.txt
```

## 16.3 Recursive Ownership

```bash
sudo chown -R alice:developers project/
```

This changes ownership recursively.

> Warning: Recursive ownership changes can affect many files. Never apply them to system directories without understanding the consequences.

Verify:

```bash
ls -l notes.txt
```

---

# 17. chgrp — Changing Group Ownership

## 17.1 What Is chgrp?

`chgrp` stands for Change Group.

It changes the group associated with a file or directory.

Syntax:

```bash
chgrp groupname filename
```

Example:

```bash
sudo chgrp developers project.txt
```

## 17.2 Recursive Group Ownership

```bash
sudo chgrp -R developers project/
```

This changes the group ownership of the directory and its contents.

Verify:

```bash
ls -l project.txt
```

## 17.3 Difference Between chown and chgrp

| Command | Purpose |
|---|---|
| `chown` | Changes owner and optionally group |
| `chgrp` | Changes group ownership |

---

# 18. umask — Default Permission Mask

## 18.1 What Is umask?

`umask` stands for User File Creation Mode Mask.

It determines which permission bits are removed from the permissions requested when new files and directories are created.

In simple words:

`umask` controls the default permissions assigned to newly created files and directories.

## 18.2 Why Is umask Important?

Suppose every newly created file automatically receives permissions that allow unrestricted access.

Other users might be able to access sensitive information.

umask helps restrict default permissions.

## 18.3 How Does umask Work?

Common maximum creation modes:

| Object | Maximum Creation Mode |
|---|---|
| Regular file | 666 (`rw-rw-rw-`) |
| Directory | 777 (`rwxrwxrwx`) |

A regular file does not normally receive execute permissions automatically.

The umask removes permission bits from these requested modes.

### Example: umask 022

Check the current umask:

```bash
umask
```

Possible output:

```text
0022
```

For regular files:

```text
666
022
---
644
```

For directories:

```text
777
022
---
755
```

Therefore:

- New files: 644.
- New directories: 755.

### Example: umask 077

```bash
umask 077
```

Regular files:

```text
666 -> 600
```

Directories:

```text
777 -> 700
```

New objects are restricted to the owner under normal creation rules.

## 18.4 Common umask Values

| umask | New File | New Directory |
|---|---|---|
| 022 | 644 | 755 |
| 027 | 640 | 750 |
| 077 | 600 | 700 |

## 18.5 Change umask Temporarily

```bash
umask 077
```

Create a file:

```bash
touch private.txt
```

Check:

```bash
ls -l private.txt
```

Expected:

```text
-rw-------
```

Restore a common default:

```bash
umask 022
```

**Important:** umask is a bit mask, not ordinary arithmetic subtraction in every situation. The examples above show common results. The final permissions also depend on the mode requested by the creating application.

---

# 19. SUID, SGID, and Sticky Bit

Linux supports special permission bits in addition to ordinary read, write, and execute permissions.

They are:

1. SUID — Set User ID.
2. SGID — Set Group ID.
3. Sticky Bit.

These are particularly important in Linux security and privilege management.

## 19.1 SUID — Set User ID

SUID is a special permission bit primarily used with executable files.

When an executable has SUID enabled, it normally runs with the effective UID of the file's owner rather than the user who launched it.

### Example: passwd

Ordinary users cannot directly modify `/etc/shadow`.

However, the password-changing program needs to perform privileged password updates.

A properly configured privileged `passwd` executable can perform the necessary operations using elevated effective privileges.

### Identify SUID Files

```bash
find / -type f -perm -4000 2>/dev/null
```

Explanation:

- `find /` searches from the root directory.
- `-type f` selects regular files.
- `-perm -4000` selects files with the SUID bit set.
- `2>/dev/null` suppresses error messages.

### Enable SUID

```bash
sudo chmod u+s program
```

### Remove SUID

```bash
sudo chmod u-s program
```

### Numeric Representation

SUID uses `4` in the leading octal position.

Example:

```bash
sudo chmod 4755 program
```

### Identify SUID in ls -l

```text
-rwsr-xr-x
```

The `s` in the owner's execute position indicates SUID.

If the SUID bit is set without owner execute permission, uppercase `S` appears.

### Cybersecurity Relevance

SUID is important in Linux privilege-escalation investigations.

An incorrectly configured SUID executable may allow a user to obtain privileges beyond those intended.

Not every SUID executable is vulnerable.

## 19.2 SGID — Set Group ID

SGID behaves differently depending on whether it is applied to a file or directory.

### SGID on Executable Files

An executable with SGID normally runs with the effective GID associated with the file.

### SGID on Directories

When SGID is enabled on a directory, newly created files and subdirectories generally inherit the directory's group ownership.

This is useful for shared directories.

Enable SGID:

```bash
sudo chmod g+s shared/
```

Numeric representation:

```bash
sudo chmod 2755 shared/
```

Identify SGID:

```bash
ls -ld shared/
```

Possible output:

```text
drwxr-sr-x
```

The `s` in the group execute position indicates SGID.

### Cybersecurity Relevance

SGID helps administrators manage shared directories.

Incorrect configurations can expose shared resources or create unexpected group access.

## 19.3 Sticky Bit

The sticky bit is commonly used on shared directories.

It restricts deletion and renaming of entries inside the directory.

In a sticky directory, users can generally remove or rename an entry only if they own the entry, own the directory, or have the relevant administrative privileges.

### Example: /tmp

Check:

```bash
ls -ld /tmp
```

Typical output:

```text
drwxrwxrwt
```

The final `t` represents the sticky bit.

### Enable Sticky Bit

```bash
sudo chmod +t shared/
```

### Remove Sticky Bit

```bash
sudo chmod -t shared/
```

### Numeric Representation

Sticky bit uses `1` in the leading octal position.

Example:

```bash
sudo chmod 1777 shared/
```

If the sticky bit is set without others execute permission, uppercase `T` appears.

## 19.4 Comparison of Special Permissions

| Permission | Numeric Value | Main Purpose |
|---|---:|---|
| SUID | 4 | Executable uses file owner's effective UID |
| SGID | 2 | Executable uses file group's effective GID; directories support group inheritance |
| Sticky Bit | 1 | Restricts deletion and renaming in shared directories |

### Combined Examples

SUID + 755:

```bash
chmod 4755 file
```

SGID + 755:

```bash
chmod 2755 directory
```

Sticky bit + 777:

```bash
chmod 1777 directory
```

**Security warning:** Do not enable special permissions on system executables just for experimentation. Use isolated lab files and inspect privileged binaries without modifying them.

---

# 20. Linux Access Control Lists (ACLs)

## 20.1 What Are ACLs?

ACL stands for Access Control List.

Traditional Linux permissions provide three basic categories:

- Owner.
- Group.
- Others.

Sometimes administrators need more flexible permissions.

Example:

Suppose Alice owns a file and the developers group is associated with it.

You want:

- Alice to have full access.
- Developers to have read access.
- Bob to have read and write access.
- Charlie to have no additional access.

Traditional permissions cannot independently assign a separate permission entry to Bob while keeping the other entries unchanged.

ACLs solve this problem.

## 20.2 Why Are ACLs Important?

ACLs provide granular access control.

They are useful for:

- Shared project directories.
- Multi-user environments.
- Server administration.
- Application access management.
- Granting individual users access without changing file ownership.

## 20.3 getfacl

`getfacl` displays ACL information.

Syntax:

```bash
getfacl filename
```

Example:

```bash
getfacl notes.txt
```

Possible output:

```text
# file: notes.txt
# owner: alice
# group: developers
user::rw-
group::r--
other::r--
```

## 20.4 setfacl

`setfacl` modifies ACL entries.

Syntax:

```bash
setfacl [options] ACL_SPECIFICATION filename
```

Grant Bob read permission:

```bash
sudo setfacl -m u:bob:r notes.txt
```

Grant Bob read and write:

```bash
sudo setfacl -m u:bob:rw notes.txt
```

Grant developers read and write:

```bash
sudo setfacl -m g:developers:rw notes.txt
```

Remove Bob's ACL entry:

```bash
sudo setfacl -x u:bob notes.txt
```

Remove extended ACL entries:

```bash
sudo setfacl -b notes.txt
```

## 20.5 Default ACL

Default ACLs control ACL entries inherited by newly created objects within a directory.

Example:

```bash
sudo setfacl -d -m g:developers:rwx shared/
```

New files and subdirectories can inherit the default ACL, subject to the requested creation mode and system behavior.

## 20.6 ACL Mask

ACLs contain a mask entry.

The mask limits the effective permissions of:

- Named users.
- Owning group.
- Named groups.

Example:

```text
user::rw-
user:bob:rw-
group::r--
mask::r--
other::---
```

Bob's entry requests read and write permissions, but the mask restricts his effective permissions to read only.

Check:

```bash
getfacl notes.txt
```

## 20.7 ACL Package Requirements

On Kali and other Debian-based systems, ACL utilities may need to be installed.

```bash
sudo apt update
sudo apt install acl
```

Verify:

```bash
getfacl --version
setfacl --version
```

ACL support also depends on the filesystem and mount configuration.

---

# 21. Important Linux Account Files

Linux stores user and group information in specific system files.

The important files in this phase are:

1. `/etc/passwd`
2. `/etc/group`
3. `/etc/shadow`

## 21.1 /etc/passwd

### What Is /etc/passwd?

`/etc/passwd` is a system file containing local user account information.

It stores:

- Username.
- Password placeholder.
- UID.
- GID.
- User description.
- Home directory.
- Login shell.

View its contents:

```bash
cat /etc/passwd
```

Example:

```text
alice:x:1001:1001:Alice:/home/alice:/bin/bash
```

### Understanding the Seven Fields

```text
alice:x:1001:1001:Alice:/home/alice:/bin/bash
```

| Field | Value | Meaning |
|---|---|---|
| 1 | alice | Username |
| 2 | x | Password information stored elsewhere |
| 3 | 1001 | UID |
| 4 | 1001 | Primary GID |
| 5 | Alice | User description |
| 6 | /home/alice | Home directory |
| 7 | /bin/bash | Login shell |

### Important Security Point

The `x` generally indicates that password hashes are stored in `/etc/shadow`, rather than directly in `/etc/passwd`.

`/etc/passwd` is normally readable by all local users because system utilities need account information.

Not every account listed in this file is an interactive human account.

## 21.2 /etc/group

### What Is /etc/group?

`/etc/group` stores local group information.

View it:

```bash
cat /etc/group
```

Example:

```text
developers:x:1002:alice,bob
```

### Understanding the Fields

| Field | Meaning |
|---|---|
| developers | Group name |
| x | Group password placeholder |
| 1002 | GID |
| alice,bob | Supplementary group members |

The final field lists supplementary members.

A user's primary group membership may not appear in this list.

Useful command:

```bash
getent group developers
```

This retrieves group information through the system's configured account database sources.

## 21.3 /etc/shadow

### What Is /etc/shadow?

`/etc/shadow` stores password-related account information.

It commonly contains:

- Password hashes.
- Password aging information.
- Password expiration details.
- Account expiration information.

View it:

```bash
sudo cat /etc/shadow
```

Ordinary users generally cannot read this file.

### Example Structure

```text
alice:$y$j9T$example-hash:20000:0:99999:7:::
```

This is an illustrative entry, not a real password hash.

### Understanding the Fields

| Field | Meaning |
|---|---|
| 1 | Username |
| 2 | Password hash or account password marker |
| 3 | Last password change |
| 4 | Minimum password age |
| 5 | Maximum password age |
| 6 | Warning period |
| 7 | Inactivity period |
| 8 | Account expiration date |
| 9 | Reserved field |

### Password Hash Field

The second field may contain a password hash.

A password hash is not a plaintext password.

Modern Linux installations may use hashing schemes such as yescrypt or SHA-512-based methods, depending on system configuration.

Password hashing is designed to make offline password guessing more difficult.

### Common Account Markers

| Marker | General Meaning |
|---|---|
| `!` | Password authentication locked |
| `*` | No valid password hash for normal password authentication |
| Empty field | No password hash; potentially dangerous depending on configuration |

Actual login behavior depends on the authentication stack and system configuration.

### Why Is /etc/shadow Protected?

If attackers obtain password hashes, they may attempt offline password guessing.

Protecting `/etc/shadow` reduces the exposure of authentication information.

Check permissions:

```bash
ls -l /etc/shadow
```

Possible output:

```text
-rw-r----- 1 root shadow 1200 Nov 11 10:00 /etc/shadow
```

Exact ownership and permissions may vary between distributions.

**Never change `/etc/shadow` permissions casually.**

---

# 22. Principle of Least Privilege

## 22.1 What Is Least Privilege?

The Principle of Least Privilege (PoLP) states:

Every user, process, and application should receive only the minimum permissions required to perform its intended task.

Example:

A web server that only needs to read website files should not automatically receive full root privileges.

Similarly:

- A student account should not have unrestricted administrative access.
- A database service should not run as root without a compelling reason.
- A web application should not access unnecessary system files.
- A script should not receive elevated privileges unless required.

## 22.2 Why Is Least Privilege Important?

It helps:

1. Reduce the attack surface.
2. Limit damage from compromised accounts.
3. Prevent unauthorized modifications.
4. Reduce privilege-escalation opportunities.
5. Improve system isolation.
6. Protect sensitive information.

## 22.3 Practical Example

Suppose a web application stores files in:

```text
/var/www/html/
```

An administrator must configure ownership and permissions according to the application and deployment requirements.

A possible example:

```bash
sudo chown -R www-data:www-data /var/www/html
```

On Debian-based systems, `www-data` is commonly used by web servers.

However, this is not automatically the best production configuration.

A safer design may separate:

- Deployment ownership.
- Web server read access.
- Writable upload directories.
- Application configuration.
- Sensitive secrets.

---

# 23. Safe Use of sudo

sudo can execute commands with elevated privileges.

Improper use can damage a system or expose sensitive information.

## 23.1 Unsafe Practices

Avoid:

```bash
sudo chmod -R 777 /
```

This attempts to make the entire filesystem broadly accessible and can severely damage system security.

Avoid destructive commands without checking paths:

```bash
sudo rm -rf /important-directory
```

Avoid blindly executing:

```bash
curl https://example.com/script.sh | sudo bash
```

This downloads and immediately executes a remote script with elevated privileges.

Always inspect scripts before execution.

## 23.2 Safe Practices

1. Use a regular account for daily activities.
2. Use sudo only when necessary.
3. Understand commands before executing them.
4. Verify file paths before destructive operations.
5. Avoid unrestricted recursive permission changes.
6. Use `visudo` to modify sudoers.
7. Keep packages updated.
8. Restrict sudo access to trusted users.
9. Review logs when investigating administrative activity.

## 23.3 sudo Logs

On many Debian-based systems, investigate sudo events using:

```bash
sudo journalctl _COMM=sudo
```

You can also inspect:

```bash
sudo grep sudo /var/log/auth.log
```

Log availability and location depend on the distribution and logging configuration.

---

# 24. Practical Linux Labs

All exercises should be performed inside your Kali Linux VMware environment.

Use isolated test accounts and directories.

## Practical Task 1 — Create a Separate User for Lab Work

### Objective

Create a dedicated Linux account named `labuser`.

### Step 1: Check Current User

```bash
whoami
```

### Step 2: Create the User

```bash
sudo useradd -m -s /bin/bash labuser
```

Explanation:

- `sudo` — Administrative privileges.
- `useradd` — Creates the user.
- `-m` — Creates the home directory.
- `-s /bin/bash` — Sets Bash as the login shell.
- `labuser` — Username.

### Step 3: Set a Password

```bash
sudo passwd labuser
```

### Step 4: Verify the User

```bash
id labuser
```

### Step 5: Check the Home Directory

```bash
ls -ld /home/labuser
```

### Step 6: Switch to labuser

```bash
su - labuser
```

Verify:

```bash
whoami
```

Expected output:

```text
labuser
```

Exit:

```bash
exit
```

### What Should You Learn?

- Creating a user.
- Setting a password.
- Creating a home directory.
- Switching between accounts.
- Verifying user identity.

---

## Practical Task 2 — Change File and Directory Permissions

### Objective

Practise numeric and symbolic permissions.

### Step 1: Create a Lab Directory

```bash
mkdir ~/permission_lab
cd ~/permission_lab
```

### Step 2: Create Files

```bash
touch file1.txt file2.txt file3.txt
```

### Step 3: View Permissions

```bash
ls -l
```

### Step 4: Set Permission 644

```bash
chmod 644 file1.txt
```

Verify:

```bash
ls -l file1.txt
```

Expected:

```text
-rw-r--r--
```

### Step 5: Set Permission 755

```bash
chmod 755 file2.txt
```

Verify:

```bash
ls -l file2.txt
```

Expected:

```text
-rwxr-xr-x
```

### Step 6: Set Permission 700

```bash
chmod 700 file3.txt
```

Verify:

```bash
ls -l file3.txt
```

Expected:

```text
-rwx------
```

### Step 7: Practise Symbolic Permissions

Add execute permission to the owner:

```bash
chmod u+x file1.txt
```

Remove write permission from others:

```bash
chmod o-w file1.txt
```

Add read and write permissions to the group:

```bash
chmod g+rw file1.txt
```

Check:

```bash
ls -l file1.txt
```

### What Should You Learn?

- Numeric permissions.
- Symbolic permissions.
- Owner, group, and others.
- How chmod modifies permissions.

---

## Practical Task 3 — Configure a Shared Directory for a Group

### Objective

Create a shared directory for a development team.

We will use SGID so newly created files inherit the directory's group.

### Step 1: Create a Group

```bash
sudo groupadd developers
```

### Step 2: Add Users to the Group

```bash
sudo usermod -aG developers labuser
```

If you have another test account:

```bash
sudo usermod -aG developers alice
```

### Step 3: Create a Shared Directory

```bash
sudo mkdir -p /opt/dev-shared
```

### Step 4: Change Group Ownership

```bash
sudo chown root:developers /opt/dev-shared
```

### Step 5: Configure Permissions

```bash
sudo chmod 2770 /opt/dev-shared
```

Breakdown:

```text
2 = SGID
7 = Owner full permissions
7 = Group full permissions
0 = Others no permissions
```

Expected permission representation:

```text
drwxrws---
```

### Step 6: Verify

```bash
ls -ld /opt/dev-shared
```

Expected ownership:

```text
root developers
```

### Step 7: Start a New Labuser Session

```bash
su - labuser
```

New group membership generally requires a fresh login session.

### Step 8: Create a File

```bash
touch /opt/dev-shared/project.txt
```

### Step 9: Check Ownership

```bash
ls -l /opt/dev-shared/
```

The file should normally inherit the `developers` group.

### Step 10: Test Another Group Member

If another test user belongs to `developers`, switch to that account and try:

```bash
touch /opt/dev-shared/second-file.txt
```

It should work if the user has the required active group membership.

**Important:** SGID controls group inheritance. It does not automatically make files group-writable. Application creation modes and umask still matter.

### What Should You Learn?

- Group management.
- Group ownership.
- Shared directories.
- SGID.
- Group inheritance.

---

## Practical Task 4 — Diagnose and Fix Permission Denied

### Objective

Understand why permission-denied errors occur and how to troubleshoot them.

### Step 1: Create a Protected File

As your regular user:

```bash
mkdir -p ~/permission_test
cd ~/permission_test
echo "Sensitive information" > secret.txt
```

### Step 2: Restrict Access

```bash
chmod 600 secret.txt
```

Check:

```bash
ls -l secret.txt
```

Expected:

```text
-rw-------
```

### Step 3: Try Accessing It as Another User

Replace `YOUR_USERNAME` with your actual username.

```bash
sudo -u labuser cat /home/YOUR_USERNAME/permission_test/secret.txt
```

The attempt should fail if the file and parent-directory permissions do not permit access.

Possible output:

```text
Permission denied
```

### Step 4: Diagnose the Problem

Check file permissions:

```bash
ls -l secret.txt
```

Check directory permissions:

```bash
ls -ld ~/permission_test
```

Check ownership:

```bash
stat secret.txt
```

Check current user:

```bash
whoami
```

Check groups:

```bash
id
```

### Step 5: Fix the Issue Using ACL

Grant `labuser` read permission:

```bash
sudo setfacl -m u:labuser:r secret.txt
```

Verify:

```bash
getfacl secret.txt
```

Test again:

```bash
sudo -u labuser cat /home/YOUR_USERNAME/permission_test/secret.txt
```

The parent directories must also allow traversal by `labuser`.

### Alternative: Group Permissions

```bash
sudo chgrp developers secret.txt
sudo chmod 640 secret.txt
```

The user must belong to `developers` and be able to traverse all parent directories.

### What Should You Learn?

- Diagnosing permission errors.
- Inspecting ownership.
- Inspecting directory permissions.
- Using ACLs.
- Using group permissions.

---

## Practical Task 5 — Understand Why Running Everything as Root Is Dangerous

### Objective

Understand the risks of unrestricted administrative privileges.

### Step 1: Check Your Identity

```bash
whoami
id
```

### Step 2: Create a Test Directory

```bash
mkdir ~/root_safety_lab
cd ~/root_safety_lab
touch important.txt
```

### Step 3: Set Restrictive Permissions

```bash
chmod 600 important.txt
```

### Step 4: Understand the Difference

A regular user cannot automatically modify files protected by ownership and permissions.

Root can generally bypass ordinary discretionary file permission checks.

For example:

```bash
sudo cat important.txt
```

### Step 5: Understand the Risk

An accidental destructive command executed as root can cause substantial system damage.

For example, a mistaken path in a recursive deletion command could remove critical files.

### Step 6: Follow Safer Practices

- Work under your normal account.
- Use sudo only for necessary operations.
- Verify paths before destructive commands.
- Avoid unknown scripts with elevated privileges.
- Maintain backups.
- Use dedicated lab accounts.

### What Should You Learn?

Root privileges bypass many normal permission restrictions, increasing the potential damage caused by mistakes and malicious programs.

---

# 25. Cybersecurity Relevance

Linux permissions are highly relevant to web application security and bug bounty preparation.

## 25.1 Linux Privilege Escalation

Privilege escalation occurs when a user obtains privileges beyond those intended.

Important areas to understand:

- SUID binaries.
- SGID binaries.
- Writable privileged files.
- Incorrect ownership.
- Weak sudo policies.
- Insecure service configurations.

## 25.2 SUID Enumeration

During an authorized Linux lab assessment:

```bash
find / -type f -perm -4000 2>/dev/null
```

This identifies SUID files.

Investigate whether the binaries are expected and whether their configurations are secure.

## 25.3 Check sudo Privileges

```bash
sudo -l
```

This displays the current user's sudo permissions.

Misconfigured sudo rules can create opportunities for privilege escalation.

## 25.4 Check World-Writable Files

```bash
find / -type f -perm -0002 2>/dev/null
```

This identifies regular files that have the others-write permission bit.

Not every world-writable file is vulnerable.

Investigate its ownership, purpose, parent-directory permissions, and whether a privileged process uses it.

## 25.5 Web Server Permissions

Web applications frequently run under dedicated service accounts.

On Debian-based systems, the common web server account is:

```text
www-data
```

Check:

```bash
id www-data
```

A security assessment should investigate:

- Which files the web server can read.
- Which directories it can modify.
- Whether sensitive configuration files are exposed.
- Whether upload directories have safe permissions.
- Whether the web server has unnecessary administrative privileges.

## 25.6 Sensitive Files

Important files include:

```text
/etc/passwd
/etc/shadow
/etc/sudoers
/etc/group
```

Their purposes and access restrictions should be understood.

During an authorized security investigation, checking their permissions can help identify misconfigurations.

---

# 26. Common Beginner Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Running everything as root | Increases damage from mistakes | Use a regular account |
| Using `chmod 777` unnecessarily | Gives everyone broad access | Apply minimum required permissions |
| Using `usermod -G` without `-a` | Can remove existing supplementary memberships | Use `usermod -aG` when appending |
| Confusing file and directory execute permissions | They have different meanings | Understand traversal vs execution |
| Assuming `644` makes a file private | Others can still read it | Use restrictive permissions when needed |
| Applying `chmod -R 755` to projects | Makes ordinary files executable | Configure files and directories appropriately |
| Modifying `/etc/shadow` manually | Can break authentication | Use account-management tools |
| Editing sudoers with nano directly | Syntax errors can break sudo access | Use `visudo` |
| Forgetting to start a new login session | New group memberships may not be active | Log out and back in |
| Assuming SUID always means vulnerable | Many SUID programs are legitimate | Investigate the binary and its behavior |

---

# 27. Quick Revision Tables

## 27.1 User and Group Commands

| Command | Purpose |
|---|---|
| `whoami` | Display effective username |
| `id` | Display UID, GID, and groups |
| `who` | Display logged-in users |
| `groups` | Display group membership |
| `useradd` | Create user |
| `usermod` | Modify user |
| `userdel` | Delete user |
| `passwd` | Manage passwords |
| `groupadd` | Create group |
| `groupmod` | Modify group |
| `groupdel` | Delete group |
| `getent` | Retrieve account database information |

## 27.2 Permission Commands

| Command | Purpose |
|---|---|
| `chmod` | Change permissions |
| `chown` | Change ownership |
| `chgrp` | Change group ownership |
| `umask` | Control default permission mask |
| `getfacl` | Display ACLs |
| `setfacl` | Modify ACLs |
| `ls -l` | Display file permissions and ownership |
| `stat` | Display file metadata |

## 27.3 Administrative Commands

| Command | Purpose |
|---|---|
| `sudo` | Execute authorized commands with elevated privileges |
| `su` | Switch user |
| `sudo -l` | List sudo permissions |
| `visudo` | Safely edit sudoers configuration |

## 27.4 Important Permission Values

| Numeric | Symbolic | Meaning |
|---|---|---|
| 644 | `rw-r--r--` | Owner read/write; others read |
| 755 | `rwxr-xr-x` | Owner full; others read/execute |
| 700 | `rwx------` | Owner full access only |
| 600 | `rw-------` | Owner read/write only |
| 750 | `rwxr-x---` | Owner full; group read/execute |
| 640 | `rw-r-----` | Owner read/write; group read |
| 444 | `r--r--r--` | Everyone read-only |
| 777 | `rwxrwxrwx` | Everyone full permissions |

## 27.5 Special Permissions

| Permission | Numeric | Purpose |
|---|---:|---|
| SUID | 4000 | Effective user identity of executable |
| SGID | 2000 | Effective group identity; group inheritance on directories |
| Sticky Bit | 1000 | Restricts deletion and renaming in shared directories |

## 27.6 Important Account Files

| File | Purpose |
|---|---|
| `/etc/passwd` | Local user account information |
| `/etc/group` | Local group information |
| `/etc/shadow` | Password hashes and account aging information |
| `/etc/sudoers` | sudo authorization policy |
| `/etc/sudoers.d/` | Additional sudo policy files |

---

# 28. Interview and Self-Assessment Questions

## Beginner Level

**Q1. What is a Linux user?**

A Linux user is an account that allows an individual, process, or service to interact with a Linux system.

**Q2. What is UID?**

UID stands for User ID. It is a numerical identifier assigned to a Linux user.

**Q3. What is GID?**

GID stands for Group ID. It identifies a Linux group.

**Q4. What is the root user?**

The root user is the superuser with UID 0 and extensive administrative privileges.

**Q5. What is the difference between a user and a group?**

A user represents an account, while a group is a collection of users used for permission management.

**Q6. What does whoami do?**

It displays the effective username of the current process.

**Q7. What does id do?**

It displays UID, GID, and group membership information.

**Q8. What is sudo?**

sudo allows an authorized user to execute commands with elevated or other specified privileges.

**Q9. What is chmod?**

chmod changes file and directory permissions.

**Q10. What does 755 mean?**

- Owner: Read, write, execute.
- Group: Read, execute.
- Others: Read, execute.

## Intermediate Level

**Q11. What is the difference between sudo and su?**

sudo executes authorized commands as another user, usually root. su switches to another user account.

**Q12. What is the difference between chmod and chown?**

chmod modifies permissions, while chown modifies ownership.

**Q13. What is umask?**

umask determines which permission bits are removed from the requested default permissions of newly created files and directories.

**Q14. What is SUID?**

SUID is a special permission that normally causes an executable to run with the effective UID of its file owner.

**Q15. What is SGID?**

SGID affects the effective group identity of executable programs and enables group inheritance on directories.

**Q16. What is the sticky bit?**

The sticky bit restricts deletion and renaming of entries inside a shared directory.

**Q17. What is ACL?**

ACL stands for Access Control List. It provides more granular permissions for individual users and groups.

**Q18. Why is /etc/shadow protected?**

It stores password hashes and account aging information. Protecting it reduces the risk of unauthorized access to authentication data.

**Q19. What is the purpose of /etc/passwd?**

It stores local user account information such as username, UID, GID, home directory, and login shell.

**Q20. Why should we avoid running everything as root?**

Mistakes and compromised programs can cause much greater damage when operating with unrestricted administrative privileges.

## Practical Questions

Try answering these without looking at the notes.

1. How would you create a new user with a home directory?
2. How would you add a user to the sudo group?
3. How would you create a group called `developers`?
4. How would you assign permission `640` to a file?
5. How would you remove write permission from others?
6. How would you change the owner of a file?
7. How would you identify SUID files?
8. How would you check the groups of a user?
9. How would you configure SGID on a shared directory?
10. How would you inspect ACL entries?
11. What is the difference between file execute permission and directory execute permission?
12. Why is `chmod -R 777 /` dangerous?

---

# 29. Phase 3 — Learning Checklist

## User and Group Management

- [ ] Understand Linux users and groups.
- [ ] Understand root and regular users.
- [ ] Understand UID and GID.
- [ ] Practise `whoami`.
- [ ] Practise `id`.
- [ ] Practise `who`.
- [ ] Practise `groups`.
- [ ] Understand `sudo`.
- [ ] Understand `su`.
- [ ] Create users using `useradd`.
- [ ] Modify users using `usermod`.
- [ ] Manage passwords using `passwd`.
- [ ] Create groups using `groupadd`.

## Linux Permissions

- [ ] Understand read, write, and execute.
- [ ] Understand owner, group, and others.
- [ ] Understand numeric permissions.
- [ ] Understand `644`.
- [ ] Understand `755`.
- [ ] Understand `700`.
- [ ] Understand symbolic permissions.
- [ ] Practise `chmod`.
- [ ] Practise `chown`.
- [ ] Practise `chgrp`.
- [ ] Understand file vs directory permissions.
- [ ] Understand `umask`.

## Advanced Permission Concepts

- [ ] Understand SUID.
- [ ] Understand SGID.
- [ ] Understand sticky bit.
- [ ] Identify SUID files.
- [ ] Understand Linux ACLs.
- [ ] Practise `getfacl`.
- [ ] Practise `setfacl`.

## Linux Account Files

- [ ] Understand `/etc/passwd`.
- [ ] Understand `/etc/group`.
- [ ] Understand `/etc/shadow`.
- [ ] Understand password hashes.
- [ ] Understand account restrictions.

## Security Concepts

- [ ] Understand least privilege.
- [ ] Understand safe sudo usage.
- [ ] Understand why running everything as root is dangerous.
- [ ] Understand how incorrect permissions create security vulnerabilities.
- [ ] Understand the relationship between permissions and privilege escalation.

## Practical Tasks

- [ ] Create a separate lab user.
- [ ] Create and manage a group.
- [ ] Change file permissions.
- [ ] Change directory permissions.
- [ ] Configure a shared group directory.
- [ ] Practise diagnosing permission-denied errors.
- [ ] Fix permission problems using chmod, chown, or ACLs.
- [ ] Explain why root access should be restricted.

---

# 30. Final Learning Outcomes

After completing Phase 3, you should be able to:

1. Explain how Linux identifies users and groups.
2. Create and manage Linux user accounts.
3. Understand root and regular-user privileges.
4. Use sudo and su correctly.
5. Read and modify Linux permissions.
6. Calculate numeric permission values.
7. Understand symbolic permission notation.
8. Configure file ownership and group access.
9. Understand default permissions through umask.
10. Explain SUID, SGID, and sticky bit.
11. Understand basic Linux ACLs.
12. Explain the purpose of important account files.
13. Apply the principle of least privilege.
14. Diagnose common permission-related problems.
15. Understand how Linux permissions relate to privilege escalation.

## Connection to Future Cybersecurity Learning

The knowledge from this phase will be useful when studying:

- Linux privilege escalation.
- Linux system hardening.
- SUID/SGID enumeration.
- sudo misconfigurations.
- Linux service security.
- Web server permissions.
- File-system security.
- Security auditing and investigation.

**Final advice:** Do not simply memorize commands. Practise changing permissions, switching users, creating groups, and diagnosing access problems inside your Kali Linux VM.

Your goal is to understand why Linux grants or denies access, not simply to remember which command fixes an error.

---

**End of Phase 3 — Linux Permissions and Users**
