def word_frequencies(filename):
    to_add = {}
    with open(filename, "r") as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                word_strip = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word_strip in to_add:
                    to_add[word_strip] += 1
                else:
                    to_add[word_strip] = 1
    return to_add                    
                    

def main():
   for word, count in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()