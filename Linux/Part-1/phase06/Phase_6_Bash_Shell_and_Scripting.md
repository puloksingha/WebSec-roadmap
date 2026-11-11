
# PHASE 6 — BASH SHELL AND SCRIPTING

# PART 1: SHELL FUNDAMENTALS

## 1. What Is a Shell?

A shell is a command-line interpreter that allows users to interact with the operating system.

It accepts commands from the user, interprets them, and requests the operating system to execute the required operations.

For example:

```bash
ls
```

When you execute this command:

1. The shell receives the command.
2. It identifies the executable.
3. It passes the required arguments.
4. The operating system executes the program.
5. The output is displayed in the terminal.

### 1.1 What Is Bash?

Bash stands for Bourne Again Shell.

It is a widely used Unix shell and command language.

Bash provides:

- Command execution.
- Variables.
- Conditional statements.
- Loops.
- Functions.
- Input and output redirection.
- Command pipelines.
- Shell scripting.
- Automation.

Bash is commonly available on Linux distributions, including Kali Linux.

Check your Bash version:

```bash
bash --version
```

Check your current shell:

```bash
echo $SHELL
```

Check the current process:

```bash
ps -p $$ -o comm=
```

## 2. Bash vs Other Shells

Linux supports different shells. Each shell provides a command-line environment with its own features and syntax.

Common shells include:

| Shell | Full name / Description |
|---|---|
| Bash | Bourne Again Shell |
| sh | Bourne-style shell interface |
| Zsh | Z Shell |
| Fish | Friendly Interactive Shell |
| Ksh | Korn Shell |
| Tcsh | TENEX C Shell |

### Bash

- Widely used in Linux.
- Supports variables, functions, loops, and conditions.
- Commonly used for automation.
- Compatible with many traditional shell scripts.

### Zsh

- Provides advanced interactive shell features.
- Supports extensive customization.
- Popular among developers and Linux users.

### Fish

- Designed to be user-friendly.
- Provides syntax highlighting and autosuggestions.
- Has syntax that differs from Bash.

### Difference Between Bash and sh

`sh` traditionally refers to the Bourne shell interface.

On modern Linux systems, `/bin/sh` may point to a different POSIX-compatible shell, such as Dash.

Bash supports additional features that are not necessarily available in POSIX shell scripts.

Important:

If portability is important, write scripts using POSIX shell syntax. If you need Bash-specific features, explicitly use Bash.

---

## 3. Shell Prompt and Command History

### 3.1 What Is a Shell Prompt?

A shell prompt is the text displayed by the terminal when it is ready to receive a command.

Example:

```text
student@kali:~$
```

Its components:

- `student`: Current username.
- `kali`: Hostname.
- `~`: Current directory (home directory).
- `$`: Indicates a regular user's shell prompt.

The root user's prompt commonly ends with:

```text
#
```

Example:

```text
root@kali:~#
```

The appearance of prompts can be customized.

### 3.2 Command History

Bash maintains a history of previously executed commands.

Display command history:

```bash
history
```

Display the last 10 commands:

```bash
history 10
```

Search history:

```bash
history | grep apt
```

Useful keyboard shortcuts:

| Shortcut | Function |
|---|---|
| Up Arrow | Previous command |
| Down Arrow | Next command |
| Ctrl + R | Search command history |
| Ctrl + A | Move to beginning of line |
| Ctrl + E | Move to end of line |
| Ctrl + U | Delete from cursor to beginning |
| Ctrl + K | Delete from cursor to end |
| Ctrl + L | Clear terminal screen |
| Ctrl + C | Interrupt current foreground command |

History is commonly stored in:

```text
~/.bash_history
```

Note: Commands from the current session may not be written to this file until the shell exits or history is explicitly saved.

---

## 4. Command Options and Arguments

A command may accept options and arguments.

### Command

The executable you want to run.

### Option

Changes how the command behaves.

### Argument

Provides information or a target to the command.

Example:

```bash
ls -l /home
```

Here:

- `ls` = Command.
- `-l` = Option.
- `/home` = Argument.

Another example:

```bash
grep -i "error" system.log
```

Here:

- `grep` = Command.
- `-i` = Case-insensitive option.
- `"error"` = Search pattern.
- `system.log` = File argument.

### 4.1 Short and Long Options

Short option:

```bash
ls -l
```

Long option:

```bash
ls --all
```

Some commands allow multiple short options together:

```bash
ls -lah
```

Always check the manual when you are unsure:

```bash
man ls
```

You can also use:

```bash
ls --help
```

---

## 5. Quoting in Bash

Quoting controls how Bash interprets characters and expressions.

The three important forms are:

1. Single quotes.
2. Double quotes.
3. Backslash escaping.

### 5.1 Single Quotes (' ')

Single quotes preserve the literal meaning of almost every character inside them.

Example:

```bash
echo 'Hello Linux'
```

Output:

```text
Hello Linux
```

Variables are not expanded inside single quotes.

Example:

```bash
name="Pulok"

echo '$name'
```

Output:

```text
$name
```

### 5.2 Double Quotes (" ")

Double quotes preserve most characters literally but allow variable expansion and command substitution.

Example:

```bash
name="Pulok"

echo "Hello $name"
```

Output:

```text
Hello Pulok
```

Command substitution also works inside double quotes:

```bash
echo "Today is $(date)"
```

### 5.3 Difference Between Single and Double Quotes

| Feature | Single quotes | Double quotes |
|---|---|---|
| Variable expansion | No | Yes |
| Command substitution | No | Yes |
| Preserves spaces | Yes | Yes |
| Preserves most special characters literally | Yes | Mostly |

### 5.4 Why Quoting Matters

