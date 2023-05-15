import sys
import re

def count_rows_with_strings(filename, search_string1, search_string2):
    count = 0
    pattern1 = re.compile(re.escape(search_string1).replace('\\*', '.*'))
    pattern2 = re.compile(re.escape(search_string2).replace('\\*', '.*'))
    with open(filename, 'r') as file:
        for line in file:
            if re.search(pattern1, line) and re.search(pattern2, line):
                count += 1
    return count

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python search_file.py <filename> <search_string1> <search_string2>")
        sys.exit(1)

    filename = sys.argv[1]
    search_string1 = sys.argv[2]
    search_string2 = sys.argv[3]

    row_count = count_rows_with_strings(filename, search_string1, search_string2)
    print(f"Number of rows containing '{search_string1}' and '{search_string2}': {row_count}")

