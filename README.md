# inet_4031_adduser_script
## Program Description
This project includes a Python script designed to automate the creation of user accounts on a Linux system. The script reads user information from an input file and performs tasks such as creating accounts, setting passwords, and assigning users to groups.

This helps reduce manual work and ensures consistency when managing multiple users.

---

## Program Operation
The script is executed by redirecting an input file into it. Each line in the input file represents a user and contains all necessary details.

Run the script using:

./create-users.py < create-users.input

---

## Input File Format
Each line in the input file must follow this format:

username:password:last_name:first_name:group1,group2

### Example:
user04:pass04:Last04:First04:group01.
user06:pass06:Last06:First06:group01,group02.

- Lines starting with `#` are treated as comments and ignored.
- Lines that do not contain exactly 5 fields are skipped.

---

## Command Execution
The script builds and executes system commands such as:

- adduser → to create user accounts.
- passwd → to set user passwords.
- adduser user group → to assign users to groups.

These commands are executed using Python’s `os.system()` function.

---

## Dry Run
Before running the script on the system, it can be tested in "dry run" mode. In this mode, commands are printed instead of executed, allowing verification without making changes.

---

## Files Included
- create-users.py — Python script for user creation. 
- create-users.input — Input file with user data. 
- README.md — Project documentation.

---

## Summary
This script demonstrates how automation can simplify system administration by efficiently creating and managing user accounts using structured input data.
