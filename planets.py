def weight_on_planets():
   # write your code here
   weight = float(raw_input("What do you weigh on earth?"))
   print "\nOn Mars you would weigh", round(0.38 * weight, 2), "pounds.\nOn Jupiter you would weigh", round(2.34 * weight, 2), "pounds."
   
   
if __name__ == '__main__':
   weight_on_planets()