Suppose a filename contains spaces:

```text
my report.txt
```

This command can cause problems:

```bash
cat my report.txt
```

Bash treats the words as separate arguments.

Correct:

```bash
cat "my report.txt"
```

This is especially important when writing scripts that handle filenames supplied by users.

---

## 6. Escaping Special Characters

Some characters have special meanings in Bash.

Examples:

```text
$  *  ?  ;  &  |  >  <  (  )  \  "  '
```

A backslash (`\`) can escape the special meaning of a character.

Example:

```bash
echo \$HOME
```

Output:

```text
$HOME
```

Without escaping:

```bash
echo $HOME
```

Bash expands the variable and displays its value.

### Escaping Spaces in Filenames

```bash
touch my\ report.txt
```

This creates a file named:

```text
my report.txt
```

Alternative:

```bash
touch "my report.txt"
```

---

# PART 2: VARIABLES AND COMMAND EXECUTION

## 7. Environment Variables

An environment variable is a named value made available to processes running in an environment.

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

Display a specific variable:

```bash
echo "$HOME"
echo "$USER"
echo "$SHELL"
echo "$PATH"
```

### 7.1 PATH

`PATH` contains directories where the shell searches for executable commands.

Example:

```bash
echo "$PATH"
```

Possible output:

```text
/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin
```

The colon (`:`) separates directory paths.

When you execute:

```bash
python3
```

Bash searches the directories listed in PATH to find the executable.

### 7.2 HOME

`HOME` stores the current user's home directory.

Example:

```bash
echo "$HOME"
```

Possible output:

```text
/home/student
```

### 7.3 USER

`USER` commonly contains the current username.

Example:

```bash
echo "$USER"
```

### 7.4 export

The `export` command makes a shell variable available to child processes through the environment.

Example:

```bash
MYNAME="Pulok"
export MYNAME
```

Or:

```bash
export MYNAME="Pulok"
```

Display it:

```bash
echo "$MYNAME"
```

Run a child shell:

```bash
bash -c 'echo "$MYNAME"'
```

The child shell can access the exported variable.

### 7.5 alias

An alias creates a shortcut for a command or command sequence.

Example:

```bash
alias ll='ls -lah'
```

Now execute:

```bash
ll
```

Display aliases:

```bash
alias
```

Remove an alias:

```bash
unalias ll
```

Create a persistent alias by adding it to:

```text
~/.bashrc
```

Example:

```bash
echo "alias ll='ls -lah'" >> ~/.bashrc
```

Reload:

```bash
source ~/.bashrc
```

---

## 8. Command Substitution

Command substitution allows you to execute a command and use its output inside another command.

Modern recommended syntax:

```bash
$(command)
```

Example:

```bash
today=$(date)
echo "$today"
```

Another example:

```bash
current_user=$(whoami)
echo "Current user: $current_user"
```

Get the current directory:

```bash
current_dir=$(pwd)
echo "$current_dir"
```

Command substitution is useful for:

- Generating timestamps.
- Collecting system information.
- Storing command output in variables.
- Automating reports.

Older syntax:

```bash
`command`
```

Example:

```bash
today=`date`
```

Prefer `$(command)` because it is easier to read and nest.

---

## 9. Exit Status ($?)

An exit status is a numeric value returned by a command after execution.

It indicates whether the command completed successfully.

Convention:

- `0` = Success.
- Non-zero = Failure or another status.

Check the exit status:

```bash
ls
echo $?
```

If the command succeeds, the result is normally:

```text
0
```

Try an invalid command:

```bash
invalidcommand
echo $?
```

The result will be a non-zero value.

### Why Exit Status Matters

Bash scripts use exit statuses to decide what to do next.

Example:

```bash
mkdir test_directory

if [ $? -eq 0 ]; then
    echo "Directory created successfully"
else
    echo "Directory creation failed"
fi
```

A cleaner approach is to place the command directly in the condition:

```bash
if mkdir test_directory; then
    echo "Directory created successfully"
else
    echo "Directory creation failed"
fi
```

---

# PART 3: INPUT, OUTPUT, REDIRECTION, AND PIPES

## 10. Standard Input, Output, and Error

Linux programs commonly use three standard data streams.

| Stream | File descriptor | Purpose |
|---|---:|---|
| Standard Input (stdin) | 0 | Receives input |
| Standard Output (stdout) | 1 | Displays normal output |
| Standard Error (stderr) | 2 | Displays error messages |

### 10.1 Standard Input

Standard input is the data received by a program.

By default, it usually comes from the keyboard in an interactive terminal.

Example:

```bash
cat
```

Type some text and press Ctrl + D to finish.

### 10.2 Standard Output

Standard output carries normal command results.

Example:

```bash
ls
```

### 10.3 Standard Error

Standard error carries error messages.

Example:

```bash
ls /directory_that_does_not_exist
```

The error message is normally displayed in the terminal.

---

## 11. Input and Output Redirection

Redirection changes where a command receives input or sends output.

### 11.1 Output Redirection (>)

The `>` operator sends standard output to a file.

Example:

```bash
echo "Linux practice" > output.txt
```

If the file does not exist, it is created.

If it already exists, its previous contents are overwritten.

### 11.2 Append Redirection (>>)

The `>>` operator appends output to the end of a file.

Example:

```bash
echo "Second line" >> output.txt
```

Unlike `>`, it does not overwrite existing contents.

### 11.3 Input Redirection (<)

The `<` operator takes input from a file.

Example:

```bash
wc -l < output.txt
```

This passes the contents of `output.txt` to the standard input of `wc`.

### 11.4 Error Redirection (2>)

The `2>` operator redirects standard error.

Example:

```bash
ls /invalid_directory 2> errors.txt
```

The error message is saved in `errors.txt`.

### 11.5 Redirect Both Output and Error

Use:

```bash
command > output.txt 2>&1
```

This redirects standard output to `output.txt`, then redirects standard error to the same destination.

Modern Bash also supports:

```bash
command &> output.txt
```

### 11.6 Discard Output

Linux provides a special device:

```text
/dev/null
```

Anything written to it is discarded.

Discard standard output:

```bash
command > /dev/null
```

Discard standard error:

```bash
command 2> /dev/null
```

Discard both:

```bash
command > /dev/null 2>&1
```

Use this carefully. Discarding errors can make troubleshooting harder.

---

## 12. Pipes (|)

A pipe sends the standard output of one command to the standard input of another command.

Syntax:

```bash
command1 | command2
```

Example:

```bash
ls -l | less
```

The output of `ls -l` becomes the input of `less`.

### Common Examples

Search for a process:

```bash
ps aux | grep firefox
```

Count files:

```bash
ls | wc -l
```

Search for errors in a log:

```bash
grep -i "error" system.log | less
```

Count failed login messages:

```bash
grep -i "failed" auth.log | wc -l
```

Pipes are extremely useful in Linux because they allow small commands to work together.

---

## 13. Logical Operators: &&, ||, and ;

These operators control how multiple commands execute.

### 13.1 AND Operator (&&)

The next command executes only if the previous command succeeds.

Example:

```bash
mkdir project && cd project
```

If directory creation succeeds, Bash executes `cd project`.

### 13.2 OR Operator (||)

The next command executes only if the previous command fails.

Example:

```bash
ping -c 1 127.0.0.1 || echo "Ping failed"
```

### 13.3 Semicolon (;)

The semicolon separates commands and executes them sequentially, regardless of whether an earlier command succeeds.

Example:

```bash
pwd; date; whoami
```

### Difference

| Operator | Behaviour |
|---|---|
| `&&` | Execute next command if previous succeeds |
| `||` | Execute next command if previous fails |
| `;` | Execute commands sequentially |

---

## 14. xargs Command

`xargs` reads items from standard input and uses them as arguments for another command.

Example:

```bash
echo "file1.txt file2.txt" | xargs touch
```

This creates two files.

Another example:

```bash
find . -name "*.tmp" -print0 | xargs -0 -r rm --
```

This removes matching temporary files in the current directory tree.

Important options:

- `-0`: Read null-separated input.
- `-r`: Do not run the command if there is no input.
- `-I`: Replace a placeholder with each input item.

Example:

```bash
printf '%s\n' "Pulok" "Linux" | xargs -I {} echo "Hello {}"
```

### Why -0 Matters

Filenames can contain spaces, tabs, and even newline characters.

For safe filename handling, combine:

```bash
find . -type f -print0 | xargs -0 command
```

This avoids many problems caused by ordinary whitespace-separated input.

---

## 15. tee Command

The `tee` command reads standard input and writes it both to the terminal and to a file.

Example:

```bash
echo "Linux practice" | tee output.txt
```

It displays the text and saves it in `output.txt`.

Append instead of overwrite:

```bash
echo "Another line" | tee -a output.txt
```

Useful for logging command output:

```bash
df -h | tee disk_report.txt
```

To save both standard output and standard error:

```bash
command 2>&1 | tee command.log
```

---

# PART 4: BASH SCRIPTING FUNDAMENTALS

## 16. What Is Bash Scripting?

Bash scripting means writing a sequence of shell commands in a file so that they can execute automatically.

Instead of manually running commands one by one, you can place them inside a script.

A Bash script can:

- Collect system information.
- Check running services.
- Process log files.
- Create backups.
- Automate repetitive tasks.
- Generate reports.
- Perform basic system checks.

Bash scripts generally use the `.sh` filename extension, although the extension is not technically required.

---

## 17. Creating and Running a Bash Script

Create a file:

```bash
nano hello.sh
```

Write:

```bash
#!/usr/bin/env bash

echo "Hello, Linux!"
echo "Welcome to Bash scripting."
```

Save and exit.

### 17.1 What Is a Shebang?

The first line:

```bash
#!/usr/bin/env bash
```

is called the shebang.

It tells the operating system which interpreter should execute the script when it is run as a program.

`/usr/bin/env` locates Bash using the current environment's PATH.

### 17.2 Run the Script Using Bash

```bash
bash hello.sh
```

This does not require the file to have executable permission.

### 17.3 Make the Script Executable

```bash
chmod +x hello.sh
```

Run:

```bash
./hello.sh
```

The `./` indicates that the script is located in the current directory.

---

## 18. Variables in Bash

Variables store values that can be reused.

Example:

```bash
name="Pulok"
age=22

echo "Name: $name"
echo "Age: $age"
```

Important rules:

- Do not put spaces around `=` when assigning a variable.
- Use `$variable` to access its value.
- Use quotes around variables when handling strings.

Correct:

```bash
name="Pulok"
```

Incorrect:

```bash
name = "Pulok"
```

### 18.1 Variable Naming Rules

- Names can contain letters, numbers, and underscores.
- Names cannot start with a number.
- Variable names are case-sensitive.

Example:

```bash
username="student"
USER_NAME="student"
```

These are different variables.

### 18.2 Read-Only Variables

Use `readonly` to prevent reassignment:

```bash
readonly VERSION="1.0"
```

Trying to change it will produce an error.

---

## 19. Positional Parameters

Positional parameters allow a script to receive values from the command line.

Example script:

```bash
#!/usr/bin/env bash

echo "First argument: $1"
echo "Second argument: $2"
```

Run:

```bash
bash script.sh Linux Security
```

Output:

```text
First argument: Linux
Second argument: Security
```

### Important Positional Parameters

| Parameter | Meaning |
|---|---|
| `$0` | Script name |
| `$1` | First argument |
| `$2` | Second argument |
| `$3` | Third argument |
| `$@` | All positional arguments as separate words |
| `$*` | All positional arguments as a combined list |
| `$#` | Number of positional arguments |
| `$$` | PID of the current shell |
| `$?` | Exit status of the last command |

### 19.1 Using $@

Example:

```bash
#!/usr/bin/env bash

for item in "$@"; do
    echo "Argument: $item"
done
```

Run:

```bash
bash script.sh Linux "Web Security" Python
```

Quoting `"$@"` preserves each argument as a separate item, including arguments containing spaces.

### 19.2 Using $#

```bash
#!/usr/bin/env bash

echo "Total arguments: $#"
```

Run:

```bash
bash script.sh one two three
```

Output:

```text
Total arguments: 3
```

---

## 20. read Command

The `read` command accepts input from the user.

Example:

```bash
#!/usr/bin/env bash

echo "Enter your name:"
read name

echo "Hello, $name"
```

A shorter version:

```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

Read a password without displaying it:

```bash
read -rsp "Enter password: " password
echo
```

For secret input, avoid printing or logging the variable.

---

## 21. Conditional Statements

Conditional statements allow a script to make decisions.

Bash supports:

- `if`
- `elif`
- `else`

### 21.1 if Statement

Syntax:

```bash
if condition; then
    commands
fi
```

Example:

```bash
#!/usr/bin/env bash

number=10

if [ "$number" -gt 5 ]; then
    echo "Number is greater than 5"
fi
```

### 21.2 if-else Statement

```bash
#!/usr/bin/env bash

number=3

if [ "$number" -gt 5 ]; then
    echo "Number is greater than 5"
else
    echo "Number is not greater than 5"
fi
```

### 21.3 if-elif-else Statement

```bash
#!/usr/bin/env bash

number=10

if [ "$number" -gt 10 ]; then
    echo "Greater than 10"
elif [ "$number" -eq 10 ]; then
    echo "Equal to 10"
else
    echo "Less than 10"
fi
```

---

## 22. case Statement

The `case` statement selects an action based on a matching pattern.

Syntax:

```bash
case "$variable" in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    *)
        default_commands
        ;;
