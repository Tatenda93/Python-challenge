# Dependencies
import os
import csv

# Defining the file path
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Define variables
total_months = 0
total_profit_loss = 0
changes = []
dates = []
previous_profit = None

# Open and read CSV file
with open(file_to_load, mode='r') as financial_data:
    csv_reader = csv.reader(financial_data)
    header = next(csv_reader)  # Skip header row

    for row in csv_reader:
        total_months += 1
        date, profit = row
        profit = int(profit)  # Convert profit to integer
        total_profit_loss += profit
        dates.append(date)

        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)

        previous_profit = profit

# Determine the greatest increase and decrease in profits
if changes:
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase) + 1]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]
else:
    greatest_increase = 0
    greatest_increase_date = "N/A"
    greatest_decrease = 0
    greatest_decrease_date = "N/A"

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Save the results to a text file
with open(file_to_output, mode='w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
