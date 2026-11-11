
# PHASE 5 — LINUX PACKAGE MANAGEMENT AND SOFTWARE

# PART 1: UNDERSTANDING PACKAGE MANAGEMENT

## 1. What Are Packages?

A package is a collection of files and metadata required to install and run a software application on an operating system.

A package may contain:

- Executable program files.
- Configuration files.
- Libraries.
- Documentation.
- Installation scripts.
- Information about dependencies.
- Package version information.

For example, when you install Firefox or Nmap on Kali Linux, the software is generally installed through a package.

### 1.1 Package Formats

Different Linux distributions use different package formats.

| Package format | Used by |
|---|---|
| `.deb` | Debian, Ubuntu, Kali Linux |
| `.rpm` | Fedora, RHEL, openSUSE |
| `.pkg.tar.zst` | Arch Linux |
| `.apk` | Alpine Linux |

Since Kali Linux is based on Debian, it primarily uses `.deb` packages.

Example:

```text
nmap_7.95+dfsg-1_amd64.deb
```

This is an illustrative Debian package filename.

### 1.2 What Is Package Management?

Package management is the process of installing, updating, configuring, and removing software packages.

Linux package managers help users:

- Install applications.
- Remove unnecessary software.
- Update existing packages.
- Resolve software dependencies.
- Verify package information.
- Manage software repositories.

On Debian-based distributions, APT is the most commonly used high-level package management tool.

---

## 2. What Are Repositories?

A repository is a storage location containing software packages and the metadata required by a package manager.

Linux distributions maintain repositories to distribute software to users.

When you install a package using APT, your system downloads the package from a configured repository.

### 2.1 How Repositories Work

The basic process is:

1. Your Linux system has repository addresses configured.
2. APT downloads package metadata from those repositories.
3. You search for or request a software package.
4. APT identifies the package and its dependencies.
5. APT downloads the required packages.
6. The package manager installs and configures them.

Example:

```bash
sudo apt update
sudo apt install nmap
```

### 2.2 Types of Repositories

Common repository categories include:

**Official repositories**

- Maintained by the Linux distribution.
- Provide packages supported by the distribution.
- Usually the safest default source for ordinary installations.

**Third-party repositories**

- Maintained by external developers or organizations.
- May provide software unavailable in official repositories.
- Require additional trust and verification.

**Local repositories**

- Package collections hosted on a local machine or network.
- Useful in offline environments and organizations.

### 2.3 Repository Configuration

APT repository configuration tells the system where it can find software packages.

Important locations:

```text
/etc/apt/sources.list
/etc/apt/sources.list.d/
```

Inspect the main repository configuration:

```bash
cat /etc/apt/sources.list
```

Inspect additional repository files:

```bash
ls /etc/apt/sources.list.d/
```

On modern Debian-based systems, repository definitions may also use the `.sources` format.

Example of an illustrative repository entry:

```text
deb http://example.com/debian stable main
```

Its components:

- `deb`: Binary package repository.
- URL: Repository location.
- `stable`: Distribution or release name.
- `main`: Repository component.

Important:

Do not randomly add repository addresses. Use repositories intended for your Linux distribution and release.

For Kali Linux, use Kali's official repository configuration. Avoid mixing Kali repositories with Ubuntu or Debian release repositories, as this can cause dependency conflicts and system instability.

---

# PART 2: APT PACKAGE MANAGEMENT

## 3. What Is APT?

APT stands for Advanced Package Tool.

It is a package management system used by Debian-based Linux distributions.

APT helps users install, update, upgrade, search, and remove software.

Common APT commands:

```bash
apt update
apt upgrade
apt install
apt remove
apt purge
apt search
apt show
```

Most system-wide package operations require administrator privileges, so they are commonly executed with `sudo`.

---

## 4. apt update

The `apt update` command refreshes the local package metadata using the configured repositories.

It does not upgrade installed software.

Syntax:

```bash
sudo apt update
```

What happens?

1. APT contacts configured repositories.
2. It downloads updated package information.
3. It refreshes the local package index.
4. It learns about available package versions and updates.

