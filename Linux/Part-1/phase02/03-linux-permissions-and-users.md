
# Phase 3 — Linux Permissions and Users

## 1. Introduction to Linux Users and Permissions

Linux is a multi-user operating system. This means multiple users can access the same Linux system, execute programs, create files, manage directories, and perform administrative operations.

However, every user should not have unlimited access to the entire system.

Linux uses a permission and ownership mechanism to control:

- Who can access a file or directory.
- Who can modify or delete files.
- Who can execute programs.
- Who can manage system configurations.
- Who can perform administrative operations.
- Which users can access shared resources.

For example:

Suppose a Linux system has three users:

- `root` — System administrator.
- `alice` — Regular user.
- `bob` — Regular user.

If Alice creates a private file, Bob should not automatically be able to read or modify it.

Linux permissions provide this type of access control.

### Why are Linux permissions important?

Permissions are important for:

1. System administration.
2. Protecting sensitive files.
3. Preventing unauthorized access.
4. Managing multiple users.
5. Securing applications and services.
6. Controlling administrative privileges.
7. Preventing privilege escalation.
8. Maintaining system integrity.

### Basic Linux permission model

Linux associates three important properties with files and directories:

| Property | Description |
|---|---|
| Owner | User who owns the file. |
| Group | Group associated with the file. |
| Others | Everyone else who is neither the owner nor a member of the file's group. |

Each category can have different permissions.

Example:

```bash
-rwxr-xr--
```

This permission string indicates:

- Owner: Read, write, execute.
- Group: Read and execute.
- Others: Read only.

We will understand this in detail throughout this phase.

---

# 2. Linux Users and Groups

## 2.1 What Are Linux Users?

A user is an account that allows an individual, application, or service to interact with a Linux system.

Every Linux user has a unique numerical identifier called a UID (User ID).

Linux uses UIDs internally to identify users and determine file ownership and access permissions.

For example:

```bash
whoami
```

Possible output:

```text
pulok
```

This means the current shell is operating under the user account `pulok`.

### Types of Linux users

Linux users can generally be divided into three categories.

#### 1. Root User

The root user is the superuser of Linux.

- UID: `0`
- Has extensive administrative privileges.
- Can access and modify most system files.
- Can create and remove users.
- Can modify system configurations.
- Can install and remove system packages.

#### 2. Regular Users

Regular users are normal accounts created for people who use the system.

- Usually have UIDs starting from `1000` on modern Debian-based installations.
- Have restricted privileges.
- Can access their own files.
- Cannot normally modify protected system files.
- Can receive additional privileges through groups and sudo policies.

UID ranges are configurable and may differ between distributions.

#### 3. System Users

System users are generally created to run system services and applications.

Examples:

- `www-data` — Commonly used by web servers.
- `mysql` — Commonly used by MySQL or MariaDB.
- `sshd` — May be used by SSH-related processes.

These accounts generally do not represent human users.

They help isolate services and reduce the impact of a compromised application.

## 2.2 What Are Linux Groups?

A group is a collection of users.

Groups make permission management easier because administrators can assign permissions to a group instead of configuring access for every user individually.

Example:

Suppose a company has three developers:

- Alice
- Bob
- Charlie

Instead of giving permissions individually, an administrator can create a group named `developers`.

All three users can become members of this group.

The administrator can then provide the group with access to a shared development directory.

### Group types

Linux commonly uses two group relationships.

**1. Primary group**

Every user has a primary group.

It is the default group associated with the user's processes and newly created files, subject to directory settings and other mechanisms.

**2. Supplementary groups**

A user can belong to additional groups.

These groups provide additional access to resources.

For example:

```bash
groups
```

Possible output:

```text
pulok sudo developers
```

This indicates that the user belongs to the groups `pulok`, `sudo`, and `developers`.

### Understanding UID and GID

| Term | Full Form | Purpose |
|---|---|---|
| UID | User ID | Identifies a user. |
| GID | Group ID | Identifies a group. |
| EUID | Effective User ID | Determines the user identity used for many permission checks. |
| EGID | Effective Group ID | Determines the effective group identity used for many permission checks. |

Linux uses numerical IDs internally rather than relying exclusively on usernames and group names.

---

# 3. Root User and Regular Users

## 3.1 What Is the Root User?

The root user is the most privileged account in Linux.

Its UID is always `0`.

Root can perform administrative operations that ordinary users cannot normally perform.

Examples:

```bash
# Install software
apt install nginx

# Modify protected system configuration
nano /etc/hosts

# Create a system user
useradd testuser

# Manage system services
systemctl restart ssh
```

Some commands require root privileges.

On a normal user account, they may return:

```text
Permission denied
```

or:

```text
E: Could not open lock file
```

Running an appropriate administrative command with `sudo` may resolve the issue.

## 3.2 What Is a Regular User?

A regular user operates with limited privileges.

For example:

```bash
whoami
```

Output:

```text
pulok
```

The account `pulok` is the current user.

A regular user can generally:

- Create files in permitted directories.
- Execute programs they are allowed to execute.
- Manage their own files.
- Run commands available to their account.
- Access shared resources when permissions allow.

A regular user cannot automatically:

- Modify `/etc/passwd`.
- Install system-wide packages.
- Change another user's password.
- Modify protected system services.
- Access every user's private files.

## 3.3 Root vs Regular User

| Feature | Root User | Regular User |
|---|---|---|
| UID | 0 | Usually 1000 or above |
| Administrative access | Extensive | Restricted |
| Modify system files | Generally yes | Requires authorization |
| Create users | Yes | Requires authorization |
| Install packages | Yes | Usually requires sudo |
| Access protected files | Generally yes | Depends on permissions |
| Security risk | High impact if compromised | Usually more limited |

### How to identify the root user?

```bash
whoami
```

If the output is:

```text
root
```

You are operating as root.

You can also check:

```bash
id
```

Output example:

```text
uid=0(root) gid=0(root) groups=0(root)
```

## 3.4 Why Should You Avoid Using Root All the Time?

Running everything as root is dangerous.

Consider this command:

```bash
rm -rf /some/directory
```

If executed as a regular user, Linux may prevent the deletion of protected files.

If executed as root, the command can remove files that the regular user cannot delete.

A mistake can damage your operating system.

Other risks include:

- Accidental deletion of important files.
- Modification of critical system configurations.
- Running malicious programs with elevated privileges.
- Increasing the impact of software vulnerabilities.
- Making privilege-escalation attacks easier.

**Best practice:** Use a regular account for daily activities and obtain administrative privileges only when necessary.

---

# 4. Identifying the Current User

Linux provides several commands for identifying users and groups.

## 4.1 `whoami`

### What is whoami?

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

This indicates that the effective user is `pulok`.

### When is it useful?

- Checking which account is running a command.
- Verifying a user switch.
- Confirming whether you are operating as root.
- Troubleshooting permission problems.

Example:

```bash
sudo whoami
```

Output:

```text
root
```

This demonstrates that `sudo` executed the command with root privileges.

