def intInput(text: str) -> int:
    """
    Function to take integer input from the user.

    Args:
    - text (str): Prompt message for the user.

    Returns:
    - int: User input as integer.
    """
    while True:
        try:
            n = int(input(text))
            return n
        except:
            print("Needs to be a number")

def hotel_cost(num_nights: int, HOTEL_COST: float) -> float:
    """
    Calculate the total hotel cost.

    Args:
    - num_nights (int): Number of nights stayed.
    - HOTEL_COST (float): Cost per night of the hotel.

    Returns:
    - float: Total cost of the hotel stay.
    """
    return num_nights * HOTEL_COST

def plane_cost(city_flight: str) -> float:
    """
    Calculate the cost of the plane ticket based on the destination city.

    Args:
    - city_flight (str): Destination city.

    Returns:
    - float: Cost of the plane ticket.
    """
    # Using a dictionary might be more efficient here instead of multiple if-elif statements
    if city_flight == "London":
        return 150.00
    elif city_flight == "Paris":
        return 140.00
    elif city_flight == "Cape Town":
        return 210.00
    elif city_flight == "Hong Kong":  
        return 3040.00
    elif city_flight == "Budapest":
        return 260.00
    else:
        print("Destination not found")  
    return -1

def car_rental(rental_days: int, RENTAL_COST: float) -> float:
    """
    Calculate the total cost of car rental.

    Args:
    - rental_days (int): Number of days for car rental.
    - RENTAL_COST (float): Cost per day of car rental.

    Returns:
    - float: Total cost of car rental.
    """
    return rental_days * RENTAL_COST

def holiday_cont(hotel_cost, plane_cost, car_rental) -> int:
    """
    Calculate the total cost of the holiday.

    Args:
    - hotel_cost (float): Cost of hotel stay.
    - plane_cost (float): Cost of plane ticket.
    - car_rental (float): Cost of car rental.

    Returns:
    - int: Total cost of the holiday.
    """
    return hotel_cost + plane_cost + car_rental

def main():
    #Fixed verbles
    RENTAL_COST: float = 5.50
    HOTEL_COST: float = 125.00
    FLIGHT_CITIES: list = ["London", "Paris", "Cape Town", "Hong Kong", "Budapest"] 
    
    city_flight: str = ""
    
    # Loop to prompt user for valid destination selection
    while True:
        for i in range(len(FLIGHT_CITIES)):
            print(f"Enter {i+1} for destination {FLIGHT_CITIES[i]}")
        n = intInput("Enter: ")
        if n > 0 and n <= len(FLIGHT_CITIES):
            city_flight = FLIGHT_CITIES[n-1]
            break
        print('Number outside of range\n')

    num_nights: int = intInput(f"How many nights are you staying at destination {city_flight} at £{'{:.2f}'.format(HOTEL_COST)} per night: ")
    rental_days: int = intInput(f"How many days will you be hiring a car at £{'{:.2f}'.format(RENTAL_COST)}: ")
    
    # Calculate and print individual costs
    print(f"Hotel cost: £{'{:.2f}'.format(hotel_cost(num_nights, HOTEL_COST))}")
    print(f"Plane cost: £{'{:.2f}'.format(plane_cost(city_flight))}")
    print(f"Car rental cost: £{'{:.2f}'.format(car_rental(rental_days, RENTAL_COST))}")
    
    # Calculate and print total holiday cost
    total_cost = holiday_cont(hotel_cost(num_nights, HOTEL_COST), plane_cost(city_flight), car_rental(rental_days, RENTAL_COST))
    print(f"Total holiday cost: £{'{:.2f}'.format(total_cost)}")

if __name__=='__main__':
    main()
