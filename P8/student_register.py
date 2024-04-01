# Function to check inputs and ensure they are integers greater than 0.
def intInput(text) -> int:
    """
    Takes user input and ensures it is a positive integer.

    Args:
    - text (str): Prompt message for user input.

    Returns:
    - int: Valid positive integer input by the user.
    """
    while True:
        try:
            n = int(input(text))
            if n > 0:
                return n
            print("Number must be grater then 0")
        except:
            print("Need to be an number")


def main():
    # Asking for number of students
    students_num = intInput("Please input the number of students: ")
    
    # Open and input student IDs into rag_form.txt 
    with open("rag_form.txt", 'w') as file:
        for _ in range(students_num):
            id_num = input("Input student ID: ")
            file.write(f"{id_num}\n..................\n") # Write each student ID followed by a line of dots for separation
        

if __name__=='__main__':
    main()
