#import regex

#Emall Class. Arguments email_address, subject_line, email_content
class Email:
    def __init__(self, email_address: str, subject_line: str, email_content: str):
        self.email_address: str = email_address
        self.subject_line: str = subject_line
        self.email_content: str = email_content
        self.has_been_read: bool = False

    def mark_as_read(self) -> None:
        self.has_been_read = True
            

def populate_inbox(inbox, *args) -> None:

    #Could get an answer about how the data
    #Fine. I'll make it robust
    if len(args) == 3:
        email_address: str = args[0]
        subject_line: str = args[1]
        email_content: str = args[2]
    elif len(args) == 0:
        email_address: str = input("Please enter email: ")
        subject_line: str = input("Please enter subject: ")
        email_content: str = input("Please enter content: ")
    else:
        email_address: str = "error@error"
        subject_line: str = "error"
        email_content: str = "error: populate_inbox given incorrect number of arguments"
        print("incorrect number of arguments")
    
    #obj = Email(email_address, subject_line, email_content)
    #return obj
    '''
    populate_inbox() - a function which creates an email object
    with the email address, subject line, and contents,
    and stores it in the inbox list
    '''
    #indox is a reference so no need to return reviewed
    inbox.append(Email(email_address, subject_line, email_content))

#Prints emails
def list_emails(inbox) -> None:
    for count, i in enumerate(inbox):
        print(count, i.subject_line)
    
#reads a single email
def read_email(email) -> None:
    print(f"Email: {email.email_address}\n\nSubject: {email.subject_line}\n\nContent: {email.email_content}\n")
    #side effect
    email.mark_as_read()
    

def intInput(text, lower_limit, upper_limit) -> int:    
    while True:
        try:
            n = int(input(text))
            if n >= lower_limit and n <= upper_limit:
                return n
            print(f"Number must be in range between {lower_limit} and {upper_limit}.")
        except:
            print("Need to be an number")



def main():
    populate_email =[
        ["mary@email", "Mary", "Mary had a little lamb Her father shot it dead. Now it goes to school with her, between two chunks of bread."],
        ["franky@email","Franky","Jack and Jill Went up the hill to have some hanky panky. Silly Jill forgot her pill And now there's little Franky."],
        ["hubbard@email","Hubbard","Old Mother Hubbard Went to the cupboard to fetch her poor dog a bone. When she bent over Rover took over, And gave her a bone of his own."]]
    
    inbox: list = []
    for i in populate_email:
        populate_inbox(inbox, i[0], i[1], i[2])

    list_emails(inbox)
    while True:
        menu = intInput("\n1. Read an email\n2. View unread emails\n3. Quit application: ", 1, 3)
        print("")
        if menu == 1:
            email = intInput("Select Email by number: ", 0, len(inbox)-1)
            print("")
            read_email(inbox[email])
            print(f"\nEmail from {inbox[email].email_address} marked as read.\n")
        elif menu == 2:
            list_emails(inbox)
        elif menu == 3:
            break
        else:
            print("Error: Out of bounds")


if __name__=='__main__':
    main()