Why is it important?

Before installing software or checking available updates, refresh the package metadata.

Example:

```bash
sudo apt update
```

Remember:

`apt update` = Refresh package information.

It does not mean updating all installed applications.

---

## 5. apt upgrade

The `apt upgrade` command installs available upgrades for installed packages.

Syntax:

```bash
sudo apt upgrade
```

What happens?

- APT checks available package upgrades.
- It calculates dependencies.
- It downloads newer package versions.
- It installs the available upgrades.

Example:

```bash
sudo apt update
sudo apt upgrade
```

The first command refreshes package information, while the second installs available upgrades.

### Difference Between update and upgrade

| Command | Function |
|---|---|
| `apt update` | Refreshes package metadata |
| `apt upgrade` | Upgrades installed packages |

Important:

On Kali Linux, which is a rolling-release distribution, you may also encounter:

```bash
sudo apt full-upgrade
```

`full-upgrade` can install upgrades that require removing or changing installed packages to resolve dependencies.

Review the proposed changes carefully before confirming, especially if APT wants to remove important packages.

---

## 6. apt install

The `apt install` command installs software packages.

Syntax:

```bash
sudo apt install package_name
```

Example:

```bash
sudo apt install nmap
```

Install multiple packages:

```bash
sudo apt install curl wget git
```

Install a specific package version when available:

```bash
sudo apt install package_name=version
```

APT automatically handles many dependencies.

### What Happens During Installation?

Suppose you install a tool that depends on three additional libraries.

APT will:

1. Find the requested package.
2. Identify its dependencies.
3. Download the required packages.
4. Install them.
5. Configure the software.

This makes package installation easier than manually downloading every required file.

---

## 7. apt remove

The `apt remove` command uninstalls a package.

Syntax:

```bash
sudo apt remove package_name
```

Example:

```bash
sudo apt remove nmap
```

Important:

`apt remove` removes the package but generally leaves its system-wide configuration files behind.

This can be useful if you plan to reinstall the application later and want to preserve its configuration.

---

## 8. apt purge

The `apt purge` command removes a package along with its package-managed system configuration files.

Syntax:

```bash
sudo apt purge package_name
```

Example:

```bash
sudo apt purge nmap
```

### Difference Between remove and purge

| Command | What it removes |
|---|---|
| `apt remove` | Package files, generally retaining configuration |
| `apt purge` | Package files and package-managed configuration |

Note:

Neither command guarantees removal of every file created by an application. User data, files stored in home directories, and unrelated dependencies may remain.

---

## 9. apt search

The `apt search` command searches package metadata for software.

Syntax:

```bash
apt search keyword
```

Example:

```bash
apt search nmap
```

Search for a networking tool:

```bash
apt search network
```

Search for a text editor:

```bash
apt search editor
```

This helps you discover packages available through your configured repositories.

---

## 10. apt show

The `apt show` command displays detailed information about a package.

Syntax:

```bash
apt show package_name
```

Example:

```bash
apt show nmap
```

It may display:

- Package name.
- Version.
- Maintainer.
- Architecture.
- Package size.
- Dependencies.
- Description.
- Repository information.

Use this command before installing unfamiliar packages to understand what they provide.

---

# PART 3: DPKG PACKAGE MANAGEMENT

## 11. What Is dpkg?

`dpkg` stands for Debian Package.

It is the lower-level package management tool used to install, inspect, and remove Debian packages.

APT uses lower-level package management functionality to perform many installation and removal operations.

The main difference:

- APT manages repositories and resolves dependencies.
- dpkg directly manages Debian package files and installed package information.

---

## 12. dpkg -l

The `dpkg -l` command lists installed and known packages.

Example:

```bash
dpkg -l
```

Search for a particular package:

```bash
dpkg -l | grep nmap
```

Display the package status and version.

Important status indicators include:

- `ii`: Package is installed and configured.
- `rc`: Package was removed, but configuration files remain.
- `un`: Package is not installed.

Example:

