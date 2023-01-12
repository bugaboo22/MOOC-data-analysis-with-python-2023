

def transform(s1, s2):
    
    a = s1.split()
    b = s2.split()
  
    a2 = list(map(int, a))
    b2 = list(map(int, b))
    Result = []
    for i1, i2 in zip(a2, b2):
        Result.append(i1*i2)
    
    return Result
def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
