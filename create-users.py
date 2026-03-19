#!/usr/bin/python3

# This script reads user data from standard input (create-users.input)
# Each valid line contains user info separated by colons
# The script creates users, sets passwords, and assigns groups

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
    # Loop through each line from the input file
    # (input is redirected using < create-users.input)
    for line in sys.stdin:

        # Check if the line is a comment (starts with '#')
        match = re.match("^#", line)

        # Remove extra whitespace and split line into fields using ':'
        fields = line.strip().split(':')

        # Skip comment lines or incorrectly formatted lines
        # A valid line must have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user information from fields
        username = fields[0]
        password = fields[1]

        # Format the full name for the GECOS field (used in /etc/passwd)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group list into individual groups
        groups = fields[4].split(',')

        # Display message for user creation
        print("==> Creating account for %s..." % username)

        # Build the command to create the user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Print and execute the command
        print(cmd)
        os.system(cmd)

        # Display message for password setup
        print("==> Setting the password for %s..." % username)

        # Build the command to set the user's password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Print and execute the command
        print(cmd)
        os.system(cmd)

        # Loop through each group and assign user
        for group in groups:

            # Skip placeholder '-' (means no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build command to add user to group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Print and execute the command
                print(cmd)
                os.system(cmd)


# Run the main function
if __name__ == '__main__':
    main()
