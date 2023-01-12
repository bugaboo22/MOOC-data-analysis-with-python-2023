

import numpy as np

def get_rows(a):
    x = []
    for i in a:
        x.append(np.array(i))
        
    return x

def get_columns(a):

    x = []
    d = a.T
    for i in d:
        x.append(np.array(i))
    return x

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))
    

if __name__ == "__main__":
    main()
