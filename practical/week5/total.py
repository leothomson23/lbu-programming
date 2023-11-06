import sys 

count = len(sys.argv)

if len(sys.argv) == 1:
    print("No arguments provided.")    
else:
    total = 0 
    while count > 1: 
        count -= 1 
        total += float(sys.argv[count]) 
    print("Total is", total)
    print("The average is", (total/len(sys.argv)))