#if __name__ == '__main__':
#I am just use to using it. I often use it for testing
#It also help me keep my code clean

def main():
    
    str_manip = input("Please enter a sentence:")

    print(len(str_manip))

    #Isn't it best working practice to make a cope of the string
    manip_new = str_manip.replace(str_manip[-1:], '@')
    print(manip_new)

    print(str_manip[:-4:-1])

    print(f"{str_manip[:3:]}{str_manip[-2::]}")


if __name__ == '__main__':
    main()
