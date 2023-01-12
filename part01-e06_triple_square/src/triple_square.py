def triple(t):
    return t*3

def square(t):
    return t**2

def main():
    for i in range(10):
        i_squared = square(i+1)
        i_tripled = triple(i+1)
        if i_squared > i_tripled:
            break
        else:
            print(f"triple({i+1})=={i_tripled} square({i+1})=={i_squared}")

if __name__ == "__main__":
    main()