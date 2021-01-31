# Import
import os
import csv

# CSV file path
csv_file = os.path.join("Resources", "PyBank.csv")
 
# Open/read CSV file
with open(csv_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    # Skip header row
    csv_header = next(csvfile)

    total_months = []
    profit_loss = []
    change = []

    # Loop through rows
    for row in csvreader: 

        # The total number of months/profit_loss included in the dataset
        total_months.append(row[0])
        profit_loss.append(int(row[1]))

    # Loop through row to get monthly change in profits
    for i in range(len(profit_loss)-1):
        
        # The net total amount of "Profit/Losses" over the entire period
        change.append(profit_loss[i+1]-profit_loss[i])
        
# The greatest increase/decrease in profits amount over the entire period
greatest_increase_value = max(change)
greatest_decrease_value = min(change)

# The greatest increase/decrease in profits date over the entire period
greatest_increase_month = change.index(max(change)) + 1
greatest_decrease_month = change.index(min(change)) + 1 

# print the analysis to the terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")

# export a text file with the results
output_file = "Analysis/analysis_file.txt"

with open(output_file,"w") as file:

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(profit_loss)}\n")
    file.write(f"Average Change: {round(sum(change)/len(change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")
