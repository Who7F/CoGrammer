def main() -> None:
    num1: float = 99.23
    num2: int = 23
    num3: int = 150
    string1: str = "100"
    

    num1 = int(num1)
    num2 = float(num2)
    num3 = str(num3)
    string1 = int(string1)
    
    #Had to check num3 type
    #print(type(num3))
    #<class 'str'>
    
    print(num1)
    print(num2)
    print(num3)
    print(string1)

if __name__== '__main__':
    main()
