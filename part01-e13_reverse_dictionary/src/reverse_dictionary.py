
def reverse_dictionary(d):
    new_dic = {}
    for k,v in d.items():
        for x in v:
            new_dic.setdefault(x,[]).append(k)
    return new_dic

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))
    
if __name__ == "__main__":
    main()
