# 49.py
# Han Rockhill
# python 3.12.2
# 04/21/2024
# Write a python program to calculate the average for each month of every year, using the functions below:
#Function Calls:
# Calculate the averages for every month, store them in a list, and then show the list to the user:
#
# function name: def get_data_list
# # parameter:     FILE_NAME  - the file's name you saved for the stock's prices
# # description:   reads a csv file, splits it by lines and puts it in a list
# # returns:       a list of lines, each element on the list is a line in the csv file
def get_data_list(FILE_NAME):
    # # parameter:     FILE_NAME  - the file's name you saved for the stock's prices
    # # description:   reads a csv file, splits it by lines and puts it in a list
    theFile = open(FILE_NAME + ".csv", 'r')
    data_list = theFile.read().splitlines()
    theFile.close()
    # # returns:       a list of lines, each element on the list is a line in the csv file
    return data_list


# # function name: get_monthly_averages
# # parameter:     data_list  - the list that you will process
# # description:   calculate monthly averages
# # returns:       a list with sub-lists containing months, years, averages
# def get_monthly_averages (data_list):
#     return monthly_average_list # a list of lists [ [mm,yyyy,avg],..., [mm,yyyy,avg] ]
def get_monthly_averages (data_list):
    listOfLines = data_list
    # show me oneline only
    aLine = listOfLines[1]
    # split each line by commas
    lineData = aLine.split(',')
    # shows list of strings ['2004-10-13', '143.32', '143.55', '140.08'...]
    # pull out the date only
    dateValue = lineData[0]
    dateData = dateValue.split('-')
    year = dateData[0]
    month = dateData[1]
    oldMonth = month
    sum =0
    count = 0
    dayCount = 0
    avgList = []
    # print('sum=', sum, 'month=', month, 'year=', year)
    for i in range(1, len(listOfLines), 1):
        # show me oneline only
        aLine = listOfLines[i]
        # split each line by commas
        lineData = aLine.split(',')
        # shows list of strings ['2004-10-13', '143.32', '143.55', '140.08'...]
        # pull out the date only
        dateValue = lineData[0]
        dateData = dateValue.split('-')
        year = dateData[0]
        month = dateData[1]
        # pull out the Close Avg (same as Avg)
        aValue = lineData[-1]
        # show me the final list we will use
        # lineList = [month, year, avgValue]
        if month == oldMonth:
            sum += float(aValue)
            dayCount += 1
            # format it so I always get the trailing zeros
            avg = '{:.2f}'.format(sum / dayCount)
            #print('sum=', sum, 'count=', dayCount, 'avg=', avg)
        if month != oldMonth or i == 1030:
            #print(' mm=', oldMonth, 'yyyy=', year, ' avg=', avg)
            monthly_average_list = [oldMonth, year, avg]
            avgList.append(monthly_average_list)

            #print ('monthly_average_list[%2i]' %malCount, '  =  ', monthly_average_list)
            # reset everything
            sum = float(aValue)
            dayCount = 1
            oldMonth = month
    return avgList


# # function name: print_info
# # parameter:     monthly_average_list  - the list that you will process
# # description:   print the monthly averages of Google stock
# # returns:       None
def print_info (avgList):
    malCount = 0
    print('monthly_average_list[%2i]' % malCount, ' = ', ['Month', 'Year', 'Average'])
    malCount = 1
    for data in avgList:
        if malCount == [0]:
            print('monthly_average_list[%2i]' % malCount, ' = ', ['Month', 'Year', 'Average'])
        else:
            print('monthly_average_list[%2i]  =  %s' % (malCount, data))
            malCount += 1
    
# call function to get the data list.
# create list from stock.csv
data_list = get_data_list('stock')

# call function to return a list with monthly averages
# format the list to get the 'Month', 'Year', 'Average'
monthly_average_list = get_monthly_averages(data_list)

