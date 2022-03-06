'''
Author: fengsc
Date: 2022-03-01 11:08:55
LastEditTime: 2022-03-01 13:38:50
'''
#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys
# Gather our code in a main() function


def main():
    print('Hello there', sys.argv[1])

# Command line args are in sys.argv[1], sys.argv[2] ...
# sys.argv[0] is the script name itself and can be ignored


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
# . A Python module can be run directly — as above "python hello.py Bob" — or it can be imported and used by some other module.
# *When a Python file is run directly, the special variable "__name__" is set to "__main__".
