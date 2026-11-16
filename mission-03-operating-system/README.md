# Mission 3 - Operating system, processes and permissions

## 1. Task / objective
Explore operating system environment details, active user accounts, available storage, running system processes (PIDs), file paths, permission bits (`rwx`), and core OS responsibilities[cite: 7, 8].

## 2. Work completed
* Completed **Task 3.1**: Inspected OS environment, user account identity, storage capacity, and system activity snapshots (redacting sensitive personal details)[cite: 7, 8].
* Completed **Task 3.2**: Examined active application processes and Process Identifiers (PIDs)[cite: 7, 8].
* Completed **Task 3.3**: Analyzed absolute vs. relative pathing within the repository and reviewed file permission flags (`rwx`) for owners[cite: 8].
* Completed **Task 3.4**: Completed the OS responsibilities table detailing process management, memory management, device management, file management, shells, and security[cite: 8].

## 3. Commands / tools used
* **Terminal**: `uname`, `whoami`, `df -h`, `ps aux` to inspect system state and running processes[cite: 7, 8].
* **macOS Activity Monitor**: Inspected application PIDs and resource utilization[cite: 8].

## 4. My understanding
An operating system acts as the core resource manager between hardware and software. It schedules CPU time through processes identified by PIDs, secures files using explicit read, write, and execute (`rwx`) permissions, and isolates storage using structured absolute and relative paths.

## 5. Difficulties faced
Ensuring that all process snapshot outputs and system paths were properly sanitized to avoid publishing sensitive personal or device usernames[cite: 8].

## 6. How I resolved them
Manually substituted any personal machine identifiers with generic placeholders (`[redacted]`) in notes and evidence logs[cite: 8].

## 7. Evidence / files
* `mission-03-operating-system/README.md` containing OS observation tables and responsibility explanations[cite: 4, 8].

## 8. Commit details
* **Commit message:** "Document operating system and file management"[cite: 14]
* **Status:** Confirmed visible and pushed successfully to GitHub[cite: 8, 14].