Note: `whoami` displays the effective user, not necessarily the original login user.

## 4.2 `id`

### What is id?

The `id` command displays user and group identity information.

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
| `groups=` | Groups associated with the user. |
| `27(sudo)` | Membership in the sudo group. |

### Important options

**Display the identity of another user:**

```bash
id username
```

**Display only the UID:**

```bash
id -u
```

**Display only the primary GID:**

```bash
id -g
```

**Display group IDs:**

```bash
id -G
```

**Display group names:**

```bash
id -Gn
```

These commands are useful for understanding account identity and group membership.

## 4.3 `who`

### What is who?

The `who` command displays information about users currently logged into the system.

Syntax:

```bash
who
```

Possible output:

```text
pulok    tty2    2026-11-09 09:30
```

Explanation:

| Field | Meaning |
|---|---|
| pulok | Logged-in username. |
| tty2 | Terminal session. |
| Date | Login date. |
| Time | Login time. |

### Important options

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

### Practical importance

System administrators can use `who` to inspect active login sessions.

It can also help during security investigations.

## 4.4 `groups`

### What is groups?

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

To check another user:

```bash
groups alice
```

Possible output:

```text
alice : alice developers
```

This means Alice belongs to her primary group and the developers group.

### Difference between id and groups

| Command | Purpose |
|---|---|
| `id` | Displays UID, GID, and group information. |
| `groups` | Displays group memberships. |
| `whoami` | Displays effective username. |
| `who` | Displays logged-in users. |

---

# 5. sudo

## 5.1 What Is sudo?

`sudo` stands for **Superuser Do**.

It allows an authorized user to execute a command with elevated privileges.

Instead of logging in as root, a regular user can execute individual administrative commands through sudo.

Example:

```bash
sudo apt update
```

This executes the package-list update with administrative privileges.

### Why is sudo important?

- Avoids the need to work continuously as root.
- Provides controlled administrative access.
- Allows administrators to define which commands users can execute.
- Can record command execution in system logs.
- Supports the principle of least privilege.

## 5.2 How Does sudo Work?

Suppose your username is `pulok`.

You execute:

```bash
sudo apt update
```

The general process is:

1. Linux identifies the requesting user.
2. `sudo` checks the sudo policy.
3. It verifies whether the user is authorized.
4. Authentication may be required.
5. The requested command executes with the authorized target privileges.
6. The operation may be recorded in authentication or sudo logs.

The default target user is usually root.

However, sudo can execute commands as other permitted users too.

## 5.3 Basic sudo Syntax

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
| `-u` | Run a command as another user. |
| `-i` | Start a login shell as the target user. |
| `-s` | Start a shell with the target user identity. |
| `-l` | List permitted commands. |
| `-k` | Invalidate cached authentication credentials. |
| `-v` | Refresh authentication credentials. |

Examples:

**Execute a command as another user:**

```bash
sudo -u alice whoami
```

Output:

```text
alice
```

**Start a root login shell:**

```bash
sudo -i
```

Check the identity:

```bash
whoami
```

Output:

```text
root
```

Exit the root shell:

```bash
exit
```

**List sudo permissions:**

```bash
sudo -l
```

This displays commands that the current user is permitted to execute through sudo.

## 5.5 sudo Group

On Debian-based distributions, including Kali and Ubuntu, users who belong to the `sudo` group are commonly authorized to use sudo.

Check group membership:

```bash
groups
```

Add a user to the sudo group:

```bash
sudo usermod -aG sudo username
```

Example:

```bash
sudo usermod -aG sudo alice
```

The user may need to log out and log back in before the new supplementary group membership becomes active in their sessions.

Verify:

```bash
id alice
```

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

Never edit the sudoers file with an ordinary text editor.

Use:

```bash
sudo visudo
```

`visudo` checks the syntax before installing the modified configuration.

A syntax error in sudoers can prevent users from using sudo.

### Example sudoers rule

```text
alice ALL=(ALL:ALL) ALL
```

Meaning:

- `alice` — The user.
- First `ALL` — Applies to all hosts.
- `(ALL:ALL)` — Can run as any user and group.
- Last `ALL` — Can run any command.

Actual authorization depends on the complete sudoers policy and its matching rules.

### Security best practices

- Give sudo access only to trusted users.
- Avoid unnecessary unrestricted privileges.
- Do not execute unknown scripts with sudo.
- Inspect commands before executing them.
- Prefer individual administrative commands over permanent root sessions.
- Use `visudo` for configuration changes.

---

# 6. su

## 6.1 What Is su?

`su` stands for **Substitute User**.

It allows a user to switch to another user account.

If no username is provided, `su` normally attempts to switch to root.

Syntax:

```bash
su [options] [username]
```

Example:

```bash
su alice
```

This switches to the Alice account after successful authentication.

### Switch to root

```bash
su
```

On many distributions, this asks for the root account password.

### Switch to root with a login environment

```bash
su -
```

The `-` option requests a login shell.

It loads the target user's login environment, including the appropriate working directory and environment settings.

### Switch to another user with a login environment

```bash
su - alice
```

### Exit the switched account

```bash
exit
```

## 6.2 Difference Between sudo and su

| Feature | sudo | su |
|---|---|---|
| Full form | Superuser Do | Substitute User |
| Main purpose | Execute authorized commands as another user | Switch to another user |
| Authentication | Usually requesting user's password | Usually target user's password |
| Default target | root | root |
| Single command | Yes | Possible with `-c` |
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

**Important:** Kali Linux commonly configures a regular installation user with sudo privileges. The availability and configuration of the root account can differ between installations.

---

# 7. Creating and Managing Users

Linux provides commands to create, modify, and manage user accounts.

The most important commands include:

- `useradd`
- `usermod`
- `passwd`
- `userdel`

## 7.1 useradd

### What is useradd?

`useradd` creates a new user account.

Syntax:

```bash
sudo useradd [options] username
```

Example:

```bash
sudo useradd alice
```

This creates an account named `alice`.

However, depending on the distribution defaults, it may not create a home directory.

### Important options

| Option | Purpose |
|---|---|
| `-m` | Create the user's home directory. |
| `-d` | Specify a home directory. |
| `-s` | Specify the login shell. |
| `-g` | Set the primary group. |
| `-G` | Set supplementary groups. |
| `-u` | Specify a UID. |
| `-c` | Add a descriptive comment. |

### Create a user with a home directory

```bash
sudo useradd -m alice
```

The home directory will normally be:

```text
/home/alice
```

### Create a user with a Bash shell

```bash
sudo useradd -m -s /bin/bash alice
```

### Create a user with a description

```bash
sudo useradd -m -c "Lab User" alice
```

### Verify the account

```bash
id alice
```

Check the home directory:

```bash
ls -ld /home/alice
```

## 7.2 passwd

### What is passwd?

The `passwd` command manages user passwords.

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

The administrator can set a password for another account without knowing its previous password.

### Important options

| Option | Purpose |
|---|---|
| `-l` | Lock an account's password authentication. |
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