esac
```

Example:

```bash
#!/usr/bin/env bash

read -p "Enter an option (start/stop/status): " choice

case "$choice" in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
    status)
        echo "Checking service status"
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

`;;` ends a case branch.

`*)` is the default pattern.

`esac` closes the case statement.

---

## 23. for Loops

A `for` loop repeats a block of commands for each item in a list.

Syntax:

```bash
for variable in list; do
    commands
done
```

Example:

```bash
#!/usr/bin/env bash

for name in Linux Python Bash; do
    echo "$name"
done
```

Output:

```text
Linux
Python
Bash
```

### 23.1 Numeric Loop

```bash
for number in {1..5}; do
    echo "$number"
done
```

### 23.2 C-Style Loop

```bash
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```

### 23.3 Loop Through Files Safely

```bash
for file in *.log; do
    [ -e "$file" ] || continue
    echo "$file"
done
```

This checks whether matching files exist before processing them.

---

## 24. while Loops

A `while` loop executes commands repeatedly while a condition remains true.

Syntax:

```bash
while condition; do
    commands
done
```

Example:

```bash
#!/usr/bin/env bash

number=1

while [ "$number" -le 5 ]; do
    echo "$number"
    ((number++))
done
```

Output:

```text
1
2
3
4
5
```

### 24.1 Read a File Line by Line

