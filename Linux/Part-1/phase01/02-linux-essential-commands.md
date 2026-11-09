
# Part 1: Linux Fundamentals

# Phase 2 — Essential Linux Commands

## Table of Contents

1. Introduction to Linux Commands
2. Understanding Linux Command Syntax
3. Navigation and File Management
   - `pwd`
   - `ls`, `ls -la`
   - `cd`
   - `tree`
   - `mkdir`
   - `touch`
   - `cp`
   - `mv`
   - `rm`, `rmdir`
   - Absolute and Relative Paths
   - Hidden Files and Directories
   - Wildcards
4. Reading and Editing Files
   - `cat`
   - `less`
   - `head`
   - `tail`
   - `tail -f`
   - `nano`
   - `vim`
   - `file`
   - `stat`
   - `wc`
   - `sort`
   - `uniq`
   - `cut`
   - `paste`
   - `tr`
   - `tee`
5. Searching and Finding Information
   - `find`
   - `grep`
   - `grep -i`, `grep -r`, `grep -n`
   - `locate`
   - `which`
   - `whereis`
   - `command -v`
   - Searching Logs and Configuration Files
   - Combining Commands to Filter Results
6. Practical Exercises
7. Quick Revision
8. Interview and Self-Assessment Questions
9. Learning Checklist

---

# 1. Introduction to Linux Commands

## 1.1 What Is a Linux Command?

A Linux command is an instruction given to the operating system through a command-line interface.

Commands allow users to perform different operations, such as:

- Creating files and directories.
- Copying and moving files.
- Deleting unwanted files.
- Reading and editing files.
- Searching for information.
- Managing processes.
- Configuring networks.
- Installing software.
- Monitoring system activities.

For example:

```bash
pwd
```

This command displays your current working directory.

Another example:

```bash
mkdir linux-practice
```

This creates a directory named `linux-practice`.

Linux commands are especially important because many administrative and cybersecurity tasks are performed through the terminal.

## 1.2 How Does a Linux Command Work?

When you enter a command in the terminal, the following process generally occurs:

1. You type a command.
2. The shell receives the command.
3. The shell interprets the command and its arguments.
4. The shell locates the corresponding command or executable.
5. The command executes.
6. The result is displayed or redirected somewhere else.

Example:

```bash
ls -la /home
```

Here:

- `ls` is the command.
- `-la` contains command options.
- `/home` is the target directory.

The command lists detailed information about the contents of `/home`, including hidden entries.

## 1.3 Types of Linux Commands

Linux commands can be classified into different categories.

### 1. Built-in Commands

Built-in commands are implemented directly inside the shell.

Examples:

```bash
cd
echo
pwd
alias
export
```

Some commands, such as `pwd` and `echo`, may also exist as external programs.

### 2. External Commands

External commands are separate executable programs installed on the system.

Examples:

```bash
ls
cp
mv
grep
find
```

Their executable files are commonly located in directories such as:

```text
/usr/bin
/usr/sbin
/bin
/sbin
```

On modern distributions, some of these directories are symbolic links into `/usr`.

### 3. Commands Requiring Elevated Privileges

Some administrative operations require root privileges.

For example:

```bash
sudo apt update
```

Here, `sudo` executes the command with elevated privileges, subject to the user's authorization.

Not every Linux command requires `sudo`.

> Important: Avoid using `sudo` unnecessarily. Running commands with elevated privileges increases the potential impact of mistakes.

---

# 2. Understanding Linux Command Syntax

Before learning individual commands, understand their general structure.

## 2.1 General Syntax

```text
command [options] [arguments]
```

Explanation:

| Component | Meaning |
|---|---|
| Command | Program or shell instruction |
| Options | Modify the command's behavior |
| Arguments | Specify the target or input |

Example:

```bash
ls -l /home
```

- `ls`: Command.
- `-l`: Option.
- `/home`: Argument.

## 2.2 Short and Long Options

Many Linux commands support short and long options.

Short option:

```bash
ls -a
```

Long option:

```bash
ls --all
```

Both display hidden directory entries.

Some options can be combined:

```bash
ls -lah
```

This combines:

- `-l`: Long listing format.
- `-a`: Include hidden entries.
- `-h`: Human-readable file sizes.

## 2.3 Command Case Sensitivity

Linux commands and filenames are generally case-sensitive.

For example:

```bash
ls
```

Works.

```bash
LS
```

Usually produces a command-not-found error because `LS` is different from `ls`.

Similarly:

```text
report.txt
Report.txt
REPORT.txt
```

Can represent three different filenames.

## 2.4 Getting Command Help

You do not need to memorize every option.

Linux provides documentation mechanisms.

### Using --help

```bash
ls --help
```

Displays command usage and available options.

### Using man

```bash
man ls
```

Opens the manual page for `ls`.

Useful navigation keys:

| Key | Purpose |
|---|---|
| `Space` | Next page |
| `b` | Previous page |
| `/word` | Search for a word |
| `n` | Next search result |
| `q` | Quit |

### Using help

```bash
help cd
```

Displays help for the Bash built-in `cd`.

The `help` command is especially useful for shell built-ins.

---

# 3. Navigation and File Management

File and directory management is one of the most important Linux fundamentals.

You must understand how to navigate directories, create files, copy data, rename files, and remove unwanted content.

## 3.1 pwd — Print Working Directory

### What Is pwd?

`pwd` stands for Print Working Directory.

It displays the absolute path of your current working directory.

### Syntax

```bash
pwd [OPTION]
```

### Basic Example

```bash
pwd
```

Expected output:

```text
/home/pulok
```

The output depends on your username and current location.

### Important Options

```bash
pwd -L
```

Displays the logical working directory, normally preserving symbolic-link paths.

```bash
pwd -P
```

Displays the physical directory path by resolving symbolic links.

### Practical Example

```bash
cd /etc
pwd
```

Expected output:

```text
/etc
```

### Why Is pwd Important?

It helps you:

- Identify your current location.
- Avoid executing file operations in the wrong directory.
- Understand absolute paths.
- Navigate large filesystem structures.

### Cybersecurity Relevance

Before executing file-management commands during a security investigation, verify your working directory.

For example:

```bash
pwd
```

This reduces the possibility of modifying or deleting files in the wrong location.

---

## 3.2 ls — List Directory Contents

### What Is ls?

`ls` displays files and directories.

It is one of the most frequently used Linux commands.

### Syntax

```bash
ls [OPTIONS] [DIRECTORY]
```

### Basic Example

```bash
ls
```

Displays files and directories in the current location.

### Important Options

| Option | Purpose |
|---|---|
| `-l` | Long listing format |
| `-a` | Include hidden entries |
| `-h` | Human-readable sizes |
| `-R` | Recursively list subdirectories |
| `-t` | Sort by modification time |
| `-r` | Reverse sorting order |
| `-S` | Sort by file size |
| `-d` | List directory itself instead of its contents |
| `-i` | Display inode numbers |

### Example 1: Detailed Listing

```bash
ls -l
```

Example output:

```text
drwxr-xr-x 2 pulok pulok 4096 Nov 9 10:00 Documents
-rw-r--r-- 1 pulok pulok  120 Nov 9 10:10 notes.txt
```

Understanding the output:

| Field | Meaning |
|---|---|
| `drwxr-xr-x` | File type and permissions |
| `2` | Hard-link count |
| `pulok` | Owner |
| `pulok` | Group |
| `4096` | Reported size in bytes |
| `Nov 9 10:00` | Modification time |
| `Documents` | Filename |

### Example 2: Show Hidden Files

```bash
ls -a
```

Displays hidden files and directories, including `.` and `..`.

### Example 3: Detailed Listing Including Hidden Files

```bash
ls -la
```

Combines long listing and hidden entries.

### Example 4: Human-Readable File Sizes

```bash
ls -lh
```

Example:

```text
-rw-r--r-- 1 pulok pulok 2.5K Nov 9 10:10 notes.txt
```

### Example 5: Sort by Modification Time

```bash
ls -lt
```

Shows recently modified entries first.

### Example 6: List a Specific Directory

```bash
ls -la /var/log
```

Displays the detailed contents of `/var/log`.

### Example 7: Recursive Listing

```bash
ls -R
```

Displays directory contents recursively.

> Security note: Hidden files are not automatically protected. A hidden file can still be read or modified by anyone who has sufficient permissions.

---

## 3.3 cd — Change Directory

### What Is cd?

`cd` stands for Change Directory.

It changes your current working directory.

It is generally a Bash built-in command.

### Syntax

```bash
cd [DIRECTORY]
```

### Example 1: Move to Home Directory

```bash
cd ~
```

### Example 2: Move to Root Directory

```bash
cd /
```

### Example 3: Move to /etc

```bash
cd /etc
```

### Example 4: Move to Parent Directory

```bash
cd ..
```

### Example 5: Move Two Levels Up

```bash
cd ../..
```

### Example 6: Move to Previous Directory

```bash
cd -
```

This switches to the previous working directory.

### Example 7: Return to Home Directory

```bash
cd
```

Running `cd` without an argument normally moves you to your home directory.

### Example 8: Navigate Using an Absolute Path

```bash
cd /var/log
```

### Example 9: Navigate Using a Relative Path

Suppose your current directory is:

```text
/home/pulok
```

You can enter:

```bash
cd Documents
```

This moves to:

```text
/home/pulok/Documents
```

### Verification

```bash
pwd
```

### Common Mistakes

Incorrect:

```bash
cd /home/pulok/Downloads/file.txt
```

If `file.txt` is a regular file, it cannot be used as a directory.

Correct:

```bash
cd /home/pulok/Downloads
```

---

## 3.4 tree — Display Directory Structure

### What Is tree?

`tree` displays files and directories in a hierarchical tree-like format.

It is useful for understanding complex directory structures.

### Installation

On Ubuntu, Debian, and Kali:

```bash
sudo apt update
sudo apt install tree
```

### Syntax

```bash
tree [OPTIONS] [DIRECTORY]
```

### Example 1

```bash
tree
```

Displays the current directory structure.

Example output:

```text
.
├── Documents
│   ├── notes.txt
│   └── report.pdf
├── Downloads
│   └── image.png
└── Projects
    ├── python
    └── web-security
```

### Important Options

| Option | Purpose |
|---|---|
| `-a` | Include hidden files |
| `-L N` | Limit directory depth |
| `-d` | Display directories only |
| `-f` | Display full path for each entry |
| `-h` | Human-readable file sizes |
| `-s` | Display file sizes |

### Example 2: Show Only Directories

```bash
tree -d
```

### Example 3: Limit the Depth

```bash
tree -L 2
```

Displays the current directory and its subdirectories up to two levels.

### Example 4: Include Hidden Files

```bash
tree -a
```

### Example 5: Show Full Paths

```bash
tree -f
```

### Cybersecurity Relevance

`tree` is useful for:

- Organizing security projects.
- Understanding application directories.
- Reviewing lab environments.
- Inspecting directory structures.
- Documenting project files.

---

