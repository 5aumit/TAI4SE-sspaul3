#!/usr/bin/python3

'''
    generator.py
    This program inputs a strings, and outputs the corresponding hex
    Creator:   Ethan Knight
    Email:     ethantknight@gmail.com
    Published: 20181116
'''

import sys
import time
import binascii

def main():
    print("\n", sys.version_info)
    try:
        while True:
            print("\n\nPress Ctrl+C to exit.")
            usr=test()
            out=binascii.hexlify(bytes(usr, encoding="utf8"))
            print("\nHex:\t\t", out)
            print("Base 10:\t", int(out,16))
            time.sleep(.5)
    except KeyboardInterrupt:
        print("\tProgram Terminated\n\n")
        sys.exit(0)

def test():
    while True:
        usr=input("Enter the string to convert\n\n\t")
        if usr!="":
            return usr
        else:
            print("\nNo string entered.")

if __name__=="__main__":
    main()
