#Funtion to check inputs
def intInput() -> int:    
    while True:
        try:
            n = int(input("input number:"))
            return n
            break #Not needed
        except:
            print("need to be an number")

def main():
    #Using a list to hold inputs
    num_arr: list = []

    #Usin True with a break as I feep it look better
    while True:
        num_arr.append(intInput())
        if num_arr[len(num_arr)-1] == -1:
            break
        
    num_arr.pop()
    print(sum(num_arr)/len(num_arr))


if __name__ == '__main__':
    main()