```bash
while IFS= read -r line; do
    echo "$line"
done < input.txt
```

Important:

- `IFS=` prevents trimming leading and trailing whitespace.
- `-r` prevents backslashes from being interpreted as escapes.
- This is a useful pattern for reading text files safely.

---

## 25. Functions

A function is a reusable block of commands.

Functions help organize scripts and avoid repeating code.

Syntax:

```bash
function_name() {
    commands
}
```

Example:

```bash
#!/usr/bin/env bash

greet() {
    echo "Welcome to Bash scripting"
}

greet
```

### 25.1 Functions With Arguments

```bash
#!/usr/bin/env bash

greet() {
    echo "Hello, $1"
}

greet "Pulok"
greet "Linux"
```

Inside the function:

- `$1` = First function argument.
- `$2` = Second function argument.
- `$@` = All function arguments.

### 25.2 Returning an Exit Status

A Bash function can return an integer status.

Example:

```bash
check_directory() {
    if [ -d "$1" ]; then
        return 0
    else
        return 1
    fi
}

if check_directory "$HOME"; then
    echo "Directory exists"
else
    echo "Directory does not exist"
fi
```

Use `return` for status values, not for returning arbitrary text. To produce text, use standard output.

---

# PART 5: TESTS AND COMPARISONS

## 26. Tests Using [ ] and [[ ]]

Bash uses conditional expressions to check values and conditions.

Two common forms:

```bash
[ condition ]
```

And:

```bash
[[ condition ]]
```

`[[ ]]` is a Bash keyword that offers additional features and safer pattern matching.

### 26.1 Numeric Comparisons

| Operator | Meaning |
|---|---|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-lt` | Less than |
| `-le` | Less than or equal |

Example:

```bash
a=10
b=5

if [ "$a" -gt "$b" ]; then
    echo "a is greater than b"
fi
```

### 26.2 String Comparisons

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `!=` | Not equal |
| `-z` | String is empty |
| `-n` | String is not empty |

Example:

```bash
name="Linux"