> Important: Locking a password does not necessarily disable every possible login method. SSH keys, existing sessions, or other authentication mechanisms may still allow access. For complete account deactivation, review all relevant authentication and account settings.

## 7.3 usermod

### What is usermod?

`usermod` modifies an existing user account.

Syntax:

```bash
sudo usermod [options] username
```

### Important options

| Option | Purpose |
|---|---|
| `-a` | Append supplementary groups. |
| `-G` | Set supplementary groups. |
| `-g` | Change the primary group. |
| `-d` | Change the home directory path. |
| `-m` | Move existing home directory contents when used with `-d`. |
| `-s` | Change login shell. |
| `-l` | Change login name. |
| `-L` | Lock password authentication. |
| `-U` | Unlock password authentication. |

### Add a user to a group

```bash
sudo usermod -aG developers alice
```

Explanation:

- `usermod` modifies the account.
- `-a` appends supplementary groups.
- `-G` specifies the supplementary group.
- `developers` is the group name.
- `alice` is the username.

**Very important:**

Do not normally use `-G` without `-a` when you intend to add a supplementary group.

For example:

```bash
sudo usermod -G developers alice
```

This replaces Alice's supplementary group list rather than simply adding the developers group. It can remove existing supplementary memberships.

### Change the login shell

```bash
sudo usermod -s /bin/bash alice
```

### Change the username

```bash
sudo usermod -l alice2 alice
```

This changes the login name. It does not automatically rename the home directory.

### Change the home directory

```bash
sudo usermod -d /home/alice2 -m alice2
```

This updates the home directory path and moves its contents.

### Verify modifications

```bash
id alice
```

## 7.4 userdel

Although not a primary topic in this phase, understanding account deletion is useful.

`userdel` deletes a user account.

```bash
sudo userdel alice
```

To remove the user's home directory and mail spool as well:

```bash
sudo userdel -r alice
```

> Warning: Account deletion can permanently remove user data. Always inspect the account and back up important files before using `-r`.

---

# 8. Managing Linux Groups

## 8.1 groupadd

### What is groupadd?

`groupadd` creates a new group.

Syntax:

```bash
sudo groupadd groupname
```

Example:

```bash
sudo groupadd developers
```

This creates a group named `developers`.

### Verify the group

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
| developers | Group name. |
| x | Password field placeholder. |
| 1002 | GID. |
| Empty field | Supplementary member list may be empty. |

## 8.2 Add Users to a Group

Use:

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

## 8.3 groupmod

`groupmod` modifies an existing group.

Change the group name:

```bash
sudo groupmod -n programmers developers
```

Change the group GID:

```bash
sudo groupmod -g 1500 programmers
```

Be careful when changing group IDs because existing files may still be associated with the old numerical GID.

## 8.4 groupdel

`groupdel` deletes a group.

Syntax:

```bash
sudo groupdel groupname
```

Example:

```bash
sudo groupdel developers
```

A group cannot normally be deleted if it is the primary group of an existing user.

Always check group membership before deleting it.

---

# 9. Linux File Permissions

## 9.1 What Are File Permissions?

Linux permissions determine what users can do with files and directories.

Linux has three basic permission types:

1. Read (`r`)
2. Write (`w`)
3. Execute (`x`)

These permissions are assigned to three categories:

1. User/Owner (`u`)
2. Group (`g`)
3. Others (`o`)

The categories and permission types together form the basic Linux permission model.

## 9.2 Read Permission (r)

Read permission allows a user to view file contents.

For example:

```bash
cat notes.txt
```

If the user has read permission, the file contents can be displayed.

For directories, read permission allows the user to list directory entries.

Example:

```bash
ls /home/alice
```

## 9.3 Write Permission (w)

For files, write permission allows modification of the file contents.

Example:

```bash
echo "Hello Linux" >> notes.txt
```

For directories, write permission allows creating, deleting, and renaming entries, subject to the directory's execute permission and additional restrictions.

## 9.4 Execute Permission (x)

For executable files, execute permission allows a user to run the file as a program, subject to other system restrictions.

Example:

```bash
./script.sh
```

For directories, execute permission means search or traversal permission.

It allows users to access entries inside the directory when they know their names and have the necessary permissions.

### Important permission table

| Permission | File | Directory |
|---|---|---|
| Read (r) | Read contents | List directory entries |
| Write (w) | Modify contents | Create, delete, or rename entries when traversal is also allowed |
| Execute (x) | Execute program | Traverse/search directory |

### Important distinction

Having write permission on a file does not automatically mean you can delete that file.

Deleting or renaming a file is primarily controlled by permissions on its parent directory.

Sticky-bit restrictions and ACLs can also affect deletion and renaming.

---

# 10. Understanding Permission Representation

Use the following command:

```bash
ls -l
```

Example output:

```text
-rwxr-xr-- 1 pulok developers 1200 Nov 9 10:00 script.sh
```

Let's understand each part.

```text
-rwxr-xr--
```

The first character indicates the file type.

The next nine characters represent permissions.

```text
- | rwx | r-x | r--
    Owner Group Others
```

Breakdown:

| Position | Meaning |
|---|---|
| 1 | File type |
| 2-4 | Owner permissions |
| 5-7 | Group permissions |
| 8-10 | Others permissions |

In the example:

- Owner has read, write, and execute.
- Group has read and execute.
- Others have read only.

### Common file type indicators

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

# 11. chmod — Changing Permissions

## 11.1 What is chmod?

`chmod` stands for Change Mode.

It changes file and directory permissions.

Syntax:

```bash
chmod [options] permissions filename
```

Example:

```bash
chmod 644 notes.txt
```

This changes the file's permissions to `644`.

There are two primary ways to use chmod:

1. Numeric (octal) permissions.
2. Symbolic permissions.

---

# 12. Numeric Permissions

Linux uses numerical values to represent permissions.

| Permission | Numeric Value |
|---|---:|
| Read (r) | 4 |
| Write (w) | 2 |
| Execute (x) | 1 |
| No permission | 0 |

These values are added together to create the permission value for each category.

### How does numeric permission work?

For each category:

```text
Read    = 4
Write   = 2
Execute = 1
```

Examples:

| Combination | Calculation | Value |
|---|---|---:|
| Read only | 4 | 4 |
| Write only | 2 | 2 |
| Execute only | 1 | 1 |
| Read + Write | 4 + 2 | 6 |
| Read + Execute | 4 + 1 | 5 |
| Write + Execute | 2 + 1 | 3 |
| Read + Write + Execute | 4 + 2 + 1 | 7 |
| No permission | 0 | 0 |

### 12.1 Understanding 644

```bash
chmod 644 notes.txt
```

Breakdown:

```text
6 = Owner
4 = Group
4 = Others
```

Calculation:

```text
Owner:  4 + 2 = 6 (rw-)
Group:  4     = 4 (r--)
Others: 4     = 4 (r--)
```

Final permissions:

```text
-rw-r--r--
```

Meaning:

- Owner can read and modify.
- Group can read.
- Others can read.

Commonly used for ordinary files.

### 12.2 Understanding 755

```bash
chmod 755 script.sh
```

Breakdown:

```text
Owner:  7 = rwx
Group:  5 = r-x
Others: 5 = r-x
```

Final permissions:

```text
-rwxr-xr-x
```

Meaning:

- Owner can read, modify, and execute.
- Group can read and execute.
- Others can read and execute.

Commonly used for executable scripts and directories that should be accessible to everyone.

### 12.3 Understanding 700

```bash
chmod 700 private.sh
```

Breakdown:

```text
Owner:  7 = rwx
Group:  0 = ---
Others: 0 = ---
```

Final permissions:

```text
-rwx------
```

Meaning:

- Owner has full access.
- Group has no access.
- Others have no access.

Useful for private scripts and directories.

### 12.4 Common numeric permissions

| Permission | Symbolic Form | Typical Purpose |
|---|---|---|
| 644 | `rw-r--r--` | Ordinary files |
| 755 | `rwxr-xr-x` | Executable files and public directories |
| 700 | `rwx------` | Private directories and scripts |
| 600 | `rw-------` | Private files |
| 750 | `rwxr-x---` | Owner and group access |
| 640 | `rw-r-----` | Owner write, group read |
| 444 | `r--r--r--` | Read-only file |
| 000 | `----------` | No basic permissions |

> These are common examples, not universal security recommendations. Select permissions according to the actual application and access requirements.

---

# 13. Symbolic Permissions

Numeric permissions use numbers, while symbolic permissions use letters.

The four important symbolic identifiers are:

| Symbol | Meaning |
|---|---|
| `u` | User/Owner |
| `g` | Group |
| `o` | Others |
| `a` | All |

The operators are:

| Operator | Meaning |
|---|---|
| `+` | Add permission |
| `-` | Remove permission |
| `=` | Set exact permission |

### 13.1 Add execute permission to owner

```bash
chmod u+x script.sh
```

This adds execute permission to the owner.

### 13.2 Remove write permission from group

```bash
chmod g-w notes.txt
```

This removes group write permission.

### 13.3 Add read permission to everyone

```bash
chmod a+r notes.txt
```

This adds read permission to owner, group, and others.

### 13.4 Remove all permissions from others

```bash
chmod o-rwx private.txt
```

This removes read, write, and execute permissions from others.

### 13.5 Set exact permissions

```bash
chmod u=rwx,g=rx,o= script.sh
```

This sets:

- Owner: Read, write, execute.
- Group: Read, execute.
- Others: No permissions.

Equivalent numeric permission:

```bash
chmod 750 script.sh
```

### 13.6 Apply permissions recursively

```bash
chmod -R 755 directory/
```

This applies permissions recursively to files and subdirectories.

> Warning: Applying `755` recursively to an entire project is usually inappropriate because it makes ordinary files executable. Use separate permissions for files and directories.

A safer example for a directory containing private data is to set permissions deliberately rather than recursively applying a broad permission.

### Verify permissions

```bash
ls -l script.sh
```

For directory permissions:

```bash
ls -ld directory/
```

---

# 14. File Permissions vs Directory Permissions

This is one of the most important Linux concepts.

The meaning of read, write, and execute differs between files and directories.

### File permissions

Suppose:

```bash
-rw-r--r--
```

The owner can:

- Read the file.
- Modify the file.

The group and others can read the file.

### Directory permissions

Suppose:

```bash
drwxr-xr-x
```

The owner can:

- List directory entries.
- Create and delete entries, subject to the parent directory and other restrictions.
- Traverse the directory.

The group and others can list and traverse the directory.

### Practical example

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

Now only the owner has normal access to the directory.

Try:

```bash
ls permission_lab
```

As another user, this should fail unless that user has access through another permission mechanism.

### Important combinations

| Directory Permission | Result |
|---|---|
| `r--` | Can list names in some cases, but cannot normally access entries without execute permission |
| `--x` | Can traverse/search known names, but cannot list entries |
| `r-x` | Can list and traverse entries |
| `rwx` | Can list, traverse, create, and remove entries subject to other restrictions |
| `---` | No normal access |

Remember:

- Directory read = list names.
- Directory write = modify directory entries.
- Directory execute = traverse/search.

---

# 15. chown — Changing Ownership

## 15.1 What is chown?

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

This changes the owner of `notes.txt` to Alice.

### Change owner and group

```bash
sudo chown alice:developers notes.txt
```

This changes:

- Owner: alice.
- Group: developers.

### Change only the group using chown

```bash
sudo chown :developers notes.txt
```

### Change ownership recursively

```bash
sudo chown -R alice:developers project/
```

This changes ownership recursively.

> Warning: Recursive ownership changes can affect many files. Avoid running them on system directories unless you fully understand the consequences.

### Verify ownership

```bash
ls -l notes.txt
```

Possible output:

```text
-rw-r--r-- 1 alice developers 100 Nov 9 10:00 notes.txt
```

---

# 16. chgrp — Changing Group Ownership

## 16.1 What is chgrp?

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

This changes the group ownership to `developers`.

### Recursive group ownership

```bash
sudo chgrp -R developers project/
```

This changes the group ownership of the directory and its contents.

### Verify

```bash
ls -l project.txt
```

### Difference between chown and chgrp

| Command | Purpose |
|---|---|
| `chown` | Change owner, and optionally group |
| `chgrp` | Change group ownership |

---

# 17. umask

## 17.1 What is umask?

`umask` stands for User File Creation Mode Mask.

It determines which permission bits are removed from the default permissions when new files and directories are created.

In simple words:

`umask` controls the default permissions assigned to newly created files and directories.

### Why is umask important?

Suppose every new file automatically receives overly permissive permissions.

Other users might access sensitive information.

`umask` helps prevent this by restricting default permissions.

## 17.2 How does umask work?

Linux commonly starts with these maximum creation permissions:

| Object | Maximum Default Permissions |
|---|---|
| Regular file | 666 (`rw-rw-rw-`) |
| Directory | 777 (`rwxrwxrwx`) |

The system applies the umask to remove permission bits.

A regular file does not normally receive execute permissions automatically.

### Example: umask 022

Check your current umask:

```bash
umask
```

Possible output:

```text
0022
```

For ordinary files:

```text
666
-022
----
644
```

For directories:

```text
777
-022
----
755
```

Therefore:

- New files: `644`
- New directories: `755`

### Example: umask 077

```bash
umask 077
```

For regular files:

```text
666 -> 600
```

For directories:

```text
777 -> 700
```

New files and directories become private to the owner under normal permission creation rules.

### Common umask values

| umask | New File | New Directory |
|---|---|---|
| 022 | 644 | 755 |
| 027 | 640 | 750 |
| 077 | 600 | 700 |

### Change umask temporarily

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

Expected permissions:

```text
-rw-------
```

### Restore a common default

```bash
umask 022
```

### Important note

