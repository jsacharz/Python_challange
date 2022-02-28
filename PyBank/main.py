#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:29:02 2022

@author: jsacharz
"""

import csv
import os
# read the file from the same folder
budget_data_csv = os.path.join('budget_data.csv')

# open the file
with open (budget_data_csv, encoding ='utf') as budget_data_csv_file:
    # use comma as the delimiter
    csvreader = csv.reader(budget_data_csv_file, delimiter = ",")
    # jump to next as the first row is the column headers
    header = next(csvreader)
    
    def TableContent(budget_data):
        Date = str(budget_data[0])
        Profit_Loss = int(budget_data[1])
        
    # Create the following variables as integers or strings
    # for the number of months
    
    month_count = 0
    
    # for the total number of Profit_Losses
    
    ProLoss_count= 0
    
    #first starting month which will then move afte rthe 1st iteration to the next one
    
    Prev_month = 'Month start'
    TotChange = 0
    AvergeChange = 0
    GreatIncrease = 'Month start'
    GreatIncreaseDate = str()
    GreatDecrease = 'Month start'
    GreatDecreaseDate = str()
    Monthly_change = 0
    
    
    # print(TotChange) so far works
    
    for row in csvreader:
        # counting all months by adding 1 to every row excpt for the first one
        month_count = month_count +1
        # Counting number of chnages in Profit_Losses in the data, same as above 
        # add 1 to eveyr row
        ProLoss_count = ProLoss_count + int(row[1])
        
        if Prev_month == 'Month start':
            Prev_month =int(row[1])
        else:
            TotChange += int(row[1]) - Prev_month
            Monthly_change = int(row[1]) - Prev_month
            if Monthly_change >= 0:
                if GreatIncrease == 'Month start':
                    GreatIncrease = Monthly_change
                    GreatIncreaseDate = str(row[0])
                elif Monthly_change > GreatIncrease:
                    GreatIncrease = Monthly_change
                    GreatIncreaseDate = str(row[0])
            if Monthly_change <0:
                if GreatDecrease == 'Month start':
                    GreatDecrease = Monthly_change
                    GreatDecreaseDate = str(row[0])
                elif Monthly_change < GreatDecrease:
                    GreatDecrease = Monthly_change
                    GreatDecreaseDate = str(row[0])
                    
            Prev_month = int(row[1])
                
       
        
#------------ Total number of months included in the dataset------------------ 
  
print(month_count)

##-----------The net total number of Profit/Losses over the entire period-----

print(ProLoss_count)

###---------- The avarage of changes between the months, by number of month---
 
# need to -1 becase the changes are between months so number of months = changes_between +1

AvergeChange = AvergeChange + TotChange/(month_count - 1)

print(AvergeChange)


#### ---------The greatest increase in Protifs (date and amount)--------------
print(GreatIncrease)

##### The greatest dcrease in profits (date and amount)
print(GreatDecrease)

#!Notes! below the instrctions:
#Commands to print all the details with dates in the Terminal:
print('Financial Analysis')
print('----------------------------')
print(f" Total Months: {month_count}")
print(f" Total: {ProLoss_count}")
print(f" Average Change: {AvergeChange}")
print(f" Greatest Increase in Profits: {GreatIncreaseDate} (${GreatIncrease})")
print(f" Greatest Decrease in Profits: {GreatDecreaseDate} (${GreatDecrease})")
print('----------------------------')

#Commands to also save it saved file.txt in a folder called 'analysis' , how to do it:
#find here: https://www.kite.com/python/answers/how-to-write-a-file-to-a-specific-directory-in-python
save_path = 'analysis'
file_name = "Bank.txt"
completeName = os. path. join(save_path, file_name)
print(completeName)
file1 = open(completeName, "w")
# how to start with a new line find here: https://www.kite.com/python/answers/how-to-write-a-string-to-a-file-on-a-new-line-every-time-in-python
file1.write('Financial Analysis\n')
file1.write('----------------------------\n')
file1.write(f" Total Months: {month_count}\n")
file1.write(f" Total: {ProLoss_count}\n")
file1.write(f" Average Change: {AvergeChange}\n")
file1.write(f" Greatest Increase in Profits: {GreatIncreaseDate} (${GreatIncrease})\n")
file1.write(f" Greatest Decrease in Profits: {GreatDecreaseDate} (${GreatDecrease})\n")

file1 = open(completeName)
file1.close()


