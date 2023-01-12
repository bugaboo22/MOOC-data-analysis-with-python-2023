

def merge(L1, L2):
    
    L = L1 + L2
    NL=[]
    for _ in range(len(L)):
        NL.append(min(L))
        L.remove(min(L))
        
    return NL
 
def main():
    L1 = [1,5,9,12]
    L2 = [7,2,6,10]
    print(merge(L1,L2))
 
if __name__ == "__main__":
    main()
 
