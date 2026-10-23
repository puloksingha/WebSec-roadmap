# Git and GitHub Command Notes

**Goal:** Learn Git and GitHub from the basics to advanced, practical workflows.  
**Recommended practice:** Run commands inside a practice repository. Never test destructive commands on important work.

---

## 1. Git and GitHub: The Difference

- **Git** is a distributed version-control system installed on your computer.
- **GitHub** is a hosting and collaboration platform for Git repositories.
- A **repository** contains the project files and Git history.
- A **commit** is a saved snapshot of changes.
- A **branch** is an independent line of development.
- A **remote** is another copy of a repository, usually hosted on GitHub.
- `origin` is the conventional name for the main remote.
- `HEAD` points to the current commit or branch.

The normal flow is:

```text
Working directory -> staging area -> local repository -> GitHub remote
```

---

## 2. Installing and Configuring Git

Check that Git is installed:

```powershell
git --version
```

Set your identity. Use the email associated with your GitHub account if you want your commits linked to GitHub:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

View configuration:

```powershell
git config --list
git config --global --list
git config user.name
git config user.email
```

Useful defaults:

```powershell
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global pull.rebase false
```

Use `core.autocrlf true` on Windows to help manage Windows and Unix line endings.

---

## 3. Creating or Downloading a Repository

Create a new local repository:

```powershell
mkdir my-project
cd my-project
git init
```

Clone an existing GitHub repository:

```powershell
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Clone into a custom folder:

```powershell
git clone https://github.com/USERNAME/REPOSITORY.git local-folder
```

Initialize the current project:

```powershell
git init
```

Check the repository root:

```powershell
git rev-parse --show-toplevel
```

---

## 4. Checking Repository State

The most important everyday command:

```powershell
git status
```

Short status:

```powershell
git status --short --branch
```

Show the current branch:

```powershell
git branch --show-current
```

List local branches:

```powershell
git branch
```

List local and remote branches:

```powershell
git branch -a
```

Show branches with their latest commits and tracking information:

```powershell
git branch -avv
```

List tracked files:

```powershell
git ls-files
```

Find ignored files:

```powershell
git status --ignored
git check-ignore -v path\to\file
```

---

## 5. Adding and Committing Changes

See unstaged changes:

```powershell
git diff
```

Stage one file:

```powershell
git add .\path\to\file.py
```

Stage a directory:

```powershell
git add .\src
```

Stage all changes in the repository:

```powershell
git add .
```

Review staged changes:

```powershell
git diff --cached
```

Unstage a file without deleting its changes:

```powershell
git restore --staged .\path\to\file.py
```

Commit staged changes:

```powershell
git commit -m "Describe the change"
```

Show the latest commit:

```powershell
git show --stat
git show
```

Show a compact history:

```powershell
git log --oneline
git log --oneline --decorate --graph --all
```

### Good commit messages

Prefer short, specific, imperative messages:

```text
Add calculator input validation
Fix division by zero handling
Document Git branching workflow
```

Avoid vague messages such as:

```text
changes
update
stuff
```

---

## 6. `.gitignore`

Create a `.gitignore` file to exclude generated files, secrets, and local environments:

```gitignore
__pycache__/
*.pyc
.venv/
.env
.env.*
node_modules/
dist/
build/
.vscode/
```

Never commit:

- Passwords
- API keys
- Access tokens
- Private keys
- Database credentials
- Personal configuration files

If a secret was already committed, adding it to `.gitignore` is not enough. Remove it from the history and rotate the secret immediately.

---

## 7. Branches

Create a branch:

```powershell
git switch -c feature/calculator
```

Switch to an existing branch:

```powershell
git switch main
```

Older equivalents:

```powershell
git checkout -b feature/calculator
git checkout main
```

Rename the current branch:

```powershell
git branch -M main
```

Delete a merged local branch:

```powershell
git branch -d feature/calculator
```

Force-delete a local branch. Use only when you are certain its work is not needed:

```powershell
git branch -D feature/calculator
```

Compare branches:

```powershell
git diff main..feature/calculator
git log --oneline main..feature/calculator
```

### Recommended feature-branch workflow

```powershell
git switch main
git pull --ff-only
git switch -c feature/my-change

# Edit files
git status
git diff
git add .
git commit -m "Implement my change"
git push -u origin feature/my-change
```

Open a pull request on GitHub, merge it, then update local `main`:

```powershell
git switch main
git pull --ff-only
git branch -d feature/my-change
```

---

## 8. Remotes and GitHub

List remotes:

```powershell
git remote -v
```

Show detailed remote information:

```powershell
git remote show origin
```

Add a remote when none exists:

```powershell
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Change an existing remote:

```powershell
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

Remove a remote:

```powershell
git remote remove origin
```

Check whether a remote is reachable:

```powershell
git ls-remote origin
```

List remote branches:

```powershell
git ls-remote --heads origin
git branch -r
```

### `add` versus `set-url`

Use `git remote add` only when `origin` does not exist:

```text
error: remote origin already exists
```

If `origin` already exists, use:

```powershell
git remote set-url origin URL
```

For the repository in this project, the corrected command was:

```powershell
git remote set-url origin https://github.com/puloksingha/WebSec-roadmap.git
git push -u origin main
```

---

## 9. Fetch, Pull, and Push

Download remote information without changing local files:

```powershell
git fetch origin
```

Fetch all remotes and remove stale remote-tracking branches:

```powershell
git fetch --all --prune
```

Pull and merge remote changes:

```powershell
git pull
```

Pull using fast-forward only. This avoids creating an unexpected merge commit:

```powershell
git pull --ff-only
```

Pull with rebase:

```powershell
git pull --rebase origin main
```

Push a branch for the first time:

```powershell
git push -u origin main
```

After upstream tracking is configured:

```powershell
git push
```

Push a feature branch:

```powershell
git push -u origin feature/my-change
```

Delete a remote branch:

```powershell
git push origin --delete feature/my-change
```

Remove stale remote-tracking references:

```powershell
git remote prune origin
```

---

## 10. Merging

Merge a feature branch into the current branch:

```powershell
git switch main
git merge feature/my-change
```

A fast-forward-only merge:

```powershell
git merge --ff-only feature/my-change
```

Abort a merge:

```powershell
git merge --abort
```

Important: this command:

```powershell
git merge test
```

merges `test` into the branch you are currently on. If you are already on `test`, Git normally reports `Already up to date`.

---

## 11. Handling Merge Conflicts

Check conflicts:

```powershell
git status
```

Conflict markers look like this:

```text
<<<<<<< HEAD
Your current branch
=======
Incoming branch
>>>>>>> feature/my-change
```

Edit the file, remove the markers, and keep the correct content. Then:

```powershell
git add .\conflicted-file
git commit
```

For a rebase conflict:

```powershell
git add .\conflicted-file
git rebase --continue
```

Abort the operation if necessary:

```powershell
git merge --abort
git rebase --abort
```

---

## 12. Undoing Changes Safely

Discard unstaged changes in one file:

```powershell
git restore .\path\to\file
```

Unstage a file:

```powershell
git restore --staged .\path\to\file
```

Create a new commit that reverses an earlier commit:

```powershell
git revert COMMIT_HASH
```

`git revert` is the safest way to undo a commit that has already been pushed.

Unstage everything:

```powershell
git reset
```

Move `HEAD` back one commit but keep changes staged:

```powershell
git reset --soft HEAD~1
```

Move `HEAD` back one commit and keep changes unstaged:

```powershell
git reset --mixed HEAD~1
```

Discard commits and working-tree changes:

```powershell
git reset --hard HEAD~1
```

`--hard` can permanently remove work. Use `git status` and `git log` before using it.

---

## 13. Stashing Work

Temporarily save uncommitted changes:

```powershell
git stash push -m "Work in progress"
```

List stashes:

```powershell
git stash list
```

Apply the latest stash and remove it:

```powershell
git stash pop
```

Apply a stash without removing it:

```powershell
git stash apply stash@{0}
```

Delete one stash:

```powershell
git stash drop stash@{0}
```

Delete all stashes:

```powershell
git stash clear
```

Do not use stashes as a permanent backup. A real commit on a private branch is usually safer.

---

## 14. Rebasing

Rebase a feature branch onto the latest `main`:

```powershell
git fetch origin
git switch feature/my-change
git rebase origin/main
```

Continue after resolving a conflict:

```powershell
git add .
git rebase --continue
```

Abort:

```powershell
git rebase --abort
```

Interactive rebase for cleaning recent commits:

```powershell
git rebase -i HEAD~3
```

Possible actions include:

- `pick` — keep a commit
- `reword` — change its message
- `edit` — stop and modify it
- `squash` — combine it with the previous commit
- `fixup` — combine it and discard its message
- `drop` — remove it

Do not rebase shared commits unless your team agrees. Rebasing changes commit identities.

---

## 15. Tags and Releases

Create an annotated tag:

```powershell
git tag -a v1.0.0 -m "First stable release"
```

List tags:

```powershell
git tag
```

Inspect a tag:

```powershell
git show v1.0.0
```

Push one tag:

```powershell
git push origin v1.0.0
```

Push all tags:

```powershell
git push origin --tags
```

Delete a local tag:

```powershell
git tag -d v1.0.0
```

Delete a remote tag:

```powershell
git push origin --delete v1.0.0
```

---

## 16. Searching and Inspecting History

Show a commit:

```powershell
git show COMMIT_HASH
```

Show files changed by a commit:

```powershell
git show --stat COMMIT_HASH
```

Search commit messages:

```powershell
git log --all --grep="calculator" --oneline
```

Show commits by one author:

```powershell
git log --author="Your Name" --oneline
```

Find the commit that introduced a string:

```powershell
git log -S "Cannot divide by zero" --oneline -- .\Variables\calculator.py
```

Find commits matching a regular expression:

```powershell
git log -G "def calculate" --oneline
```

See who changed each line:

```powershell
git blame .\Variables\calculator.py
```

Compare local work with the remote:

```powershell
git diff origin/main..HEAD
git log --oneline origin/main..HEAD
```

---

## 17. Reflog: Recovering Lost Work

View movements of `HEAD`:

```powershell
git reflog
```

Inspect a previous state:

```powershell
git show HEAD@{2}
```

Create a recovery branch:

```powershell
git switch -c recovery HEAD@{2}
```

The reflog is especially useful after an accidental reset, rebase, or branch deletion. It is local history and is not normally uploaded to GitHub.

---

## 18. GitHub Authentication

GitHub HTTPS operations generally use Git Credential Manager or a personal access token rather than an account password.

If GitHub CLI is installed:

```powershell
gh auth login
gh auth status
```

SSH remote format:

```powershell
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

