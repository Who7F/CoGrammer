def main():
    #Having fill string and using string slice for the patten
    lucky_stars = "*****"
    n = 1
    patten_more = True
    
    while n != 0:
        print(lucky_stars[:n:])

        #Using mattan more to know if its going up or down
        if patten_more == False:
            n -= 1
        elif n == 4:
            n += 1
            patten_more = False
        else:
            n += 1
        

if __name__ == '__main__':
    main()
