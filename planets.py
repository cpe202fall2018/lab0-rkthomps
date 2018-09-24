#
# Robert Kyle Thompson
# Username: rkthomps
# 9/24/18
#
# Lab 0
# Section
# Purpose: Create a program that takes in weight on earth and outputs weight on Mars and Jupiter

def weight_on_planets():
   # write your code here
   weight = float(raw_input("What do you weigh on earth?"))
   print "\nOn Mars you would weigh", round(0.38 * weight, 2), "pounds.\nOn Jupiter you would weigh", round(2.34 * weight, 2), "pounds."
   
   
if __name__ == '__main__':
   weight_on_planets()