if [[ "$name" == "Linux" ]]; then
    echo "Match found"
fi
```

Check whether a string is empty:

```bash
if [[ -z "$name" ]]; then
    echo "Name is empty"
fi
```

### 26.3 File and Directory Checks

| Operator | Meaning |
|---|---|
| `-e` | Path exists |
| `-f` | Regular file exists |
| `-d` | Directory exists |
| `-r` | File is readable |
| `-w` | File is writable |
| `-x` | File is executable |
| `-s` | File exists and is not empty |
| `-L` | Path is a symbolic link |

Example:

```bash
file="report.txt"

if [ -f "$file" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
```

Directory check:

```bash
if [ -d "$HOME" ]; then
    echo "Home directory exists"
fi
```

---

## 27. Arrays

An array stores multiple values under one variable name.

Bash supports indexed arrays and associative arrays.

### 27.1 Indexed Arrays

Create an array:

```bash
tools=("nmap" "wireshark" "burpsuite")
```

Access an element:

```bash
echo "${tools[0]}"
```

Output:

```text
nmap
```

Remember: Bash arrays use zero-based indexing.

Display all elements:

```bash
echo "${tools[@]}"
```

Display array length:

```bash
echo "${#tools[@]}"
```

Loop through the array:

```bash
for tool in "${tools[@]}"; do
    echo "$tool"
done
```

Add an element:

```bash
tools+=("curl")
```

### 27.2 Associative Arrays

Associative arrays store key-value pairs.

Declare:

```bash
declare -A student

student[name]="Pulok"
student[field]="Computer Science"
```

Access values:

```bash
echo "${student[name]}"
echo "${student[field]}"
```

Associative arrays require Bash 4 or newer.

---

## 28. getopts for Script Arguments

`getopts` processes command-line options in Bash scripts.

It is useful when building command-line tools.

Example:

```bash
#!/usr/bin/env bash

while getopts ":u:p:" opt; do
    case "$opt" in
        u)
            username="$OPTARG"
            ;;
        p)
            port="$OPTARG"
            ;;
        :)
            echo "Option -$OPTARG requires an argument"
            exit 1
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
    esac
done

echo "Username: ${username:-Not provided}"
echo "Port: ${port:-Not provided}"
```

Run:

```bash
bash script.sh -u student -p 8080
```

Important:

- `-u` accepts an argument.
- `-p` accepts an argument.
- `OPTARG` stores the option's argument.
- `OPTIND` tracks the next argument position.

---

# PART 6: ERROR HANDLING AND SAFE SCRIPTING

## 29. Exit Codes and exit

The `exit` command terminates the script and returns an exit status.

Example:

```bash
#!/usr/bin/env bash

echo "Task completed"
exit 0
```

Use a non-zero status for failure:

```bash
#!/usr/bin/env bash

echo "An error occurred" >&2
exit 1
```

Common convention:

- `0`: Success.
- `1`: General error.
- Other non-zero values: Different failure conditions.

### 29.1 set -e

```bash
set -e
```

This makes Bash exit when certain commands fail.

However, `set -e` has exceptions and context-dependent behaviour. It is not a complete error-handling solution.

### 29.2 set -u

```bash
set -u
```

This causes Bash to treat references to unset variables as errors in many contexts.

### 29.3 set -o pipefail

```bash
set -o pipefail
```

Normally, a pipeline's status is based on its last command.

With `pipefail`, a pipeline reports failure if a command in the pipeline fails, subject to Bash's pipeline status rules.

A commonly used starting configuration is:

```bash
set -euo pipefail
```

Understand the implications before using it in every script.

### 29.4 Check Errors Explicitly

Example:

```bash
if ! mkdir -p "$HOME/test"; then
    echo "Could not create directory" >&2
    exit 1
fi
```

Explicit checks are especially useful for scripts that perform important operations.

---

## 30. Logging and Timestamps

Logging means recording information about what a script does.

Logs help you:

- Troubleshoot problems.
- Track script execution.
- Identify failures.
- Review completed operations.

### 30.1 Display a Timestamp

```bash
date
```

Formatted timestamp:

```bash
date +"%Y-%m-%d %H:%M:%S"
```

### 30.2 Create a Log File

```bash
echo "Script started at $(date)" >> script.log
```

### 30.3 Logging Function

```bash
#!/usr/bin/env bash

LOG_FILE="script.log"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log_message "Script started"
log_message "Checking system"
log_message "Script completed"
```

This displays messages and appends them to the log file.

For scripts that handle untrusted input, be careful not to log passwords, tokens, or other secrets.

---

## 31. trap for Cleanup

The `trap` command allows a script to execute commands when it receives a signal or reaches a particular exit condition.

It is useful for cleaning temporary files.

Example:

```bash
#!/usr/bin/env bash

TEMP_FILE=$(mktemp)

cleanup() {
    rm -f -- "$TEMP_FILE"
}

trap cleanup EXIT

echo "Temporary data" > "$TEMP_FILE"

cat "$TEMP_FILE"
```

When the script exits, the cleanup function runs.

### Common Signals

| Signal | Meaning |
|---|---|
| EXIT | Shell exits |
| INT | Interrupt, commonly Ctrl + C |
| TERM | Termination request |
| HUP | Hangup |

Example:

```bash
trap 'echo "Script interrupted"' INT TERM
```

Important:

Cleanup code should be carefully written so that it only removes files created by the script.

---

## 32. Basic Input Validation

Input validation checks whether user-provided values are acceptable before processing them.

Example:

```bash
#!/usr/bin/env bash

read -p "Enter your name: " name

if [[ -z "$name" ]]; then
    echo "Name cannot be empty" >&2
    exit 1
fi

