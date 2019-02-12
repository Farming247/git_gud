# File: Cake2.py
# Author: Farming247
# Date: 2/12/2019

def main():
   userCake = input("Did you bake this cake? (bake/buy): ")
   print(userCake)

   if userCake == "buy":
      userStore = input("Where did you but this cake?")
      print(userStore)
      print("Read the label from " + userStore + " to find out the sweetness!")
      print("Regardless of how sweet you like it, enjoy your cake!")

   elif userCake == "bake":
      userSugar = float(input("How many cups of sugar did you use?"))
      print(userSugar)

      if userSugar <=2.49:
         print("You must not like sweet things!")
         print("Regardless of how sweet you like it, enjoy your cake!")

      elif userSugar >= 2.51:
         print("Wow! You must have quite the sweet tooth!")
         print("Regardless of how sweet you like it, enjoy your cake!")
      else: 
         print("That is the perfect amount of sweetness!")
         print("Regardless of how sweet you like it, enjoy your cake!")
    
main()
