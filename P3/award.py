def qualifyingCriteria(swimming, cycling, running)-> str:
    if sum([swimming, cycling, running]) <= 100:
        return "Provincial colours"
    elif sum([swimming, cycling, running]) <= 105:
        return "Provincial half colours"
    elif sum([swimming, cycling, running]) <= 110:
        return "Provincial scroll"
    else:
        return "No award"

#Funtion to check inputs
def intInput(text) -> int:    
    while True:
        try:
            n = int(input(f"Enter time in minutes for {text}: "))
            return n
            break #Not needed
        except:
            print("need to be an int")

def main():
    #I haven't been given a data type

    #testing
    print("Triathlon events")
    swimming: int = intInput("swimming")
    cycling: int = intInput("cycling")
    running: int = intInput("running")
    print(qualifyingCriteria(swimming, cycling, running))
    


if __name__ == '__main__':
    main()