echo "Welcome, $name"
```

### Validate a Number

```bash
#!/usr/bin/env bash

read -p "Enter a number: " number

if [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Valid positive integer"
else
    echo "Invalid input" >&2
    exit 1
fi
```

### Validate a Directory

```bash
#!/usr/bin/env bash

read -p "Enter directory path: " directory

if [[ -d "$directory" ]]; then
    echo "Directory exists"
else
    echo "Directory not found"
fi
```

Validation is important because scripts should not blindly trust user input.

---

## 33. Safe Handling of Filenames and Untrusted Input

When writing Bash scripts, incorrect handling of filenames can cause unexpected behaviour.

### 33.1 Quote Variables

Unsafe:

```bash
rm $filename
```

Safer:

```bash
rm -- "$filename"
```

Quoting prevents word splitting and pathname expansion.

The `--` tells many commands that subsequent arguments should not be treated as options.

### 33.2 Avoid eval

Avoid using `eval` with untrusted input.

Example of dangerous design:

```bash
eval "$user_input"
```

This can execute arbitrary shell commands supplied by the user.

### 33.3 Use Arrays for Command Arguments

Avoid constructing a command as a single string and executing it.

Risky approach:

```bash
command="ls -l $directory"
$command
```

Safer approach:

```bash
args=(-l -- "$directory")
ls "${args[@]}"
```

Arrays preserve argument boundaries.

### 33.4 Use Safe Temporary Files

Use:

```bash
temp_file=$(mktemp)
```

Instead of predictable temporary filenames such as:

```text
/tmp/my_temp_file
```

Predictable filenames can create security problems involving symbolic links and race conditions.

### 33.5 Handle Filenames Safely With find

Example:

```bash
find . -type f -print0
```

Process the results safely:

```bash
while IFS= read -r -d '' file; do
    printf 'Found: %s\n' "$file"
done < <(find . -type f -print0)
```

This supports filenames containing spaces and many other special characters.

---

# PART 7: SCHEDULING AND AUTOMATION

## 34. What Is Task Scheduling?

Task scheduling means configuring commands or scripts to execute automatically at a particular time or interval.

Linux provides tools such as:

- cron
- crontab
- at

They are useful for repetitive maintenance and automation.

---

## 35. cron

Cron is a time-based job scheduler used to execute commands automatically.

A cron job can run:

- Every minute.
- Every hour.
- Every day.
- On selected weekdays.
- On particular dates.

Check whether the cron service is available:

```bash
systemctl status cron
```

### 35.1 Cron Syntax

A cron entry generally contains five time fields followed by a command.

```text
* * * * * command
```

The five fields are:

```text
minute hour day-of-month month day-of-week
```

| Field | Allowed values |
|---|---|
| Minute | 0–59 |
| Hour | 0–23 |
| Day of month | 1–31 |
| Month | 1–12 |
| Day of week | 0–7 (Sunday is commonly 0 or 7) |

### 35.2 Examples

Run every minute:

```text
* * * * * command
```

Run every hour:

```text
0 * * * * command
```

Run every day at midnight:

```text
0 0 * * * command
```

Run every day at 9 AM:

```text
0 9 * * * command
```

Run every Sunday at 10 AM:

```text
0 10 * * 0 command
```

Run every five minutes:

```text
*/5 * * * * command
```

### 35.3 Special Cron Strings

| Expression | Meaning |
|---|---|
| `@reboot` | Run at startup |
| `@hourly` | Run hourly |
| `@daily` | Run daily |
| `@weekly` | Run weekly |
| `@monthly` | Run monthly |
| `@yearly` | Run yearly |

---

## 36. crontab

`crontab` manages a user's scheduled cron jobs.

Display current user's cron jobs:

```bash
crontab -l
```

Edit cron jobs:

```bash
crontab -e
```

Remove the current user's cron jobs:

```bash
crontab -r
```

Be careful: `crontab -r` removes the entire current user's crontab.

### Example: Schedule a Backup Script

Suppose your backup script is:

```text
/home/student/scripts/backup.sh
```

Schedule it to run every day at 8 PM:

```text
0 20 * * * /home/student/scripts/backup.sh
```

Use absolute paths in cron jobs because cron may run with a limited environment and a different working directory.

---

## 37. at Command

The `at` command schedules a command to execute once at a specified time.

It may not be installed or enabled by default.

Install it if needed:

```bash
sudo apt install at
```

Check the service:

```bash
systemctl status atd
```

Schedule a command:

```bash
echo "date >> $HOME/time.log" | at 18:00
```

List scheduled jobs:

```bash
atq
```

Remove a scheduled job:

```bash
atrm job_number
```

Unlike cron, `at` is designed primarily for one-time scheduled execution.

---

# PART 8: PRACTICAL PROJECTS

## PROJECT 1 — Disk and Memory Usage Reporter

### Objective

Create a script that reports disk and memory usage.

Create a file:

```bash
nano system_report.sh
```

Script:

```bash
#!/usr/bin/env bash

set -u

echo "================================"
echo "       SYSTEM RESOURCE REPORT"
echo "================================"

echo
echo "Date and Time:"
date

echo
echo "Disk Usage:"
df -h

echo
echo "Memory Usage:"
free -h

echo
echo "System Uptime:"
uptime

echo
echo "Report completed."
```

Make executable:

```bash
chmod +x system_report.sh
```

Run:

```bash
./system_report.sh
```

### Tasks

1. Display the current date.
2. Display disk usage.
3. Display memory usage.
4. Display system uptime.
5. Save the report to a file.

Hint:

```bash
./system_report.sh > system_report.txt
```

---

## PROJECT 2 — Log File Analyzer

### Objective

Create a script that summarizes selected log entries.

Create:

```bash
nano log_analyzer.sh
```

Script:

```bash
#!/usr/bin/env bash

set -u

LOG_FILE="${1:-}"

if [[ -z "$LOG_FILE" ]]; then
    echo "Usage: $0 <log_file>" >&2
    exit 1
fi

if [[ ! -f "$LOG_FILE" || ! -r "$LOG_FILE" ]]; then
    echo "Error: File does not exist or is not readable." >&2
    exit 1
fi

echo "================================"
echo "          LOG ANALYZER"
echo "================================"

echo
echo "Log file: $LOG_FILE"

echo
echo "Total lines:"
wc -l < "$LOG_FILE"

echo
echo "Lines containing errors:"
grep -ic "error" "$LOG_FILE" || true

echo
echo "Lines containing warnings:"
grep -ic "warning" "$LOG_FILE" || true

echo
echo "Recent error entries:"
grep -in "error" "$LOG_FILE" | tail -n 10 || true
```

Run:

```bash
chmod +x log_analyzer.sh
./log_analyzer.sh /var/log/syslog
```

If `/var/log/syslog` is unavailable or unreadable, use an accessible test log file.

### Tasks

1. Accept a log file as an argument.
2. Count the total number of lines.
3. Count error entries.
4. Count warning entries.
5. Display the latest error entries.
6. Add timestamps to the report.

Security note:

Log files may contain sensitive information. Do not publish or share them without reviewing their contents.

---

## PROJECT 3 — Local Service Status Checker

### Objective

Create a script that checks whether a local systemd service is running.

Create:

```bash
nano service_checker.sh
```

Script:

```bash
#!/usr/bin/env bash

set -u

SERVICE="${1:-}"

if [[ -z "$SERVICE" ]]; then
    echo "Usage: $0 <service_name>" >&2
    exit 1
fi

if ! command -v systemctl >/dev/null 2>&1; then
    echo "Error: systemctl is unavailable." >&2
    exit 1
fi

if systemctl is-active --quiet "$SERVICE"; then
    echo "Service $SERVICE is active."
else
    echo "Service $SERVICE is not active."
fi

echo
systemctl status "$SERVICE" --no-pager
```

Run:

```bash
chmod +x service_checker.sh
./service_checker.sh ssh
```

Try another service:

```bash
./service_checker.sh cron
```

Important:

This script checks systemd service state. It does not prove that a network service is reachable or functioning correctly.

---

## PROJECT 4 — Project Directory Backup Script

### Objective

Create a backup of a project directory.

Create:

```bash
nano backup.sh
```

Script:

```bash
#!/usr/bin/env bash

set -euo pipefail

SOURCE="${1:-}"
BACKUP_DIR="${2:-$HOME/backups}"

if [[ -z "$SOURCE" ]]; then
    echo "Usage: $0 <source_directory> [backup_directory]" >&2
    exit 1
fi

if [[ ! -d "$SOURCE" ]]; then
    echo "Error: Source directory does not exist." >&2
    exit 1
fi

mkdir -p -- "$BACKUP_DIR"

SOURCE_NAME=$(basename -- "$SOURCE")
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

BACKUP_FILE="$BACKUP_DIR/${SOURCE_NAME}_${TIMESTAMP}.tar.gz"

tar -czf "$BACKUP_FILE" -C "$(dirname -- "$SOURCE")" -- "$SOURCE_NAME"

echo "Backup created successfully:"
echo "$BACKUP_FILE"
```

Run:

```bash
chmod +x backup.sh
./backup.sh "$HOME/myproject"
```

Specify a different backup location:

```bash
./backup.sh "$HOME/myproject" "$HOME/mybackups"
```

Verify the backup:

```bash
tar -tzf "$HOME/backups/myproject_YYYYMMDD_HHMMSS.tar.gz"
```

Replace the example filename with the actual backup filename.

### Tasks

1. Accept the source directory as an argument.
2. Create a backup directory if necessary.
3. Generate a timestamped backup filename.
4. Compress the project directory.
5. Verify the backup archive.
6. Handle invalid input.

---

## PROJECT 5 — Command-Line System Information Tool

### Objective

Build a command-line utility that accepts arguments and generates a report.

Create:

```bash
nano sysinfo.sh
```

Script:

```bash
#!/usr/bin/env bash

set -u

OUTPUT=""

usage() {
    echo "Usage: $0 [-o output_file]"
}

while getopts ":o:h" opt; do
    case "$opt" in
        o)
            OUTPUT="$OPTARG"
            ;;
        h)
            usage
            exit 0
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            usage
            exit 1
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            exit 1
            ;;
    esac
