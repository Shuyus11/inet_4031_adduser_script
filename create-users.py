#!/usr/bin/python3

# INET4031
# Shuayb Yusuf
# Date Created: 03/19/2026
# Date Last Modified: 03/19/2026

# os: used to run system commands
# re: used to detect comment lines starting with '#'
# sys: used to read input from stdin (input file)
import os
import re
import sys

def main():
    # Read each line from the input file
    for line in sys.stdin:

        # Check if line starts with '#' (comment line)
        match = re.match("^#", line)

        # Remove whitespace and split by colon
        fields = line.strip().split(':')

        # Skip comments or malformed lines (not exactly 5 fields)
        if match or len(fields) != 5:
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

        # Dry run (print instead of execute)
        print(cmd)
        # os.system(cmd)

        # Show password setting step
        print("==> Setting the password for %s..." % username)

        # Build command to set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Dry run
        print(cmd)
        # os.system(cmd)

        # Assign user to groups
        for group in groups:
            # Skip if group is '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build command to add user to group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Dry run
                print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()