The umask is a permission-bit mask, not an ordinary arithmetic subtraction in every possible case. The examples above show common results.

The actual creation mode is restricted by the requested mode and the umask.

Also, applications can request different creation modes, so the final permissions are not always identical to the simple examples.

---

# 18. SUID, SGID, and Sticky Bit

Linux supports special permission bits in addition to ordinary read, write, and execute permissions.

These include:

1. SUID — Set User ID.
2. SGID — Set Group ID.
3. Sticky Bit.

These permissions are particularly important in Linux security.

They can affect privilege boundaries and access to shared directories.

## 18.1 SUID (Set User ID)

SUID is a special permission bit used primarily with executable files.

When an executable has SUID enabled, it normally runs with the effective user ID of the file's owner rather than the user who launched it.

Example:

The `passwd` program needs to update protected password information.

Ordinary users cannot directly modify `/etc/shadow`.

A properly configured privileged password-changing program can perform the required operation with elevated effective privileges.

### Identify SUID files

Use:

```bash
find / -type f -perm -4000 2>/dev/null
```

Explanation:

- `find /` searches from the root directory.
- `-type f` selects regular files.
- `-perm -4000` selects files with the SUID bit set.
- `2>/dev/null` suppresses permission-related error messages.

This search can take some time.

### Enable SUID

```bash
sudo chmod u+s program
```

### Remove SUID

```bash
sudo chmod u-s program
```

### Numeric representation

SUID uses the special permission value `4` in the leading octal position.

Example:

```bash
sudo chmod 4755 program
```

### Identify SUID in ls -l

Example:

```text
-rwsr-xr-x
```

The `s` in the owner's execute position indicates SUID.

If SUID is set but owner execute permission is not set, the character appears as uppercase `S`.

### Security relevance

SUID is important in privilege-escalation investigations.

An incorrectly configured SUID executable may allow an attacker to obtain privileges beyond those intended.

Never assume that every SUID binary is vulnerable.

## 18.2 SGID (Set Group ID)

SGID has different behavior depending on whether it is applied to a file or directory.

### SGID on executable files

An executable with SGID normally runs with the effective group ID associated with the file.

### SGID on directories

When SGID is enabled on a directory, newly created files and subdirectories generally inherit the directory's group ownership.

This is useful for shared directories.

Example:

```bash
sudo chmod g+s shared/
```

Now new files created inside the directory normally inherit its group.

### Numeric representation

SGID uses the value `2` in the leading octal position.

Example:

```bash
sudo chmod 2755 shared/
```

### Identify SGID

```bash
ls -ld shared/
```

Possible output:

```text
drwxr-sr-x
```

The `s` in the group's execute position indicates SGID.

### Security relevance

SGID helps administrators manage shared project directories.

Incorrect SGID configurations can expose shared resources or create unexpected group access.

## 18.3 Sticky Bit

The sticky bit is commonly used on shared directories.

It restricts deletion and renaming of entries inside the directory.

In a sticky directory, users can generally remove or rename an entry only if they own the entry, own the directory, or have the relevant administrative privilege.

### Example: /tmp

The `/tmp` directory is commonly configured with sticky bit permissions.

Check:

```bash
ls -ld /tmp
```

Typical output:

```text
drwxrwxrwt
```

The final `t` represents the sticky bit.

### Enable sticky bit

```bash
sudo chmod +t shared/
```

### Remove sticky bit

```bash
sudo chmod -t shared/
```

### Numeric representation

Sticky bit uses the value `1` in the leading octal position.

Example:

```bash
sudo chmod 1777 shared/
```

### Identify sticky bit

```text
drwxrwxrwt
```

The final `t` indicates sticky bit.

If the sticky bit is set without the others execute bit, it appears as uppercase `T`.

## 18.4 Comparison of Special Permissions

| Permission | Numeric Value | Main Purpose |
|---|---:|---|
| SUID | 4 | Executable uses file owner's effective UID |
| SGID | 2 | Executable uses file group's effective GID; directories support group inheritance |
| Sticky Bit | 1 | Restricts deletion and renaming in shared directories |

### Combined numeric permissions

Example:

```bash
chmod 4755 file
```

SUID + 755.

```bash
chmod 2755 directory
```

SGID + 755.

```bash
chmod 1777 directory
```

Sticky bit + 777.

### Important cybersecurity warning

Special permissions can create security risks when configured incorrectly.

During a Linux security assessment, examine:

- Unusual SUID binaries.
- Unexpected SGID binaries.
- Writable privileged executables.
- Untrusted executable paths.
- Incorrect ownership.
- Dangerous permissions on shared directories.

Never modify privileged binaries on a production system just to experiment.

---

# 19. Linux Access Control Lists (ACLs)

## 19.1 What Are ACLs?

ACL stands for Access Control List.

Traditional Linux permissions provide three basic categories:

- Owner.
- Group.
- Others.

However, sometimes administrators need more flexible permissions.

For example:

Suppose a file belongs to Alice.

Its group is developers.

You want:

- Alice to have full access.
- The developers group to have read access.
- Bob to have read and write access.
- Charlie to have no additional access.

Traditional owner/group/others permissions cannot independently assign a separate permission entry to Bob while keeping the other entries unchanged.

ACLs solve this problem.

## 19.2 Why Are ACLs Important?

ACLs provide more detailed access control.

They are useful for:

- Shared project directories.
- Multi-user environments.
- Server administration.
- Application access management.
- Granting access to individual users without changing file ownership.

## 19.3 getfacl

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

This displays the file's ACL entries.

## 19.4 setfacl

`setfacl` modifies ACL entries.

Syntax:

```bash
setfacl [options] ACL_SPECIFICATION filename
```

Grant Bob read permission:

```bash
sudo setfacl -m u:bob:r notes.txt
```

Grant Bob read and write permission:

```bash
sudo setfacl -m u:bob:rw notes.txt
```

Grant the developers group read and write access:

```bash
sudo setfacl -m g:developers:rw notes.txt
```

### Remove a specific ACL entry

```bash
sudo setfacl -x u:bob notes.txt
```

### Remove all extended ACL entries

```bash
sudo setfacl -b notes.txt
```

### Recursive ACL

```bash
sudo setfacl -R -m g:developers:rwx project/
```

This recursively grants the developers group the specified permissions.

### Default ACL

Default ACLs control the ACL entries inherited by newly created objects within a directory.

Example:

```bash
sudo setfacl -d -m g:developers:rwx shared/
```

New files and subdirectories can inherit the default ACL, subject to the creating application's requested permissions and system behavior.

### ACL mask

ACLs also contain a mask entry.

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

Although Bob's ACL entry requests read and write, the mask limits his effective permission to read only.

Check effective permissions with:

```bash
getfacl notes.txt
```

### ACL package requirements

On Kali and many Debian-based systems, ACL utilities may need to be installed.

```bash
sudo apt update
sudo apt install acl
```

Check availability:

```bash
getfacl --version
setfacl --version
```

ACL support also depends on the filesystem and mount configuration.

