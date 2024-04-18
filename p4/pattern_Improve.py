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

    '''
    Code Efficiency. Okay my code is ugly
    I was given code example below 
    '''
    start = 1
    end = 10
    width = 5

    asterisk_number = (row_number if row_number <= width else end - row_number for row_number in range(start, end))
    
    for num in asterisk_number:
        print("^" * num)

    '''
    Snazzy.
    below would be my improvement 
    '''

    for i in range(1, 10):
        print('|'*i) if i <= width else print('|'*(10-i))

    '''
    Simple. But is that the best use of python.
    Of course not. It's all about the flex
    '''
    
    SexyMap:dir = {'up':lambda n : n,
                'down':lambda n : end - n}

    a_range:range = range(start, end)
    
    black_magic = ('up' if row_number <= width else 'down' for row_number in a_range)
    
    for i in a_range:
        print(SexyMap.get(next(black_magic), 'error')(i) * '-')
 
    '''
    Na. I just want to try out lambda in a dictionary 
    '''
    
if __name__ == '__main__':
    main()