done

generate_report() {
    echo "================================"
    echo "        SYSTEM INFORMATION"
    echo "================================"

    echo
    echo "Hostname:"
    hostname

    echo
    echo "Current User:"
    whoami

    echo
    echo "Kernel:"
    uname -r

    echo
    echo "Date:"
    date

    echo
    echo "Uptime:"
    uptime

    echo
    echo "Disk Usage:"
    df -h

    echo
    echo "Memory:"
    free -h
}

if [[ -n "$OUTPUT" ]]; then
    if generate_report > "$OUTPUT"; then
        echo "Report saved to: $OUTPUT"
    else
        echo "Could not save report." >&2
        exit 1
    fi
else
    generate_report
fi
```

Run:

```bash
chmod +x sysinfo.sh
```

Display the report:

```bash
./sysinfo.sh
```

Save the report:

```bash
./sysinfo.sh -o system_report.txt
```

Display help:

```bash
./sysinfo.sh -h
```

### Tasks

1. Accept an output filename.
2. Display system information.
3. Save the report when `-o` is supplied.
4. Display help using `-h`.
5. Handle invalid options.
6. Add a timestamp to the report.

---

# PART 9: IMPORTANT COMMAND REVISION

## Shell Fundamentals

| Command / Symbol | Purpose |
|---|---|
| `bash` | Start Bash |
| `history` | Display command history |
| `printenv` | Display environment variables |
| `export` | Export environment variables |
| `alias` | Create command shortcuts |
| `unalias` | Remove aliases |
| `$(command)` | Command substitution |
| `$?` | Last command's exit status |
| `$$` | Current shell PID |
| `"$@"` | All positional arguments |

## Input and Output

| Symbol / Command | Purpose |
|---|---|
| `>` | Redirect standard output |
| `>>` | Append standard output |
| `<` | Redirect standard input |
| `2>` | Redirect standard error |
| `2>&1` | Redirect stderr to stdout's current destination |
| `|` | Pipe output to another command |
| `&&` | Execute next command on success |
| `||` | Execute next command on failure |
| `;` | Separate sequential commands |
| `xargs` | Convert input into command arguments |
| `tee` | Display and save output |

## Bash Scripting

| Keyword / Command | Purpose |
|---|---|
| `if` | Conditional execution |
| `elif` | Additional condition |
| `else` | Alternative branch |
| `case` | Pattern-based selection |
| `for` | Iterate over items |
| `while` | Repeat while a condition is true |
| `read` | Accept input |
| `function` / `()` | Define a function |
| `return` | Return function status |
| `exit` | Terminate a script |
| `getopts` | Parse command-line options |
| `trap` | Handle signals and cleanup |
| `set -euo pipefail` | Enable commonly used strict-mode behaviours |

## Scheduling

| Command | Purpose |
|---|---|
| `cron` | Time-based scheduler |
| `crontab -e` | Edit scheduled jobs |
| `crontab -l` | List scheduled jobs |
| `at` | Schedule a one-time task |
| `atq` | List pending at jobs |
| `atrm` | Remove a scheduled at job |

---

# PART 10: KNOWLEDGE CHECK

Before moving to Phase 7, make sure you can answer these questions:

1. What is a shell?
2. What is Bash?
3. What is the difference between Bash and Zsh?
4. What is a shell prompt?
5. What is command history?
6. What is the difference between a command, option, and argument?
7. What is the difference between single and double quotes?
8. What is escaping in Bash?
9. What are environment variables?
10. What is the purpose of PATH?
11. What does export do?
12. What is an alias?
13. What is command substitution?
14. What does `$?` represent?
15. What are stdin, stdout, and stderr?
16. What is the difference between `>` and `>>`?
17. What does `2>&1` do?
18. What is a pipe?
19. What is the difference between `&&` and `||`?
20. What is the purpose of xargs?
21. What is the purpose of tee?
22. What is Bash scripting?
23. What is a shebang?
24. What are positional parameters?
25. What is the difference between `$@` and `$#`?
26. What is the purpose of read?
27. What is the difference between if and case?
28. What is the difference between for and while loops?
29. What are Bash functions?
30. What is the purpose of `getopts`?
31. What are file tests such as `-f` and `-d`?
32. What is the purpose of `set -euo pipefail`?
33. What is the purpose of trap?
34. Why should variables be quoted?
35. Why should untrusted input never be passed directly to eval?
36. What is cron?
37. What is the difference between cron and at?
38. How can you create an automated backup script?