---

# 20. Important Linux Account Files

Linux stores user and group account information in specific system files.

The most important files in this phase are:

1. `/etc/passwd`
2. `/etc/group`
3. `/etc/shadow`

Understanding these files is important for Linux administration and security investigations.

## 20.1 /etc/passwd

### What is /etc/passwd?

`/etc/passwd` is a system file containing user account information.

It stores information such as:

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

### Understanding the fields

The file contains seven colon-separated fields.

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

### Important security point

The `x` generally indicates that password hashes are stored in `/etc/shadow`, rather than directly in `/etc/passwd`.

The `/etc/passwd` file is normally readable by all local users because many system utilities need account information.

Do not assume that every account listed in `/etc/passwd` is an interactive human account.

## 20.2 /etc/group

### What is /etc/group?

`/etc/group` stores local group information.

View it:

```bash
cat /etc/group
```

Example:

```text
developers:x:1002:alice,bob
```

### Understanding the fields

```text
developers:x:1002:alice,bob
```

| Field | Meaning |
|---|---|
| developers | Group name |
| x | Group password placeholder |
| 1002 | GID |
| alice,bob | Supplementary group members |

The final field lists supplementary members.

A user's primary group membership may not appear in this list.

### Useful command

```bash
getent group developers
```

This retrieves the group information through the system's configured account database sources.

## 20.3 /etc/shadow

### What is /etc/shadow?

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

Its access restrictions help protect password hashes and authentication information.

### Example structure

```text
alice:$y$j9T$example-hash:20000:0:99999:7:::
```

This is an illustrative entry, not a real password hash.

### Understanding the fields

| Field | Meaning |
|---|---|
| 1 | Username |
| 2 | Encrypted password hash or account password marker |
| 3 | Last password change |
| 4 | Minimum password age |
| 5 | Maximum password age |
| 6 | Warning period |
| 7 | Inactivity period |
| 8 | Account expiration date |
| 9 | Reserved field |

### Password hash field

The second field may contain a password hash.

It is not normally a plaintext password.

Modern Linux installations may use password hashing schemes such as yescrypt or SHA-512-based methods, depending on system configuration.

A password hash is not the same as encryption.

Password hashing is designed to be computationally expensive to reverse and is normally verified by hashing a candidate password and comparing the result.

### Common account markers

| Marker | General Meaning |
|---|---|
| `!` | Password authentication locked |
| `*` | No valid password hash for normal password authentication |
| Empty field | No password hash; potentially dangerous depending on configuration |

Actual login behavior depends on the authentication stack and system configuration.

### Why is /etc/shadow protected?

If attackers obtain password hashes, they may attempt offline password guessing.

Protecting `/etc/shadow` reduces the exposure of authentication data.

Typical permissions:

```bash
ls -l /etc/shadow
```

Possible output:

```text
-rw-r----- 1 root shadow 1200 Nov 9 10:00 /etc/shadow
```

Exact ownership and permissions can vary between distributions.

**Never change `/etc/shadow` permissions casually.**

---

# 21. Principle of Least Privilege

## 21.1 What Is Least Privilege?

The Principle of Least Privilege (PoLP) is a security principle that states:

Every user, process, and application should receive only the minimum permissions required to perform its intended task.

For example:

Suppose a web server only needs to read website files.

It should not automatically receive full root privileges.

Similarly:

- A student account should not have unrestricted administrative access.
- A database service should not run as root without a compelling reason.
- A web application should not have unnecessary access to system files.
- A script should not receive elevated privileges unless required.

## 21.2 Why Is Least Privilege Important?

It helps:

1. Reduce the attack surface.
2. Limit damage from compromised accounts.
3. Prevent unauthorized modifications.
4. Reduce privilege-escalation opportunities.
5. Improve system isolation.
6. Protect sensitive information.

## 21.3 Practical Example

Suppose a web application stores files in:

```text
/var/www/html/
```

Instead of giving every user full access, an administrator can configure ownership and permissions for the intended application and deployment workflow.

Example:

```bash
sudo chown -R www-data:www-data /var/www/html
```

This assigns ownership to the common web server account on Debian-based systems.

However, this is not automatically the best deployment configuration.

A safer production design may separate:

- Deployment ownership.
- Web server read access.
- Writable upload directories.
- Application configuration.
- Sensitive secrets.

### Cybersecurity relevance

Least privilege is essential in:

- Linux privilege escalation prevention.
- Web server security.
- Database isolation.
- Container security.
- Service account management.
- Application security.

---

# 22. Safe Use of sudo

`sudo` is powerful because it can execute commands with elevated privileges.

Improper use can damage a system or expose sensitive information.

### 22.1 Common unsafe practices

Avoid:

```bash
sudo chmod -R 777 /
```

This attempts to make the entire filesystem broadly accessible and can severely damage system security.

Avoid:

```bash
sudo rm -rf /
```

This is a destructive command that can delete critical system data.

Avoid blindly executing:

```bash
curl https://example.com/script.sh | sudo bash
```

This downloads and immediately executes a remote script with elevated privileges.

You should inspect downloaded scripts before executing them.

### 22.2 Safe practices

1. Use a regular account for daily activities.
2. Use sudo only when necessary.
3. Understand commands before executing them.
4. Verify file paths before using destructive commands.
5. Avoid unrestricted recursive permission changes.
6. Use `visudo` to modify sudoers.
7. Keep packages updated.
8. Restrict sudo access to trusted users.
9. Review logs when investigating administrative activity.

### 22.3 sudo logs

On many Debian-based systems, authentication and sudo activity can be investigated through:

```bash
sudo journalctl _COMM=sudo
```

You can also inspect:

```bash
sudo grep sudo /var/log/auth.log
```

The log location and availability depend on the distribution and logging configuration.

On some systems, sudo events may be recorded in the system journal instead.

---

# 23. Practical Lab Environment

Before starting the exercises, understand the environment.

We will create a separate lab user and group.

The practical exercises should be performed inside your Kali Linux VMware virtual machine.

Avoid experimenting with user accounts and permissions on important production systems.

## Lab objectives

You will:

1. Create a separate user for lab work.
2. Create a group.
3. Add users to the group.
4. Change file permissions.
5. Change ownership.
6. Configure a shared directory.
7. Test permission-denied errors.
8. Investigate permissions using Linux commands.

---

# 24. Practical Task 1 — Create a Separate Lab User

### Objective

Create a dedicated Linux user named `labuser`.

This account will be used for practical exercises without requiring you to perform all activities as root.

### Step 1: Check your current user

```bash
whoami
```

### Step 2: Create the user

```bash
sudo useradd -m -s /bin/bash labuser
```

Explanation:

- `sudo` — Administrative privileges.
- `useradd` — Creates a user.
- `-m` — Creates the home directory.
- `-s /bin/bash` — Sets Bash as the login shell.
- `labuser` — Username.

### Step 3: Set a password

```bash
sudo passwd labuser
```

Enter a password when prompted.

### Step 4: Verify the user

