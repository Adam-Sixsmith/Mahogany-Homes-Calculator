import math

#####################################################################################################################################################
#         This calculator uses the total xp you have currently, takes the total xp you need to get to and works out how much xp you have left       #
#             until you've got to the level you're needing and will also work out the total contracts, rounded to the next whole number.            #
#                   This calculator assumes you already have the carpenters outfit based on the average xp per contract                             #
#                                                being 4,445 xp per contract                                                                        #
#####################################################################################################################################################


def XpLeft():
    global total_xp_left
    
    current_xp = int(input("What is your current XP? "))
    
    # Having to use this as the target XP due to not knowing the proper way to work out the XP based
    # on what level they want yet without having a bunch of code with each level and it's xp required
    target_xp = int(input("What is the target XP you're looking to get? (You can get this from Runelites Cacluator)"))
    
    total_xp_left = target_xp - current_xp
    
    xp_left_to_get = f"You have {target_xp - current_xp} xp left to get to your level"
    
    print(xp_left_to_get)
    
    
def contracts():
    average_xp_per_contract = 4445
    
    total_contracts = total_xp_left / average_xp_per_contract
    
    rounded_number_of_contracts = math.ceil(total_contracts)
    
    print(f"You have roughly {rounded_number_of_contracts} contracts left until your level")
    
def planks_needed():
    average_plank_xp = 344
    
    planks_user_needs = total_xp_left / average_plank_xp
    
    rounded_number_of_planks = math.ceil(planks_user_needs)
    
    while True:
        plank_number_question = input("Would you like to know how many planks on average you would need? (yes/no) ")
        
        if plank_number_question == "yes":
            print(f"You would need on average {rounded_number_of_planks} planks")
            break
        elif plank_number_question == "no":
            print("Thanks for using the calculator")
            break
        else:
            print("Answer not recognised, please only input yes or no")
            
    
    
def main():
    XpLeft()
    contracts()
    planks_needed()
    
    
main()