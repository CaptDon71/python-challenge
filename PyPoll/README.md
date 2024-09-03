**Overview**
This Python script, PyPoll, is designed to analyze election data from a CSV file, tally the total votes, calculate the percentage of votes each candidate received, and determine the winner of the election. The results are printed to the terminal and saved to a text file.

**How It Works**
Reading Data: The script reads election data from a CSV file located in the Resources folder.
Counting Votes: It tallies the total votes for each candidate and stores the counts in a dictionary.
Calculating Results: The script calculates the total number of votes, the percentage of votes each candidate received, and identifies the winner.
Output: The election results are formatted and printed to the terminal, and also saved to a text file in the analysis folder.

**File Paths**
Input File: Resources/election_data.csv
Output File: analysis/election_analysis.txt

**Key Variables**
candidates: A dictionary that stores the vote count for each candidate.
total_votes: Total number of votes cast in the election.
winner: The candidate with the most votes.

**Usage**
Ensure the required input file is placed in the correct directory.
Run the script using Python to generate and save the election results.
