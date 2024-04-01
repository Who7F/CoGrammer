def main():
    # Input file 
    INPUT_FILE = "DOB.txt"

    # Open the input file and read its contents
    with open(INPUT_FILE, 'r') as f:
        my_file = f.read()
        
    # Print out names
    print("\nName:-")
    for line in list(my_file.splitlines()):
        # Extract and print the first two elements (first name and last name)
        print(' '.join(list(line.split())[:2]))
        
    # Print out birthdays
    print("\nBirthday:-")
    for line in list(my_file.splitlines()):
        # Extract and print the last three elements (day, month, and year)
        print(' '.join(list(line.split())[-3:]))


if __name__=='__main__':
    main()