## 3.5 mkdir — Create Directories

### What Is mkdir?

`mkdir` stands for Make Directory.

It creates new directories.

### Syntax

```bash
mkdir [OPTIONS] DIRECTORY
```

### Example 1: Create a Directory

```bash
mkdir linux-lab
```

Creates a directory named `linux-lab`.

### Example 2: Create Multiple Directories

```bash
mkdir python bash networking
```

Creates three directories in the current location.

### Example 3: Create Nested Directories

```bash
mkdir -p cybersecurity/linux/commands
```

The `-p` option creates missing parent directories automatically.

Without `-p`, creating a nested directory may fail if its parent does not exist.

### Example 4: Create Directories with Verbose Output

```bash
mkdir -v practice
```

Displays a message when the directory is created.

### Example 5: Set Permissions During Creation

```bash
mkdir -m 750 secure-lab
```

Creates the directory with the requested permissions, subject to the system's filesystem and permission rules.

### Cybersecurity Relevance

Use `mkdir -p` to organize:

- Pentesting reports.
- Security research.
- Web application testing projects.
- Python scripts.
- Bash automation.
- Lab documentation.

---

## 3.6 touch — Create Files

### What Is touch?

`touch` creates an empty file if it does not already exist.

If the file already exists, it normally updates its access and modification timestamps.

### Syntax

```bash
touch [OPTIONS] FILE
```

### Example 1: Create an Empty File

```bash
touch notes.txt
```

### Example 2: Create Multiple Files

```bash
touch file1.txt file2.txt file3.txt
```

### Example 3: Create a File Inside a Directory

```bash
touch linux-lab/commands.txt
```

The parent directory must already exist.

### Example 4: Avoid Creating a Missing File

```bash
touch -c notes.txt
```

The `-c` option prevents creation of a file that does not exist.

### Verification

```bash
ls -l
```

### Important Point

`touch` does not normally erase the contents of an existing file.

However, it can change its timestamps.

---

## 3.7 cp — Copy Files and Directories

### What Is cp?

`cp` stands for Copy.

It copies files and, with suitable options, directories.

### Syntax

```bash
cp [OPTIONS] SOURCE DESTINATION
```

### Example 1: Copy a File

```bash
cp notes.txt backup.txt
```

Creates `backup.txt` containing a copy of `notes.txt`.

### Example 2: Copy a File into Another Directory

```bash
cp notes.txt Documents/
```

### Example 3: Copy Multiple Files

```bash
cp file1.txt file2.txt Documents/
```

Copies both files into `Documents`.

### Example 4: Copy a Directory Recursively

```bash
cp -r project backup-project
```

The `-r` option recursively copies the directory and its contents.

### Example 5: Preserve File Attributes

```bash
cp -p notes.txt backup.txt
```

Attempts to preserve mode, ownership, and timestamps where permitted.

### Example 6: Display Copy Operations

```bash
cp -v notes.txt backup.txt
```

### Example 7: Interactive Copying

```bash
cp -i notes.txt backup.txt
```

Prompts before overwriting an existing destination.

### Example 8: Archive-Style Copying

```bash
cp -a project project-backup
```

Archive mode preserves important attributes and symbolic links while copying recursively.

### Important Options

| Option | Purpose |
|---|---|
| `-r` | Copy directories recursively |
| `-R` | Recursive copying |
| `-i` | Ask before overwriting |
| `-v` | Verbose output |
| `-p` | Preserve mode, ownership where permitted, and timestamps |
| `-a` | Archive mode |

> Warning: Copying a large directory can consume considerable storage space. Always check the destination before copying.

---

## 3.8 mv — Move or Rename Files

### What Is mv?

`mv` moves files and directories from one location to another.

It can also rename files and directories.

### Syntax

```bash
mv [OPTIONS] SOURCE DESTINATION
```

### Example 1: Rename a File

```bash
mv old.txt new.txt
```

Renames `old.txt` to `new.txt`.

### Example 2: Move a File

```bash
mv notes.txt Documents/
```

Moves `notes.txt` into `Documents`.

### Example 3: Move and Rename

```bash
mv notes.txt Documents/linux-notes.txt
```

Moves the file and gives it a new name.

### Example 4: Move a Directory

```bash
mv project backup-project
```

Renames the directory in the same parent directory.

### Example 5: Interactive Move

```bash
mv -i notes.txt Documents/
```

Prompts before overwriting an existing destination.

### Example 6: Verbose Output

```bash
mv -v notes.txt Documents/
```

### Important Options

| Option | Purpose |
|---|---|
| `-i` | Prompt before overwriting |
| `-f` | Do not prompt before overwriting |
| `-n` | Do not overwrite an existing destination |
| `-v` | Display operations |

> Warning: Moving a file across filesystems may involve copying it to the destination and deleting the original. Check the destination before performing important moves.

---

## 3.9 rm — Remove Files and Directories

### What Is rm?

`rm` stands for Remove.

It deletes files and, with appropriate options, directories.

### Syntax

```bash
rm [OPTIONS] FILE
```

### Example 1: Remove a File

```bash
rm notes.txt
```

Deletes `notes.txt`.

### Example 2: Interactive Deletion

```bash
rm -i notes.txt
```

Prompts before deleting the file.

### Example 3: Verbose Deletion

```bash
rm -v notes.txt
```

Displays the removed filename.

### Example 4: Remove Multiple Files

```bash
rm file1.txt file2.txt
```

### Example 5: Remove a Directory and Its Contents

```bash
rm -r project
```

The `-r` option recursively removes a directory and its contents.

### Example 6: Forceful Recursive Removal

```bash
rm -rf project
```

- `-r`: Recursive removal.
- `-f`: Force removal without prompting for confirmation in ordinary cases.

> CRITICAL WARNING: `rm -rf` can permanently delete large amounts of data. It does not normally move files to a recycle bin. Never execute unfamiliar recursive deletion commands, especially when variables or wildcards are involved.

### Safer Practice

Before deleting:

```bash
pwd
ls -la
```

Then inspect the exact target.

Use interactive deletion when appropriate:

```bash
rm -ri project
```

---

## 3.10 rmdir — Remove Empty Directories

### What Is rmdir?

`rmdir` removes empty directories.

Unlike `rm -r`, it will not normally remove a directory containing files or subdirectories.

### Syntax

```bash
rmdir [OPTIONS] DIRECTORY
```

### Example 1: Remove an Empty Directory

```bash
rmdir old-folder
```

### Example 2: Remove Multiple Empty Directories

```bash
rmdir folder1 folder2
```

### Example 3: Remove Empty Parent Directories

```bash
rmdir -p parent/child
```

Removes the child directory and then attempts to remove the parent if it is also empty.

### Difference Between rm and rmdir

| Command | Purpose |
|---|---|
| `rm file.txt` | Remove a file |
| `rm -r directory` | Remove a directory and its contents |
| `rmdir directory` | Remove an empty directory |

---

## 3.11 Absolute Paths vs Relative Paths

A path identifies the location of a file or directory.

Linux uses two major path types.

### Absolute Path

An absolute path starts from the root directory `/`.

Example:

```text
/home/pulok/Documents/notes.txt
```

It identifies the file's location independently of your current working directory.

### Relative Path

A relative path starts from your current working directory.

Suppose your current location is:

```text
/home/pulok
```

You can access the same file using:

```text
Documents/notes.txt
```

### Comparison

| Feature | Absolute Path | Relative Path |
|---|---|---|
| Starting point | `/` | Current directory |
| Depends on current location | No | Yes |
| Example | `/home/pulok/file.txt` | `file.txt` |
| Use | Unambiguous file location | Convenient navigation |

### Special Path Symbols

| Symbol | Meaning |
|---|---|
| `/` | Root directory |
| `.` | Current directory |
| `..` | Parent directory |
| `~` | Current user's home directory |
| `-` | Previous directory with `cd -` |

### Practical Examples

```bash
cd /var/log
```

Uses an absolute path.

```bash
cd Documents
```

Uses a relative path.

```bash
cd ../Downloads
```

Moves to the sibling `Downloads` directory from the current directory's parent.

```bash
cat ~/Documents/notes.txt
```

Reads a file using a path based on the user's home directory.

---

## 3.12 Hidden Files and Directories

### What Are Hidden Files?

In Linux, filenames beginning with a dot (`.`) are normally treated as hidden by standard directory-listing tools.

Examples:

```text
.bashrc
.profile
.gitconfig
.ssh
.config
```

These files are not necessarily protected or encrypted.

They are simply omitted from ordinary `ls` output unless hidden entries are requested.

### Create a Hidden File

```bash
touch .secret.txt
```

### List Normal Files

```bash
ls
```

The hidden file usually will not appear.

### List Hidden Files

```bash
ls -a
```

### Display Hidden Files in Long Format

```bash
ls -la
```

### Read a Hidden File

```bash
cat .secret.txt
```

### Hidden Directories

Create one:

```bash
mkdir .private
```

List it:

```bash
ls -la
```

### Why Are Hidden Files Important?

Linux applications commonly use hidden files and directories for configuration.

Examples:

| Path | Purpose |
|---|---|
| `~/.bashrc` | Bash interactive shell configuration |
| `~/.profile` | Login shell environment configuration |
| `~/.ssh` | SSH-related user configuration and keys |
| `~/.config` | User application configuration |
| `~/.gitconfig` | Git configuration |

### Cybersecurity Relevance

Hidden files can contain:

- Application configurations.
- SSH configuration.
- Git credentials or configuration.
- Environment-related information.
- Application secrets, if stored insecurely.

During authorized security assessments, inspect relevant files while respecting permissions and data privacy.

Remember: hidden does not mean secure.

---

## 3.13 Wildcards: *, ?, and Character Patterns

### What Are Wildcards?

Wildcards are special patterns used by the shell to match filenames.

They make it easier to work with multiple files.

In Bash, filename patterns are commonly expanded by the shell before a command executes.

The three important pattern types are:

- `*`
- `?`
- Character patterns such as `[abc]` and `[0-9]`

### 1. Asterisk (*)

Matches zero or more characters in a filename component.

Example:

```bash
ls *.txt
```

Lists filenames ending in `.txt` in the current directory.

Other examples:

```bash
ls log*
```

Matches names beginning with `log`.

```bash
ls *report*
```

Matches names containing `report`.

```bash
rm *.tmp
```

Removes matching `.tmp` files in the current directory.

> Warning: Always inspect wildcard matches before using destructive commands.

Safer inspection:

```bash
printf '%s\n' *.tmp
```

### 2. Question Mark (?)

Matches exactly one character in a filename component.

Example:

```bash
ls file?.txt
```

May match:

```text
file1.txt
file2.txt
fileA.txt
```

It does not match:

```text
file10.txt
```

because two characters appear where one `?` is expected.

### 3. Character Patterns ([ ])

Matches one character from a specified set or range.

Example:

```bash
ls file[123].txt
```

Matches:

```text
file1.txt
file2.txt
file3.txt
```

### Character Ranges