```bash
dpkg -l | grep curl
```

---

## 13. dpkg -L

The `dpkg -L` command lists files installed by a particular package.

Syntax:

```bash
dpkg -L package_name
```

Example:

```bash
dpkg -L curl
```

It can show:

- Executable locations.
- Configuration files.
- Documentation.
- Libraries.
- Other package-owned files.

Find the executable location:

```bash
dpkg -L curl | grep /bin/
```

This is useful when you want to understand where a package has installed its files.

---

## 14. Other Useful dpkg Commands

### 14.1 Install a Local .deb Package

```bash
sudo dpkg -i package.deb
```

This installs a local Debian package.

Unlike APT, dpkg does not automatically resolve and download missing dependencies.

If dependencies are missing, you may need:

```bash
sudo apt --fix-broken install
```

### 14.2 Remove a Package

```bash
sudo dpkg -r package_name
```

### 14.3 Display Package Information

```bash
dpkg -s package_name
```

### 14.4 Find Which Installed Package Owns a File

```bash
dpkg -S /usr/bin/curl
```

This identifies the installed package that owns the specified file.

---

# PART 4: PACKAGE DEPENDENCIES

## 15. What Are Package Dependencies?

A dependency is another software package or library required by an application to function correctly.

Many Linux applications depend on additional libraries and tools.

Example:

Suppose Application A requires:

- Library B.
- Library C.
- Package D.

Without these dependencies, Application A may fail to run.

### 15.1 Types of Dependencies

**Required dependencies**

Packages that must be installed for the software to work correctly.

**Recommended packages**

Packages that provide useful functionality and are commonly installed alongside the requested software.

**Suggested packages**

Optional packages that provide additional features.

### 15.2 How APT Handles Dependencies

When installing software:

```bash
sudo apt install package_name
```

APT:

1. Checks package metadata.
2. Identifies required dependencies.
3. Checks which dependencies are already installed.
4. Downloads missing packages.
5. Installs and configures the required packages.

### 15.3 View Package Dependencies

Use:

```bash
apt show nmap
```

You can inspect the Depends, Recommends, and Suggests fields.

You can also use:

```bash
apt-cache depends nmap
```

To inspect reverse dependencies:

```bash
apt-cache rdepends nmap
```

Reverse dependencies are packages that depend on the selected package.

### 15.4 Remove Unnecessary Dependencies

APT can identify packages that were automatically installed and are no longer required.

Use:

```bash
sudo apt autoremove
```

Review the proposed removal list before confirming.

Do not blindly remove packages, because you should understand what APT proposes to uninstall.

---

# PART 5: SOFTWARE UPDATES AND SECURITY

## 16. Software Updates and Security Patches

Software updates are important for maintaining system stability, performance, and security.

Developers and distribution maintainers release updates to:

- Fix software bugs.
- Repair security vulnerabilities.
- Improve performance.
- Add features.
- Improve compatibility.
- Resolve dependency issues.

### 16.1 What Is a Security Patch?

A security patch is an update that fixes a security vulnerability in software.

For example:

An application may contain a vulnerability that allows an attacker to execute unauthorized commands.

The software developer releases a security update to fix the vulnerability.

Installing the update reduces exposure to that known vulnerability.

### 16.2 Check Available Updates

First, refresh package metadata:

```bash
sudo apt update
```

List upgradable packages:

```bash
apt list --upgradable
```

Upgrade packages:

```bash
sudo apt upgrade
```

### 16.3 Why Regular Updates Matter in Cybersecurity

Outdated software may contain publicly known vulnerabilities.

Attackers can exploit vulnerable software to:

- Gain unauthorized access.
- Execute malicious code.
- Escalate privileges.
- Steal information.
- Disrupt services.

Regularly updating your system reduces the risk of attacks based on known vulnerabilities.

---

# PART 6: INSTALLING SOFTWARE SAFELY

## 17. Installing Software From Trusted Sources

Not every website or download source is safe.

Downloading and executing software from an unknown source can expose your system to malware.

