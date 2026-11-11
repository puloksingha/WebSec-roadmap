
# Phase 8: SSH, Remote Access, and File Transfer

## Table of Contents

1. [Introduction to SSH](#1-introduction-to-ssh)
2. [Understanding SSH Architecture](#2-understanding-ssh-architecture)
3. [SSH Client and SSH Server](#3-ssh-client-and-ssh-server)
4. [Connecting to a Remote Linux Machine](#4-connecting-to-a-remote-linux-machine)
5. [SSH Authentication Methods](#5-ssh-authentication-methods)
6. [Generating SSH Keys Using ssh-keygen](#6-generating-ssh-keys-using-ssh-keygen)
7. [Public-Key Authentication](#7-public-key-authentication)
8. [SSH Configuration File](#8-ssh-configuration-file)
9. [Secure File Transfer Using SCP](#9-secure-file-transfer-using-scp)
10. [File Transfer Using SFTP](#10-file-transfer-using-sftp)
11. [File Synchronization Using rsync](#11-file-synchronization-using-rsync)
12. [SSH Host-Key Verification](#12-ssh-host-key-verification)
13. [SSH Private Key Permissions](#13-ssh-private-key-permissions)
14. [SSH Troubleshooting](#14-ssh-troubleshooting)
15. [SSH Logs and Authentication Monitoring](#15-ssh-logs-and-authentication-monitoring)
16. [Secure Remote Administration](#16-secure-remote-administration)
17. [Common SSH Security Risks](#17-common-ssh-security-risks)
18. [Cybersecurity Applications](#18-cybersecurity-applications)
19. [Practical Linux Commands Reference](#19-practical-linux-commands-reference)
20. [Hands-on Lab Exercises](#20-hands-on-lab-exercises)
21. [Interview Questions and Answers](#21-interview-questions-and-answers)
22. [Quick Revision](#22-quick-revision)

---

# 1. Introduction to SSH

## 1.1 What is SSH?

SSH stands for **Secure Shell**.

SSH is a cryptographic network protocol that allows users to securely connect to and control another computer over an unsecured network.

It provides a secure way to:

- Access remote Linux machines.
- Execute commands on remote systems.
- Transfer files between computers.
- Manage remote servers.
- Perform administrative tasks.
- Establish encrypted communication between two systems.

For example, suppose you have two Linux machines:

- Machine A: Your personal computer.
- Machine B: A remote Linux server.

You can use SSH from Machine A to access the terminal of Machine B without physically accessing it.

### Example

```bash
ssh username@192.168.1.100
```

Here:

- `ssh` is the SSH command.
- `username` is the account on the remote machine.
- `192.168.1.100` is the remote machine's IP address.

After successful authentication, you can execute commands on the remote machine.

## 1.2 Why is SSH important?

Before SSH became widely used, administrators often used protocols such as Telnet for remote access.

Telnet does not encrypt its communication. This means usernames, passwords, and transmitted data can potentially be captured by someone monitoring the network.

SSH solves this problem by encrypting communication.

| Feature | Telnet | SSH |
|---|---|---|
| Encryption | No | Yes |
| Secure authentication | Limited | Yes |
| Remote command execution | Yes | Yes |
| Secure file transfer | No built-in secure transfer | SCP and SFTP |
| Default port | 23 | 22 |
| Security | Insecure | Secure when configured properly |

## 1.3 Important characteristics of SSH

1. Encryption: Protects transmitted data from being read by unauthorized parties.
2. Authentication: Verifies the identity of the connecting user or server.
3. Integrity: Helps detect unauthorized modification of transmitted data.
4. Remote access: Allows command execution on remote machines.
5. Port forwarding: Can securely forward network connections through an SSH tunnel.

### Cybersecurity relevance

SSH is important in cybersecurity because:

- Security professionals remotely administer Linux servers.
- Penetration testers use SSH to access authorized lab machines.
- System administrators investigate remote systems.
- Attackers may attempt to exploit weak SSH configurations or stolen credentials.
- Blue teams monitor SSH authentication logs to identify suspicious access.

---

# 2. Understanding SSH Architecture

## 2.1 How SSH works

SSH follows a client-server architecture.

There are two main components:

1. SSH Client: Initiates a connection.
2. SSH Server: Accepts incoming SSH connections.

The SSH client communicates with the SSH server through an encrypted connection.

### SSH architecture diagram

```text
+--------------------------+
|      CLIENT MACHINE      |
|                          |
|  SSH Client              |
|  ssh username@IP         |
+------------+-------------+
             |
             |
       SSH Connection
       TCP Port 22
       Encrypted
             |
             |
+------------v-------------+
|       REMOTE SERVER      |
|                          |
|  SSH Server (sshd)       |
|                          |
|  Authentication          |
|  Remote Shell            |
|  Command Execution       |
+--------------------------+
```

## 2.2 Basic SSH connection process

The SSH connection generally follows these steps:

1. The client requests a connection to the remote SSH server.
2. The server presents its host identity.
3. The client and server negotiate cryptographic algorithms.
4. They establish shared session encryption keys.
5. The client authenticates the user.
6. An encrypted session is established.
7. The user can execute commands remotely.

### Important distinction

SSH uses cryptographic techniques for different purposes:

- Asymmetric cryptography helps establish trust and exchange or establish session secrets.
- Symmetric cryptography protects the actual session data efficiently.
- Hashing and message authentication mechanisms help protect integrity.

SSH is not simply a protocol that encrypts everything using the user's public key.

## 2.3 SSH default port

SSH uses TCP port **22** by default.

You can check whether an SSH server is listening using:

```bash
ss -tlnp
```

To check specifically for port 22:

```bash
ss -tlnp | grep ':22'
```

You can also check whether a remote SSH port is reachable:

```bash
nc -vz 192.168.1.100 22
```

A reachable port does not necessarily mean authentication will succeed.

---

# 3. SSH Client and SSH Server

## 3.1 SSH Client

An SSH client is a program used to connect to a remote SSH server.

Common SSH client commands:

```bash
ssh
ssh-keygen
scp
sftp
```

Check whether SSH is installed:

```bash
ssh -V
```

This displays the installed SSH client version.

## 3.2 SSH Server

An SSH server accepts incoming SSH connections.

On many Linux distributions, the OpenSSH server service is called `ssh` or `sshd`.

On Kali Linux and Debian-based distributions, you can install it using:

```bash
sudo apt update
sudo apt install openssh-server
```

Start the SSH service:

```bash
sudo systemctl start ssh
```

Enable it to start automatically during boot:

```bash
sudo systemctl enable ssh
```

Check service status:

```bash
sudo systemctl status ssh
```

Restart the service:

```bash
sudo systemctl restart ssh
```

Stop the service:

```bash
sudo systemctl stop ssh
```

### Important commands

| Command | Purpose |
|---|---|
| `systemctl start ssh` | Starts SSH service |
| `systemctl stop ssh` | Stops SSH service |
| `systemctl restart ssh` | Restarts SSH service |
| `systemctl status ssh` | Checks SSH service status |
| `systemctl enable ssh` | Enables SSH at boot |
| `systemctl disable ssh` | Disables automatic startup |

## 3.3 Verify the SSH server

Check whether the SSH daemon is running:

```bash
ps aux | grep sshd
```

Check listening ports:

```bash
sudo ss -tlnp | grep ':22'
```

Check the SSH service:

```bash
sudo systemctl status ssh
```

### Security note

Do not expose an SSH server to the public internet unless it is necessary and properly secured.

For learning, use your own virtual machines on a controlled network.

---

# 4. Connecting to a Remote Linux Machine

## 4.1 Basic SSH syntax

```bash
ssh username@hostname
```

Or:

```bash
ssh username@IP_ADDRESS
```

Example:

```bash
ssh pulok@192.168.1.100
```

The command attempts to connect to the remote machine using the specified account.

## 4.2 Connecting using a custom port

If the SSH server uses a port other than 22:

```bash
ssh -p 2222 username@192.168.1.100
```

Here, `-p` specifies the destination SSH port.

## 4.3 Connecting with verbose output

For troubleshooting:

```bash
ssh -v username@192.168.1.100
```

For more detailed debugging:

```bash
ssh -vv username@192.168.1.100
```

Maximum verbosity:

```bash
ssh -vvv username@192.168.1.100
```

These options help identify connection, authentication, and configuration problems.

## 4.4 Executing a remote command

You do not always need to open an interactive shell.

You can execute a command directly:

```bash
ssh username@192.168.1.100 "whoami"
```

Another example:

```bash
ssh username@192.168.1.100 "hostname && uptime"
```

The command runs on the remote machine.

## 4.5 Understanding remote IP addresses

Before connecting, identify the remote machine's IP address.

On the remote Linux machine:

```bash
ip addr
```

Or:

```bash
hostname -I
```

Check network connectivity:

```bash
ping 192.168.1.100
```

Remember that a failed ping does not always mean SSH is unavailable. ICMP traffic may be blocked while TCP port 22 remains accessible.

---

# 5. SSH Authentication Methods

Authentication is the process of verifying the identity of a user or system.

SSH supports multiple authentication methods.

## 5.1 Password Authentication

In password authentication, the user provides an account password.

Example:

```bash
ssh username@192.168.1.100
```

The server asks for the user's password if password authentication is enabled.

### Advantages

- Easy to understand.
- Simple to configure.
- Suitable for basic learning environments.

### Disadvantages

- Weak passwords can be guessed.
- Credentials may be reused.
- Passwords can be exposed through phishing or other compromise.
- Automated brute-force attempts may target exposed SSH services.

## 5.2 Public-Key Authentication

Public-key authentication uses a cryptographic key pair:

1. Private key
2. Public key

The private key stays with the client.

The public key is placed in the remote account's authorized keys file.

The server verifies that the connecting client can prove possession of the corresponding private key.

Example:

```bash
ssh -i ~/.ssh/id_ed25519 username@192.168.1.100
```

### Advantages

- Strong authentication when properly configured.
- Can avoid repeatedly entering an account password.
- Supports automation.
- Private keys can be protected with passphrases.

## 5.3 Password vs Public-Key Authentication

| Feature | Password | Public-Key |
|---|---|---|
| Authentication | Password | Cryptographic key pair |
| Security | Depends heavily on password strength | Strong when securely managed |
| Brute-force exposure | Common target | Not vulnerable to ordinary password guessing in the same way |
| Automation | Less convenient | Convenient |
| Key management | Not required | Required |

### Important concept

A private key is sensitive. Never share it with other people or upload it to public repositories.

---

# 6. Generating SSH Keys Using ssh-keygen

## 6.1 What is ssh-keygen?

`ssh-keygen` is a command-line utility used to generate, manage, and convert SSH authentication keys.

It is commonly used to create public-private key pairs.

## 6.2 Generate an Ed25519 key pair

Recommended modern example:

```bash
ssh-keygen -t ed25519
```

The command asks where to save the key.

The default location is usually:

```text
~/.ssh/id_ed25519
```

The public key is saved as:

```text
~/.ssh/id_ed25519.pub
```

You can also provide a custom filename:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/lab_key
```

## 6.3 Understanding the generated files

After generating a key pair:

```text
~/.ssh/
│
├── id_ed25519
└── id_ed25519.pub
```

| File | Purpose |
|---|---|
| `id_ed25519` | Private key |
| `id_ed25519.pub` | Public key |

**Never share your private key.** The public key is designed to be shared with the systems you want to authenticate to.

## 6.4 View your public key

```bash
cat ~/.ssh/id_ed25519.pub
```

This displays the public key.

You can safely provide this public key to the administrator of a server where you need access.

## 6.5 Generate an RSA key

RSA is another supported key type.

Example:

```bash
ssh-keygen -t rsa -b 4096
```

Here:

- `-t rsa` selects RSA.
- `-b 4096` specifies a 4096-bit key.

Ed25519 is generally a convenient modern default when supported by both client and server.

## 6.6 Use a passphrase

During key generation, SSH asks whether you want to protect the private key with a passphrase.

A passphrase adds protection if someone obtains a copy of your private key.

You can change a key's passphrase using:

```bash
ssh-keygen -p -f ~/.ssh/id_ed25519
```

## 6.7 List SSH keys

```bash
ls -la ~/.ssh/
```

This shows the files inside your SSH directory.

---

# 7. Public-Key Authentication

## 7.1 What is public-key authentication?

Public-key authentication is an SSH authentication method in which the client proves possession of a private key corresponding to a public key trusted by the remote server.

The server normally checks the user's:

```text
~/.ssh/authorized_keys
```

file.

## 7.2 How public-key authentication works

```text
+----------------------+
|     CLIENT MACHINE   |
|                      |
| Private Key          |
| Public Key           |
+----------+-----------+
           |
           | SSH Request
           |
           v
+----------------------+
|     SSH SERVER       |
|                      |
| authorized_keys      |
|                      |
| Checks Public Key    |
+----------+-----------+
           |
           v
   Authentication
      Successful
           |
           v
    Secure SSH Session
```

Conceptually, the server checks whether the client can produce a valid cryptographic proof using the private key associated with a trusted public key.

The private key is not sent to the server.

## 7.3 Copy the public key to the remote machine

The easiest method on OpenSSH systems is:

```bash
ssh-copy-id username@192.168.1.100
```

This normally appends the client's public key to the remote account's `authorized_keys` file.

If using a custom key:

```bash
ssh-copy-id -i ~/.ssh/lab_key.pub username@192.168.1.100
```

## 7.4 Manual public-key installation

First, display your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

On the remote machine, create the SSH directory if necessary:

```bash
mkdir -p ~/.ssh
```

Add the public key to:

```bash
nano ~/.ssh/authorized_keys
```

Paste the public key as a single line and save the file.

Set suitable permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

## 7.5 Test key-based authentication

```bash
ssh -i ~/.ssh/id_ed25519 username@192.168.1.100
```

If the key is accepted and the account is correctly configured, authentication should succeed.

### Important

Do not disable password authentication until you have tested key-based login and confirmed that you have a working recovery method.

---

# 8. SSH Configuration File

## 8.1 What is SSH configuration?

SSH supports configuration files that allow users to define connection settings.

The main user-specific SSH configuration file is:

```text
~/.ssh/config
```

The system-wide client configuration file is:

```text
/etc/ssh/ssh_config
```

The SSH server configuration file is commonly:

```text
/etc/ssh/sshd_config
```

These files have different purposes.

| File | Purpose |
|---|---|
| `~/.ssh/config` | User-specific client settings |
| `/etc/ssh/ssh_config` | System-wide client settings |
| `/etc/ssh/sshd_config` | Server configuration |

## 8.2 Create an SSH config file

```bash
nano ~/.ssh/config
```

Example configuration:

```sshconfig
Host lab-server
    HostName 192.168.1.100
    User pulok
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

Now connect using the alias:

```bash
ssh lab-server
```

Instead of typing the full connection command every time, SSH uses the saved settings.

## 8.3 Common SSH configuration options

| Option | Purpose |
|---|---|
| `Host` | Defines a connection alias or matching pattern |
| `HostName` | Actual hostname or IP address |
| `User` | Remote username |
| `Port` | Remote SSH port |
| `IdentityFile` | Private key location |
| `ConnectTimeout` | Connection timeout |
| `ServerAliveInterval` | Interval for sending keepalive messages |

## 8.4 SSH server configuration

Open the server configuration file:

```bash
sudo nano /etc/ssh/sshd_config
```

Some important directives:

```text
Port 22
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication yes
```

These are examples, not instructions to blindly overwrite your existing configuration.

### Important directives

| Directive | Purpose |
|---|---|
| `Port` | Sets the SSH listening port |
| `PermitRootLogin` | Controls direct root login |
| `PubkeyAuthentication` | Controls public-key authentication |
| `PasswordAuthentication` | Controls password authentication |
| `AllowUsers` | Restricts which users may log in |
| `MaxAuthTries` | Limits authentication attempts |

Before applying changes, validate the server configuration:

```bash
sudo sshd -t
```

If the configuration is valid, reload the service:

```bash
sudo systemctl reload ssh
```

On some systems or after certain changes, a restart may be required.

**Security warning:** Keep your existing session open while testing a new SSH configuration. Otherwise, an incorrect change could lock you out.

---

# 9. Secure File Transfer Using SCP

## 9.1 What is SCP?

SCP stands for **Secure Copy Protocol**.

The `scp` command is used to copy files between local and remote systems over an SSH connection.

It provides encrypted file transfer.

## 9.2 Basic SCP syntax

```bash
scp SOURCE DESTINATION
```

## 9.3 Copy a local file to a remote machine

```bash
scp notes.txt username@192.168.1.100:/home/username/
```

This copies `notes.txt` from the local machine to the remote directory.

## 9.4 Copy a remote file to the local machine

```bash
scp username@192.168.1.100:/home/username/notes.txt .
```

The dot (`.`) represents the current local directory.

## 9.5 Copy a directory recursively

```bash
scp -r project/ username@192.168.1.100:/home/username/
```

Here:

- `-r` means recursive.
- `project/` is the local directory.
- The remote path is the destination.

## 9.6 Use a custom SSH port

```bash
scp -P 2222 notes.txt username@192.168.1.100:/home/username/
```

Notice the uppercase `-P` for SCP, unlike SSH's lowercase `-p`.

## 9.7 Use a specific private key

```bash
scp -i ~/.ssh/id_ed25519 notes.txt username@192.168.1.100:/home/username/
```

### SCP security note

Modern OpenSSH versions use the SFTP protocol internally for many SCP operations by default. The `scp` command remains useful, but its modern behavior differs from the original SCP protocol.

---

# 10. File Transfer Using SFTP

## 10.1 What is SFTP?

SFTP stands for **SSH File Transfer Protocol**.

It is a secure file transfer protocol that operates over SSH.

It allows users to upload, download, rename, delete, and manage files on remote systems.

SFTP is different from traditional FTP.

| Feature | FTP | SFTP |
|---|---|---|
| Encryption | Not provided by standard FTP | Uses SSH encryption |
| Default port | 21 | Usually 22 |
| Authentication | Password or other supported methods | SSH-supported authentication |
| Secure file transfer | Requires additional protection such as FTPS | Yes |

## 10.2 Connect using SFTP

```bash
sftp username@192.168.1.100
```

After successful authentication, an SFTP prompt appears.

Example:

```text
sftp>
```

## 10.3 Important SFTP commands

| Command | Purpose |
|---|---|
| `ls` | Lists remote files |
| `pwd` | Displays remote working directory |
| `cd` | Changes remote directory |
| `lpwd` | Displays local working directory |
| `lls` | Lists local files |
| `lcd` | Changes local directory |
| `get` | Downloads a remote file |
| `put` | Uploads a local file |
| `mkdir` | Creates a remote directory |
| `rename` | Renames a remote file |
| `rm` | Deletes a remote file |
| `exit` | Exits SFTP |

## 10.4 Download a file

Inside the SFTP session:

```bash
get notes.txt
```

This downloads the remote file to the local working directory.

## 10.5 Upload a file

```bash
put report.txt
```

This uploads a local file to the remote working directory.

## 10.6 Download a directory

```bash
get -r project/
```

## 10.7 Upload a directory

```bash
put -r project/
```

### Cybersecurity relevance

SFTP is useful when securely transferring:

- Log files.
- Configuration files.
- Backup files.
- Investigation reports.
- Application files.

Always verify that you are transferring files to the intended remote system and directory.

---

# 11. File Synchronization Using rsync

## 11.1 What is rsync?

`rsync` is a command-line utility used to synchronize files and directories between systems.

It can transfer files locally or over a network, commonly using SSH.

It is particularly useful for backups and repeated file synchronization.

## 11.2 Basic syntax

```bash
rsync [OPTIONS] SOURCE DESTINATION
```

## 11.3 Copy a local file to a remote machine

```bash
rsync -av notes.txt username@192.168.1.100:/home/username/
```

## 11.4 Copy a remote directory to a local machine

```bash
rsync -av username@192.168.1.100:/home/username/project/ ./project/
```

## 11.5 Important rsync options

| Option | Purpose |
|---|---|
| `-a` | Archive mode; preserves common file attributes |
| `-v` | Verbose output |
| `-r` | Recursive copying |
| `-z` | Compresses data during transfer |
| `-h` | Human-readable output |
| `--progress` | Displays transfer progress |
| `--delete` | Deletes destination files absent from the source |

## 11.6 Synchronize directories

```bash
rsync -av ~/project/ username@192.168.1.100:~/project/
```

This synchronizes the contents of the local project directory with the remote destination.

## 11.7 Use rsync over a custom SSH port

```bash
rsync -av -e "ssh -p 2222" project/ username@192.168.1.100:~/project/
```

## 11.8 Understand trailing slashes

These two commands behave differently:

```bash
rsync -av project/ remote:~/project/
```

This copies the contents of `project/`.

```bash
rsync -av project remote:~/project/
```

This copies the `project` directory itself into the destination.

## 11.9 Understand --delete

Example:

```bash
rsync -av --delete project/ remote:~/project/
```

The `--delete` option removes destination files that are not present in the source.

**Warning:** Use this option carefully. A wrong source or destination can cause unwanted data loss.

Preview changes first:

```bash
rsync -av --delete --dry-run project/ remote:~/project/
```

---

# 12. SSH Host-Key Verification

## 12.1 What is a host key?

An SSH host key is a cryptographic key used by an SSH server to establish its identity.

It helps the client determine whether it is connecting to the expected server.

Do not confuse:

- Host keys: Identify the SSH server.
- User authentication keys: Help authenticate the connecting user.

These are different key pairs serving different purposes.

## 12.2 What happens during the first connection?

When connecting to a server for the first time, SSH may display a message similar to:

```text
The authenticity of host '192.168.1.100' can't be established.

Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

The client is asking you to verify the server's host-key fingerprint.

If you accept it, the host key is normally recorded in:

```text
~/.ssh/known_hosts
```

## 12.3 What is known_hosts?

The `known_hosts` file stores host identities previously accepted by the SSH client.

View it:

```bash
cat ~/.ssh/known_hosts
```

The entries may be hashed, so they might not appear as readable IP addresses or hostnames.

## 12.4 Host-key mismatch warning

You may encounter:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Possible explanations include:

- The server was rebuilt.
- The SSH host keys were regenerated.
- The server's IP address now points to another machine.
- A man-in-the-middle attack may be occurring.

Do not blindly ignore this warning.

First, verify the server's new fingerprint through a trusted channel.

## 12.5 Remove an old host-key entry

After verifying that the server's host key legitimately changed:

```bash
ssh-keygen -R 192.168.1.100
```

Then reconnect and verify the new fingerprint before accepting it.

### Security importance

Host-key verification helps defend against man-in-the-middle attacks.

---

# 13. SSH Private Key Permissions

## 13.1 Why are permissions important?

SSH private keys contain sensitive authentication material.

If other users can read your private key, they may be able to use it to impersonate you, depending on its protection and the associated server permissions.

SSH checks key-file permissions and may reject private keys that are accessible to other users.

## 13.2 Recommended permissions

Common permission settings:

| File or Directory | Permission | Command |
|---|---|---|
| `.ssh` directory | 700 | `chmod 700 ~/.ssh` |
| Private key | 600 | `chmod 600 ~/.ssh/id_ed25519` |
| Public key | 644 | `chmod 644 ~/.ssh/id_ed25519.pub` |
| `authorized_keys` | 600 | `chmod 600 ~/.ssh/authorized_keys` |
| `known_hosts` | 644 | `chmod 644 ~/.ssh/known_hosts` |

## 13.3 Apply permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
```

These are common suitable permissions, although exact ownership and permission requirements can vary by SSH configuration and operating system.

## 13.4 Check permissions

```bash
ls -la ~/.ssh/
```

Example:

```text
drwx------  .ssh
-rw-------  id_ed25519
-rw-r--r--  id_ed25519.pub
-rw-------  authorized_keys
-rw-r--r--  known_hosts
```

### Important security rule

Never:

- Upload private keys to GitHub.
- Send private keys through public messaging platforms.
- Store private keys in publicly accessible directories.
- Share your private key with someone who only needs your public key.

---

# 14. SSH Troubleshooting

SSH connections can fail for several reasons.

Understanding the error messages helps identify the actual problem.

## 14.1 Connection refused

Example:

```text
ssh: connect to host 192.168.1.100 port 22: Connection refused
```

Possible causes:

- SSH server is not running.
- SSH is not listening on port 22.
- The server is using a different port.
- A firewall is actively rejecting the connection.

Check the remote server:

```bash
sudo systemctl status ssh
```

Check listening ports:

```bash
sudo ss -tlnp | grep ':22'
```

## 14.2 Connection timed out

Example:

```text
ssh: connect to host 192.168.1.100 port 22: Connection timed out
```

Possible causes:

- Incorrect IP address.
- Network connectivity problem.
- Firewall dropping packets.
- Routing issue.
- Remote machine is unavailable.

Useful commands:

```bash
ip addr
ip route
ping 192.168.1.100
nc -vz 192.168.1.100 22
```

## 14.3 Permission denied

Example:

```text
Permission denied (publickey,password).
```

Possible causes:

- Incorrect username.
- Incorrect password.
- Public key is not installed correctly.
- Wrong private key is being used.
- Incorrect SSH directory permissions.
- Authentication method is disabled.

Troubleshoot using:

```bash
ssh -vvv username@192.168.1.100
```

Check the client's key:

```bash
ls -la ~/.ssh/
```

Check the server's authentication logs.

## 14.4 Host-key verification failed

Possible causes:

- Changed server host key.
- Reinstalled remote operating system.
- IP address reassigned to another system.
- Possible man-in-the-middle attack.

Verify the fingerprint before updating `known_hosts`.

## 14.5 SSH service not found

If you get an error such as:

```text
Unit ssh.service could not be found.
```

The OpenSSH server package may not be installed.

On Debian-based systems:

```bash
sudo apt update
sudo apt install openssh-server
```

Then start the service:

```bash
sudo systemctl start ssh
```

## 14.6 General SSH troubleshooting checklist

1. Verify the remote IP address.
2. Check network connectivity.
3. Verify the SSH server is installed.
4. Check whether the SSH service is running.
5. Confirm the listening port.
6. Check firewall rules.
7. Verify the username.
8. Check authentication configuration.
9. Verify private-key permissions.
10. Examine SSH logs.

---

# 15. SSH Logs and Authentication Monitoring

## 15.1 Why are SSH logs important?

SSH logs contain information about SSH service activity and authentication attempts.

System administrators and security professionals use these logs to identify:

- Successful logins.
- Failed login attempts.
- Invalid usernames.
- Authentication failures.
- Suspicious remote connections.
- Configuration problems.

## 15.2 View SSH service logs

On systems using systemd:

```bash
sudo journalctl -u ssh
```

Follow logs in real time:

```bash
sudo journalctl -u ssh -f
```

Some distributions use the service name `sshd`:

```bash
sudo journalctl -u sshd
```

## 15.3 Check authentication logs

On many Debian-based distributions:

```bash
sudo cat /var/log/auth.log
```

On Red Hat-based systems, authentication messages are commonly available through:

```bash
sudo journalctl -u sshd
```

The exact log location depends on the distribution and logging configuration.

## 15.4 Search for failed login attempts

On Debian-based systems:

```bash
sudo grep "Failed password" /var/log/auth.log
```

Search for successful logins:

```bash
sudo grep "Accepted" /var/log/auth.log
```

Search for invalid users:

```bash
sudo grep "Invalid user" /var/log/auth.log
```

## 15.5 Monitor logs in real time

```bash
sudo tail -f /var/log/auth.log
```

This continuously displays new authentication log entries.

### Cybersecurity relevance

A blue-team analyst can use SSH logs to investigate:

- Repeated failed login attempts.
- Unexpected successful logins.
- Access from unfamiliar IP addresses.
- Attempts to log in as root.
- Unusual login times.

A failed login alone does not prove an attack. Investigate the surrounding evidence before drawing conclusions.

---

# 16. Secure Remote Administration

Remote administration means managing a computer or server through a network without physically accessing it.

SSH is commonly used for this purpose.

## 16.1 Basic SSH security practices

1. Use strong authentication.
2. Prefer public-key authentication where practical.
3. Protect private keys with suitable permissions and passphrases.
4. Disable direct root login when it is not needed.
5. Restrict SSH access to necessary users.
6. Keep OpenSSH updated.
7. Monitor authentication logs.
8. Use firewall rules to limit access.
9. Verify host keys.
10. Avoid exposing SSH publicly without a clear need and appropriate protection.

## 16.2 Restrict allowed users

In the server configuration file:

```text
AllowUsers pulok admin
```

This restricts SSH login to the listed accounts.

Use actual account names from your server.

After changing the configuration:

```bash
sudo sshd -t
```

Then reload the SSH service if validation succeeds.

## 16.3 Disable root login

A common hardening setting is:

```text
PermitRootLogin no
```

This prevents direct root login over SSH.

Users can authenticate using their own accounts and then use `sudo` for authorized administrative tasks.

## 16.4 Disable password authentication

After public-key authentication has been configured and tested:

```text
PasswordAuthentication no
```

Before applying this change:

- Confirm your key-based login works.
- Keep an existing administrative session open.
- Ensure you have another recovery method.
- Validate the configuration.

## 16.5 Change the default SSH port

You can configure a different SSH port:

```text
Port 2222
```

This can reduce some automated noise but is not a substitute for authentication security, firewall restrictions, or patching.

Remember to update firewall rules and client connection commands.

---

# 17. Common SSH Security Risks

## 17.1 Brute-force attacks

A brute-force attack attempts many possible passwords to gain unauthorized access.

**Defensive measures:**

- Use strong authentication.
- Prefer public-key authentication.
- Restrict access to trusted networks where possible.
- Monitor failed login attempts.
- Use appropriate rate limiting or protective controls.

## 17.2 Credential theft

An attacker may obtain credentials through phishing, malware, or compromised devices.

**Defensive measures:**

- Protect private keys.
- Use passphrases.
- Secure the client machine.
- Rotate compromised keys.
- Review authorized keys.

## 17.3 Man-in-the-middle attacks

An attacker may attempt to intercept or impersonate the SSH server.

**Defensive measures:**

- Verify host-key fingerprints.
- Investigate host-key mismatch warnings.
- Avoid blindly accepting unknown host keys.

## 17.4 Exposed private keys

If a private key is accidentally uploaded to a public repository, another person may use it to access systems that trust it.

**Defensive measures:**

- Never commit private keys.
- Add private-key patterns to `.gitignore`.
- Revoke compromised public keys from authorized servers.
- Generate a replacement key pair.

Example `.gitignore` entries:

```gitignore
.ssh/
id_rsa
id_ed25519
*.pem
```

A `.gitignore` rule is not enough if the key was already committed. Remove the exposed key from the affected systems and rotate it.

## 17.5 Weak SSH configuration

Examples include:

- Unnecessary root access.
- Unrestricted remote access.
- Weak or outdated cryptographic settings.
- Excessive authentication attempts.
- Poor key management.

A secure SSH setup should follow the principle of least privilege.

---

# 18. Cybersecurity Applications

SSH is useful in several areas of cybersecurity.

## 18.1 Penetration Testing

During an authorized penetration test, SSH may be used to:

- Connect to lab machines.
- Access systems where credentials have been legitimately provided.
- Transfer approved testing tools and files.
- Execute commands remotely.
- Collect permitted system information.

## 18.2 Security Operations Center (SOC)

SOC analysts may use SSH to:

- Investigate Linux servers.
- Examine system logs.
- Review user accounts.
- Check running services.
- Investigate suspicious login activity.

## 18.3 Incident Response

During incident response, SSH can help authorized responders:

- Access affected Linux machines.
- Collect logs.
- Inspect running processes.
- Review network connections.
- Transfer investigation evidence securely.

Always follow the organization's authorization and evidence-handling procedures.

## 18.4 Web Application Security

SSH can support web application security work by allowing authorized access to:

- Application servers.
- Web server logs.
- Deployment environments.
- Configuration files.
- Test environments.

For example:

```bash
ssh username@server-ip
```

Then inspect a web server log:

```bash
sudo tail -f /var/log/nginx/access.log
```

The exact log location depends on the web server and operating system.

## 18.5 Bug Bounty Context

In bug bounty work, SSH is generally an infrastructure administration tool rather than a vulnerability-testing tool for ordinary web targets.

You may use SSH to manage your own testing machines, VPS, or authorized lab infrastructure.

Do not attempt SSH access to a bug bounty target unless the program explicitly authorizes that activity.

---

# 19. Practical Linux Commands Reference

## 19.1 SSH commands

| Command | Purpose |
|---|---|
| `ssh -V` | Displays SSH client version |
| `ssh user@IP` | Connects to remote system |
| `ssh -p 2222 user@IP` | Connects using custom port |
| `ssh -v user@IP` | Displays debugging information |
| `ssh -i key user@IP` | Uses a specified private key |
| `ssh-keygen` | Generates SSH keys |
| `ssh-copy-id user@IP` | Installs a public key remotely |

## 19.2 SSH service commands

| Command | Purpose |
|---|---|
| `sudo systemctl start ssh` | Starts SSH service |
| `sudo systemctl stop ssh` | Stops SSH service |
| `sudo systemctl restart ssh` | Restarts SSH service |
| `sudo systemctl status ssh` | Checks service status |
| `sudo systemctl enable ssh` | Enables service at boot |
| `sudo sshd -t` | Validates server configuration |

## 19.3 File transfer commands

| Command | Purpose |
|---|---|
| `scp file user@IP:/path/` | Uploads a file |
| `scp user@IP:/path/file .` | Downloads a file |
| `sftp user@IP` | Opens an SFTP session |
| `rsync -av source destination` | Synchronizes files |
| `rsync --dry-run` | Previews synchronization changes |

## 19.4 SSH key and permission commands

| Command | Purpose |
|---|---|
| `ls -la ~/.ssh/` | Lists SSH files |
| `cat ~/.ssh/id_ed25519.pub` | Displays public key |
| `chmod 700 ~/.ssh` | Secures SSH directory permissions |
| `chmod 600 ~/.ssh/id_ed25519` | Restricts private-key permissions |
| `chmod 600 ~/.ssh/authorized_keys` | Restricts authorized-key file permissions |
| `ssh-keygen -R HOST` | Removes a known-host entry |

## 19.5 Monitoring commands

| Command | Purpose |
|---|---|
| `sudo journalctl -u ssh` | Displays SSH service logs |
| `sudo journalctl -u ssh -f` | Follows SSH logs |
| `sudo tail -f /var/log/auth.log` | Monitors authentication log |
| `sudo grep "Failed password" /var/log/auth.log` | Searches failed password attempts |
| `sudo ss -tlnp` | Displays listening TCP sockets |

---

# 20. Hands-on Lab Exercises

These labs are designed for your own Kali Linux and Linux virtual machines in VMware.

## Lab 1: Install and Start SSH Server

**Objective:** Install and start the SSH server on your Linux VM.

Commands:

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh
sudo systemctl status ssh
```

Verify that the server is listening:

```bash
sudo ss -tlnp | grep ':22'
```

Expected result:

You should be able to identify whether the SSH service is listening on TCP port 22.

## Lab 2: Identify Your Machine's IP Address

**Objective:** Find the IP address of your Linux VM.

```bash
ip addr
```

Or:

```bash
hostname -I
```

Record the IP address of each VM.

Make sure both machines can communicate over their configured VMware network.

## Lab 3: Connect to Another Linux VM

**Objective:** Connect to your second Linux VM using SSH.

```bash
ssh username@REMOTE_IP
```

Example:

```bash
ssh pulok@192.168.1.100
```

After successful login, run:

```bash
whoami
hostname
ip addr
pwd
```

Observe that these commands execute on the remote machine.

## Lab 4: Generate SSH Keys

**Objective:** Generate an SSH key pair.

```bash
ssh-keygen -t ed25519
```

Inspect the generated files:

```bash
ls -la ~/.ssh/
```

Display the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Identify which file is private and which is public.

## Lab 5: Configure Key-Based Authentication

**Objective:** Authenticate using an SSH key.

On the client machine:

```bash
ssh-copy-id username@REMOTE_IP
```

Then connect:

```bash
ssh username@REMOTE_IP
```

Verify that key-based authentication works.

Do not disable password authentication yet.

## Lab 6: Transfer Files Using SCP

**Objective:** Transfer a file between your own VMs.

Create a test file:

```bash
echo "SSH file transfer lab" > test.txt
```

Upload it:

```bash
scp test.txt username@REMOTE_IP:/home/username/
```

Verify the file on the remote machine:

```bash
ssh username@REMOTE_IP "cat ~/test.txt"
```

## Lab 7: Transfer Files Using SFTP

**Objective:** Learn interactive file transfer.

Connect:

```bash
sftp username@REMOTE_IP
```

Inside SFTP:

```bash
pwd
ls
put test.txt
get test.txt
exit
```

Observe the difference between local and remote working directories.

## Lab 8: Synchronize Files Using rsync

**Objective:** Synchronize a directory between your own machines.

Create a directory:

```bash
mkdir project
echo "First version" > project/file.txt
```

Synchronize it:

```bash
rsync -av project/ username@REMOTE_IP:~/project/
```

Modify the local file:

```bash
echo "Updated version" >> project/file.txt
```

Run rsync again and observe the changes.

Try a preview:

```bash
rsync -av --dry-run project/ username@REMOTE_IP:~/project/
```

## Lab 9: Review SSH Configuration

**Objective:** Understand SSH client and server configuration.

Inspect the client configuration:

```bash
cat ~/.ssh/config
```

Inspect the server configuration:

```bash
sudo cat /etc/ssh/sshd_config
```

Check the current SSH settings and identify:

- SSH port.
- Root login policy.
- Password authentication setting.
- Public-key authentication setting.

Do not modify production or shared system settings during this exercise.

## Lab 10: Monitor SSH Authentication Logs

**Objective:** Observe SSH login activity.

On a Debian-based server:

```bash
sudo tail -f /var/log/auth.log
```

In another terminal, attempt to connect to your own VM.

Observe the log entries generated by your connection.

You can also inspect historical events:

```bash
sudo grep "Accepted" /var/log/auth.log
sudo grep "Failed password" /var/log/auth.log
```

## Lab 11: Troubleshoot SSH

**Objective:** Understand common SSH failures.

Investigate these scenarios in your isolated lab:

1. SSH service is stopped.
2. Incorrect IP address is used.
3. Incorrect username is used.
4. SSH is configured to listen on a different port.
5. Private-key permissions are incorrect.
6. Public key is missing from `authorized_keys`.

For every scenario, identify:

- The error message.
- The possible cause.
- The command used to investigate it.
- The appropriate correction.

---

# 21. Interview Questions and Answers

## Q1. What is SSH?

SSH stands for Secure Shell. It is a cryptographic network protocol used to securely access and manage remote computers over a network.

## Q2. What is the default SSH port?

The default SSH port is TCP port 22.

## Q3. What is the difference between SSH and Telnet?

SSH encrypts communication, whereas traditional Telnet sends data without encryption. SSH is therefore more suitable for secure remote administration.

## Q4. What is an SSH client?

An SSH client is a program that initiates a connection to a remote SSH server.

## Q5. What is an SSH server?

An SSH server accepts incoming SSH connections and provides authenticated remote access.

## Q6. What is sshd?

`sshd` is the OpenSSH server daemon. It listens for and handles incoming SSH connections.

## Q7. What is ssh-keygen?

`ssh-keygen` is a utility used to generate and manage SSH cryptographic keys.

## Q8. What is the difference between a public key and a private key?

A public key can be shared with the systems that need to trust it. A private key must remain confidential and is used by the client to prove possession of the corresponding key.

## Q9. What is authorized_keys?

`authorized_keys` is a file that contains public keys permitted to authenticate to a particular user account.

## Q10. What is known_hosts?

`known_hosts` stores host identities previously accepted by the SSH client.

## Q11. What is SCP?

SCP is a command-line utility used to copy files securely between systems over SSH.

## Q12. What is SFTP?

SFTP is the SSH File Transfer Protocol, used for secure file management and transfer over SSH.

## Q13. What is the difference between SCP and SFTP?

SCP primarily provides file-copy operations, while SFTP provides an interactive file-management interface with commands for uploading, downloading, renaming, and deleting files.

## Q14. What is rsync?

Rsync is a utility used to synchronize files and directories locally or between remote systems, often over SSH.

## Q15. What is the purpose of the SSH config file?

The SSH client configuration file stores reusable connection settings such as hostname, username, port, and identity file.

## Q16. What is a host-key verification warning?

It indicates that the host identity presented by the server differs from the identity previously recorded by the client. The change must be investigated before proceeding.

## Q17. Why should private-key permissions be restricted?

Restricting private-key permissions prevents unauthorized local users from reading the key and potentially using it to authenticate.

## Q18. What is password authentication?

It is an SSH authentication method in which the user proves identity using an account password.

## Q19. What is public-key authentication?

It is an authentication method in which the client proves possession of a private key corresponding to a public key trusted by the server.

## Q20. How can you check whether SSH is running?

```bash
sudo systemctl status ssh
```

## Q21. How can you check whether SSH is listening on port 22?

```bash
sudo ss -tlnp | grep ':22'
```

## Q22. How can you troubleshoot an SSH connection?

Use verbose SSH output:

```bash
ssh -vvv username@REMOTE_IP
```

Also inspect the service status, network connectivity, firewall rules, authentication settings, and server logs.

---

# 22. Quick Revision

## Important concepts

| Concept | Meaning |
|---|---|
| SSH | Secure Shell |
| SSH Client | Initiates remote connection |
| SSH Server | Accepts remote connection |
| sshd | SSH server daemon |
| TCP 22 | Default SSH port |
| ssh-keygen | Generates SSH keys |
| Private Key | Secret authentication key |
| Public Key | Key installed on the remote server |
| authorized_keys | Stores trusted user public keys |
| known_hosts | Stores previously accepted server identities |
| SCP | Secure file-copy utility |
| SFTP | Secure file-transfer protocol over SSH |
| rsync | File synchronization utility |
| ssh_config | SSH client configuration |
| sshd_config | SSH server configuration |

## Commands you must remember

```bash
# Check SSH version
ssh -V

# Install SSH server
sudo apt install openssh-server

# Start SSH
sudo systemctl start ssh

# Check SSH status
sudo systemctl status ssh

# Connect to a remote machine
ssh username@REMOTE_IP

# Connect using a custom port
ssh -p 2222 username@REMOTE_IP

# Generate SSH key pair
ssh-keygen -t ed25519

# Copy public key to remote machine
ssh-copy-id username@REMOTE_IP

# Copy file using SCP
scp file.txt username@REMOTE_IP:/path/

# Connect using SFTP
sftp username@REMOTE_IP

# Synchronize files using rsync
rsync -av source/ username@REMOTE_IP:/destination/

# View SSH logs
sudo journalctl -u ssh

# Follow authentication logs (Debian-based)
sudo tail -f /var/log/auth.log

# Validate SSH server configuration
sudo sshd -t

# Check SSH listening port
sudo ss -tlnp | grep ':22'
```

## Final Learning Checklist

After completing this phase, you should be able to:

- [ ] Explain what SSH is and why it is used.
- [ ] Understand SSH client-server architecture.
- [ ] Install and manage the OpenSSH server.
- [ ] Connect to another Linux machine.
- [ ] Generate public-private SSH key pairs.
- [ ] Configure public-key authentication.
- [ ] Understand SSH configuration files.
- [ ] Transfer files using SCP.
- [ ] Upload and download files using SFTP.
- [ ] Synchronize files using rsync.
- [ ] Understand host-key verification.
- [ ] Set appropriate SSH file permissions.
- [ ] Troubleshoot common SSH connection problems.
- [ ] Inspect SSH authentication logs.
- [ ] Apply basic SSH security practices.
- [ ] Remotely administer your own Linux virtual machines.

---

## Further Reading

1. OpenSSH Manual: https://www.openssh.com/manual.html
2. SSH Manual: https://man.openbsd.org/ssh
3. ssh-keygen Manual: https://man.openbsd.org/ssh-keygen
4. SCP Manual: https://man.openbsd.org/scp
5. SFTP Manual: https://man.openbsd.org/sftp
6. rsync Documentation: https://rsync.samba.org/documentation.html

**End of Phase 8 — SSH, Remote Access, and File Transfer**
