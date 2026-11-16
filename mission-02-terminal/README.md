| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| Current-directory display (`pwd`) | Prints the full absolute path of the directory you are currently working in. | Outputs the full path starting from the root directory. |
| Directory listing (`ls`) | Lists all visible files and folders in your current location. | Shows a clean horizontal or vertical list of files and folder names. |
| Detailed listing (`ls -l`) | Lists files in a long format with permissions, owner, size, and modification date. | Displays detailed rows including file permissions, links, owner name, size in bytes, and timestamp. |
| Change directory (`cd`) | Navigates into a specified folder or moves up a directory (`cd ..`). | Changes the terminal prompt path to reflect the new active folder. |
| Create directory (`mkdir`) | Creates a new folder (directory) in your current location. | Successfully provisions a new empty folder visible via `ls`. |
| Create empty file (`touch`) | Creates a new, empty file of size zero. | Generates a blank file with the specified filename. |
| Copy file (`cp`) | Makes a duplicate copy of a file with a new name or location. | Duplicates the source file to the destination path. |
| Move / rename file (`mv`) | Moves a file to a new location or renames it. | Relocates or renames the target file instantly. |
| Display file contents (`cat`) | Prints the text contents of a file directly inside the terminal window. | Outputs the entire text payload of the file onto the screen. |