### 17.1 Trusted Software Sources

Prefer:

1. Official distribution repositories.
2. Official software vendor websites.
3. Verified project release pages.
4. Trusted and documented third-party repositories.

For Kali Linux, prefer official Kali repositories whenever the required package is available there.

### 17.2 Why Random Installation Scripts Can Be Dangerous

You may encounter commands like:

```bash
curl https://example.com/install.sh | bash
```

This downloads a script and immediately executes it using Bash.

Why is this risky?

- You may not know what the script does.
- It may execute destructive commands.
- It may download additional malicious files.
- It may change system configurations.
- It may collect sensitive information.
- It may execute commands with your current user's privileges.

If executed using `sudo`, the script may gain administrative privileges.

### Safer Approach

Download the script first:

```bash
curl -O https://example.com/install.sh
```

Inspect its contents:

```bash
less install.sh
```

Search for suspicious commands:

```bash
grep -nE 'sudo|rm -rf|curl|wget|chmod|bash' install.sh
```

This search is only a starting point, not a security guarantee.

Verify the source and integrity of the script before executing it.

Never assume a script is safe merely because it is hosted on a popular website.

---

## 18. Verifying Downloads and Checksums

A checksum is a value calculated from the contents of a file using a hash algorithm.

It helps verify whether a downloaded file matches an expected version.

Common hashing algorithms:

- MD5
- SHA-1
- SHA-256
- SHA-512

For security-sensitive verification, prefer SHA-256 or stronger modern algorithms.

### 18.1 What Is SHA-256?

SHA-256 is a cryptographic hash function that produces a 256-bit hash value.

Even a small change in a file generally produces a different hash.

Example:

```bash
sha256sum file.iso
```

Output:

```text
a1b2c3d4... file.iso
```

The displayed hash is illustrative.

### 18.2 Verify a Download

Suppose you download a Linux ISO file and the official website provides its expected SHA-256 checksum.

Generate your local checksum:

```bash
sha256sum kali-linux.iso
```

Compare it with the checksum published by the official source.

If both values match exactly, the file matches the published checksum.

### 18.3 Verify Using a Checksum File

If the official source provides a checksum file:

```bash
sha256sum -c SHA256SUMS
```

This checks files against the expected hashes listed in that file.

Important:

A matching checksum confirms integrity relative to the checksum you obtained. It does not independently prove authenticity if an attacker could also replace the checksum file.

For stronger authenticity verification, use the official project's cryptographic signature and trusted public key.

---

# PART 7: ENVIRONMENT VARIABLES AND PATH

## 19. What Are Environment Variables?

Environment variables are named values maintained by the operating system or shell and made available to running processes.

They provide configuration information to programs.

Examples:

- `PATH`
- `HOME`
- `USER`
- `SHELL`
- `PWD`
- `LANG`

Display all environment variables:

```bash
printenv
```

Display a particular variable:

```bash
echo $HOME
```

Display the current user:

```bash
echo $USER
```

Display the shell:

```bash
echo $SHELL
```

---

## 20. What Is PATH?

`PATH` is an environment variable that contains a list of directories where the shell searches for executable commands.

When you type a command, the shell searches these directories to locate the executable.

Display PATH:

```bash
echo $PATH
```

Example:

```text
/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin
```

The colon (`:`) separates individual directory paths.

### 20.1 How PATH Works

Suppose you execute:

```bash
python3
```

The shell searches directories listed in `PATH` to locate the Python executable.

If the executable is found, the shell runs it.

If the executable cannot be located, you may receive:

```text
bash: python3: command not found
```

### 20.2 Locate an Executable

Use:

```bash
which python3
```

Or:

```bash
command -v python3
```

The `command -v` command is generally preferable for checking whether a command is available in the current shell.

### 20.3 Add a Directory to PATH Temporarily

Example:

```bash
export PATH="$PATH:$HOME/mytools"
```

This adds the `mytools` directory to PATH for the current shell and its child processes.

It does not permanently modify the PATH for future terminal sessions.

### 20.4 Make PATH Changes Persistent

