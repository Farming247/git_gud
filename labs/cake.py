# File: cake.py
# Author: Farming247
# Date: 2/11/2019

def main():
    userCake = input("Did you bake the cake yourself? (bake/buy):")
    print(userCake)
 
    if userCake == "buy":
    print("Where did you buy it?")
    userStore = input()
    print("Read the labe from " + userStore + " to find out the sweetness!")
  
    userSugar = float(input("How many cups of sugar is in the cake?"))
    print(userSugar)

    elif userCake == "bake":
    userSugar = float(input("How many cups of sugar is in the cake?"))
    print(userSugar)

  
        if userSugar <= 2.49:
            print("You must not like sweet things! " + "Regardless of how sweet you like it, enjoy your cake!")

        elif userSugar >= 2.51:
            print("Wow, you must have quite the sweet tooth! " + "Regardless of how sweet you like it, enjoy your cake!")

        elif userSugar == 2.5:
            print("That is the perfect amount of sweetness. " + "Regardless of how sweet you like it, enjoy your cake!")
   

        else:
   
    main()
