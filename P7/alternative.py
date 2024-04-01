def main():
    # Input string
    read_string: str = "Hello word. This will show you why you never go full sticky caps"

    # Initialize an empty string for storing the sticky caps version of the string
    some_string: str = ""
    
    #Converting string to sticky caps
    for i in range(len(read_string)):
        if i%2 == 0:
            some_string = some_string + read_string[i].upper()
        else:
            some_string = some_string + read_string[i].lower()
            
    # Display the string in sticky caps, upper case, and lower case        
    print(f"String in sticky caps: {some_string}")
    print(f"String in  upper case: {some_string.upper()}")
    print(f"String in  lower case: {some_string.lower()}")
    
    #Converts string to a list
    some_string: list = some_string.split()

    
    # Convert the list elements to alternative title case
    for i in range(len(some_string)):
        if i%2 == 0:
            some_string[i] = some_string[i].upper()
        else:
            some_string[i] = some_string[i].lower()

    # Join the list elements back into a string and print        
    print(f"String in alternative: {' '.join(some_string)}")
    # You're quite right. It said alternative words
    
if __name__=='__main__':
    main()
