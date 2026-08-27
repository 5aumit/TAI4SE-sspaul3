#!/usr/bin/env python3
import sys
from pathlib import Path


def print_usage():
    sys.stderr.write('''
Find the length of the biggest line in the file.
Usage: ./biggestLine <delimiter> <field number - first element is 0> <file path>
            ''')


def main():
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)

    delimiter = sys.argv[1]
    field_number = int(sys.argv[2])
    file_path = sys.argv[3]

    my_file = Path(file_path)

    biggest_string = ""
    try:
        with open(my_file, 'r') as f:
            line = f.readline()
            line_num = 0
            while line:
                    line_num = line_num + 1
                    line = f.readline()
                    curr = line.split(delimiter)[field_number]
                    if len(curr) > len(biggest_string):
                        biggest_string = curr
                    print('Processing Line ' + str(line_num), end='\r')
    except IndexError:
        print('\nError on line '+str(line_num))
    except KeyboardInterrupt:
        sys.exit(0)
    except FileNotFoundError:
        sys.stderr.write('file not found')
        sys.exit(1)

    print("biggest string is " + str(len(biggest_string)) + " characters")


main()
