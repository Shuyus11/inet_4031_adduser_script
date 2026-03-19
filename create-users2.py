#!/usr/bin/python3

# This script reads user data from standard input (create-users.input)
# Each valid line contains user info separated by colons
# The script can run in dry-run mode or normal mode

# INET4031
# Shuayb Yusuf
# Date Created: 03/19/2026
# Date Last Modified: 03/19/2026

# os: executes system commands (adduser, passwd)
# re: checks for comment lines starting with '#'
# sys: reads input from standard input (stdin)
import os
import re
import sys


def main():
    # Ask the user whether to run in dry-run mode
    # /dev/tty is used so the prompt still works when input is redirected
    with open("/dev/tty") as tty:
        print("Run in dry-run mode? (Y/N): ", end='', flush=True)
        choice = tty.readline().strip().upper()

    # True = dry-run mode, False = normal execution
    dry_run = (choice == "Y")

    # Read each line from standard input (data is passed using < create-users.input)
    for line in sys.stdin:

        # Check if line starts with '#' (comment line)
        match = re.match("^#", line)

        # Remove whitespace and split by colon
        fields = line.strip().split(':')

        # Skip comments or malformed lines
        # In dry-run mode, print why the line was skipped
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("Skipping comment line:", line.strip())
                else:
                    print("Error: invalid line ->", line.strip())
            continue

        # Extract values from fields
        username = fields[0]
        password = fields[1]

        # Format full name (GECOS field in /etc/passwd)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group list by commas
        groups = fields[4].split(',')

        # Show user creation step
        print("==> Creating account for %s..." % username)

        # Build command to create user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # In dry-run mode, print the command instead of executing it
        if dry_run:
            print("DRY RUN:", cmd)
        else:
            print(cmd)
            os.system(cmd)

        # Show password setting step
        print("==> Setting the password for %s..." % username)

        # Build command to set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # In dry-run mode, print the command instead of executing it
        if dry_run:
            print("DRY RUN:", cmd)
        else:
            print(cmd)
            os.system(cmd)

        # Assign user to groups
        for group in groups:
            # Skip placeholder '-' which means no group assignment
            if group == '-':
                continue

            print("==> Assigning %s to the %s group..." % (username, group))

            # Build command to add user to group
            cmd = "/usr/sbin/adduser %s %s" % (username, group)

            # In dry-run mode, print the command instead of executing it
            if dry_run:
                print("DRY RUN:", cmd)
            else:
                print(cmd)
                os.system(cmd)


if __name__ == '__main__':
    main()
