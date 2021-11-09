def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    if distance_to_pump > mpg * fuel_left:
        fuel = False
        print("You need to fuel up earlier!")
    else:
        fuel = True
        print("You will get to destination!")
    return fuel