---

# PART 11: PHASE 6 COMPLETION CHECKLIST

- [ ] Understand what a shell is.
- [ ] Understand Bash and other shells.
- [ ] Use shell prompts and command history.
- [ ] Understand command options and arguments.
- [ ] Use single and double quotes correctly.
- [ ] Understand escaping special characters.
- [ ] Work with environment variables.
- [ ] Understand PATH, HOME, and USER.
- [ ] Use export and alias.
- [ ] Use command substitution.
- [ ] Understand exit statuses.
- [ ] Understand stdin, stdout, and stderr.
- [ ] Perform input and output redirection.
- [ ] Use pipes and logical operators.
- [ ] Understand xargs and tee.
- [ ] Create and execute Bash scripts.
- [ ] Understand shebangs.
- [ ] Work with variables and positional parameters.
- [ ] Accept input using read.
- [ ] Use if, elif, else, and case.
- [ ] Use for and while loops.
- [ ] Create and use functions.
- [ ] Understand exit codes.
- [ ] Use `[ ]` and `[[ ]]`.
- [ ] Perform file and directory checks.
- [ ] Work with strings and arrays.
- [ ] Parse arguments using getopts.
- [ ] Implement basic error handling.
- [ ] Create logs and timestamps.
- [ ] Use trap for cleanup.
- [ ] Validate user input.
- [ ] Handle filenames safely.
- [ ] Understand cron, crontab, and at.
- [ ] Create a backup script.
- [ ] Build a command-line reporting tool.

# WHY THIS PHASE MATTERS IN CYBERSECURITY

Bash scripting is useful in several cybersecurity activities:

1. **Security Automation:** Automating repetitive security checks and administrative tasks.
2. **Log Analysis:** Searching and summarizing authentication and system logs.
3. **System Enumeration:** Collecting information about users, services, processes, and system configurations.
4. **Backup Automation:** Creating backups of projects and important files.
5. **Incident Response:** Collecting system information and generating investigation reports.
6. **Penetration Testing Support:** Automating authorized reconnaissance and processing scan results.
7. **Tool Development:** Building your own command-line utilities for security workflows.

**Your goal:** Move beyond memorizing Bash commands. Learn to combine commands, write reliable scripts, handle errors, validate input, and automate practical Linux tasks.