For Bash users, add the export command to:

```text
~/.bashrc
```

Example:

```bash
echo 'export PATH="$PATH:$HOME/mytools"' >> ~/.bashrc
```

Reload the configuration:

```bash
source ~/.bashrc
```

Verify:

```bash
echo $PATH
```

Important:

Only add directories you trust to PATH. If an untrusted directory appears early in PATH, a malicious executable could be run instead of the intended command.

---

# PART 8: TROUBLESHOOTING PACKAGE INSTALLATION

## 21. Common Package Management Errors

Package installation may fail because of repository problems, dependency conflicts, interrupted installations, network errors, or insufficient permissions.

### 21.1 Package Not Found

Example:

```text
E: Unable to locate package example
```

Possible reasons:

- Incorrect package name.
- Package is unavailable in configured repositories.
- Package metadata is outdated.
- Repository configuration is incorrect.

Troubleshooting:

```bash
sudo apt update
apt search example
apt show example
```

Check the package name and configured repositories.

### 21.2 Dependency Problems

Example:

```text
The following packages have unmet dependencies
```

Possible reasons:

- Conflicting package versions.
- Missing dependencies.
- Incompatible repositories.
- Interrupted package installation.

Try:

```bash
sudo apt --fix-broken install
```

This asks APT to repair broken dependency relationships.

Review the proposed changes before confirming.

### 21.3 Interrupted Package Installation

If package installation was interrupted, some packages may remain unpacked but unconfigured.

Try:

```bash
sudo dpkg --configure -a
```

This attempts to configure unpacked packages.

Then:

```bash
sudo apt --fix-broken install
```

### 21.4 Repository Errors

Possible causes:

- Incorrect repository URL.
- Network connectivity problems.
- Expired or invalid repository signing information.
- Unsupported distribution release.
- Incorrect repository configuration.

Inspect repository configuration:

```bash
cat /etc/apt/sources.list
```

Also inspect:

```bash
ls /etc/apt/sources.list.d/
```

Then refresh package information:

```bash
sudo apt update
```

Do not disable package signature verification as a workaround.

### 21.5 Permission Denied

Example:

```text
Permission denied
```

Possible reason:

The operation requires administrator privileges.

For system-wide package operations, use:

```bash
sudo apt install package_name
```

### 21.6 Package Manager Lock

Example:

```text
Could not get lock /var/lib/dpkg/lock-frontend
```

Possible reasons:

- Another APT operation is running.
- Automatic updates are running.
- Another package management process is using dpkg.

Check for active package processes:

```bash
ps aux | grep -E 'apt|dpkg'
```

Wait for the existing package operation to finish.

Important:

Do not immediately delete lock files. Doing so while another package operation is active can damage package management state.

---

# PART 9: PRACTICAL LABS

Perform these exercises in your Kali Linux virtual machine.

## LAB 1 — Update Package Metadata

Objective: Understand how APT retrieves repository information.

Run:

```bash
sudo apt update
```

Tasks:

1. Observe the repository URLs.
2. Identify the package metadata being downloaded.
3. Check whether any repository errors occur.
4. Explain why this command is important before installing software.

## LAB 2 — Install a Harmless Utility

Objective: Learn how to install a package.

Use the `tree` utility.

First, search for it:

```bash
apt search tree
```

Inspect package information:

```bash
apt show tree
```

Install:

```bash
sudo apt install tree
```

Verify installation:

```bash
tree --version
```

Try it:

```bash
tree ~
```

## LAB 3 — Remove and Purge a Package

Objective: Understand package removal.

Remove the utility:

```bash
sudo apt remove tree
```

Check whether it is installed:

```bash
dpkg -l | grep tree
```

If you want to remove its package-managed configuration too:

```bash
sudo apt purge tree
```

Remember: `remove` and `purge` do not necessarily delete every user-created file.

## LAB 4 — Find Which Package Provides a Command

Objective: Identify the package associated with an installed executable.

Check a command:

```bash
command -v curl
```

Suppose the output is:

