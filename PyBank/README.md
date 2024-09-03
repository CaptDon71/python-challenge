**Overview**
The PyBank script is designed to analyze financial records from a CSV file. It computes the total number of months included in the dataset, the net total amount of profit/losses over the entire period, the average change in profit/losses between months, and identifies both the greatest increase and greatest decrease in profits during the analysis period. The results are displayed in the terminal and saved to a text file.

**How It Works**
**Reading Data:** The script reads financial data from a CSV file located in the Resources folder.

**Processing Data:**
It converts profit/loss values to integers.
Calculates the total number of months and the net total amount of profit/losses.
Computes the monthly changes in profit/losses and calculates the average change.
Identifies the greatest increase and decrease in profits, along with the corresponding dates.

**Output:** The script formats the analysis results and prints them to the terminal, and saves the results to a text file in the analysis folder.
File Paths
Input File: Resources/budget_data.csv
Output File: analysis/budget_analysis.txt

**Key Variables**
data: A list that stores date and profit/loss information from the CSV file.
changes: A list that stores the changes in profit/losses between months.
total_months: The total number of months included in the dataset.
total_net: The net total amount of profit/losses over the entire period.
greatest_increase: The greatest increase in profits and the corresponding date.
greatest_decrease: The greatest decrease in profits and the corresponding date.