```bash
id labuser
```

### Step 5: Check the home directory

```bash
ls -ld /home/labuser
```

Expected result:

A directory named `/home/labuser` should exist.

### Step 6: Switch to the lab user

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

### What did you learn?

- How to create a user.
- How to configure a home directory.
- How to set a password.
- How to switch between users.

---

# 25. Practical Task 2 — Change File and Directory Permissions

### Objective

Understand numeric and symbolic permissions through practical examples.

### Step 1: Create a lab directory

```bash
mkdir ~/permission_lab
```

### Step 2: Create files

```bash
cd ~/permission_lab
touch file1.txt file2.txt file3.txt
```

### Step 3: View current permissions

```bash
ls -l
```

### Step 4: Set permission 644

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

### Step 5: Set permission 755

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

### Step 6: Set permission 700

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

### Step 7: Practise symbolic permissions

Add execute permission to the owner:

```bash
chmod u+x file1.txt
```

Remove write permission from others:

```bash
chmod o-w file1.txt
```

Give group read and write permissions:

```bash
chmod g+rw file1.txt
```

Check:

```bash
ls -l file1.txt
```

### What did you learn?

- Numeric permissions.
- Symbolic permissions.
- Owner, group, and others.
- How chmod changes permissions.

---

# 26. Practical Task 3 — Configure a Shared Directory for a Group

### Objective

Create a shared directory that allows members of a group to collaborate.

We will use SGID so newly created files inherit the shared group.

### Step 1: Create a group

```bash
sudo groupadd developers
```

### Step 2: Add users to the group

```bash
sudo usermod -aG developers labuser
```

If you have another test account:

```bash
sudo usermod -aG developers alice
```

### Step 3: Create a shared directory

```bash
sudo mkdir -p /opt/dev-shared
```

### Step 4: Change group ownership

```bash
sudo chown root:developers /opt/dev-shared
```

### Step 5: Configure permissions

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

### Step 6: Check the configuration

```bash
ls -ld /opt/dev-shared
```

Expected ownership:

```text
root developers
```

### Step 7: Switch to labuser

```bash
su - labuser
```

### Step 8: Create a file inside the shared directory

```bash
touch /opt/dev-shared/project.txt
```

### Step 9: Check ownership

```bash
ls -l /opt/dev-shared/
```

The file should normally inherit the `developers` group.

### Step 10: Test access from another group member

If another test user belongs to `developers`, switch to that account and try:

```bash
touch /opt/dev-shared/second-file.txt
```

It should be possible if the account has the required active group membership.

### Important note

New group membership generally requires a fresh login session.

Also, the SGID bit controls group inheritance; it does not automatically make all files group-writable.

Applications' creation modes and umask still matter.

For a more controlled shared directory, default ACLs can also be configured.

### What did you learn?

- Group management.
- Group ownership.
- Shared directories.
- SGID.
- Permission inheritance.

---

# 27. Practical Task 4 — Diagnose and Fix Permission Denied

### Objective

Understand why permission-denied errors occur and how to diagnose them.

### Step 1: Create a protected file

As your regular user:

```bash
mkdir -p ~/permission_test
cd ~/permission_test
echo "Sensitive information" > secret.txt
```

### Step 2: Remove access from others

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

### Step 3: Try accessing it as another user

For example:

```bash
sudo -u labuser cat /home/YOUR_USERNAME/permission_test/secret.txt
```

Replace `YOUR_USERNAME` with your actual username.

If the file is owned by another user and has mode `600`, the attempt should fail, provided no other access mechanism grants permission.

You may see:

```text
Permission denied
```

### Step 4: Diagnose the problem

Check the file permissions:

```bash
ls -l secret.txt
```

Check ownership:

```bash
ls -l
```

Check the directory permissions:

```bash
ls -ld ~/permission_test
```

Check the current user:

```bash
whoami
```

Check group membership:

```bash
id
```

### Step 5: Fix the issue

If you want to allow a particular user to read the file, one option is to use an ACL:

```bash
sudo setfacl -m u:labuser:r secret.txt
```

Verify:

```bash
getfacl secret.txt
```

Now test again:

```bash
sudo -u labuser cat /home/YOUR_USERNAME/permission_test/secret.txt
```

The parent directories must also allow traversal by `labuser` for this access to work.

### Alternative solution: Group permissions

You can also assign the file to a shared group and configure group read access.

```bash
sudo chgrp developers secret.txt
sudo chmod 640 secret.txt
```

The user must be a member of `developers` and must be able to traverse all parent directories.

### What did you learn?

- How to identify permission errors.
- How to inspect ownership.
- How to inspect directory permissions.
- How to use ACLs.
- How group permissions solve access problems.

---

# 28. Practical Task 5 — Why Running Everything as Root Is Dangerous

### Objective

Understand the risks of unrestricted administrative privileges.

### Step 1: Check your current identity

```bash
whoami
id
```

### Step 2: Create a test directory

```bash
mkdir ~/root_safety_lab
cd ~/root_safety_lab
touch important.txt
```

### Step 3: Set restrictive permissions

```bash
chmod 600 important.txt
```

### Step 4: Understand the difference

A regular user cannot automatically modify files protected by ownership and permissions.

However, root can generally bypass ordinary discretionary file permission checks.

For example:

```bash
sudo cat important.txt
```

### Step 5: Understand the danger

Imagine accidentally executing:

```bash
sudo rm -rf /important-directory
```

If the path is correct and the command is allowed to execute, it can permanently remove important data.

The same operation may have been prevented by permissions if performed as an ordinary user.

### Step 6: Follow safer practices

- Work under your normal account.
- Use sudo only for necessary operations.
- Check paths before destructive commands.
- Avoid executing unknown scripts as root.
- Keep backups of important data.
- Use dedicated lab accounts.

### What did you learn?

Root privileges bypass many normal permission restrictions, increasing the potential damage caused by mistakes and malicious programs.

---

# 29. Cybersecurity Relevance — Linux Permissions

Linux permissions are highly relevant to web application security and bug bounty preparation.

Understanding permissions helps you identify security weaknesses during authorized system assessments.

## 29.1 Linux Privilege Escalation

Privilege escalation occurs when a user or attacker obtains privileges beyond their intended permissions.

For example:

A regular user might discover an incorrectly configured privileged executable.

If the executable provides an exploitable path to elevated privileges, it may create a privilege-escalation vulnerability.

Important concepts:

- SUID binaries.
- SGID binaries.
- Writable privileged files.
- Incorrect ownership.
- Weak sudo policies.
- Insecure service configurations.

## 29.2 SUID Enumeration

During an authorized Linux lab assessment:

```bash
find / -type f -perm -4000 2>/dev/null
```

This identifies SUID files.

Investigate whether the binaries are expected and whether their configuration is secure.

## 29.3 Check sudo privileges

```bash
sudo -l
```

This shows the current user's sudo permissions.

Misconfigured sudo rules can create opportunities for privilege escalation.

## 29.4 Check writable files