```text
/usr/bin/curl
```

Find the owning package:

```bash
dpkg -S /usr/bin/curl
```

Try with:

```bash
dpkg -S /usr/bin/ls
```

Tasks:

1. Find the executable location.
2. Identify its owning package.
3. Explain why a command name and package name may be different.

For a command that is not installed, you can use `apt-file` to search repository file lists.

Install it:

```bash
sudo apt install apt-file
```

Update its file index:

```bash
sudo apt-file update
```

Search for a file:

```bash
apt-file search bin/command_name
```

## LAB 5 — Inspect Installed Packages

Objective: Learn to inspect package information.

Run:

```bash
dpkg -l
```

Search for a particular package:

```bash
dpkg -l | grep curl
```

Inspect package details:

```bash
apt show curl
```

List files installed by the package:

```bash
dpkg -L curl
```

Tasks:

1. Find the installed version.
2. Identify the package architecture.
3. Find the executable location.
4. Identify its dependencies.

## LAB 6 — Check Available Updates

Objective: Understand package updates.

Refresh metadata:

```bash
sudo apt update
```

List available upgrades:

```bash
apt list --upgradable
```

Inspect a package:

```bash
apt show package_name
```

Tasks:

1. Find how many packages have upgrades available.
2. Identify one package that has an available update.
3. Check its installed and candidate versions using:

```bash
apt-cache policy package_name
```

## LAB 7 — Verify a Download Using SHA-256

Objective: Learn basic download integrity verification.

Create a test file:

```bash
echo "Linux security practice" > test.txt
```

Calculate its hash:

```bash
sha256sum test.txt
```

Save the hash:

```bash
sha256sum test.txt > SHA256SUMS
```

Verify:

```bash
sha256sum -c SHA256SUMS
```

Expected result:

```text
test.txt: OK
```

Modify the file:

```bash
echo "Modified content" >> test.txt
```

Verify again:

```bash
sha256sum -c SHA256SUMS
```

Expected result:

```text
test.txt: FAILED
```

This demonstrates how a file modification changes its hash.

Clean up:

```bash
rm test.txt SHA256SUMS
```

## LAB 8 — Understand Environment Variables

Objective: Learn how environment variables work.

Display all variables:

```bash
printenv
```

Inspect important variables:

```bash
echo $HOME
echo $USER
echo $SHELL
echo $PATH
```

Create a temporary variable:

```bash
export MYNAME="Linux Student"
```

Display it:

```bash
echo $MYNAME
```

Remove it:

```bash
unset MYNAME
```

Check it again:

```bash
echo $MYNAME
```

## LAB 9 — Diagnose a Missing Command

Objective: Understand how to troubleshoot a command-not-found error.

Try:

```bash
tree --version
```

If the command is unavailable, inspect:

```bash
command -v tree
```

Search the package repository:

```bash
apt search tree
```

Inspect the package:

```bash
apt show tree
```

Install it:

```bash
sudo apt install tree
```

Verify:

```bash
tree --version
```

Tasks:

1. Understand why the command was unavailable.
2. Identify which package provides it.
3. Install the package.
4. Verify that the command works.

---

# PART 10: IMPORTANT COMMAND REVISION

## APT Commands

| Command | Purpose |
|---|---|
| `sudo apt update` | Refresh package metadata |
| `sudo apt upgrade` | Upgrade installed packages |
| `sudo apt full-upgrade` | Upgrade packages while resolving changing dependencies |
| `sudo apt install` | Install packages |
| `sudo apt remove` | Remove packages |
| `sudo apt purge` | Remove packages and package-managed configuration |
| `apt search` | Search for packages |
| `apt show` | Display package details |
| `apt list --upgradable` | List available package upgrades |
| `sudo apt autoremove` | Remove automatically installed packages no longer needed |
| `sudo apt --fix-broken install` | Attempt to repair broken dependencies |

## DPKG Commands

