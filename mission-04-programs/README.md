### Task 4.2: Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code *before* execution, generating a standalone executable file[cite: 9]. | Translates and executes the source code line-by-line *at runtime* during execution[cite: 9]. |
| **Typical output** | An intermediate or executable machine code file (e.g., `.exe` or binary)[cite: 9]. | Direct program output or runtime behavior without generating a separate compiled file[cite: 9]. |
| **One example** | C / C++ (`gcc`)[cite: 9] | Python (`python3`)[cite: 9] or JavaScript[cite: 9]. |
| **One advantage** | Compiled programs typically execute much faster because translation is already complete before running[cite: 9]. | Easier to test code and debug interactively on the fly since errors appear immediately line-by-line[cite: 9]. |

#### Explanation of Differences
A compiler translates the entire source code of a program into machine code all at once before the program is run, which usually results in faster execution speeds[cite: 9]. In contrast, an interpreter reads, translates, and executes the code line-by-line dynamically at runtime, making it more flexible for testing and debugging[cite: 9]. Many modern languages use hybrid approaches that combine both techniques[cite: 9].