Find world-writable regular files:

```bash
find / -type f -perm -0002 2>/dev/null
```

This can help identify files that anyone can modify.

Not every world-writable file is vulnerable.

Investigate ownership, purpose, parent-directory permissions, and whether the file is used by a privileged process.

## 29.5 Web Server Permissions

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

## 29.6 Sensitive Files

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

# 30. Important Linux Commands — Quick Revision

| Command | Purpose |
|---|---|
| `whoami` | Display effective username |
| `id` | Display UID, GID, and groups |
| `who` | Display logged-in users |
| `groups` | Display group membership |
| `sudo` | Execute authorized commands with elevated privileges |
| `su` | Switch user |
| `useradd` | Create user |
| `usermod` | Modify user |
| `userdel` | Delete user |
| `passwd` | Manage passwords |
| `groupadd` | Create group |
| `groupmod` | Modify group |
| `groupdel` | Delete group |
| `chmod` | Change permissions |
| `chown` | Change ownership |
| `chgrp` | Change group ownership |
| `umask` | Control default permission masks |
| `getfacl` | Display ACL entries |
| `setfacl` | Modify ACL entries |
| `getent` | Retrieve account database information |
| `visudo` | Safely edit sudoers configuration |
| `find` | Search for files and directories |
| `ls -l` | Display file permissions and ownership |

---

# 31. Important Permission Values — Quick Revision

| Permission | Value | Meaning |
|---|---:|---|
| Read | 4 | Read file contents |
| Write | 2 | Modify file contents |
| Execute | 1 | Execute file |
| No permission | 0 | No access |

### Common permissions

| Numeric | Symbolic | Meaning |
|---|---|---|
| 644 | `rw-r--r--` | Owner read/write; others read |
| 755 | `rwxr-xr-x` | Owner full; others read/execute |
| 700 | `rwx------` | Owner full access only |
| 600 | `rw-------` | Owner read/write only |
| 750 | `rwxr-x---` | Owner full; group read/execute |
| 640 | `rw-r-----` | Owner read/write; group read |
| 777 | `rwxrwxrwx` | Everyone full permissions |

### Special permissions

| Permission | Numeric | Symbolic |
|---|---:|---|
| SUID | 4000 | `s` in owner execute position |
| SGID | 2000 | `s` in group execute position |
| Sticky bit | 1000 | `t` in others execute position |

---

# 32. Important Differences to Remember

| Concept | Difference |
|---|---|
| UID vs GID | UID identifies a user; GID identifies a group. |
| Root vs regular user | Root has extensive administrative privileges; regular users have restricted access. |
| sudo vs su | sudo executes authorized commands; su switches user accounts. |
| useradd vs usermod | useradd creates accounts; usermod modifies accounts. |
| chmod vs chown | chmod changes permissions; chown changes ownership. |
| chown vs chgrp | chown changes owner and optionally group; chgrp changes group ownership. |
| Primary vs supplementary group | Primary is the default group; supplementary groups provide additional membership. |
| File read vs directory read | File read displays contents; directory read lists entries. |
| File execute vs directory execute | File execute runs a program; directory execute permits traversal. |
| SUID vs SGID | SUID affects effective user identity; SGID affects effective group identity and directory group inheritance. |
| ACL vs traditional permissions | ACLs provide more granular access entries. |
| /etc/passwd vs /etc/shadow | passwd contains account information; shadow stores password-related information. |

---

# 33. Interview and Self-Assessment Questions

## Beginner Level

### Q1. What is a Linux user?

A Linux user is an account that allows a person, process, or service to interact with a Linux system.

### Q2. What is UID?

UID stands for User ID. It is a numerical identifier assigned to a Linux user.

### Q3. What is GID?

GID stands for Group ID. It identifies a Linux group.

### Q4. What is the root user?

The root user is the superuser with UID 0 and extensive administrative privileges.

### Q5. What is the difference between a user and a group?

A user represents an account, while a group is a collection of users used for permission management.

### Q6. What does whoami do?

It displays the effective username of the current process.

### Q7. What does id do?

It displays UID, GID, and group membership information.

### Q8. What is sudo?

sudo allows an authorized user to execute commands with elevated or other specified privileges.

### Q9. What is the purpose of chmod?

chmod changes file and directory permissions.

### Q10. What does 755 mean?

- Owner: Read, write, execute.
- Group: Read, execute.
- Others: Read, execute.

## Intermediate Level

### Q11. What is the difference between sudo and su?

sudo executes authorized commands as another user, usually root. su switches to another user account.

### Q12. What is the difference between chmod and chown?

chmod modifies permissions, while chown modifies ownership.

### Q13. What is umask?

umask controls which permission bits are removed from the default permissions of newly created files and directories.

### Q14. What is SUID?

SUID is a special permission that causes an executable to normally run with the effective UID of its file owner.

### Q15. What is SGID?

SGID affects the effective group identity of executable programs and enables group inheritance on directories.

### Q16. What is the sticky bit?

The sticky bit restricts deletion and renaming of entries in a shared directory.

### Q17. What is ACL?

ACL stands for Access Control List. It provides more granular permissions for individual users and groups.

### Q18. Why is /etc/shadow protected?

It stores password hashes and account aging information. Protecting it reduces the risk of unauthorized access to authentication data.

### Q19. What is the purpose of /etc/passwd?

It stores local user account information such as username, UID, GID, home directory, and login shell.

### Q20. Why should we avoid running everything as root?

Because mistakes and compromised programs can cause much greater damage when operating with unrestricted administrative privileges.

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

# 34. Phase 3 — Practical Completion Checklist

Use this checklist to track your progress.

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
- [ ] Modify accounts using `usermod`.
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
- [ ] Understand how incorrect permissions can create security vulnerabilities.
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

# 35. Final Learning Outcome

After completing Phase 3, you should be able to:

1. Explain how Linux identifies users and groups.
2. Create and manage user accounts.
3. Understand root and regular-user privileges.
4. Use sudo and su correctly.
5. Read and modify Linux permissions.
6. Calculate numeric permission values.
7. Understand symbolic permission notation.
8. Configure ownership and group access.
9. Understand default permissions through umask.
10. Explain SUID, SGID, and sticky bit.
11. Understand basic Linux ACLs.
12. Explain the purpose of important account files.
13. Apply the principle of least privilege.
14. Diagnose common permission-related problems.
15. Understand how Linux permissions relate to privilege escalation.

## Connection to the Next Cybersecurity Learning Stages

The knowledge from this phase will be useful when studying:

- Linux privilege escalation.
- Linux system hardening.
- SUID/SGID enumeration.
- Sudo misconfigurations.
- Linux service security.
- Web server permissions.
- File-system security.
- Security auditing and investigation.

**Remember:** Do not just memorize commands. Practise changing permissions, switching users, creating groups, and diagnosing access problems inside your Kali Linux VM.

The goal is to understand why Linux grants or denies access, not simply to remember which command fixes an error.

---

**End of Phase 3 — Linux Permissions and Users**