```bash
ls file[0-9].txt
```

Matches filenames with one digit in that position.

### Character Negation

```bash
ls file[!0-9].txt
```

Matches one character in that position that is not in the range `0-9`.

### Wildcard Comparison

| Pattern | Meaning |
|---|---|
| `*` | Zero or more characters |
| `?` | Exactly one character |
| `[abc]` | One character: a, b, or c |
| `[0-9]` | One digit |
| `[a-z]` | One lowercase letter in the range |
| `[!abc]` | One character not in the specified set |

### Important Difference: Shell Wildcards vs Regular Expressions

Wildcards and regular expressions are not the same.

For example:

```bash
ls *.log
```

Uses shell filename expansion.

But:

```bash
grep 'error.*failed' application.log
```

Uses a regular expression interpreted by `grep`.

The `*` has different meanings in these two contexts.

---

# 4. Reading and Editing Files

Linux provides several commands and text editors for reading and modifying files.

These are particularly important when inspecting:

- System logs.
- Configuration files.
- Application source code.
- Security reports.
- Bash scripts.
- Web server logs.

## 4.1 cat — Display File Contents

### What Is cat?

`cat` stands for Concatenate.

It displays file contents and can combine multiple files.

### Syntax

```bash
cat [OPTIONS] [FILE]
```

### Example 1: Read a File

```bash
cat notes.txt
```

Displays the complete contents of `notes.txt`.

### Example 2: Read Multiple Files

```bash
cat file1.txt file2.txt
```

Displays the contents of both files in sequence.

### Example 3: Combine Files

```bash
cat file1.txt file2.txt > combined.txt
```

Combines the contents of both files into `combined.txt`.

The `>` operator overwrites an existing destination file.

### Example 4: Append File Contents

```bash
cat file1.txt >> combined.txt
```

Appends the contents of `file1.txt` to `combined.txt`.

### Example 5: Display Line Numbers

```bash
cat -n notes.txt
```

Displays line numbers for all lines.

### Example 6: Display Non-Empty Line Numbers

```bash
cat -b notes.txt
```

Numbers non-empty lines.

### Important Options

| Option | Purpose |
|---|---|
| `-n` | Number all output lines |
| `-b` | Number non-empty lines |
| `-s` | Suppress repeated empty output lines |
| `-A` | Show non-printing characters visibly |

### When Should You Use cat?

Use `cat` for:

- Small files.
- Short configuration files.
- Displaying command output.
- Combining text files.

For very large files, use `less` instead.

---

## 4.2 less — Read Files Page by Page

### What Is less?

`less` is a terminal pager that allows you to read large files one screen at a time.

Unlike `cat`, it does not need to print the entire file to the terminal at once.

### Syntax

```bash
less [OPTIONS] FILE
```

### Example

```bash
less /var/log/syslog
```

Opens the log file in a scrollable viewer if that file exists.

### Navigation Keys

| Key | Purpose |
|---|---|
| `Space` | Move forward one page |
| `b` | Move backward one page |
| `Enter` | Move down one line |
| `k` | Move up one line |
| `g` | Go to the beginning |
| `G` | Go to the end |
| `/word` | Search forward |
| `?word` | Search backward |
| `n` | Next match |
| `N` | Previous match |
| `q` | Quit |

### Example: Search Inside a Log

```bash
less /var/log/auth.log
```

Inside the viewer, type:

```text
/Failed password
```

Press Enter to search.

### Cybersecurity Relevance

`less` is especially useful when analyzing:

- Authentication logs.
- Web server logs.
- Application logs.
- Large configuration files.
- Incident investigation records.

---

## 4.3 head — Display the Beginning of a File

### What Is head?

`head` displays the first lines of a file.

By default, it displays the first 10 lines.

### Syntax

```bash
head [OPTIONS] FILE
```

### Example 1

```bash
head notes.txt
```

Displays the first 10 lines.

### Example 2: Display First Five Lines

```bash
head -n 5 notes.txt
```

### Example 3: Display First Twenty Lines

```bash
head -n 20 notes.txt
```

### Example 4: Display First 100 Bytes

```bash
head -c 100 notes.txt
```

### Example 5: Inspect a Log Header

```bash
head -n 20 /var/log/auth.log
```

Useful when you want to inspect the beginning of an authentication log.

---

## 4.4 tail — Display the End of a File

### What Is tail?

`tail` displays the last lines of a file.

By default, it displays the last 10 lines.

### Syntax

```bash
tail [OPTIONS] FILE
```

### Example 1

```bash
tail notes.txt
```

Displays the final 10 lines.

### Example 2: Display Last Five Lines

```bash
tail -n 5 notes.txt
```

### Example 3: Display Last Twenty Lines

```bash
tail -n 20 notes.txt
```

### Example 4: Display Last 100 Bytes

```bash
tail -c 100 notes.txt
```

### Example 5: Inspect Recent Authentication Events

```bash
sudo tail -n 20 /var/log/auth.log
```

The file may require elevated permissions and may not exist on every distribution.

---

## 4.5 tail -f — Monitor Logs in Real Time

### What Is tail -f?

The `-f` option means follow.

It allows you to monitor new content added to a file.

### Syntax

```bash
tail -f FILE
```

### Example

```bash
sudo tail -f /var/log/auth.log
```

Displays new log entries as they are appended.

### How Does It Work?

1. The command opens the specified file.
2. It displays the final lines.
3. It waits for new data.
4. When new content is appended, it displays that content.

### Stop Monitoring

Press:

```text
Ctrl + C
```

### Example: Generate Test Log Entries

In one terminal:

```bash
tail -f ~/linux-practice/events.log
```

In another terminal:

```bash
echo "Test event generated" >> ~/linux-practice/events.log
```

The first terminal should display the new entry.

### Difference Between -f and -F

```bash
tail -f application.log
```

Follows the currently opened file descriptor.

```bash
tail -F application.log
```

Follows the filename and attempts to reopen it if the file is replaced or recreated.

`-F` is useful for monitoring logs that undergo rotation.

### Cybersecurity Relevance

Live log monitoring is useful for:

- Observing authentication attempts.
- Monitoring application errors.
- Investigating suspicious events.
- Watching web server activity.
- Debugging security testing environments.

---

## 4.6 nano — Beginner-Friendly Text Editor

### What Is nano?

`nano` is a simple terminal-based text editor.

It is useful for creating and editing configuration files, notes, and scripts.

### Installation

```bash
sudo apt install nano
```

It is commonly preinstalled on many distributions.

### Open a File

```bash
nano notes.txt
```

If the file does not exist, nano can create it when saved.

### Important Keyboard Shortcuts

