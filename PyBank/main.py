import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

months = 0
total = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    months += 1
    total += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        months += 1

        total = total + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average"
    avg_change = sum(profits)/len(profits)
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


output = open("Text.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(months)}")
line4 = str(f"Total: ${str(total)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))