# call to show monthly_average_list as shown in the sample run below
# show the list broken down by month
    # output should look like
    # monthly_average_list[ 0]  =  ['Month', 'Year', 'Average']
    # monthly_average_list[ 1]  =  ['09', '2008', '437.70']
    # monthly_average_list[ 2]  =  ['08', '2008', '485.91']
    # monthly_average_list[ 3]  =  ['07', '2008', '510.03']
print_info (monthly_average_list)

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: /Users/42o/PycharmProjects/Week11/49.py ===============
monthly_average_list[ 0]  =  ['Month', 'Year', 'Average']
monthly_average_list[ 1]  =  ['09', '2008', '437.70']
monthly_average_list[ 2]  =  ['08', '2008', '485.91']
monthly_average_list[ 3]  =  ['07', '2008', '510.03']
monthly_average_list[ 4]  =  ['06', '2008', '556.32']
monthly_average_list[ 5]  =  ['05', '2008', '575.92']
monthly_average_list[ 6]  =  ['04', '2008', '497.58']
monthly_average_list[ 7]  =  ['03', '2008', '440.33']
monthly_average_list[ 8]  =  ['02', '2008', '503.80']
monthly_average_list[ 9]  =  ['01', '2007', '611.81']
monthly_average_list[10]  =  ['12', '2007', '695.40']
monthly_average_list[11]  =  ['11', '2007', '676.37']
monthly_average_list[12]  =  ['10', '2007', '635.39']
monthly_average_list[13]  =  ['09', '2007', '540.43']
monthly_average_list[14]  =  ['08', '2007', '509.83']
monthly_average_list[15]  =  ['07', '2007', '532.48']
monthly_average_list[16]  =  ['06', '2007', '515.02']
monthly_average_list[17]  =  ['05', '2007', '473.01']
monthly_average_list[18]  =  ['04', '2007', '472.50']
monthly_average_list[19]  =  ['03', '2007', '452.91']
monthly_average_list[20]  =  ['02', '2007', '467.22']
monthly_average_list[21]  =  ['01', '2006', '490.58']
monthly_average_list[22]  =  ['12', '2006', '473.50']
monthly_average_list[23]  =  ['11', '2006', '485.63']
monthly_average_list[24]  =  ['10', '2006', '440.53']
monthly_average_list[25]  =  ['09', '2006', '397.06']
monthly_average_list[26]  =  ['08', '2006', '377.09']
monthly_average_list[27]  =  ['07', '2006', '403.53']
monthly_average_list[28]  =  ['06', '2006', '393.59']
monthly_average_list[29]  =  ['05', '2006', '383.80']
monthly_average_list[30]  =  ['04', '2006', '413.78']
monthly_average_list[31]  =  ['03', '2006', '358.87']
monthly_average_list[32]  =  ['02', '2006', '370.00']
monthly_average_list[33]  =  ['01', '2005', '445.71']
monthly_average_list[34]  =  ['12', '2005', '418.95']
monthly_average_list[35]  =  ['11', '2005', '399.14']
monthly_average_list[36]  =  ['10', '2005', '322.47']
monthly_average_list[37]  =  ['09', '2005', '304.24']
monthly_average_list[38]  =  ['08', '2005', '286.92']
monthly_average_list[39]  =  ['07', '2005', '298.21']
monthly_average_list[40]  =  ['06', '2005', '287.55']
monthly_average_list[41]  =  ['05', '2005', '239.71']
monthly_average_list[42]  =  ['04', '2005', '199.21']
monthly_average_list[43]  =  ['03', '2005', '181.16']
monthly_average_list[44]  =  ['02', '2005', '195.01']
monthly_average_list[45]  =  ['01', '2004', '192.85']
monthly_average_list[46]  =  ['12', '2004', '181.77']
monthly_average_list[47]  =  ['11', '2004', '177.50']
monthly_average_list[48]  =  ['10', '2004', '153.23']
monthly_average_list[49]  =  ['09', '2004', '113.23']
monthly_average_list[50]  =  ['08', '2004', '105.26']
'''