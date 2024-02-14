
# File Organizer

The File Organizer is a Python script designed to organize files within a specified directory based on their file extensions. It prompts the user to input the path to the target directory containing the files to be organized. The script then identifies the unique file extensions present in the directory, creates subdirectories for each file extension, and moves the files into their respective subdirectories.

## Features

-  The script validates the user-provided directory path to ensure it exists and is valid.
- It organizes files within the directory into subdirectories based on their file extensions.
- Before organizing files, the script checks if the files are already sorted. If no new file extensions are detected, it informs the user that the files are already sorted in the directory.
 


## Possible Bugs

- Permission Issues: If the script encounters permission issues while attempting to read, write, or move files, it may fail to execute properly.
- File Overwrite: If files with the same name already exist in the destination subdirectories, the script may overwrite them without warning.
- Directory Structure: If the directory structure is complex or deeply nested, the script may encounter issues with creating subdirectories.
- Invalid File Extensions: If files have no extensions or non-standard extensions, they may not be organized correctly.
- User Input Handling: The script assumes valid user input; however, improper input handling may lead to unexpected behavior or errors.
- Large File Sets: Processing a large number of files may impact performance and execution time.
