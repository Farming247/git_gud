# File: Cake2.py
# Author: Farming247
# Date: 2/12/2019

def main():
   userCake = input("Did you bake this cake? (Bake/Buy): ")
   print(userCake)

   if userCake == "Buy":
      userStore = input("Where did you but this cake?")
      print(userStore)
      print("Read the label from " + userStore + " to find out the sweetness!")
      
    
main()
