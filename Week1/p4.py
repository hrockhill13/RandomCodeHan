# p4.py
# Han Rockhill
# 02/01/2024
# Python 3.12.1
# Print a large C using input characters
let = input("Choose a letter to draw with: ")
print("****************************")   # Border of *****
print("")                                           # blank space
print("          %s%s%s          " % (let, let, let))   # start of letters top
print("        %s     %s           " % (let, let))
print("       %s       %s          " % (let, let))
print("      %s                   " % let)
print("      %s                   " % let)
print("      %s                   " % let)
print("      %s                   " % let)
print("       %s       %s          " % (let, let))
print("        %s     %s           " % (let, let))
print("          %s%s%s             " % (let, let, let))   # end of letter bottom
print("")                                           # another blank space
print("****************************")   # close of border ****
print("")
'''
Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: /Users/42o/Documents/p4.py ===================
Choose a letter to draw with: #
****************************

          ###          
        #     #           
       #       #          
      #                   
      #                   
      #                   
      #                   
       #       #          
        #     #           
          ###             

****************************

'''