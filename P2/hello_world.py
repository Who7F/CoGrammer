#I dont like snake_case. I find camelCase or Pascal Case easyer to read
#Types are not enfoced. The below code has a type error. 
def snake_main() -> None:
    snake_name: str = input("Input Name: ")
    print(f"Input Name is {snake_name}")
    
    snake_age: int = input("Input Age: ")
    print(f"Input Age is {snake_age}")
    #print(type(snake_age))
    
    print("Hello World")

if __name__== '__main__':
    snake_main()
