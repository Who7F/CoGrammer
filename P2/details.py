def main() -> None:
    #Loop Through a Dictionary to input the data
    #No error checking. 
    user: dir ={'Name': '', 'Age': '', 'House_Number': '', 'Steet_Name': ''}
    for key in user:
        user[key]: str = input(f"Input {key} ")
        
    print(f"This is {user['Name']}. They are {user['Age']} years old lives at house number {user['House_Number']} on {user['Steet_Name']}")

if __name__== '__main__':
    main()
