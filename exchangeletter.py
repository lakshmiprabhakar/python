def swap(string):
     
    # storing the first character
    start = string[0]
     
    # storing the last character
    end = string[-1]
     
    swapped_string = end + string[1:-1] + start
    print(swapped_string)
    
     

a=input("Enter the string ")
swap(a)
