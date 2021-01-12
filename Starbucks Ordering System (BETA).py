# List of Global Variables 
DRINK1_NAME = "Latte"
DRINK1_COST = 2.99

DRINK2_NAME = "Cappuccino"
DRINK2_COST = 3.99

DRINK3_NAME = "Americano"
DRINK3_COST = 4.49

DRINK4_NAME = "Espresso"
DRINK4_COST = 5.95


SIZE1_NAME = "small"
SIZE1_COST = -2.0

SIZE2_NAME = "medium"
SIZE2_COST = 0.0

SIZE3_NAME = "large"
SIZE3_COST = +2.0

SIZE4_NAME = "gigantore"
SIZE4_COST = +100.0


TOPPING1_NAME = "whipped cream"
TOPPING1_COST = 0.0

TOPPING2_NAME = "white chocolate"
TOPPING2_COST = 1.0

TOPPING3_NAME = "marshmallow"
TOPPING3_COST = 1.0

TOPPING4_NAME = "nutmeg"
TOPPING4_COST = 1.0





def initial_question (question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    """
    Input Arguments: (str, str, float, str, float, str, float, str, float)
    
    Description: Prints posed question and menu of choices, depending on posed question, and takes the user's choice for smoothie, size,
    and topping as input and returns the chosen option
    

    """
    
    
    print(posed_question)
    print ("1.)\t$", cost1, "\t", option1, "\n2.)\t$", cost2, "\t", option2, "\n3.)\t$", cost3, "\t", option3, "\n4.)\t$", cost4, "\t", option4) #Prints menu depending on which input arguments are used
    
    your_choice = input("Your choice (1-4): ") #assigns your_choice depending on input

    if your_choice == "1":
        print (option1, ' has been selected.')
        return option1
        
    elif your_choice == "2":
        print (option2, ' has been selected.')
        return option2
       
    elif your_choice == "3":
        print (option3, ' has been selected.')
        return option3
                   
    elif your_choice == "4":
        print (option4, ' has been selected.')
        return option4
       
    else:
        return print("Invalid Input, please try again") #Returns function if invalid input is used



def subtotal_calculator (drink_type, drink_size, topping):
    """
    Input Arguments: calculate_subtotal (str, str, str)
    
   
    """
    
    if drink_type == DRINK_NAME: #assigns cost to type depending on selection given by user 
        drink_type = float(DRINK1_COST)
    
    elif drink_type == DRINK2_NAME:
        drink_type = float(DRINK2_COST)
        
    elif drink_type == DRINK3_NAME:
        drink_type = float(DRINK3_COST)
        
    elif drink_type == DRINK4_NAME:
        drink_type = float(DRINK4_COST)

    
    
    if drink_size == SIZE1_NAME: #assigns cost to size depending on selection given by user 
        drink_size = float(SIZE1_COST)
        
    elif drink_size == SIZE2_NAME:
        drink_size = float(SIZE2_COST)
    
    elif drink_size == SIZE3_NAME:
        drink_size = float(SIZE3_COST)
        
    elif drink_size == SIZE4_NAME:
        drink_size = float(SIZE4_COST)
        
        
        
    if topping == TOPPING1_NAME: #assigns cost to topping depending on selection given by user 
        topping = float(TOPPING1_COST)
        
    elif topping == TOPPING2_NAME:
        topping = float(TOPPING2_COST)
        
    elif topping == TOPPING3_NAME:
        topping = float(TOPPING3_COST)
        
    elif topping == TOPPING4_NAME:
        topping = float(TOPPING4_COST)
        
    
    drink_price = drink_type + drink_size + topping #calculates subtotal of drink by adding costs of type, size, and topping
   
    
    return drink_price 





   
