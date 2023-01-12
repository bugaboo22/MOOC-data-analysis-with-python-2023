# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    
    print(triangle.hypothenuse(10,5))
    print(triangle.area(5,2))
if __name__ == "__main__":
    main()
