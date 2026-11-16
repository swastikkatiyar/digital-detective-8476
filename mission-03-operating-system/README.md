### Task 3.1: Explore Your Operating System

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Kernel version, release, and hardware architecture | Darwin [redacted] 24.x.x arm64 |
| **Current account identity** | The username of the currently logged-in user session | [redacted] |
| **Available and used storage** | Total disk capacity, space used, and available free storage | [redacted] total disk space, [redacted] available |
| **System activity snapshot** | Active processes running with their PID and resource usage | Top system processes including terminal, window server, and background daemons |


### Task 3.2: Understand Processes

* **What is a process?**  
  A process is an instance of a computer program that is currently being executed[cite: 8].

* **What does the PID column represent?**  
  The Process Identifier (PID) column represents the unique numeric ID assigned by the operating system to each active process, allowing the system to track, manage, and communicate with it.

* **Give two examples of processes that may be running on your computer:**  
  1. A web browser application (e.g., Safari or Google Chrome).  
  2. A text editor or development tool (e.g., Visual Studio Code or Terminal).


  ### Task 3.3: Understand Paths and Permissions

* **Difference between Absolute and Relative Paths:**
  * **Absolute Path:** Specifies a file or folder's exact location starting all the way from the root directory (`/`), such as `/Users/[redacted]/digital-detective-8476/mission-03-operating-system`.
  * **Relative Path:** Specifies the location of a file or folder relative to your current working directory, such as `./mission-03-operating-system` or `../`.

* **File Permissions Table (Owner Permissions):**
  | Permission | Meaning | Example |
  | :--- | :--- | :--- |
  | **r (Read)** | Allows a file's contents to be read[cite: 9]. | Opening a text file[cite: 9]. |
  | **w (Write)** | Allows a file to be changed, modified, or deleted[cite: 9]. | Editing or saving text inside a file[cite: 9]. |
  | **x (Execute)** | Allows a file to be run; on a directory, allows access and traversal[cite: 9]. | Running a script or entering a folder[cite: 9]. |



### Task 3.4: Explain Operating-System Responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | The OS creates, schedules, manages, and terminates processes (running programs) to ensure fair CPU access. | Running multiple applications simultaneously like a browser and a text editor. |
| **Memory management** | The OS allocates and deallocates memory space for programs currently running, preventing applications from interfering with each other's data. | Assigning RAM to open tabs in Chrome and reclaiming it when closed. |
| **Device management** | The OS controls and communicates with hardware devices and peripherals using specialized drivers. | Sending a document from your computer to a connected printer or reading a USB drive. |
| **File management** | The OS organizes, creates, reads, writes, and secures files and directories within a hierarchical file system structure. | Saving a Word document into a specific folder on your hard drive. |
| **User interface / shell** | The OS provides a medium (CLI or GUI) through which users and applications can interact with the computer system. | Using the Terminal (CLI) or desktop icons and windows (GUI) to interact with files. |
| **Security and permissions** | The OS enforces access control, user authentication, and file permissions to protect system resources from unauthorized access. | Restricting a standard user account from modifying system configuration or application files. |


