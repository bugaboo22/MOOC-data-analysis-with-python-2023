
import string
def acronyms(s):

    word = s.split()
    chars = string.punctuation + string.whitespace
    uppers = []
    
    new_lst = [s.strip(chars) for s in word]

    for word in new_lst:
        if word.isupper():
            uppers.append(word)
            
    return uppers
    
def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))

if __name__ == "__main__":
    main()
