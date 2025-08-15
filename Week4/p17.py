# p17.py
# Han Rockhill
# python version 3.12.2
# 02/20/2024 - 02/21/2024
# Suppose that the tuition for a university is $10,000 this year and increases 5% every year.
# Write a program that computes the tuition in ten years and displays a table of the years and tuition costs.
# A loop must be used.

# print the header
print('Tuition Costs in the State of California')
print('========================================')
# start the first year with the original price  (year 1 price 10k)
price = 10000 	# amount of dollars starting at 10k
for year in range(1,11,1): 	# defines the start, range , and step
	# reserve space for school year and space for price to be displayed in a table format
	print ("School Year %3i" % year, "... Tuition Cost = %5.2f" % price)
	# increase YoY price by 5%
	price = price + price * 0.05
'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Desktop/p17.py ======================
Tuition Costs in the State of California
========================================
School Year   1 ... Tuition Cost = 10000.00
School Year   2 ... Tuition Cost = 10500.00
School Year   3 ... Tuition Cost = 11025.00
School Year   4 ... Tuition Cost = 11576.25
School Year   5 ... Tuition Cost = 12155.06
School Year   6 ... Tuition Cost = 12762.82
School Year   7 ... Tuition Cost = 13400.96
School Year   8 ... Tuition Cost = 14071.00
School Year   9 ... Tuition Cost = 14774.55
School Year  10 ... Tuition Cost = 15513.28

'''