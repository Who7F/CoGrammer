def main():
    #Input file 
    INPUT_FILE = "DOB.txt"

    #I just think it looks cleaner with a with and no close
    with open(INPUT_FILE, 'r') as f:
        my_file = f.read()
        
    #Prints out names
    print("\nName")
    for line in list(my_file.splitlines()):
        print(' '.join(list(line.split())[:2]))
        
    #Prints out birthdays
    print("\nBirthday")
    for line in list(my_file.splitlines()):
        print(' '.join(list(line.split())[-3:]))


if __name__=='__main__':
    main()
