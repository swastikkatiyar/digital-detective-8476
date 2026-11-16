### Task 6.1: Understand the Basic Git Workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Displays the current state of your working directory and staging area, showing which files are untracked, modified, or staged for commit[cite: 11]. |
| **Stage selected changes** (`git add <file>`) | Moves file changes from your working directory into the staging area, marking them to be included in the next snapshot[cite: 11]. |
| **Create a commit** (`git commit -m "message"`) | Takes the staged snapshot and records it permanently into the repository's local history along with a descriptive commit message[cite: 11]. |
| **View commit history** (`git log`) | Displays a chronological list of all previous commits made in the repository, showing unique commit hashes, author details, dates, and messages[cite: 11]. |

#### Difference Between Staging and Committing
* **Staging (`git add`):** Acts as a preparation or draft area. It allows you to selectively choose *which* modified files you want to bundle together before saving them.
* **Committing (`git commit`):** Permanently saves that bundled snapshot of changes into your project's version history, creating a secure milestone checkpoint that you can track or share.


### Task 6.3: Branches, Pull Requests, and Collaboration

* **What is a Branch?**  
  A branch is a parallel, independent line of development within a Git repository. It allows you to create features, fix bugs, or experiment with changes safely without altering or disrupting the main production code (`main`)[cite: 11, 12].

* **What is a Pull Request (PR)?**  
  A Pull Request is an online feature on GitHub that proposes merging changes from one branch into another (such as from `update-about` into `main`)[cite: 11, 12]. It provides a dedicated workspace to review code diffs, discuss changes, and perform automated checks before integrating the work[cite: 11, 12].

* **Why are they useful when people work on the same project?**  
  * **Isolated Development:** Multiple team members can work on different features simultaneously without stepping on each other's toes or breaking the stable main codebase[cite: 11, 12].
  * **Code Review & Quality Control:** Pull requests allow peers or instructors to inspect code changes, spot errors, and provide feedback before changes become final[cite: 11, 12].
  * **Safe Integration:** They ensure changes are thoroughly tested and verified before being merged back into the primary project branch[cite: 11, 12].


  ### Mission 6: Git and GitHub

## 1. Task / Objective
Understand version control fundamentals, practise staging and committing changes, create branches, open and merge Pull Requests, and build a Git command glossary[cite: 11, 12].

## 2. Work Completed
* Examined and executed basic Git workflow commands (`status`, `add`, `commit`, `log`)[cite: 11].
* Created a dedicated feature branch (`update-about`) to update the root `README.md` with a learning summary[cite: 11, 12].
* Published the branch to GitHub, opened and merged a Pull Request, and pulled the latest changes back to the local `main` branch[cite: 11, 12].
* Compiled a complete glossary of essential Git operations[cite: 11, 12].

## 3. Commands / Tools Used
* **`git init`**: Initialises a new local Git repository in the current working directory[cite: 11, 12].
* **`git status`**: Displays the current status of the working tree and staging area[cite: 11].
* **`git add <file>`**: Stages selected file changes to prepare them for the next commit snapshot[cite: 11].
* **`git commit -m "msg"`**: Permanently records the staged changes into the repository history with a message[cite: 11].
* **`git log`**: Displays the chronological commit history of the repository[cite: 11].
* **`git branch`**: Lists existing local branches or creates a new branch[cite: 11, 12].
* **`git checkout <branch>` / `git switch`**: Switches your active working context to a different branch[cite: 11, 12].
* **`git push`**: Uploads local commits and branches to the remote repository (GitHub)[cite: 11, 12].
* **`git pull`**: Downloads and merges the latest updates from the remote repository to your local machine[cite: 11, 12].

## 4. Task 6.4: Git Command Glossary
| Git Operation | Explanation |
| :--- | :--- |
| **Initialise a repository** | Creates a new hidden `.git` directory to start tracking version control in a project folder[cite: 11, 12]. |
| **Check status** | Shows which files are modified, untracked, or staged in the current workspace[cite: 11]. |
| **Stage changes** | Moves file modifications into the staging area to bundle them before committing[cite: 11]. |
| **Commit changes** | Saves a permanent snapshot of the staged files into the local repository history with a descriptive message[cite: 11]. |
| **View history** | Lists past commits chronologically, including unique hashes, authors, and timestamps[cite: 11]. |
| **Create or list branches** | Displays all local development branches or sets up a new independent line of work[cite: 11, 12]. |
| **Switch branches** | Moves your active workspace between different branches in your repository[cite: 11, 12]. |
| **Publish changes** | Uploads your local commits and branches up to GitHub[cite: 11, 12]. |
| **Retrieve remote changes** | Fetches and merges updates from the remote repository down to your local computer[cite: 11, 12]. |

## 5. Key Concepts & Understanding
* **Difference Between Staging (`git add`) and Committing (`git commit`):** Staging acts as a preparation or draft area where you selectively choose which modified files to bundle, whereas committing permanently records that snapshot into your project's official history[cite: 11].
* **Purpose of a Branch and Pull Request:** Branches allow safe, parallel experimentation without breaking the stable code[cite: 11, 12], while Pull Requests provide a structured workspace to review diffs, discuss changes, and safely merge code into `main`[cite: 11, 12].

## 6. Difficulties Faced
* No major difficulties encountered while creating branches or handling remote pushes.

## 7. How I Resolved Them
* Not applicable[cite: 12].

## 8. Evidence / Files
* Root `README.md` containing the updated "My Learning" section.
* Active Git commit history and closed Pull Request on GitHub (`digital-detective-8476`)[cite: 11, 12].

## 9. Commit Details
* **Commit Message:** `"Complete Git and GitHub collaboration mission"`[cite: 15]
* **Status:** Pushed successfully to GitHub[cite: 12, 15].