| Command | Purpose |
|---|---|
| `dpkg -l` | List packages |
| `dpkg -L` | List files installed by a package |
| `dpkg -i` | Install a local `.deb` package |
| `dpkg -r` | Remove a package |
| `dpkg -s` | Display package status |
| `dpkg -S` | Find the package owning a file |
| `sudo dpkg --configure -a` | Configure unpacked packages |

## Download Verification Commands

| Command | Purpose |
|---|---|
| `sha256sum file` | Calculate SHA-256 hash |
| `sha512sum file` | Calculate SHA-512 hash |
| `sha256sum -c file` | Verify hashes against a checksum file |
| `less file` | Inspect file contents |
| `file filename` | Identify file type |

## Environment Variable Commands

| Command | Purpose |
|---|---|
| `printenv` | Display environment variables |
| `env` | Display or run commands with environment variables |
| `echo $PATH` | Display PATH |
| `echo $HOME` | Display home directory |
| `export NAME=value` | Set an environment variable for the shell and child processes |
| `unset NAME` | Remove an environment variable |
| `which command` | Locate an executable using PATH |
| `command -v command` | Check how the shell resolves a command |
| `source ~/.bashrc` | Reload Bash configuration |

---

# PART 11: KNOWLEDGE CHECK

Before moving to Phase 6, make sure you can answer these questions.

1. What is a software package?
2. What is package management?
3. What is a software repository?
4. What is the difference between official and third-party repositories?
5. What is APT?
6. What happens when you execute `apt update`?
7. What is the difference between `apt update` and `apt upgrade`?
8. How do you install software using APT?
9. What is the difference between `apt remove` and `apt purge`?
10. What is dpkg?
11. What is the difference between APT and dpkg?
12. What is the purpose of `dpkg -l`?
13. What does `dpkg -L` display?
14. What are package dependencies?
15. What is the purpose of `apt autoremove`?
16. What is a security patch?
17. Why should you install software from trusted sources?
18. Why can executing random installation scripts be dangerous?
19. What is a checksum?
20. What is SHA-256?
21. Does a matching checksum independently prove that a download is authentic?
22. What is an environment variable?
23. What is PATH?
24. How does Linux locate an executable command?
25. How would you troubleshoot a package installation failure?
26. What would you do if APT reports unmet dependencies?
27. What should you do if the package manager reports that a lock is held?

---

# PART 12: PHASE 5 COMPLETION CHECKLIST

- [ ] Understand packages and repositories.
- [ ] Understand APT package management.
- [ ] Use `apt update`.
- [ ] Use `apt upgrade`.
- [ ] Install software using `apt install`.
- [ ] Remove software using `apt remove`.
- [ ] Purge software using `apt purge`.
- [ ] Search for packages using `apt search`.
- [ ] Inspect packages using `apt show`.
- [ ] Inspect installed packages using `dpkg -l`.
- [ ] List package files using `dpkg -L`.
- [ ] Understand package dependencies.
- [ ] Understand repository configuration.
- [ ] Check available updates.
- [ ] Understand security patches.
- [ ] Install software from trusted sources.
- [ ] Verify downloads using SHA-256.
- [ ] Understand the risks of random installation scripts.
- [ ] Troubleshoot package installation failures.
- [ ] Understand environment variables.
- [ ] Understand and configure PATH.

# WHY THIS PHASE MATTERS IN CYBERSECURITY

Package management is an important skill for cybersecurity professionals.

You will use these skills for:

1. **Security Tool Installation:** Installing Nmap, Wireshark, Burp Suite dependencies, and other security utilities.
2. **System Maintenance:** Keeping Kali Linux and its installed software updated.
3. **Software Verification:** Checking downloaded files before executing them.
4. **Dependency Management:** Understanding libraries and packages required by security tools.
5. **System Troubleshooting:** Fixing package conflicts and installation errors.
6. **Command Execution:** Understanding PATH and how Linux locates executable programs.
7. **Supply Chain Security:** Recognizing the risks of untrusted repositories and installation scripts.

**Your goal:** Become comfortable installing, inspecting, updating, verifying, and troubleshooting Linux software without blindly executing commands.
