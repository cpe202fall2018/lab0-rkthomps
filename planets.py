#
# Robert Kyle Thompson
# Username: rkthomps
# 9/24/18
#
# Lab 0
# Section
# Purpose: Create a program that takes in weight on earth and outputs weight on Mars and Jupiter


#This function prints a persons weight on Mars and Jupiter given their weight on earth
def weight_on_planets():
   # weight is the weight in pounds of the user on earth
   weight = float(input("What do you weigh on earth? "))
   #print("\nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds.")
   print ("\nOn Mars you would weigh",weight * .38,"pounds.\nOn Jupiter you would weigh",weight * 2.34,"pounds.")

   
if __name__ == '__main__':
   weight_on_planets()