| Shortcut | Purpose |
|---|---|
| `Ctrl + O` | Save file |
| `Ctrl + X` | Exit |
| `Ctrl + W` | Search |
| `Ctrl + K` | Cut current line |
| `Ctrl + U` | Paste previously cut text |
| `Ctrl + G` | Help |
| `Ctrl + \` | Search and replace |
| `Ctrl + C` | Display cursor position |

### Practical Example

Open a file:

```bash
nano linux-notes.txt
```

Write:

```text
I am learning Linux.
I am practising Linux commands.
I am preparing for cybersecurity.
```

Save:

1. Press `Ctrl + O`.
2. Press Enter to confirm the filename.
3. Press `Ctrl + X` to exit.

Verify:

```bash
cat linux-notes.txt
```

### Cybersecurity Relevance

nano is useful for editing:

- Configuration files.
- SSH configuration.
- Bash scripts.
- Application settings.
- Local lab documentation.

Be careful when editing system-wide configuration files.

---

## 4.7 vim — Basic Text Editing

### What Is Vim?

Vim stands for Vi IMproved.

It is a powerful terminal-based text editor commonly available in Linux environments.

Vim is especially useful for editing files on remote Linux servers.

### Installation

```bash
sudo apt install vim
```

### Open a File

```bash
vim notes.txt
```

### Understanding Vim Modes

Vim is a modal editor.

This means different keys perform different operations depending on the current mode.

The most important modes are:

### 1. Normal Mode

Used for navigation and editing commands.

Press:

```text
Esc
```

to return to Normal mode from Insert mode or another mode.

### 2. Insert Mode

Used for entering text.

Press:

```text
i
```

to enter Insert mode at the current cursor position.

### 3. Command-Line Mode

Used for commands such as saving and exiting.

Press:

```text
:
```

from Normal mode.

### Basic Vim Workflow

Open a file:

```bash
vim notes.txt
```

Enter Insert mode:

```text
i
```

Type:

```text
Learning Vim basics.
```

Return to Normal mode:

```text
Esc
```

Save and exit:

```text
:wq
```

Press Enter.

### Important Vim Commands

| Command | Purpose |
|---|---|
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `o` | Open a new line below |
| `O` | Open a new line above |
| `Esc` | Return to Normal mode |
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |
| `dd` | Delete current line |
| `yy` | Copy current line |
| `p` | Paste after cursor |
| `u` | Undo |
| `Ctrl + r` | Redo |
| `/word` | Search for word |
| `n` | Next search result |
| `gg` | Go to first line |
| `G` | Go to last line |
| `:set number` | Display line numbers |

### Important Vim Example

Suppose you open a file:

```bash
vim config.txt
```

Make changes and save:

```text
Esc
:w
Enter
```

Save and exit:

```text
Esc
:wq
Enter
```

Exit without saving:

```text
Esc
:q!
Enter
```

### Nano vs Vim

| Feature | Nano | Vim |
|---|---|---|
| Learning difficulty | Easier | More difficult initially |
| Editing style | Mostly direct text editing | Modal editing |
| Keyboard commands | Displayed on screen | Must learn commands |
| Advanced editing | Basic | Extensive |
| Server administration | Useful | Very common |

**Learning recommendation:** Become comfortable with nano first, then gradually learn Vim.

---

## 4.8 file — Identify File Type

### What Is file?

The `file` command identifies the type of a file.

It examines file contents and metadata using file-signature information and other classification rules.

It does not rely exclusively on the filename extension.

### Syntax

```bash
file [OPTIONS] FILE
```

### Example 1

```bash
file notes.txt
```

Possible output:

```text
notes.txt: ASCII text
```

### Example 2

```bash
file image.png
```

Possible output:

```text
image.png: PNG image data
```

### Example 3: Inspect Multiple Files

```bash
file *
```

Attempts to identify every matching entry.

### Example 4: Display MIME Type

```bash
file --mime-type notes.txt
```

Possible output:

```text
notes.txt: text/plain
```

### Important Options

| Option | Purpose |
|---|---|
| `-b` | Brief output without filename |
| `-i` | Display MIME type and encoding information |
| `-L` | Follow symbolic links |

### Cybersecurity Relevance

File identification is useful when:

- Inspecting unknown files.
- Investigating uploaded files.
- Examining suspicious attachments.
- Checking file types during digital forensics.
- Identifying files with misleading extensions.

For example, a file named `image.jpg` is not necessarily a genuine JPEG image.

---

## 4.9 stat — Display File Metadata

### What Is stat?

`stat` displays detailed information about a file or filesystem.

It can reveal metadata that is not immediately visible through a normal directory listing.

### Syntax

```bash
stat [OPTIONS] FILE
```

### Example

```bash
stat notes.txt
```

Example output:

```text
File: notes.txt
Size: 120
Blocks: 8
IO Block: 4096
regular file
Device: ...
Inode: ...
Access: (0644/-rw-r--r--)
Uid: (1000/pulok)
Gid: (1000/pulok)
Access: 2026-11-09 ...
Modify: 2026-11-09 ...
Change: 2026-11-09 ...
Birth: ...
```

Exact output varies by filesystem and operating system.

### Important Metadata

| Metadata | Meaning |
|---|---|
| File | Filename |
| Size | File size in bytes |
| Blocks | Allocated storage blocks |
| Inode | Filesystem object identifier |
| Access | Permission information |
| Uid | Owner user ID |
| Gid | Owner group ID |
| Access time | Last access timestamp |
| Modify time | Last content modification timestamp |
| Change time | Last metadata change timestamp |
| Birth time | File creation time, if supported |

### Important Difference Between Timestamps

**Access time (atime):** Records the last access time, subject to filesystem mount options.

**Modification time (mtime):** Changes when file contents are modified.

**Change time (ctime):** Changes when file metadata or contents change.

**Birth time:** Represents creation time where supported.

Do not confuse ctime with creation time.

### Important Options

```bash
stat -c '%n %s %U %G' notes.txt
```

Displays selected metadata:

- `%n`: Filename.
- `%s`: Size.
- `%U`: Owner username.
- `%G`: Group name.

### Cybersecurity Relevance

Metadata inspection helps with:

- File investigations.
- Incident timelines.
- Identifying unexpected modifications.
- Understanding file ownership.
- Examining suspicious files.

Timestamps alone are not proof of when an event occurred because they can be affected by system clocks and administrative changes.

---

## 4.10 wc — Count Lines, Words, and Characters

### What Is wc?

`wc` stands for Word Count.

It counts lines, words, bytes, and characters in files or standard input.

### Syntax

```bash
wc [OPTIONS] FILE
```

### Example 1

```bash
wc notes.txt
```

Possible output:

```text
5  25  140 notes.txt
```

The fields represent:

1. Lines.
2. Words.
3. Bytes.
4. Filename.

### Important Options

| Option | Purpose |
|---|---|
| `-l` | Count lines |
| `-w` | Count words |
| `-c` | Count bytes |
| `-m` | Count characters |
| `-L` | Display maximum line length |

### Examples

Count lines:

```bash
wc -l notes.txt
```

Count words:

```bash
wc -w notes.txt
```

Count bytes:

```bash
wc -c notes.txt
```

Count characters:

```bash
wc -m notes.txt
```

Display maximum line length:

```bash
wc -L notes.txt
```

### Example with Pipes

```bash
cat notes.txt | wc -l
```

Counts the number of lines provided through standard input.

A shorter alternative is:

```bash
wc -l < notes.txt
```

---

## 4.11 sort — Sort Text Data

### What Is sort?

`sort` arranges lines of text in a particular order.

By default, it sorts lexicographically according to the current locale.

### Syntax

```bash
sort [OPTIONS] FILE
```

### Example 1

Suppose `names.txt` contains:

```text
Rahul
Amit
Pulok
Ankit
```

Execute:

```bash
sort names.txt
```

Output:

```text
Amit
Ankit
Pulok
Rahul
```

### Important Options

| Option | Purpose |
|---|---|
| `-r` | Reverse sorting |
| `-n` | Numeric sorting |
| `-u` | Remove duplicate lines from sorted output |
| `-f` | Ignore case differences during sorting |
| `-k` | Sort by a specified field |
| `-t` | Specify a field delimiter |
| `-h` | Human-readable numeric sorting |

### Example 2: Reverse Sorting

```bash
sort -r names.txt
```

### Example 3: Numeric Sorting

Suppose `numbers.txt` contains:

```text
100
20
3
50
```

Normal sorting:

```bash
sort numbers.txt
```

Numeric sorting:

```bash
sort -n numbers.txt
```

Output:

```text
3
20
50
100
```

### Example 4: Case-Insensitive Sorting

```bash
sort -f names.txt
```

### Example 5: Sort a CSV File by the Second Field

```bash
sort -t ',' -k2,2 users.csv
```

This sorts lines using the second comma-separated field.

This basic example does not automatically account for CSV quoting or commas embedded inside quoted fields.

---

## 4.12 uniq — Find or Remove Adjacent Duplicate Lines

### What Is uniq?

`uniq` processes repeated adjacent lines in text.

It is commonly used with `sort`.

### Syntax

```bash
uniq [OPTIONS] INPUT [OUTPUT]
```

### Important Concept

`uniq` normally detects consecutive duplicate lines, not every duplicate occurrence throughout an unsorted file.

### Example

Suppose `names.txt` contains:

```text
Amit
Amit
Rahul
Pulok
Pulok
```

Run:

```bash
uniq names.txt
```

Output:

```text
Amit
Rahul
Pulok
```

### Example: Remove All Duplicates After Sorting

```bash
sort names.txt | uniq
```

Sorting places identical lines next to each other before `uniq` processes them.

### Important Options

| Option | Purpose |
|---|---|
| `-c` | Count occurrences of adjacent lines |
| `-d` | Display only repeated lines |
| `-u` | Display only unique lines |
| `-i` | Ignore case differences |
| `-D` | Display all repeated lines |

### Example: Count Repeated Entries

```bash
sort names.txt | uniq -c
```

Possible output:

```text
2 Amit
1 Rahul
2 Pulok
```

### Example: Show Only Duplicate Entries

```bash
sort names.txt | uniq -d
```

### Example: Show Only Unique Entries

```bash
sort names.txt | uniq -u
```

### Cybersecurity Relevance

Useful for:

- Counting repeated IP addresses.
- Identifying repeated usernames.
- Analyzing web server requests.
- Finding recurring log entries.

---

## 4.13 cut — Extract Selected Fields or Characters

### What Is cut?

`cut` extracts selected portions of each input line.

It is useful when working with structured text, especially delimiter-separated files.

### Syntax

```bash
cut [OPTIONS] FILE
```

### Important Options

| Option | Purpose |
|---|---|
| `-d` | Specify delimiter |
| `-f` | Select fields |
| `-c` | Select character positions |
| `-b` | Select byte positions |
| `--complement` | Select everything except the specified positions |

### Example 1: Extract a Field

Suppose `users.txt` contains:

```text
pulok:admin:1001
rahul:user:1002
amit:guest:1003
```

Execute:

```bash
cut -d ':' -f1 users.txt
```

Output:

```text
pulok
rahul
amit
```

Explanation:

- `-d ':'` specifies the colon delimiter.
- `-f1` selects the first field.

### Example 2: Extract the Second Field

```bash
cut -d ':' -f2 users.txt
```

Output:

```text
admin
user
guest
```

### Example 3: Extract Multiple Fields

```bash
cut -d ':' -f1,3 users.txt
```

Output:

```text
pulok:1001
rahul:1002
amit:1003
```

### Example 4: Extract a Range of Fields

```bash
cut -d ':' -f1-2 users.txt
```

### Example 5: Extract Character Positions

```bash
cut -c1-5 notes.txt
```

Displays characters 1 through 5 from each line.

### Example 6: Select All Fields Except the First

```bash
cut -d ':' -f1 --complement users.txt
```

### Important Limitation

`cut` is not a complete CSV parser.

If a CSV field contains quoted delimiters, use a CSV-aware tool such as Python's `csv` module instead.

### Cybersecurity Relevance

`cut` is useful for extracting:

- Usernames.
- IP addresses.
- Selected log fields.
- Network information.
- Structured configuration values.

---

## 4.14 paste — Merge Lines or Columns

### What Is paste?

`paste` combines corresponding lines from multiple files.

By default, it joins lines using a tab character.

### Syntax

```bash
paste [OPTIONS] FILE1 FILE2
```

### Example 1

`names.txt`:

```text
Pulok
Rahul
Amit
```

`ages.txt`:

```text
22
23
21
```

Execute:

```bash
paste names.txt ages.txt
```

Output:

```text
Pulok   22
Rahul   23
Amit    21
```

### Example 2: Use a Comma as Delimiter

```bash
paste -d ',' names.txt ages.txt
```

Output:

```text
Pulok,22
Rahul,23
Amit,21
```

### Example 3: Merge Multiple Files

```bash
paste names.txt ages.txt departments.txt
```

Combines corresponding lines from all three files.

### Example 4: Combine All Lines into One Line

```bash
paste -s names.txt
```

Serial mode joins lines from the same input file.

### Important Options

| Option | Purpose |
|---|---|
| `-d` | Specify delimiter |
| `-s` | Serial mode |

### Practical Use

`paste` is useful when combining:

- Names and identifiers.
- IP addresses and descriptions.
- Report columns.
- Separate text-based datasets.

---

## 4.15 tr — Translate or Delete Characters

### What Is tr?

`tr` stands for Translate.

It translates, deletes, or squeezes characters from standard input.

It does not normally accept a filename argument directly. Use input redirection or a pipeline.

### Syntax

```bash
tr [OPTIONS] SET1 [SET2]
```

### Example 1: Convert Lowercase to Uppercase

```bash
echo "hello linux" | tr 'a-z' 'A-Z'
```

Output:

```text
HELLO LINUX
```

### Example 2: Convert Uppercase to Lowercase

```bash
echo "HELLO LINUX" | tr 'A-Z' 'a-z'
```

Output:

```text
hello linux
```

### Example 3: Replace Spaces with Underscores

```bash
echo "linux commands practice" | tr ' ' '_'
```

Output:

```text
linux_commands_practice
```

### Example 4: Delete Digits

```bash
echo "user123admin456" | tr -d '0-9'
```

Output:

```text
useradmin
```

### Example 5: Squeeze Repeated Spaces

```bash
echo "Linux     Commands" | tr -s ' '
```

Output:

```text
Linux Commands
```

### Example 6: Delete Newline Characters

```bash
tr -d '\n' < notes.txt
```

Removes newline characters from the input stream.

### Important Options

| Option | Purpose |
|---|---|
| `-d` | Delete characters |
| `-s` | Squeeze repeated characters |
| `-c` | Complement the specified character set |

### Cybersecurity Relevance

`tr` can help normalize text before analysis.

For example, you can convert log text to lowercase before searching:

```bash
tr 'A-Z' 'a-z' < application.log
```

---

## 4.16 tee — Display and Save Output Simultaneously

### What Is tee?

`tee` reads data from standard input and sends it to both:

1. Standard output.
2. One or more files.

It is useful when you want to see command output and save it in a report.

### Syntax

```bash
command | tee [OPTIONS] FILE
```

### Example 1: Display and Save Output

```bash
ls -la | tee directory-report.txt
```

The output is:

- Displayed in the terminal.
- Saved in `directory-report.txt`.

### Example 2: Append Output

```bash
date | tee -a report.txt
```

The `-a` option appends output instead of overwriting the destination.

### Example 3: Save Process Information

```bash
ps aux | tee process-report.txt
```

### Example 4: Save Output to Multiple Files

```bash
uname -a | tee system1.txt system2.txt
```

### Example 5: Use tee with sudo

Suppose you need to write to a root-owned file.

This may fail:

```bash
sudo echo "example" > /etc/example.conf
```

The shell performs the redirection before `sudo` executes.

A suitable alternative is:

```bash
echo "example" | sudo tee /etc/example.conf
```

This example overwrites the destination file, so inspect and back up important configuration files first.

### Important Options

| Option | Purpose |
|---|---|
| `-a` | Append instead of overwrite |
| `-i` | Ignore interrupt signals |

### Cybersecurity Relevance

`tee` is useful for:

- Saving system information.
- Creating investigation reports.
- Capturing command output.
- Documenting authorized security tests.
- Maintaining repeatable lab records.

---

# 5. Searching and Finding Information

Searching is one of the most important skills in Linux.

A Linux system can contain thousands of files, configuration entries, log records, and processes.

You need to know how to locate information efficiently.

---

## 5.1 find — Search for Files and Directories

### What Is find?

`find` searches for files and directories within a specified directory hierarchy.

It can search based on:

- Filename.
- File type.
- Size.
- Owner.
- Group.
- Permissions.
- Modification time.
- Access time.

### Syntax

```bash
find PATH [OPTIONS] [EXPRESSION]
```

### Example 1: Find All Files in a Directory

```bash
find /home/pulok
```

Displays entries under the specified directory recursively.

### Example 2: Find a Specific Filename

```bash
find /home/pulok -name "notes.txt"
```

### Example 3: Case-Insensitive Filename Search

```bash
find /home/pulok -iname "NOTES.TXT"
```

The `-iname` option ignores filename case.

### Example 4: Find All .log Files

```bash
find /var/log -type f -name "*.log"
```

Explanation:

- `/var/log`: Search starting location.
- `-type f`: Match regular files.
- `-name "*.log"`: Match names ending in `.log`.

The quotation marks prevent the shell from expanding the wildcard before `find` receives it.

### Example 5: Find Directories Only

```bash
find /home/pulok -type d
```

### Example 6: Find Files Only

```bash
find /home/pulok -type f
```

### Example 7: Find Empty Files

```bash
find /home/pulok -type f -empty
```

### Example 8: Find Files Larger Than 100 MB

```bash
find /home/pulok -type f -size +100M
```

### Example 9: Find Files Smaller Than 1 KB

```bash
find /home/pulok -type f -size -1k
```

### Example 10: Find Files Modified Within the Last 24 Hours

```bash
find /home/pulok -type f -mtime -1
```

`-mtime` measures age in whole 24-hour periods.

### Example 11: Find Files Modified More Than Seven Days Ago

```bash
find /home/pulok -type f -mtime +7
```

### Example 12: Find Files Owned by a User

```bash
find /home -user pulok
```

### Example 13: Find Files with Specific Permissions

```bash
find /home/pulok -type f -perm 644
```

This matches files whose permission bits match the specified mode.

### Example 14: Execute a Command on Matching Files

```bash
find /home/pulok -type f -name "*.txt" -exec file {} \;
```

Explanation:

- `-exec`: Execute another command on matching entries.
- `file`: Identify the file type.
- `{}`: Represents the current matching path.
- `\;`: Ends the `-exec` command.

### Example 15: Search for Files and Ignore Permission Errors

```bash
find /var/log -type f -name "*.log" 2>/dev/null
```

Here:

- `2>` redirects standard error.
- `/dev/null` discards the error messages.

This suppresses permission-related messages, but it does not grant access to restricted files.

### Important find Options

| Option | Purpose |
|---|---|
| `-name` | Search by filename |
| `-iname` | Case-insensitive filename search |
| `-type f` | Regular files |
| `-type d` | Directories |
| `-size` | Search by file size |
| `-mtime` | Modification age in days |
| `-user` | Search by owner |
| `-group` | Search by group |
| `-perm` | Search by permissions |
| `-empty` | Search for empty files or directories |
| `-exec` | Execute a command on matches |

### Cybersecurity Relevance

`find` is useful for:

- Locating log files.
- Identifying sensitive configuration files.
- Finding unexpected executable files.
- Searching for old files.
- Investigating file ownership.
- Reviewing potentially unsafe permissions.

Use authorized directories and avoid indiscriminate recursive searches across sensitive systems.

---

## 5.2 grep — Search Text Patterns

### What Is grep?

`grep` stands for Global Regular Expression Print.

It searches input for lines matching a specified pattern.

It is commonly used to analyze:

- Logs.
- Configuration files.
- Source code.
- Text reports.
- System information.

### Syntax

```bash
grep [OPTIONS] PATTERN FILE
```

### Example 1: Search for a Word

Suppose `notes.txt` contains:

```text
Linux is an operating system kernel.
Linux supports multitasking.
Python is useful for automation.
```

Execute:

```bash
grep "Linux" notes.txt
```

Output:

```text
Linux is an operating system kernel.
Linux supports multitasking.
```

### Example 2: Search for a Phrase

```bash
grep "operating system" notes.txt
```

### Example 3: Search in Multiple Files

```bash
grep "error" application.log system.log
```

### Example 4: Search Using a Regular Expression

```bash
grep "error.*failed" application.log
```

This searches for lines containing `error`, followed later by `failed`.

By default, grep uses basic regular expressions. The `.*` expression works in this example.

### Example 5: Search for Lines Beginning with a Word

```bash
grep "^ERROR" application.log
```

The `^` anchor matches the beginning of a line.

### Example 6: Search for Lines Ending with a Word

```bash
grep "failed$" application.log
```

The `$` anchor matches the end of a line.

---

## 5.3 Important grep Options

### 1. grep -i — Case-Insensitive Search

```bash
grep -i "error" application.log
```

Matches variations such as:

```text
ERROR
Error
error
```

### 2. grep -r — Recursive Search

```bash
grep -r "password" /etc
```

Searches recursively through files in the specified directory.

This may encounter permission errors.

A more restricted example:

```bash
grep -r "Listen" /etc/apache2
```

### 3. grep -n — Display Line Numbers

```bash
grep -n "failed" application.log
```

Example output:

```text
12:Authentication failed
28:Login failed
```

### 4. grep -v — Invert Matching

```bash
grep -v "success" application.log
```

Displays lines that do not match `success`.

### 5. grep -c — Count Matching Lines

```bash
grep -c "failed" application.log
```

Displays the number of matching lines.

### 6. grep -l — Display Matching Filenames

```bash
grep -rl "error" /var/log
```

Displays filenames containing matching text.

### 7. grep -w — Match Whole Words

```bash
grep -w "root" /etc/passwd
```

Matches `root` as a whole word rather than matching it as part of a longer word.

### 8. grep -o — Display Only Matching Text

```bash
grep -o "192\.168\.1\.[0-9]*" application.log
```

Displays only matching text rather than the complete matching line.

### 9. grep -E — Extended Regular Expressions

```bash
grep -E "error|failed|warning" application.log
```

Matches any of the three alternatives.

### 10. grep -A and grep -B

Display surrounding lines.

```bash
grep -A 3 "ERROR" application.log
```

Displays three lines after each match.

```bash
grep -B 3 "ERROR" application.log
```

Displays three lines before each match.

```bash
grep -C 3 "ERROR" application.log
```

Displays three lines before and after each match.

### grep Options Summary

| Option | Purpose |
|---|---|
| `-i` | Ignore case |
| `-r` | Recursive search |
| `-n` | Display line numbers |
| `-v` | Invert matching |
| `-c` | Count matching lines |
| `-l` | Display matching filenames |
| `-w` | Match whole words |
| `-o` | Display only matching text |
| `-E` | Extended regular expressions |
| `-A N` | Display N lines after a match |
| `-B N` | Display N lines before a match |
| `-C N` | Display surrounding lines |

### Cybersecurity Relevance

grep is particularly important for:

- Searching failed-login events.
- Identifying error messages.
- Searching application logs.
- Finding configuration entries.
- Investigating suspicious IP addresses.
- Filtering security events.

---

## 5.4 locate — Search Files Using an Index

### What Is locate?

`locate` searches for filenames using a prebuilt database or index.

Unlike `find`, which normally walks through the filesystem, `locate` searches its filename database.

This makes it fast for many searches.

### Installation

On Debian-based distributions:

```bash
sudo apt install plocate
```

Some systems provide the older `mlocate` implementation or compatibility commands.

### Update the Database

Depending on the installed implementation:

```bash
sudo updatedb
```

This updates the filename database.

The database may be updated automatically by a scheduled service or timer.

### Example 1: Find a File

```bash
locate notes.txt
```

### Example 2: Search for Log Files

```bash
locate "*.log"
```

### Example 3: Limit Results

```bash
locate -n 10 "*.conf"
```

Displays at most 10 matches.

### Example 4: Case-Insensitive Search

```bash
locate -i "README"
```

### locate vs find

| Feature | locate | find |
|---|---|---|
| Search method | Database/index | Filesystem traversal |
| Speed | Usually faster | Depends on search scope |
| Freshness | Depends on database updates | Searches current filesystem state |
| Search criteria | Primarily filenames and paths | Names, type, size, owner, permissions, time, etc. |
| Database required | Yes | No |

### Important Limitation

A newly created file may not appear in `locate` until the database is updated.

Also, the search database can contain paths that are no longer present if it is stale.

---

## 5.5 which — Locate an Executable

### What Is which?

`which` displays the executable path of a command found through the shell's PATH search.

### Syntax

```bash
which COMMAND
```

### Example 1

```bash
which python3
```

Possible output:

```text
/usr/bin/python3
```

### Example 2

```bash
which bash
```

Possible output:

```text
/usr/bin/bash
```

### Example 3: Locate Multiple Commands

```bash
which python3 bash grep
```

### Important Limitation

`which` is generally an external utility and may not correctly identify shell aliases, functions, or built-in commands.

For general shell command resolution, `command -v` is usually more suitable.

---

## 5.6 whereis — Locate Binary, Source, and Manual Files

### What Is whereis?

`whereis` searches standard locations for the binary, source, and manual-page files associated with a command.

### Syntax

```bash
whereis COMMAND
```

### Example

```bash
whereis python3
```

Possible output:

```text
python3: /usr/bin/python3 /usr/lib/python3 /usr/share/man/man1/python3.1.gz
```

The exact output varies by installation.

### Important Options

| Option | Purpose |
|---|---|
| `-b` | Search for binary files |
| `-m` | Search for manual files |
| `-s` | Search for source files |

### Examples

```bash
whereis -b python3
```

Finds binary-related paths.

```bash
whereis -m bash
```

Finds manual-page locations.

### which vs whereis

| which | whereis |
|---|---|
| Searches executable commands through PATH | Searches standard locations for binary, source, and manual files |
| Useful for finding the executable selected by PATH | Useful for finding related installation files |
| Does not reliably identify shell built-ins | Does not provide complete shell command resolution |

---

## 5.7 command -v — Identify How a Command Is Resolved

### What Is command -v?

`command -v` is a shell command used to identify how a command name would be interpreted.

It can identify:

- Shell built-ins.
- Executable commands.
- Shell functions.
- Aliases, depending on the shell and context.

### Syntax

```bash
command -v COMMAND
```

### Example 1

```bash
command -v ls
```

Possible output:

```text
/usr/bin/ls
```

### Example 2

```bash
command -v cd
```

Possible output in Bash:

```text
cd
```

This indicates that `cd` is a shell built-in.

### Example 3

```bash
command -v grep
```

Possible output:

```text
/usr/bin/grep
```

### Example 4: Check Whether a Command Exists

```bash
if command -v curl >/dev/null 2>&1; then
    echo "curl is available"