Test SSH authentication:

```powershell
ssh -T git@github.com
```

Never put a token directly in a command that may be saved in shell history:

```text
https://TOKEN@github.com/USERNAME/REPOSITORY.git
```

If a token is exposed, revoke it and create a replacement immediately.

---

## 19. Common Errors and Fixes

### `remote origin already exists`

Inspect the remote:

```powershell
git remote -v
```

Replace its URL:

```powershell
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

### `Repository not found`

Check spelling, repository visibility, permissions, authentication, and the `.git` suffix:

```powershell
git remote -v
git ls-remote origin
```

Correct the URL:

```powershell
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

### `pathspec 'branch' did not match`

The branch does not exist locally. Create it:

```powershell
git switch -c branch
```

Or fetch and track a remote branch:

```powershell
git fetch origin
git switch -c branch --track origin/branch
```

### `src refspec main does not match any`

You may have no commits or may be on another branch:

```powershell
git status
git branch --show-current
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### `Updates were rejected`

The remote has commits you do not have:

```powershell
git pull --rebase origin main
git push
```

Resolve conflicts if Git reports them.

### `nothing to commit, working tree clean`

There are no uncommitted changes. Check history and branches:

```powershell
git log --oneline --decorate --all
git branch -avv
```

---

## 20. Complete First-Push Workflow

For a local project that has never been pushed:

```powershell
cd path\to\project
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git ls-remote origin
git push -u origin main
```

If `origin` already exists:

```powershell
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

---

## 21. Daily Professional Workflow

```powershell
git switch main
git pull --ff-only
git switch -c feature/short-description

# Make and test changes
git status
git diff

git add .\file-that-changed
git diff --cached
git commit -m "Describe the completed change"
git push -u origin feature/short-description
```

After the pull request is merged:

```powershell
git switch main
git pull --ff-only
git branch -d feature/short-description
git fetch --prune
```

---

## 22. Safe Command Checklist

Before committing:

```powershell
git status
git diff
git diff --cached
```

Before pushing:

```powershell
git branch --show-current
git remote -v
git log --oneline -3
```

Before a destructive command:

```powershell
git status
git log --oneline --decorate --all -10
git reflog
```

Prefer:

- `git restore` for discarding or unstaging specific files.
- `git revert` for undoing pushed commits.
- `git pull --ff-only` for a predictable update.
- Feature branches and pull requests for collaborative work.
- Small, focused commits.

Be cautious with:

- `git reset --hard`
- `git clean -fd`
- `git push --force`
- `git push --force-with-lease`
- Rebasing commits that others already use

`--force-with-lease` is safer than `--force`, but both can rewrite remote history.

---

## 23. Practice Exercises

- [ ] Initialize a practice repository.
- [ ] Create a `.gitignore`.
- [ ] Make and commit a file.
- [ ] Create a feature branch.
- [ ] Make two commits and inspect them with `git log`.
- [ ] Compare the feature branch with `main`.
- [ ] Push the branch to GitHub.
- [ ] Create and merge a pull request.
- [ ] Resolve a deliberate merge conflict.
- [ ] Stash work and restore it.
- [ ] Revert a commit.
- [ ] Create and push a version tag.
- [ ] Use `git reflog` to locate an earlier commit.

---

## 24. Quick Reference

```powershell
git status
git init
git clone URL
git add .
git commit -m "message"
git log --oneline --graph --decorate --all
git switch main
git switch -c feature/name
git merge branch
git fetch origin
git pull --ff-only
git pull --rebase
git push -u origin main
git remote -v
git remote set-url origin URL
git diff
git diff --cached
git restore file
git restore --staged file
git revert COMMIT
git stash
git reflog
git tag -a v1.0.0 -m "release"
```
