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