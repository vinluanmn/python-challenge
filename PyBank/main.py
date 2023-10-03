import os
import csv

# find and load the csv file
budget_csv = os.path.join("Resources","budget_data.csv")

# assign variables
months_count = 0
total_profit = 0

# create a list for changes in Profit/Losses
changes = []
#create additional variables
#variable previous_profit is assigned None - absence of a value
previous_profit = None
avg_change = 0
greatincrease = 0 
greatincreasemonth = ""
greatdecrease = 0
greatdecreasemonth = ""

# create reader
with open(budget_csv) as csvfile:
    # read the file
    csvreader = csv.reader(csvfile, delimiter=",")
    # use next to bypass header
    csvHeader = next(csvreader)
    # loop through rows to read the csvFile
    for row in csvreader: 
        # index 0 is the month/each row is an individual month and year
        # add 1 to month_count as reader continues through each row
        months_count += 1
        # index 1 is Profit/Losses
        profitAndlosses = int(row[1])
        # for each row, add proft/loss to total_profit     
        total_profit += profitAndlosses
        
        #create loop to .append change to our list
        if previous_profit is not None:
            change = int(row[1]) - previous_profit
            changes.append(change)
            #create a loop to determine the greatest increase
            if change > greatincrease:
                greatincrease = change
                #assign the month of change to the increase
                greatincreasemonth = row[0]
            #create a loop to determin the greatest decrease
            elif change < greatdecrease: 
                greatdecrease = change
                #assign the month of change to the decrease
                greatdecreasemonth = row[0]

        previous_profit = profitAndlosses
#calculate average of our profit/losses changes in the dataset
avg_change = sum(changes) / len(changes)

#print in terminal output of calculations and findings
print(f"Financial Analysis\n")
print("-------------------------------\n")
print(f"Months: {months_count}\n")
print(f"Total: ${total_profit}\n")
print(f"Average Change: ${avg_change:.2f}\n")
print(f"Greatest Increase in Profits: {greatincreasemonth} (${greatincrease})\n")
print(f"Greatest Decrease in Profits: {greatdecreasemonth} (${greatdecrease})")

#create a text file e in analysis folder with output 
analysis_output = ""
analysis_output += "Financial Analysis\n"
analysis_output += "-------------------------------\n"
analysis_output += (f"Months: {months_count}\n")
analysis_output += (f"Total: ${total_profit}\n")
analysis_output += (f"Average Change: ${avg_change:.2f}\n")
analysis_output += (f"Greatest Increase in Profits: {greatincreasemonth} (${greatincrease})\n")
analysis_output += (f"Greatest Decrease in Profits: {greatdecreasemonth} (${greatdecrease})")

#create path for where file will be written
create_file = os.path.join("analysis", "analysis.txt")
with open(create_file, 'w') as file:
    file.write(analysis_output)

#create conditional statement to verify file was created. 
if os.path.exists(create_file):
    print(f"File has been successfully written as {create_file}")
else:
    print("Error: The file was not created or written.")