# File: Major.py
# Author: Farming247
# Date: 2/11/2019

def main():
   userMajor = input("Please enter your major:")
   print(userMajor)

   if userMajor == "CMSC" or userMajor == "CMPE":
        print("You need to earn at least a B for CMSC 201 to count.")
   else:
        print("You need to earn at least a C for CMSC 201 to count.")

main()
        
    
