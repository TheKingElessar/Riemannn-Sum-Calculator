lower_bound = float(input("Lower bound: "))
upper_bound = float(input("Upper bound: "))
divisions = input("Divisions? (leave blank for full printout): ")
print("\n")

def function(x):

    #########################################
    # Change the line below to the function
    #########################################
    return 10 - x**2


if input == "":

    divisions = 1
    breaknext = False
    while True:
        division_size = (upper_bound - lower_bound) / divisions

        total_right = 0
        total_left = 0
        for i in range(1, divisions + 1):
            total_right += function(lower_bound + (division_size * i)) * division_size
            total_left += function((division_size * i) - division_size) * division_size

        print("DIVISIONS: " + str(divisions))
        print("Right sum: " + str(total_right))
        print("Left sum: " + str(total_left))
        print("\n")
        
        if breaknext:
            break
        
        divisions = divisions * 2
        if divisions >= 100000:
            breaknext = True
            
else:
    divisions = int(divisions)
    division_size = (upper_bound - lower_bound) / divisions

    total_right = 0
    total_left = 0
    for i in range(1, divisions + 1):
        total_right += function(lower_bound + (division_size * i)) * division_size
        total_left += function((division_size * i) - division_size) * division_size

    print("DIVISIONS: " + str(divisions))
    print("Right sum: " + str(total_right))
    print("Left sum: " + str(total_left))
    print("\n")
    
