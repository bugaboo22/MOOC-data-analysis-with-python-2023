

def positive_list(L):

    result = filter(lambda x: x > 0, L)
    return list(result)

def main():

    print(positive_list([2,-2,0,1,-7]))

if __name__ == "__main__":
    main()
