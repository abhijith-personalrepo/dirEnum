README


**Introduction**

This script is designed to print the directory tree of a specified folder path. It uses the os module to traverse the folder structure and print out all the files and folders in a tree-like structure.

Prerequisites
This script requires Python 3.x to be installed on the system.

**Usage**

To use this script, you can execute it from the command line with the following command:

**

python dirEnum.py -p /path/to/folder

**
Alternatively, you can run the script without the -p option and enter the folder path when prompted.

If the specified folder path is valid, the script will print out the directory tree. Otherwise, it will display an error message.

**Options**

The script accepts the following command line options:

-p, --path: The path to the destination folder from the root directory. This option is optional, and if not specified, the script will prompt the user to enter the folder path.

**Functionality**

The script first checks if the specified path is a file or a directory. If it is a file, the script prints its name and exits. If it is a directory, the script uses the os module to get the list of files and directories in the folder.

The script then iterates over each file and directory, recursively calling itself for any directories it encounters. It indents the output for each level of the directory tree.

The script also includes error handling for cases where the specified path is not found, is not a directory, or the user does not have permission to access it. If any such error occurs, the script will print an error message and exit.

**Conclusion**

This script provides a simple way to print out the directory tree of a specified folder path in a tree-like structure. With its error handling and command line options, it is a useful tool for navigating large and complex file systems.
