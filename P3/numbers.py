#Funtion to check inputs
def intInput() -> int:    
    while True:
        try:
            n = int(input("input int:"))
            return n
            break #Not needed
        except:
            print("need to be an int")
    

def main():
    #try block and force the string inputs to be ints
    int_first: int = intInput()
    int_second: int = intInput()
    int_third: int = intInput()

    #iterate through the inputted values
    for i in int_first, int_second, int_third:
        print(i)

    #sum takes at most 2 arguments. So I gave the value as a single array
    print(f"The sum of the numbers is: {sum([int_first, int_second, int_third])}")
    print(f"The first nember minus the second number is: {int_first- int_second}")
    print(f"The third nember nultipied by the first number is: {int_third * int_first}")
    print(f"The sum of the numbers devided by the third number is: {sum([int_first, int_second, int_third])/ int_third}")

if __name__ == '__main__':
    main()
