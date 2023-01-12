import re


def file_listing(filename="src/listing.txt"):
    lst = []
    
    counter = 0
    file_toopen = open(filename, "r")
    content = file_toopen.read()
    colist = content.split("\n")
    for i in colist:
        if i:
                counter += 1


    with open(filename, "r") as f:
        for i in range(counter):
            line = f.readline()
            line_lst = line.split()
            size = int(line_lst[4])
            month = line_lst[5]
            day = int(line_lst[6])
            time = line_lst[7]
            hour = int(time.split(":")[0])
            minute = int(time.split(":")[1])
            name = line_lst[8]
            to_add = (size, month, day, hour, minute, name)      
            lst.append(to_add)
    return lst   

def main():

    result = file_listing("src/listing.txt")
    print(result)
 

    
if __name__ == "__main__":
    main()
