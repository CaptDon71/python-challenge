#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PyBank Challenge
import csv
import os


# In[2]:


# Detremine files to read and write 
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_write = os.path.join("analysis", "budget_analysis.txt")


# In[5]:


# declare variables
data = []
changes = []
total_months = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
total_net = 0


# In[6]:


# read csv and convert into lists of dictionaries
with open(file_to_load) as finanical_data:
    reader = csv.reader(finanical_data)
    # read header
    header = next(reader)
    # Create a list of tuples [0], [1] showing (date, profit/losses)
    for row in reader:
        data.append(row)



# In[7]:


# Convert Profit/Losses values to integers
for record in data:
    record[1] = int(record[1])

# Calculate the total number of months
total_months = len(data)

# Calculate the total amount of "Profit/Losses"
total_net = sum(record[1] for record in data)

# Calculate the changes in "Profit/Losses"

for i in range(1, total_months):
    change = data[i][1] - data[i - 1][1]
    changes.append(change)

# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase) + 1  # offset to compare changes
greatest_increase_date = data[greatest_increase_index][0]

# Find the greatest decrease in profits
greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease) + 1  # offset to compare changes
greatest_decrease_date = data[greatest_decrease_index][0]


# In[8]:


# Create a reuseable multiline string variable
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Profit/Losses: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the results to terminal
print(results)

# Export the results to a text file
with open(file_to_write, 'w') as file:
    file.write(results)