else
    echo "curl is not available"
fi
```

This checks whether the shell can resolve `curl`.

### which vs whereis vs command -v

| Command | Main Purpose |
|---|---|
| `which` | Find executable through PATH |
| `whereis` | Find binary, source, and manual locations |
| `command -v` | Identify shell command resolution |

---

# 6. Searching Logs and Configuration Files

Logs and configuration files are extremely important in Linux administration and cybersecurity.

## 6.1 What Are Log Files?

Log files record events that occur within an operating system or application.

Examples include:

- Authentication events.
- System startup events.
- Application errors.
- Network events.
- Service activity.
- Security-related events.

Common log locations include:

```text
/var/log/
```

Examples of log files:

```text
/var/log/auth.log
/var/log/syslog
/var/log/kern.log
/var/log/apache2/access.log
/var/log/apache2/error.log
```

Not every distribution uses these exact files.

For example:

- Debian and Ubuntu commonly use `/var/log/auth.log` when traditional authentication logging is configured.
- Fedora commonly uses journal-based logging and may have different file locations.
- Some systems rely primarily on systemd-journald.

## 6.2 View Authentication Logs

On Debian-based systems, try:

```bash
sudo less /var/log/auth.log
```

Search for failed authentication messages:

```bash
sudo grep -i "failed" /var/log/auth.log
```

Search for failed SSH password attempts:

```bash
sudo grep -i "failed password" /var/log/auth.log
```

Display matching line numbers:

```bash
sudo grep -in "failed password" /var/log/auth.log
```

## 6.3 Search System Logs

```bash
sudo grep -i "error" /var/log/syslog
```

Searches for error-related entries if the file exists.

Search for warnings:

```bash
sudo grep -i "warning" /var/log/syslog
```

Search for multiple keywords:

```bash
sudo grep -Ei "error|failed|warning" /var/log/syslog
```

## 6.4 Use journalctl

On systemd-based systems, `journalctl` provides access to the system journal.

Display logs:

```bash
journalctl
```

Display logs from the current boot:

```bash
journalctl -b
```

Display logs from a particular service:

```bash
sudo journalctl -u ssh
```

Follow logs live:

```bash
sudo journalctl -f
```

Display only error-priority messages:

```bash
journalctl -p err
```

Display logs from the previous boot, when retained:

```bash
journalctl -b -1
```

The previous boot's logs may not be available if persistent journal storage is not configured.

## 6.5 Search Configuration Files

Linux configuration files are commonly stored in:

```text
/etc/
```

Examples:

| File | Purpose |
|---|---|
| `/etc/passwd` | User account information |
| `/etc/group` | Group information |
| `/etc/hostname` | System hostname |
| `/etc/hosts` | Local hostname mappings |
| `/etc/fstab` | Filesystem mount configuration |
| `/etc/ssh/sshd_config` | SSH server configuration |
| `/etc/os-release` | Distribution identification |

### Example 1: Search for SSH Configuration

```bash
grep -n "Port" /etc/ssh/sshd_config
```

### Example 2: Search for Hostname

```bash
grep -n "hostname" /etc/hostname
```

The file usually contains the hostname itself rather than a `hostname=` setting, so a simple read is more appropriate:

```bash
cat /etc/hostname
```

### Example 3: Search for a User

```bash
grep "^root:" /etc/passwd
```

The `^` symbol ensures the line starts with `root:`.

### Example 4: Find Configuration Files

```bash
find /etc -type f -name "*.conf"
```

### Cybersecurity Relevance

Searching logs and configuration files is essential for:

- Authentication investigations.
- Detecting repeated login failures.
- Understanding SSH settings.
- Reviewing web server errors.
- Investigating suspicious configuration changes.
- Identifying exposed or incorrectly configured services.

> Security note: Configuration files may contain sensitive information. Do not publish or share passwords, private keys, tokens, or other secrets found during an investigation.

---

# 7. Combining Commands to Filter Results

One of the most powerful features of Linux is the ability to combine commands.

Instead of performing every operation separately, you can connect commands using pipes and redirection.

## 7.1 What Is a Pipe?

A pipe (`|`) sends the standard output of one command to the standard input of another command.

### Basic Syntax

```bash
command1 | command2
```

Example:

```bash
ls /var/log | grep "auth"
```

How it works:

1. `ls /var/log` lists directory entries.
2. Its output is passed through the pipe.
3. `grep "auth"` filters matching lines.
4. Only matching results are displayed.

## 7.2 What Is Standard Input, Output, and Error?

Linux programs commonly use three standard streams.

| Stream | File Descriptor | Purpose |
|---|---:|---|
| Standard Input (stdin) | 0 | Input to a program |
| Standard Output (stdout) | 1 | Normal output |
| Standard Error (stderr) | 2 | Error messages |

These streams can be redirected.

## 7.3 Output Redirection

### Overwrite a File: >

```bash
ls -la > report.txt
```

Saves command output to `report.txt`.

If the file already exists, its previous contents are replaced.

### Append to a File: >>

```bash
date >> report.txt
```

Appends the date to the existing file.

### Redirect Standard Error: 2>

```bash
find /root -type f 2> errors.txt
```

Saves error messages to `errors.txt`.

### Redirect Standard Output and Error Together

```bash
find /root -type f > results.txt 2>&1
```

Redirects standard output to `results.txt`, then redirects standard error to the same destination.

A common Bash alternative is:

```bash
find /root -type f &> results.txt
```

## 7.4 Combining grep with Other Commands

### Example 1: Filter Directory Contents

```bash
ls -la /var/log | grep ".log"
```

### Example 2: Search Running Processes

```bash
ps aux | grep "python"
```

This can also match the grep command itself.

A more suitable alternative for process-name searches is:

```bash
pgrep -a python
```

### Example 3: Count Matching Processes

```bash
ps aux | grep -c "python"
```

Remember that this simple approach may count the grep command itself.

### Example 4: Find Unique IP Addresses in a Log

Suppose a text file contains one IP address per line:

```bash
sort ips.txt | uniq
```

### Example 5: Count IP Address Occurrences

```bash
sort ips.txt | uniq -c | sort -nr
```

This:

1. Sorts IP addresses.
2. Counts repeated adjacent entries.
3. Sorts counts numerically in reverse order.

### Example 6: Search and Display Line Numbers

```bash
grep -in "failed" application.log
```

### Example 7: Search Multiple Log Files

```bash
grep -in "error" /var/log/*.log
```

### Example 8: Find and Search Log Files

```bash
find /var/log -type f -name "*.log" -exec grep -inH "error" {} +
```

Explanation:

- `find`: Locates files.
- `-type f`: Selects regular files.
- `-name "*.log"`: Matches log filenames.
- `-exec`: Executes another command.
- `grep`: Searches file contents.
- `-i`: Ignores case.
- `-n`: Displays line numbers.
- `-H`: Displays filenames.
- `{}`: Represents matched files.
- `+`: Passes multiple matched paths to each command invocation where possible.

### Example 9: Extract and Sort Usernames

Suppose a file contains colon-separated records:

```text
pulok:admin:1001
rahul:user:1002
amit:guest:1003
```

Execute:

```bash
cut -d ':' -f1 users.txt | sort
```

### Example 10: Save Filtered Output

```bash
grep -in "error" application.log | tee error-report.txt
```

Displays matching lines and saves them into a report.

## 7.5 Why Command Combination Matters

Linux command combinations help with:

- Log analysis.
- Data extraction.
- Automation.
- System administration.
- Incident investigation.
- Security reporting.
- Processing large text files.

Learning pipes and redirection is an important step toward Bash scripting.

---

# 8. Practical Exercises

All exercises below are designed for your own Ubuntu/Kali virtual machine.

Use test files rather than modifying important system files.

---

## Practical 1: Create a Directory Structure for Cybersecurity Projects

### Objective

Create a well-organized directory structure for cybersecurity learning and projects.

### Step 1: Move to Home Directory

```bash
cd ~
```

### Step 2: Create the Main Directory

```bash
mkdir -p Cybersecurity
```

### Step 3: Create Project Directories

```bash
mkdir -p Cybersecurity/{Linux,Networking,Python,Bash,Web-Security,Bug-Bounty,Reports,Labs}
```

This uses Bash brace expansion to create multiple directories.

### Step 4: Create Subdirectories

```bash
mkdir -p Cybersecurity/Web-Security/{Notes,Tools,Reports,Practice}
```

```bash
mkdir -p Cybersecurity/Bug-Bounty/{Programs,Findings,Reports,Research}
```

### Step 5: Create Practice Files

```bash
touch Cybersecurity/Linux/commands.txt
touch Cybersecurity/Networking/network-notes.txt
touch Cybersecurity/Python/python-notes.py
touch Cybersecurity/Bash/scripts.sh
```

### Step 6: View the Structure

```bash
tree ~/Cybersecurity
```

If `tree` is not installed:

```bash
sudo apt install tree
```

### Expected Structure

```text
Cybersecurity
├── Bash
│   └── scripts.sh
├── Bug-Bounty
│   ├── Findings
│   ├── Programs
│   ├── Reports
│   └── Research
├── Labs
├── Linux
│   └── commands.txt
├── Networking
│   └── network-notes.txt
├── Python
│   └── python-notes.py
├── Reports
└── Web-Security
    ├── Notes
    ├── Practice
    ├── Reports
    └── Tools
```

### What You Should Observe

- The main directory exists.
- Subdirectories are organized by subject.
- Files are stored in their respective directories.

### Verification

```bash
ls -la ~/Cybersecurity
```

### What You Learned

- Creating nested directories.
- Using brace expansion.
- Creating files.
- Organizing cybersecurity projects.

---

## Practical 2: Find All .log Files in a Directory

### Objective

Learn to locate log files recursively.

### Step 1: Create a Test Directory

```bash
mkdir -p ~/linux-practice/logs/archive
```

### Step 2: Create Test Log Files

```bash
touch ~/linux-practice/logs/system.log
touch ~/linux-practice/logs/application.log
touch ~/linux-practice/logs/archive/old.log
touch ~/linux-practice/logs/notes.txt
```

### Step 3: Search for Log Files

```bash
find ~/linux-practice/logs -type f -name "*.log"
```

### Expected Output

```text
/home/pulok/linux-practice/logs/system.log
/home/pulok/linux-practice/logs/application.log
/home/pulok/linux-practice/logs/archive/old.log
```

The order may differ.

### Step 4: Count the Log Files

```bash
find ~/linux-practice/logs -type f -name "*.log" | wc -l
```

Expected output:

```text
3
```

### Step 5: Search Case-Insensitively

```bash
find ~/linux-practice/logs -type f -iname "*.LOG"
```

### What You Learned

- Recursive file searching.
- Filename patterns.
- File-type filtering.
- Combining find and wc.

---

## Practical 3: Search a Log for Failed-Login Messages

### Objective

Learn how to identify failed authentication attempts in a log file.

### Step 1: Create a Test Log

```bash
cat > ~/linux-practice/auth.log <<'EOF'
Nov 09 09:00:01 server sshd: Accepted password for pulok
Nov 09 09:01:15 server sshd: Failed password for invalid user admin
Nov 09 09:02:30 server sshd: Failed password for root
Nov 09 09:03:10 server sshd: Accepted publickey for pulok
Nov 09 09:04:20 server sshd: Failed password for test
EOF
```

This creates a sample authentication log using a here-document.

### Step 2: Display the Log

```bash
cat ~/linux-practice/auth.log
```

### Step 3: Search for Failed Password Entries

```bash
grep "Failed password" ~/linux-practice/auth.log
```

### Expected Output

```text
Nov 09 09:01:15 server sshd: Failed password for invalid user admin
Nov 09 09:02:30 server sshd: Failed password for root
Nov 09 09:04:20 server sshd: Failed password for test
```

### Step 4: Search Case-Insensitively

```bash
grep -i "failed password" ~/linux-practice/auth.log
```

### Step 5: Display Line Numbers

```bash
grep -in "failed password" ~/linux-practice/auth.log
```

### Step 6: Count Failed-Login Lines

```bash
grep -ic "failed password" ~/linux-practice/auth.log
```

Expected output:

```text
3
```

### Step 7: Display Only Matching Lines Without Other Text

```bash
grep -i "failed password" ~/linux-practice/auth.log
```

### Step 8: Monitor the Log

In one terminal:

```bash
tail -f ~/linux-practice/auth.log
```

In another terminal:

```bash
echo "Nov 09 09:05:00 server sshd: Failed password for guest" >> ~/linux-practice/auth.log
```

The first terminal should display the new entry.

Stop monitoring with `Ctrl + C`.

### What You Should Observe

- `grep` identifies failed-login entries.
- `-i` ignores letter case.
- `-n` displays line numbers.
- `-c` counts matching lines.
- `tail -f` displays newly appended entries.

### Cybersecurity Connection

This exercise demonstrates a simplified authentication-log investigation.

In real environments, failed login events should be interpreted alongside:

- Source IP addresses.
- Usernames.
- Timestamps.
- Authentication methods.
- Successful login events.
- Other related system events.

A failed login by itself does not prove an attack.

---

## Practical 4: Extract Selected Columns from a Text File

### Objective

Learn how to extract fields from structured text using `cut`.

### Step 1: Create a Sample File

```bash
cat > ~/linux-practice/users.txt <<'EOF'
pulok:admin:1001
rahul:user:1002
amit:guest:1003
john:developer:1004
EOF
```

### Step 2: Display the File

```bash
cat ~/linux-practice/users.txt
```

### Step 3: Extract Usernames

```bash
cut -d ':' -f1 ~/linux-practice/users.txt
```

Expected output:

```text
pulok
rahul
amit
john
```

### Step 4: Extract Roles

```bash
cut -d ':' -f2 ~/linux-practice/users.txt
```

Expected output:

```text
admin
user
guest
developer
```

### Step 5: Extract IDs

```bash
cut -d ':' -f3 ~/linux-practice/users.txt
```

Expected output:

```text
1001
1002
1003
1004
```

### Step 6: Extract Username and ID

```bash
cut -d ':' -f1,3 ~/linux-practice/users.txt
```

Expected output:

```text
pulok:1001
rahul:1002
amit:1003
john:1004
```

### Step 7: Convert the Delimiter

```bash
cut -d ':' -f1,3 ~/linux-practice/users.txt | tr ':' ','
```

Expected output:

```text
pulok,1001
rahul,1002
amit,1003
john,1004
```

### What You Learned

- Extracting fields.
- Specifying delimiters.
- Selecting multiple columns.
- Combining cut and tr.

---

## Practical 5: Save Command Output to a Report File

### Objective

Learn how to capture system information and save it into a report.

### Step 1: Create a Report Directory

```bash
mkdir -p ~/Cybersecurity/Reports
```

### Step 2: Create a Report File

```bash
touch ~/Cybersecurity/Reports/system-report.txt
```

### Step 3: Save the Date

```bash
date > ~/Cybersecurity/Reports/system-report.txt
```

The `>` operator overwrites the destination.

### Step 4: Append Hostname

```bash
hostname >> ~/Cybersecurity/Reports/system-report.txt
```

### Step 5: Append Kernel Information

```bash
uname -a >> ~/Cybersecurity/Reports/system-report.txt
```

### Step 6: Append Distribution Information

```bash
cat /etc/os-release >> ~/Cybersecurity/Reports/system-report.txt
```

### Step 7: Append Memory Information

```bash
free -h >> ~/Cybersecurity/Reports/system-report.txt
```

### Step 8: Append Disk Information

```bash
df -h >> ~/Cybersecurity/Reports/system-report.txt
```

### Step 9: Display the Report

```bash
cat ~/Cybersecurity/Reports/system-report.txt
```

### Alternative: Generate a Report Using tee

```bash
{
    echo "SYSTEM REPORT"
    echo "============="
    echo
    date
    echo
    hostname
    echo
    uname -a
    echo
    free -h
    echo
    df -h
} | tee ~/Cybersecurity/Reports/system-report-2.txt
```

This displays the report in the terminal and saves it into a file.

### Verification

```bash
ls -lh ~/Cybersecurity/Reports/
```

```bash
wc -l ~/Cybersecurity/Reports/system-report.txt
```

### What You Learned

- Output redirection.
- Appending data.
- Using `tee`.
- Generating a system report.
- Combining multiple commands.

---

## Practical 6: Combine Commands for Log Analysis

### Objective

Practise a realistic text-analysis workflow.

### Step 1: Create a Sample Access Log

```bash
cat > ~/linux-practice/access.log <<'EOF'
192.168.1.10 GET /index.html 200
192.168.1.20 POST /login 401
192.168.1.10 GET /dashboard 200
192.168.1.30 POST /login 401
192.168.1.20 GET /admin 403
192.168.1.10 GET /profile 200
192.168.1.20 POST /login 401
EOF
```

This is a simplified custom log format for practising text processing, not a standard Apache or Nginx log format.

### Step 2: Find Failed HTTP Status Codes

```bash
grep " 401$" ~/linux-practice/access.log
```

### Step 3: Extract IP Addresses from Failed Requests

```bash
grep " 401$" ~/linux-practice/access.log | cut -d ' ' -f1
```

### Step 4: Count Requests Per IP

```bash
grep " 401$" ~/linux-practice/access.log | cut -d ' ' -f1 | sort | uniq -c
```

Expected output:

```text
2 192.168.1.20
1 192.168.1.30
```

### Step 5: Sort by Request Frequency

```bash
grep " 401$" ~/linux-practice/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -nr
```

### Step 6: Save the Analysis

```bash
grep " 401$" ~/linux-practice/access.log | cut -d ' ' -f1 | sort | uniq -c | sort -nr | tee ~/Cybersecurity/Reports/failed-requests.txt
```

### What You Learned

- Searching text patterns.
- Filtering HTTP status codes.
- Extracting IP addresses.
- Counting repeated values.
- Sorting results.
- Saving analysis reports.

### Cybersecurity Connection

This is a basic example of analyzing repeated failed HTTP responses.

In a real web application, investigate the associated endpoints, timestamps, session context, request methods, and response patterns before deciding whether activity is suspicious.

---

# 9. Common Mistakes and Troubleshooting

## 9.1 Using the Wrong Directory

Problem:

```bash
rm notes.txt
```

You receive:

```text
No such file or directory
```

Possible reason:

You are not in the directory containing the file.

Solution:

```bash
pwd
ls -la
```

Then navigate to the correct location.

## 9.2 Forgetting Recursive Options

Problem:

```bash
cp project backup
```

Fails when attempting to copy a directory without recursive handling.

Solution:

```bash
cp -r project backup
```

## 9.3 Using rm on an Important Directory

Problem:

```bash
rm -rf project
```

Can delete an entire directory tree without an ordinary confirmation prompt.

Solution:

Inspect the target first:

```bash
pwd
ls -la project
```

Use interactive removal when appropriate:

```bash
rm -ri project
```

## 9.4 Forgetting Quotes Around Filenames

A filename containing spaces should normally be quoted.

Incorrect:

```bash
cat my notes.txt
```

Correct:

```bash
cat "my notes.txt"
```

Alternative:

```bash
cat my\ notes.txt
```

## 9.5 Searching with an Unquoted Wildcard

Incorrect:

```bash
find /var/log -name *.log
```

The shell may expand the wildcard before `find` receives it.

Correct:

```bash
find /var/log -name "*.log"
```

## 9.6 Expecting uniq to Find Every Duplicate

Problem:

```bash
uniq names.txt
```

Does not remove duplicates that are separated by other lines.

Solution:

```bash
sort names.txt | uniq
```

## 9.7 Expecting locate to Find a Newly Created File

Problem:

```bash
locate newfile.txt
```

Does not show a file that was created after the database update.

Solution:

```bash
sudo updatedb
```

Then search again, if the implementation supports this command.

## 9.8 Using grep on Binary Files

Some files are binary rather than ordinary text.

`grep` may display a binary-file match message or produce unexpected results.

For binary content, use suitable file-inspection or analysis tools.

Start by identifying the file:

```bash
file suspicious-file
```

## 9.9 Confusing > and >>

Incorrect when you want to preserve existing content:

```bash
echo "New entry" > report.txt
```

This overwrites the file.

Correct for appending:

```bash
echo "New entry" >> report.txt
```

## 9.10 Forgetting Vim Modes

If you type in Vim but text does not appear as expected, you may be in Normal mode.

Press:

```text
i
```

to enter Insert mode.

Press:

```text
Esc
```

to return to Normal mode.

---

# 10. Security Best Practices

While learning file-management and searching commands, follow these practices.

## 10.1 Verify Before Deleting

Before using `rm`, inspect the target.

```bash
pwd
ls -la
```

## 10.2 Avoid Unnecessary sudo

Do not use root privileges for normal file operations inside your home directory.

## 10.3 Use Trusted Files and Directories

Do not execute scripts merely because they are located in a directory with a familiar name.

Inspect them first.

```bash
file script.sh
cat script.sh
```

## 10.4 Protect Sensitive Files

Be careful with:

- SSH private keys.
- Password files.
- API tokens.
- Environment files.
- Application configuration files.

Never publish sensitive content in reports.

## 10.5 Avoid Unsafe Wildcard Operations

Before running:

```bash
rm *.log
```

Inspect matching files:

```bash
printf '%s\n' *.log
```

## 10.6 Be Careful with Recursive Searches

Commands such as:

```bash
find /
```

can produce large amounts of output and permission errors.

Prefer a targeted starting directory.

## 10.7 Validate Configuration Changes

Before modifying important configuration files:

1. Inspect the existing content.
2. Create a backup.
3. Understand the intended change.
4. Make the modification.
5. Validate the configuration.
6. Restart or reload the relevant service only when necessary.

## 10.8 Keep Investigation Records

When performing authorized security work, save relevant command output and document:

- Date and time.
- System or lab being examined.
- Commands executed.
- Findings.
- Limitations.
- Relevant evidence.

---

# 11. Quick Revision

## 11.1 Navigation and File Management

| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls` | List directory contents |
| `ls -la` | Detailed listing including hidden entries |
| `cd` | Change directory |
| `tree` | Display directory hierarchy |
| `mkdir` | Create directory |
| `mkdir -p` | Create nested directories |
| `touch` | Create empty file or update timestamps |
| `cp` | Copy files |
| `cp -r` | Copy directories recursively |
| `mv` | Move or rename files |
| `rm` | Remove files |
| `rm -r` | Remove directory recursively |
| `rmdir` | Remove empty directories |

## 11.2 Reading and Editing

| Command | Purpose |
|---|---|
| `cat` | Display or concatenate files |
| `less` | Read files page by page |
| `head` | Display first lines |
| `tail` | Display last lines |
| `tail -f` | Follow a file as it grows |
| `nano` | Simple terminal text editor |
| `vim` | Modal terminal text editor |
| `file` | Identify file type |
| `stat` | Display file metadata |
| `wc` | Count lines, words, and bytes |
| `sort` | Sort text lines |
| `uniq` | Process adjacent duplicate lines |
| `cut` | Extract fields or character positions |
| `paste` | Merge corresponding lines |
| `tr` | Translate, delete, or squeeze characters |
| `tee` | Display and save standard input |

## 11.3 Searching and Finding

| Command | Purpose |
|---|---|
| `find` | Search filesystem entries |
| `grep` | Search text patterns |
| `grep -i` | Case-insensitive search |
| `grep -r` | Recursive text search |
| `grep -n` | Display line numbers |
| `grep -v` | Invert matching |
| `grep -c` | Count matching lines |
| `locate` | Search indexed filenames |
| `which` | Locate executable through PATH |
| `whereis` | Locate binary, source, and manual files |
| `command -v` | Identify shell command resolution |

## 11.4 Important Operators and Symbols

| Symbol | Purpose |
|---|---|
| `>` | Redirect stdout and overwrite |
| `>>` | Redirect stdout and append |
| `2>` | Redirect stderr |
| `2>&1` | Redirect stderr to current stdout destination |
| `|` | Pipe output to another command |
| `*` | Match zero or more filename characters |
| `?` | Match one filename character |
| `[abc]` | Match one character from a set |
| `~` | Home directory |
| `.` | Current directory |
| `..` | Parent directory |
| `{}` | Placeholder in find -exec |
| `;` | Command separator or find -exec terminator, depending on context |

---

# 12. Interview and Self-Assessment Questions

## Beginner-Level Questions

### Q1. What is the purpose of the pwd command?

It displays the current working directory.

### Q2. What is the difference between ls and ls -la?

`ls` displays ordinary directory entries, whereas `ls -la` displays detailed information, including hidden entries.

### Q3. What is the purpose of cd?

It changes the current working directory.

### Q4. What is the difference between mkdir and touch?

`mkdir` creates directories, while `touch` creates an empty file if it does not exist.

### Q5. What is the difference between cp and mv?

`cp` copies files, whereas `mv` moves or renames files.

### Q6. What is the difference between rm and rmdir?

`rm` removes files and can recursively remove directories. `rmdir` removes empty directories.

### Q7. What is an absolute path?

A path that starts from the root directory `/`.

### Q8. What is a relative path?

A path interpreted relative to the current working directory.

### Q9. How do you display hidden files?

```bash
ls -a
```

### Q10. What does the wildcard * represent?

It matches zero or more characters in a filename component.

### Q11. What is the purpose of cat?

It displays and concatenates file contents.

### Q12. What is the difference between head and tail?

`head` displays the beginning of a file, whereas `tail` displays its end.

### Q13. What is the purpose of tail -f?

It monitors new data appended to a file.

### Q14. What is the difference between nano and Vim?

Nano is a simple terminal editor, while Vim is a modal editor with more advanced editing capabilities.

### Q15. What does file command do?

It identifies a file's type using its content and other information.

## Intermediate-Level Questions

### Q16. What is the difference between mtime and ctime?

mtime represents the last content modification time. ctime represents the last metadata change time, which can also change when file contents change.

### Q17. What does wc -l do?

It counts newline characters, generally corresponding to the number of lines in ordinary text files.

### Q18. Why is sort often combined with uniq?

Because uniq processes adjacent duplicate lines. Sorting groups identical lines together.

### Q19. What is the difference between cut and paste?

`cut` extracts selected portions of input lines. `paste` combines corresponding lines from multiple inputs.

### Q20. What is the purpose of tr?

It translates, deletes, or squeezes characters in standard input.

### Q21. What does tee do?

It sends standard input to standard output and one or more files.

### Q22. What is the difference between find and locate?

`find` searches the filesystem directly, while `locate` searches a prebuilt filename database.

### Q23. What is the difference between grep -i and grep -n?

`-i` ignores case, while `-n` displays matching line numbers.

### Q24. Why should wildcard patterns be quoted when used with find?

Quoting prevents the shell from expanding the pattern before `find` receives it.

### Q25. What is the difference between which and command -v?

`which` searches for executable commands through PATH. `command -v` identifies how the shell resolves a command, including built-ins and functions.

## Practical and Scenario-Based Questions

### Q26. How do you find all .log files recursively?

```bash
find /path/to/directory -type f -name "*.log"
```

### Q27. How do you search for failed password messages in a log?

```bash
grep -i "failed password" auth.log
```

### Q28. How do you display line numbers for matching error messages?

```bash
grep -in "error" application.log
```

### Q29. How do you count failed login entries?

```bash
grep -ic "failed password" auth.log
```

### Q30. How do you extract the first field from a colon-separated file?

```bash
cut -d ':' -f1 users.txt
```

### Q31. How do you save command output to a file without displaying it?

```bash
ls -la > report.txt
```

### Q32. How do you display command output and save it simultaneously?

```bash
ls -la | tee report.txt
```

### Q33. How do you append command output to an existing file?

```bash
date >> report.txt
```

### Q34. How do you identify the executable path of Python?

```bash
command -v python3
```

### Q35. How do you count unique IP addresses in a file containing one IP per line?

```bash
sort ips.txt | uniq | wc -l
```

---

# 13. Learning Checklist

Use this checklist to track your progress.

## Navigation

- [ ] I understand the Linux command structure.
- [ ] I can use `pwd`.
- [ ] I can use `ls`.
- [ ] I understand `ls -la`.
- [ ] I can navigate using `cd`.
- [ ] I can use `tree`.
- [ ] I can create directories using `mkdir`.
- [ ] I can create files using `touch`.
- [ ] I can copy files using `cp`.
- [ ] I can move and rename files using `mv`.
- [ ] I understand `rm` and `rmdir`.
- [ ] I understand absolute and relative paths.
- [ ] I understand hidden files and directories.
- [ ] I understand wildcard patterns.

## Reading and Editing Files

- [ ] I can display files using `cat`.
- [ ] I can read large files using `less`.
- [ ] I can display the beginning of a file using `head`.
- [ ] I can display the end of a file using `tail`.
- [ ] I can monitor logs using `tail -f`.
- [ ] I can edit files using `nano`.
- [ ] I understand basic Vim modes.
- [ ] I can identify file types using `file`.
- [ ] I can inspect metadata using `stat`.
- [ ] I can count lines and words using `wc`.
- [ ] I can sort text using `sort`.
- [ ] I understand adjacent duplicate handling using `uniq`.
- [ ] I can extract fields using `cut`.
- [ ] I can merge text using `paste`.
- [ ] I can translate characters using `tr`.
- [ ] I can save output using `tee`.

## Searching

- [ ] I can search for files using `find`.
- [ ] I can search file contents using `grep`.
- [ ] I understand `grep -i`.
- [ ] I understand `grep -r`.
- [ ] I understand `grep -n`.
- [ ] I understand other useful grep options.
- [ ] I can search indexed filenames using `locate`.
- [ ] I understand `which`.
- [ ] I understand `whereis`.
- [ ] I can use `command -v`.
- [ ] I can search Linux logs.
- [ ] I can inspect configuration files.
- [ ] I can combine commands using pipes.

## Practical Skills

- [ ] I created a cybersecurity directory structure.
- [ ] I created files and subdirectories.
- [ ] I found all `.log` files in a directory.
- [ ] I searched for failed-login messages.
- [ ] I extracted selected fields from a text file.
- [ ] I saved system information into a report.
- [ ] I combined multiple commands to analyze log data.
- [ ] I understand the difference between `>` and `>>`.
- [ ] I can use `tee` to save and display output.

---

# 14. Phase 2 Completion Criteria

Before moving to Phase 3, you should be comfortable performing these tasks without constantly looking at your notes:

1. Navigate anywhere in your Linux filesystem.
2. Create, copy, move, rename, and delete files safely.
3. Read small and large text files.
4. Edit text files using nano.
5. Perform basic editing in Vim.
6. Find files using find and locate.
7. Search text using grep.
8. Extract information using cut.
9. Sort and count repeated entries using sort and uniq.
10. Combine commands using pipes.
11. Redirect output into files.
12. Generate a basic system or log-analysis report.

## Final Learning Advice

Do not try to memorize all these commands in one sitting.

Practise them in your Ubuntu or Kali Linux terminal.

A useful approach is:

- First, understand what a command does.
- Second, execute it yourself.
- Third, experiment with its options.
- Fourth, combine it with another command.
- Fifth, explain its output in your own words.

Pay particular attention to these commands:

```bash
pwd
ls -la
cd
mkdir
cp
mv
rm
cat
less
head
tail -f
grep
find
cut
sort
uniq
tee
```

These commands will become building blocks for more advanced Linux topics and Bash scripting.

**Phase 2 Completion Goal:** You should be able to navigate the filesystem, manage files, inspect text, search logs, extract useful information, and generate reports entirely through the Linux terminal.

**End of Phase 2 — Essential Linux Commands**
