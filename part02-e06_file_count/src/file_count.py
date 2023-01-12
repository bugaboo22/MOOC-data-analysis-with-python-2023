

import sys

def file_count(filename):
   
    char_count = 0
    word_count = 0
    line_count = 0

    with open(filename, 'r') as f:

        for line in f:
            words = line.split()
            word_count += len(words)
            char_count += len(line)
            line_count += 1

    return line_count, word_count, char_count

def main():
    
    for filename in sys.argv[1:]:
        tup = file_count(filename)
        print(f"{tup[0]}\t{tup[1]}\t{tup[2]}\t{filename}")

if __name__ == "__main__":
    main()
